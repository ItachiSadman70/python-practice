i=1
while i<=10:
    print("i")
    i=i+1
print("Program end")

n=int(input("Enter a number: "))
sum = 0
i = 2
while i<=n:
    sum = sum+i
    i = i+2

print(sum)

subjects =["C","C++","Java","Python","C#","Html"]
print(subjects)
print(subjects[2:])
print("CSS" in subjects)
print(subjects + ["Flutter"])
print(len(subjects))
subjects.insert(2,"OS")
print(subjects)
subjects.pop()
print(subjects)

num=list(range(15))
print(num)


