"""
Initialize and populate a SQLite database with topic information.

This script connects to a SQLite database, creates a 'TopicModel' table if it doesn't exist,
inserts initial topic data, retrieves and prints all records, and then closes the connection.

The 'TopicModel' table structure:
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - title: TEXT
    - content: TEXT
    - source: TEXT
    - url: TEXT
    - image_url: TEXT
    - date_added: TEXT
    - last_updated: TEXT

Parameters: 
    None

Returns:
    None

Side effects:
    - Creates or connects to a SQLite database file named 'your_database.db'
    - Creates a 'TopicModel' table in the database if it doesn't exist
    - Inserts initial topic data into the 'TopicModel' table
    - Prints all records from the 'TopicModel' table
    - Commits changes to the database
    - Closes the database connection
"""
import sqlite3
# connect to the SQLite database to create a file named "your_database.db"
connection = sqlite3.connect('your_database.db')

# create a cursor object to interact with the database
cursor = connection.cursor()

# create the TopicModel table
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
# Insert data into the "TopicModel" table
cursor.execute('''
       INSERT INTO TopicModel (title, content, source, url, image_url, date_added, last_updated)
       VALUES (?,?,?,?,?,?,?)        
               ''', (# Define the initial topics
initial_topics = [
    ('Physics', 'The study of matter, energy, and their interactions', 'Wikipedia', 'https://en.wikipedia.org/wiki/Physics', 'https://example.com/physics.jpg', '2023-09-01', '2023-09-01'),
    ('Chemistry', 'The study of substances, their properties, and reactions', 'Wikipedia', 'https://en.wikipedia.org/wiki/Chemistry', 'https://example.com/chemistry.jpg', '2023-09-01', '2023-09-01'),
    ('Biology', 'The study of living organisms and their interactions', 'Wikipedia', 'https://en.wikipedia.org/wiki/Biology', 'https://example.com/biology.jpg', '2023-09-01', '2023-09-01'),
    ('Astronomy', 'The study of celestial objects and phenomena', 'Wikipedia', 'https://en.wikipedia.org/wiki/Astronomy', 'https://example.com/astronomy.jpg', '2023-09-01', '2023-09-01'),
    ('Geology', 'The study of the Earth, its structure, and its processes', 'Wikipedia', 'https://en.wikipedia.org/wiki/Geology', 'https://example.com/geology.jpg', '2023-09-01', '2023-09-01'),
    ('Mathematics', 'The study of numbers, quantities, and shapes', 'Wikipedia', 'https://en.wikipedia.org/wiki/Mathematics', 'https://example.com/mathematics.jpg', '2023-09-01', '2023-09-01'),
    ('Computer Science', 'The study of computation and information processing', 'Wikipedia', 'https://en.wikipedia.org/wiki/Computer_science', 'https://example.com/computer_science.jpg', '2023-09-01', '2023-09-01'),
    ('Environmental Science', 'The study of the environment and environmental problems', 'Wikipedia', 'https://en.wikipedia.org/wiki/Environmental_science', 'https://example.com/environmental_science.jpg', '2023-09-01', '2023-09-01'),
    ('Psychology', 'The study of the mind and behavior', 'Wikipedia', 'https://en.wikipedia.org/wiki/Psychology', 'https://example.com/psychology.jpg', '2023-09-01', '2023-09-01'),
    ('Neuroscience', 'The study of the nervous system', 'Wikipedia', 'https://en.wikipedia.org/wiki/Neuroscience', 'https://example.com/neuroscience.jpg', '2023-09-01', '2023-09-01')
]
))
# Retrieve data from the "TopicModel" table
cursor.execute('SELECT * FROM TopicModel')
rows = cursor.fetchall()
for row in rows:
    print(row)
# Commit the chnages to the database
connection.commit()
# close connection
connection.close()
