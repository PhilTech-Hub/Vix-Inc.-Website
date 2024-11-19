from app import app, db
from flask import request, jsonify
from app.models import Service, QuoteRequest

# Add Service
@app.route('/admin/service', methods=['POST'])
def add_service():
    data = request.get_json()
    new_service = Service(name=data['name'], description=data['description'], price=data['price'], category=data['category'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify({"message": "Service added successfully!"}), 201

# Get all services for customers
@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    service_list = [{"id": service.id, "name": service.name, "description": service.description, "price": service.price, "category": service.category} for service in services]
    return jsonify(service_list)

# Request a quote
@app.route('/quote', methods=['POST'])
def request_quote():
    data = request.get_json()
    quote = QuoteRequest(customer_name=data['customer_name'], service_id=data['service_id'], email=data['email'], message=data['message'])
    db.session.add(quote)
    db.session.commit()
    return jsonify({"message": "Quote request submitted successfully!"}), 201
