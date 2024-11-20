import importlib
from flask import redirect, render_template
import os

from flask import Flask
from flask_socketio import SocketIO
from os import name as true_os_name
from datetime import timedelta
from lib.os_name import get_os_name


app = Flask(__name__, template_folder="site")
os_name: str = get_os_name()

# You can choose from: [light, dark, dark_dimmed, dark_high_contrast]
theme: str = "dark_dimmed"
login_page_backgrounds = ["/static/img/login_background.png"]
app.debug: bool = False
app.secret_key = "Test"
app.permanent_session_lifetime = timedelta(minutes=5)

socketio = SocketIO(app)

current_game = None


for file in os.listdir("views"):
    # Make sure the file ends with .py
    if file.endswith(".py"):
        module = importlib.import_module(f"views.{file.replace('.py', '')}")
        print(f"Loading: {module}")
        app.register_blueprint(module.site)


@app.route("/")
def home() -> None:
    return redirect("login")

@app.errorhandler(404)
def handle_404(error):
    return render_template("pages/404.html"), 404

if __name__ == "__main__":
    #app.config["SECRET_KEY"] = ""
    socketio.init_app(app)
    socketio.run(app)
