from flask import Blueprint, url_for, render_template, g
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
# Blueprint(별칭, 인수("main_views"), '@bp.route()' 앞에 붙는 접두어 url)

@bp.route('/')
def index():
    if g.user:
        return redirect(url_for('question.create'))
    return render_template('index.html')