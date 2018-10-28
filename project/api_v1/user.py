from flask import jsonify, request

from . import api
from . import ml_engine
from .. import db, bcrypt, login_manager
from ..models.user import User, UserData, UserIssue, Issue
from ..schemas.user import user_schema, users_schema, user_schema_secure, users_schema_secure
from ..validator import validate_json, validate_schema
from ..util import copy_not_null
from flask_login import login_user, logout_user, login_required, current_user
import json


from dummy import create_users

def set_up():
  fakes = create_users()
  for i in fakes:
    db.session.add(User(fakes[i][1], fakes[i][0], fakes[i][2]))
  db.session.commit()
  return jsonify(fakes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@api.route('/users/login', methods=['POST'])
def login():
    credentials = request.get_json()
    user = User.query.filter_by(email=credentials['email']).first()
    if user and bcrypt.check_password_hash(user.password, credentials['password']):
        login_user(user)
        return user_schema_secure.jsonify(user)
    return jsonify({}), 401

@api.route('/users/logout')
@login_required
def logout():
    logout_user()
    return jsonify({}), 200

@api.route('/user/help/<int:id>', methods=['GET'])
def get_help(id):
    # user = User.query.get(id)
    # user_out = ml_engine.runEngineSingle(user)
    # login for populatin issue table for users with possible issue
    return jsonify({"user": 1}), 200

@api.route('/user/issues/<int:id>', methods=['POST'])
def post_issue(id):
    data = request.get_json()
    if data["type"] == 'specific':
      userIssue = UserIssue.query.get(data["issueId"])
      userIssue.issue_origin = "user"
      userIssue.priority = "high"
    else:
      db.session.add(UserIssue(id, issue_status="unresolved", issue_origin="user", priority="high"))
      db.session.commit()
    # login for populatin issue table for users with possible issue
    return jsonify({"posted": True}), 200

@api.route('/user/issues/<int:id>', methods=['GET'])
def get_issues(id):
    # issue = UserIssue.query.filter_by(user_id=id).first()
    gen_Issues = Issue.query.all()
    res =[]
    for row in gen_Issues:
      rw = row.as_dict()
      rw["type"] = "generic"
      res.append(rw)
    # login for populatin issue table for users with possible issue
    # posts=list(BlogPost.query.all())
    return jsonify({"genIssues": res}), 200


@api.route('/users', methods=['GET'])
def get_users():
    return users_schema_secure.dumps(User.query.all()) 

@api.route('/users/logged')
@login_required
def get_current_user():
    return user_schema_secure.jsonify(current_user)

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is not None:
        return user_schema_secure.jsonify(User.query.get(id))
    return jsonify({}), 404

@api.route('/user_data/<int:id>', methods=['GET'])
def get_user_data(id):
    user = UserData.query.filter_by(user_id=id).all()
    return jsonify({"user": user}), 200

@api.route('/run/ml', methods=['GET'])
def run_ml():
    users = User.query.all()
    user_outs = ml_engine.runEngine(users)
    # login for populatin issue table for users with possible issue
    return jsonify({"user": 1}), 200


@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data["email"])
    db.session.add(User(data["email"], data["username"], data["password"]))
    db.session.commit()
    return jsonify({"issue": 1}), 200

@api.route('/users', methods=['GET'])
def list_user():
    data = User.query.all()
    return jsonify({"users": data}), 200



@api.route('/users/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)
    scheme = user_schema_secure.load(request.get_json(), partial=True)  
    #copy_not_null(scheme.data, user)
    #user.id = id
    #user.created_date = None
    #user.email = scheme.data.email
    #user = scheme.data
    #user.id = id
    #user.roles = []
    db.session.add(user)
    db.session.commit()
    return user_schema_secure.jsonify(user)


@api.route('/users/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({}), 200

@api.route('/health', methods=['GET'])
def health_check():
    set_up()
    return jsonify({}), 200


