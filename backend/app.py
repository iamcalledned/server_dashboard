from flask import Flask, render_template
from backend.health_api import api_health_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(api_health_bp)

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
