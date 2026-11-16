"""Exact depth-eight checks of the candidate third-gap and terminal invariants."""
from fractions import Fraction as Q
from itertools import accumulate
from math import prod


def block_coefficient(k, start, end):
    rising_start = prod(range(start + k + 1, start + 4 * k + 1))
    rising_end = prod(range(end + k, end + 4 * k))
    return Q(end + k - 1, 28 * (4 * end + k - 1)) * Q(rising_start, rising_end)


def center_and_derivative(rates, z, active):
    """Block indices start at one; differentiate the flagged numerator wrt t."""
    derivative = Q(0)
    for i in range(len(rates), 0, -1):
        a = rates[i - 1]
        denominator = 1 + a * z
        derivative = -a * derivative / denominator**2
        if i == active:
            derivative += z / denominator
        z = 1 / denominator
    return z, derivative


def odds(x):
    return x / (1 - x)


def check(gaps):
    c = sum(gaps) + 2
    stocks = [c] + [c - consumed for consumed in accumulate(gaps[:8])]
    rates = [block_coefficient(17 - 2 * i, stocks[i], stocks[i+1]) for i in range(8)]
    w = stocks[-1]
    W = Q((w + 2) * (w + 3) * (w + 4), 840)
    d, D = Q(1, 2), Q(5)
    p, q = 1 / (1 + d * W), 1 / (1 + D * W)
    convergents = [center_and_derivative(rates[:i], Q(0), 0)[0] for i in range(9)]
    for i in range(1, 8):
        X, dX = center_and_derivative(rates, p, i)
        Y, dY = center_and_derivative(rates, q, i)
        Md, MD = odds(X), odds(Y)
        tangent = (dX / (1-X)**2) / (dY / (1-Y)**2)
        if i == 1:
            assert (Md - tangent*MD) / (1-tangent) == -1
        elif i == 3:
            assert (Md - tangent*MD) / (1-tangent) == (1 + rates[1]) / rates[0]
        else:
            a, b = odds(convergents[i]), odds(convergents[i - 2])
            assert tangent == ((Md-a)*(Md-b))/((MD-a)*(MD-b))
            # Cross multiply to include a possible infinite companion.
            assert (Md-tangent*MD)*(Md+MD-a-b) == (1-tangent)*(Md*MD-a*b)
    P = convergents[8]
    assert convergents[6] < P
    yd, yD = 1 / (X - P), 1 / (Y - P)
    jc = d + (1 / (convergents[6]-P)-yd) * (D-d) / (yD-yd)
    assert -jc == (1 + rates[7]) / W


def main():
    words = [((a, b, 0, 4, 7, 11, 13, 17, 21)) for a in range(3) for b in range(4)]
    words += [(4,8,3,11,17,23,31,41,51), (7,2,1,13,19,24,30,39,46),
              (13,15,17,19,21,23,25,2,6), (69,60,50,40,30,20,10,4,9)]
    for gaps in words:
        check(gaps)
    print(f'{len(words)} finite inventories, {7*len(words)} tangent checks and {len(words)} terminal identifications verified exactly.')


if __name__ == '__main__':
    main()
