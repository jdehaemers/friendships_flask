from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM friendships LEFT JOIN users AS a ON a.id = friendships.user_id LEFT JOIN users AS b ON b.id = friendships.friend_id;'
        results = connectToMySQL('friendships_schema').query_db(query)
        return results
    
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO friendships (user_id, friend_id) VALUES ( %(user_id)s, %(friend_id)s );'
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    @classmethod
    def check(cls, data):
        query = 'SELECT * FROM friendships WHERE (user_id = %(user_id)s AND friend_id = %(friend_id)s) OR (user_id = %(friend_id)s AND friend_id = %(user_id)s);'
        if len(connectToMySQL('friendships_schema').query_db(query, data)) > 0:
            return True