#!/usr/bin/env python3
"""R291 exact all-integer checks for the BRC auxiliary gap cone.
No float/scientific propagator: count variable y, branch-resolved six-edge DP.
"""
from collections import defaultdict
from math import comb
import json

J=70
DP_N=100
M=4*J+6

def truncmul(a,b,N=J):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for k in range(N-i+1):
                if b[k]: out[i+k]+=x*b[k]
    return out

def shift(a,d):
    return [0]*d+a[:J+1-d]

h=[0]*(J+1)
for n in range(J+1):
    v=int(n==4)
    for d,c in ((1,1),(2,2),(3,1),(4,1)):
        if n>=d:v+=c*h[n-d]
    for d,c in ((1,1),(2,2),(3,1)):
        if n>=d:v+=c*sum(h[a]*h[n-d-a] for a in range(n-d+1))
    h[n]=v
assert h[:8]==[0,0,0,0,1,1,3,6]
b=[int(n==0)+h[n] for n in range(J+1)]
w=[b[n]+(b[n-1] if n else 0) for n in range(J+1)]
assert w[:8]==[1,1,0,0,1,2,4,9]
wp=[[1]+[0]*J]
for m in range(M+3):wp.append(truncmul(wp[-1],w))

# q=1,2 universal binomial comparison with certificate ratios
ratio_inequalities=0
for j in range(1,J+1):
    for q in (1,2):
        for r in range(j,M+1):
            if (r-j+1)*(r-j+2)>=q*j*(r+1):
                for ell in range(1,j+1):
                    assert comb(r,ell)>=q*comb(r+1,ell-1)
                    ratio_inequalities+=1
                break
        else:raise AssertionError((j,q))

# Explicit forms: G_minus=(1+h) w^(m-2) (1-yw),
# G_plus=(1+h) w^m (1-y+y^2-yw).
def gap(s,m):
    r=(m-2 if s=='-' else m)
    W=wp[r]
    z=[0]*(J+1)
    for j in range(J+1):
        if s=='-':
            z[j]=W[j]-(wp[r+1][j-1] if j>=1 else 0)
        else:
            z[j]=W[j]-(W[j-1] if j>=1 else 0)+(W[j-2] if j>=2 else 0)-(wp[r+1][j-1] if j>=1 else 0)
    return truncmul(b,z)

G={}
for s in ('+','-'):
    for m in range(1 if s=='+' else 2,M+1):
        G[s,m]=gap(s,m)

strict_wedge_checks=0
sharp_quadratic_checks=0
for (s,m),coeff in G.items():
    r=m if s=='+' else m-2
    q=2 if s=='+' else 1
    for j in range(J+1):
        if (r>=4*j if s=='+' else r>=3*j):
            assert coeff[j]>0,(s,m,j,coeff[j])
            strict_wedge_checks+=1
        if j==0 or (r>=j and (r-j+1)*(r-j+2)>=q*j*(r+1)):
            assert coeff[j]>=0,(s,m,j,coeff[j])
            sharp_quadratic_checks+=1

# Independent full-affine source DP with forbidden consecutive 00.
EDGES=(((2,-1,-1),(2,1,-1)),((0,-1,-1),(0,1,-1)),((1,1,1),(2,1,-1)))
states={(0,1,0,False):1}
dp_checks=0
for n in range(DP_N+1):
    counter=defaultdict(int)
    for (q,e,k,prev0),count in states.items():
        if q==0:counter[e,k]+=count
    for s in ('+','-'):
        e=1 if s=='+' else -1
        for m in range(1 if s=='+' else 2,min(M,n+10)+1):
            j=(n-m-2)//2
            expected=G[s,m][j] if n>=m+2 and ((n-m-2)%2==0) and j<=J else 0
            actual=counter[e,-m]-counter[e,-m-2]
            assert expected==actual,(n,s,m,j,actual,expected)
            dp_checks+=1
    nxt=defaultdict(int)
    for (q,e,k,prev0),count in states.items():
        for bit in (0,1):
            if prev0 and bit==0:continue
            q2,eta,d=EDGES[q][bit]
            nxt[q2,eta*e,eta*k+d,bit==0]+=count
    states=nxt
result={
    'schema':'EM_R291_UNIFORM_DISPLACEMENT_CONE_V1',
    'status':'PASS','arithmetic':'Python arbitrary-precision integers',
    'h_degree_max':J,'power_index_max':M,'source_dp_length_max':DP_N,
    'binomial_inequalities_tested':ratio_inequalities,
    'strict_linear_cone_coefficient_checks':strict_wedge_checks,
    'quadratic_cone_coefficient_checks':sharp_quadratic_checks,
    'raw_six_edge_gap_comparisons':dp_checks,
    'example_minus_11':G['-',11][:10],
    'example_plus_13':G['+',13][:10],
    'proof_scope':'all m,j by universal binomial injection; local DP and series only finite corroboration',
    'native_claim':False,'driver_review':False,'math_admitted':False
}
print(json.dumps(result,ensure_ascii=False,indent=2))
