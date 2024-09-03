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

studentId ={

    2002070 : "sadman sakib",
    2002069 : "rafil",
    2002068 : "deba",
    2002065 : "toukir",
}
print(studentId[2002069])

