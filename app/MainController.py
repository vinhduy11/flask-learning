from flask import Flask, Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound
from libs.logger import logger
from middleware.securities import login_required
from libs.mysql import MySQL
from models.AuthorizedModels import AuthorizedModels

MainCtl = Blueprint('main', __name__, url_prefix='/main', template_folder='../views', static_folder='../static')



@MainCtl.route("/")
@login_required
def main_index():
    login_info = {'username': 'duy.dinh', 'password': 'P@ssw0rd!@#$%'}
    result = AuthorizedModels().user_authen_process(params=login_info)
    logger.info(result)
    #logger.info(q_result)
    fullname = session['fullname'] if 'fullname' in session else 'Testing'
    return render_template('pages/main/index.html', modules='Dashboard', session_fullname = fullname)
