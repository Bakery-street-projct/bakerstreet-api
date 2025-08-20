# 🚀 Deployment Guide - Baker Street Laboratory API

## Prerequisites

1. **Python 3.9+** installed
2. **Docker** (optional but recommended)
3. **Stripe Account** for payment processing
4. **Domain Name** (optional but recommended)

## Quick Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Bakery-street-projct/bakerstreet-api.git
cd bakerstreet-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file:
```bash
API_SECRET_KEY=your-very-secure-secret-key
STRIPE_SECRET_KEY=sk_test_your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable_key
```

### 4. Run the Application
```bash
python -m api.app
```

The API will be available at `http://localhost:5000`

## Docker Deployment

### 1. Build and Run with Docker
```bash
docker-compose up --build
```

### 2. Access the API
Visit `http://localhost:5000`

## Production Deployment

### Option 1: Heroku (Easiest)
```bash
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
```

### Option 2: AWS EC2
1. Launch an EC2 instance
2. Install Docker and Docker Compose
3. Deploy using docker-compose

### Option 3: Google Cloud Run
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/bakerstreet-api
gcloud run deploy --image gcr.io/PROJECT-ID/bakerstreet-api --platform managed
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_SECRET_KEY` | Secret key for JWT tokens | Yes |
| `STRIPE_SECRET_KEY` | Stripe secret key | Yes |
| `STRIPE_PUBLISHABLE_KEY` | Stripe publishable key | Yes |
| `DATABASE_URL` | PostgreSQL database URL | No (uses SQLite by default) |

## API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get API key

### Models
- `POST /api/v1/models/scientific/query` - Scientific research
- `POST /api/v1/models/legal/query` - Legal research
- `POST /api/v1/models/creative/query` - Creative writing
- `GET /api/v1/models/status` - Model status

### Account Management
- `GET /api/v1/usage` - Usage statistics
- `GET /api/v1/pricing` - Pricing information

## Testing

Run the test suite:
```bash
python -m tests.test_api
```

## Monitoring

Set up monitoring with:
1. **Sentry** for error tracking
2. **New Relic** for performance monitoring
3. **Papertrail** for log management

## Scaling

For high-traffic deployments:
1. Use a load balancer
2. Set up Redis for caching
3. Use PostgreSQL instead of SQLite
4. Implement horizontal scaling with Kubernetes

## Security

1. Always use HTTPS in production
2. Rotate API keys regularly
3. Implement rate limiting
4. Use environment variables for secrets
5. Regular security audits

## Backup and Recovery

1. Daily database backups
2. API key rotation policy
3. Disaster recovery plan
4. Monitoring alerts

## Support

For deployment issues:
- Email: iamthatiamresearch@gmail.com
- GitHub Issues: https://github.com/Bakery-street-projct/bakerstreet-api/issues

---

*"In business, as in research, the most improbable solutions often yield the greatest returns."*