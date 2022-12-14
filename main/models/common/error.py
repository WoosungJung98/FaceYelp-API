from marshmallow import fields, Schema


class Error:
  def __init__(self, id, msg, code):
    self.id = id
    self.msg = msg
    self.code = code

  def get_response(self, **msg_kwargs):
    msg = self.msg.format(**msg_kwargs)
    return {"msg_id": self.id, "msg": msg}, self.code


class ResponseError(Schema):
  msg_id = fields.Str(data_key="msgID")
  msg = fields.Str()


ERROR_LIST_PAGE_INVALID = Error("u001", "Page must be larger than 0.", 400)
ERROR_LIST_LENGTH_INVALID = Error("u002", "Length must be positive or 0.", 400)

ERROR_BUSINESS_ID_NOT_EXISTS_PATH = Error("u101", "Specified Business ID Does Not Exist!", 404)

ERROR_INVALID_CREDENTIALS = Error("u201", "Invalid email or password!", 401)
SUCCESS_LOGOUT = Error("u202", "Log out success.", 200)
SUCCESS_CHANGE_PASSWORD = Error("u203", "Change password success.", 200)
ERROR_PASSWORD_CONFIRMATION = Error("u204", "Password confirmation failure!", 422)
ERROR_EMAIL_PATTERN_INVALID = Error("u205", "Email is formatted incorrectly!", 422)
ERROR_FAILED_ACCOUNT_CREATION = Error("u206", "Account creation failed!", 409)
SUCCESS_ACCOUNT_CREATION = Error("u207", "Account successfully created!", 200)
ERROR_EMAIL_ALREADY_TAKEN = Error("u208", "Given email address already exists in database!", 409)
SUCCESS_EMAIL_AVAILABLE = Error("u209", "Given email address is available.", 200)

ERROR_NONEXISTENT_FRIEND = Error("u301", "Given friend is not found in database!", 404)
ERROR_NO_SELF_FRIEND_REQUEST = Error("u302", "Sending friend request to oneself is prohibited.", 409)
ERROR_ALREADY_FRIENDS = Error("u303", "Given friendship already exists in database!", 409)
ERROR_FRIEND_REQUEST_ALREADY_SENT = Error("u304", "Friend request has already been sent to target user!", 409)
SUCCESS_SEND_FRIEND_REQUEST = Error("u305", "Successfully sent friend request to target user.", 200)
ERROR_NONEXISTENT_FRIEND_REQUEST = Error("u306", "Given friend request is not found in database!", 404)
ERROR_FRIEND_REQUEST_UNAUTHORIZED = Error("u307", "User does not have permission to act upon given friend request.", 401)
SUCCESS_ACCEPT_FRIEND_REQUEST = Error("u308", "Successfully accepted given friend request.", 200)
SUCCESS_IGNORE_FRIEND_REQUEST = Error("u309", "Successfully ignored given friend request.", 200)

ERROR_NONEXISTENT_RESTAURANT = Error("u401", "Given restaurant is not found in database!", 404)
ERROR_FRIEND_REQUIRED_MEAL_REQUEST = Error("u402", "User must be friends with target friend to send meal request!", 409)
ERROR_INVALID_MEAL_TIME = Error("u403", "Given time is invalid for scheduling meal request!", 400)
ERROR_MEAL_ALREADY_SCHEDULED = Error("u404", "Meal has already been scheduled!", 409)
ERROR_MEAL_REQUEST_ALREADY_SENT = Error("u405", "Meal request has already been sent to target user!", 409)
SUCCESS_SEND_MEAL_REQUEST = Error("u406", "Successfully sent meal request to target user.", 200)
ERROR_NONEXISTENT_MEAL_REQUEST = Error("u407", "Given meal request is not found in database!", 404)
ERROR_MEAL_REQUEST_UNAUTHORIZED = Error("u408", "User does not have permission to act upon given meal request.", 401)
SUCCESS_ACCEPT_MEAL_REQUEST = Error("u409", "Successfully accepted given meal request.", 200)
SUCCESS_IGNORE_MEAL_REQUEST = Error("u410", "Successfully ignored given meal request.", 200)

ERROR_REVIEW_CREATE_FAILED = Error("u501", "Review creation has failed.", 409)
SUCCESS_REVIEW_CREATE = Error("u502", "Successfully created a review.", 200)
