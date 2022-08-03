# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import MySQLConnection

# model the class after the friend table from our database
class user_model:
    
    def __init__(self, data):
        self.id =data["id"]
        self.first_name= data["first_name"]
        self.last_name= data["last_name"]
        self.email= data["email"]
        self.created_at= data["created_at"]
        
    @classmethod
    def get_all(cls):

        query = "select * from users_table;"
        results = MySQLConnection("user_cr").query_db(query)
        users= []
        for user in results:
            users.append(cls(user))
        # print(results)
        return users

    @classmethod
    def create_user(cls,data):
        query = "insert into users_table (first_name, last_name, email) values (%(first_name)s, %(last_name)s, %(email)s);"
        results = MySQLConnection("user_cr").query_db(query, data)
        print(results)
        return results

    @classmethod
    def one_user_function(cls,data):
        query= "select * from users_table where id = %(id)s"
        user = MySQLConnection("user_cr").query_db( query,data )
        return cls(user[0])
    
    @classmethod
    def edit_user_info(cls,data):
        query = "update users_table set first_name = %(first_name)s, last_name=%(last_name)s,email=%(email)s where id = %(id)s;"
        results = MySQLConnection("user_cr").query_db(query, data)
        return results
    
    @classmethod
    def delete_user_info(cls,data):
        query = "delete from users_table where id = %(id)s;"
        results = MySQLConnection("user_cr").query_db(query, data)
        return results

