"""PREFIX-727-R6: exact Bernstein variation certificate on the frozen 189-row BRC-Gamma auxiliary observer.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Extends the exact witness gap already reproduced by PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py.
Run with Python 3 standard library; outputs a JSON certificate next to this file.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

N=189
WD=1 << 18
@lru_cache(None)
def inside(m,k,x):
    return 40*(m+1)*comb(m,k)*x**k*(WD-x)**(m-k)>WD**m
@lru_cache(None)
def wide(m,k):
    if k>m//2:
        return wide(m,m-k)
    mid=k*WD//m
    assert inside(m,k,mid)
    if k==0:
        lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(m,k,x):b=x
            else:a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(m,k,x):a=x
        else:b=x
    if 4*(a-hi)>WD:return True
    if 4*(b-lo)<WD:return False
    raise ValueError('Unresolved width under frozen integer predicate')

rows=[{0:1}]
for n in range(1,N+1):
    counts=defaultdict(int)
    for k,val in rows[-1].items():
        counts[k]+=val
        counts[k+1]+=val
    rows.append({k:val for k,val in counts.items() if wide(n,k)})
assert not rows[N]
assert sum(map(len,rows[:N]))==9529

center=F(11,96)
radius=F(1,2000)
a=center-radius
b=center+radius
assert F(0)<a<b<F(1,2)
precision=10**6
T1=T2=0
monotone_rows=0
nonbinary_controls=0
for n,row in enumerate(rows[:N]):
    assert all(0 <= v <= comb(n,k) for k,v in row.items())
    assert all(row.get(k,0)==row.get(n-k,0) for k in range(n+1))
    for k in range(n//2):
        assert row.get(k+1,0)*comb(n,k) >= row.get(k,0)*comb(n,k+1)
    monotone_rows+=1
    nonbinary_controls+=sum(0<v<comb(n,k) for k,v in row.items())
    if n<2:
        continue
    for k in range(n):
        left=row.get(k,0)
        right=row.get(k+1,0)
        if left==right==0:continue
        delta=F(right,comb(n,k+1))-F(left,comb(n,k))
        if not delta:continue
        x=min(b,max(a,F(k,n-1)))
        B=comb(n-1,k)*x**k*(1-x)**(n-1-k)
        term=n*abs(delta)*B
        rounding=(term.numerator*precision+term.denominator-1)//term.denominator
        T1+=rounding
        T2+=2*(n+1)*rounding

# Symmetric, unimodal normalized controls imply s_n(p) nondecreasing on [0,1/2].
ET_b=sum(sum(v*b**k*(1-b)**(n-k) for k,v in row.items()) for n,row in enumerate(rows[:N]))
assert ET_b<72
assert F(T1,precision)<544
assert F(T2,precision)<80400
L=F(80400)+(2*F(144)+F(1,2))*544
assert L==237344
margin=245-2*L*radius
assert margin==F(957,125)>0
assert nonbinary_controls>0

result={
    'schema':'PREFIX727_R6_LOCAL_BERNSTEIN_CERTIFICATE_V1',
    'scientific_source':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'predecessor':'PREFIX726_R6',
    'center':'11/96',
    'square_radius':'1/2000',
    'comparator':'(0,73/500)',
    'q_domain':'all real q >= 2',
    'nonzero_frozen_survivor_cells':9529,
    'normalized_Bernstein_control_type':'counts / binomial coefficient; rational in [0,1], not binary',
    'exact_symmetric_unimodal_control_rows':monotone_rows,
    'nonbinary_control_entries':nonbinary_controls,
    'ET_b_strict_upper':72,
    'rounded_upper_U1_numerator':T1,
    'rounded_upper_U2_numerator':T2,
    'rounded_bound_denominator':precision,
    'strict_U1_upper':544,
    'strict_U2_upper':80400,
    'mu_strict_upper':144,
    'L_strict_upper':str(L),
    'inherited_center_comparator_gap_strict_lower':'245 (PREFIX726 exact endpoints)',
    'V_q_gap_strict_lower':'(957/125)*q^2',
    'grid_coverage':'inherited 139018/147456; no extra full cells claimed',
    'validation':'local exact integer / Fraction checker; no independent review',
    'formal_admission':'NOT_ADMITTED',
}
if __name__=='__main__':
    Path(__file__).with_name('PREFIX727_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX727-R6')
    print('nonbinary controls:',nonbinary_controls)
    print('ET_b <72',ET_b<72,'upper sums:',T1,'/',precision,T2,'/',precision)
    print('L <',L,'and V_q gap >', margin, '*q^2')
