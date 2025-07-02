print("function without parameter")
def show():
    print("how are you")
show()#calling a function

print("function with a parameter ")
def sum_2numbers(a,b):
    result=a+b
    print(result)
sum_2numbers(5,2)

print("function with default parameter ")
def naming(name="uzma"):
    print(name)
naming("sabah")
naming()

print("function with return value - does not return none ")
print("variable length arguments")
#*args:used to pass multiple arguments as tuple
#**args:used to pass multiple value as key value pair

def sum_all(*numbers):
    return sum(numbers)
print(sum_all(11,12,13,14,15))

def person_details(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
person_details(name="uzma",age=22,city="bangalore")

print("lambda function")
#small one line function without arguments
#syntax:lambda argument:expression
result=lambda a,b:a*b
print(result(3,2))



