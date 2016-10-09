# -*- coding: utf-8 -*-

"""
Script Name : gitCommit.py
Author      : LURUI
Created	    : 4 April 2016
Version	    : 1.0
Description	: This simple script is to commit and push changes of my project to GitHub automatically.

"""


import os
import numpy as np
import subprocess
import time

workDir = 'C:/Users/Administrator/Desktop/sync/GitHub/Grand/'
os.chdir(workDir)
commitNum = np.random.randint(3,21)
fileType = ['.txt','.html','.md','.py']
print 'the program will make %s commits today!' %(commitNum)
for i in range(commitNum):
    typeNum = np.random.randint(0,4)
    fileName = np.random.randint(100,1000)
    path = workDir+str(fileName)+fileType[typeNum]
    with open(path,'wb') as code:
        code.close()
    print str(fileName)+fileType[typeNum]+' have been created!'
    gitShell = subprocess.Popen(workDir+'sync.sh',shell=True)
    print 'the new change is being commited and push, please wait a few seconds!'
    if gitShell.wait() == 0:
        os.remove(path)
        print str(fileName)+fileType[typeNum]+' have been deleted!'
print 'all changes have been committed!'
raw_input('press any key to exit!')