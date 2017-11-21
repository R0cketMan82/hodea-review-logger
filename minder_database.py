# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:04:16 2017

@author: Daniel
"""

import json

jsonbody ='''{
"overview": [
{
"iopen": 0,
"iclosed": 0,
"irejected" :0,
"icomment": 0,
"imajor": 0,
"iminor": 0,
"iundefined": 0
}
],
"reviewitem": [
]
}'''
########################################################
# Function: 
# create database if not availeable 
# and call read database
########################################################                
def Getdb(topdir):


    dbdir = topdir + r'/review_minder/reviewlog.db'

    if not (os.path.isdir(topdir + r'\review')):
        os.mkdir(topdir + r'\review')
    if not (os.path.exists(dbdir)):
        flog = open(dbdir, 'w')   
        flog.write(jsonbody) 
        flog.close()  
         
    read_db()