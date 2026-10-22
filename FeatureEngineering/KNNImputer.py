from sklearn.impute import KNNImputer
def KNNImputerFunction(X_train,Xtest,neighbors=5):
  imputer=KNNImputer(n_neighbors=neighbors)

  X_train_imputed=imputer.fit_transform(X_train)
  X_test_imputed=imputer.transform(Xtest)


  return X_train_imputed,X_test_imputed
