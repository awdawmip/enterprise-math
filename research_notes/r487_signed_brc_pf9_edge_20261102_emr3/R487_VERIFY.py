#!/usr/bin/env python3
"""R487 exact rank-nine signed BRC right-edge positivity certificate.
Frozen scientific source: Enterprise Math R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f.
This is author-side proof evidence for the auxiliary scalar; no native X6 claim.
Python standard library; all arithmetic exact.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import permutations
import json

P9 = [
30488174811436077344, 170919639444739933520,
457015367175128473468, 769634476094022208096,
907002495747852366161, 786447369487609119500,
512937008031624899686, 251983678844847048544,
91023587483000222637, 22353777136781862972,
2702476171614340312, -361186673732372288,
-231379626293779248, -41490969483215808,
-849995956369408, 995936342073344,
184509506322432, 12350460788736,
]
DEN9 = 120989018964005127936000000000

def B(n,j): return comb(n,j) if 0 <= j <= n else 0
def C(k): return comb(2*k,k)//(k+1)
def H(k,t):
    r=2*k+1
    if t<2 or t>r: return 0
    return B(r+t,2*t)*sum(B(r-t,q)*(B(2*t,r-2*q)-B(2*t,r-2*q-1)) for q in range(r-t+1))
def add(a,b):
    out=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: out[i+j]+=x*y
    return out
def prod(seq):
    out=[F(1)]
    for x in seq: out=mul(out,x)
    return out
def ev(poly,x):
    result=F(0)
    for c in reversed(poly): result=result*x+c
    return result

def p(t):
    """Closed Catalan polynomial from R484/485; independently checked vs raw signed convolution."""
    result=[F(0)]
    for q in range((t-1)//2+1):
        factors=[]
        for h in range(q): factors.extend(([-h,1],[1-h,1]))
        for ell in range(2-t,t+2):
            if ell not in range(1-2*q,1): factors.append([ell,2])
        result=add(result,[F(B(t-1,2*q)*4**q,factorial(2*t))*v for v in prod(factors)])
    return result

ps={t:p(t) for t in range(2,12)}
D=[[F(1)]]
for m in range(1,10):
    z=[F(0)]
    for l in range(1,m+1):
        z=add(z,[(-1)**(l-1)*v for v in prod([ps[l+2]]+[ps[2]]*(l-1)+[D[m-l]])])
    D.append(z)

assert len(D[9])==55
factor9=prod([[0,1]]*9+[[1,1]]*9+[[1,2]]*9+[[3,2]]*9+[[2,1]])
expected=[F(z,DEN9) for z in mul(factor9,P9)]
assert len(expected)==55 and D[9]==expected, '55 exact coefficient identities'
shift4=[sum(P9[i]*B(i,j)*4**(i-j) for i in range(j,18)) for j in range(18)]
assert len(shift4)==18 and all(v>0 for v in shift4)
small=[int(ev(P9,k)) for k in (1,2,3)]
assert all(v>0 for v in small)

rawchecks=0
for k in range(1,101):
    for t in range(2,12):
        assert ev(ps[t],k)*C(k)==H(k,t), (k,t)
        rawchecks+=1

def det_bareiss(a):
    a=[row[:] for row in a]
    n=len(a); sign=1; divisor=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]),None)
            if j is None: return 0
            a[i],a[j]=a[j],a[i]
            sign*=-1
        pivot=a[i][i]
        for j in range(i+1,n):
            for q in range(i+1,n):
                z=a[j][q]*pivot-a[j][i]*a[i][q]
                assert z%divisor==0
                a[j][q]=z//divisor
            a[j][i]=0
        divisor=pivot
    return sign*a[-1][-1]

ks=list(range(1,21))+[22,24,30,49,64,100,101]
examples={}
for k in ks:
    matrix=[[H(k,3+i-j) for j in range(9)] for i in range(9)]
    rawdet=det_bareiss(matrix)
    formula=ev(D[9],k)*C(k)**9
    assert formula.denominator==1 and rawdet==formula
    assert rawdet>0,(k,rawdet)
    if k in (1,3,4,6,8,9,49): examples[str(k)]=str(rawdet)
    if k==6:
        crosscheck=0
        for perm in permutations(range(9)):
            term=1
            for i,j in enumerate(perm): term*=matrix[i][j]
            inversions=sum(perm[i]>perm[j] for i in range(9) for j in range(i+1,9))
            crosscheck+=term if inversions%2==0 else -term
        assert crosscheck==rawdet
for k in (6,8,9):
    raw8=det_bareiss([[H(k,3+i-j) for j in range(8)] for i in range(8)])
    assert (raw8<0 if k<=8 else raw8>0)

print(json.dumps({
    'status':'R487_EXACT_PASS',
    'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
    'scope':'SIGNED_BRC_AUXILIARY_SCALAR_RIGHT_EDGE_s3_m9',
    'proof':'F9(k)=k^9(k+1)^9(k+2)(2k+1)^9(2k+3)^9 P9(k)/DEN9; P9(4+u) has 18 strictly positive coefficients; P9(1),P9(2),P9(3) positive',
    'P9_ascending':P9, 'DEN9':DEN9,
    'shift4_ascending':shift4,
    'shift4_min':str(min(shift4)),
    'P9_at_1_2_3':[str(v) for v in small],
    'polynomial_coefficients_checked':55,
    'shift_coefficients_checked':18,
    'raw_convolution_equalities_checked':rawchecks,
    'raw_integer_det9_checked':len(ks),
    'independent_permutation_det9_checked':1,
    'permutation_terms':factorial(9),
    'raw_integer_det8_comparison_checked':3,
    'raw_integer_det9_examples':examples,
    'rank9_r_asymptotic_constant':str(D[9][-1]/2**54),
    'arithmetic':'stdlib int/Fraction, no floating point',
    'admission':'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED'
}, ensure_ascii=False, sort_keys=True, indent=2))
