# Project Outline
## Description: "Enlighten" is an educational web application that takes users on an interactive journey through various scientific topics. The main interface features a 3D tree of life with 10 branches, each representing a different area of science. Users can click on each branch to explore a wealth of information, visuals, and interactive elements

## Technology Stack

Backend: Python (using a web framework like Flask or Django)
Frontend: JavaScript, HTML, CSS
3D Graphics: Three.js (a popular library for creating 3D graphics in the browser)
Database: PostgreSQL or MongoDB

### Project Structure

#### Backend (Python)

 Models: Define data models for each topic, including content, links to external sources, and interactive elements.

#### Routes: Set up routes for handling user interactions, such as clicking on a branch or requesting information

#### Data Retrieval: Use APIs to fetch data from sources like Wikipedia, Google Maps, and others

#### Logic: Implement logic to process and organize information for presentation to the user

#### Frontend (JavaScript HTML, CSS)

#### Index Page: Create a landing page with a 3D tree of life using Three.js

#### Branch Pages: Develop individual pages   for each branch, featuring interactive elements and content

#### UI Components: Design and implement user interface components for navigation, information display, and user interactions

    ####Database:
    Topic Data: Store information about each topic, including text, images, videos, and links.
    User Progress: Track user progress through the game, allowing them to continue where they left off.

    #### Additional Features:

#### Music and Sound Effects: Integrate audio to enhance the user experience

#### Dev Containers: Utilize dev containers to create a consistent development environment

##### External APIs: Leverage APIs from  Wikipedia, Google Maps, and other sources to fetch data.
#######  The schema file typically refers to a file that defines the structure and organization of data in a database or data storage system. The type of file used for a schema can vary depending on the database management system (DBMS) or data storage solution being used. Here are a few common types of files used for database schemas:

##### 1. **SQL Script Files**: In relational databases, the schema is often defined using SQL (Structured Query Language) statements. Schema files for such databases might be plain text files with a `.sql` extension, containing SQL statements to create tables, define columns, set constraints, and establish relationships between tables.
2. **Data Definition Language (DDL) Files**: DDL is a subset of SQL used specifically for defining the structure of a database. Schema files in this context would contain DDL statements, such as `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`.
##### 3. **XML Schema Files**: XML (eXtensible Markup Language) is often used to define data structures and schemas. An XML schema file, typically with a `.xsd` extension, describes the structure, content, and constraints of an XML document.
##### 4. **JSON Schema Files**: JSON (JavaScript Object Notation) Schema is a popular format for defining the structure of JSON data. A JSON schema file, usually with a `.json` extension, specifies the types,, and constraints of JSON data.
##### 5. **Database-Specific Schema Files**: Different database systems may have their own proprietary schema file formats. For example, MongoDB uses JSON-like documents to define schemas, while systems like Apache Avro use `.avsc` files to define data types and schemas.
###### 6. **ERD (Entity-Relationship Diagram) Files**: While not strictly a file type, ERDs are visual representations of database schemas. They show entities (tables), their attributes (columns), and the relationships between them. ERD files are often saved as images or diagrams with extensions like `.png`, `.jpg`, or `.draw`.

##### The specific type of schema file you use depends on the database system you are working with and the tools or frameworks you have chosen for your project. Always refer to the documentation of your chosen DBMS or data storage solution to determine the recommended or supported schema file format.

###### To create a tree with ten operational branches that open into ten different Python map paths of information about each of the ten topics/branches of the tree of life, you can follow these steps:

##### 1. **Define your topics/branches**: List the ten topics/branches that you want to include in your tree. For example:

   ```python
   topics = ["Science", "Technology", "Engineering", "Mathematics", "Art", "History", "Geography", "Music", "Literature", "Sports"]
   ```

##### 2. **Create a class for your tree branches**: Create a class that represents each branch of your tree. This class should have properties such as the branch's name, the topics it represents, and the Python map path that opens when the branch is clicked.

   ```python
   class TreeBranch:
       def __init__(self, name, topics, map_path):
           self.name = name
           self.topics = topics
           self.map_path = map_path
   ```

