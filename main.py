# Data Types in Python
from pyscript import display

# Str
fullname = 'Luis Ezekiel Valdez Bacay'  

# Int
age = 15  

# Int
He1ght = 167  

# List
Count_ries = ['Korea', 'France', 'and Canada'] 

# Bool
student_type = False 

# Dict
student_profile = {
    'color': 'Red',
    'car_brand': 'Ford',
    'shoe_size': 10,
    'best_friend': 'Joel'
} 

# Set 
favorite_fruits = {'Kiwi', 'Apple', 'Banana', 'Strawberry', 'Grape'} 

# Tuple
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 


# Displaying f-strings
display(f"Hello! My name is {fullname}.", target='output1')
display(f"I am {age} years old and {He1ght}cm tall.", target='output1')
display(f"New student: {student_type}.", target='output1')
display(f"The countries I want to visit are {Count_ries}.", target='output1')
display(f"My favorite color is {student_profile['color']}.", target='output1')
display(f"My car brand is {student_profile['car_brand']}.", target='output1')
display(f"My shoe size is {student_profile['shoe_size']}.", target='output1')
display(f"My best friend is {student_profile['best_friend']}.", target='output1')
display(f"My favorite fruits are {favorite_fruits}.", target='output1')
display(f"The days of the week start are {days_of_week}.", target='output1')
