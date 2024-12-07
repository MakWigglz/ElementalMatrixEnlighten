from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wikipedia
from datetime import datetime

Base = declarative_base()

INITIAL_TOPICS = ['Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology', 
                  'Mathematics', 'Computer Science', 'Environmental Science', 
                  'Psychology', 'Neuroscience']

# Replace this with your actual database connection URL
DATABASE_URL = 'postgresql://username:password@localhost:5432/Maks_ElementalMatrixGame/ModuleRoot/Docker/firstDraft_subModule/SQL Database module/TopicModelSQLiteDB.py'

# Define your TopicModel class as a SQLAlchemy model
class TopicModel(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    source = Column(String)
    url = Column(String)
    image_url = Column(String)
    date_added = Column(String)
    last_updated = Column(String)

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def fetch_wikipedia_data(topic):
    # ... (rest of the function remains the same)

def save_topic_data(topic_data):
    # ... (rest of the function remains the same)

def get_topic_data(topic_id):
    # ... (rest of the function remains the same)

def update_topic_data(topic_id, updated_data):
    # ... (rest of the function remains the same)

def delete_topic_data(topic_id):
    # ... (rest of the function remains the same)

def initialize_topics():
    for topic in INITIAL_TOPICS:
        if not session.query(TopicModel).filter_by(title=topic).first():
            topic_data = fetch_wikipedia_data(topic)
            if 'error' not in topic_data:
                save_topic_data(topic_data)

# Call this function when your app starts
initialize_topics()

app = Flask(__name__)

# ... (rest of the Flask routes remain the same)

if __name__ == '__main__':
    app.run()