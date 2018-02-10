class student:
	usn=""
	name=""
	marks=[]
	
	def __init__ (self):
		self.name=input("Enter the Name : ")
		self.usn=input("Enter the USN : ")
		for range in (0,3):
			self.marks.append(int(input("Enter the marks :")))
	def calculate(self):
		print(" SUM : ",sum(self.marks))
	def display(self):
		print(self.usn)
		print(self.name)
		print(self.marks)

for range in (0,3):
	stud=student()
	stud.calculate()
	stud.display()
