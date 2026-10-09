import numpy as np
class MyLinearRegression:
    def __init__(self):
        self.coefficients=None
        self.intercept=None
      
    def fit(self,X,Y):
        onesarr=np.ones((X.shape[0],1))
        xb=np.column_stack((onesarr,X))
        beta = np.linalg.lstsq(xb, Y, rcond=None)[0]
        self.intercept = beta[0]
        self.coefficients = beta[1:]
        
    def predict(self,X):
        y_pred=self.intercept+X @ self.coefficients
        return y_pred