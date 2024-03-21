from authors_app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from authors_app.models.user import User

# # Create the Flask app instance
# app = Flask(__name__)

# # Configure the database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'

# # Initialize SQLAlchemy extension
# db = SQLAlchemy(app)

# # Import your blueprintfrom authors_app import create_app

# from authors_app import auth_blueprint

# # Register blueprints with the app
# app.register_blueprint(auth_blueprint)

# if __name__ == "__main__":
#     # Run the Flask application
#     app.run(debug=True)