#!/usr/bin/env python3

round = 0
answer = ''
while round <3 and answer.lower() != 'brian':
    round +=1
    print ('Finish the movie title, \"Monty Python\'s The Life of _____\"\n')
    answer = input('Try your luck here-->: ')
    if answer.lower() == 'brian':
        print('Whoa! look at you!')
    elif round == 3:
        print('Always look on the bright side of life.\nBut not right now you\'re just wrong.\n')
    else:
        print('Your mother was a hamster and your father smelt of elderberries! Try again.\n\n')



