# API Documentation

## Authentication

All API requests require an API key. Include it in the `X-API-Key` header:

```
X-API-Key: YOUR_API_KEY_HERE
```

### Register
```bash
curl -X POST /auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### Login
```bash
curl -X POST /auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

## Scientific Model API

### Query Endpoint
`POST /api/v1/models/scientific/query`

#### Request Body
```json
{
  "prompt": "Your research question here",
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 1000
  }
}
```

#### Response
```json
{
  "model": "baker-street-scientific",
  "query": "Your research question here",
  "methodology": "Mixed-Methods Research Design",
  "approach": "Quantitative-qualitative sequential explanatory strategy",
  "steps": [
    "Literature Review and Theoretical Framework Development",
    "Hypothesis Formulation",
    "Research Design and Methodology Selection"
  ],
  "estimated_time": "4-6 weeks",
  "confidence_score": 0.87,
  "timestamp": "2025-08-20T20:00:00Z"
}
```

## Legal Model API

### Query Endpoint
`POST /api/v1/models/legal/query`

#### Request Body
```json
{
  "prompt": "Legal requirements for clinical trials",
  "parameters": {
    "jurisdiction": "US"
  }
}
```

## Creative Model API

### Query Endpoint
`POST /api/v1/models/creative/query`

#### Request Body
```json
{
  "prompt": "Write an executive summary for our research",
  "parameters": {
    "tone": "professional"
  }
}
```

## Rate Limits

- **Free Tier**: 100 requests per month
- **Starter Tier**: 1,000 requests per month
- **Professional Tier**: 10,000 requests per month
- **Enterprise Tier**: 100,000 requests per month

## Error Responses

```json
{
  "message": "Error description"
}
```

Common HTTP status codes:
- `200` - Success
- `400` - Bad Request
- `401` - Unauthorized
- `429` - Rate limit exceeded
- `500` - Internal server error