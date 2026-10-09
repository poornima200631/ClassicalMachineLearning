from MyLinearRegression import MyLinearRegression 
import numpy as np
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 3],
    [2500, 4],
    [3000, 5]
])
mlr = MyLinearRegression()
Y = np.array([200, 280, 330, 400, 500])
mlr.fit(X,Y)
A=np.array([[3500,6],[1450,2]])
predicted_val=mlr.predict(A)
print("Predictedvals=",predicted_val)




