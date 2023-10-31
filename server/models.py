from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref='users')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    

class School(db.Model, SerializerMixin):

    __tablename__ = "schools"

    id = db.Column(db.Integer(), primary_key=True)
    school_name = db.Column(db.String, nullable=False)
    poster = db.Column(db.String(), nullable=False, unique=True) 
    location = db.Column(db.String, nullable=False, unique=True)
    owner_id = db.Column(db.Interger, nullable=False)
   
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
class CLasses(db.Model, SerializerMixin):

    __tablename__ = "classes"

    id = db.column(db.Integer(), primary_key=True)
    class_name = db.Column(db.String, nullable=False)
    educator_id = db.column(db.Integer, nullable=False)
    school_id = db.colum(db.Integer, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

class Assessments(db.Model, SerializerMixin):

    __tablename__ = "Assessments"

    id = db.column(db.Integer(), primary_key=True)
    class_id = db.column(db.Integer(), nullable=False)
    title = db.column(db.String, nullable=False)
    body = db.column(db.string, nullable=False)
    start_time = db.column(db.Integer, nullable=False)
    end_time = db.column(db.Integer, nullable=False)
    duration = db.column(db.Integer, nullable=False)

    def __init__(self, class_id, title, body, start_time, end_time, duration):
        self.class_id = class_id
        self.title = title
        self.body = body
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration


class Resource(db.Model, SerializerMixin):
    
    __tablename__ = 'resources'
    resource_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    type = db.Column(db.String)
    url = db.Column(db.String)
    content = db.Column(db.String)
    educator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, title, type, url, content, educator_id):
        self.title = title
        self.type = type
        self.url = url
        self.content = content
        self.educator_id = educator_id