##### . **Create a class for your tree**: Create a class that represents the entire tree. This class should have methods for initializing the tree, adding branches, and handling user interactions.

   ```python
   class Tree:
       def __init__(self, container):
           self.container = container
           self.branches = []
           self.numBranches = 10
           # Set the number of branches
           self.topics = [
               "Science", "Technology", "Engineering", "Mathematics",
               "Art", "History", "Geography", "Music", "Literature", "Sports"
           ]  # Add your topics here

       def init(self):
           # Create the branches and add them to the tree
           for i in range(self.numBranches):
               branch = TreeBranch(self, i, self.topics[i])
               branch.create()
               self.branches.append(branch)

       def handle_branch_click(self, branch_id):
           # Find the branch with the given ID and open the corresponding Python map path
           branch = self.find_branch_by_id(branch_id)
           if branch:
               window.location.href = branch.map_path

       def find_branch_by_id(self, branch_id):
           # Search for the branch with the given ID
           for branch in self.branches:
               if branch.id == branch_id:
                   return branch
           return None
   ```

###### 4. **Update the front-end HTML file**: Modify the `front-end.html` file to include the `Tree` class and its methods. Replace the existing JavaScript code with the following code:

   ```javascript
   <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
   <script src="js/tree.js"></script> <!-- Your custom JavaScript for the tree -->
   <script>
       // Initialize the tree and handle interactions
       const treeContainer = document.getElementById('tree-container');
       const tree = new Tree(treeContainer);
       tree.init();

       // Add event listeners for branch clicks
       tree.branches.forEach(branch => {
           branch.addEventListener('click', () => {
               const topicId = branch.dataset.topicId; // Assuming you set a data attribute on the branch
               window.location.href = `/topics/${topicId}`;
           });
       });
   </script>
   ```

###### 5. **Create a new SQLite database schema  file**: Create a new file called `dataBaseSchema.sql` and add the following SQL code to define a table for your topic data:

   ```sql
   CREATE TABLE topics (
       id INTEGER PRIMARY KEY,
       title TEXT,
       content TEXT,
       source TEXT,
       url TEXT,
       image_url TEXT
   );
   ```

###### 6. **Update the back-end Python file**: Modify the `backEnd.py` file to include the `TopicModel` class and its methods. Replace the existing code with the following code:

   ```python
   from flask import Flask, request, jsonify
   from sqlite3 import connect, cursor

   app = Flask(__name__)

   # Define your topic data models and database connection here
   def save_topic_data(topic_data):
       new_topic = TopicModel(
           title=topic_data['title'],
           content=topic_data['content'],
           source=topic_data['source'],
           url=topic_data['url'],
           image_url=topic_data['image_url']
       )

       # Connect to the SQLite database
       db = connect('topics.db')

       # Save the topic data to the database
       cursor = db.cursor()
       cursor.execute("INSERT INTO topics (title, content, source, url, image_url) VALUES (?, ?, ?, ?, ?, ?)", (new_topic.title, new_topic.content, new_topic.source, new_topic.url, new_topic.image_url))


       db.commit()

   @app.route('/save_topic', methods=['POST'])
   def save_topic():
       topic_data = request.get_json()
       save_topic_data(topic_data)
       return jsonify({ "message": "Topic data saved successfully." })
   ```

###### 7. **Create a new Python file for the topic data model**: Create a new file called `TopicModel.py` and add the following code to define the `TopicModel` class:


   ```python
   class TopicModel:
       def __init__(self, db):
           self.db = db

       def save_topic_data(self, topic_data):
           cursor = self.db.cursor()
           cursor.execute("INSERT INTO topics (title, content, source, url, image_url) VALUES (?, ?, ?, ?, ?, ?)", (topic_data['title'], topic_data['content'], topic_data['source'], topic_data['url'], topic_data['image_url']))


       db.commit()
   ```

8. **Update the front-end HTML file**: Modify the `front-end.html` file to include the `TopicModel` class and its methods. Replace the existing code with the following code:


   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Enlighten: The Tree of Life</title>
       <link rel="stylesheet" href="styles.css">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Enlighten: The Tree of Life</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <div id="tree-container"></div>


       <script src="https://cdnjs.cloudflare.com/ajax/libs/ajax/lib.js"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/lib.js"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/lib.js"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/lib.js"></script>
       <script src="js/tree.js"></script>
       <script>
       // Initialize the tree and handle interactions
       const treeContainer = document.getElementById('tree-container');
       const tree = new Tree(treeContainer);
       tree.init();


       // Add event listeners for branch clicks
       tree.branches.forEach(branch => {
           if (typeof branch.dataset.topicId !== undefined) {
                const topicId = parseInt(document.querySelector('tree-container').dataset.topicId);
                window.location.href = `/topics/${topicId}`;
           }
       });


       </body>
       <script>
       This is a sample code to create a tree with ten branches.
       Each branch of the tree will open a 3D web-based application.
       </script>
   ```


   This is a sample code to create a tree with ten branches. Each branch of the tree will open a 3D web-based application.
   ```
   ```
  
   ```
 


