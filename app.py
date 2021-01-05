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
    """
    Home page which shows board and form for word submission

    """
    board=boggle_game.make_board()
    session['board'] = board
    highscore=session.get("highscore", 0) #if no highscore, then the highscore is set to 0
    nplays=session.get("nplays", 0) #if no plays, then the highscore is set to 0
    return render_template("home.html", highscore=highscore, nplays=nplays)

@app.route('/word-guess')
def check_word():
    """
    runs the check_valid_word function to see if the word submitted counts as a valid english word on the board.
    responds with a json object containing the result from the function

    """
    my_word=request.args['word']
    board=session["board"]
    result = boggle_game.check_valid_word(board, my_word) #pass in the board and the word to check
    
    return jsonify({"result": result})

@app.route('/score', methods=["POST"])
def post_score():
    """
    takes the current score at the end of the game 

    """
    score= request.json['currentScore'] #why not request.form?
    highscore = session.get("highscore", 0)
    nplays=session.get("nplays", 0)

    session['nplays']=nplays+1
    session['highscore']=max(score, highscore) #the highscore becomes the current score

    return jsonify(brokeRecord=score > highscore)
