#!/usr/bin/env python3
"""EC49FUC-S exact rational certificate for the all-real finite-bin minimax proof.

Regression checks validate constants and symbolic comparison. The proof for all
real epsilon and delta is in EC49FUC_SHARP_FINITE_BIN_MINIMAX_EXTENSION.md.
"""
from fractions import Fraction as F

M, L, U = F(1469, 64), F(951, 1280), F(3, 4)
W, E = U - L, F(1048576, 18958647)
A0, A1 = F(1, 8400), F(133679, 65536000)
B0, B1 = F(23, 181440), F(948007537, 428070666240)

MU_A = A1 / A0
MU_B = B1 / B0
MU_T = (A1 + B1) / (A0 + B0)

def q(e):
    return (B0 - e * B1) / (A0 + B0 - e * (A1 + B1))

def rho(e, delta):
    return delta * (1 - e * M * (U - delta / 2)) / (
        W * (1 - e * M * (L + U) / 2))

def v(e, delta):
    return q(e) * (1 - rho(e, delta))

def exact_certificate():
    assert W == F(9, 1280)
    assert MU_A == F(2807259, 163840)
    assert MU_B == F(41217719, 2359296)
    assert MU_T == F(45529434409, 2630615040)
    assert MU_B > MU_T > MU_A > M * L > 0
    assert 1 - E * MU_B > 0
    assert 1 - E * MU_T > 0
    ratio_lower_bound = (MU_B - MU_T) / (M * W / 2)
    ratio_upper_bound = MU_B * MU_T / (MU_A * M * L)
    assert ratio_lower_bound == F(3965947, 1965522)
    assert ratio_upper_bound == F(
        9383097168495465355, 9067439094875650944)
    assert ratio_lower_bound - ratio_upper_bound == F(
        8912797192394315189, 9067439094875650944) > 0
    assert q(E) == F(3310244525, 8132285009)
    assert rho(E, W / 4) == F(1547881, 6614596)
    assert v(E, W / 4) == F(
        16772065588485375, 53791779891391364)
    assert (1 - v(E, W / 4)) / 2 == F(
        37019714302905989, 107583559782782728)
    for delta in [F(0), W / 4, W / 2, F(3, 4) * W]:
        vals = [v(e, delta) for e in
                [F(-10000), F(-100), F(-1), F(0), E]]
        assert all(a > b for a, b in zip(vals, vals[1:]))
    assert v(E, W) == 0
    print("EC49FUC-S exact Fraction certificate: PASS")
    print("global strict inequality gap:", ratio_lower_bound - ratio_upper_bound)
    print("sharp one-sample equal-prior risk at delta=W/4:",
          (1 - v(E, W / 4)) / 2)

if __name__ == "__main__":
    exact_certificate()
