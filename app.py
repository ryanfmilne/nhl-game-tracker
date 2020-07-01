from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nhltracker.db'
db = SQLAlchemy(app)


class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	team = db.Column(db.String(100), nullable=False)
	game_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return 'game ' + str(self.id)


class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return 'team ' + str(self.id)
		
class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return 'player ' + str(self.id)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/tracker')
def tracker():
	return render_template('tracker.html')


 
if __name__ == "__main__":
	app.run(debug=True)