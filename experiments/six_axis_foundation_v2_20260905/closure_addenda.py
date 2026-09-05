"""Closure addenda for the six-axis derived foundation V2.

This module extends the V1 `six_axis.py` without changing its verified bytes.
It closes the chart-sign gauge class and the one-parameter quadratic metric
fork.  Nothing here promotes six-counts to native Cell addresses or selects a
native global metric.
"""
from fractions import Fraction
from itertools import combinations
from six_axis import ChartSignConnection, integers

OPPOSITE_EDGE = (5, 4, 3, 2, 1, 0)
FACES = ((0,1,2,0),(0,1,3,0),(0,2,3,0),(1,2,3,1))


def opposite_edge(edge):
    if type(edge) is not int or not 0 <= edge < 6:
        raise ValueError("axis edge must be an integer from 0 to 5")
    return OPPOSITE_EDGE[edge]


def triangle_products(connection):
    if not isinstance(connection, ChartSignConnection):
        raise TypeError("ChartSignConnection required")
    return tuple(connection.walk_product(face) for face in FACES)


def is_fcc_orientation_connection(connection):
    """Exactly the fixed-curvature gauge class induced by local 120° charts."""
    return triangle_products(connection) == (-1,-1,-1,-1)


def gauge_to_all_negative(connection):
    """Return one vertex gauge taking a valid connection to the all-negative one."""
    if not isinstance(connection, ChartSignConnection) or not is_fcc_orientation_connection(connection):
        raise ValueError("connection is outside the FCC orientation gauge class")
    # EDGE order from the V1 atlas is AB,AC,AD,BC,BD,CD.
    eps = [1, -connection.signs[0], -connection.signs[1], -connection.signs[2]]
    eps = tuple(eps)
    target = connection.gauge(eps)
    if target.signs != (-1,)*6:
        raise AssertionError("triangle constraints should make the gauge global")
    return eps


def quadratic_components(n):
    """Exact P_+/P_- decomposition for the conditional metric family."""
    n = integers(n,6)
    plus = tuple(Fraction(n[e] + n[OPPOSITE_EDGE[e]], 2) for e in range(6))
    minus = tuple(Fraction(n[e] - n[OPPOSITE_EDGE[e]], 2) for e in range(6))
    return plus, minus


def quadratic_spectral_extension(n, c=Fraction(0)):
    """Q_c in spectral form; a derived candidate family, not native length."""
    if isinstance(c, bool) or not isinstance(c, (int, Fraction)):
        raise TypeError("c must be exact rational")
    c = Fraction(c)
    if not -1 < c < 1:
        raise ValueError("positive definite extension requires -1<c<1")
    plus, minus = quadratic_components(n)
    p = sum(x*x for x in plus)
    m = sum(x*x for x in minus)
    return (1+c)*p + (1-c)*m


def metric_eigenvalues(c=Fraction(0)):
    """Return exact `(eigenvalue,multiplicity)` data for I+cJ."""
    if isinstance(c, bool) or not isinstance(c, (int, Fraction)):
        raise TypeError("c must be exact rational")
    c = Fraction(c)
    return ((1+c,3),(1-c,3))
