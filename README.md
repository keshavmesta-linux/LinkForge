LinkForge 🔗

A lightweight URL shortener built with Python, FastAPI, and SQLite.

LinkForge turns long URLs into short links and provides a web interface, link history, click statistics, and a command-line interface.

Features

- Shorten URLs with randomly generated short codes
- Redirect short links to their original destinations
- Track link clicks
- View saved links and statistics
- Responsive web interface built with HTML, CSS, and JavaScript
- Command-line interface (CLI)
- SQLite database for persistent storage
- API endpoints powered by FastAPI

Tech Stack

- Backend: Python, FastAPI
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- CLI: Python

Project Structure

linkforge/
├── cli/
│   └── banner.py
├── static/
│   ├── app.js
│   └── style.css
├── templates/
│   └── index.html
├── main.py
├── st.py
├── requirements.txt
├── .gitignore
└── README.md

Run Locally

1. Clone the repository

git clone YOUR_REPOSITORY_URL
cd linkforge

Replace "YOUR_REPOSITORY_URL" with your actual repository URL.

2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Start the server

uvicorn main:app --host 127.0.0.1 --port 8000

Open "http://127.0.0.1:8000/" in your browser.

Interactive API documentation is available at "http://127.0.0.1:8000/docs".

API Endpoints

Method| Endpoint| Purpose
GET| "/"| Web interface
POST| "/api/shorten"| Create a short link
GET| "/api/links"| View saved links
GET| "/{short_code}"| Redirect to the original URL

Security Notes

- The SQLite database and local environment files should not be committed to Git.
- Use HTTPS and appropriate abuse prevention before deploying publicly.
- Do not store passwords, API keys, or other secrets in source code.

Author

Keshav Nagaraj Mesta

GitHub: https://github.com/keshavmesta-linux

---

Built as a Python web development project.
