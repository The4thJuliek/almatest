import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
     app.config.from_pyfile('config.py', silent=True)

    else:
     app.config.from_mapping(test_config)

    try:
     os.makedirs(app.instance_path)
    except OSError:
        pass

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )