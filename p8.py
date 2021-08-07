import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()




class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons)) #both function return a matrix of shape (first_arg,sec_arg)

    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU: #rectifed linear unit
    def forward(self,inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis=1,keepdims=True))
        probabilities = exp_values /np.sum(exp_values,axis=1,keepdims=True)
        self.output = probabilities

class Loss:
    def calculate(self,output,y):
        sample_losses = self.forward(output,y)
        data_loss = np.mean(sample_losses)
        return data_loss
class Loss_CategoricalCrossentropy(Loss): #inhare from/with Loss read more about this
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred,1e-7,1-1e-7)

        if len(y_true.shape)==1: #array is one dimential
            correct_confidences= y_pred_clipped[range(samples),y_true]
        if len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true,axis=1)
            

X, y = spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2,3) #2 musi byc bo jest x,y

activation1 = Activation_ReLU()

dense2 = Layer_Dense(3,3)
#pierwsza 3ka po z poprzedniego wyjscia dostaniemy 3 wejscia
#druga w sumie znowu moglaby byc czymkolwiek
#ale powinniśmy potraktowac drugi argument jako pytanie ile danych na wyjsciu powinna miec ta warstwa
# a konkretniej ile neuronów powinna mieć 3 klasy 3 neurony w tym przypadku

activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5]) #we get batch of 300 samples
#but printing only first 5.

#czysty model powinien zwracac nam rowne szanse