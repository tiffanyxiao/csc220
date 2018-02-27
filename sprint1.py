
import re
##test out 

class Contact:
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

		self.email_check()
		self.phone_check()



	def email_check(self):
		if "@" not in self.email or ".com" not in self.email :
			print("invalid email")

	def phone_check(self):

		no_char = re.sub('[^0-9]','', self.phone)


		
		if len(no_char) > 10:
			print("invalid phone number", no_char)

	def change_phone(self, new_phone):
		self.phone = new_phone

	def change_email(self, new_email):
		self.email = new_email



	def __str__(self):
		all_info = (self.name) + " " +  (self.phone) + " " + (self.email)
		return all_info


	
def main():

	my_info = Contact("Karen", "845-326-6255", "sanmakaren@gmail.com");
	print(my_info)
	my_info.change_phone("6345346")
	print(my_info)
	
	

main()