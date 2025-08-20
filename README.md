# Baker Street Laboratory API

## Revolutionary AI Research API Platform

Transform your research capabilities with our cutting-edge AI API ecosystem. With 7/8 specialized AI models operational (25GB total), this system delivers immediate ROI through accelerated research, reduced costs, and breakthrough insights via simple API calls.

## 🚀 Quick Start

### 1. Get Your API Key
```bash
curl -X POST https://api.bakerstreetlabs.com/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'

curl -X POST https://api.bakerstreetlabs.com/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### 2. Make Your First API Call
```bash
curl -X POST https://api.bakerstreetlabs.com/api/v1/models/scientific/query \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "prompt": "Design a clinical trial for psilocybin depression treatment",
    "parameters": {
      "temperature": 0.7,
      "max_tokens": 1000
    }
  }'
```

## 🔧 API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get API key

### Models
- `POST /api/v1/models/scientific/query` - Scientific research methodology
- `POST /api/v1/models/legal/query` - Legal research and compliance
- `POST /api/v1/models/creative/query` - Creative writing and reports
- `GET /api/v1/models/status` - Check model status

### Account Management
- `GET /api/v1/usage` - Check your usage limits
- `GET /api/v1/pricing` - View pricing tiers

## 💰 Pricing

| Tier | Price | Requests/Month | Models | Features |
|------|-------|----------------|---------|----------|
| **Free** | $0 | 100 | 3 | Basic access |
| **Starter** | $29 | 1,000 | 5 | Priority support |
| **Professional** | $99 | 10,000 | All | 24/7 support |
| **Enterprise** | $499 | 100,000 | All | Dedicated support |

## 📚 Documentation

- [API Reference](/docs/api.md)
- [Authentication Guide](/docs/auth.md)
- [Model Parameters](/docs/parameters.md)
- [Rate Limits](/docs/rate-limits.md)

## 🛠️ SDKs

- [Python SDK](https://github.com/Bakery-street-projct/bakerstreet-python-sdk)
- [JavaScript SDK](https://github.com/Bakery-street-projct/bakerstreet-js-sdk)
- [Java SDK](https://github.com/Bakery-street-projct/bakerstreet-java-sdk)

## 💖 Support

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/REALbakerstreet221b)

**Bank Transfer (Lowest Fees):**
- **IBAN**: BE70 9051 5229 1825
- **BIC/SWIFT**: WIREDEMMXXX
- **Account Holder**: Kiliaan V
- **Bank**: Wise (formerly TransferWise)
- **Wise Tag**: @kiliaanv

## 📞 Contact

- **Email**: iamthatiamresearch@gmail.com
- **Phone**: +32 471 31 52 83

---
*"In business, as in research, the most improbable solutions often yield the greatest returns."*
## 💖 Support Our Work

If you find this API useful, please consider supporting us:

[![GitHub Sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/BoozeLee)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/REALbakerstreet221b)
[![Wise](https://img.shields.io/badge/Wise-FFDD00?style=for-the-badge&logo=wise&logoColor=black)](https://wise.com/pay/me/kiliaanv)

Thank you for supporting open-source AI research and development!

