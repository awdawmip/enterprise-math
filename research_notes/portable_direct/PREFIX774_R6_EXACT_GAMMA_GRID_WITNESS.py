"""PREFIX-774: exact rational mixed differences in one 1/768 Gamma-clock square.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Independent auxiliary model, not an original comparator grid exclusion.
Standard library only; final signs are verified with arbitrary-precision integers.
"""
from math import comb
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal,localcontext
import json
N=189;W=1<<18;BASE=768;HALF=1<<377
@lru_cache(None)
def inside(n,k,x):return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise AssertionError((n,k))
rows=[{0:1}]
for n in range(1,N+1):
    nr=defaultdict(int)
    for k,c in rows[-1].items():nr[k]+=c;nr[k+1]+=c
    rows.append({k:c for k,c in nr.items() if wide(n,k)})
assert not rows[-1]
assert sum(map(len,rows[:N]))==9529

def survivor(a):
    x=[1];y=[1];B=[1]
    for _ in range(N):x.append(x[-1]*a);y.append(y[-1]*(BASE-a));B.append(B[-1]*BASE)
    s=[]
    for n,row in enumerate(rows[:N]):
        t=sum(c*x[k]*y[n-k] for k,c in row.items())
        s.append(t*B[188-n])
    return s

K=[[comb(i+j,i)<<(376-i-j) for j in range(N)] for i in range(N)]

def bilinear(s,t,withL=False):
    v=0
    for i,si in enumerate(s):
        if not si: continue
        row=K[i];inner=0
        if withL:
            for j,tj in enumerate(t):
                if tj:inner+=row[j]*(i+j+1)*tj
        else:
            for j,tj in enumerate(t):
                if tj:inner+=row[j]*tj
        v+=si*inner
    return v

E=BASE**188;H=E*E*HALF
S38=survivor(38);S39=survivor(39)
def moment_numerators(s,t):
    ks=bilinear(s,t);ls=bilinear(s,t,True)
    mu=(sum(s)+sum(t))*E*HALF-ks
    m2=2*(sum((i+1)*x for i,x in enumerate(s))+sum((i+1)*x for i,x in enumerate(t)))*E*HALF-ls
    variance=m2*H-mu*mu
    assert mu>0 and variance>0
    return mu,variance
m00,w00=moment_numerators(S38,S38)
m01,w01=moment_numerators(S38,S39)
m11,w11=moment_numerators(S39,S39)
DMU=m11-2*m01+m00
DW=w11-2*w01+w00
assert DMU<0 and DW<0
TNUM=H*DMU;TDEN=DW
assert TNUM<0 and TDEN<0
assert 2852034258349*TDEN > (10**14)*TNUM
assert 2852034258350*TDEN < (10**14)*TNUM
assert 2*DW-H*DMU < 0
with localcontext() as ctx:
    ctx.prec=42
    result={
        'schema':'PREFIX774_R6_EXACT_1_768_GAMMA_GRID_MIXED_SIGN_V1',
        'frozen_scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'grid_square':{'p':['38/768','39/768'],'z':['38/768','39/768']},
        'model':'external independent first-stop Gamma maximum Y=max(C_p,C_z)',
        'survivor_nonzero_positions':9529,
        'terminal_survivor_empty':True,
        'mixed_mu_sign':'negative','mixed_variance_sign':'negative',
        'mixed_mu_decimal':str(Decimal(DMU)/Decimal(H)),
        'mixed_variance_decimal':str(Decimal(DW)/Decimal(H*H)),
        'grid_switch_ratio_decimal':str(Decimal(TNUM)/Decimal(TDEN)),
        'grid_switch_ratio_certified_rational_interval':['2852034258349/10^14','2852034258350/10^14'],
        'mixed_V2_sign':'negative',
        'mixed_V2_decimal':str(Decimal(4*DW-2*H*DMU)/Decimal(H*H)),
        'verification':'ALL_CHECKS_PASS PREFIX774',
        'original_1_768_comparator_exclusion_area_added':False,
        'status':'AUTHOR_EXACT_INTEGER_GRID_WITNESS / UNREVIEWED / NOT_ADMITTED'
    }
with open(__import__('pathlib').Path(__file__).with_name('PREFIX774_R6_EXACT_GAMMA_GRID_RESULTS.json'),'w') as f:
    json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
