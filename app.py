from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nhltracker.db'
db = SQLAlchemy(app)


class Game(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	away_team = db.Column(db.String(100), nullable=False)
	away_player = db.Column(db.String(100), nullable=False)
	away_period_1 = db.Column(db.Integer, nullable=False)
	away_period_2 = db.Column(db.Integer, nullable=False)
	away_period_3 = db.Column(db.Integer, nullable=False)
	away_final = db.Column(db.Integer, nullable=False)
	home_team = db.Column(db.String(100), nullable=False)
	home_player = db.Column(db.String(100), nullable=False)
	home_period_1 = db.Column(db.Integer, nullable=False)
	home_period_2 = db.Column(db.Integer, nullable=False)
	home_period_3 = db.Column(db.Integer, nullable=False)
	home_final = db.Column(db.Integer, nullable=False)

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

@app.route('/tracker', methods=['GET', 'POST'])
def tracker():

	if request.method == 'POST':
		away_1 = request.form['away-period-1']
		away_2 = request.form['away-period-2']
		away_3 = request.form['away-period-3']
		home_1 = request.form['home-period-1']
		home_2 = request.form['home-period-2']
		home_3 = request.form['home-period-3']
		away_final_score = int(away_1) + int(away_2) + int(away_3)
		home_final_score = int(home_1) + int(home_2) + int(home_3)

		all_games = Game(
			away_team='Nashville Predators',
			away_player='Ryan',
			away_period_1=away_1,
			away_period_2=away_2,
			away_period_3=away_3,
			away_final=away_final_score, #
			home_team='Washington Capitals',
			home_player='Nick',
			home_period_1=home_1,
			home_period_2=home_2,
			home_period_3=home_3,
			home_final=home_final_score,
			)
		db.session.add(all_games)
		db.session.commit()
		return redirect('/tracker')
	else:
		all_games = Game.query.order_by(Game.game_date).all()	
		return render_template('tracker.html', games=all_games)


 
if __name__ == "__main__":
	app.run(debug=True)