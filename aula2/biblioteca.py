class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.books = []
    
    def __str__(self):
        return f"{self.name} - {self.age}"
class Book:
    def __init__(self, title, year,authors=None):
        self.title = title
        self.year = year
        if (authors is None):
            self.authors = []
        else:
            self.authors = authors
    
    def __str__(self):
        return f"{self.title} - {self.year}"

# Programa

auth1 = Author("Jane", 33)
auth2 = Author("Taylor", 38)
auth1 = Author("Elena", 68)

#print(f"{auth1} = {auth1.books}")
#print(f"{auth2} = {auth2.books}")
#print(f"{auth3} = {auth3.books}")

b1 = Book("Orgulho e Preconceito", 1878, [auth1])
b2 = Book("Os Sete Maridos de Evelyn Hugo", 2016, [auth2])
auth1.books=[b1]
auth2.books = [b2]

print(f"{auth1} = {auth1.books}")
print(f"{auth2} = {auth2.books}")

