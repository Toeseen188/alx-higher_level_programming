#!/usr/bin/python3
""" module doc"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplication of matrix
    Args:
        m_a(list of lists of int/float): matrix arg
        m_b(list of lists of int/float): matrix arg
    Returns:
        returns m_a x m_b
    """
    return (np.matmul(m_a, m_b))
