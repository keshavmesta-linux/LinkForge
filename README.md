⚡ LinkForge

🔗 Turn long URLs into short, shareable links.

LinkForge is a lightweight URL shortener built with Python and FastAPI. Create short links, redirect visitors to original URLs, and track link clicks through a clean web interface.

<p align="center">
  <strong>🐍 Python · ⚡ FastAPI · 🗄️ SQLite · 🎨 HTML · CSS · JavaScript</strong>
</p>---

✨ Features

- 🔗 URL Shortening — Generate short codes for long URLs.
- 🚀 Fast Redirects — Redirect users to the original destination.
- 📊 Click Tracking — Count visits to shortened links.
- 🖥️ Web Interface — Use LinkForge through your browser.
- 🔌 REST API — Create and list links through API endpoints.
- 🗄️ SQLite Database — Store links locally.
- 📱 Mobile-Friendly Development — Run the project using Termux.
- 🧩 Open Source Code — Explore the implementation and learn how it works.

---

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
FastAPI| Web framework and API
SQLite| Local database
HTML| Page structure
CSS| User interface styling
JavaScript| Frontend interactions
Uvicorn| ASGI server

---

📸 Preview

«Run LinkForge locally to explore the interface and create your first short link.»

---

🚀 Installation

1. Install prerequisites

Install Git and Python in Termux.
```bash
pkg update
pkg install git python
```

2. Clone the repository
```bash
git clone https://github.com/keshavmesta-linux/LinkForge.git
cd LinkForge
```

3. Create a virtual environment
```bash
python -m venv .venv
```

4. Activate the virtual environment
```bash
source .venv/bin/activate
```

5. Install dependencies
```bash
python -m pip install -r requirements.txt
```

6. Start the application
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

7. Open LinkForge

Open your browser and visit:

Web Interface:<b> http://127.0.0.1:8000/</b>

Interactive API Documentation: <b>http://127.0.0.1:8000/docs</b>

Keep the Termux session running while you use the application.

---

🔌 API Endpoints

Method| Endpoint| Description
"GET"| "/"| Open the web interface
<br>
"POST"| "/api/shorten"| Create a shortened link<br>
"GET"| "/api/links"| List stored links<br>
"GET"| "/{short_code}"| Redirect to the destination<br>

Explore request formats and responses through the interactive API documentation at "/docs".

---

📁 Project Structure

LinkForge/
├── cli/
│   └── banner.py
├── static/
│   ├── app.js
│   └── style.css
├── templates/
│   └── index.html
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
└── st.py

---

🗄️ Database

LinkForge uses SQLite to store shortened URLs and their click counts.

The database file is created locally when the application initializes. Each installation maintains its own database unless a shared database is configured.

Note: The database file is local application data and is not included in the Git repository.

---

🔒 Security & Privacy

- Use HTTPS when deploying a public instance.
- Validate URLs and protect the service against spam and abuse before public deployment.
- Do not commit database files, credentials, or environment secrets.
- Avoid storing sensitive information in shortened URLs.
- Click counts are basic analytics, not a complete analytics system.

---

🗺️ Roadmap

- [x] Basic URL shortening
- [x] Redirect handling
- [x] Click tracking
- [x] Web interface
- [x] REST API
- [ ] Custom short URLs
- [ ] QR code generation
- [ ] Improved analytics
- [ ] Production deployment

---

👨‍💻 Author

Keshav Nagaraj Mesta

GitHub: "@keshavmesta-linux" (https://github.com/keshavmesta-linux)

---

<p align="center">
  ⚡ <strong>LinkForge — Short links. Simple sharing.</strong>
</p>
