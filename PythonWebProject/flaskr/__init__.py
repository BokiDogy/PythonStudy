import os

from flask import Flask
from flaskr.studentsinfo import student as student_bp
from flaskr.classesinfo import classinfo as class_bp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        #,DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.debug=True
    app.register_blueprint(student_bp,url_prefix="/student")
    app.register_blueprint(class_bp,url_prefix="/class")
    print(app.url_map)
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
