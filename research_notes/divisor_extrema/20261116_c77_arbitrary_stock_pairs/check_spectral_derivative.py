"""Exact checks of derivative and fractional orders for adjacent-stock precision."""
from fractions import Fraction as Q
import json


def main():
    b = Q(7,16)
    x_prefactor = Q(15, 4)
    y_prefactor = Q(21, 2)
    lower_x_order = x_prefactor - Q(9, 4)
    upper_y_order = y_prefactor
    assert lower_x_order == Q(3, 2) and upper_y_order != lower_x_order
    assert lower_x_order.denominator == upper_y_order.denominator == 2
    assert Q(15) - Q(9,4) == Q(51,4)
    assert Q(51,4) + x_prefactor == Q(66,4)
    # At x=4^(-4/15), A=1. The derivative in stock, restricted to
    # this line, has absolute value proportional to D^(14/3)|1-D|/(1+bD)^2.
    d = Q(2)
    derivative = Q(14,3)/d + 1/(d-1) - 2*b/(1+b*d)
    assert derivative == Q(43,15)
    return dict(signed_branch_x0=str(lower_x_order), signed_branch_y0=str(upper_y_order),
                stock_derivative_log_slope_in_D_at_D2=str(derivative))


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
