from flask import current_app as app
from main import db
from sqlalchemy.dialects.postgresql import ARRAY, JSON


t_cities = db.Table(
    "cities",
    db.Column("state", db.String(22), primary_key=True),
    db.Column("city", db.String(22), nullable=False),
    db.Column("latitude", db.Float, nullable=False),
    db.Column("longitude", db.Float, nullable=False),
    schema=app.config["SCHEMA_FACEYELP"],
    extend_existing=True)