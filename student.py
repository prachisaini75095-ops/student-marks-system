name = input("Enter student name :")
rollno = input("Enter roll number :")
marks = []

for i in range(5):
    m = float(input("Enter subject marks :"))
    marks.append(m)

total = sum(marks)
percentage = total/5

if percentage>=90 and percentage<=100:
    grade = "A+"
elif percentage>=80 and percentage<=90:
    grade = "A"
elif percentage>=70 and percentage<=80:
    grade = "B"
elif percentage>=60 and percentage<=70:
    grade = "C"
elif percentage>=40 and percentage<=60:
    grade = "D"
else:
    grade = "Fail"

print("\n STUDENT REPORT CARD ")
print("Name :",name)
print("Roll number :",rollno)
print("Marks :",marks)
print("Total marks :",total,"/500")
print("Percentage :",percentage,"%")
print("Grade :",grade)
