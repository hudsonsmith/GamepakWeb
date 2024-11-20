import sqlite3
import json
from lib.logged_in import logged_in
from lib.version import version
from random import choice
from flask import (
    Blueprint,
    render_template,
    abort,
    session,
    redirect,
    request,
    url_for,
    send_from_directory,
)
# import git

import os


site = Blueprint("games", __name__, template_folder="site")
current_game = None


@site.route("/static/games/<path:path>")
@logged_in
def game_renderer(path):
    # print(f"static/games/{path}")
    if path.split("/")[0] in os.listdir("static/games"):
        if path[-1] != "/":
            fixed_path = ""
            file = path.split("/")[-1]

            for i, p in enumerate(path.split("/")):
                if i == len(path.split("/")) - 1:
                    break

                else:
                    fixed_path += f"{p}/"

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            game = path.split("/")[0]

            print(f"\n\n{game}\n\n")

            if file == "index.html":
                cursor.execute(f"SELECT game FROM plays WHERE game='{game}'")
                conn.commit()

                result = cursor.fetchone()

                # If the result is found, that means that the game exists.
                print(f"\n\nRESULTS: {result}\n\n")

                if result:
                    cursor.execute(
                        f"UPDATE plays SET plays = plays + 1 WHERE game='{path.split('/')[0]}'"
                    )
                    conn.commit()

                else:
                    cursor.execute(f"INSERT INTO plays VALUES('{game}', 1)")
                    conn.commit()

                conn.close()

            return send_from_directory(f"static/games/{fixed_path}", file)

        # return send_from_directory("static", f"games/{path}/index.html")


@site.route("/games")
@logged_in
def games():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    games_dirs = {}

    for game in os.listdir("static/games"):
        cursor.execute(f"SELECT plays FROM plays WHERE game='{game}'")
        plays = cursor.fetchone()
        print(plays)

        # If plays is a number return it, else return 0
        if plays != None:
            games_dirs[game] = plays[0]

        else:
            games_dirs[game] = 0

    games_dirs = sorted(games_dirs.items(), key=lambda item: item[1], reverse=True)

    return render_template("pages/games.html", game_dirs=games_dirs, version=version)
