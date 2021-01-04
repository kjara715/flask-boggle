from boggle import Boggle
from flask import Flask, request, render_template, session, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS, cross_origin

app=Flask(__name__)
app.debug = True
CORS(app)
app.config['SECRET_KEY'] = "secretkey"

toolbar=DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def game_page():
    board=boggle_game.make_board()
    session['board'] = board
    highscore=session.get("highscore", 0) #if no highscore, then the highscore is set to 0
    nplays=session.get("nplays", 0) #if no plays, then the highscore is set to 0
    return render_template("home.html", highscore=highscore, nplays=nplays)

@app.route('/word-guess')
def check_word():
    my_word=request.args['word']
    board=session["board"]
    result = boggle_game.check_valid_word(board, my_word) #pass in the board and the word to check
    
    return jsonify({"result": result})

# @app.route('/score', methods=["POST", "GET"])
# def post_score():
#     score= request.json['currentScore'] #why not request.form?
