# Be sure to rename this file to benchmark.py or your solution will not be autograded properly

# THESE NEXT TWO LINES ARE NEEDED WHEN YOU SUBMIT YOUR PROJECT
# they are what activate the QVM in the background that your code runs against.
# Feel free to comment them out for local testing, but be sure to enable them when submitting
import subprocess
subprocess.Popen("/src/qvm/qvm -S > qvm.log 2>&1", shell=True)


def get_model(filename):
    with open('noise_model.quil', 'r') as file:
        model_info = file.read()
        return model_info

# you are to complete this function
def benchmark_T1(filename):
    # ...
    # the return type is a dictionary whose keys are qubit ids and whose value is the T1 in seconds
    return {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

# you are to complete this function
def benchmark_T2(filename):
    # ...
    # the return type is a dictionary whose keys are qubit ids and whose value is the T2 in seconds
    return {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
