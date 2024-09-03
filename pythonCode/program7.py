num =[10,20,30,40,50]
#print(num)

sum = 0
for s in num:
    sum = sum + s
print(sum)
"""
index=0
while index<5:
    print(num[index])
    index=index +1
"""

n=int(input("Enter the last number :"))
sum=1
for i in range(1,n+1,1):
    sum = sum * i
print(sum)

n=3
for i in range(n+1):
    print((2*i-1)*"*")


numOfWords=0
numOfLetters=0
numOfDigits=0

text= input("Enter a text of numbers : ")

for x in text:
        x=x.lower()
        if x >='a' and x <='z':
            numOfLetters = numOfLetters+1
        elif x >='0' and x <='9':
            numOfDigits =numOfDigits+1
        elif x == ' ':
            numOfWords=numOfWords+1

print(numOfWords)
print(numOfLetters)
print(numOfDigits)


