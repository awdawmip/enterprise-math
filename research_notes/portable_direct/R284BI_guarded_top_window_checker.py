#!/usr/bin/env python3
"""R284BI: exact guarded leading-window Port readout verification."""
from fractions import Fraction as F
from itertools import product
from math import factorial
import random, json

def det(M):
    a = [list(map(int, row)) for row in M]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1,n) if a[j][k]), None)
            if j is None: return 0
            a[k],a[j] = a[j],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v = a[i][j]*pivot-a[i][k]*a[k][j]
                assert v % prev == 0
                a[i][j] = v // prev
        for i in range(k+1,n): a[i][k] = 0
        prev = pivot
    return sign*a[n-1][n-1]

def prime(n):
    def isprime(x):
        return x>=2 and all(x%k for k in range(2,int(x**.5)+1))
    x=max(3,n)
    while not (x%2 and isprime(x)): x+=1
    return x

def rnd_ratio(x,den):
    return (2*x+den)//(2*den)

def centered_at(x,b,k):
    m=rnd_ratio(x,pow(b,k))
    h=(b-1)//2
    return (m+h)%b-h

def experiment(c,H,delta=7000):
    n=len(c)
    p=prime(n)
    a=[2*p*j+(j*j%p) for j in range(n)]
    A=max(a)
    Q=4*A+2
    R=A+1
    e=[Q+v for v in a]
    t=[0]+[R+2*a[i] for i in range(1,n)]
    S=sum(e)
    T=3*Q-R+A
    K=S-T
    L=n*factorial(n)*pow(1+H,n)
    b=4*L+8*delta+9
    assert b%2==1 and K>=1
    d=[pow(b,v) for v in e]
    z=[0]+[pow(b,t[i]) for i in range(1,n)]
    mat=[[(d[i] if i==j else 0)-c[i][j]-(z[j] if i==0 and j else 0) for j in range(n)] for i in range(n)]
    y=det(mat)
    q=rnd_ratio(y-pow(b,S),pow(b,K))
    assert q==rnd_ratio(y+delta-pow(b,S),pow(b,K))
    assert q==rnd_ratio(y-delta-pow(b,S),pow(b,K))
    target={}
    for i in range(n):
        h=Q+a[i]
        target[h]=-c[i][i]
    for i in range(n):
        for j in range(i+1,n):
            h=2*Q+a[i]+a[j]
            target[h]=c[i][i]*c[j][j]-c[i][j]*c[j][i]
    for i in range(1,n):
        h=2*Q-R-a[i]
        target[h]=-c[i][0]
        for j in range(1,n):
            if j==i:continue
            h=3*Q-R-a[i]+a[j]
            target[h]=c[i][0]*c[j][j]-c[i][j]*c[j][0]
    assert len(target)==n+n*(n-1)//2+(n-1)+(n-1)*(n-2)
    assert all(Q<=h<=T for h in target)
    for h,expect in target.items():
        actual=centered_at(q,b,T-h)
        assert actual==expect,(n,h,expect,actual)
    assert abs(q).bit_length()<abs(y).bit_length()
    return {'n':n,'H':H,'A':A,'S':S,'T':T,'K':K,'Q':Q,'b_bits':b.bit_length(),
            'raw_bits':abs(y).bit_length(),'window_bits':abs(q).bit_length(),'targets':len(target)}

rng=random.Random(28420261121)
results=[]
binary3=list(product((1,2),repeat=9))
for n,amount in [(3,512),(4,40),(5,20),(6,8)]:
    for ix in range(amount):
        if n==3:
            bits=binary3[ix]
            c=[list(bits[i*3:i*3+3]) for i in range(3)]
        else:
            c=[[rng.randint(1,2) for _ in range(n)] for _ in range(n)]
        results.append(experiment(c,2))
summary={'schema':'R284BI_BG_GUARDED_TOP_WINDOW_V1','seed':28420261121,
         'status':'PASS','checks':len(results),'by_dimension':[],
         'scope':'Exact integer determinant and balanced-digit recovery; changed source-side quotient readout interface.'}
for n in (3,4,5,6):
    rows=[r for r in results if r['n']==n]
    summary['by_dimension'].append({
        'n':n,'checked':len(rows),'S':rows[0]['S'],'T':rows[0]['T'],
        'K':rows[0]['K'],'Q':rows[0]['Q'],
        'number_of_target_coefficients':rows[0]['targets'],
        'raw_bits_min':min(r['raw_bits'] for r in rows),
        'raw_bits_max':max(r['raw_bits'] for r in rows),
        'window_bits_min':min(r['window_bits'] for r in rows),
        'window_bits_max':max(r['window_bits'] for r in rows)})
with open('R284BI_guarded_top_window_verification.json','w') as f:
    json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
