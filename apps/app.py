from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql
# Create the extension
db = SQLAlchemy()
# Create a Flask Instance
app = Flask(__name__)
# Add DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost:3306/greenbone"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Greenbone/auth/local.db"
# Secret Key
app.config['SECRET_KEY'] = 'jpadjapsfiajsiwef'
# Initialize the app with the extension
db.init_app(app)

# Create Model
class User(db.Model):
    # 定義直欄內容
    user_id = db.Column(db.String(10), primary_key=True, unique=True)
    password = db.Column(db.String(120), nullable=False)

    # 一對多的一
    # db_user_record = db.relationship("Record", backrdf="user", lazy=True)
    
    # def __init__(self, user_id, password):
    #     self.user_id = user_id
    #     self.password = password

# class Record(db.Model):
#     # 定義直欄內容
#     record_id = db.Column(db.Integer, primary_key=True)
#     host = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

#     # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

#     # 一對多的多
#     def __init__(self, user_id, record_id, host, create_at):
#         self.user_id = user_id
#         self.record_id = record_id
#         self.host = host
#         self.created_at = create_at


# Create a Form Class
class UserForm(FlaskForm):
    user_id = StringField("ID", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template('index.html')

# Create user Page
@app.route('/user', methods=['GET', 'POST'])
def user():
    user_id = None
    # user = None
    form = UserForm()

    # Validate Form
    if form.validate_on_submit():
        user = User.query.filter_by(user_id=form.user_id.data).first()
        if user is None:
            user = User(user_id=form.user_id.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
        user_id = form.user_id.data
        form.user_id.data = ''
        form.password.data = ''
        flash("User Added Successfully!")
    our_users = User.query.all()

    return render_template("user.html", form=form, user_id=user_id, our_users=our_users)