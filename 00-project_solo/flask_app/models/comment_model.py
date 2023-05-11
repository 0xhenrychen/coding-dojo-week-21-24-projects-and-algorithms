from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model, class_model

database = "beast_mode_gyms_db"

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.class_comment = data['class_comment']
        self.class_id = data['class_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.commentor = None
        
    @classmethod
    def save_comment(cls, data):
        query = '''
                    INSERT INTO comments (class_comment, class_id, user_id)
                    VALUES (%(class_comment)s, %(class_id)s, %(user_id)s);
                '''
        connectToMySQL(database).query_db(query, data)
        
    @classmethod
    def get_all_comments_by_class(cls, data):
        query = '''
                    SELECT * FROM comments
                    JOIN users ON users.id = comments.user_id
                    WHERE comments.class_id = %(class_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        output = []
        for row in results:
            this_commentor = cls(row)
            
            commentor_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            user_commentor = user_model.User(commentor_data)
            this_commentor.commentor = user_commentor
            output.append(this_commentor)
        return output