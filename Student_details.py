N=int(input("Enter number of student: "))
roll=[]
Students_name=[]
Students_email=[]
Student_details=[]
for i in range(N):
    rollNo=int(input("Enter Roll number:"))
    name=(input("Enter name: "))
    email=(input("Enter email: "))
    roll.append(rollNo)
    Students_name.append(name)
    Students_email.append(email)
Students_roll=tuple(roll)
Student_details.extend([list(a) for a in zip(Students_name,Students_email)])
print(Student_details)

stud_roll=int(input("Enter the roll no whose information you want: "))
index=Students_roll.index(stud_roll)
print("The Name of Student is: " ,Students_name[index])
print("The E-mail of Student is: ",Students_email[index])

stud_roll_pop=int(input("Enter the roll number whose information you want to delete: "))
index_pop=Students_roll.index(stud_roll_pop)
Student_details.pop(index_pop)
print(len(Student_details))

