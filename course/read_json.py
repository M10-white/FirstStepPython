import json

with open('./data/user.json') as user_file:
    file_contents = user_file.read()
    user_json_dict = json.loads(file_contents)

print(f"Age : {user_json_dict['age']}")
print(f"Second hobbie : {user_json_dict['hobbies'][1]}")
print(f"Email : {user_json_dict['email']}")