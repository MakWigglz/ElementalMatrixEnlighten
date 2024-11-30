from Maks_ElementalMatrixGame.ModuleRoot.Docker.firstDraft_subModule.SQL_Database_module import SQLDatabaseModule

# Initialize the database module with the existing database
db = SQLDatabaseModule()

# Retrieve all existing topics
existing_topics = db.get_all_topics()
print("Existing topics:")
for topic in existing_topics:
    print(topic)

# Insert a new test topic
db.insert_topic(
    "Test Title",
    "This is test content",
    "Test Source",
    "http://test.url",
    "http://test.image.url",
    "2023-06-14",
    "2023-06-14"
)

# Retrieve all topics again to verify the insertion
updated_topics = db.get_all_topics()
print("\nUpdated topics:")
for topic in updated_topics:
    print(topic)

# Execute a custom query
custom_query = "SELECT title, content FROM TopicModel WHERE source = ?"
result = db.execute_custom_query(custom_query, ("Test Source",))
print("\nCustom query result:")
for row in result:
    print(row)

# Close the connection
db.close_connection()