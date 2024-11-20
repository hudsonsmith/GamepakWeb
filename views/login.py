import json
from random import choice
from flask import Blueprint, render_template, abort, session, redirect, request, url_for

site = Blueprint("login", __name__)


@site.route("/login", methods=["POST", "GET"])
def loginpage():
    """The login page view."""
    print(f'Session User: {session.get("user")}')

    if session.get("user"):
        return redirect("games")

    if request.method == "POST":
        # Get the username.
        user = request.form["username"]
        password = request.form["password"]

        # Make sure the username is not empty.
        if user == "" or password == "":
            return redirect("login")

        with open("data.json", "r") as f:
            data = json.load(f)

        if password == data["users"].get(user):
            # Set the session to last.
            session.permanent = True
            session["user"] = {"name": user}

            return redirect(
                url_for(
                    "games.games",
                )
            )

        else:
            return redirect("login")

    else:
        return render_template(
            "pages/login.html",
            background="/static/img/login_background.png",
        )
