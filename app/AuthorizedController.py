from flask import Flask, Blueprint, render_template, abort, request, jsonify, session
from jinja2 import TemplateNotFound
from libs.logger import logger
from models.AuthorizedModels import AuthorizedModels

AuthorizedCtl = Blueprint("authorized", __name__, url_prefix='/authorized', template_folder='../views', static_folder='../static')

@AuthorizedCtl.route("/login")
def login_page():
    return render_template('pages/login/login.html')

@AuthorizedCtl.route("/doLogin", methods=['POST'])
def login():
    response = {}
    post_param = request.get_json()
    if 'username' in post_param and 'password' in post_param:
        if not post_param['username'] or not post_param['password']:
            response = {'status': False, 'code': 1, 'msg': 'Username or Password can not be blank!'}
        else:
            query_rs = AuthorizedModels().user_authen_process(params=post_param)

            if query_rs:
                response.update(query_rs)
    return jsonify(response)

@AuthorizedCtl.route("/doLogout", methods=['GET'])
def logout():
    session = None

    if session is None:
        response = {'status': True, 'code': 0, 'msg': 'Logout Successful!'}
    else:
        response = {'status': False, 'code': -1, 'msg': 'Error Processing!'}
    return jsonify(response)