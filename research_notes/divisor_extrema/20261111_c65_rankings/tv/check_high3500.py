"""Rational threshold checks for the case splits in HIGH_3500.md."""
from fractions import Fraction as Q

b,h,d=Q(21,10),Q(377,378),Q(99,100)
assert Q(76,129)<Q(3,5)
assert Q(4913,8192)<Q(3,5)
assert Q(63)*Q(17,92)**2<3
assert Q(7)/(1+Q(7,256))**2>6 and Q(3,16)>Q(6,256)
bounds={
    'many_defects': h*d*b**12, 'small_initial_stock': h*d*b*4096,
    'double_or_longer': h*d*3840,
    'negative_initial_empty': h*d*16*240,
    'negative_initial_single_many': h*d*16*Q(50*64,46)*b**2,
    'negative_off_diagonal': h*600*16*b,
    'negative_returns': h*d*16*Q(50*64,46)*240,
    'nonnegative_many': h*b**3*600, 'nonnegative_few': h*b*49508,
}
assert min(bounds.values())>3500
assert Q(53,37)*3500>5013
if __name__=='__main__':
    print({case: value//1 for case,value in bounds.items()})
