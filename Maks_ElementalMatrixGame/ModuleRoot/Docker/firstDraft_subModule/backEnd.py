from flask import Flask, request, jsonify
from your_database_module import TopicModel  # Replace with your database model
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

# Replace this with your actual database connection URL
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

# Replace this with your actual database connection URL
DATABASE_URL = 'postgresql://username:password@localhost:5432/your_database_name'

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session

DATABASE_URL = 'postgresql://username:password@localhost:5432/your_database_name'

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session

app = Flask(__name__)

# Define your topic data models and database connection here
def save_topic_data(topic_data):
    new_topic = TopicModel(
        title=topic_data['title'],
        content=topic_data['content'],=topic_data['source'],
        url=topic_data['url'],
        image_url=topic_data['image_url']
    )
    
    session.add(new_topic)
    session.commit()
    
    return new_topic.id

def get_topic_data(topic_id):
    topic = session.query(TopicModel).filter_by(id=topic_id).first()
    return topic

# Example usage:
topic = get_topic_data(topic_id)
print(topic.title)
print(topic.content)
# ... and so on

# Example usage:
topic_id = save_topic_data(fetch_wikipedia_data('Science'))

@app.route('/topics/<int:topic_id>')
def get_topic_data(topic_id):
    topic = TopicModel.get_by_id(topic_id)
    return jsonify(topic.to_dict())

# Add more routes and logic needed

if __name__ == '__main__':
    app.run()