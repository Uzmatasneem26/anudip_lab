marks=[]
for i in range (1,6):
    mark = float(input(f"enter the subjects marks {i}:"))
    marks.append(mark)
    
average=sum(marks)/5

if average >=90:
    grade="A+"
elif average >=80:
    grade="A"
elif average >=70:
    grade= "B"
elif average >=60:
    grade= "C"
elif average >=50:
    grade="D"
else:
    grade="F(fail)"
    
print(f"\n Average marks:{average:.2f}")
print(f"the grade of the above student is :{grade}")
