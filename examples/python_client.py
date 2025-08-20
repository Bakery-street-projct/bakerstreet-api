# examples/python_client.py
import requests
import json

class BakerStreetClient:
    def __init__(self, base_url="http://localhost:5000", api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["X-API-Key"] = api_key
    
    def register(self, username, password):
        """Register a new user"""
        data = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth/register", 
                               headers=self.headers, 
                               data=json.dumps(data))
        return response.json()
    
    def login(self, username, password):
        """Login and get API key"""
        data = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth/login", 
                               headers=self.headers, 
                               data=json.dumps(data))
        result = response.json()
        if 'api_key' in result:
            self.api_key = result['api_key']
            self.headers["X-API-Key"] = self.api_key
        return result
    
    def scientific_query(self, prompt, parameters=None):
        """Query the scientific model"""
        data = {"prompt": prompt}
        if parameters:
            data["parameters"] = parameters
            
        response = requests.post(f"{self.base_url}/api/v1/models/scientific/query", 
                               headers=self.headers, 
                               data=json.dumps(data))
        return response.json()
    
    def legal_query(self, prompt, parameters=None):
        """Query the legal model"""
        data = {"prompt": prompt}
        if parameters:
            data["parameters"] = parameters
            
        response = requests.post(f"{self.base_url}/api/v1/models/legal/query", 
                               headers=self.headers, 
                               data=json.dumps(data))
        return response.json()
    
    def creative_query(self, prompt, parameters=None):
        """Query the creative model"""
        data = {"prompt": prompt}
        if parameters:
            data["parameters"] = parameters
            
        response = requests.post(f"{self.base_url}/api/v1/models/creative/query", 
                               headers=self.headers, 
                               data=json.dumps(data))
        return response.json()

# Example usage
if __name__ == "__main__":
    # Initialize client
    client = BakerStreetClient()
    
    # Register and login (for demo purposes)
    print("Registering user...")
    result = client.register("demo_user", "demo_password")
    print(result)
    
    print("\nLogging in...")
    result = client.login("demo_user", "demo_password")
    print(result)
    
    # Make a scientific query
    print("\nMaking scientific query...")
    result = client.scientific_query("Design a clinical trial for depression treatment")
    print(json.dumps(result, indent=2))