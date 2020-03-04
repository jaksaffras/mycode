#!/usr/bin/env python3

#open file in read mode

with open('dnsservers.txt','r') as dnsfile:
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        svr = svr.rstrip('\n') #remove new line if exists

        if svr.endswith('org'):
            with open('org-domain.txt','a') as srvfile:
                srvfile.write(svr + '\n')
        elif svr.endswith('com'):
            with open('com-domain.txt','a') as srvfile:
                srvfile.write(svr + '\n')


