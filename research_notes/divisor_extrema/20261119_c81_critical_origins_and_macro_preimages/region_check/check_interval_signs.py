"""Compare the integer root sign oracle with direct fractions at bracketing endpoints."""
from fractions import Fraction as F

from crosscheck_region import h
from endpoint_certificate import Q, START, right_min, zero_bracket
from union_area import area

def check():
    checks=0
    for d in (START,F(11,10),F(1119,1000),F(9,8),F(2),F(3),F(4)):
        for left in (True,False):
            lo,hi=zero_bracket(d,left)
            target=right_min() if left else F(4)
            assert h(F(lo,Q),d,not left)>=target>h(F(hi,Q),d,not left)
            checks+=1
    all_cells={"n":4,"row_runs":[[i,0,4] for i in range(4)]}
    lo,hi=area(all_cells,64)
    assert lo<=10**12<=hi
    return checks

if __name__=='__main__':
    print(check(), "exact rational sign checks and one unit-mass union passed")
