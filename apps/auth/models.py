from apps.app import db
from werkzeug.security import generate_password_hash
from datetime import datetime

# 建立繼承 db.Model 的 User 類別
class User(db.Model):
    # 資料表名稱
    __tablename__ = 'users'
    # 定義欄位內容
    id = db.Column(db.Integet, primary_key=True)
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
    record = db.relationship('Record', backref='user', lazy=True)

    # 定義初始化參數
    def __init__(self, id, password_hash):
        self.id = id
        self.password_hash = password_hash

# 建立繼承 db.Model 的 Record 類別
class Record(db.Model):
    # 資料表名稱
    __tablename__ = 'records'

    # 定義欄位內容
    id = db.Column(db.Integert, primary_key=True)
    host = db.Column(db.String(16))
    created_at = db.Column(db.Datetime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    # 定義初始化參數
    def __init__(self, id, host, create_at, user_id):
        self.id = id
        self.host = host
        self.created_at = create_at
        self.user_id = user_id

# 查詢關聯資料表的方式
# user = User.query.get(primary_key_value)
# record = user.record

# 使用初始化參數
# user = User(1234, "1234")
# db.session.add(user)
# db.session.commit()