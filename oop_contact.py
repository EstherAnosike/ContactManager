class Contact():

	def __init__(self, name, phone_number, gender, email_address, postal_address):
		self.name = name
		self.phone_number = phone_number
		self.gender = gender
		self.email_address = email_address
		self.postal_address = postal_address

	def new_contact(self):
		print ("Name is {}\n".format(self.name), "Phone Number is {}\n".format(self.phone_number), "Gender is {}\n".format(self.gender), 
			"Email Address is {}\n".format(self.email_address), "Postal Address is {}\n".format(self.postal_address))
	
class ContactManager():
	def __init__(self, contacts=[]):
		self.contacts=contacts

	def add_contact(self, contact):
		self.contacts.append(contact)

	def delete_contact(self, contact):
		for contact in self.contacts:
			if contact.name == name:
				self.contacts.remove(contact)
				return contact
		return None

	def search_contact(self, contact):
		for contact in self.contacts:
			print(contact.name)


name = input ("Please enter your name: ")
phone_number = input ("Please enter phone number: ")
gender = input ("Please enter your gender: ")
email_address = input ("Please enter your email address: ")
postal_address = input ("Please enter your postal address: ")

contactfile = Contact(name, phone_number, gender, email_address, postal_address)

contactfile.new_contact()

contactfile = ContactManager()
contactfile.add_contact(Contact(name = "", phone_number = "", gender = "", email_address = "", postal_address = ""))
contactfile.delete_contact(Contact(name = "", phone_number = "", gender = "", email_address = "", postal_address = ""))

#print(len(contactfile.contacts))

