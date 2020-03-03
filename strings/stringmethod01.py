#!/usr/bin/env python3

# create a small string
lilstring = 'Alta 3 Research offers classes on Python coding'
newlist = lilstring.split(' ') # returns a list split on whitespace
print(newlist)

# create a list of strings
myiplist = ['192','168','0','12']
#set single ip as the result of joning the list myiplist around the '.'
singleip = '.'.join(myiplist)
print(singleip) #display singleip
