from flask import *
from flask_bootstrap import Bootstrap
from os import urandom

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = urandom(24)
bootstrap = Bootstrap(app)

#Strona /index
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#Strona /krzywe-przejsciowe
@app.route('/krzywe-przejsciowe', methods=['GET', 'POST'])
def krzywe_przejsciowe():
    return render_template('krzywe-przejsciowe.html')

#Strona /wpisy-do-semaforow
@app.route('/wpisy-do-semaforow', methods=['GET', 'POST'])
def wpisy_do_semaforow():
    return render_template('wpisy-do-semaforow.html')

#Strona /dlugosc-luku-pionowego
@app.route('/dlugosc-luku-pionowego', methods=['GET', 'POST'])
def dlugosc_luku_pionowego():
    return render_template('dlugosc-luku-pionowego.html')

@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html'), 404