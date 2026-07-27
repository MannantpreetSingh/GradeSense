import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv("data.csv")
x=data[["hours","attendance"]]
y=data["result"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=LogisticRegression()
model.fit(x_train,y_train)
prediction = model.predict(x_test)
print("prediction :",prediction)
print("Accuracy:", accuracy_score(y_test, prediction ))