from flask import Blueprint, render_template, redirect, url_for, flash, session
from apps.auth.forms import UserForm, RecordForm
from apps.auth.models import User, Record
from apps.app import db

# 建立 Blueprint 物件; url_prefix路由為/auth/其他
auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

# 定義 auth_bp 路由
@auth_bp.route('/')
def index():
    user = User.query.get(1234)
    for record in user.records:
        print(record.host)
    return render_template('auth/index.html')

@auth_bp.route('/user', methods=['GET', 'POST'])
def user():
    # 建立 UserForm 物件
    form = UserForm()

    # 驗證表單內容
    if form.validate_on_submit():
        # 查詢資料庫資料；form.id.data表單取值
        user = User.query.filter_by(id=form.id.data).first()
        if user:
            if user.password_hash == form.password.data:
                session['user_id'] = user.id
                flash('Login successful')
                return redirect(url_for('auth.record'))
            else:
                flash('Incorrect password')
        else:
            flash('User does not exist')

    return render_template('auth/user.html', form=form)

@auth_bp.route('/record', methods=['GET', 'POST'])
def record():
    # 建立 RecordForm 物件
    form = RecordForm()

    # 提交表單內容
    if form.validate_on_submit():
        record = Record(host=form.host.data, user_id=session['user_id'])
        db.session.add(record)
        db.session.commit()
        flash("Submitted Successful")
        form.host.data = ''

    user = User.query.get(session['user_id'])

    return render_template('/auth/record.html', form=form, records=user.records)