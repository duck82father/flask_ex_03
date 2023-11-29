from svm_model import db

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