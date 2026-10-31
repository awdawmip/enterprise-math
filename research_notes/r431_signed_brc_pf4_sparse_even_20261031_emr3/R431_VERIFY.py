#!/usr/bin/env python3
"""R431 original signed BRC PF4 exact verifier, Python standard library only."""
import json
from fractions import Fraction as Q
from itertools import permutations,product
from math import comb
from pathlib import Path

def choose(n,m): return comb(n,m) if 0<=m<=n else 0

def raw_h(r,s):
    if not 2<=s<=r: return 0
    h=r-s
    return choose(r+s,2*s)*sum(choose(h,i)*(choose(2*s,r-2*i)-choose(2*s,r-2*i-1)) for i in range(h+1))

def cat(n): return choose(2*n,n)//(n+1)

def via_cat(r,s):
    if not 2<=s<=r:return 0
    if r%2==0:
        k=r//2
        z=sum(choose(s-1,2*t+1)*2**(2*t+1)*cat(k-1-t) for t in range((s-2)//2+1) if k-1-t>=0)
    else:
        k=(r-1)//2
        z=sum(choose(s-1,2*t)*2**(2*t)*cat(k-t) for t in range((s-1)//2+1) if k-t>=0)
    return choose(r+s,2*s)*z

def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return a
def add(a,b):
    o=[Q(0)]*max(len(a),len(b))
    for j,t in enumerate(a):o[j]+=t
    for j,t in enumerate(b):o[j]+=t
    return trim(o)
def mul(a,b):
    o=[Q(0)]*(len(a)+len(b)-1)
    for i,t in enumerate(a):
        for j,u in enumerate(b):o[i+j]+=t*u
    return trim(o)
def scaled(a,t):return trim([x*Q(t) for x in a])
def linear(a,b):return [Q(b),Q(a)]
def factored(scale,linear_factors=(),other_factors=()):
    o=[Q(scale)]
    for a,b in linear_factors:o=mul(o,linear(a,b))
    for f in other_factors:o=mul(o,[Q(t) for t in f])
    return o
def peval(poly,k):return sum(t*k**i for i,t in enumerate(poly))
def polydet(mat):
    o=[Q(0)]
    for perm in permutations(range(len(mat))):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        z=[Q(sign)]
        for i,j in enumerate(perm):z=mul(z,mat[i][j])
        o=add(o,z)
    return o

def signed_b_polys():
    return [
        [Q(1)],
        factored(Q(2,15),[(1,-1),(2,3)]),
        factored(Q(1,420),[(1,-1),(1,2),(2,3)],[[-9,8]]),
        factored(Q(1,4725),[(1,-2),(1,-1),(1,2),(2,3),(2,5)],[[-3,4]]),
        factored(Q(1,1247400),[(1,-2),(1,-1),(1,2),(1,3),(2,3),(2,5)],[[75,-184,64]]),
        factored(Q(1,56756700),[(1,-3),(1,-2),(1,-1),(1,2),(1,3),(2,3),(2,5),(2,7)],[[45,-160,64]]),
        factored(Q(1,13621608000),[(1,-3),(1,-2),(1,-1),(1,2),(1,3),(1,4),(2,3),(2,5),(2,7)],[[-735,4048,-2880,512]])
    ]

def bareiss(mat):
    a=[row[:] for row in mat];n=len(a)
    if n==1:return a[0][0]
    last=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            t=next((i for i in range(k+1,n) if a[i][k]),None)
            if t is None:return 0
            a[t],a[k]=a[k],a[t];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%last==0
                a[i][j]=num//last
            a[i][k]=0
        last=pivot
    return sign*a[-1][-1]

def verify_even_symbolic():
    b=signed_b_polys();z=[Q(0)]
    mat=[[b[3],b[0],z,z],[b[4],b[1],b[0],z],[b[5],b[2],b[1],b[0]],[b[6],b[3],b[2],b[1]]]
    f=list(map(Q,[234792,8610327,8706006,9249085,809990,836128,-3495552,564224]))
    target=factored(Q(1,1021620600000),[(1,-2),(1,-1),(1,2),(2,3),(2,5)],[f])
    assert polydet(mat)==target
    sh=[sum(f[i]*choose(i,j)*6**(i-j) for i in range(j,len(f))) for j in range(len(f))]
    assert sh==list(map(Q,[4772729250,28412494875,26338175280,10822110925,2403829190,301549600,20201856,564224]))
    assert all(x>0 for x in sh)
    assert all(peval(f,k)<0 for k in (3,4,5))
    count=0
    for k in range(4,31):
        r=2*k;h0=raw_h(r,2)
        for s in range(2,9):
            assert raw_h(r,s)==via_cat(r,s)
            assert Q(raw_h(r,s),h0)==peval(b[s-2],k)
            count+=1
    # Additional signed-to-Catalan checks over odd and even rows.
    for rr in range(5,32):
        for s in range(2,min(rr,8)+1):
            assert raw_h(rr,s)==via_cat(rr,s)
            count+=1
    assert count==372
    edge={}
    for k in range(3,12):
        r=2*k;n=r-2
        a=[raw_h(r,r-h) for h in range(n+1)]
        cols=(n-3,n,n+1,n+2)
        d=bareiss([[a[j-i] if 0<=j-i<=n else 0 for j in cols] for i in range(4)])
        predicted=peval(target,k)*a[n]**4
        assert predicted.denominator==1 and predicted.numerator==d
        edge[str(r)]=str(d)
    return {'identity':'EXACT_Q_POLYNOMIAL_COEFFICIENT_EQUALITY','raw_and_poly_crosschecks':count,'edge_determinants':edge,'F_shift6_ascending':[str(i) for i in sh]}

def verify_consecutive():
    R=linear(1,0);one=[Q(1)]
    def frac(num,den):return num,den
    def times(a,b):return mul(a[0],b[0]),mul(a[1],b[1])
    def plus(a,b):return add(mul(a[0],b[1]),mul(a[1],b[0])),mul(a[1],b[1])
    def scale(a,t):return scaled(a[0],t),a[1]
    c1=frac(linear(1,-2),R)
    c2=frac(mul(linear(1,-1),[Q(9),Q(-5),Q(1)]),mul(mul(R,R),linear(2,-1)))
    c3=frac(mul(mul(linear(1,-4),linear(1,-2)),[Q(15),Q(-5),Q(1)]),mul(scaled(mul(mul(R,R),R),3),linear(2,-1)))
    c4=frac(mul(mul(linear(1,-3),linear(1,-2)),[Q(525),Q(-316),Q(89),Q(-14),Q(1)]),mul(mul(scaled(mul(mul(R,R),mul(R,R)),6),linear(2,-3)),linear(2,-1)))
    J=plus(plus(plus(times(times(c1,c1),times(c1,c1)),scale(times(times(c1,c1),c2),-3)),times(c2,c2)),plus(scale(times(c1,c3),2),scale(c4,-1)))
    q=list(map(Q,[468,-1305,-41,465,29,-59,-3,2]))
    den=mul(mul(scaled(mul(mul(R,R),mul(R,R)),6),linear(2,-3)),mul(linear(2,-1),linear(2,-1)))
    assert mul(J[0],den)==mul(J[1],q)
    sh=[sum(q[i]*choose(i,j)*6**(i-j) for i in range(j,len(q))) for j in range(len(q))]
    assert sh==list(map(Q,[90306,204375,155425,57681,11759,1345,81,2]))
    assert all(x>0 for x in sh)
    for r in range(4,151):
        c=[Q(raw_h(r,r-h),cat(r)*r**h) for h in range(5)]
        j=c[1]**4-3*c[1]**2*c[2]+c[2]**2+2*c[1]*c[3]-c[4]
        if r>=6:
            assert j==Q(peval(q,r),peval(den,r)) and j>0
        elif r==4:assert j==Q(-251,12544)
        else:assert j==Q(-1,625)
    return {'identity':'CLEARED_DENOMINATOR_Q_POLYNOMIAL','original_signed_checks':'r=4..150','Q_shift6_ascending':[str(i) for i in sh]}

def finite_exact(r,order):
    n=r-2
    a=[raw_h(r,r-h) for h in range(n+1)]
    assert all(x>0 for x in a)
    def av(h):return a[h] if 0<=h<=n else 0
    checked=negative=zero=0;negative_examples=[]
    for gaps in product(range(1,n+1),repeat=order-1):
        rows=(0,)+tuple(sum(gaps[:t]) for t in range(1,order))
        def walk(t,cols):
            nonlocal checked,negative,zero
            if t==order:
                d=bareiss([[av(j-i) for j in cols] for i in rows])
                checked+=1
                if d<0:
                    negative+=1
                    if len(negative_examples)<5:negative_examples.append({'rows':rows,'cols':cols,'value':str(d)})
                elif d==0:zero+=1
                return
            lo=max(rows[t],cols[-1]+1 if cols else 0)
            for j in range(lo,rows[t]+n+1): walk(t+1,cols+(j,))
        walk(0,())
    assert zero==0
    return {'r':r,'order':order,'checked':checked,'negative':negative,'zero':zero,'negative_examples':negative_examples}

def run():
    cert=verify_even_symbolic()
    cert['consecutive']=verify_consecutive()
    tests=[finite_exact(r,k) for r in range(5,12) for k in (2,3,4)]
    assert sum(x['checked'] for x in tests)==6494878
    assert sum(x['negative'] for x in tests)==16
    assert all(x['negative']==0 for x in tests if x['order']<=3 or x['r'] in (7,9,11))
    assert all(x['negative']>0 for x in tests if x['order']==4 and x['r'] in (5,6,8,10))
    evidence={'status':'R431_EXACT_PASS','scope':'signed BRC auxiliary, symbolic all even r>=6; exhaustive complete PF4 r=7,9,11','certificate':cert,'enumeration':tests}
    output=Path(__file__).with_name('R431_EVIDENCE.json')
    output.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('R431_EXACT_PASS',sum(x['checked'] for x in tests),'minors',
          sum(x['negative'] for x in tests),'negative')

if __name__=='__main__':run()
