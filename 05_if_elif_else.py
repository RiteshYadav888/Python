age = 18

if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")




    ##  elif.....
marks = int(input("Enter your Marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


##marks Pass Fail.......
marks = int(input("Enter Your Marks: "))

if marks > 90:
    print("Grade A")
elif marks >= 60:
    print ("Grade B")
    marks >= 40
    print("Grade C")
else:
    print("Fail")



##age is greater then 18 or not.....
a = int(input("Enter your age: "))

if(a >= 18):
    print("You are above the given age")
    print("Good for You")
else:
    print("You are not above the given age")


age = int(input("Enter your age: "))

if(age >= 18):
    print("Yes")

else:
    print("No")

##Greatest number......
a1 = int(input("Enter number 1; "))
a2 = int(input("Enter number 2; "))
a3 = int(input("Enter number 3; "))
a4 = int(input("Enter number 4; "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)

##percentage pass/fail........
marks1 = int(input("Enter Marks 1; "))
marks2= int(input("Enter Marks 2; "))
marks3 = int(input("Enter Marks 3; "))

#check for totle percentage........
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage and marks1>33 and marks2>33 and marks3>33):
    print("You are Passed:", total_percentage )

else:
    print("You are Failed,try again next year:", total_percentage)


##scamer detect......
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This message is spam")

else:
    print("This message is not spame")


##username contain 10 charaxters or not.......
name = input("Enter your name: ")

if (len(name)<10):
    print("Your name is contains less then 10 characters")

else:
    print("Your name is contains more then 10 characters")

##name present in list or not.........
list = ["Ritesh", "Nikhil", "Arpit", "Prince"]

name  = input("Enter your name: ")

if(name in list):
    print("Your name is in list")

else:
    print("Your name is not is list")


#WAP to print carde according to marks.......
marks = int(input("Enter Your Marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex" 
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your Garde is:", grade)

