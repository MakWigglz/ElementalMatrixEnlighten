-- PostgreSQL schema.sql file

-- Create a new database (if it doesn't exist)
CREATE DATABASE my_database;

-- Connect to the database
 

-- Create a new table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create another table with a foreign key reference
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    author_id INTEGER REFERENCES users(id)
);

-- Add an index to improve query performance
CREATE INDEX idx_posts_title ON posts (title);

-- ... Add more table definitions, constraints, and indexes as needed