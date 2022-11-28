from flask_apispec import use_kwargs, marshal_with, doc
from flask_jwt_extended import jwt_required

from main.controllers.friend import friend_bp, API_CATEGORY, authorization_header
from main.controllers.common.jwt import check_jwt_user
from main.models.common.error import (
    ResponseError,
    ERROR_NONEXISTENT_FRIEND,
    ERROR_ALREADY_FRIENDS,
    ERROR_FRIEND_REQUEST_ALREADY_SENT,
    SUCCESS_SEND_FRIEND_REQUEST
)
from main.models.schema.friend import RequestFriendAddSchema
from main.models.friend import t_friend
from main.models.friend_request import t_friend_request
from main.models.user import get_user
from main import db
from sqlalchemy import func


@friend_bp.route("/add", methods=["POST"])
@jwt_required()
@check_jwt_user
@use_kwargs(RequestFriendAddSchema)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="Send Friend Request",
     description="Sends friend request to target user",
     params=authorization_header)
def friend_add(user, friend_id):
  if not get_user(friend_id):
    return ERROR_NONEXISTENT_FRIEND.get_response()
  
  friend_query = db.session.query(t_friend.c.user_id)\
                   .filter(t_friend.c.user_id == user.user_id)\
                   .filter(t_friend.c.friend_id == friend_id)
  reverse_query = db.session.query(t_friend.c.user_id)\
                    .filter(t_friend.c.user_id == friend_id)\
                    .filter(t_friend.c.friend_id == user.user_id)
  result = friend_query.union_all(reverse_query).count()
  if result == 2:
    return ERROR_ALREADY_FRIENDS.get_response()

  try:
    add_friend_request_query = db.insert(t_friend_request)\
      .values(user_id=user.user_id, friend_id=friend_id, created_at=func.now())
    db.session.execute(add_friend_request_query)
    db.session.commit()
  except:
    return ERROR_FRIEND_REQUEST_ALREADY_SENT.get_response()

  return SUCCESS_SEND_FRIEND_REQUEST.get_response()
