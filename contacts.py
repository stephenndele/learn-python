contacts = {
    "number":4,
    "students":[
        {"name": "John", "email":"john@example.com"},
        {'name': "kim", "email": "kim@example.com"},
        {'name': "steve", "email": "steve@example.com"},
    ]
}

for student in contacts["students"]:
    print(student['email'])