books = []

books.append("Learn C")
books.append("Learn Python")
books.append("Learn Java")
print(books)

books.pop()
print(books)

from collections import deque

bank = deque(["apple", "banana", "cherry"])
print(bank)
bank.popleft()
print(bank)

def add(a,b):
    sum= a+b
    print(sum)

add(20,80)
add(28,45)

def add(a,b):
    sum= a+b
    return sum
result = add(20,80)
print(result)

def student(*details):
    print(details[1])

student(101,"Sadman")
student(101,"Sadman",3.55)



