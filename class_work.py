import os
os.system('clear')



# Task 1 - it works

print('Task 1')
users = [
    {
        'name': 'Holly',
        'type': 'Student',
        'password': 'hunter',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': True
            },
            {
                'title': 'Python basics',
                'completed': False
            }
        ]
    },
    {
        'name': 'Peter',
        'type': 'Student',
        'password': 'pan',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': False
            }
        ]
    },
    {
        'name': 'Luke',
        'type': 'Student',
        'password': 'skywalker',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': True
            }
        ]
    },
    {
        'name': 'Janis',
        'type': 'Teacher',
        'password': 'joplin'
    }
]

def show_registration(username, password, modulename):
    user = next((u for u in users if u['name'] == username and u['password'] == password), None)
    if not user:
        print(f'You did not register to the module {modulename}')
        return
    
    if user['type'] == 'Teacher':
        print('You are a teacher')
        return
    
    if user['type'] == 'Student':
        for module in user.get('modules', []):
            if module['title'] == modulename:
                print(f'You are registered to the module {modulename}')
                return
        
    print(f'You did not register to module {modulename}')

username = input('What is your username? ')
password = input(f'Type the password for username {username}: ')
modulename = input('What module do you want to check? ')



# Task 2 - it works

print('\nTask 2')

def has_completed_module(username, password, modulename):
    user = next((u for u in users if u['name'] == username and u['password'] == password), None) 
    if not user or user['type'] == 'Teacher':
        return
    
    if user['type'] == 'Student':
        for module in user.get('modules', []):
            if module['title'] == modulename:
                if module.get('completed'):
                    print(f'You have completed the module {modulename}')
                else:
                    print(f'You did not complete the module {modulename}')
                return

    print(f'You did not complete the module {modulename}')

username = input('What is your username? ')
password = input(f'Type the password for username {username}: ')
modulename = input('What module do you want to check? ')
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)



# Task 3 - it works

print('\nTask 3')


users = [
    {
        'name': 'Holly',
        'type': 'Student',
        'password': 'hunter',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': True
            },
            {
                'title': 'Python basics',
                'completed': False
            }
        ]
    },
    {
        'name': 'Peter',
        'type': 'Student',
        'password': 'pan',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': False
            }
        ]
    },
    {
        'name': 'Luke',
        'type': 'Student',
        'password': 'skywalker',
        'modules': [
            {
                'title': 'Computer basics',
                'completed': True
            }
        ]
    },
    {
        'name': 'Janis',
        'type': 'Teacher',
        'password': 'joplin'
    }
]


modules = [
    {
        'name': 'Computer basics'
    },
    {
        'name': 'Python basics',
        'requirement': 'Computer basics'
    },
    {
        'name': 'Django',
        'requirement': 'Python basics'
    }
]


def has_no_requirement(modulename):
    module = next((m for m in modules if m['name'] == modulename), None)     # Look for the module in the modules list by its name
    return module and 'requirement' not in module                            # Check if the module exists and does not have a 'requirement' key

def meets_requirement(user, requirement):
    for module in user.get('modules', []):                                   # Iterate through the user's modules to check if the requirement is met    
        if module['title'] == requirement and module.get('completed'):       # If the module title matches the requirement and it's completed, return True
            return True
    return False                                                             # If no matching and completed module is found, return False
    
def may_enroll(username, password, modulename):
    user = next((u for u in users if u['name'] == username and u['password'] == password), None)# Look for the user in the users list by username and password
    if not user:                                                                                # If the user is not found, check if the module has no requirement
        return has_no_requirement(modulename)
    
    if user['type'] == 'Teacher':                                            # If the user is a Teacher, they cannot enroll in modules
        return False
    
    if user['type'] == 'Student':                                            # If the user is a Student
        for module in user.get('modules', []):                               # Check if the student is already enrolled in the module
            if module['title'] == modulename:
                return False        
        module = next((m for m in modules if m['name'] == modulename), None) # Look for the module in the modules list by its name        
        if not module:                                                       # If the module is not found, return False
            return False
        if 'requirement' not in module:                                      # If the module has no requirement, the student may enroll
            return True
        
        requirement = module['requirement']                                  # Get the module's requirement and check if the student meets it
        
        return meets_requirement(user, requirement)                          # Return the result of the meets_requirement function
    return False                                                             # If the user type is not recognized, return False
    

username = input('What is your username? ')
password = input(f'Type the password for username {username}: ')
modulename = input('What module do you want to check? ')
if may_enroll(username, password, modulename):
    print(f'You may register to the module {modulename}.')
else:
    print(f'You may not register to the module {modulename}.')