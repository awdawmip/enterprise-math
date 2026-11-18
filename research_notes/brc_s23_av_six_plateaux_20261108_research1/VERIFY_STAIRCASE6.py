#!/usr/bin/env python3
"""Exact rational arithmetic certificate for first six S23/AV capacity plateaux."""
from fractions import Fraction as F
Q=10**26
LO=545569623581288298975349314
HI=LO+1
V0=380295
K0=2074774
HMAX=2282517

def log_bound(z,terms=45):
    s=F(0);t=z
    for j in range(terms):
        s+=2*t/(2*j+1)
        t*=z*z
    return s,s+2*t/((2*terms+1)*(1-z*z))
l2,u2=log_bound(F(1,3));l9,u9=log_bound(F(1,9));l15,u15=log_bound(F(1,15))
a,b=3*l2-u15,3*u2-l15;c,d=l9+l15,u9+u15
assert F(LO,Q)<a/d and b/c<F(HI,Q)
e_lo=79*LO-431*Q;e_hi=79*HI-431*Q
eta_lo=11*LO-60*Q;eta_hi=11*HI-60*Q
g_lo=371*Q-68*HI;g_hi=371*Q-68*LO
s_lo=K0*Q-HI*V0;s_hi=K0*Q-LO*V0
assert 0<s_lo<s_hi<e_lo
assert eta_lo>4800*e_hi
assert 0<g_lo and g_lo>6*e_hi
assert e_hi*HMAX<7*Q
assert e_hi*(HMAX+79)<7*Q
assert 79*g_hi+e_hi*HMAX<8*Q
assert 431*4800-60+79*4800-11>HMAX
# Any difference between points in D_H can be written a*u + b*w, det(u,w)=-1.
# For a hypothetical gap x strictly between 0 and eps,
# b=79*x-eps*dv is an integer in (-7,7), hence -6<=b<=6.
# For every nonzero b, exact log bounds locate the unique integer a that
# could satisfy 0<a*eps+b*eta<eps. The minimal triangle needed for such a
# displacement is max(sum_positive_components, sum_negative_components).
assert e_hi*HMAX<7*Q and e_hi*(HMAX+79)<7*Q
min_cost=10**20
for beta in range(-6,7):
    if beta==0:continue
    c=abs(beta)
    flo_lo=(c*eta_lo)//e_hi
    flo_hi=(c*eta_hi)//e_lo
    assert flo_lo==flo_hi
    a=-flo_lo if beta>0 else flo_lo+1
    dv=79*a+11*beta
    dj=431*a+60*beta
    low=(a*e_lo if a>=0 else a*e_hi)+(beta*eta_lo if beta>=0 else beta*eta_hi)
    up=(a*e_hi if a>=0 else a*e_lo)+(beta*eta_hi if beta>=0 else beta*eta_lo)
    assert 0<low<up<e_lo
    cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    assert cost>HMAX,(beta,a,dv,dj,cost)
    min_cost=min(min_cost,cost)
    print('POTENTIAL_SUBEPS_GAP',beta,'a',a,'dv',dv,'dj',dj,'min_triangle_size',cost)
assert min_cost==2455069
print('PASS_GLOBAL_SPACING_ARITHMETIC_HMAX',HMAX,'min_sub_eps_gap_triangle',min_cost,'eta_over_eps_gt',4800)

rows=[]
for i in range(1,7):
    a_i=(i*s_lo)//e_hi
    assert a_i*e_hi < i*s_lo and i*s_hi<(a_i+1)*e_lo
    v_i=i*V0+79*a_i;k_i=i*K0+431*a_i
    delta_lo=i*s_lo-a_i*e_hi
    delta_hi=i*s_hi-a_i*e_lo
    assert 0<delta_lo<delta_hi<e_lo
    assert k_i>HMAX if i>=2 else k_i>1902143
    M_i=k_i+v_i if i==1 else k_i+v_i-(rows[-1][2]+1)
    H_i=v_i+510
    rows.append((i,a_i,v_i,k_i,M_i,H_i))
    print('ROW',i,'a',a_i,'V',v_i,'K',k_i,'plateau_min_prefix',M_i,'plateau_h_end',H_i,'delta_num_interval',delta_lo,delta_hi)
    for m in range(1,7):
        L=v_i+68+79*m
        K=k_i+371+431*m
        wlo=delta_lo+g_lo-m*e_hi
        whi=delta_hi+g_hi-m*e_lo
        assert 0<wlo and whi<g_lo
        if m==6: assert L>=v_i+510
        assert K>H_i and k_i+3498<=M_i
    ell=H_i*Q//LO+1;k=HI*H_i//Q+1
    assert LO*ell>Q*H_i and k*Q>HI*H_i and ell<=M_i and k<=M_i
    print('PASS_PLATEAU_COVERAGE',i,'start',510 if i==1 else rows[-2][5]+1,'end',H_i,'N_exact',M_i,'outer',(ell,k))
assert [r[1] for r in rows]==[0,1,1,2,2,3]
assert [r[4] for r in rows]==[2455069,4530352,6605047,8680331,10755026,12830310]
assert [r[5] for r in rows]==[380805,761179,1141474,1521848,1902143,2282517]
assert all(rows[i][4]>rows[i-1][4] for i in range(1,6))
# At H > K1 the low-v, large-j cells cannot use W1 (K1-j<0).
# They instead use W6: j>K1 implies v+j>=K1+1>=V5+1.
V5=rows[4][2]
V6,K6,M6=rows[5][2],rows[5][3],rows[5][4]
assert K0+1>V5+1
assert K6+V6-(K0+1)<=M6
print('PASS_LARGE_J_REPAIR_BY_LAST_WITNESS',K0+1,M6)
print('PASS_S23_AV_SIX_ANALYTIC_PLATEAUX_AND_FIVE_EXACT_JUMPS',HMAX)
