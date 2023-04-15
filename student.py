#----------------------------------------------------student.py-----------------------------------------------------
#import the functions form Authentication
from authentication import *

#Get the username and password form user
#uname = line 1 (user name) stored in authentication.txt
#pword = password (pass word) store d in authentication.txt
uname = input("Enter your username: ")
pword = input("Enter your password: ")

#call the Authentication file to check the user name & password
file = "Authentication.txt"

#check the user name & password
if (signin(uname,pword,file) == True):

	#Student.py file to read the data, has been stored in student.txt
	file = open("students.txt", "r")

	#Print the headign
	#here i used ("\033[1m'-headign- \033[0m") to bold the headign
	studentdata = ("\033[1mStudent ID\t\tStudent Name\t\tStudent Age\t\tStudent Location\033[0m")
	print()
	Mainheading = ("\033[1m********STUDENTD DETAILS********\033[0m")
	width = 70
	center = Mainheading.center(width)
	print(center)
	print()
	print(studentdata)
	#print the underline
	print("-" * len(studentdata)+"-----")

	#creat the arrays to store the datas
	Student_Id = []
	Student_name = []
	Student_age = []
	Student_location = []

	#append the data into created arrays
	for data in file:
		details = data.strip().split("\t\t\t\t")
		Student_Id.append(details[0])
		Student_name.append(str(details[1]))
		Student_age.append(int(details[2]))
		Student_location.append(details[3])

	#print the data
		print(data.strip())

	print()
	print("No. of Students: ",len(Student_Id))
	print("Lowest Age of Student: ",min(Student_age))
	print("Highest Age of Student: ",max(Student_age))

else:
	#Warning Message
	print()
	print("Unauthorized Access!" ,"Please Enter the Correct User Name & Password.")