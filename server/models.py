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
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', backref='users')


class School(db.Model, SerializerMixin):

    __tablename__ = "schools"

    id = db.Column(db.Integer(), primary_key=True)
    school_name = db.Column(db.String, nullable=False)
    poster = db.Column(db.String(), nullable=False, unique=True) 
    location = db.Column(db.String, nullable=False, unique=True)
    owner_id = db.Column(db.Interger, nullable=False)
   
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
class CLasses(db.MOdel, SerializerMixin):

    __tablename__ = "classes"

    id = db.column(db.Integer(), primary_key=True)
    class_name = db.Column(db.String, nullable=False)
    educator_id = db.column(db.Integer, nullable=False)
    school_id = db.colum(db.Integer, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())



