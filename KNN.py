
import numpy as np
from collections import Counter


class KNN:

    def __init__(self, k=3):

        self.k = k

    def fit(self, X, y):

        self.X_train = np.asarray(X)
        self.y_train = np.asarray(y)

        if self.k <= 0 or self.k > len(self.X_train):
            raise ValueError("Invalid value of k")

        if len(self.X_train) != len(self.y_train):
            raise ValueError("X and y must have equal samples")

    def euclidean_distance(self, x1, x2):

        return np.sqrt(np.sum((x1 - x2)**2))

    def predict_one(self, x):

        distances = []

        for i in range(len(self.X_train)):

            distance = self.euclidean_distance(
                x, self.X_train[i]
            )

            distances.append((distance, self.y_train[i]))

        distances.sort(key=lambda item: item[0])

        k_nearest = distances[:self.k]

        labels = [item[1] for item in k_nearest]

        return Counter(labels).most_common(1)[0][0]

    def predict(self, X):

        predictions = []

        for x in X:

            predictions.append(self.predict_one(x))

        return np.array(predictions)
