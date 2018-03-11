from matrix import Matrix
from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


class NeuralNetwork(object):
    """This class allows you to use machine learning"""

    def __init__(self, inputs_nodes, hidden_nodes, output_nodes):
        """ Takes number of nodes of each layer """
        self.inputs_nodes = inputs_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Here the weights between input and hidden
        self.w1 = Matrix(self.hidden_nodes, self.inputs_nodes)
        # Here the weights between hidden and ouput
        self.w2 = Matrix(self.output_nodes, self.hidden_nodes)

        # Initialize the weights between -1 and 1
        self.w1.randomize()
        self.w2.randomize()

        self.biais_hidden = Matrix(self.hidden_nodes, 1)
        self.biais_output = Matrix(self.output_nodes, 1)
        self.biais_hidden.randomize()
        self.biais_output.randomize()

    def feed_forward(self, input_arr):
        """ The neural network try to guess the answer """

        inputs = Matrix.fromArray(input_arr)

        hidden = Matrix.multiply(self.w1, inputs)
        hidden.addition(self.biais_hidden)
        # Activation fonction
        hidden.map(sigmoid)

        output = Matrix.multiply(self.w2, hidden)
        output.addition(self.biais_output)
        output.map(sigmoid)

        return output.toArray()
