"""Exploratory signed six-phase density probes at the two Morse critical values.
Numerical quadrature is not a certified interval bound.
Reproduction: python PREFIX1036_R6_BESSEL_RESONANT_PROBE.py
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.integrate import quad, simpson
from scipy.special import j0, j1, jv


def integrand(t, y):
    r = math.sqrt(y)
    h = y * y * (36 - y) ** 2
    dh = 4 * y * (y - 36) * (y - 18)
    p = y * (y - 36) * (17 * y - 91)
    j2_over_t = jv(2, r * t) / t if t else 0.0
    kernel = ((2 * dh - p) * t * j0(r * t)
              - (h / r) * t * t * j1(r * t)
              + 12 * (11 + y) *
              (r * (y - 6) * j1(r * t) - 2 * y * j2_over_t))
    return j0(t) ** 6 * kernel / 5


def finite_integral(y, upper, step=0.05, split=20.0):
    first = quad(lambda t: integrand(t, y), 0, split,
                 epsabs=1e-10, epsrel=1e-11, limit=300)[0]
    t = np.linspace(split, upper, round((upper - split) / step) + 1)
    r = math.sqrt(y)
    h = y * y * (36 - y) ** 2
    dh = 4 * y * (y - 36) * (y - 18)
    p = y * (y - 36) * (17 * y - 91)
    kern = ((2 * dh - p) * t * j0(r * t)
            - (h / r) * t * t * j1(r * t)
            + 12 * (11 + y) *
            (r * (y - 6) * j1(r * t) - 2 * y * jv(2, r * t) / t))
    return float(first + simpson(j0(t) ** 6 * kern / 5, x=t))


def resonant_tail_coefficient(y):
    if y == 4:
        return -1536 * math.sqrt(2) / (math.pi ** 3.5)
    if y == 16:
        return -1920 / (math.pi ** 3.5)
    raise ValueError("Only y=4 and y=16 have an interior resonance")


if __name__ == "__main__":
    for y in (4, 16):
        c = resonant_tail_coefficient(y)
        for upper in (800, 1600, 3200, 6400):
            raw = finite_integral(y, upper)
            corrected = raw + 2 * c / math.sqrt(upper)
            print(f"y={y:2d} T={upper:5d} I_T={raw:.9f} corrected={corrected:.9f}")
        at_3200 = finite_integral(y, 3200) + 2 * c / math.sqrt(3200)
        expected = 114.914896 if y == 4 else 22.347189
        assert abs(at_3200 - expected) < 0.01
