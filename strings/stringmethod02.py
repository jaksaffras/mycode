#!/usr/bin/env python3

def main():
    '''Run-time code '''
    #create a small string
    lilstring = 'alta research offers classes on python coding'
    newlist = lilstring.split(' ')
    print(newlist)

    myiplist = ['192','168','0','12']
    singleip = '.'.join(myiplist)
    print(singleip)

# call our main functions
main()
