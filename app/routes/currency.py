# app/routes/currency.py
from flask import Blueprint, request, jsonify

currency_api = Blueprint('currency_api', __name__)

conversion_rates = {
    'IN': 83,     # INR
    'US': 1,      # USD
    'FR': 0.9,    # Euro
    'JP': 110,    # Yen
}

@currency_api.route('/pricing', methods=['GET'])
def pricing():
    country = request.args.get('country', 'US')
    base_price_usd = 100
    rate = conversion_rates.get(country.upper(), 1)
    local_price = base_price_usd * rate
    return jsonify({
        "currency": country.upper(),
        "price": local_price
    })
