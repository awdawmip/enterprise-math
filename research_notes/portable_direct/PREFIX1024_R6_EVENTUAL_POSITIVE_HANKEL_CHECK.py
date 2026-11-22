"""PREFIX-1024: exact X6 Laurent test of eventual positive-port Hankel positivity.

Input: P000 V5 frozen f42f2906..., candidate Stage46 signed kernel;
       PREFIX-1023 exact positive-port Laurent packet.
Only stdlib exact integer arithmetic. Writes adjacent JSON certificate.
"""
from collections import defaultdict
from math import factorial
from pathlib import Path
import json

D = 6
ZERO = (0,)*D
ONE={ZERO:1}

def mono(i,k=1):
    a=list(ZERO); a[i]=k
    return {tuple(a):1}

def plus(*terms):
    o=defaultdict(int)
    for p in terms:
        for v,c in p.items():o[v]+=c
    return {v:c for v,c in o.items() if c}

def mul(a,b):
    o=defaultdict(int)
    for v,c in a.items():
        for w,d in b.items():o[tuple(x+y for x,y in zip(v,w))]+=c*d
    return {v:c for v,c in o.items() if c}

def scale(a,c):return {v:c*x for v,x in a.items() if c*x}
S=plus(*(mono(i) for i in range(D)))
U=plus(*(mono(i,-1) for i in range(D)))
L=mul(S,U)
L36=plus(L,scale(ONE,-36))
S1=plus(S,scale(mono(0),-1))

def b_packet(m,j):
    E=plus(scale(ONE,72),scale(mul(S,plus(mono(0,-1),mono(j,-1))),-6))
    A=plus(scale(L36,m+3),E)
    return mul(mono(j),plus(mul(S1,A),mul(mono(0),L36),scale(mono(0),25)))

def compositions(total, k):
    if k == 1:
        yield (total,)
    else:
        for a in range(total+1):
            for rest in compositions(total-a,k-1):yield (a,)+rest

def spower(m):
    fac=[factorial(i) for i in range(m+1)];f=fac[m]
    return {a:f//(fac[a[0]]*fac[a[1]]*fac[a[2]]*fac[a[3]]*fac[a[4]]*fac[a[5]]) for a in compositions(m,D)}

def mass(n,j,powS):
    p=mul(powS,b_packet(n-4,j))
    return sum(c*c for c in p.values())

def determinant(mat):
    a=[list(row) for row in mat];n=len(a);den=1;sgn=1
    for k in range(n-1):
        if a[k][k]==0:
            swap=next((i for i in range(k+1,n) if a[i][k]),None)
            if swap is None:return 0
            a[k],a[swap]=a[swap],a[k];sgn=-sgn
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=a[i][j]*p-a[i][k]*a[k][j]
                assert x%den==0
                a[i][j]=x//den
            a[i][k]=0
        den=p
    return sgn*a[-1][-1]

previous={
    5:(135110,109490),6:(2918820,2532792),7:(66735540,59610948),
    8:(1607486710,1458235054),9:(40552191300,37154147448),
    10:(1064532083910,982562886810),11:(28900330619000,26836839882872)
}
# Compute through n=18, enough to audit 3x3 and 4x4 consecutive starts.
values={}
for n in range(5,19):
    s=spower(n-4)
    a,b=mass(n,0,s),mass(n,1,s)
    values[n]=(a,b)
    if n in previous:assert (a,b)==previous[n],(n,a,b)
    print(f'n={n}: Q1={a}, Qother={b}, S-support={len(s)}',flush=True)

hankel={}
for h in (2,3,4):
    for port in (0,1):
        series=[values[n][port] for n in range(5,19)]
        d={}
        for s in range(len(series)-2*h+2):
            d[str(s+5)]=str(determinant([[series[s+i+j] for j in range(h)] for i in range(h)]))
        hankel[f'port{port}_order{h}']=d

assert int(hankel['port1_order3']['5'])<0
assert int(hankel['port1_order3']['6'])<0
assert int(hankel['port1_order3']['7'])>0
assert int(hankel['port1_order3']['7'])==1467655835015118265181899984
assert int(hankel['port1_order4']['5'])<0
# Finite data only: no general positive claim based on tests.
cert={
    'id':'PREFIX-1024',
    'scientific_input':'P000 V5 frozen enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'packet':'PREFIX-1023 exact signed Laurent positive port packet; k=1; blocked Link {0,e1}',
    'numeric_scope':'exact integer n=5..18, ports j=1 and representative j=2',
    'prior_crosscheck':'exact match with PREFIX1023 n=5..11 on both representatives',
    'values':{str(n):{'axis1':str(a),'other_each':str(b)} for n,(a,b) in values.items()},
    'hankel_consecutive_start':hankel,
    'proven_analytic_claim':'for each fixed size h, Hankel determinant eventually strictly positive; proof in accompanying note via full Laplace expansion and finite differences',
    'not_proven':'uniform threshold in h, positive definiteness at all n0, nonlinear future-state sufficiency, theorem admission',
    'review':'AUTHOR_PROOF_NOT_INDEPENDENTLY_REVIEWED'
}
out=Path(__file__).with_name('PREFIX1024_R6_EXACT_INTEGER_RESULTS.json')
out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('CERTIFICATE',out,'size',out.stat().st_size,flush=True)
