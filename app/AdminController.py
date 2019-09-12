from flask import Flask, Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound
from libs.logger import logger

AdminCtl = Blueprint('admin', __name__, url_prefix='/admin', template_folder='../views', static_folder='../static')

@AdminCtl.route("/")
def admin_index():
    logger.info('1')
    fullname = session['fullname'] if 'fullname' in session else 'Testing'
    return render_template('pages/main/index.html', modules='Main', fullname=fullname)
