#!/usr/bin/env python3
"""R285: exact positive-tree kernel, crosschecked BRC coefficients,
plus rational checks of a hand-proved, conservative effective gap threshold.
Only the six-edge ordered positive-count auxiliary BRC, not P000 native physics.
Run: python3 R285_verify_effective_gap.py
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from json import dumps
from math import comb
from pathlib import Path

MAX_SERIES=240
MAX_WORD_DP=160
MASSIVE_TAIL_INDEX=10_000_000

# Positive tree grammar: S=y^4+(2y+y^3)S+y*S^2.
def get(xs,j):
    return xs[j] if 0 <= j < len(xs) else 0

s=[0]*4
for n in range(4,MAX_SERIES+1):
    s.append(int(n==4)+2*get(s,n-1)+get(s,n-3)
             +sum(s[i]*s[n-1-i] for i in range(n)))
r=[1,1]+[get(s,n) for n in range(2,MAX_SERIES+1)]
assert s[:12] == [0,0,0,0,1,2,4,9,20,45,103,238],s[:12]
assert all(s[n]>=2*s[n-1]>0 for n in range(5,MAX_SERIES+1))

# Independent Catalan/tree coefficient formula.
# S= sum_{j>=0} Catalan(j)*y^(5*j+4)*(1-2y-y^3)^(-2j-1).
def tree_closed_coefficient(n):
    z=0
    for j in range((n-4)//5+1):
        Cj=comb(2*j,j)//(j+1)
        left=n-5*j-4
        for b in range(left//3+1):
            a=left-3*b
            z += Cj*comb(2*j+a+b,a+b)*comb(a+b,a)*2**a
    return z
for n in range(4,151):
    assert s[n] == tree_closed_coefficient(n),('catalan',n)

# Independent signed Laurent kernel g=sqrt(h/q) from R284's ODE,
# and the new positive-tree identity (1-y^3)g=a-2yr.
g_tree=[]
for n in range(MAX_SERIES+1):
    aj=int(n==0)+2*int(n==2)-int(n==3)
    g_tree.append(aj-2*get(r,n-1)+get(g_tree,n-3))
g_ode=[1]
for n in range(MAX_SERIES):
    top=((2*n-2)*get(g_ode,n)+(n-1)*get(g_ode,n-1)
        +(2*n-2)*get(g_ode,n-2)-(n-3)*get(g_ode,n-3))
    assert top%(n+1)==0,('ODE divisibility',n)
    g_ode.append(top//(n+1))
assert g_tree==g_ode
assert g_tree[:10]==[1,-2,0,0,-2,-2,-4,-10,-20,-44]

# K=[(y-1)P7-P8*g] / [2y(1+y)], coefficients vs original ordered BRC.
P7=[-1,1,-8,4,-6,11,-6,1]
P8=[1,-2,1,-8,6,-3,7,-5,1]
A=[0]*9
for i,v in enumerate(P7):
    A[i]-=v
    A[i+1]+=v
K=[]
for m in range(MAX_SERIES-1):
    num=get(A,m+1)-sum(v*get(g_tree,m+1-i) for i,v in enumerate(P8))
    assert num%2==0,('K parity',m)
    K.append(num//2-get(K,m-1))
assert K[:12] == [1,1,-2,-3,1,2,-2,-3,-2,-6,-13,-24]
p=[1,-1,0,-2,1]
PK=[sum(p[j]*get(K,m-j) for j in range(len(p))) for m in range(len(K))]

EDGES={(0,0):(2,-1,-1),(0,1):(2,+1,-1),(1,0):(0,-1,-1),
       (1,1):(0,+1,-1),(2,0):(1,+1,+1),(2,1):(2,+1,-1)}
dp={(0,2,+1,0):1}
compared_even=compared_odd=0
for n in range(MAX_WORD_DP+1):
    h=defaultdict(int)
    for (q,prev,eps,k),multiplicity in dp.items():
        if q==0: h[(eps,k)]+=multiplicity
    if n>=8 and n%2==0:
        assert h[(+1,-4)]-h[(-1,-4)]==K[(n-8)//2],('original gap even',n)
        compared_even+=1
    if n>=5 and n%2==1:
        assert h[(-1,-3)]-h[(+1,-5)]==PK[(n-5)//2],('original gap odd',n)
        compared_odd+=1
    nxt=defaultdict(int)
    for (q,prev,eps,k),v in dp.items():
        for bit in (0,1):
            if prev==0 and bit==0:continue
            qq,eta,c=EDGES[(q,bit)]
            nxt[(qq,bit,eps*eta,eta*k+c)]+=v
    dp=nxt

# Exact rational checks for all constants used by the analytic certificate.
# Analytical inequality statements are proved in companion note, not inferred
# from these checks or from limited coefficient calculation.
R=Fraction(1,2)
poly_bound=sum(Fraction(abs(c),2**j) for j,c in enumerate(P8))
assert poly_bound==Fraction(991,256)<4
p_circle_bound=sum(Fraction(abs(c),2**j) for j,c in enumerate(p))
assert p_circle_bound==Fraction(29,16)<2
assert Fraction(72,35)<Fraction(9,4)
assert Fraction(3,8)*Fraction(7,200)==Fraction(21,1600)>Fraction(1,80)
assert Fraction(2,5)*Fraction(9,200)==Fraction(9,500)<Fraction(1,50)
assert Fraction(1,2)*Fraction(1,80)==Fraction(1,160)
assert Fraction(12,1)+Fraction(1,50)<Fraction(121,10)
assert Fraction(2,5)*121*5*30==7260
assert Fraction(2,5)*121*5*Fraction(3,2)==363
assert 363*240000==87120000 and 87120000**2<1_000_000**3
assert 200*384*2560 < 1_000_000**2 # weaker but fully integer and sufficient
margin=Fraction(1,640)-Fraction(7261,MASSIVE_TAIL_INDEX)-Fraction(1,2560)
assert margin==Fraction(17831,40_000_000)>Fraction(1,2500)
assert (2*MASSIVE_TAIL_INDEX+6)%2==0
assert (2*MASSIVE_TAIL_INDEX+3)%2==1

out={
 'schema':'ENTERPRISE_MATH_R285_EFFECTIVE_CENTRAL_GAP_V1',
 'status':'PASS', 'model':'six-edge ordered positive-count clean reset BRC auxiliary only',
 'new_exact_tree_equation':'S=y^4+(2y+y^3)S+y*S^2; r=1+y+S',
 'positive_coefficients':'S_n>=2*S_(n-1)>0 for all n>=5; Catalan expansion proves S_n>0 for n>=4',
 'tree_grammar_checked_through':MAX_SERIES,
 'catalan_independent_exact_check_range':[4,150],
 'g_ode_equals_positive_tree_laurent_series_through':MAX_SERIES,
 'original_six_edge_clean_DP_max_length':MAX_WORD_DP,
 'even_gap_comparisons':compared_even,'odd_gap_comparisons':compared_odd,
 'effective_tail_index_yK':MASSIVE_TAIL_INDEX,
 'proven_effective_even_original_length_lower':2*MASSIVE_TAIL_INDEX+6,
 'proven_effective_odd_original_length_lower':2*MASSIVE_TAIL_INDEX+3,
 'analytic_tail_claim':'for Q=1 or p, [y^(n-1)]QK > rho^(-n)/(2500*n^(3/2)), every n>=10^7',
 'analytic_tail_method':'explicit circle R=1/2 Cauchy bound + exact binomial coefficient inequalities, written in proof',
 'finite_execution_is_not_infinite_proof':True,
 'n_10000000_coefficients_not_computed':True,
 'margin_fraction':str(margin),
 'R284_dependencies':'exact single-kernel K representation; R279/R283 Laurent input',
 'claim_scope':'central pairwise gap positivity, NOT unique global peak/6-channel equality/physical transfer',
 'driver_review':'NOT_DONE', 'native_claim':'NOT_OBTAINED',
 'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()
}
target=Path(__file__).with_name('EXACT_EVIDENCE.json')
target.write_text(dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('PASS: positive Catalan tree series 0..%d, 6-edge DP 0..%d, tail rational bounds; effective original thresholds even %d / odd %d' %
      (MAX_SERIES,MAX_WORD_DP,2*MASSIVE_TAIL_INDEX+6,2*MASSIVE_TAIL_INDEX+3))
print('Evidence',target)
