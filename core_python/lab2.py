#div function
def div(a,b):
    if b!=0:
        result=a/b
        return print(f"the division of {a} by {b} is {result}")
    else:
        print("the division is not possible")
div(4,2)


#square function
def square(a):
    result=a*a
    return print(f"the square of the number {a} is {result}")
square(2)


#accept a name from user and display it in lowercase
name=input("enter your name")
print("Your name in lowercase is ",name.lower())


#find the max and min of the random numbers:
import random

#generate 5 random numbers
numbers=[random.randint(1,100) for i in range(5)]
print("random numbers:",numbers)

#display max and min numbers
print("maximum numbers is ",max(numbers))
print("minimum of numbers is",min(numbers))


#labda function
#define lambda function
check_sign=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"

#test_function
print(check_sign(10))
print(check_sign(-2))
print(check_sign(0))
