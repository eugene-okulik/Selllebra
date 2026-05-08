my_dict = {'tuple': (10, 20, 30, 40, 50),
    'list':['tea', 'milk', 'eggs', 'tomatoes', 'cucumbers'],
    'dict':{'rain': False, 'wind': False, 'sun': True, 'clouds': True, 'lightning': False},
    'set':{'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'}
    }
print(my_dict['tuple'][-1])
my_dict['list'].append('coffee')
my_dict['list'].pop(1)
my_dict['dict']['message'] = 'i am a tuple'
my_dict['dict'].pop('rain')
my_dict['set'].add('Saturday')
my_dict['set'].remove('Monday')

print(my_dict)
