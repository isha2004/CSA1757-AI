import math
import random

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize sizes
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases with random values
        self.weights_input_hidden = []
        for _ in range(self.input_size):
            self.weights_input_hidden.append([random.uniform(-1, 1) for _ in range(self.hidden_size)])

        self.bias_hidden = [random.uniform(-1, 1) for _ in range(self.hidden_size)]

        self.weights_hidden_output = []
        for _ in range(self.hidden_size):
            self.weights_hidden_output.append([random.uniform(-1, 1) for _ in range(self.output_size)])

        self.bias_output = [random.uniform(-1, 1) for _ in range(self.output_size)]

    def feedforward(self, inputs):
        # Compute output of hidden layer
        hidden_sum = []
        for j in range(self.hidden_size):
            neuron_sum = 0
            for i in range(self.input_size):
                neuron_sum += inputs[i] * self.weights_input_hidden[i][j]
            neuron_sum += self.bias_hidden[j]
            hidden_sum.append(neuron_sum)

        hidden_output = [sigmoid(x) for x in hidden_sum]

        # Compute final output
        output_sum = []
        for k in range(self.output_size):
            neuron_sum = 0
            for j in range(self.hidden_size):
                neuron_sum += hidden_output[j] * self.weights_hidden_output[j][k]
            neuron_sum += self.bias_output[k]
            output_sum.append(neuron_sum)

        final_output = [sigmoid(x) for x in output_sum]

        return final_output


# Example usage:
if __name__ == "__main__":
    # Initialize a neural network with 2 input neurons, 3 hidden neurons, and 1 output neuron
    nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)

    # Example input
    input_data = [0.7, 0.3]

    # Perform feedforward pass
    output = nn.feedforward(input_data)
    print("Input:", input_data)
    print("Output:", output)