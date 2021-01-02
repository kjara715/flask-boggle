from boggle import Boggle
from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

debug=DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def game_page():
    session['board'] = boggle_game.make_board()
    return render_template("home.html")