f2c_list=[]
c2f_list=[]

def f2c_conversion(fahr):
	return ((fahr-32)*5.0/9.0)
def c2f_conversion(cel):
	return (9.0/5.0*cel+32)
i=True
while(i):
	ch=input("Enter the choice : ")
	if ch=="1":
		ip_fahr=float(input("Enter fahr : "))
		f2c_list.append((ip_fahr,f2c_conversion(ip_fahr)))
		print(f2c_list)
	elif ch=="2":
		ip_cel=float(input("Enter celsius : "))
		c2f_list.append((ip_cel,c2f_conversion(ip_cel)))
		print(c2f_list)
	elif ch=="3":
		sort_ch=input("Enter 1 for F and 2 for C")
		if ch=="1":
			print("f2c list : ",sorted(f2c_list,key=lambda x:x[0]))
			print("c2f list : ",sorted(c2f_list,key=lambda x:x[1]))
		else:
			print("f2c list : ",sorted(f2c_list,key=lambda x:x[1]))
			print("c2f list : ",sorted(c2f_list,key=lambda x:x[0]))
	else:
		i=False
