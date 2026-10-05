## for loop
for i in range(1, 21):
    print(i)

    ## Table By using for loop
for i in range(1, 11):
    print(f"{3} X {i} = {3*i}")

    ## For loop with else.....
l = [67, 69, 77, 33, 54]
for i in l:
    print(i)
else:
    print("Khatam Tataa Bye Bye........")

    # Break..... 
for i in range(100):
    if(i == 34):
        break  #//break the loop....
    print(i)

    #continue....
for i in range(100):
    if(i == 34):
        continue  #//skip perticuler item
    print(i)

    #JUMP print.....
for i in range(1, 40, 4):
    print(i)

    # For loops with lists.......
list = ["Hello", "Ritesh", "Bhai", "kya", "hall chall"]
for i in list:
    print(i)

    ## For loops with tuple.........
tuple = ("Ritesh","Shreya", "Diya", "Arpit", "Prince", 67, 69)
for i in tuple:
    print(i)

    ##For loops with strings......
str = "Ritesh"
for i in str:
    print(i)


##while loop....
    ##Incresing number....
i = 1
while i <=5:
    print(i)
    i += 1

    ##Decresing number.....
i = 10
while i >=1:
    print(i)
    i -= 1

    ##Table By using whileloop......
i = 1
while(i<11):
    print(f"{16} X {i} = {16*i}")
    i += 1

    ##printing lists........
l = ["Ritesh", "Fall", "in", "love", "with", "Shreya"]

i = 0

while (i<len(l)):
    print(l[i])
    i += 1



    ## Questions........
#WAP to print table of given number using for loop??

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

    ##if name starts with "S" greet them
list = ["Ritesh", "Shreya", "Arpit", "Prince"]

for name in list:
    if(name.startswith("S")):
        print(f"Hello {name}")

    #WAP to print table of given number using for whileloop??
n= int(input("Enter a number: "))

i = 1
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i += 1

    # WAP given number is prime or not
n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("The number is not Prime")
        break
else:
    print("The number is Prime")  



