#Authentication File
#Define the Authentication file
def signin(username,password,filename):

# read the file
	myfile = open(filename,"r")
	uname = myfile.readline().strip()
	pword = myfile.readline().strip()
	myfile.close()

#Match the username & password
	if (username == uname and password == pword):
		return True
	else:
		return False