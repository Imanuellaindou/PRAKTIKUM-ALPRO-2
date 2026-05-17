from collections import OrderedDict
Lista = ['red', 'green', 'blue']
Listb = ['#FF0000', '#008000', '#0000FF']
color_dict = OrderedDict([
    ('green', '#008000'),
    ('blue', '#0000FF'),
    ('red', '#FF0000')
])
print(dict(color_dict))