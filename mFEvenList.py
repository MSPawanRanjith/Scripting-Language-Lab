org_list=eval(input("Enter the list , seperated : "))
def removeDuplicates():
	new_list=[]
	for x in org_list:
		if x not in new_list:
			new_list.append(x)
	return new_list
print(removeDuplicates())
print(set(org_list))
