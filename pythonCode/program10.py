
def square(x):
    return x*x

num={1,2,3,4,5}

result= list(map(square,num))
print(result)


num={1,2,3,4,5,6}

result =list(filter(lambda x:x%2==0,num))
print(result)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(8))


file= open("student.txt","r+")

for line in file:
    print(line)

file.close()

file= open("student.txt","a")
file.write("\nI love you")
file.close()