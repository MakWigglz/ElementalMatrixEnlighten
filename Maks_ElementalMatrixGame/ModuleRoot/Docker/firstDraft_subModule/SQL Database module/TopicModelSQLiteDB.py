import sqlite3

# Connect to the SQLite database (in-memory database for this example)
connection = sqlite3.connect(':memory:')

# Create a cursor object to interact with the database
cursor = connection.cursor()

sql_query = '''
    SELECT * FROMModel
    WHERE date_added > '2023-01-01'
'''
# Create the TopicModel table
# Create the "TopicModel" table
cursor.execute('''
    CREATE TABLE TopicModel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        source TEXT,
        url TEXT,
        image_url TEXT,
        date_added TEXT,
        last_updated
    )
''')
# Insert data into the "TopicModel" table
cursor.execute('''
    INSERT INTO TopicModel (title, content, source, url, image_url, date_added, last_updated)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', ('Python Basics', 'Learn Python from scratch', 'TutorialsPoint', 'https://www.tutorialspoint.com/python', 'https://www.example.com/python-image.jpg', '2023-09-01', '2023-09-01'))

# Retrieve data from the "TopicModel" table
cursor.execute('SELECT * FROM TopicModel')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Commit the changes to the database
connection.commit()

# Commit the changes to the database
connection.commit()

# Close the database connection
connection.close()