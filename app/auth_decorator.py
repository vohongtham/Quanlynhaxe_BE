import os
import jwt
from functools import wraps
from flask import request, jsonify

# Securely retrieve the JWT secret key (from config or environment variables)
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# In-memory storage for blacklisted tokens (ideally, this should be stored in a persistent store)
blacklisted_tokens = set()

def add_to_blacklist(token):
    blacklisted_tokens.add(token)

def remove_from_blacklist(token):
    blacklisted_tokens.discard(token)

def is_blacklisted(token):
    return token in blacklisted_tokens

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 401
        
        try:
            # Extract token from the Authorization header
            token = auth_header.split(" ")[1]

            # Check if the token is blacklisted
            if is_blacklisted(token):
                return jsonify({"error": "Token has been blacklisted. Please log in again."}), 401

            # Decode the JWT token
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])

            # Attach user information to the request if necessary
            request.user = decoded_token

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired. Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token. Please log in again."}), 401
        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 400

        return f(*args, **kwargs)
    
    return decorator

