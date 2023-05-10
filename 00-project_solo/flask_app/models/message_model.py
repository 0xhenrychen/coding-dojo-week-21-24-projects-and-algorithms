from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model, class_model

database = "beast_mode_gyms_db"

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ride_id = data['rides_id']  # should be rides_id
        self.user_id = data['users_id']  # should be users_id
        self.sender = None
        
    # @classmethod
    # def save(cls, data):
    #     query = '''
    #                 INSERT INTO messages (content, rides_id, users_id)
    #                 VALUES (%(content)s, %(ride_id)s, %(user_id)s);
    #             '''
    #     connectToMySQL(database).query_db(query, data)
        
    # @classmethod
    # def get_all_join_user(cls, data):
    #     query = '''
    #             SELECT * from messages
    #             JOIN users on messages.users_id = users.id
    #             WHERE messages.rides_id = %(ride_id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     output = []
    #     for row in results:
    #         this_message = cls(row)
            
    #         user_data = {
    #             "id": row["users.id"],
    #             "first_name": row["first_name"],
    #             "last_name": row["last_name"],
    #             "email": row["email"],
    #             "password": row["password"],
    #             "created_at": row["users.created_at"],
    #             "updated_at": row["users.updated_at"]
    #         }
    #         message_poster = user.User(user_data)
    #         this_message.sender = message_poster
            
    #         output.append(this_message)
    #     return output