#Add and remove student names from a list
students = ["Alice", "Bob", "Charlie"]
# Add a student
students.append("David")
# Remove a student
students.remove("Bob")
print("Updated student list:", students)


# Create a list of even numbers from 1 to 20
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)


# Find the average of marks from a list
marks = [75, 80, 90, 60, 85]
average = sum(marks) / len(marks)
print("Average marks:", average)


#Check if a product is available in a shopping cart
shopping_cart = ["milk", "bread", "butter", "eggs"]
product = "bread"
if product in shopping_cart:
    print(f"{product} is available in the cart.")
else:
    print(f"{product} is not in the cart.")


#Count how many times a name appears in a list
names = ["Alice", "Bob", "Alice", "Charlie", "Alice"]
name_to_count = "Alice"
count = names.count(name_to_count)
print(f"{name_to_count} appears {count} times in the list.")

#Split a given list into two parts where the first part has a specified length
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3
part1 = original_list[:split_length]
part2 = original_list[split_length:]
print("Splitted the list into two parts:")
print(part1, part2)

