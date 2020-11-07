from flask import Flask, request, render_template, redirect,send_file, make_response
from flask_pymongo import pymongo
import pymongo
from hashlib import sha256
import numpy as np

CONNECTION_STRING = "mongodb+srv://sanjana:sanjana@cluster0.wqgdc.mongodb.net/job?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)

db = pymongo.database.Database(client, 'job')
# col = pymongo.collection.Collection(db, 'job')

from flask import Flask
app = Flask(__name__,template_folder='templates',static_url_path='/static')

@app.route('/employee',methods=['GET','POST'])
def employee():
    if(request.form['employee']=='Employee'):
        return render_template('form.html')
    
@app.route('/employer',methods=['GET','POST'])
def employer():
    if(request.form['employer']=='employer'):
        return render_template('login2.html')
    
@app.route('/signup',methods=['GET','POST'])
def signup():
    if(request.form['signup']=='signup'):
        return render_template('emp_reg.html')
    
@app.route("/test2",methods=['POST','GET'])
def test2():
    if request.method == 'POST':
        name=request.form['name']
        phoneno=request.form['phoneno']
        city=request.form['city']
        username=request.form['username']

        pwd=request.form['pwd']
        hashedWord = sha256(pwd.encode('utf-8')).hexdigest()
#         exp=request.form['exp']
        role=request.form.get("role", None)
        col = pymongo.collection.Collection(db, 'employer')
        col.insert_one({"name": name,"Phoneno":phoneno,"City":city,"role":role,"username":username,"password":hashedWord})
#     col.insert_one({"name": "name","Phoneno":"phoneno","Experience":"exp","City":"city"})
        return render_template('thank2.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if(request.form['login']=='Login'):
        return render_template('login2.html')
    
@app.route('/login_sure',methods=['GET','POST'])
def login_sure():
    user=request.form['username1']
    pwd=request.form['password1']
    hashedpwd=sha256(pwd.encode('utf-8')).hexdigest()
    col = pymongo.collection.Collection(db, 'employer')

    d=col.find({"username":user,"password":hashedpwd},{"role": 1} )
    res = not bool(d)
    if(res==True):
        return render_template('login2.html',me="invalid username or password")
    else:
        rolee=""
        for element in d:
            rolee=element["role"]
            break
        labels={"Restaurant":"Restaurant","Carpenter":"Carpenter","Driver":"Driver","Barber":"Barber","House help":"HouseHelp"}
        st=labels[rolee]
        s=st+".html"
        col = pymongo.collection.Collection(db, st)

        Project_List_Col = col.find()
#         return render_template('Barber.html',tasks=Project_List_Col)
        return render_template(s,tasks=Project_List_Col)

@app.route("/test4",methods=['GET','POST'])
def test4():
    if(request.form['carpenterjob']=="Carpenterjob"):
        return render_template("job_desc.html")
        
@app.route("/test5",methods=['GET','POST'])
def test5():
    if(request.form['barberjob']=="Barberjob"):
        return render_template("job_desc.html")
    
@app.route("/test8",methods=['GET','POST'])
def test8():
    if(request.form['restaurantjob']=="Restaurantjob"):
        return render_template("job_desc.html")

@app.route("/test6",methods=['GET','POST'])
def test6():
    if(request.form['househelpjob']=="Househelpjob"):
        return render_template("job_desc.html")
    
@app.route("/test7",methods=['GET','POST'])
def test7():
    if(request.form['driverjob']=="Driverjob"):
        return render_template("job_desc.html")
    
    
@app.route("/test",methods=['POST','GET'])
def test():
    if request.method == 'POST':
        name=request.form['name']
        phoneno=request.form['phoneno']
        city=request.form['city']
        exp=request.form['exp']
        role=request.form.get("role", None)
        col = pymongo.collection.Collection(db, role)
        col.insert_one({"name": name,"Phoneno":phoneno,"Experience":exp,"City":city,"role":role})
#     col.insert_one({"name": "name","Phoneno":"phoneno","Experience":"exp","City":"city"})
        return render_template('thank.html')

@app.route("/jobdesc",methods=['POST','GET'])
def jobdesc():
    if request.method == 'POST':
        desc=request.form['desc']
        vac=request.form['vac']
        sal=request.form['sal']
        date=request.form['trip-start']
#         role=request.form.get("role", None)
        col = pymongo.collection.Collection(db, "job")
        col.insert_one({"desc": desc,"vac":vac,"sal":sal,"date":date})
#     col.insert_one({"name": "name","Phoneno":"phoneno","Experience":"exp","City":"city"})
        return render_template('thank3.html')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/seejobs2',methods=['POST','GET'])
def seejobs2():  
    if(request.form['seejobs2']=="Seejobs2"):
        col = pymongo.collection.Collection(db, "job")

        Project_List_Col = col.find()
        return render_template('alljob.html',tasks=Project_List_Col)
    
@app.route('/train',methods=['POST','GET'])
def train():
    return render_template("training.html")
    
@app.route('/seejobs',methods=['POST','GET'])
def seejobs():  
    if(request.form['seejobs']=="Seejobs"):
        col = pymongo.collection.Collection(db, "job")

        Project_List_Col = col.find()
        return render_template('alljob.html',tasks=Project_List_Col)
    
# @app.route('/Barber')
# def Barber():  
#         col = pymongo.collection.Collection(db, "Barber")

#         Project_List_Col = col.find()
#         return render_template('Barber.html',tasks=Project_List_Col)
    
# @app.route('/Carpenter')
# def Carpenter():  
#         col = pymongo.collection.Collection(db, "Carpenter")

#         Project_List_Col = col.find()
#         return render_template('Carpenter.html',tasks=Project_List_Col)
    
    
# @app.route('/HouseHelp')
# def HouseHelp():  
#         col = pymongo.collection.Collection(db, "HouseHelp")

#         Project_List_Col = col.find()
#         return render_template('HouseHelp.html',tasks=Project_List_Col)
    
# @app.route('/Restaurant')
# def Restaurant():  
#         col = pymongo.collection.Collection(db, "Restaurant")

#         Project_List_Col = col.find()
#         return render_template('Restaurant.html',tasks=Project_List_Col)
    
# @app.route('/Driver')
# def Driver():  
#         col = pymongo.collection.Collection(db, "Driver")

#         Project_List_Col = col.find()
#         return render_template('Driver.html',tasks=Project_List_Col)
 
@app.route('/barbert')
def barbert():  
        
        return render_template('Barbert.html')
    
@app.route('/carpentert')
def carpentert():  
        
        return render_template('carpentert.html')
    
    
@app.route('/househelpt')
def househelpt():  
        
        return render_template('HouseHoldt.html')
    
@app.route('/restaurantt')
def restaurantt():  
        
        return render_template('Restaurantt.html')
    
@app.route('/drivert')
def drivert():  

        return render_template('Drivert.html')
    
@app.route('/scroll')
def scroll():  

        return render_template('news_scroll.html')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)