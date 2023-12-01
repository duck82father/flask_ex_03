from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect

from svm_model import db
from svm_model.forms import QuestionForm, AnswerForm
from svm_model.models import Question
from svm_model.views.auth_views import login_required

from datetime import datetime
from svm_load_model import predictions


bp = Blueprint('question', __name__, url_prefix='/question')

# @bp.route('/list/')
# def _list():
#     page = request.args.get('page', type=int, default=1)    # 페이지
#     question_list = Question.query.order_by(Question.create_date.desc())
#     question_list = question_list.paginate(page=page, per_page=10)
#     return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    if not g.user :
        return render_template('index.html')
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(three=form.subject.data, blk=form.content.data)
        # db.session.add(question)
        # db.session.commit()   
        three = question.three
        blk = question.blk
        prediction = predictions.loader(three, blk)
        pred_text = f"3P : {three}, BLK : {blk} 인 선수의 포지션은 {("슈팅가드" if prediction == 'SG' else '센터')} 입니다."
        return render_template('question/question_form.html', form=form, pred_text=pred_text)
    return render_template('question/question_form.html', form=form)
