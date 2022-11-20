from marshmallow import Schema, fields, validate


# Requests
class RequestFriendListSchema(Schema):
  friend_name = fields.Str(validate = validate.Length(min = 3, max = 255))

# Responses
class FriendList(Schema):
  friend_id = fields.Str(data_key="friendID")
  user_name = fields.Str(data_key="userName")
  profile_photo = fields.Str(data_key="profilePhoto")


class ResponseFriendListSchema(Schema):
  friend_list = fields.List(fields.Nested(FriendList), data_key="friendList")
