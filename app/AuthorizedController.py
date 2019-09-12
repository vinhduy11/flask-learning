from flask import Flask, Blueprint, render_template, abort, request, jsonify, session
from jinja2 import TemplateNotFound
from libs.logger import logger

AuthorizedCtl = Blueprint("authorized", __name__, url_prefix='/authorized', template_folder='../views', static_folder='../static')

@AuthorizedCtl.route("/login")
def login_page():
    return render_template('pages/login/login.html')

@AuthorizedCtl.route("/doLogin", methods=['POST'])
def login():
    response = None
    post_param = request.get_json()
    if 'username' in post_param and 'password' in post_param:
        if not post_param['username'] or not post_param['password']:
            response = {'status': False, 'code': 1, 'msg': 'Username or Password can not be blank!'}
        else:
            if post_param['username'] == 'admin' and post_param['password'] == 'admin':
                session['username'] = post_param['username']
                session['fullname'] = post_param['username']
                response = {'status': True, 'code': 0, 'msg': 'Login Successful!'}
            else:
                response = {'status': False, 'code': 2, 'msg': 'Wrong Username or Password!'}
    return jsonify(response)

@AuthorizedCtl.route("/doLogout", methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('fullname', None)

    if 'username' and 'fullname' not in session:
        response = {'status': True, 'code': 0, 'msg': 'Login Successful!'}
    else:
        response = {'status': False, 'code': -1, 'msg': 'Error Processing!'}
    return jsonify(response)