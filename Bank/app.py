from flask import *

app=Flask(__name__)
app.secret_key="secret"

@app.route("/",methods=["GET","POST"])
def banking():
	try:
		balance=session["balance"]
		count=session["count"]
	except KeyError:
		balance=session["balance"]=8000
		count=session["count"]=0
	
	if request.method=="GET":
		return render_template("bank.html",bal=balance)
	if request.method=="POST":
		if session["count"]>=5:
			msg="TIMED OUT"
			session.clear()
			return render_template("bank.html",msg=msg,count=count,bal=balance)
		if request.form["action"]=="Withdraw":
			if int(request.form["amt"])>session["balance"] :
				msg="Balnce is low"
				return render_template("bank.html",msg=msg,bal=balance)
			else:
				balance=balance-int(request.form["amt"])
				session["balance"]=balance
				count=count+1
				session["count"]=count
				msg="Debited Sucessfully"
				return render_template("bank.html",msg=msg,bal=balance,count=count)
		elif request.form["action"]=="Deposit":
				balance=balance+int(request.form["amt"])
				session["balance"]=balance
				count=count+1
				session["count"]=count
				msg="Credited Sucessfully"
				return render_template("bank.html",msg=msg,bal=balance,count=count)
if __name__ =="__main__":
	app.run()
				
		
