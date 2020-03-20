"""gss Grammatical Structure Similarity Module
This Module implementes a calculation for GSS
"""
from typing import NamedTuple

import numpy as np
from nltk.tree import Tree


class GSS(NamedTuple):
    """
        Helper Class to specifie the return type of gss
    """

    gss: float
    nA: float
    nB: float
    nAB: float


def calc_gss(
    a: Tree,
    b: Tree,
) -> GSS:
    """
    Calculates the gss for Tree a and b

    Parameters:
        a: Tree
        b: Tree

    Returns:

    """
    # Set Dummy Values
    nA = 19
    nB = 19
    nAB = 17

    return GSS(((2 * nAB)) / (nA + nB), nA, nB, nAB)

