from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model

database = "beast_mode_gyms_db"

class Class:
    def __init__(self, data):
        self.id = data["id"]
        self.class_name = data["class_name"]
        self.class_date = data["class_date"]
        self.class_time = data["class_time"]
        self.class_location = data["class_location"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.trainer_id = data["trainer_id"]
        self.trainer = None
        self.trainee = None
    
    @classmethod
    def get_all_classes(cls):
        query = ''' SELECT * FROM classes
                    JOIN users ON users.id = classes.trainer_id
                    ORDER BY class_date ASC, class_time ASC;
                '''
        results = connectToMySQL(database).query_db(query)
        output = []
        for row in results:
            this_trainer = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            user_trainer = user_model.User(user_data)
            this_trainer.trainer = user_trainer
            output.append(this_trainer)
        return output

    @classmethod
    def get_all_classes_trainer(cls, data):
        query = ''' SELECT * FROM classes
                    JOIN users ON users.id = classes.trainer_id
                    WHERE classes.trainer_id = %(user_id)s
                    ORDER BY class_date ASC, class_time ASC;
                '''
        results = connectToMySQL(database).query_db(query, data)
        output = []
        for row in results:
            this_class = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            user_trainer = user_model.User(user_data)
            this_class.trainer = user_trainer
            output.append(this_class)
        return output
    
    @classmethod
    def get_all_trainees_class(cls, data):
        query = ''' SELECT * FROM joined_classes
                    JOIN users ON users.id = joined_classes.user_id
                    JOIN classes ON classes.id = joined_classes.class_id
                    WHERE classes.id = %(class_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results
    
    @classmethod
    def get_all_classes_trainee_scheduled(cls, data):
        query = ''' SELECT * from joined_classes
                    JOIN classes ON classes.id = joined_classes.class_id
                    JOIN users ON users.id = joined_classes.user_id
                    JOIN users TR ON TR.id = classes.trainer_id 
                    WHERE users.id = %(user_id)s
                    ORDER BY classes.class_date ASC, classes.class_time ASC;
                '''       
        results = connectToMySQL(database).query_db(query, data)
        output = []
        for row in results:
            this_class = cls(row)
            
            trainee_data = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            user_trainee = user_model.User(trainee_data)
            this_class.trainee = user_trainee
            
            trainer_data = {
                "id": row["TR.id"],
                "first_name": row["TR.first_name"],
                "last_name": row["TR.last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["TR.created_at"],
                "updated_at": row["TR.updated_at"]
            }
            user_trainer = user_model.User(trainer_data)
            this_class.trainer = user_trainer
            output.append(this_class)
        return output
    
    @classmethod
    def get_all_classes_trainee_not_scheduled(cls, data):
        query = '''
                    SELECT * FROM classes
                    LEFT JOIN users ON users.id = classes.trainer_id
                    WHERE classes.id NOT IN (SELECT class_id FROM joined_classes WHERE user_id = %(user_id)s);
                '''
        results = connectToMySQL(database).query_db(query, data)
        output = []
        for row in results:
            this_class = cls(row)
            trainer_data = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            user_trainer = user_model.User(trainer_data)
            this_class.trainer = user_trainer
            output.append(this_class)
        return output

    @classmethod
    def get_class_by_id(cls, data):
        query = ''' SELECT * FROM classes
                    WHERE classes.id = %(class_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results[0]
    
    @classmethod
    def get_class_and_trainer_by_id(cls, data):
        query = ''' SELECT * FROM classes
                    JOIN users ON users.id = classes.trainer_id
                    WHERE classes.id = %(class_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        this_class = cls(results[0])
        for row in results:
            trainer_data = {
                "id": row["id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            user_trainer = user_model.User(trainer_data)
            this_class.trainer = user_trainer
        return this_class
    
    @classmethod
    def trainer_save_class(cls, data):
        query = '''
                    INSERT INTO classes (class_name, class_date, class_time, class_location, trainer_id)
                    VALUES (%(class_name)s, %(class_date)s, %(class_time)s, %(class_location)s, %(trainer_id)s);
                '''
        connectToMySQL(database).query_db(query, data)
        
    @classmethod
    def trainer_edit_class(cls, data):
        query = ''' UPDATE classes
                    SET class_name = %(class_name)s, class_date = %(class_date)s, class_time = %(class_time)s, class_location = %(class_location)s
                    WHERE ID = %(class_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results
    
    @classmethod
    def trainer_delete_class(cls, data):
        query = ''' DELETE FROM classes
                    WHERE ID = %(class_id)s;
                '''
        connectToMySQL(database).query_db(query, data)
        
    @classmethod
    def trainee_cancel_class(cls, data):
        query = ''' DELETE FROM joined_classes
                    WHERE class_id = %(class_id)s AND user_id = %(user_id)s;
                '''
        connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def assign_trainee_to_class(cls, data):
        query = ''' INSERT INTO joined_classes (user_id, class_id)
                    VALUES (%(user_id)s, %(class_id)s);
                '''
        connectToMySQL(database).query_db(query, data)
        
    @staticmethod
    def validate_create_class_form(class_data):
        is_valid = True
        if len(class_data["class_name"]) < 1:
            flash("Class name can't be empty.", "class")
            is_valid = False
        elif len(class_data["class_name"]) < 3:
            flash("Class name must be at least 3 characters.", "class")
            is_valid = False
        if len(class_data["class_date"]) < 1:
            flash("Class date can't be empty.", "class")
            is_valid = False
            
        if class_data["class_time"] == "":
            flash("Class time can't be empty.", "class")
            is_valid = False
        
        if class_data["class_location"] == "":
            flash("Please choose a class location.", "class")
            is_valid = False
        return is_valid