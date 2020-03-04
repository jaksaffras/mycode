#!/usr/bin/env python3
import uuid
qty = int(input('How many UUIDs should be generated? '))

print('Generating UUIDs...')

for r in range(qty):
    print(uuid.uuid4().int)

