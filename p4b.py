import numpy as np

np.random.seed(0)
#X == inputs
X = [ [1, 2 ,3 ,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5, 2.7, 3.3 , -0.8]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons)) #both function return a matrix of shape (first_arg,sec_arg)

    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4,5) #f_arg = size of the inputs s_arg = yyyy
layer2 = Layer_Dense(5,2) #l1 is trze input soo we have to set f_a to 5
#secondary argument can be a random integer


layer1.forward(X) #

#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)