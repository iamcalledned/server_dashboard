# Server Dashboard

**Server Dashboard** is a lightweight, customizable Flask-based web dashboard to monitor and visualize the health of important server processes and services.

Designed for sysadmins, developers, and enthusiasts who want a simple, self-hosted, and extendable way to:
- Monitor critical services (e.g., Bitcoin Node, Login Process, Apache)
- View system metrics (CPU, Memory, Connections)
- See live login/user counts
- Detect failures or crashes instantly

Built to be:
- **Minimal**: No bloat. Just Python, Flask, psutil, and systemd hooks.
- **Extendable**: Add your own services, metrics, or custom logic easily.
- **Deployable**: Run it manually or as a systemd service.

---

## Features

- ✅ Service health monitoring (systemd integration)
- ✅ Live user counts via Redis or database
- ✅ Apache/HTTPD connection tracking
- ✅ Bitcoin Node status (via RPC or process monitoring)
- ✅ Auto-refreshing frontend dashboard (no page reloads)
- ✅ Lightweight and beautiful UI using Tailwind CSS + DaisyUI
- ✅ Extendable API for additional checks or services
- ✅ Clean project structure, ready for deployment or GitHub publication

---

## Folder Structure

```
/server-dashboard
  /backend
    __init__.py
    health_api.py
    app.py
  /frontend
    templates/
      dashboard.html
    static/
      dashboard.js
  /systemd
    dashboard.service (optional)
  README.md
  requirements.txt
  .gitignore
```

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourname/server-dashboard.git
cd server-dashboard
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Locally
```bash
python backend/app.py
```
Visit `http://localhost:5000` to view the dashboard.

### 4. (Optional) Deploy with systemd

- Copy `systemd/dashboard.service` into `/etc/systemd/system/`
- Adjust paths and user permissions inside the service file
- Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable dashboard.service
sudo systemctl start dashboard.service
```

Dashboard will now auto-start on boot.

---

## Requirements

- Python 3.8+
- Flask >=2.0.0
- psutil >=5.8.0
- redis >=4.0.0 (only if using live user tracking)

Install manually if needed:
```bash
pip install flask psutil redis
```

---

## Customizing

- Add new services to monitor in `backend/health_api.py`
- Adjust frontend layout in `frontend/templates/dashboard.html`
- Customize refresh intervals and visual styles in `frontend/static/dashboard.js`
- Extend API endpoints or add authentication if desired

---

## Contributing

Pull requests and suggestions are welcome!
If you build new health checks (e.g., MySQL, Docker containers), feel free to contribute them.

To keep the project clean:
- Stick to the `/backend` and `/frontend` separation
- Keep the API lightweight
- Avoid hardcoding environment-specific paths

---

## License

MIT License. Free for personal or commercial use.

---

**Built by**: Ned

**Version**: 0.1.0  
**Status**: Early development, fully working core features.

---

> 🌌 "Monitor what matters. Run your server with confidence."
