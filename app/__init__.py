from flask import Flask
from app.MainController import MainCtl
from app.AuthorizedController import AuthorizedCtl
#Create Instance
app = Flask('app')
app.secret_key = '9085908324sklnfash89258nsoyi921312io780*)&*(&*(io))'
app.register_blueprint(MainCtl)
app.register_blueprint(AuthorizedCtl)

#Default Route:
@app.route('/')
def index():
    return 'Index Page'

