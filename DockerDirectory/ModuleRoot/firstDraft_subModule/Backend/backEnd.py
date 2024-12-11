from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import wikipedia
from datetime import datetime

Base = declarative_base()

INITIAL_TOPICS = ['Physics', 'Chemistry', 'Biology', 'Astronomy', 'Geology', 
                  'Mathematics', 'Computer Science', 'Environmental Science', 
                  'Psychology', 'Neuroscience']

# Use SQLite for simplicity
DATABASE_URL = 'sqlite:///topics.db'

class TopicModel(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)
    source = Column(String)
    url = Column(String)
    image_url = Column(String)
    date_added = Column(String)
    last_updated = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def fetch_wikipedia_data(topic):
    try:
        page = wikipedia.page(topic)
        return {
            'title': page.title,
            'content': page.summary,
            'source': 'Wikipedia',
            'url': page.url,
            'image_url': page.images[0] if page.images else None,
            'date_added': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat()
        }
    except wikipedia.exceptions.DisambiguationError as e:
        return {'error': f"Disambiguation error for {topic}: {str(e)}"}
    except wikipedia.exceptions.PageError:
        return {'error': f"No Wikipedia page found for {topic}"}
    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}

def save_topic_data(topic_data):
    session = Session()
    try:
        new_topic = TopicModel(**topic_data)
        session.add(new_topic)
        session.commit()
        return new_topic.id
    except Exception as e:
        session.rollback()
        return {'error': f"Failed to save topic: {str(e)}"}
    finally:
        session.close()

def get_topic_data(topic_id):
    session = Session()
    try:
        topic = session.query(TopicModel).get(topic_id)
        return topic.__dict__ if topic else None
    finally:
        session.close()

def update_topic_data(topic_id, updated_data):
    session = Session()
    try:
        topic = session.query(TopicModel).get(topic_id)
        if topic:
            for key, value in updated_data.items():
                setattr(topic, key, value)
            topic.last_updated = datetime.now().isoformat()
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        return {'error': f"Failed to update topic: {str(e)}"}
    finally:
        session.close()

def delete_topic_data(topic_id):
    session = Session()
    try:
        topic = session.query(TopicModel).get(topic_id)
        if topic:
            session.delete(topic)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        return {'error': f"Failed to delete topic: {str(e)}"}
    finally:
        session.close()

def initialize_topics():
    session = Session()
    try:
        for topic in INITIAL_TOPICS:
            if not session.query(TopicModel).filter_by(title=topic).first():
                topic_data = fetch_wikipedia_data(topic)
                if 'error' not in topic_data:
                    save_topic_data(topic_data)
    finally:
        session.close()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/topics', methods=['GET'])
def get_topics():
    session = Session()
    try:
        topics = session.query(TopicModel).all()
        return jsonify([topic.__dict__ for topic in topics])
    finally:
        session.close()

@app.route('/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    topic = get_topic_data(topic_id)
    return jsonify(topic) if topic else ('', 404)

@app.route('/topics', methods=['POST'])
def create_topic():
    topic_data = request.json
    topic_id = save_topic_data(topic_data)
    return jsonify({'id': topic_id}), 201

@app.route('/topics/<int:topic_id>', methods=['PUT'])
def update_topic(topic_id):
    updated_data = request.json
    success = update_topic_data(topic_id, updated_data)
    return ('', 204) if success else ('', 404)

@app.route('/topics/<int:topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    success = delete_topic_data(topic_id)
    return ('', 204) if success else ('', 404)

if __name__ == '__main__':
    initialize_topics()
    app.run(debug=True)