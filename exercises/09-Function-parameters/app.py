# Your code goes here:
def render_person(name, DOB, eye_color, age , gender):
    # INSTEAD OF LINE 3 USE LINE 4 IN PYTHON return name + ' is a ' + str(age) + ' years old ' +gender + ' born in ' +DOB + ' with ' +eye_color 
    return f'{name} is a {str(age)} years old {gender} born in {DOB} with {eye_color} eyes'


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))