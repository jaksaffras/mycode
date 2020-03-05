#!/usr/bin/env python3

with open('vlanconfig.cfg','r') as f:
    clist = f.readlines()
    for x in clist:
        print(x.strip())
