

#! /usr/bin/env python3.6

"""
tryna make my web store work
with stripe docs 
and youtube videos 
and stripe ai vscode assistant 
"""
import os
import stripe
from flask import Flask, jsonify, redirect, request
from dotenv import load_dotenv

# This is your test secret API key.
stripe.api_key = os.getenv('STRIPE_SECRET_KEY') 

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'https://www.lightbeamgiftco.com'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:

        cart_items = request.json.get('items',[])

        line_items = []
        for item in cart_items:
            line_items.append({

                'price': item['price_id'],
                'quantity': item['quantity'],
            })

        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=line_items,
            mode='payment',
            return_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
            automatic_tax={'enabled': True},
        )

        return jsonify(clientSecret=session.client_secret)      
    except Exception as e:
        return str(e), 400
    # 400??

    

@app.route('/session-status', methods=['GET'])
def session_status():
  session = stripe.checkout.Session.retrieve(request.args.get('session_id'))

  return jsonify(status=session.status, customer_email=session.customer_details.email)

if __name__ == '__main__':

    app.run(port=YOUR_DOMAIN)
