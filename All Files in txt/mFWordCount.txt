import collections as ct

def wordCount(line):
	return ct.Counter(line.read().split())
print(wordCount(open("data.txt")))
worddic={}
def wordpresent(fname):
	infile=open(fname)
	for line in infile:
		myline=line.split()
		for words in myline:
			w=worddic.get(words,0)
			worddic[words]=w+1
	return worddic
print(wordpresent("data.txt"))
