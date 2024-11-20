from lib.logged_in import logged_in
from flask import Blueprint, send_from_directory

site = Blueprint("favicon", __name__, template_folder="site")


@site.route("/favicon.ico")
def favicon():
    return send_from_directory("static/img", "logo.ico")