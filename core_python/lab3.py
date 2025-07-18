#check if the number is a palindrome or not
def is_palindrome(text):
    text=text.lower().replace(" ","")
    return text==text[::-1]

s=input("enter a string")
print("palindrome"if is_palindrome(s) else "not a palindrome")

#count the number of vowels in a text
def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text :
        if char in vowels:
            count+=1
    return count
text=input("enter the text")
print("number of vowels:",count_vowels(text))


#replace all spaces in text with -
text=input("enter a text")
result=text.replace(" ","-")
print(result)

#check if a password has at least 8 character,one uppercase,one number
password=input("enter a password")
def is_valid(password):
    if len(password)<8:
        return False
    else:
        for char in password:
            if char.isupper():
                return True
            elif char.isdigit():
                return True
print(f"valid" if is_valid(password) else "not_valid")

#extract domain from email(user@example.com) in python
def extract_domain(email):
    # Split the email at '@' and take the second part
    return email.split('@')[1]

# Input from user
email = input("Enter your email: ")
print("Domain:", extract_domain(email))
