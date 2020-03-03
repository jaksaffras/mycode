#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')
source = input('File to move: ')
destination  = input('New directory: ')

shutil.move(source,destination)
print('File moved successfully')



#xname = input('New file name: ')
#shutil.move('ceph_storage/kerrigan.obj','ceph_storage/' +xname)


