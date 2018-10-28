from .. import db
from datetime import datetime

# user_datas = db.Table('user_data',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )

# issues = db.Table('UserIssue',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
#     db.Column('authority_id', db.Integer, db.ForeignKey('authority.id'), primary_key=True)
# )

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    #firstname = db.Column(db.String(80))
    #lastname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    RepresentativeIssue = db.relationship('RepresentativeIssue', backref='user', lazy=True)
    user_data = db.relationship('UserData', backref='user', lazy=True)
    UserIssue = db.relationship('UserIssue', backref='user', lazy=True)
    # ChatTranscripts = db.relationship('ChatTranscript', backref='user', lazy=True)
    # Additional fields

    
    def __init__(self, email, password, username=None):
        self.email = email
        self.username = email if username is None else username   
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return 'User {}>'.format(self)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(80))
    status = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    region_tech_cases = db.Column(db.Integer)
    region_bill_cases = db.Column(db.Integer)
    common_interaction_type = db.Column(db.String(80))
    amnt_tech_issues = db.Column(db.Integer)
    amnt_bill_issues = db.Column(db.Integer)
    bill_amnt = db.Column(db.Float)
    avg_bill_paid = db.Column(db.Float)
    data_rate = db.Column(db.Integer)
    avg_speed = db.Column(db.Integer)
    intcall_request = db.Column(db.Integer)
    time_between_upgrades = db.Column(db.Integer)
    device_age = db.Column(db.Integer)
    avg_call_time_five_min = db.Column(db.Integer)
    region_network_state = db.Column(db.Integer)
    failed_msg_amnt = db.Column(db.Integer)
    account_stt = db.Column(db.Integer)
    failed_acct_login = db.Column(db.Integer)
    amnt_disconnections_ten_min = db.Column(db.Integer)
    def __repr__(self):
        return 'UserData {}>'.format(self)


class Representative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80))
    created_date = db.Column(db.String(100), default=datetime.utcnow())
    enabled = db.Column(db.Boolean, default=True)
    ChatTranscripts = db.relationship('ChatTranscript', backref='Representative', lazy=True)
    RepresentativeIssues = db.relationship('RepresentativeIssue', backref='Representative', lazy=True)
    # roles = db.relationship('Role', secondary=roles, backref=db.backref('users', lazy='dynamic'))
    # Additional fields

    
    def __init__(self, email, password, username=None):
        self.email = email
        #self.username = email if username is None else username   
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return 'Representative {}>'.format(self)


class UserIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(100), default=datetime.utcnow())
    issue_status = db.Column(db.String(80))
    issue_origin = db.Column(db.String(80))
    priority = db.Column(db.Integer)
    issue_id = db.Column(db.Integer, db.ForeignKey('issue.id'), nullable=False)
    ChatTranscripts = db.relationship('ChatTranscript',  primaryjoin="UserIssue.id==ChatTranscript.UserIssue_id")
    #  primaryjoin="Workgrp.workgrp_owner==Usrmst.id
    def __repr__(self):
        return 'UserIssue {}>'.format(self)

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    UserIssue = db.relationship('UserIssue', backref='User', lazy=True)
    def __repr__(self):
        return 'Issue {}>'.format(self)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RepresentativeIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(100), default=datetime.utcnow())
    representative_id = db.Column(db.Integer, db.ForeignKey('representative.id'), nullable=False)
    UserIssue_id = db.Column(db.Integer, db.ForeignKey('user_issue.id'), nullable=False)
    def __repr__(self):
        return 'RepresentativeIssue {}>'.format(self)

class ChatTranscript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserIssue_id = db.Column(db.Integer, db.ForeignKey('user_issue.id'), nullable=False)
    representative_id = db.Column(db.Integer, db.ForeignKey('representative.id'), nullable=False)
    # issue = db.Column(db.String(80))
    message = db.Column(db.String(255))
    date = db.Column(db.String(100), default=datetime.utcnow())
    def __repr__(self):
        return 'ChatTranscript {}>'.format(self)
