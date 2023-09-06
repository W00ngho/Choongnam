import pandas as pd
df = pd.read_csv('pytorch/data/train.csv')
index_col = 'PassengerId'
print(df.head())

df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']]
df['Sex'] = df['Sex'].map({'male': 0, 'female''ignore': 1})
df = df.dropna()
X = df.drop('Survived', axis = 1)
y = df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)

from sklearn import tree
model = tree.DecisionTreeClassifier()

model.fit(X_train, y_train)

y_predict = model.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predict)


# X_train, X_test, y_traain, y_test = sklearn.model_selection.train_test_split(X, y, random_state = 1)
# model = sklearn.tree.DecisionTreeClassfiter()
# 
# model.fit(X_train, y_train)
# y_predict = model.predict(X_test)
# sklearn.metrics.accuracy_score(y_test, y_predict)
# 
# pd.DataFrame(sklearn.metrics.confusion_matrix(y_test, y_predict),
            #  columns = ['Predicted Not Survival', 'Predicted Survival'])

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)

from sklearn.metrics import confusion_matrix
pd.DataFrame(
    confusion_matrix(y_test, y_predict),
    columns = ['Predicted Not Survival', 'Predicted Survival'],
    index = ['True Not Survival', 'True Survival']
)

