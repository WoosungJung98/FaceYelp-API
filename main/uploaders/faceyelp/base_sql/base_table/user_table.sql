DROP TABLE IF EXISTS {schema_name}.user;

CREATE TABLE {schema_name}.user (
  user_id CHAR(22) PRIMARY KEY NOT NULL,
  user_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  profile_photo CHAR(22),
  avatar_num INT,
  password_digest BYTEA,
  review_count INT NOT NULL,
  useful INT NOT NULL,
  funny INT NOT NULL,
  cool INT NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);

COMMENT ON COLUMN {schema_name}.user.user_id IS '22 character unique user id, maps to the user in user.json';
COMMENT ON COLUMN {schema_name}.user.user_name IS 'the users first and last name';
COMMENT ON COLUMN {schema_name}.user.email IS 'the users email address, must be unique';
COMMENT ON COLUMN {schema_name}.user.profile_photo IS 'the users profile photo unique ID';
COMMENT ON COLUMN {schema_name}.user.avatar_num IS 'the users avatar number';
COMMENT ON COLUMN {schema_name}.user.password_digest IS 'the users hashed password';
COMMENT ON COLUMN {schema_name}.user.review_count IS 'the number of reviews theyve written';
COMMENT ON COLUMN {schema_name}.user.useful IS 'number of useful votes sent by the user';
COMMENT ON COLUMN {schema_name}.user.funny IS 'number of funny votes sent by the user';
COMMENT ON COLUMN {schema_name}.user.cool IS 'number of cool votes sent by the user';
COMMENT ON COLUMN {schema_name}.user.created_at IS 'when the user joined FaceYelp';
COMMENT ON COLUMN {schema_name}.user.updated_at IS 'when the user updated info on FaceYelp';
