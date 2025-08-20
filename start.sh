#!/bin/bash
# start.sh

echo "🚀 Starting Baker Street Laboratory API..."

# Check if we're in a virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Not in a virtual environment. Consider creating one for isolation."
fi

# Start the Flask development server
echo "🔧 Starting Flask development server..."
python -m api.app

echo "✅ API server stopped."