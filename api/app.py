# api/app.py
from flask import Flask, request, jsonify
from functools import wraps
import os
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api.routes import init_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_SECRET_KEY', 'your-secret-key-change-in-production')

# In-memory storage (replace with database in production)
users = {}
api_keys = {}
usage_limits = {}

# Authentication decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = None
        if 'X-API-Key' in request.headers:
            api_key = request.headers['X-API-Key']
        
        if not api_key:
            return jsonify({'message': 'API key is missing'}), 401
        
        if api_key not in api_keys:
            return jsonify({'message': 'Invalid API key'}), 401
            
        # Check usage limits
        user_id = api_keys[api_key]
        if user_id in usage_limits:
            limit = usage_limits[user_id]['limit']
            used = usage_limits[user_id]['used']
            if used >= limit:
                return jsonify({'message': 'Usage limit exceeded'}), 429
            usage_limits[user_id]['used'] += 1
        
        return f(*args, **kwargs)
    return decorated_function

# Initialize routes
init_routes(app)

# Basic routes
@app.route('/')
def home():
    return jsonify({
        'message': 'Baker Street Laboratory API',
        'version': '1.0.0',
        'documentation': '/docs'
    })

@app.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
    
    if data['username'] in users:
        return jsonify({'message': 'User already exists'}), 409
    
    users[data['username']] = {
        'password': generate_password_hash(data['password']),
        'created_at': datetime.datetime.utcnow()
    }
    
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
    
    if data['username'] not in users:
        return jsonify({'message': 'Invalid credentials'}), 401
    
    if not check_password_hash(users[data['username']]['password'], data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # Generate API key
    api_key = jwt.encode({
        'username': data['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)
    }, app.config['SECRET_KEY'])
    
    api_keys[api_key] = data['username']
    usage_limits[data['username']] = {'limit': 100, 'used': 0}  # Free tier
    
    return jsonify({
        'api_key': api_key,
        'message': 'Login successful'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)