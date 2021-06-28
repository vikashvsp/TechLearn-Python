n=int(input("Enter the number of student:- "))
stu_roll=int(input("Enter the first student roll number: "))
stu_record={}
for i in range(n):
    stu_name=str(input("Enter the Student name: "))
    stu_email=str(input("Enter the Student email-ID: "))
    stu_section=str(input("Enter the Student section: "))
    new_record={'name':stu_name,'email-id':stu_email,"roll":stu_roll,'section':stu_section}
    stu_record.update({stu_roll:new_record})
    stu_roll+=1
print(stu_record)
print("The count of Student is")
print(len(stu_record))
stu_roll=int(input("Enter roll number whose email ID you want to change:- "))
new_email=str(input("Enter the new email ID:- "))
stu_record.update({stu_roll:{'name':stu_name,'email-id':new_email,"roll":stu_roll,'section':stu_section}})
print(stu_record)

pop_roll=int(input("Enter the roll number of student whose record you want to delete:- "))
stu_record.pop(pop_roll)
print(stu_record)