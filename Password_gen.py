#Create a command-line password generator in Python that generates random passwords based on user-defined criteria, such as length and character types (letters, numbers, symbols). Allow users to specify password length and character set preferences.

import string
import random

length= int(input("Specify the length of the password: "))
print("Choose character set for password from these:\n 1. Digits\n 2. Letters\n 3. Special character\n 4. Exit\n")
my_list = ""

while(True):
	choice = int(input("Enter a number for your choice "))
	if(choice == 1):
		my_list += string.ascii_letters
	elif(choice == 2):
		my_list += string.digits
	elif(choice == 3):
		my_list += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Invalid. Please upload correct value ")
		
password = ""
for i in range(length):
	word = random.choice(my_list)
	password += word
	
print(f"Your password is : {password}")
