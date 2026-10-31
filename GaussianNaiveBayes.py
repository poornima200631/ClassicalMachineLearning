import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
  accuracy_score,
  confusion_matrix,
  classification_report
)

iris=load_iris()

x=iris.data
y=iris.target

xtrain,xtest,ytrain,ytest=train_test_split(
  x,
  y,
  test_size=0.2,
  random_state=42,
  stratify=y
)

class GausianNaiveBayes:
  def __init__(self,var_smoothing=1e-9):
    self.var_smoothing=var_smoothing
    self.classes=None
    self.mean={}
    self.var={}
    self.prior={}
    self.epsilon=None


  def fit(self,x,y):

    x=np.asarray(x,dtype=np.float64)
    y=np.asarray(y)

    self.classes=np.unique(y)
    self.epsilon = (
    self.var_smoothing *
    np.var(x, axis=0).max()
)
    for c in self.classes:
      x_c=x[y==c]
      self.mean[c]=np.mean(x_c,axis=0)
      self.var[c]=np.var(x_c,axis=0)+self.epsilon
      self.prior[c] = len(x_c) / len(x)

    return self
  # calulating score for each class one with highest score will be the ans
  def gaussian_Probability(self,x,c):
    mean=self.mean[c]
    var=self.var[c]

    numerator = np.exp(
        -((x - mean) ** 2) / (2 * var)
    )

    denominator = np.sqrt(2 * np.pi * var)

    return numerator / denominator

  def predict_one(self,x):
    scores=[]
    for c in self.classes:
      prior=self.prior[c]
      likelihood=self.gaussian_Probability(x,c)
      posterior=prior*np.prod(likelihood)

      scores.append(posterior)

    return self.classes[np.argmax(scores)]

  def predict(self,x):

    predictions=[]

    for sample in x:

      result=self.predict_one(sample)

      predictions.append(result)

    return np.array(predictions)
  


model=GausianNaiveBayes()

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

print("Predictions:",ypred)
print("Accuracy:",accuracy_score(ytest,ypred))
print("Confusion Matrix:")
print(confusion_matrix(ytest,ypred))
print("Classification Report:")
print(classification_report(ytest,ypred))