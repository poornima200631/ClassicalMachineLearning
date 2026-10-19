from  sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
def pca(X,n_components):
     scaler=StandardScaler()
     X_scaled=scaler.fit_transform(X)
     pca=PCA(n_components=n_components)
     X_pca=pca.fit_transform(X_scaled)
     X_new=X_pca.fit_transform(X_scaled)
     return X_new