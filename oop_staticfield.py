class Fellow:
	fellow_count = 0

	def __init__(self,name,nat):
		if Fellow.fellow_count < 3:
			self.name = name
			self.nat = nat
			Fellow.fellow_count += 1
		else:
			raise ValueError("We cannot afford to pay for the fifth fellow",name)

for i in range(5):
	name = input('Enter name: ')
	nat = input('Enter nationality: ')
	Fellow(name, nat)