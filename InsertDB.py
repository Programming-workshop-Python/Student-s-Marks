from sqlalchemy import MetaData # for getting table metadata
from sqlalchemy import Table # for interacting with tables
from sqlalchemy import create_engine # for creating db engine
from sqlalchemy.dialects.postgresql import insert
import uuid
from DB import Group,Student,Subject
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import Select

class Instdate:

    def add(name,index):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            if index==0:
                subs = metadata.tables["subject"]
                addname = subs.insert().values(id=str(uuid.uuid4()), sub=name)
            else:
                gr = metadata.tables["group"]
                addname = gr.insert().values(id=str(uuid.uuid4()), name=name)

            engine.execute(addname)


    def addStud(name,sex,group):#addStudent
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            student = metadata.tables["student"]
            get_id = Select.Select.id(group,1)
            addsub = student.insert().values(id=str(uuid.uuid4()), fio = name, gender = sex, group_id = get_id)
            engine.execute(addsub)


    def addMark(date,gr,fio,mark,sub):#addmark
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            table = metadata.tables["mark"]
            get_id=Select.Select.sql_group(fio,1)
            get_id_group =get_id[1]
            get_id_fio = get_id[0]
            get_id_sub = Select.Select.getID(sub)
            addmark = table.insert().values(id=str(uuid.uuid4()), mark = mark, data = date, group_id = get_id_group, subject_id = get_id_sub, student_id = get_id_fio)
            engine.execute(addmark)