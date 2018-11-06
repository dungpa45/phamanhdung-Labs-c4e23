import pyexcel
from collections import OrderedDict



#2 chuan bij du lieu

a_list_of_dictionaries =[
    OrderedDict({
        "Name": 'Adam',
         "Age": 28
    }),
    OrderedDict({
        "Name": 'lucas',
         "Age": 28
    }),
    OrderedDict({
        "Name": 'alex',
         "Age": 28
    }),
    OrderedDict({
        "Name": 'eva',
         "Age": 28
    }),
]

#list comprehension

#3 luu file su dung save_as()
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xlsx")
