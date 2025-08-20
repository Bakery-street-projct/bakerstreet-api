# api/billing/stripe_handler.py
import stripe
import os
from flask import jsonify

# Initialize Stripe
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_your_stripe_key_here')

def create_customer(email, name):
    """Create a Stripe customer"""
    try:
        customer = stripe.Customer.create(
            email=email,
            name=name
        )
        return customer
    except Exception as e:
        return None

def create_subscription(customer_id, price_id):
    """Create a subscription for a customer"""
    try:
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[{'price': price_id}],
            payment_behavior='default_incomplete',
            expand=['latest_invoice.payment_intent']
        )
        return subscription
    except Exception as e:
        return None

def get_subscription_tiers():
    """Return available subscription tiers"""
    # In a real implementation, these would be actual Stripe Price IDs
    return {
        'free': {
            'name': 'Free Tier',
            'price': 0,
            'price_id': 'price_free',
            'description': '100 requests per month'
        },
        'starter': {
            'name': 'Starter Tier',
            'price': 29,
            'price_id': 'price_starter_monthly',
            'description': '1,000 requests per month'
        },
        'professional': {
            'name': 'Professional Tier',
            'price': 99,
            'price_id': 'price_professional_monthly',
            'description': '10,000 requests per month'
        },
        'enterprise': {
            'name': 'Enterprise Tier',
            'price': 499,
            'price_id': 'price_enterprise_monthly',
            'description': '100,000 requests per month'
        }
    }

def process_payment_intent(amount, currency='usd'):
    """Create a payment intent for one-time payments"""
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount * 100,  # Convert to cents
            currency=currency,
            automatic_payment_methods={'enabled': True}
        )
        return intent
    except Exception as e:
        return None