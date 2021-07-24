import numpy as np

X = [ [1, 2 ,3 ,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5, 2.7, 3.3 , -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros(1,n_neurons) #both function return a matrix of shape (first_arg,sec_arg)
        
    def forward(self):
        pass