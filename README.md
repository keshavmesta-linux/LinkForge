LinkForge 🔗

A lightweight URL shortener built with Python, FastAPI, and SQLite.

LinkForge converts long URLs into short links, redirects visitors to the original destinations, and tracks link clicks. It includes a web interface and a command-line interface (CLI).

✨ Features

- Generate short links with random codes
- Redirect short links to their original URLs
- Track click counts
- View link history and statistics
- Responsive web interface
- Command-line interface
- SQLite database with automatic initialization
- FastAPI backend and interactive API documentation

🛠️ Tech Stack

- Backend: Python, FastAPI
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- CLI: Python
- Version Control: Git and GitHub

📂 Project Structure

LinkForge/
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

🚀 Installation

1. Install prerequisites

On Termux, install Git and Python:

pkg update
pkg install git python

2. Clone the repository

git clone https://github.com/keshavmesta-linux/LinkForge.git
cd LinkForge

3. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate

4. Install dependencies

python -m pip install -r requirements.txt

5. Start the application

uvicorn main:app --host 127.0.0.1 --port 8000

6. Open LinkForge

Open the following address in your browser:

http://127.0.0.1:8000/

Interactive API documentation:

http://127.0.0.1:8000/docs

Keep the server running while using the application.

🔌 API Endpoints

Method| Endpoint| Description
GET| "/"| Displays the web interface
POST| "/api/shorten"| Creates a short link
GET| "/api/links"| Returns saved links and click statistics
GET| "/{short_code}"| Redirects to the original URL

💾 Database

LinkForge initializes its SQLite database automatically when the application starts. Each installation maintains its own database and link records.

The local database file is excluded from Git using ".gitignore".

🔐 Security

- Do not commit databases, credentials, or private configuration files.
- Review URL validation and abuse prevention before public deployment.
- Use HTTPS and persistent database storage when deploying a shared public service.

👨‍💻 Author

Keshav Nagaraj Mesta

GitHub: https://github.com/keshavmesta-linux

---

Built with Python and FastAPI.
