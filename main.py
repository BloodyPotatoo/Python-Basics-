'''
#Its a remainder calculator
'''
input_1 = int(input("Enter a number: "))
input_2 = int(input("Enter a number: "))

print("The remainder is: ", input_1 % input_2)
'''
#Its a datatype calculator
'''
for i in range(5):
    User_input = input()
    print(type(User_input))
'''
#Its a string slicer
'''
a = input("Enter your name: ")
new_a = a[0:3]
print(new_a)

print(f"Your name is {a} and your shorter name is {new_a}")
'''
#Lists
'''
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print(fruits[0])
fruits[0] = "Grapes"
print(fruits[0])

fruits.append("Mango") #end of the list
print(fruits)
fruits.remove("Grapes") #remove
print(fruits)
fruits.sort() #sort
print(fruits)
fruits.insert(2,"Grapes")
print(fruits)
fruits.extend(["Kiwi", "Lemon"]) #add multiple items
'''
#Tuples
'''
a = (1, 2, 3, 4, 5)
print(a[0])
number = a.count(1) #how many times 1 is present in the tuple
print(number)
index = a.index(3) #index of 3
print(index)

b = (1,2)
c = b*3
print(c)

print(b+c+a)
print(2 in a) #check if 2 is present in the tuple
'''
#List to add
'''
a = [1, 2, 3, 4, 5]
print(sum(a))
'''
#Dictionary
'''
Price = {
    "coffee": 100,
    "Tea" : 50,
    "Juice": 150,
    "Water": 20
}

print(Price, type(Price))
print(Price["coffee1"]) # give none
print(Price.get("coffee1")) #give an error

print(Price.items())
print(Price.keys())
print(Price.values())

Price.update({"coffee": 99}) #update the price of coffee
print(Price)

Price.clear() #clear the dictionary
print(Price)
'''
#Sets
'''
a = {1, 2, 3, 4, 5, 5, 5}
print(a) #duplicate values are not allowed in sets
a.add(6) #add an element to the set
print(a)
a.remove(3) #remove an element from the set
print(a)
print(len(a)) #print the length of the set

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2)) #union of two sets
print(s1.intersection(s2)) #intersection of two sets
print(s1.difference(s2)) #difference of two sets
print(s2.difference(s1)) #difference of two sets
'''
#loops (For/while)
'''
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])

j = 0 
while j < len(l):
    print(l[j])
    j += 1

for i in range(10):
    if i == 5: #break loop when i is 5
        break
    print(i)
else:
    print("Done")

for i in range(10):
    if i == 5:
        continue # skip 5 and continoue with the next iteration
'''
#Functions
'''
def Add():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print("The sum is: ", a+b)

Add()

def Add2(a,b):
    print("The sum is: ", a+b)

Add2(5,5)

def Add3(a,b):
    print("The sum is: ", a+b)
    return(1) #now this def has a value can be store in a variable

x = Add3(5,5)
print(x)

def Add4(a,b = 2):
    print(a + b)

Add4(5) # b will take the default value of 2

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")
'''
#Files (Input/Output)
'''
#files are now named as Text.txt and Text3.txt so currently this will show an error but you cna fix this!
f = open("file.txt")
Data = f.read()
print(Data)
f.close()

new_data = Hi #use '''''' here
Varun here! its currently 2/15/2026 and i am cooking some code and learning python in advance
I have learnt python but now its time to level up.

Just Chill

a = open("file.txt", "w")
a.write(new_data)
a.close()

b = open("file.txt")
lines = b.readlines() #readlines will read the file line by line and return a list of lines
print(lines, type(lines))
b.close()

c = open("file.txt")
line1 = c.readline()
print(line1) #readline will read the file line by line and return a string of the line
line2 = c.readline()
print(line2)
line3 = c.readline()
print(line3)
line4 = c.readline()
print(line4)
line5 = c.readline()
print(line5)
c.close()

d = open("file.txt", "a")
st = "\nYou have been leveled up! Congrats!"
d.write(st) #append to the file
d.close()

with open("file.txt) as f # no need to close the file when using with statement
    data = f.read()
    print(data)
'''
#Classes and Objects
'''
class employee:
    language = "Python" #class variable
    salary = 100000 #class variable

varun = employee()
print(varun.language)

Arnab = employee()
Arnab.language = "Java" #object variable
print(Arnab.language)

class student:
    class_student = "10th"
    section_student = "D"
    def get_info(self):
        print(f"The student is in {self.class_student} and section is {self.section_student}")

Varun = student()
Varun.get_info()


class Anmie:
    def __init__(self): #dunder method (methods starts with __ and ends with __)
        season = "3"
        time = "1d 13h 28m 24s"
        print(f"The season is {season} and time is {time}")

DBZ = Anmie()

class cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"The car is {brand} and model is {model}")

BMW = cars("BMW", "X5")
'''
#Inheritance
'''
class employee:
    name = "Google"
    def get_info(self):
        print(f"The employee works in {self.name}")
class programmer(employee):
    name = "Microsoft"
    def get_info(self):
        print(f"The employee works in {self.name}")

a = employee()
b = programmer()
a.get_info()
b.get_info()

class coder:
    def __init__(self):
        print("Class coder is created")
    a = 1
class programmer(coder):
    def __init__(self):
        print("Class programmer is created")
    b = 2
class coder_programmer(programmer):
    def __init__(self):
        print("Class coder_programmer is created")
    c = 3
x = coder()
y = programmer()
z = coder_programmer()

print(x.a)
print(y.b, y.a)
print(z.c, z.b, z.a)
'''
#Match statements
'''
def number(n):
    match n:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case _:
            return "Unknown number"

print(number(6))
'''
