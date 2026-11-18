#!/usr/bin/env python3
"""Exact all-real Bernstein certificate for S23 conditional AV n=3 symmetric
rational kernel, frozen science enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
All assertions use Python unbounded ints/Fraction. Floats only for printed diagnostics.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, lcm

M=10**14
H=sorted(h for h in product(range(4),repeat=3) if sum(h)==3)
MULT=[factorial(3)//(factorial(h[0])*factorial(h[1])*factorial(h[2])) for h in H]
K=[[0, 0, 0, 100000000000000, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1747112991682, 0, 98252887008318, 0], [121269627318, 444444444444, 11084232590318, 0, 22195343701318, 12471322964682, 16568032896677, 31974633557918, 10312735866, 5130407481459], [5375704166, 0, 26622927530, 0, 26878520682, 0, 5071818328318, 2418691424318, 32373716247318, 60076896847668]]
assert len(H)==10 and sum(MULT)==27
assert len(K)==4 and all(len(row)==10 and min(row)>=0 and sum(row)==M for row in K)
LOWER=F(5211,21952)
T=LOWER+F(49,100_000_000_000) # improvement to within 4.9e-10 of exact fiber lower bound

def residual(a,c):
    z=(1-a)*c
    p=(a,z,(1-a)*(1-c))
    w=[comb(3,k)*z**(3-k)*(1-z)**k for k in range(4)]
    return [MULT[j]*p[0]**h[0]*p[1]**h[1]*p[2]**h[2]
            -sum(w[k]*K[k][j] for k in range(4))/M for j,h in enumerate(H)]

def init():
    nodes=[F(1,2)+F(i,8) for i in range(4)] # u,v=0,1/3,2/3,1
    U=[[F(1),F(0),F(0),F(0)],[-F(5,6),F(3),-F(3,2),F(1,3)],
       [F(1,3),-F(3,2),F(3),-F(5,6)],[F(0),F(0),F(0),F(1)]]
    val=[[residual(a,c) for c in nodes] for a in nodes]
    cp=[[[sum(U[i][p]*U[j][q]*val[p][q][h] for p in range(4) for q in range(4))
          for j in range(4)] for i in range(4)] for h in range(10)]
    den=lcm(*(v.denominator for h in cp for row in h for v in row))
    B=[[[int(v*den) for v in row] for row in h] for h in cp]
    for a,c in [(F(11,16),F(13,16)),(F(17,32),F(19,32)),(F(5,8),F(3,4))]:
        u=(a-F(1,2))/F(3,8);v=(c-F(1,2))/F(3,8)
        bu=[comb(3,i)*u**i*(1-u)**(3-i) for i in range(4)]
        bv=[comb(3,j)*v**j*(1-v)**(3-j) for j in range(4)]
        assert [sum(F(B[h][i][j],den)*bu[i]*bv[j] for i in range(4)
                    for j in range(4)) for h in range(10)] == residual(a,c)
    return B,den

def hull(B):return max(sum(max(0,B[h][i][j]) for h in range(10))
                        for i in range(4) for j in range(4))
def bisect(B,axis):
    L=[[[0]*4 for _ in range(4)] for _ in range(10)]
    R=[[[0]*4 for _ in range(4)] for _ in range(10)]
    for h in range(10):
        for v in range(4):
            p=[B[h][i][v] if axis==0 else B[h][v][i] for i in range(4)]
            lo=[8*p[0],4*(p[0]+p[1]),2*(p[0]+2*p[1]+p[2]),p[0]+3*p[1]+3*p[2]+p[3]]
            hi=[lo[3],2*(p[1]+2*p[2]+p[3]),4*(p[2]+p[3]),8*p[3]]
            for i in range(4):
                if axis==0:L[h][i][v]=lo[i];R[h][i][v]=hi[i]
                else:L[h][v][i]=lo[i];R[h][v][i]=hi[i]
    return L,R

def main():
    # Independent exact test of the existing two-point obstruction.
    l0=residual(F(1,2),F(1,2))
    l1=residual(F(5,7),F(7,8))
    assert sum(max(0,u-v) for u,v in zip(l0,l1))==2*LOWER
    B,den=init();stack=[(B,den,0)];splits=leaves=maxdepth=0;maxleaf=F(0)
    while stack:
        block,d,depth=stack.pop()
        num=hull(block)
        if num*T.denominator<=T.numerator*d:
            leaves+=1;maxdepth=max(maxdepth,depth)
            maxleaf=max(maxleaf,F(num,d))
        else:
            assert depth<140 and splits<200000,('UNRESOLVED',splits,depth,float(F(num,d)))
            left,right=bisect(block,depth%2)
            stack.extend([(right,8*d,depth+1),(left,8*d,depth+1)])
            splits+=1
    assert leaves==splits+1 and maxleaf<=T and LOWER<T
    print('PASS_S23_N3_RATIONAL_NEAR_FIBER_OPTIMAL_BERNSTEIN_20261107')
    print('frozen_science','43ec6098b1330ae86d0a7863be336c5d97f6ef34')
    print('parameter_domain','a,c in [1/2,7/8], all real')
    print('histogram_multiplicities',MULT,'total',sum(MULT))
    print('row_sums',[sum(row) for row in K], 'M',M)
    print('positive_kernel_cells',sum(x>0 for row in K for x in row))
    print('exact_fiber_lower',LOWER, 'decimal',format(float(LOWER),'.17f'))
    print('new_all_real_upper',T,'decimal',format(float(T),'.17f'))
    print('gap_exact',T-LOWER)
    print('Bernstein_leaves',leaves,'splits',splits,'max_depth',maxdepth)
    print('largest_accepted_hull',maxleaf,'decimal',format(float(maxleaf),'.17f'))
if __name__=='__main__':main()
