from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from svm_model import db
from svm_model.forms import HobbyForm
from svm_model.models import Question, Hobby
from datetime import datetime

bp = Blueprint('hobby', __name__, url_prefix='/hobby')

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = HobbyForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = HobbyForm()
    if request.method == 'POST' and form.validate_on_submit():
        hobby = Hobby(
            username=form.username.data,
            age=form.age.data,
            purpose=form.purpose.data,
            hobby4=form.hobby4.data,
            hobby3=form.hobby3.data,
            hobby2=form.hobby2.data,
            hobby1=form.hobby1.data,
            email=form.email.data
        )
        db.session.add(hobby)
        db.session.commit()
        return render_template('hobby/hobby_detail.html', form=Hobby.query.order_by(Hobby.id.desc()).first())
    return render_template('hobby/hobby_form.html', form=form)


    