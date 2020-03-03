#!/usr/bin/env python3

ipChk = input('Please provide the IP Address: ')

if ipChk.startswith('192.'):
    print('IP Address provided is not recommended')
elif ipChk:
    print('IP Address provided:',ipChk)
else:
    print('No value provided.')

print('Exiting script')

