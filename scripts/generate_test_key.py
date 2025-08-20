#!/usr/bin/env python3
# generate_test_key.py - Generate a test API key for development

import jwt
import datetime
import os
import sys

def generate_test_key(username="test_user", days=365):
    """Generate a test API key for development"""
    
    # Use a default secret key for testing
    secret_key = os.environ.get('API_SECRET_KEY', 'test-secret-key-for-development-only')
    
    # Create a JWT token
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=days),
        'iat': datetime.datetime.utcnow(),
        'test': True
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = "test_user"
    
    api_key = generate_test_key(username)
    
    print(f"🧪 Test API Key Generated for user: {username}")
    print("=" * 50)
    print(f"🔑 API Key: {api_key}")
    print("")
    print("💡 Usage example:")
    print(f"curl -H 'X-API-Key: {api_key}' https://api.bakerstreetlabs.com/api/v1/models/status")
    print("")
    print("⚠️  WARNING: This is a TEST key for development only!")
    print("⚠️  Do not use in production!")

if __name__ == "__main__":
    main()