from datetime import datetime
from app import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Subscriber('{self.name}, '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}, '{self.date_posted}')"

db.create_all()
# sub_1 = Subscriber(name='alex', email='demo@demo.com')
# db.session.add(sub_1)
# db.session.commit()
# print(sub_1)