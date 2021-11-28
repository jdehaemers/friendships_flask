from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL('friendships_schema').query_db(query)
        return results
    
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name) VALUES ( %(first_name)s, %(last_name)s );'
        return connectToMySQL('friendships_schema').query_db(query, data)