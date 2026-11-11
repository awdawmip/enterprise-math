"""Exact enclosure of the limiting multiplier of the eventual fourth suffix."""
from fractions import Fraction as Q
import json
from edge_helpers import terminal_weights, transition_list
from ratio_certificate import coefficients, outward


def derivative(r, c, suffix, x):
    edges, remaining = transition_list(r, c, suffix)
    slope = Q(1)
    for tau, rho in edges:
        denom = tau + 1 + (rho - 1) * x
        slope *= tau * abs(rho - 1) / denom**2
        x = tau / denom
    a,b,d = terminal_weights(remaining)
    return slope * d*(7*a+b) / (7*a+d+(b-d)*x)**2


def run():
    x, y = Q(0), Q(1)
    for j in reversed(range(4, 18)):
        alpha,beta = coefficients(j)
        x,y = 1/(alpha-beta*x),1/(alpha-beta*y)
    # The derivative ratio of two fractional-linear maps is the square of
    # a positive fractional-linear function, hence monotone or constant.
    ratios = [derivative(3,4,(0,0,2,0),v)/derivative(3,4,(1,1,0,0),v)
              for v in (x,y)]
    return {'k':18, 'derivative_ratio_interval':[
        outward(min(ratios),39),outward(max(ratios),39,True)]}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
