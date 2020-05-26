from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import InsertDB as inst
import Select,Update


app = Flask(__name__)

@app.route('/')
def start_page() -> 'html':
   return render_template('1.html')

#STUDENT
@app.route('/AddStudent')
def add_student()->'html':
    group = Select.Select.select(1)
    return render_template('Registr.html',data = group[0])

@app.route('/Student', methods=['POST'])
def addstud() -> "str":
    if request.method =="POST":
        name = request.form['surname']
        sex = request.form['sex']
        group = request.form['group']
        inst.Instdate.addStud(name,sex,group)
    return render_template('Registr.html')

@app.route('/UpdStudent',methods=['POST','GET'])
def upd_student()->'html':
    data = Select.Select.select(2)
    return render_template('UpdStud.html',data=data[0]);

@app.route('/UpdStud',methods=["POST"])
def upd_std() -> 'html':
    Update.Update.stud(request.form['oldstd'],request.form['new'])
    return render_template('UpdStud.html');



#GROUP
@app.route('/AddGroup')
def add_group()->'html':
    return render_template('Add_group.html')


@app.route('/Group', methods=['POST'])
def group() -> "str":
    if request.method =="POST":
        gr =  request.form['group']
        inst.Instdate.add(gr,1)
    return render_template('Add_group.html')


@app.route('/UpdGroup')
def upd_group()->'html':
    group = Select.Select.select(1)
    return render_template('UpdGroup.html',data = group[0]);


@app.route('/Ugroup',methods=['POST'])
def u_group()->'html':
    if request.method == "POST":
        gr = request.form['oldgr']
        new_name = request.form['new']
        Update.Update.group(gr,new_name)
    group = Select.Select.select(1)
    return render_template('UpdGroup.html', data=group[0])


#SUBJECT
@app.route('/AddSubject')
def add_Subject()->'html':
   return render_template('Add_sub.html')

@app.route('/Successfully', methods=['POST'])
def db() -> "str":
    if request.method =="POST":
        sub= request.form['subject']
        inst.Instdate.add(sub,0)
    return render_template('Add_sub.html')

@app.route('/UpdSubject')
def upd_Subject()->'html':
    subject = Select.Select.select(0)
    return render_template('UpdSub.html', data=subject[0]);

@app.route('/Updsub',methods=['POST'])
def u_sub()->'html':
    if request.method == "POST":
        sub = request.form['oldsub']
        new_name = request.form['new']
        Update.Update.subject(sub,new_name)
    sub = Select.Select.select(1)
    return render_template('UpdSub.html', data=sub[0])

#MARK

@app.route('/AddMark')
def add_mark()->'html':
    stud = Select.Select.select(2)
    return render_template('AddMark.html',data = stud[0])

@app.route('/Mark',methods=["POST","GET"])
def add_M()->'html':
    fio = request.form['group']
    data = Select.Select.select(0)
    group =Select.Select.sql_group(fio,0)
    return render_template('Mark.html',fio = fio, data = data[0],group=group)

@app.route('/SucsMark',methods = ["POST"])
def SAVE()->'html':
    mark = request.form['mark']
    gr = request.form['group']
    fio = request.form['fio']
    sub =request.form['sub']
    date = request.form['date']
    inst.Instdate.addMark(date,gr,fio,mark,sub)
    stud = Select.Select.select(2)
    return render_template('AddMark.html',data = stud[0])

@app.route('/Update')
def update()->'html':
    stud = Select.Select.select(2)
    return render_template('selectfio.html',data = stud[0])

@app.route('/update',methods = ['POST'])
def upd()->'html':
    fio = request.form['group']
    data = Select.Select.sub_mark(fio)#mark,id_sub
    sub = Select.Select.select(data[0],0)
    group = Select.Select.sql_group(data[1], 0)
    return render_template('newmark.html', fio=fio, data=data[0], group=group)


@app.route('/Select')
def ustdsel()->'html':
    stud = Select.Select.select(2)
    return render_template('SelectStudent.html',data = stud[0])

@app.route('/SelectSub')
def subdsel()->'html':
    stud = Select.Select.select(0)
    return render_template('selectSub.html',data = stud[0])





#subject


#Group


#student










@app.route('/UpdMark')
def upd_mark()->'html':
    return render_template('Estimatiom.html');


app.run(debug=True)
