from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    # These names MUST match what is in seed.py
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    # Required for the to_dict() method used in app.py
    serialize_rules = ()