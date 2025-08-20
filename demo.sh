#!/bin/bash
# demo.sh - Demonstration script for Baker Street Laboratory API

echo "🧪 Baker Street Laboratory API - Live Demo"
echo "============================================="
echo ""

# Check if required tools are installed
if ! command -v curl &> /dev/null; then
    echo "❌ curl is required but not installed."
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "⚠️  jq is recommended for pretty JSON output."
    echo ""
fi

echo "🚀 Testing API connectivity..."
echo ""

# Test basic API endpoint
echo "📡 Testing API root endpoint..."
curl -s https://api.bakerstreetlabs.com/ 2>/dev/null || echo "⚠️  API not responding. Using mock response."

echo ""
echo "📋 Mock API Response:"
cat << 'EOF'
{
  "message": "Baker Street Laboratory API",
  "version": "1.0.0",
  "documentation": "/docs"
}
EOF

echo ""
echo "🔐 Authentication Demo:"
echo "To register a new user:"
echo 'curl -X POST https://api.bakerstreetlabs.com/auth/register \'
echo '  -H "Content-Type: application/json" \'
echo '  -d '"'"'{"username": "demo_user", "password": "demo_password"}'"'"''
echo ""

echo "To login and get an API key:"
echo 'curl -X POST https://api.bakerstreetlabs.com/auth/login \'
echo '  -H "Content-Type: application/json" \'
echo '  -d '"'"'{"username": "demo_user", "password": "demo_password"}'"'"''
echo ""

echo "🔬 Scientific Model Demo:"
echo "Example scientific query request:"
echo 'curl -X POST https://api.bakerstreetlabs.com/api/v1/models/scientific/query \'
echo '  -H "Content-Type: application/json" \'
echo '  -H "X-API-Key: YOUR_API_KEY" \'
echo '  -d '"'"'{"prompt": "Design a clinical trial for psilocybin depression treatment"}'"'"''
echo ""

echo "📋 Mock Scientific Response:"
cat << 'EOF'
{
  "model": "baker-street-scientific",
  "query": "Design a clinical trial for psilocybin depression treatment",
  "methodology": "Randomized Controlled Trial (RCT)",
  "approach": "Double-blind, placebo-controlled study",
  "steps": [
    "Recruitment and screening of participants",
    "Baseline assessment and randomization",
    "Treatment administration and monitoring",
    "Follow-up assessments at 1, 4, 8, 12 weeks",
    "Statistical analysis and reporting"
  ],
  "estimated_time": "16-20 weeks",
  "confidence_score": 0.91,
  "timestamp": "2025-08-20T22:00:00Z"
}
EOF

echo ""
echo "⚖️ Legal Model Demo:"
echo "Example legal query request:"
echo 'curl -X POST https://api.bakerstreetlabs.com/api/v1/models/legal/query \'
echo '  -H "Content-Type: application/json" \'
echo '  -H "X-API-Key: YOUR_API_KEY" \'
echo '  -d '"'"'{"prompt": "FDA regulations for psychedelic clinical trials"}'"'"''
echo ""

echo "✍️ Creative Model Demo:"
echo "Example creative query request:"
echo 'curl -X POST https://api.bakerstreetlabs.com/api/v1/models/creative/query \'
echo '  -H "Content-Type: application/json" \'
echo '  -H "X-API-Key: YOUR_API_KEY" \'
echo '  -d '"'"'{"prompt": "Write an executive summary for our psilocybin research"}'"'"''
echo ""

echo "💰 Pricing Tiers:"
echo "----------------"
echo "Free Tier: $0/month (100 requests)"
echo "Starter Tier: $29/month (1,000 requests)" 
echo "Professional Tier: $99/month (10,000 requests)"
echo "Enterprise Tier: $499/month (100,000 requests)"
echo ""

echo "💖 Support Our Work:"
echo "--------------------"
echo "GitHub Sponsors: https://github.com/sponsors/BoozeLee"
echo "PayPal: https://paypal.me/REALbakerstreet221b"
echo "Wise: https://wise.com/pay/me/kiliaanv"
echo ""

echo "📚 Documentation & Resources:"
echo "----------------------------"
echo "API Documentation: https://github.com/Bakery-street-projct/bakerstreet-api"
echo "Deployment Guide: https://github.com/Bakery-street-projct/bakerstreet-api/blob/main/docs/deployment.md"
echo "Monetization Strategy: https://github.com/Bakery-street-projct/bakerstreet-api/blob/main/docs/monetization.md"
echo ""

echo "🧪 Ready to revolutionize your research workflow?"
echo "Contact: iamthatiamresearch@gmail.com | +32 471 31 52 83"