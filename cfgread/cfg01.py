#!/usr/bin/env python3

cfile = open('vlanconfig.cfg','r')
print(cfile.read())
cfile.close()


cfile = open('vlanconfig.cfg','r')
cfilelist = cfile.readlines()
print(cfilelist)

for x in cfilelist:
    print(x)

## no lines


print('Step 13: ')

cfile = open('vlanconfig.cfg','r')
cfileread = cfile.read()
cfilelist = cfileread.splitlines()

print(cfilelist)
cfile.close()


