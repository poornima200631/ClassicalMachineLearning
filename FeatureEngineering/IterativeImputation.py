from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

def IterativeImputer(X_train,X_test,max_ter=10):
  imputer =IterativeImputer(estimator=BayesianRidge(),max_ter=max_ter,random_state=42)

  X_train_imputed=imputer.fit_transform(X_train)
  X_test_imputed=imputer.transform(X_test)

  return X_train_imputed,X_test_imputed

