from app import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))
    price = db.Column(db.Float)
    category = db.Column(db.String(100))

class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    email = db.Column(db.String(100))
    message = db.Column(db.String(500))
    service = db.relationship('Service', backref=db.backref('quote_requests', lazy=True))
