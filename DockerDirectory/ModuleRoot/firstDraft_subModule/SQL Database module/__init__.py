import sqlite3

def create_connection(db_path='Maks_ElementalMatrixGame/ModuleRoot/Docker/firstDraft_subModule/SQL Database module/your_database.db'):
    """Create a database connection to a SQLite database"""
    connection = sqlite3.connect(db_path)
    return connection, connection.cursor()

def create_topic_model_table(cursor):
    """Create the TopicModel table"""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TopicModel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            source TEXT,
            url TEXT,
            image_url TEXT,
            date_added TEXT,
            last_updated TEXT
        )
    ''')

def insert_topic_model_data(cursor, title, content, source, url, image_url, date_added, last_updated):
    """Insert data into the TopicModel table"""
    cursor.execute('''
        INSERT INTO TopicModel (title, content, source, url, image_url, date_added, last_updated)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, content, source, url, image_url, date_added, last_updated))

def retrieve_topic_model_data(cursor):
    """Retrieve all data from the TopicModel table"""
    cursor.execute('SELECT * FROM TopicModel')
    return cursor.fetchall()

def execute_query(cursor, query, params=None):
    """Execute a custom SQL query"""
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchall()

class SQLDatabaseModule:
    def __init__(self, db_path='Maks_ElementalMatrixGame/ModuleRoot/Docker/firstDraft_subModule/SQL Database module/your_database.db'):
        self.connection, self.cursor = create_connection(db_path)
        create_topic_model_table(self.cursor)

    def insert_topic(self, title, content, source, url, image_url, date_added, last_updated):
        insert_topic_model_data(self.cursor, title, content, source, url, image_url, date_added, last_updated)
        self.connection.commit()

    def get_all_topics(self):
        return retrieve_topic_model_data(self.cursor)

    def execute_custom_query(self, query, params=None):
        return execute_query(self.cursor, query, params)

    def close_connection(self):
        self.connection.close()

# Expose the main class and functions
__all__ = ['SQLDatabaseModule', 'create_connection', 'create_topic_model_table', 
           'insert_topic_model_data', 'retrieve_topic_model_data', 'execute_query']