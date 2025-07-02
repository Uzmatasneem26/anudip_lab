number=10
while number<=15:
    print(number)
    number+=1
#to control loop
#break-------------------------------
for i in range(15):
    if i==5:
        break;#stop the iteration
    print(i)
    
#continue--------------------------
for i in range(15):
    if i==5:
        continue
    print(i)#skip tht number and continue iteration

#else----------------------------------
for i in range(5):
    print(i)
else:
        print("loop completed")

#pass-----------------------------------
for i in range(3):
    if i==3:
        pass
    print(i)#pass statements does nothing

