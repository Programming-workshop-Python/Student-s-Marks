from sqlalchemy import update
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData # for getting table metadata
from sqlalchemy import Table # for interacting with tables
from sqlalchemy import create_engine # for creating db engine
from sqlalchemy.dialects import postgresql

import uuid


import DB

class Update:
    def group(gr,newgr):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            group = metadata.tables["group"]
            sel = update(group).where(group.c.name==gr).values(name=newgr)
            res = conn.execute(sel)

    def subject(sub,newsub):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            subject = metadata.tables["subject"]
            sel = update(subject).where(subject.c.sub==sub).values(sub=newsub)
            res = conn.execute(sel)
    def stud(std,newstd):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            table = metadata.tables["student"]
            sel = update(table).where(table.c.fio == std).values(fio=newstd)
            res = conn.execute(sel)

