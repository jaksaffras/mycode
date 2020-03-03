#!/usr/bin/env python3

data = input('Please provide a numeric grade: ')


if data:
    try:
        data = float(data)
        if data >100 or data <0:
            print(f'The max possible score is 100. {data} is outside this range.')
        elif data <= 100 and data >=90:
            print(f'Letter grade for {data} is A.')
        elif data >=80 and data <90:
            print(f'Letter grade for {data} is B.')
        elif data >=70 and data <80:
            print(f'Letter grade for {data} is C.')
        elif data >=60 and data <70:
            print(f'Letter grade for {data} is D.')
        elif data <= 59:
            print(f'Letter grade for {data} is F. Uh-oh!')
        else:
            print(f'How did you get here?! {data} doesn\t make sense at all!')
    except ValueError:
        print(f'{data} is non-numeric! Was this a reading test?')

else:
    print('No input provided!')

print('Exiting... ')

