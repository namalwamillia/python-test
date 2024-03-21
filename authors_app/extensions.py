

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
bcrypt =Bcrypt()
