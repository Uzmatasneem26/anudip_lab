#calculate the mean
dict_1={"a":6,"b":7,"c":8}
mean1=sum(dict_1.values())/len(dict_1)
print(f"mean:{mean1}")

'''conacatenate dictionaries to create a simple dictionary'''
dict_1={"a":6,"b":7,"c":8}
dict_2={"d":6,"e":7}
concatenate={**dict_1,**dict_2}
print(concatenate)


#get the key, value and item in a dictionary
dict_1={"a":6,"b":7,"c":8}

print("\n keys")
for key in dict_1.keys():
    print(key)
print("\n values")
for value in dict_1.values():
    print(value)
print("\n items")
for item in dict_1.items():
    print(item)


#get the key, value and item in a dictionary
input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

print("\n keys")
for key in input_dict.keys():
    print(key)
print("\n values")
for value in input_dict.values():
    print(value)
print("\n items")
for item in input_dict.items():
    print(item)


#real-time example of employee
employees={
    101:{"name":"alice","salary":80000,"dep":"it"},
    102:{"name":"roshan","salary":90000,"dep":"cse"},
    103:{"name":"alia","salary":70000,"dep":"aero"}}
emp_id=int(input("enter the employee id"))
if emp_id in employees:
    emp=employees[emp_id]
    print(f"Name:{emp['name']}")
    print(f"Salary:{emp['salary']}")
    print(f"Department:{emp['dep']}")
else:
    print("Employee not found!")
    
