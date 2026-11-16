"""First relative correction of the true column ratio on both alias branches."""
from fractions import Fraction as F
import json
from check_macro_point import Interval


def denominator_slope(x,y):
    a=4*x.sqrt().sqrt()**15
    d=4*(y/x).sqrt().sqrt()**9
    b=F(7,16)*a**5
    l=F(7,16)*d**5
    return l*(1+b)/((1+b*d)*y.sqrt().sqrt()**3)


def main():
    m=Interval('0.199999999','0.200000001')
    x=1-m; y=Interval('0.38767','0.38769')
    u=Interval('0.52080224','0.52083276')
    q=denominator_slope(x,y)
    r=denominator_slope(u,u-m)
    assert q.inside('0.30','0.35') and r.inside('4.4','4.6')
    return {'first_branch':['0.30','0.35'],'middle_branch':['4.4','4.6'],
            'normalization':'y^(-3/4) times denominator log-slope'}
if __name__=='__main__':
    print(json.dumps(main(),indent=2))
