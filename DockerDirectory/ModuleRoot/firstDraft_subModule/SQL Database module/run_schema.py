import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Read the SQL file
with open('dataBaseSchema.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL
cursor.executescript(sql_script)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Schema has been successfully applied to the database.")