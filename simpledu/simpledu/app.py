from flask import Flask,render_template
from simpledu.config import configs
from simpledu.models import db,Course

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)

    @app.route('/')
    def index():
        courses = Course.query.all()
        return render_template('index.html',courses=courses)

    @app.route('/admin')
    def admin_index():
        return 'admin'

    return app
