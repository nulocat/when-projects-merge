from flask import Flask, Blueprint

def load_blueprints(instance: Flask | Blueprint):
    from Pomodoro.pomodoro import create_blueprint as pomo_create_bp
    instance.register_blueprint(pomo_create_bp(), url_prefix='/pomo')
    return instance

def create_app(): # for use like a standalone app
    app = Flask(__name__)
    app = load_blueprints(app)
    app.config.from_object('config.Config')
    return app

def create_blueprint(): # for use like a subapp
    bp = Blueprint('pomodoro', __name__, template_folder='templates')
    bp = load_blueprints(bp)
    return bp


