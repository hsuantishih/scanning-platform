from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length

# 新增使用者和編輯使用者的表單類別
class UserForm(FlaskForm):
    # 設定使用者表單中 ID 屬性的標籤和驗證器
    id = IntegerField(
        "ID",
        validators=[DataRequired(message="必須填寫ID")]
    )
    # 設定使用者表單中 password 屬性的標籤和驗證器
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="必須填寫密碼"), length(max=8, message="請勿超過8個字元")]
    )
    # 設定使用者表單中 submit 的內容
    submit = SubmitField("提交表單")