import json

with open('user.json') as user_file:
    file_contents = user_file.read()

print(file_contents)

parsed_json = json.loads(file_contents)