Here's a summary of the selected code:

###### 1. **Technology Stack**: The project will use Python (with a web framework like Flask or Django) for the backend, and JavaScript, HTML, and CSS for the frontend. Three.js, a popular library for creating 3D graphics in the browser, will be used to create the 3D tree of life interface.

2. **Project Structure**: The project will have several subdirectories, including `ModuleRoot/Docker/firstDraft_subModule/Outline.md`, which contains the outline for the project. Other subdirectories will contain Python scripts, HTML files, and other resources.

3. **Backend (Python)**: The project will use Python to define data models for each topic, handle user interactions, retrieve data from external sources, and implement logic to process and organize information for presentation to the user.

4. **Frontend (JavaScript HTML, CSS)**: The project will use JavaScript, HTML, and CSS to create the interactive 3D tree of life interface, as well as individual pages for each branch that feature interactive elements and content.

5. **Database**: The project will use a SQLite database to store information about each topic, including text, images, videos, and links. User progress will also be tracked in the database.

6. **Additional Features**: The project will incorporate additional features such as music and sound effects, dev containers for creating a consistent development environment, and external APIs from sources like Wikipedia, Google Maps, and others to fetch data.


   Maks_ElementalMatrixGame/
    ├── Maks_ElementalMatrixGame/
    │   ├── __init__.py
    │   ├── docker/
    │   │   ├── Dockerfile
    │   │   ├── firstDraft_subModule/
    │   │   │   ├── __init__.py
    │   │   │   ├── backEnd.py
    │   │   │   ├── dataBaseSchema.sql
    │   │   │   ├── front-end.html
    │   │   │   ├── tree.js
    │   │   │   ├── Tree.1.js
    │   │   │   ├── TopicModelSQLiteDB.py
    │   │   │   └── data/
    │   │       └── topics.db
    │   ├── ModuleRoot/
    │   │   ├── Dockerfile
    │   │   ├── firstDraft_subModule/
    │   │   │   ├── __init__.py
    │   │   │   ├── backEnd.py
    │   │   │   ├── dataBaseSchema.sql
    │   │   │   ├── front-end.html
    │   │   │   ├── tree.js
    │   │   │   ├── Tree.1.js
    │   │   │   ├── TopicModelSQLiteDB.py
    │   │   │   └── data/
    │   │       └── topics.db
    │   ├── ModuleRoot/Docker/
    │   │   ├── Dockerfile
    │   │   ├── firstDraft_subModule/
    │   │   │   ├── __init__.py
    │   │   │   ├── backEnd.py
    │   │   │   ├── dataBaseSchema.sql
    │   │   │   ├── front-end.html
    │   │   │   ├── tree.js
    │   │   │   ├── Tree.1.js
    │   │   │   ├── TopicModelSQLiteDB.py
    │   │   │   └── data/
    │   │       └── topics.db
    │   └── README.md


######  `__init__.py` file for the SQL Database module. This module provides a simple interface for working with a SQLite database, specifically for managing a "TopicModel" table. Here's a breakdown of the code:

###### 1. The code starts by importing the `sqlite3` module, which is Python's built-in library for working with SQLite databases.

###### 2. Several functions are defined to handle database operations:

   ###### - `create_connection`: Creates a connection to a SQLite database, either in-memory or file-based.
   - `create_topic_model_table`: Creates the "TopicModel" table if it doesn't exist.
   - `insert_topic_model_data`: Inserts data into the "TopicModel" table.
   - `retrieve_topic_model_data`: Retrieves all data from the "TopicModel" table.
   - `execute_query`: Executes a custom SQL query with optional parameters.

3. The main class `SQLDatabaseModule` is defined, which encapsulates the database operations:

   - The constructor initializes a database connection and creates the "TopicModel" table.
   - `insert_topic`: Inserts a new topic into the database.
   - `get_all_topics`: Retrieves all topics from the database.
   - `execute_custom_query`: Allows executing custom SQL queries.
   - `close_connection`: Closes the database connection.

##### 4. The `__all__` list at the end specifies which names should be imported when using `from module import *`. It includes the main class and utility functions.


