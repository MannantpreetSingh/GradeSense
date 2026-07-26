import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    'hours': [1,2,3,4,5,6],
    'attendance': [50,60,70,80,90,95],
    'marks': [30,40,50,60,70,80],
    'result': [0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[['hours','attendance','marks']]
y = df['result']

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[4,75,60]])

print("Prediction:", prediction)