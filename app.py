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
