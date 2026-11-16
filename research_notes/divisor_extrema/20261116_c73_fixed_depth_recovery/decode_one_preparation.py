"""Recover the center pair from a single inventory-dependent H(0,t) reading."""
from fractions import Fraction
import json

from blind_center_decoder import public_height, recover, simulate, truth


def preparation(blocks, stock):
    height = public_height(blocks, stock)
    precision = 6 * (height - 1).bit_length() + 6
    return height, precision, Fraction(1, 1 << precision)


def decode_one(blocks, stock, observed):
    height, precision, t = preparation(blocks, stock)
    ratio_height = (1 << precision) * height**2
    oriented, bits = recover(observed, ratio_height)
    ratio = max(oriented, 1 / oriented)
    if ratio == 1:
        raise ValueError("coincident centers")
    estimate = (ratio - 1) / t
    difference = estimate.limit_denominator(height**2)
    low = 1 + (t * difference / (ratio - 1) - 1) / t
    high = low + difference
    if not 1 < low < high or max(low.numerator, low.denominator,
                                high.numerator, high.denominator) > height:
        raise ValueError("no center pair in the public height bound")
    return sorted((1 / low, 1 / high)), bits


def single_observation(gaps, t):
    # Synthesize exactly the one scalar using the original model's two extrema.
    # This separate forward path has access to the test word.
    g, h = simulate(gaps)
    low = (h - 1) / (g - h)
    high = g * low
    return (1 + t * (high - 1)) / (1 + t * (low - 1))


if __name__ == "__main__":
    checks = []
    for gaps in ((1900, 2100), (4200, 4300, 4400)):
        r, c = len(gaps) - 1, sum(gaps) + 2
        _, preparation_bits, t = preparation(r, c)
        observation = single_observation(gaps, t)
        recovered, dyadic_bits = decode_one(r, c, observation)
        assert recovered == truth(gaps)
        checks.append(dict(blocks=r, stock=c, gaps=gaps,
                           preparation_bits=preparation_bits, dyadic_bits=dyadic_bits,
                           centers_verified=True))
    print(json.dumps(checks, indent=2))
