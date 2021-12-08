import json
from csv import DictReader

with open("users-39204-8e2f95.json", "r") as file:
    users = json.loads(file.read())

with open("books-133064-871075.csv", newline='') as file:
    books = DictReader(file)

    books_list = []

    for row in books:
        temp_book = {
            'title': row['Title'],
            'author': row['Author'],
            'pages': int(row['Pages']),
            'genre': row['Genre']
        }
        books_list.append(temp_book)

result = []
count = 0

for row in users:
    temp_user = {
        'name': row['name'],
        'gender': row['gender'],
        'address': row['address'],
        'age': row['age'],
        'books': []
    }
    result.append(temp_user)

while count < len(books_list)-1:
    for row in range(len(result)):
        if count == len(books_list):
            break
        result[row]['books'].append(books_list[count])
        count += 1

with open('result.json', 'w') as file:
    res = json.dumps(result, indent=4)
    file.write(res)
