# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:15:45 2021

@author: HOME
"""

from flask import Flask,render_template,request
import db


app = Flask(__name__)


@app.route("/homepage")
def home():
    return render_template("homepage.html")


@app.route("/addtask")
def inserttask():
    return render_template("inserttask.html")


@app.route("/inserttask_data", methods=["POST"])
def inserttask_data():
    name=request.form["name"]
    desc=request.form["description"]
    deadline=request.form["deadline"]
    t=(name,desc,deadline)
    
    if db.insert_task(t):
        return render_template("inserttask.html")
    else:
        return "Exception occurred"


@app.route("/fulldbtable")
def fulltable():
    tasks=db.get_full_table()
    
    if tasks==False:
        return "Exception occured"
    else:
        if not len(tasks)>0:
            return render_template("addnewtask.html",data="add new task")
        else:
            return render_template("fulltable.html",data=tasks)
 
    
@app.route("/upcominglines")
def fulltablesorted():
    tasks=db.get_full_sorted_table()
    
    if tasks==False:
        return "Exception occurred"
    else:
        if not len(tasks)>0:
            return render_template("nosuchdeadlinepresent.html",data="no such deadline present")
        else:
            return render_template("fulltablesorted.html",data=tasks)


@app.route("/task")
def task():
    tasks=db.get_full_table()
    if tasks==False:
        return "Exception occurred"
    else:
        if not len(tasks)>0:
            return render_template("notasktoedit.html",data="no task to edit")
        else:
            return render_template("task.html",data=tasks)
 
    
@app.route("/updatetask/<si_no>")
def updatetask1(si_no):
    t=(int(si_no),)
    task=db.get_specific(t)
    
    if task == False:
         return "Exception occurred"
    else:
        return render_template("updatetask2.html",data=task)

    
@app.route("/updatetask3/<si_no>",methods=["POST"])
def updatetask3(si_no):
    name=request.form["name"]
    desc=request.form["description"]
    deadline=request.form["deadline"]
    t=(name,desc,deadline,int(si_no))
    
    if db.update_task(t):
        return render_template("task.html",data=db.get_full_table())####################
    else:
        return "Exception occurred"


@app.route("/deletetask/<si_no>")
def deletetask1(si_no):
    t=(si_no,)
    task=db.get_full_table()
    if db.delete_task(t):
        if not task==():
            return render_template("task.html",data=task)
        else:
            return render_template("notasktoedit.html",data="no task to edit")##################
    else:
        return "Exception occurred"
       
    

@app.route("/progress")
def uncomplete():
    task=db.progress_rate()
    if task==False:
        return "Exception occurred"
    else:
        if not len(task)>0:
            return render_template("alltaskcompl.html",data="all task completed")
        else:
            return render_template("fulltablesorted2.html",data=task)


app.run()


