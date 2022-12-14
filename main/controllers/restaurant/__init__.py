from flask import Blueprint

restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/restaurant")

API_CATEGORY = "Restaurant"

from main.controllers import authorization_header

from main.controllers.restaurant.list import restaurant_list
from main.controllers.restaurant.info import restaurant_info
from main.controllers.restaurant.photos import restaurant_photos
from main.controllers.restaurant.reviews import (
    restaurant_reviews,
    restaurant_review_create
)
