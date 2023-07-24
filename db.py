# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:12:59 2021

@author: HOME
"""

import pymysql as p


def connect():
    return p.connect(user="root",host="localhost",password="",database="mytododb")


def insert_task(t):
    try:
        db = connect()
        cr = db.cursor()
        sql = "insert into mytodo_table(task_name,task_description,task_deadline) values(%s,%s,%s)"
        cr.execute(sql,t)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()
        
        
def get_full_table():
    
    try:
        db = connect()
        cr = db.cursor()
        sql = "select si_no,task_name,task_description,date_format(task_deadline,'%d/%m/%Y  %I:%i %p') from  mytodo_table;"
        cr.execute(sql)
        tasks = cr.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()
        
        
def get_specific(t):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from mytodo_table where si_no=%s"
        cs.execute(sql,t)
        task = cs.fetchone()
        return task
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()      
       
        
def update_task(t):
    try:
        db = connect()
        cr = db.cursor()
        sql = "update mytodo_table set task_name=%s, task_description=%s, task_deadline=%s where si_no=%s" 
        cr.execute(sql,t)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()   

 
def delete_task(t):
    try:
        db = connect()
        cr = db.cursor()
        sql = "delete from mytodo_table where si_no=%s"
        cr.execute(sql,t)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()

    
def get_full_sorted_table():
    try:
        db = connect()
        cr = db.cursor()
        sql = "select task_name,task_description,date_format(task_deadline,'%d/%m/%Y  %I:%i %p') from mytodo_table where task_deadline>now() order by task_deadline"
        cr.execute(sql)
        tasks = cr.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()

        
def progress_rate():
    try:
        db = connect()
        cr = db.cursor()
        sql="select task_name,task_description,date_format(task_deadline,'%d/%m/%Y  %I:%i %p') from mytodo_table where task_deadline<now()"
        cr.execute(sql)
        tasks = cr.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()


def onlytime():
    try:
        db = connect()
        cr = db.cursor()
        sql="select date_format(task_deadline,'%I:%i %p') from mytodo_table where task_deadline>now() order by task_deadline"
        cr.execute(sql)
        tasks = cr.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()


def onlynamedesc():
    try:
        db = connect()
        cr = db.cursor()
        sql="select task_name,task_description from mytodo_table where task_deadline>now() order by task_deadline"
        cr.execute(sql)
        tasks = cr.fetchall()
        return tasks
    except:
        return False
    finally:
        db.close()


        