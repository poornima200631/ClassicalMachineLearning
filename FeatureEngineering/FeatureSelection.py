from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif,chi2,mutual_info_classif,SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
def VarianceThresholdSelector(X,threshold=0.0):
    selector=VarianceThreshold(threshold=threshold)
    X_new=selector.fit_transform(X)
    return X_new


def AnovaSelector(X,Y):
    selector=SelectKBest(score_func=f_classif,k='all')
    X_new=selector.fit_transform(X,Y)
    return X_new

def Chi2Selector(X,Y):
    selector=SelectKBest(score_func=chi2,k='all')
    X_new=selector.fit_transform(X,Y)
    return X_new

def MutualInfoSelector(X,Y):
    selector=SelectKBest(score_func=mutual_info_classif,k='all')
    X_new=selector.fit_transform(X,Y)
    return X_new

def LogisticSelector(X,Y):
    model=LogisticRegression(penalty='l1',solver='liblinear',max_iter=3000)
    selector=SelectFromModel(model)
    X_new=selector.fit_transform(X,Y)
    return X_new

def randonforestSelector(X,Y):
    model=RandomForestClassifier(n_estimators=100)
    selector=SelectFromModel(model)
    X_new=selector.fit_transform(X,Y)
    return X_new