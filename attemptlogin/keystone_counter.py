#!/usr/bin/env python3

loginfail = 0 #counter for fails
# open file

with open('keystone.common.wsgi','r') as file:
    lines = file.readlines()
    for l in lines:
        if '- - - - -] Authorization failed.' in l:
            loginfail +=1

print('The number of failed login attempts is:',loginfail )
