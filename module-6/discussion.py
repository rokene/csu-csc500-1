#!/usr/bin/env python3

# initial list of users
users = [
    {
        "id": 1,
        "name": "Lindsey",
        "email": "lindsey@gmail.com",
        "age": 33
    },
    {
        "id": 2,
        "name": "Hazel",
        "email": "hazel@gmail.com",
        "age": 10
    },
    {
        "id": 3,
        "name": "Clark",
        "email": "clark@gmail.com",
        "age": 8
    },
]

print("\nList of users initially:")
for user in users:
    print(user)

# add a new user
new_user = {
    "id": 4,
    "name": "Ben",
    "email": "ben@gmail.com",
    "age": 3
}

users.append(new_user)

print("\nList of users after adding a user:")
for user in users:
    print(user)

# update user with id 2’s email to yahoo.
for user in users:
    if user["id"] == 2:
        user["email"] = "hazel@yahoo.com" 

print("\nList of users after updating a user:")
for user in users:
    print(user)

# remove a user by id
users = [user for user in users if user["id"] != 3]

print("\nList of users after removing a user:")
for user in users:
    print(user)
