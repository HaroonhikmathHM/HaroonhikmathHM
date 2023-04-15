#----------------------------------------------------insert.py-----------------------------------------------------
#import the functions form Authentication
from authentication import *

#Get the username and password form user
#uname = line 1 (user name) stored in authentication.txt
#pword = password (pass word) stored in authentication.txt
uname = input("Enter your username: ")
pword = input("Enter your password: ")

#call the Authentication file to check the user name & password
file = "Authentication.txt"

#check the user name & password
if (signin(uname,pword,file) == True):

	print("you have successfully login")
	print("*****************************")
	print()
	print("ENTER THE STUDENTS DATA")
	print("-----------------------")

#This  function will word after the user input the correct user name and password, stored in atuthentication.txt

#Open the file
	file = open("students.txt", "a")

#write the data to file
	more_data = "Yes" or "No"
	while more_data == "Yes":
	#get the inputs from user
		Student_ID = input("Enter the student's ID: ")
		Student_Name = input("Enter the student's name: ")
		Student_Age = input("Enter the student's age: ")
		Student_Location = input("Enter the student's Location: ")
	#devide the data
		studentdata = Student_ID + "\t\t\t\t" + Student_Name + "\t\t\t\t" + Student_Age + "\t\t\t\t" + Student_Location
		more_data = input("Do you want to add another student details? (Yes or No): ")

		if more_data == "Yes":
			print("******Enter the next student's data******")
		else:
			print()
			print("Thank you for storing the data")
	#write function to store the data in student.txt file
		file.write(studentdata+"\n")

else:
	#Warning Message
	print()
	print("Unauthorized Access!" ,"Please Enter the Correct User Name & Password.")