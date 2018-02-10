class sentenceReverser:
	vowels=["a","e","i","o","u"]
	vcount=0
	sentence=""
	reverse=""
	
	def __init__ (self,sentence):
		self.sentence=sentence
		self.reverseSentence()
	def reverseSentence(self):
		self.reverse=" ".join(reversed(self.sentence.split()))
	def getCount(self):
		self.vcount=sum(s in self.vowels for s in self.sentence.lower())
		return self.vcount
		
	def getReverse(self):
		return self.reverse
objlist=[]
for i in range (0,3):
	sent=input("Sentence  : ")
	obj=sentenceReverser(sent)
	objlist.append(obj)
sorted_list=sorted(objlist,key=lambda x:x.getCount(),reverse=True)
for i in range (0,3):
	print(sorted_list[i].sentence+"  reversed : "+sorted_list[i].getReverse()+" vCOUNT  : "+str(sorted_list[i].vcount))
