import pennylane as qml
from pennylane import numpy as np

# tell PennyLane which device we want to use;
# for this, we'll just use a simple reference simulator
dev = qml.device('default.qubit', wires=1)


@qml.qnode(dev)
def circuit(theta1, theta2):
    """
    :param theta1: Parameter angle for the one qubit circuit in the assignment pdf
    :param theta2: Parameter angle for the one qubit circuit in the assignment pdf
    :return: A Pennylane Expectation calculation
    """
    pass


def circuit_grad(theta1, theta2):
    """
    :param theta1: Parameter angle for the one qubit circuit in the assignment pdf
    :param theta2: Parameter angle for the one qubit circuit in the assignment pdf
    :return: The gradient of the circuit with respect to the two paramters as a list
    """
    """YOUR CODE HERE"""
    return [grad_theta, grad_phi]
