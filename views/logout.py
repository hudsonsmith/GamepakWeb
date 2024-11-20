from flask import redirect, session, url_for, Blueprint

site = Blueprint("logout", __name__, template_folder="site")


@site.route("/logout")
def logout():
    if session.get("user"):
        del session["user"]

    return redirect(url_for("login.loginpage"))
