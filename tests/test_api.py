# tests/test_api.py
import unittest
import sys
import os

# Add the parent directory to the path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.models.scientific import process_scientific_query, process_legal_query, process_creative_query

class TestAPIModels(unittest.TestCase):
    
    def test_scientific_query(self):
        """Test scientific query processing"""
        result = process_scientific_query("Design a clinical trial for depression treatment")
        self.assertIn('model', result)
        self.assertEqual(result['model'], 'baker-street-scientific')
        self.assertIn('methodology', result)
        
    def test_legal_query(self):
        """Test legal query processing"""
        result = process_legal_query("What are the regulations for clinical trials?")
        self.assertIn('model', result)
        self.assertEqual(result['model'], 'baker-street-legal')
        self.assertIn('jurisdiction', result)
        
    def test_creative_query(self):
        """Test creative query processing"""
        result = process_creative_query("Write an executive summary")
        self.assertIn('model', result)
        self.assertEqual(result['model'], 'baker-street-creative')
        self.assertIn('content_type', result)

if __name__ == '__main__':
    unittest.main()