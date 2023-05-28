from flask import Blueprint, render_template, redirect, url_for
from apps.auth.forms import UserForm
from apps.auth.models import User
from apps.app import db

# 建立 Blueprint 物件; url_prefix路由為/auth/其他
auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

# 定義 auth_bp 路由
@auth_bp.route('/')
def index():
    return render_template('auth/index.html')

@auth_bp.route('/user', methods=['GET', 'POST'])
def user():
    # 建立 UserForm 物件
    form = UserForm()
    user = User.query.filter_by(id=4577).first()
    print(user)
    # 驗證表單值
    # if form.validate_on_submit():
        # 建立使用者

    return render_template('auth/user.html', form=form)
