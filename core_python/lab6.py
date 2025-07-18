#Write a Python program to Get Only unique items from two sets.
set1={1,2,3,4}
set2={3,4,5}
unique_items=set1.union(set2)
print("the unique elements are:",unique_items)

#Write a Python program to Return a set of elements present in Set A or B, but not both.
set1={1,2,3,4}
set2={3,4,5,6,7}
difference=set1.symmetric_difference(set2)
print(difference)

#Write a Python program to Check if two sets have any elements in common. If
set1={1,2,3,4}
set2={3,4,5}
intersetion_items=set1.intersection(set2)
print(intersetion_items)

#Write a Python program to Remove items from set1 that are not common to both set1 and set2.
set1={1,2,3,4}
set2={3,4,5}
intersection=set1.intersection(set2)
print(intersection)

#The list of unique visitors The list of unique visitors.
num_visitors=int(input("how many visitors visited the website"))
visitors=set()
for i in range (num_visitors):
    name=input("enter the name of the visitors")
    visitors.add(name)
print("the visitors name:",visitors)
print("the total number of visitors are:",len(visitors))
    
#hobbies of friends
rahul_hobbies = set(input("Enter the hobbies of Rahul (comma-separated): ").strip().lower().split(','))
ganesh_hobbies = set(input("Enter the hobbies of Ganesh (comma-separated): ").strip().lower().split(','))

print(f"Common hobbies are :{rahul_hobbies.intersection(ganesh_hobbies)}")
print(f"all hobbies are :{rahul_hobbies.union(ganesh_hobbies)}")
print(f"Hobbies unique to each friend:{rahul_hobbies.symmetric_difference(ganesh_hobbies)}")
