#1. FindLeap Year of a number

print("Find Year is leap year or not")
year = int(input("Enter a Year: "))

if (year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


#2. Find largest of three numbers

print("Find largest of three numbers")
num1,num2,num3 = int(input("Enter a number: ")),int(input("Enter a number: ")),int(input("Enter a number: "))

if(num1>num2):
    if (num1>num3):
        print(num1,"is largest")
    else:
        print(num3,"is largest")
else:
    if (num2>num3):
        print(num2,"is largest")
    else:
        print(num3,"is largest")

#3. Find odd or even of a given number
        
print("odd or even")

chknum =int(input("Enter a numb: "))

if (chknum%2==0):
    print(chknum ,"is even")
else:
    print(chknum ,"is odd")

#4. Find summing numbers using while loop

n=int(input("enter a num: "))
i=1
sum=0

while i<=n:
    sum=sum+i
    i +=1
print("sum of nth number of",n,"is",sum)


#5. Find Countdown of a number using while loop
i=0

cnum=int(input("Number to count: "))
cdown=cnum

while i<=cnum:
    print(cdown)
    cdown -=1
    i +=1

#6. Write a program to create a list of fruits and copy only 'e' letter fruits to the new list

fruits=[]
newFruits=[]
get="nan"

print("Enter fruits name one by one, when You are done blank enter")
while (get!=""):
    get=input("Enter a Fruit: ")
    if(get!=""):
        fruits.append(get)
print(fruits,"oldFruits")

#fruits with e

for x in range(0,len(fruits)):
    if("e" in fruits[x]):
        newFruits.append(fruits[x])
print(newFruits,"newFruits")

#7. ⁠write program to find prime number or not

chkpri = int(input("enter a num: "))

if chkpri > 1:
    for i in range(2,int(chkpri/2)+1):
        if (chkpri % i) == 0:
            print(chkpri, "is not a prime number")
            break
    else:
        print(chkpri, "is a prime number")
else:
    print(chkpri, "is not a prime number")


