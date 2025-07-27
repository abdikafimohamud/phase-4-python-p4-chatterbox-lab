from app import app
from models import db, Message
from datetime import datetime

# Create application context
with app.app_context():
    print("Clearing old data...")
    Message.query.delete()

    print("Seeding messages...")
    messages = [
        Message(body="Hello everyone!", username="Alice"),
        Message(body="What's up?", username="Bob"),
        Message(body="Just learning Flask!", username="Charlie"),
        Message(body="React frontend is cool!", username="Dana"),
        Message(body="Python + React = ❤️", username="Eve")
    ]

    db.session.bulk_save_objects(messages)
    db.session.commit()

    print("Done seeding!")
