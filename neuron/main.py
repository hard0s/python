import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

class neuron:
    def __init__(self,weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs)+ self.bias
        return sigmoid(total)

weights = np.array([0, 1])
bias = 4
