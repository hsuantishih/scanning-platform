from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 建立 app 物件
app = Flask(__name__)
# 建立資料庫物件
db = SQLAlchemy()
# 設定 app 配置
app.config.from_pyfile('config.py')
# 連結 SQLAlchemy 和應用程式
db.init_app(app)
# 連結 Migrate 和應用程式
Migrate(app, db)

# 註冊使用者登入 Blueprint
from apps.auth.views import auth_bp
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()