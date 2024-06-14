'''
working with lists
car_brands = ['BMW', 'Audi', 'Volkswagen']
for brand in car_brands:   # loop over all items in the list
  print(brand)
car_brands.append('Volvo') # adding an item to the listr
car_brands.pop(0)          # removing the first item from the list

# working with dictionaries
fruits = {'red': ['apple', 'cherry', 'strawberry'],
          'orange':['orange', 'mango', 'peach'],
          'yellow': ['banana', 'lemon']}
fruits['green'] = ['watermelon']            # adding a new key-value pair
fruits.update({'green': ['watermelon']})    
fruits.pop('yellow')                        # removing a key-value pair
for color, colored_fruits in fruits.items():# loop over all key-value pairs in the dictionary
  print(color + ' fruits:')
  for fruit in colored_fruits:
    print('- ' + fruit)

## Tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple[0])  # prints 1
print(my_tuple[2])  # prints 3
'''


# Task 1 - Validate the input credentials of a user. You should print the message `Welcome, {username}!` if the credentials are valid 
# and the message `Credentials are invalid` if they are not.
print("Task 1")
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}

if username == valid["username"] and password == valid["password"]:
    print(f"Welcome, {username}!")
else:
    print("Credentials are invalid")



# Task 2 - Define a function named `isweekend` that accepts a parameter named `date` of type `Datetime` (with a default value of `datetime.datetime.now()`).
print("\nTask 2")
import datetime
def isweekend(date=datetime.datetime.now()):
    if date.weekday() in [5, 6]:
        return True
    return False

print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))



# Task 3 - We now want a version of the first task, that will implement an "open doors" policy on the weekends. 
# So, if the user credentials are valid, or the date is on the weekend, the conditional should evaluate to `True` and greet the user.


username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime.date(2021, 8, 6)
if username == valid["username"] and password == valid["password"] or isweekend(today):
    print(f"Welcome, {username}!")
else:
    print("Credentials are invalid")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
today = datetime.date(2021, 8, 7)
if username == valid["username"] and password == valid["password"] or isweekend(today):
    print(f"Welcome, {username}!")
else:
    print("Credentials are invalid")




# Task 4 - Now define a function named `get_user` with the input arguments `username` and `password`, both as a `String`.
# There is a global variable named `users` as a list of dictionaries:
# The function should return the first dictionary in the list `users` matching the `username` and `password` provided. If no user matches, it should return `None`.
# When the user provided is invalid (when `get_user` returned None) the function should show the message `An error occurred. You are not authorized.`.
#> Do nothing if the user is valid.
#> Use the "truthy" and "falsy" nature of the Non-boolean values returned by `get_user`.

print("\nTask 4")
users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]


def get_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return None

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
user = get_user(username, password)
if user:
    print(f"Welcome, {username}!")
else:
    print("An error occurred. You are not authorized.")



# Task 5 - Now define a function named `show_offers` that accepts, again, a `username` and `password` as `Strings`.
# This function will print a message if the user is a Student or anonymous (the `get_user` function returned None) saying 
# `We have great courses to offer you!`. If the user is a Teacher it should do nothing.
# > Reuse the `get_user` function from before.
# > Use a single conditional (use functions to simplify it or make it more readable).
# > Use short-circuiting to avoid errors.

print("\nTask 5")
def show_offers(username, password):
    user = get_user(username, password)
    #if not user or user["type"] == "Student":    # One issue here , you need Ensure 'user' is not None before checking type
    if not user or (user and user["type"] == "Student"):
        print("We have great courses to offer you!")

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
show_offers(username, password)
