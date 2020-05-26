from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:1@localhost/WebApp'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column(db.String,primary_key = True)
    name = db.Column(db.String)
    students = relationship('Student', backref="group", lazy=True)


class Student(db.Model):
    id = db.Column(db.String, primary_key=True)
    fio = db.Column(db.String)
    gender = db.Column(db.String)
    mark =db.relationship('Mark',backref='student',lazy=True)
    group_id = db.Column(db.String, db.ForeignKey('group.id'), nullable=False)

class Subject(db.Model):
    id = db.Column(db.String,primary_key = True)
    sub = db.Column(db.String)
    mark = db.relationship('Mark',backref='subject',lazy=True)

class Mark(db.Model):
    id = db.Column(db.String, primary_key=True)
    mark = db.Column(db.Integer)
    data = db.Column(db.Date)
    group_id = db.Column(db.String, db.ForeignKey('group.id'))
    subject_id = db.Column(db.String, db.ForeignKey('subject.id'))
    student_id = db.Column(db.String, db.ForeignKey('student.id'))


