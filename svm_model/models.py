from svm_model import db


hobby_voter = db.Table(
    'hobby_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    three = db.Column(db.Integer, nullable=False)
    blk = db.Column(db.Integer, nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    position = db.Column(db.Text(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    purpose = db.Column(db.String(150), nullable=False)
    hobby1 = db.Column(db.String(150), nullable=True)
    hobby2 = db.Column(db.String(150), nullable=True)
    hobby3 = db.Column(db.String(150), nullable=True)
    hobby4 = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('hobby_set'))
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=hobby_voter, backref=db.backref('hobby_voter_set'))