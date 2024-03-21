from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from authors_app.extensions import db
from authors_app.models.user import MyUser  # Adjust import statement

# Initialize Flask extensions
bcrypt = Bcrypt()

# Define the blueprint
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

# Define the registration endpoint
@auth.route('/register', methods=["POST"])
def register():
    try:
        # Extract user data from the request JSON
        data = request.json
        required_fields = ['first_name', 'last_name', 'email', 'user_type', 'password', 'contact']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f"{field.capitalize()} is required"}), 400

        # Validate input data
        if len(data['password']) < 6:
            return jsonify({'error': "Your password must have at least 6 characters"}), 400

        if MyUser.query.filter_by(email=data['email']).first():
            return jsonify({'error': "The email already exists"}), 409

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Create a new instance of the User model
        new_user = MyUser(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            user_type=data['user_type'],
            password=hashed_password,
            contact=data['contact']
        )

        # Add the new user instance to the database session
        db.session.add(new_user)

        # Commit the session to save the changes to the database
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@auth.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = MyUser.query.get_or_404(id)
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'contact': user.contact,
            'password': user.password,
            'user_type': user.user_type,
            'image': 'jpeg'
        }
        return jsonify(user_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = MyUser.query.all()
        user_data = []
        for user in users:
            user_info = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'contact': user.contact,
                'user_type': user.user_type
            }
            user_data.append(user_info)
        return jsonify({'users': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@auth.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = MyUser.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@auth.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = MyUser.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.contact = data.get('contact', user.contact)
        user.user_type = data.get('user_type', user.user_type)
        password = data.get('password')
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')

        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
