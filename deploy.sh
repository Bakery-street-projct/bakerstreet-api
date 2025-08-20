#!/bin/bash
# deploy.sh

echo "🚀 Deploying Baker Street Laboratory API..."

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null
then
    echo "❌ docker-compose is not installed. Please install docker-compose first."
    exit 1
fi

# Build and start the containers
echo "📦 Building Docker images..."
docker-compose build

echo "🚀 Starting services..."
docker-compose up -d

echo "✅ API is now running on http://localhost:5000"

echo ""
echo "🔧 Next steps:"
echo "1. Test the API: curl http://localhost:5000"
echo "2. Register a user: curl -X POST http://localhost:5000/auth/register -H 'Content-Type: application/json' -d '{\"username\": \"test\", \"password\": \"test123\"}'"
echo "3. Login to get an API key: curl -X POST http://localhost:5000/auth/login -H 'Content-Type: application/json' -d '{\"username\": \"test\", \"password\": \"test123\"}'"
echo ""
echo "🌐 For production deployment:"
echo "1. Update the SECRET_KEY in environment variables"
echo "2. Set up Stripe API keys for billing"
echo "3. Configure domain and SSL certificates"
echo "4. Set up a production database (PostgreSQL recommended)"