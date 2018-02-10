def Max(list):
	if len(list)==1:
		return list[0]
	m=Max(list[1:])
	return m if m>list[0] else list[0]
print(Max([1,0,9,5]))
