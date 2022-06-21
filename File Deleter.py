# code to delete entire data along with file
import os

file = input("Whats the name of the file?\n")

# check if file exists
if os.path.exists(file):
	choice = input("Are you sure you want to delete the following item? : " + file + "\n")
	if choice == "yes":
		os.remove(file)
	
	if choice == "no":
		quit()
	# Print the statement once
	# the file is deleted
	print("File deleted !")

else:

	# Print if file is not present
	print("File doesnot exist !")
