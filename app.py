from boggle import Boggle
from flask import Flask, request, render_template, session, flash
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
    session['board'] = boggle_game.make_board()
    return render_template("home.html")

@app.route('/word-guess')
@cross_origin()
def check_word():
    my_word = request.args["word-guess"] #I think it's based on the id so this should work, should give the form value, which is the word that was typed in
    all_words=boggle_game.words #gives list of all words in our dictionary
    if my_word not in all_words:
        flash("Not a valid word")
        return redirect('/')

#     result = boggle_game.check_valid_word(session['board'], my_word) #pass in the board and the word to check
#     if result is "ok"
#         flash('is word')
    


