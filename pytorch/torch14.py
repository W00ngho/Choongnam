import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('pytorch/data/weather.csv')

# dataset.plot(x='MinTemp', y='MaxTemp', style = 'o')
# plt.title('MinTemp vs MaxTemp')
# plt.xlabel('MinTemp')
# plt.ylabel('MaxTemp')
# plt.show()

x = dataset['MinTemp'].values.reshape(-1, 1)
y = dataset['MaxTemp'].values.reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(sklearn.metrics.accuracy_score(y_pred, y_test))

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

# plt.scatter(x_test, y_test, color = 'gray')
# plt.plot(x_test, y_pred, color = 'red', linewidth = 2)
# plt.show()

print('평균제곱법:', sklearn.metrics.mean_squared_error(y_test, y_pred))
print('루트 평균제곱법', np.sqrt(sklearn.metrics.mean_squared_error(y_test, y_pred)))

