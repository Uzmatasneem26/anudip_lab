#check if the number is a prime number or not
def is_prime(n):
    if n<=1:
        return false
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return false
    return true
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not an prime number ")
print("check if 243 is a prime number")
print (is_prime(243))
