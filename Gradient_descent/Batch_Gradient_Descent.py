import numpy as np
from scipy.optimize import approx_fprime
class BatchGradientDescent:
       def __init__(self, learning_rate=0.01, epochs=1000, epsilon=1e-5):
              self.learning_rate=learning_rate
              self.epochs=epochs
              self.epsilon = epsilon

       def fit(self,loss_fn,params):
              params=np.random.randn(params.shape[0])

              for i in range(self.epochs):
                     gradients=approx_fprime(params,loss_fn,self.epsilon)
                     params=params-self.learning_rate*gradients
              self.params=params.copy()
              return self.params
       