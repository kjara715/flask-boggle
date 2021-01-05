from unittest import TestCase
from boggle import Boggle
from flask import session 
from app import app

class TestGame(TestCase):

    def setUp(self):
        self.client=app.test_client()
        app.config['TESTING']= True

    def test_gamepage(self):
        with self.client:
            res=self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'<p class="high-score">', res.data)
    def test_valid_word(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board']=[
                    ["M", "O", "S", "S", "T"],
                    ["M", "O", "S", "S", "T"],
                    ["M", "O", "S", "S", "T"],
                    ["M", "O", "S", "S", "T"],
                    ["M", "O", "S", "S", "T"]
                ]
            response = self.client.get('/word-guess?word=moss')
            self.assertEqual(response.json['result'], 'ok')
    
    def test_invalid_word(self):
        self.client.get('/')
        response=self.client.get('/word-guess?word=meat')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_not_a_word(self):
        self.client.get('/')
        response=self.client.get('/word-guess?word=dkfjlsf')
        self.assertEqual(response.json['result'], 'not-word')