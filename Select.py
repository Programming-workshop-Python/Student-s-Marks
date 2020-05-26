from sqlalchemy import MetaData # for getting table metadata
from sqlalchemy import Table # for interacting with tables
from sqlalchemy import create_engine # for creating db engine
from sqlalchemy.dialects import postgresql
from sqlalchemy import select

import uuid
class Select:

    def select(index):
        data = []
        id = []
        stud = []
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            if index==1:
                group = metadata.tables["group"]
                sel = select([group.c.id,group.c.name])
            if index==0:
                sub = metadata.tables["subject"]
                sel = select([sub.c.id,sub.c.sub])
            if index==2:
                student = metadata.tables["student"]
                sel = select([student.c.id, student.c.fio])
            res = conn.execute(sel)

        for i in res:
            cut = str(i[1])
            idGr = str(i[0])
            data.append(i[1])
            id.append(i[0])
        return (data,id)


    def id(name,index):
        if index==0:
            mas_id=Select.select(0)
        if index==1:
             mas_id = Select.select(1)
        shot_mas=mas_id[0]
        for i in range(len(shot_mas)):
            if name == shot_mas[i]:
                return mas_id[1][i]

    def sql_group(fio,index):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            student = metadata.tables["student"]
            if index==1:
                sel = select([student.c.group_id,student.c.id]).where(student.c.fio == fio)
            else:
                sel = select([student.c.group_id]).where(student.c.fio ==fio)
            res_id = conn.execute(sel)
            for i in res_id:
                if index ==1:
                   return str(i[1]),str(i[0])
                else:
                    idgr = str(i)
                    idgr = idgr[2:len(idgr)-3]
            metadata = MetaData(engine, reflect=True)
            group = metadata.tables["group"]
            sel = select([group.c.name]).where(group.c.id==idgr)
            res= conn.execute(sel)
            for i in res:
                result = str(i)
            return result[2:len(result)-3]


    def getID(name):
        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            table = metadata.tables["subject"]
            sel = select([table.c.id]).where(table.c.sub == name)
            res = conn.execute(sel)
            for i in res:
                result = str(i)
            return result[2:len(result)-3]

    def sub_mark(fio):

        group_id=[]
        id= Select.sql_group(fio,1)
        fio_id=id[0]
        group_id=id[1]

        engine = create_engine('postgresql://postgres:1@localhost/WebApp')
        with engine.connect() as conn:
            metadata = MetaData(engine, reflect=True)
            table = metadata.tables["mark"]
            sel = select([table.c.mark,table.c.subject_id]).where(table.c.student_id == fio_id)
            res = conn.execute(sel)
        mark = []
        sub_id=[]
        for i in res:
            mark.append(i[0])
            sub_id.append(i[1])
        sub = []
        sub = metadata.tables["subject"]

        for i in range(len(sub_id)):
            sel = select([sub.c.sub]).where(sub.c.id==sub_id[i])
            res = conn.execute(sel)
            sub.append[str(res)]
        return mark,sub_id







