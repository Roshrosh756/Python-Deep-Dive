dictionary = {}
grades = {
    "Alice" : 85,
    "Bob" :90,
    "Charlie" : 78
    }
print(grades["Bob"])

grades["David"] = 92
grades["Alice"]= 81

for name, grade in grades.items():
    print(name, "->", grade)
