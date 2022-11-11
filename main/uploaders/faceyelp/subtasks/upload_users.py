from main.uploaders.faceyelp.subtasks.base_task import BaseTask
from main.uploaders.common.query import load_sql
import os
import time
import ujson
from psycopg2.extras import execute_values

class UploadUser(BaseTask):
    def __init__(self, conn, schema_name, sql_path, file_path):
        super().__init__(conn, schema_name, sql_path, file_path)
    
    def execute(self):
        print("\n====================Start Uploading User====================\n")
        start_time = time.time()

        INSERT_LIMIT = 1000
        column_names = ["user_id","user_name", "email", "profile_photo",
                            "password_digest","review_count","useful","funny",
                                "cool","created_at", "updated_at"]
        f = open(f"{self.file_path}/json_datasets/yelp_academic_dataset_user.json", "r")
        user_list = []
        processed_line = []
        for line in f:
            if len(user_list) == INSERT_LIMIT:
                execute_values(
                self.cursor,
                f"INSERT INTO {self.schema_name}.user ({', '.join(column_names)}) VALUES %s",
                user_list)
                user_list.clear()
            loaded_line = ujson.loads(line)
            processed_line = []
            for col in column_names:
                match col:
                    case "user_name":
                        dat = loaded_line["name"]
                    case "created_at":
                        dat = loaded_line["yelping_since"] 
                    case "email":
                        username = loaded_line["name"]
                        "".join(username.split())
                        dat = f"{username}@gmail.com"
                    case "profile_photo":
                        dat = None
                    case "password_digest":
                        dat = None
                    case "updated_at":
                        dat = loaded_line["yelping_since"]
                    case other:
                        dat = loaded_line[col]
                if col != "friends":
                    processed_line.append(dat)
            friends=loaded_line["friends"].split(", ")
            user_list.append(tuple(processed_line))
        f.close()
        if len(user_list) > 0:
            execute_values(
                self.cursor,
                f"INSERT INTO {self.schema_name}.user ({', '.join(column_names)}) VALUES %s",
                user_list)

        end_time = time.time()
        print(f"User Uploading time: {end_time-start_time:.2f}secs\n")
        print("====================Finished Uploading Users====================\n")