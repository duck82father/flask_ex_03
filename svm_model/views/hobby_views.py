from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect, secure_filename

from svm_model import db
from svm_model.forms import HobbyForm
from svm_model.models import Question, Hobby
from svm_model.views.auth_views import login_required

import os, config
from datetime import datetime

bp = Blueprint('hobby', __name__, url_prefix='/hobby')

@bp.route('/list/')
@login_required
def list():
    form = HobbyForm
    hobby_list = Hobby.query.order_by(Hobby.id.desc())
    return render_template('hobby/hobby_list.html', form = form, list=hobby_list)

# 파일 저장
def save_file(file):
    try:
        filename = secure_filename(file.filename)
        current_time = datetime.utcnow()
        unique_filename = f"{current_time.strftime('%Y%m%d%H%M%S')}_{filename}"

        # 년도와 월을 포함하는 디렉토리 경로 생성
        year_month_path = os.path.join(config.UPLOAD_FORDER, current_time.strftime('%Y/%m'))

        # 해당 경로가 존재하지 않으면 생성
        if not os.path.exists(year_month_path, unique_filename):
            os.makedirs(year_month_path)

        filepath = os.path.join(year_month_path, unique_filename)
        file.save(filepath)
        return unique_filename

    except Exception as e:
        # 에러 처리 (로그 기록 등)
        return None


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    if not g.user :
        return render_template('index.html')
    form = HobbyForm()
    if request.method == 'POST' and form.validate_on_submit():
        f = form.file.data
        hobby = Hobby(
            username = form.username.data,
            age = form.age.data,
            purpose = form.purpose.data,
            hobby4 = form.hobby4.data,
            hobby3 = form.hobby3.data,
            hobby2 = form.hobby2.data,
            hobby1 = form.hobby1.data,
            email = form.email.data,
            create_date = datetime.now(),
            user = g.user,
            # 첨부파일이 있는 경우 저장하고 없으면 None
            filename = save_file(f) if f else None
        )
        db.session.add(hobby)
        db.session.commit()
        return redirect(url_for('hobby.detail', hobby_id = hobby.id))
    return render_template('hobby/hobby_form.html', form = form)

@bp.route('/detail/<int:hobby_id>', methods=('GET','POST',))
def detail(hobby_id):
    hobby = Hobby.query.get_or_404(hobby_id)
    hobby_list = Hobby.query.order_by(Hobby.id.desc())
    return render_template('hobby/hobby_detail.html', form=hobby, list=hobby_list)