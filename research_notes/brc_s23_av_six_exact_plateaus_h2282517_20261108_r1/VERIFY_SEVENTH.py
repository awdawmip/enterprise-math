"""Exact arithmetic premises for seventh S23/AV capacity plateau.

Uses the same certified 45-term rational atanh enclosure as VERIFY_FIRST_JUMP.py.
"""
from fractions import Fraction

def bound(a,b,terms=45):
    z=Fraction(a-b,a+b)
    s=sum((2*z**(2*k+1)/(2*k+1) for k in range(terms)),Fraction())
    rem=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return s,s+rem
l2,u2=bound(2,1);l87,u87=bound(8,7);l54,u54=bound(5,4)
rlo=(3*l2-u87)/(u54+u87)
rhi=(3*u2-l87)/(l54+l87)
lo,hi=545569623581288298975349314,545569623581288298975349315
q=10**26
assert Fraction(lo,q)<rlo<rhi<Fraction(hi,q)
epslo,epshi=79*rlo-431,79*rhi-431
etalo,etahi=2074774-380295*rhi,2074774-380295*rlo
assert 4*epshi<7*etalo<7*etahi<5*epslo
v6=2282007
v7=7*380295+4*79
k7=7*2074774+4*431
assert (v7,k7)==(2662381,14525142)
N7=v7+k7-(v6+1)
assert N7==14905515
hstart=v6+511
hend=2455068
assert hstart==2282518 and hstart<=hend<v7
assert hend+1==380295+2074774
assert k7>hend and N7>rhi*hend
# For every left endpoint up to hend, W_i (i<=7) is eligible,
# and the exact min-gap lemma applies for h<m1.
# The symbolic least-i / shifted-prefix argument is in SEVENTH_PLATEAU.md.
print('PASS_S23_AV_SEVENTH_PLATEAU')
print('b7=(a,v,k)=(4,2662381,14525142)')
print('N(h)=14905515 for every integer 2282518<=h<=2455068')
print('new_exact_horizons='+str(hend-hstart+1))
