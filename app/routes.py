from flask import render_template, redirect, request, flash
from app import app
from .forms import BetForm, ActionForm
from app.gamecode.human import Human


makehuman = True
negativeAccount = 1
@app.route('/', methods=['GET', 'POST'])
@app.route('/bet', methods=['GET', 'POST'])
def index():
    global makehuman, human, negativeAccount
    if (makehuman or negativeAccount <= 0):
        human = Human(1000)
        makehuman = False
    form = BetForm()
    if request.method == 'POST':
        human.create_game(form.betAmount.data)
        return redirect('/action')
    elif request.method == 'GET':
        return render_template('bet.html', form = form, account=human.get_cash())

@app.route('/action', methods=['GET', 'POST'])
def action():
    global human, negativeAccount
    form = ActionForm()
    if request.method == 'POST':
        if 'hit' in request.form:
            continueGame = human.action(human.convert('hit'))
            if continueGame:
                human.write_to_file("human.csv")
                return redirect('/action')
            else:
                human.write_to_file("human.csv")
                flash(human.display_result())
                negativeAccount = human.get_cash()
                return redirect('/bet')
        elif 'stand' in request.form:
            continueGame = human.action(human.convert('stand'))
            flash(human.display_result())
            negativeAccount = human.get_cash()
            return redirect('/bet')
    human.response()
    return render_template('action.html', form = form, dealer=human.display_dealer(), player=human.display_player())

@app.route('/about')
def about():
    return render_template('about.html')