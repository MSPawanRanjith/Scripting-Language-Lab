import sys
import functools
import os

if(len(sys.argv)!=2):
	print("Invalid args")
	sys.exit()
if(not os.path.exists(sys.argv[1])):
	print("Invalid file")
	sys.exit()
if(sys.argv[1].split(".")[-1]!="txt"):
	print("Only txt")
	sys.exit()

infile=open(sys.argv[1])
worddic={}
len_list=[]
for line in infile :
	myline=line.split()
	for words in myline:
		w=worddic.get(words,0)
		worddic[words]=w+1
print(worddic)

sorteddic=sorted(worddic.items(),key=lambda x:x[1],reverse=True)
print(sorteddic[:10])
for word in sorteddic:
	len_list.append(len(word[0]))
	print(word[0] ,"len ",len(word[0]))
#print(len_list)
#mysum=functools.reduce(lambda x,y:x+y,len_list)
mysum=functools.reduce(lambda x,y:x+y,len_list)
print(mysum/len(len_list))
print([x**2 for x in len_list if x%2!=0])





