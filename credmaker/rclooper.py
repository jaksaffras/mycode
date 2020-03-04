#!/usr/bin/env python3

import csv

f = open('csv_users.txt','r')

i = 0

for r in csv.reader(f):
    i+=1
    filename = 'admin.rc%d'%(i,)

    rcfile = open(filename,'w')

    print('export OS_IDENTITY_URL='  + r[0],file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3',file=rcfile)
    print('export OS_PROJECT_NAME='  + r[1],file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + r[2], file = rcfile)
    print('export OS_USERNAME=' + r[3], file = rcfile)
    print('export OS_USER_DOMAIN_NAME=' + r[4], file = rcfile)
    print('export OS_PASSWORD=' + r[5], file = rcfile)
    rcfile.close()
f.close()
