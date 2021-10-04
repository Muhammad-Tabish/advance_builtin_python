friends =[

    {
        'name': 'Tabish',
        'location': 'karachi'
    },

    {
         'name': 'hammad',
          'location': 'islamabad',

    },

    {
        'name': 'atif',
        'location': 'karachi',


    },

    {
        'name': 'atif',
        'location': 'islamabad',

    }

]

your_location = input('enter your location: ')
friend_nearby = [friend for friend in friends if friend['location']== your_location]

if any(friend_nearby):
    print('your are not alone')
else:
    print('sorry')


print(all([ 1, 2 , 3, 4 ]))

