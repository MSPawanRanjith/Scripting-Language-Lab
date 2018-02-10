from flask import *
import re
import time

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def check():
	if request.method=="GET":
		return render_template("index.html")
	if request.method=="POST":
		try:
			time.strptime(request.form["dob"],"%d/%m/%Y")
		except ValueError:
			msg="INVALID DATE "
			return render_template("index.html",msg=msg)
		m1=int(request.form["sub1"])
		m2=int(request.form["sub2"])
		m3=int(request.form["sub3"])
		m4=int(request.form["sub4"])
		m5=int(request.form["sub5"])
		c1=int(request.form["cr1"])
		c2=int(request.form["cr2"])
		c3=int(request.form["cr3"])
		c4=int(request.form["cr4"])
		c5=int(request.form["cr5"])
		c=[]
		m=[]
		points=0
		g=[]
		c.extend((c1,c2,c3,c4,c5))
		m.extend((m1,m2,m3,m4,m5))
		for (num,cr) in zip(m,c):
			if(num>=90):
				g.append("A")
				points=points+10*cr
			elif(num<90 and num>=70):
				points=points+8*cr
				g.append("B")
			else:
				points=points+5*cr
				g.append("C")
		msg="SGPA : "+str(points)
		
		return render_template("finish.html",msg=msg,marks=g)
if __name__ =="__main__":
	app.run()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
