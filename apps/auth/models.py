from apps.app import db
from werkzeug.security import generate_password_hash
from datetime import datetime

# 建立繼承 db.Model 的 User 類別
class User(db.Model):
    # 資料表名稱
    __tablename__ = 'users'
    # 定義欄位內容
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(8))

    # 設置密碼的屬性
    @property
    def password(self):
        raise AttributeError("無法加載")
    
    # 藉由設定密碼的 setter 函數，設定經過雜湊處理的密碼
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 建立資料表關係
    records = db.relationship('Record', backref='user')

    # 定義初始化參數
    def __init__(self, id, password_hash):
        self.id = id
        self.password_hash = password_hash

    # 設定回傳值
    def __repr__(self):
        return f"<User {self.id}>"

# 建立繼承 db.Model 的 Record 類別
class Record(db.Model):
    # 資料表名稱
    __tablename__ = 'records'

    # 定義欄位內容
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host = db.Column(db.String(16))
    created_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # TableName.TableColumn, ex: users.id

    # 定義初始化參數
    def __init__(self, host, user_id):
        self.host = host
        self.user_id = user_id

    # 設定回傳值
    def __repr__(self):
        return f"<Record {self.id}>"

# 查詢關聯資料表的方式
# users = User.query.all()
# for user in users:
#     print(user)
#     for record in user.records:
#         print(record.host)

# 使用初始化參數
# user = User(1234, "1234")
# db.session.add(user)
# db.session.commit()

# 查看回傳值
# user = User(1234, "1234")
# print(user) OUTPUT: <User 1234>