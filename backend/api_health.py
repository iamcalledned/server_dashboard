from flask import Blueprint, jsonify
import subprocess
import psutil
import redis

api_health_bp = Blueprint("api_health", __name__)

# Initialize Redis client
try:
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
except redis.RedisError:
    r = None

def check_service(name):
    result = subprocess.run(["systemctl", "is-active", name], capture_output=True, text=True)
    return result.stdout.strip()

def get_bitcoin_status():
    try:
        result = subprocess.run(["bitcoin-cli", "getblockchaininfo"], capture_output=True, text=True)
        if result.returncode == 0:
            return "Running"
        else:
            return "Error"
    except Exception:
        return "Unavailable"

@api_health_bp.route('/api/health')
def health():
    return jsonify({
        "bitcoin": {
            "status": check_service("bitcoind.service"),
            "details": get_bitcoin_status()
        },
        "login_handler": {
            "status": check_service("login_handler.service"),
            "users_logged_in": int(r.get("current_logged_in_users") or 0) if r else "N/A"
        },
        "background_updater": {
            "status": check_service("background_updaters.service")
        },
        "market_dashboard": {
            "status": check_service("market_dashboard.service")
        },
        "apache2": {
            "status": check_service("apache2.service"),
            "connections": len(psutil.net_connections(kind='inet'))
        }
    })
