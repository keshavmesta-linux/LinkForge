
import secrets
import sqlite3
import string
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, HttpUrl

# ---------- APP CONFIGURATION ----------

app = FastAPI(
    title="LinkForge API",
    description="A personal URL shortening service",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "linkforge.db"
BASE_URL = "http://127.0.0.1:8000"

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return (BASE_DIR / "templates" / "index.html").read_text(encoding="utf-8")

# ---------- DATABASE ----------

def initialize_database():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short_code TEXT UNIQUE NOT NULL,
                target_url TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0
            )
        """)
        conn.commit()


initialize_database()

# ---------- REQUEST MODEL ----------

class ShortenRequest(BaseModel):
    url: HttpUrl

# ---------- SHORT CODE GENERATOR ----------

def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(
        secrets.choice(characters) for _ in range(length)
    )

# ---------- CREATE SHORT URL ----------

@app.post("/api/shorten", status_code=201)
def shorten_url(request: ShortenRequest):
    target_url = str(request.url)

    with closing(sqlite3.connect(DB_PATH)) as conn:
        for _ in range(10):
            code = generate_short_code()

            try:
                conn.execute(
                    """
                    INSERT INTO links (short_code, target_url)
                    VALUES (?, ?)
                    """,
                    (code, target_url),
                )
                conn.commit()

                return {
                    "short_code": code,
                    "short_url": f"{BASE_URL}/{code}",
                    "target_url": target_url,
                }

            except sqlite3.IntegrityError:
                # A generated code already exists. Try another.
                continue

    raise HTTPException(
        status_code=500,
        detail="Could not generate a unique short code",
    )

# ---------- REDIRECT TO ORIGINAL URL ----------

@app.get("/{short_code}")
def redirect_to_target(short_code: str):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        row = conn.execute(
            """
            SELECT target_url
            FROM links
            WHERE short_code = ?
            """,
            (short_code,),
        ).fetchone()

        if row is None:
            raise HTTPException(
                status_code=404,
                detail="Short URL not found",
            )

        target_url = row[0]

        conn.execute(
            """
            UPDATE links
            SET clicks = clicks + 1
            WHERE short_code = ?
            """,
            (short_code,),
        )
        conn.commit()

    return RedirectResponse(
        url=target_url,
        status_code=307,
    )



@app.get("/api/links")
def list_links():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT short_code, target_url, created_at, clicks
            FROM links
            ORDER BY id DESC
        """).fetchall()

    return [
        {
            "short_code": row["short_code"],
            "short_url": f"{BASE_URL}/{row['short_code']}",
            "target_url": row["target_url"],
            "created_at": row["created_at"],
            "clicks": row["clicks"],
        }
        for row in rows
    ]
