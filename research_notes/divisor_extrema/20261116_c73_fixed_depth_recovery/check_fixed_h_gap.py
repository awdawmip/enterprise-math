"""Diagnostic: only fixed g and public stock enter the dyadic readout."""
from fractions import Fraction
from blind_center_decoder import blind, simulate, truth


def valuation(x):
    n, d = x.numerator, x.denominator
    assert n
    return (n & -n).bit_length() - (d & -d).bit_length()


def gap_readout(r,c,g):
    center, _ = blind(r,c,g)
    order1 = valuation(g/center-1)
    order2 = valuation(1/(g*center)-1)
    assert order1 != order2
    return max(order1, order2)


if __name__=='__main__':
    for gaplist in [(1200, 1900, 1600, 2100), (1800, 1300, 1700, 2000),
                    (2000, 1800, 1350, 1700), (2400, 1750, 1900, 1400)]:
        c=sum(gaplist)+2
        g,h=simulate(gaplist)
        value=gap_readout(len(gaplist)-1,c,g)
        assert abs(value - 3*min(gaplist)) < 10*c.bit_length()
        print(c,gaplist.index(min(gaplist))+1,value,3*min(gaplist))
