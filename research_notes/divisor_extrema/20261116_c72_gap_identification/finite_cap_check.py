"""Use the exact attainable inner-column maximum to bound first landings."""
from fractions import Fraction
from math import prod
from verify_strip import ratio_without_center

Q = Fraction
COEFFICIENTS = ((Q(3, 32), Q(15, 32)), (Q(3, 2), Q(15, 8)), (Q(6), Q(3)))


def maximum_or_one(v):
    rho = Q(4 * v + 3, v + 3)
    tau = Q(28 * (4 * v + 3) * (4 * v + 2), (v + 12) * (v + 2))
    y = prod((Q(4 * j + 1, 4 * (j + 1)) for j in range(3, v + 1)), start=Q(1))
    x = Q(840, (v + 2) * (v + 3) * (v + 4))
    cap = Q(1)
    for w in range(v, 1, -1):
        # All smaller w have rho at most this rho, and all outputs lie
        # between 1 and the rho of their block.
        if rho <= cap:
            break
        for a, b in COEFFICIENTS:
            t = y * (x * a + b) / (1 + x * y * a)
            cap = max(cap, (rho + tau * t) / (1 + tau * t))
        if w > 2:
            rho *= Q(4 * w - 1, 4 * (w + 2))
            tau *= Q((4 * w - 1) * (w + 2) * (4 * w - 2),
                     4 * (w + 11) * (4 * w + 2) * (w + 1))
            y *= Q(4 * w + 4, 4 * w + 1)
            x *= Q(w + 4, w + 1)
    return cap


def main():
    c = 2501
    v = 1150
    rho_next = prod((Q(4 * j + 5, 4 * (j + 5))
                     for j in range(v + 1, c + 1)), start=Q(4))
    for v in range(1150, c):
        cap = maximum_or_one(v)
        score = ratio_without_center(c, v) * (1 - rho_next) * cap / 4
        assert rho_next < Q(4, 5)
        if score >= 1:
            assert v == 1197 and Q(101182, 100000) < score < Q(101183, 100000)
            print("first failed sufficient test:", v, "cap", float(cap), "score", float(score))
            break
        if v == 1196:
            assert Q(99945, 100000) < score < Q(99946, 100000)
        if v >= 1190:
            print(v, "cap", float(cap), "score", float(score))
        rho_next *= Q(4 * (v + 6), 4 * (v + 1) + 5)


if __name__ == "__main__":
    main()
