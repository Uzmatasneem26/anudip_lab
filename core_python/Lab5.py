#count the number of times 4 appears in tuple
tuple=(1,2,3,4,4,4,7)
result=tuple.count(4)
print(tuple)
print(f"the maximum number of times number 4 occuring is :{result}")



#find the sum of the numbers in a list of tuples
tuple_list=[(1,2),(3,4),(5,6),(7,8)]
total_sum=sum(sum(t) for t in tuple_list)
print(total_sum)

#Iterate and display employee records stored in tuples
employee1=("john","hr",500000)
employee2=("jasmin","developer",600000)
employees=[employee1,employee2]
for emp in employees:
    print(f"\nName:{emp[0]}")
    print(f"Position:{emp[1]}")
    print(f"Salary:{emp[2]}")



#real-time example of simple billing example
num_products=int(input("enter the number of products"))#the number of products
products=[]#creating a list to store the products

for i in range (num_products):
    print(f"enter the product details")
    name=input("enter the name of the product:")
    price=float(input("enter the price of product:"))
    quantities=int(input("enter the number of quantities of product"))
    products.append((name,price,quantities))

#display the bill
print("display bill details")
total_amount=0

for product in products:
    name,price,quatities=product
    item_total=price*quantities
    total_amount+=item_total
    
print(f"{name}:{price} multiply {quatities}={item_total}")
print(f"total_amount:{total_amount}")

#convert list into tuple
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print("Output:", tuplex)


