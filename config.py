# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:27:05 2017

@author: Daniel
"""
import os
from configparser import ConfigParser

configtemplate = '''# hodea review minder cfg file

[minder_cfg]

# !!! USE INDENTIONS FOR MULTILINE OPTIONS !!!
# !!! Option Seperator: EOL or ";" !!!
;-----------------------------------------------------------------
# Project Name

name = insert project name here

;-----------------------------------------------------------------
# File types, which has to be parsed

filetype = .c;.h;.cpp

;-----------------------------------------------------------------
# exclude path
# all sub-directories will be excluded as well

exclude =  ./review_minder


;-----------------------------------------------------------------

'''
########################################################
# Function: 
# read & handle config file
########################################################
def read_config(cfgfile):
    
    config = ConfigParser()
   
    flog = open(cfgfile, 'rb')
    config.read(cfgfile)
    flog.close()
    return config
    
    
########################################################
# Function: 
# create config if not availeable and call read database
########################################################
def Getconfig(topdir):

    if not (os.path.isdir(topdir + r'/review_minder')):
        os.mkdir(topdir + r'/review_minder')
    if not (os.path.exists(topdir + r'/review_minder/minder.cfg')):
        flog = open(topdir + r'/review_minder/minder.cfg', 'w')   
        flog.write(configtemplate) 
        flog.close()  
         
    return read_config(topdir + r'/review_minder/minder.cfg')
    
    