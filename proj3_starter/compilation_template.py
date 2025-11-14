from typing import Tuple, List

from pyquil import Program
from pyquil.gates import CNOT, CZ, H, X, Z
from pyquil.unitary_tools import program_unitary

import numpy as np
import networkx as nx
from networkx.algorithms.traversal.breadth_first_search import bfs_edges

# YOU MUST COMMENT THESE LINES OUT TO RUN ON THE AUTOGRADER TO START THE QVM SERVER
# import subprocess
# subprocess.Popen("/src/qvm/qvm -S > qvm.log 2>&1", shell=True)


def mat_eq(m1, m2):
    """
    Accepts two numpy arrays and returns True if they are the same element wise
    """
    return np.allclose(m1, m2)


def cnot_to_cz(pq: Program) -> Program:
    """

    :param pq:
    :return: A program that has the same operation but converts all CNOTs to CZs
    """
    pass


# These are the two ways of making a GHZ state that are described in the notes
def make_ghz_1(size: int) -> Program:
    pass


def make_ghz_2(size: int) -> Program:
    pass


# You want to check that both programs create the same wavefunction as a final state


def ghz_compile(edges: List[Tuple]) -> Program:
    """
    Produce a pyQuil Program that makes a GHZ state over all qubits, but that only uses two qubit gates
    between qubits whose edges are allowed.

    *Hint The networkx library is a very helpful library for working with graphs in Python*

    :param edges: The list of edges where two qubit gates can be applied.
    :return: The compiled program.
    """
    pass

