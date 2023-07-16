from flask import Flask
from backend.backend_routes import backend_app
from frontend.frontend_routes import frontend_app
import threading

app = Flask(__name__)

app.register_blueprint(backend_app)
app.register_blueprint(frontend_app)

if __name__ == '__main__':
    def run_backend_app():
        app_backend = Flask(__name__)
        app_backend.register_blueprint(backend_app)
        app_backend.run(host='0.0.0.0', port=2087)

    def run_frontend_app():
        app_frontend = Flask(__name__)
        app_frontend.register_blueprint(frontend_app)
        app_frontend.run(host='0.0.0.0', port=2083)

    backend_thread = threading.Thread(target=run_backend_app)
    frontend_thread = threading.Thread(target=run_frontend_app)

    backend_thread.start()
    frontend_thread.start()
