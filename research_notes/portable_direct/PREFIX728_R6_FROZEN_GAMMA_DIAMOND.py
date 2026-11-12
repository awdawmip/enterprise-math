"""PREFIX-728-R6: enlarged exact frozen-Gamma L1 diamond certificate by renewed local Bernstein bounds.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Inherits only the exact center witness gap from PREFIX726_R6_GAMMA_WITNESS_LIPSCHITZ.py.
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
radius=F(1,975)
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
assert ET_b<F(357,5)
assert T1==549269886 and F(T1,precision)<550
assert T2==81257510320 and F(T2,precision)<81260
L=F(81260)+(2*F(714,5)+F(1,2))*550
assert L==238615
margin=245-L*radius
assert margin==F(4,15)>0
assert nonbinary_controls==8904
assert center==F(44,384) and radius<2*F(1,384)
old_area=4*F(1,2000)**2
diamond_area=2*radius**2
area_ratio=diamond_area/old_area
assert area_ratio==F(3200,1521)>2 and 2*F(1,2000)<radius

result={
 'schema':'PREFIX728_R6_FROZEN_GAMMA_L1_DIAMOND_CERTIFICATE_V1',
 'scientific_source':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'predecessors':['PREFIX726_R6','PREFIX727_R6'],
 'center':'11/96','witness':['0','73/500'],
 'domain':'all real q >= 2; (p,z) in [0,1/2]^2',
 'region':'abs(p-11/96)+abs(z-11/96) <= 1/975',
 'n_frozen_survivor_cells':9529,
 'nonbinary_controls':nonbinary_controls,
 'local_interval':[str(a),str(b)],
 'rounded_up_denominator':precision,'T1':T1,'T2':T2,
 'ET_b_lt':'357/5','U1_lt':'550','U2_lt':'81260',
 'mu_lt':'714/5','coordinate_gradient_lt':'238615',
 'inherited_center_gap_gt':'245 for t=0 and t=1/2 (PREFIX726 exact)',
 'uniform_Vq_gap_gt':str(margin)+' * q^2',
 'diamond_area':str(diamond_area),
 'area_ratio_over_PREFIX727_square':str(area_ratio),
 'grid_full_cell_increment':'0; new diamond lies within the four adjacent fine cells',
 'status':'AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED'
}
if __name__=='__main__':
    Path(__file__).with_name('PREFIX728_R6_RESULTS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('ALL_CHECKS_PASS PREFIX728-R6')
    print('nonbinary controls:',nonbinary_controls)
    print('ET_b <72',ET_b<357/5,'rounded upper sums:',T1,'/',precision,T2,'/',precision)
    print('L <',L,'and V_q gap >', margin, '*q^2')
