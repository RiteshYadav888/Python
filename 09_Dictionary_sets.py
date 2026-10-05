# Dictionary......
marks = {
    "Ritesh": 100,
    "Nikhil": 56,
    "Piyush": 24,
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ritesh": 99, "Harry": 100})
print(marks)
print(marks.get("Harry")) #print NONE...
print(marks["Harry"])  #returs error...


# Sets.....
s1 = {1, 5, 3, 45, 98, 68}

print (s1, type(s1))
s1.add(76)
print(s1)
s1.remove(5)
print(s1)

s1 = {1, 5, 3, 45, 98, 68}
s2 = {1, 5, 7, 456, 89, 44}

print(s1.union(s2))
print(s1.intersection(s2))

words = {
    "maddad": "Help",
    "billi": "Cat",
    "kutta": "Dog"
}

word = input("Enter the word you want meaning of: ")
print(words[word])

s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)