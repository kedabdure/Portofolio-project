from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap

# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    # db.init_app(app)
    # migrate.init_app(app, db)
    # Bootstrap(app)
    
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    
    return app
