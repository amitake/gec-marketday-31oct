from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('sushi.config') #config.pyにアプリ設定を追加

# main page
@app.route('/')
def index():
    return render_template('main.html', title='GEC-MarketDay')

# food menu page
@app.route('/food')
def food():
    return render_template('food.html', title='GEC-MarketDay')

# acitivities page
@app.route('/activities')
def act():
    return render_template('activities.html', title='GEC-MarketDay')