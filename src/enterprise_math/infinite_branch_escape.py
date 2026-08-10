"""Infinite branch alphabets can evade finite-label lcm coherence.

Let labelled branches be indexed by positive integers k and define the exact
branch law

    P_k : 0 = k.

Every exact branch is impossible.  Modulo M, however, branch k is locally
solvable exactly when

    M | k.

Hence the branch support is

    S_M = {k>0 : M divides k}.

Every S_M is nonempty, and ``M|N`` implies ``S_N subseteq S_M``.  Nevertheless

    intersection_(M>=1) S_M = empty,

because no positive integer is divisible by every positive modulus.

Thus the finite-label survival theorem fails for an infinite witness alphabet:
the witness label can escape to ever larger values as precision increases.
Finiteness (or a suitable compactness condition on the witness space) is a real
semantic resource, not a proof convenience.
"""

from __future__ import annotations


def _modulus(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("modulus must be an integer")
    if value <= 0:
        raise ValueError("modulus must be positive")
    return value


def infinite_branch_locally_solvable(label: int, modulus: int) -> bool:
    if isinstance(label, bool) or not isinstance(label, int):
        raise TypeError("label must be an integer")
    if label <= 0:
        raise ValueError("label must be positive")
    M = _modulus(modulus)
    return label % M == 0


def least_local_branch_label(modulus: int) -> int:
    """Smallest branch label surviving the declared modulus."""
    return _modulus(modulus)


def finite_prefix_common_survivor(max_modulus: int) -> int:
    """One label surviving every modulus 1..max_modulus: their lcm."""
    M = _modulus(max_modulus)
    from math import lcm

    label = 1
    for modulus in range(1, M + 1):
        label = lcm(label, modulus)
    if not all(infinite_branch_locally_solvable(label, modulus) for modulus in range(1, M + 1)):
        raise AssertionError("finite-prefix witness failed one local branch condition")
    return label


def fixed_label_blocker(label: int) -> int:
    """Return one modulus blocking this fixed positive label."""
    if isinstance(label, bool) or not isinstance(label, int):
        raise TypeError("label must be an integer")
    if label <= 0:
        raise ValueError("label must be positive")
    blocker = label + 1
    if infinite_branch_locally_solvable(label, blocker):
        raise AssertionError("fixed-label blocker construction failed")
    return blocker
