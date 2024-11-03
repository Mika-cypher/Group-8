from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.password import get_password

db = SQLAlchemy()
migrate = Migrate()

DB_USER = 'root'
DB_PASSWORD = get_password()
DB_HOST = 'localhost'
DB_NAME = 'group_8'

def create_app() :
    app = Flask (__name__)
    

    db.init_app(app)
    migrate.init_app(app,db)

    DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    app.config 
    {'SQLALCHEMY_DATABASE_URI'}= DATABASE_URI
    app.config
    {'SQLALCHEMY_TRACK_MODIFICATIONS'} = False


    from app.home.views import home_bp
    from app.module1.views import module1_bp
    from app.module2.views import module2_bp
    from app.module3.views import module3_bp
    from app.module4.views import module4_bp
    from app.module5.views import module5_bp
    from app.module6.views import module6_bp
    from app.module7.views import module7_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(module1_bp)
    app.register_blueprint(module2_bp)
    app.register_blueprint(module3_bp)
    app.register_blueprint(module4_bp)
    app.register_blueprint(module5_bp)
    app.register_blueprint(module6_bp)
    app.register_blueprint(module7_bp)


    with app.app_context():
        db.create_all()

        
    return app
