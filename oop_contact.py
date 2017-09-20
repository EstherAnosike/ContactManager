class Contact():

	def __init__(self, name, phone_number, gender, email_address, postal_address):
		self.name = name
		self.phone_number = phone_number
		self.gender = gender
		self.email_address = email_address
		self.postal_address = postal_address
	
	def __repr__(self):
		return (" Name:{}\n Phone Number:{}\n Gender:{}\n Email Address:{}\n Postal Address:{}".format(self.name,self.phone_number,self.gender,self.email_address,self.postal_address))

class ContactManager():
	def __init__(self, contacts=[]):
		self.contacts=contacts
		self.load_existing_contacts()

	def add_contact(self, contact):
		self.contacts.append(contact)

	def delete_contact(self, contact):
		if len(self.contacts) != 0:
		
			if isinstance(contact, Contact):
				if contact in self.contacts:
					self.contacts.remove(contact)
					return True
				else:
					return None 
			else:
				raise TypeError ("Not a contact!")
		else:
			raise ValueError("Zero Contacts!!")

	def search_contact(self, name):
		for contact in self.contacts:
			if contact.name == name:
				return contact
			else:
				return None

	def load_existing_contacts(self):
		with open('contacts.csv') as file:
			for line in file.readlines():
				name, gender, email = line.split(',')
				self.add_contact(Contact())

	def save_contacts(self):
		pass
	
end = True
address_book = ContactManager()

while end:
	
	action = input('What do you want to do? Enter a number \n1) Add contact\n2) Search for a contact\n3) Delete a contact\n4) Exit')

	if action == '1':
		name = input("Please enter your name: ")
		phone_number = input("Please enter phone number: ")
		gender = input("Please enter your gender: ")
		email_address = input("Please enter your email address: ")
		postal_address = input("Please enter your postal address: ")

		address_book.add_contact(Contact(name, phone_number, gender, email_address, postal_address))
	elif action == '2':
		name = input('Enter a name to search for:')
		print(address_book.search_contact(name))

	elif action == '3':
		action = input('Delete a contact? what is the name: ')
		c = address_book.search_contact(action)
		if address_book.delete_contact(c):
			print("{} Deleted".format(c.name))
		else:
			print ("Not found!")
	elif action == '4':
		end = False
		address_book.save_contacts()
	else:
		print('Wrong option. Do you want to quit the program? Exit by entering 4')