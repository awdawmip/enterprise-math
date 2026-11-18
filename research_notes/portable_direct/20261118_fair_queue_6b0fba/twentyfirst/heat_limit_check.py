"""Exact algebraic checks for the sharp heat comparison (Python standard library)."""
import json
from fractions import Fraction as F
from itertools import product


def piecewise_linear(nodes, lengths):
    grad, mass, cross = F(0), F(0), F(0)
    for left, right, length in zip(nodes, nodes[1:], lengths):
        slope = (right - left) / length
        grad += length*slope**2
        mass += length*(left**2 + left*right + right**2)/3
        cross += slope*length*(left+right)/2
    return grad, mass, cross


def main():
    alpha = F(4, 5)
    c = F(3, 4)
    beta = F(1, 4)
    assert alpha*(1+beta) == 1 and alpha*(1-beta**2) == c
    paths = 0
    for vals in product((F(-3, 5), F(-1, 3), F(0), F(1, 2), F(5, 4)), repeat=3):
        nodes = (F(0),) + vals
        grad, mass, cross = piecewise_linear(nodes, (F(1, 3), F(4, 5), F(2)))
        lhs = alpha*(grad+2*cross+mass)-nodes[-1]**2-c*mass
        rhs = alpha*(grad-2*beta*cross+beta**2*mass)
        assert lhs == rhs >= 0
        paths += 1
    defects = {}
    for m in (2, 3, 10, 100, 1000):
        m = F(m)
        defect = (1-m**(-2))/(2*(m-m**(-1))**2)
        assert defect == 1/(2*(m**2-1))
        defects[str(m)] = {"reverse_exponential_defect": str(defect),
                           "squared_ratio_lower_times_nu": str(alpha*(1-defect/2))}
    weights = 0
    for M in (1, 2, 3, 5):
        for K in range(M+1, 24):
            bound2 = F((K+M)**2, K*(K-M)**3)
            for R in range(K, 43):
                for r in range(R-M, R+M+1):
                    assert F((R+M)**2, R*r**3) <= bound2
                    weights += 1
    # Original a=1/10, nu=1, K=8 sqrt(8). The factor C(K)^2 is rational.
    tail_factor2 = F(9, 8)**2*F(8, 7)/(49*8)
    perturbation2 = F(16, 15)*F(4, 5)**2*F(33, 10)**2*tail_factor2
    assert perturbation2 < F(17, 100)**2
    print(json.dumps({"completed_square_piecewise_linear_tests": paths,
                      "near_extremizers": defects,
                      "scalar_shift_weight_tests": weights,
                      "four_wave_K_8sqrt8_CK_squared": str(tail_factor2),
                      "four_wave_frozen_inverse_perturbation_bound_squared": str(perturbation2),
                      "normalized_heat_squared_norm_times_nu": str(alpha)}, indent=2))


if __name__ == '__main__':
    main()
