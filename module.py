import pandas as pd
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("data.csv")

X = df[['hours','attendance','marks']]
y = df['result']

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[4,75,33]])

print("Prediction:", prediction)
if prediction == [0]:
    print("fail")
else :
    print ("pass")    