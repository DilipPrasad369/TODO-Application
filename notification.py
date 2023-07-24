# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:27:08 2021

@author: HOME
"""

from win10toast import ToastNotifier
import time
import db
 

hr=ToastNotifier()

moment=db.onlytime()
print(moment)
content=db.onlynamedesc()
print(content)


for i in range(len(moment)):
    while True:
        cur_time=time.strftime("%I:%M %p")
        if cur_time==str(moment[i][0]):
            hr.show_toast(content[i][0],content[i][1],icon_path="C:\\Users\\HOME\\Downloads\\Mkho-Christmas-Bell.ico") 
            print(cur_time)
            break
        else:
            pass







    