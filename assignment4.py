# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
person = [{'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'hiking']},
          {'name': 'Bob', 'age': 10, 'hobbies': ['gaming', 'cooking']},
          {'name': 'Charlie', 'age': 35, 'hobbies': ['swimming', 'cycling']}]
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [person['name'] for person in person]
# 3) Use a list comprehension to check whether all persons are older than 20.
all_older_than_20 = all([person['age'] > 20 for person in person])
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# person_copy = person[:]
person_copy = [p.copy() for p in person]
person_copy[0]['name'] = 'Alex'
# 5) Unpack the persons of the original list into different variables and output these variables.
person1, person2, person3 = person
print(person1)
print(person2)
print(person3)
# Output the results
print("Names:", names)
print("All older than 20:", all_older_than_20)
print("Original person:", person)
print("Modified copy:", person_copy)
