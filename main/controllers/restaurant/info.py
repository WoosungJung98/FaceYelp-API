from main import db
from main.controllers.restaurant import restaurant_bp, API_CATEGORY
from flask_apispec import marshal_with, doc
from main.models.common.error import (
    ResponseError,
    ERROR_BUSINESS_ID_NOT_EXISTS_PATH
)
from main.models.schema.restaurant import ResponseRestaurantInfoSchema
from main.models.business import get_restaurant

@restaurant_bp.route("/<string:business_id>/info", methods=["GET"])
@marshal_with(ResponseRestaurantInfoSchema, code=200)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="Restaurant Info",
    description="Shows detailed info of Restaurant"
)
def restaurant_info(business_id):
  restaurant = get_restaurant(business_id)
  if not restaurant:
    return ERROR_BUSINESS_ID_NOT_EXISTS_PATH.get_response()
  return {
    "business_info": {
      "business_id": restaurant.business_id,
      "business_name": restaurant.business_name,
      "address": restaurant.address,
      "city": restaurant.city,
      "state": restaurant.state,
      "postal_code": restaurant.postal_code,
      "latitude": restaurant.latitude,
      "longitude": restaurant.longitude,
      "stars": restaurant.stars,
      "review_count": restaurant.review_count,
      "is_open": restaurant.is_open,
      "categories": restaurant.categories,
      "hours": {
        "mon" : restaurant.hours.get('Monday', "Closed"),
        "tues" : restaurant.hours.get('Tuesday', "Closed"),
        "wed" : restaurant.hours.get('Wednesday', "Closed"),
        "thurs" : restaurant.hours.get('Thursday', "Closed"),
        "fri" : restaurant.hours.get('Friday', "Closed"),
        "sat" : restaurant.hours.get('Saturday', "Closed"),
        "sun" : restaurant.hours.get('Sunday', "Closed")
      } if restaurant.hours else {},
    }
  }
