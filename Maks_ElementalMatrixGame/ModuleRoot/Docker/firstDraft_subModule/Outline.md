# Project Outline
# Description: "Enlighten" is an educational web application that takes users on an interactive journey through various scientific topics. The main interface features a 3D tree of life with 10 branches, each representing a different area of science. Users can click on each branch to explore a wealth of information, visuals, and interactive elements

# Technology Stack

Backend: Python (using a web framework like Flask or Django)
Frontend: JavaScript, HTML, CSS
3D Graphics: Three.js (a popular library for creating 3D graphics in the browser)
Database: PostgreSQL or MongoDB

## Project Structure

## Backend (Python)

 Models: Define data models for each topic, including content, links to external sources, and interactive elements.

## Routes: Set up routes for handling user interactions, such as clicking on a branch or requesting information

## Data Retrieval: Use APIs to fetch data from sources like Wikipedia, Google Maps, and others

## Logic: Implement logic to process and organize information for presentation to the user

### Frontend (JavaScript HTML, CSS)

### Index Page: Create a landing page with a 3D tree of life using Three.js

### Branch Pages: Develop individual pages   for each branch, featuring interactive elements and content

#### UI Components: Design and implement user interface components for navigation, information display, and user interactions

    ####Database:
    Topic Data: Store information about each topic, including text, images, videos, and links.
    User Progress: Track user progress through the game, allowing them to continue where they left off.

    #### Additional Features:

#### Music and Sound Effects: Integrate audio to enhance the user experience

#### Dev Containers: Utilize dev containers to create a consistent development environment

##### External APIs: Leverage APIs from  Wikipedia, Google Maps, and other sources to fetch data.
#######  The schema file typically refers to a file that defines the structure and organization of data in a database or data storage system. The type of file used for a schema can vary depending on the database management system (DBMS) or data storage solution being used. Here are a few common types of files used for database schemas:

1. **SQL Script Files**: In relational databases, the schema is often defined using SQL (Structured Query Language) statements. Schema files for such databases might be plain text files with a `.sql` extension, containing SQL statements to create tables, define columns, set constraints, and establish relationships between tables.
2. **Data Definition Language (DDL) Files**: DDL is a subset of SQL used specifically for defining the structure of a database. Schema files in this context would contain DDL statements, such as `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`.
3. **XML Schema Files**: XML (eXtensible Markup Language) is often used to define data structures and schemas. An XML schema file, typically with a `.xsd` extension, describes the structure, content, and constraints of an XML document.
4. **JSON Schema Files**: JSON (JavaScript Object Notation) Schema is a popular format for defining the structure of JSON data. A JSON schema file, usually with a `.json` extension, specifies the types,, and constraints of JSON data.
5. **Database-Specific Schema Files**: Different database systems may have their own proprietary schema file formats. For example, MongoDB uses JSON-like documents to define schemas, while systems like Apache Avro use `.avsc` files to define data types and schemas.
6. **ERD (Entity-Relationship Diagram) Files**: While not strictly a file type, ERDs are visual representations of database schemas. They show entities (tables), their attributes (columns), and the relationships between them. ERD files are often saved as images or diagrams with extensions like `.png`, `.jpg`, or `.draw`.

The specific type of schema file you use depends on the database system you are working with and the tools or frameworks you have chosen for your project. Always refer to the documentation of your chosen DBMS or data storage solution to determine the recommended or supported schema file format.