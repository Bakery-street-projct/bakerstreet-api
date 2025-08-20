# api/routes.py
from flask import request, jsonify
from api.models.scientific import process_scientific_query, process_legal_query, process_creative_query
from api.app import require_api_key
import datetime

def init_routes(app):
    @app.route('/api/v1/models/scientific/query', methods=['POST'])
    @require_api_key
    def scientific_query():
        data = request.get_json()
        
        if not data or not data.get('prompt'):
            return jsonify({'message': 'Prompt is required'}), 400
        
        prompt = data['prompt']
        parameters = data.get('parameters', {})
        
        # Process the query
        result = process_scientific_query(prompt, parameters)
        
        return jsonify(result), 200
    
    @app.route('/api/v1/models/legal/query', methods=['POST'])
    @require_api_key
    def legal_query():
        data = request.get_json()
        
        if not data or not data.get('prompt'):
            return jsonify({'message': 'Prompt is required'}), 400
        
        prompt = data['prompt']
        parameters = data.get('parameters', {})
        
        # Process the query
        result = process_legal_query(prompt, parameters)
        
        return jsonify(result), 200
    
    @app.route('/api/v1/models/creative/query', methods=['POST'])
    @require_api_key
    def creative_query():
        data = request.get_json()
        
        if not data or not data.get('prompt'):
            return jsonify({'message': 'Prompt is required'}), 400
        
        prompt = data['prompt']
        parameters = data.get('parameters', {})
        
        # Process the query
        result = process_creative_query(prompt, parameters)
        
        return jsonify(result), 200
    
    @app.route('/api/v1/usage', methods=['GET'])
    @require_api_key
    def get_usage():
        # This would integrate with your actual usage tracking
        return jsonify({
            'period': 'monthly',
            'requests_used': 45,
            'requests_limit': 100,
            'reset_date': '2025-09-01T00:00:00Z',
            'tier': 'free'
        }), 200
    
    @app.route('/api/v1/pricing', methods=['GET'])
    def get_pricing():
        return jsonify({
            'tiers': [
                {
                    'name': 'Free',
                    'price': 0,
                    'requests_per_month': 100,
                    'models': ['scientific', 'legal', 'creative'],
                    'features': ['Basic API access', 'Community support']
                },
                {
                    'name': 'Starter',
                    'price': 29,
                    'requests_per_month': 1000,
                    'models': ['scientific', 'legal', 'creative', 'coder', 'audio'],
                    'features': ['Priority support', 'Higher rate limits', 'Advanced parameters']
                },
                {
                    'name': 'Professional',
                    'price': 99,
                    'requests_per_month': 10000,
                    'models': ['all_models'],
                    'features': ['24/7 support', 'Highest rate limits', 'Custom parameters', 'Early access to new models']
                },
                {
                    'name': 'Enterprise',
                    'price': 499,
                    'requests_per_month': 100000,
                    'models': ['all_models'],
                    'features': ['Dedicated support', 'Custom rate limits', 'SLA guarantee', 'Private model access']
                }
            ]
        }), 200