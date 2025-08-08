print("/___|")
print("   /|")
print("  / |")
print(" /  |")

character_name = "Tom"
character_age = "5"

print("There once was a man named "+character_name+", ")
print("He was "+ character_age +" years old")
character_age = "9"
print("he really liked the name : "+ character_age +",")
print("but didn't Like being 35.")

pharse = "bernia PJademy"
print(pharse.upper().isupper())
print(len(pharse))
print(pharse[0])
print(pharse[5])
int(pharse.index("P"))
print(pharse.replace("bernia","Elephant"))

print(-2.556596)
print(3 + 6.5 )
print(5 * 48.2)
print(10 % 3)
my_num = 5
print(my_num)
print(str(my_num)+ "My favourite number")

print(pow(2,5))
x = -8
print(abs(x))

print(round(3.5))

from math import *
print(floor(3.5))
print(ceil(6.4))
print(sqrt(36))

# getting input from users
#name = input("Enter your name : ")
#age = input("Enter your age : ")
#print("hello "+ name + " !  You are " + age)

#Building a basic calculator
num1 =  input("Enter a number: ")
num2 =  input("Enter another number: ")
result = int(num1) + int(num2)
print(result)

#Mad lips game

color = input("Enter a color : ")
plural_noun = input("Enter Plural Noun : ")
celebrity = input("Enter a celebrity : ")

print("Roses are "+ color)
print(plural_noun+" are blue ")
print("I love "+ celebrity)

# Lists
friends  = ["John", "Joey", "John", "Joey","oamni"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[-2])
print(friends[1 :])
print(friends[:3])
friends[1] = "sudu"
print(friends[1])

#List functions
lucky_number =  [4,6,7,9,3,4,5,1]
friends = ["uijed","vbijd","rhefd","yerjd"]
friends.extend(lucky_number)
print(friends)
friends.append("cred")
print(friends)
lucky_number.sort()
print(lucky_number)
friends.sort()

# Tupples
coordinates = [(4, 5),(5,9),(2,9)]
print(coordinates[1])

#functiins
def say_hi():
    print("hellow user")


print("Top")
say_hi()
print("bottom")

def say_hi(name):
    print("Hello " + name)

say_hi("Mike")

#Return statement
def cube(num):
    return num**3
print(cube(5))

def cube (num):
    return num*num*num

result =cube(5)
print(result)

#If statements
is_male = True
if is_male:
    print("You are a male")
else:
    print("You are a female")

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male or tall")
elif is_male and is_tall:
    print("You are a male or short")
else :
    print("You are a female or tall")

# if statement & comparisions