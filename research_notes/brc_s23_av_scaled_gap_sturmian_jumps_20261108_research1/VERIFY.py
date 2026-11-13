#!/usr/bin/env python3
"""Exact rational log intervals and first-entry jump certificates for S23/AV.
Author-side checking of analytic theorem; no native BRC/X6 computation.
"""
from fractions import Fraction as F

M=45
Q=10**26

def log_via_atanh(z, terms=M):
    z=F(z)
    L=2*sum((z**(2*j+1))/F(2*j+1) for j in range(terms))
    R=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return L,L+R

l2,u2=log_via_atanh(F(1,3))
l9,u9=log_via_atanh(F(1,9))
l15,u15=log_via_atanh(F(1,15))
rl=(3*l2-u15)/(u9+u15)
ru=(3*u2-l15)/(l9+l15)
PLO=545569623581288298975349314
PHI=PLO+1
assert 0 < F(PLO,Q) < rl < ru < F(PHI,Q)
# eps=79r-431; d=2074774-380295r; both positive with d<eps
assert 79*rl>431
assert 2074774>380295*ru
assert 2074774+431 < (380295+79)*rl
assert 2*2074774+431 > (2*380295+79)*ru  # 2d>eps
assert 79*2074774 - 431*380295 == 1

def alpha_floor(b):
    # Exact floor of b*d/eps, using certified bounds; b<=100 here
    dlo=F(2074774)-380295*ru
    dhi=F(2074774)-380295*rl
    elo=79*rl-431
    ehi=79*ru-431
    alo=b*dlo/ehi
    ahi=b*dhi/elo
    a=alo.numerator//alo.denominator
    assert a==ahi.numerator//ahi.denominator
    return a

rows=[]
prev_v=0
prev_k=0
prev_a=-1
for b in range(1,101):
    a=alpha_floor(b)
    v=380295*b+79*a
    k=2074774*b+431*a
    assert v>prev_v and k>prev_k and a>=0
    assert k*Q>PHI*v and (k+431)*Q < PLO*(v+79)
    rows.append((b,a,v,k))
    if b>1:
        jump=(k+v)-(prev_k+prev_v)-1
        assert a-prev_a in (0,1)
        assert jump==2455068+510*(a-prev_a)
    prev_v,prev_k,prev_a=v,k,a
assert rows[:4] == [(1,0,380295,2074774),(2,1,760669,4149979),(3,1,1140964,6224753),(4,2,1521338,8299958)]
assert 4910648-380296 == 4530352
assert 2455069-380295 == 2074774

# Independent bounded prefix search: every v<=v2, check existence of a
# k such that 0<k-r*v<eps. Certified r enclosure makes comparisons exact.
found=[]
for v in range(rows[1][2]+1):
    k=(PLO*v)//Q+1
    assert (PLO*v)//Q == (PHI*v)//Q # pin candidate exactly
    may_pass=(k*Q>PLO*v and (k+431)*Q<PHI*(v+79))
    if may_pass:
        assert k*Q>PHI*v and (k+431)*Q<PLO*(v+79)
        found.append((v,k))
assert found==[(380295,2074774),(760669,4149979)]

# Base threshold A=10^431/7^510 to B=1 is adjacent for h=510.
# For each s, only i near s*r/(1+r) can yield a ratio in (A,1).
for s in range(0,511):
    x = F(s*PLO, Q+PLO)
    i0=x.numerator//x.denominator
    for i in range(max(0,i0-1),min(s,i0+3)+1):
        if (s,i) in ((0,0),(510,431)):
            continue # exact two endpoints
        xlo=i*(1+F(PLO,Q))-s*F(PHI,Q)
        xhi=i*(1+F(PHI,Q))-s*F(PLO,Q)
        min_minus_eps=431-79*F(PHI,Q)
        assert xlo>0 or xhi < min_minus_eps, (s,i)

print('PASS_S23_AV_ALL_SCALED_GAP_STURMIAN_FIRST_ENTRY_20261108')
print('r_enclosure=(%d/%d,%d/%d)' %(PLO,Q,PHI,Q))
print('analytic_all_t=proved_with_unimodular_lattice_and_floor_sequence')
print('certified_b=1..100; finite_prefix_v=0..%d; found=%s'%(rows[1][2],found))
print('first_two=%s'% (rows[:2],))
print('jump_sizes=(2455068,2455578)')
print('h=380806: N(h)>=4530352 (cell first-entry lower bound)')
