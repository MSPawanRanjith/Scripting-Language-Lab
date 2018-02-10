import pandas as pd
import matplotlib.pyplot as plt

titanic_df=pd.read_csv("train.csv")
print(titanic_df.head())
titanic_df.info()
print(titanic_df.describe())

titanic_df=titanic_df.drop(["PassengerId","Name","Ticket","Parch"],axis=1)
print(titanic_df.columns)

print(titanic_df["Embarked"])
titanic_df["Embarked"]=titanic_df["Embarked"].fillna("x")
print(titanic_df["Embarked"])

print(len(titanic_df))
print (len(titanic_df.columns))

titanic_df.info()
print("Max Age : ",titanic_df.Age.max())
print("Min Age : ",titanic_df.Age.min())
print("Mean Age : ",titanic_df.Age.mean())

plot=titanic_df.Age.hist()
plot.set(xLabel="No. of ppl",yLabel="Age")
plt.show()

titanic_df.Age.plot()
plt.show()
