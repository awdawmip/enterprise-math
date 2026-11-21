"""Frozen R5 true-intersection primitive-19 universal theorem verifier.

Integer-only computation in Z[z]/(z^19-1), then quotient by Phi_19.
Run: python VERIFY_ALLM.py
This is author-side exact arithmetic, not independent proof review.
"""
import json

D = 7
C = 76
S = {
    0:(214,215,216,217,218),
    1:(214,216,217,218,219,220,221),
    2:(215,216,217,218,219,220,221)
}

def zero(): return (0,)*D
def scalar(k): return (k,)+(0,)*(D-1)
def mono(p): return tuple(int(i==p%D) for i in range(D))
def add(a,b,sign=1): return tuple(x+sign*y for x,y in zip(a,b))
def mul(a,b):
    out=[0]*D
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                if bj: out[(i+j)%D]+=ai*bj
    return tuple(out)
def factors(prices):
    r=scalar(1)
    for p in prices:
        r=mul(r,add(scalar(1),mono(p),-1))
    return r

def seq_h(prices,n):
    # h_k of the selected cyclic weights; coefficient of t^k.
    h=[scalar(int(i==0)) for i in range(n)]
    for p in prices:
        w=mono(p)
        for k in range(1,n):
            h[k]=add(h[k],mul(w,h[k-1]))
    return h

def geom(p,n): return [mono(k*p) for k in range(n)]
def smul(a,b):
    n=len(a); out=[zero() for _ in range(n)]
    for i,x in enumerate(a):
        if any(x):
            for j,y in enumerate(b[:n-i]):
                if any(y):out[i+j]=add(out[i+j],mul(x,y))
    return out
def prefix(a):
    out=[]; x=zero()
    for v in a:
        x=add(x,v);out.append(x)
    return out

def wmax(p,J):
    # Coefficients of sum z^(p*y)*h_j*t^max(y,j).
    n=len(J); g=geom(p,n); pj=prefix(J);pg=prefix(g)
    return [
        add(mul(g[k],pj[k]),mul(J[k],pg[k-1] if k else zero()))
        for k in range(n)
    ]
def wab(a,b,n):
    ga=geom(a,n);gb=geom(b,n);pa=prefix(ga);pb=prefix(gb)
    return [
        add(mul(ga[k],pb[k]),mul(gb[k],pa[k-1] if k else zero()))
        for k in range(n)
    ]
def triple(a,b,J):
    # min(x,y,j) separation, with NO collapsed constraint.
    # V012 = [(1-t) A(t)+t J(t)] / [(1-a*t)(1-b*t)]
    # A_n = sum_{0<=k<=n/2} (ab)^k h_(n-k).
    n=len(J); gab=geom(a+b,n);A=[]
    for i in range(n):
        v=zero()
        for k in range(i//2+1):
            v=add(v,mul(gab[k],J[i-k]))
        A.append(v)
    T=[add(A[i],add(J[i-1],A[i-1],-1) if i else zero())
       for i in range(n)]
    return smul(seq_h((a,b),n),T)

def numerator_rows(n=76,shared=None):
    U=seq_h((216,217,218),n)
    J=seq_h((219,220,221),n)
    A=geom(214,n);B=geom(215,n)
    V0=seq_h((214,215),n)
    V1=smul(A,J);V2=smul(B,J)
    V01=smul(A,wmax(215,J))
    V02=smul(B,wmax(214,J))
    V12=smul(J,wab(214,215,n))
    V012=triple(214,215,J)
    UB=factors(tuple(p for p in (216,217,218) if p!=shared))
    JB=factors((219,220,221))
    ba=add(scalar(1),mono(214),-1)
    bb=add(scalar(1),mono(215),-1)
    B0=mul(UB,mul(ba,bb))
    B1=mul(UB,mul(ba,JB))
    B2=mul(UB,mul(bb,JB))
    BU=mul(B0,JB)
    W=[]
    for k in range(n):
        w=zero()
        for factor,series,sgn in [
            (B0,V0,1),(B1,V1,1),(B2,V2,1),
            (BU,V01,-1),(BU,V02,-1),(BU,V12,-1),(BU,V012,1)
        ]:
            w=add(w,mul(factor,series[k]),sgn)
        W.append(w)
    # U(t)/(1-t) multiplication keeps full multiplicity and phase.
    return prefix(smul(U,W))


from fractions import Fraction
from math import lcm

PRICES=tuple(range(214,315))
SETS=(set(range(214,219)),{214,216,217,218,219,220,221},
      {215,216,217,218,219,220,221},set(range(223,291)),set(range(296,313)))

def cyclo(d,v):
    if d==7:return [v[i]-v[6] for i in range(6)]
    if d==9:return [v[i]-v[i+6] if i<3 else v[i]-v[i+3] for i in range(6)]
    raise ValueError(d)

def direct_true_intersections(d,m,shared):
    """Second algorithm: enumerate all seven genuine event conjunctions."""
    total=[0]*d
    for mask in range(1,8):
        I=[i for i in range(3) if mask&(1<<i)]
        U=sorted(set.union(*(SETS[i] for i in I)))
        assert shared in U
        fac=[1]+[0]*(d-1)
        for p in U:
            if p!=shared:fac=[fac[j]-fac[(j-p)%d] for j in range(d)]
        hist=[0]*d
        def go(j,loads,cost):
            if j==len(U):
                hist[cost%d]+=1
                return
            p=U[j]
            for a in range(m):
                nxt=tuple(loads[t]+a*int(p in SETS[i]) for t,i in enumerate(I))
                if max(nxt)>=m:break
                go(j+1,nxt,cost+p*a)
        go(0,(0,)*len(I),0)
        sign=1 if len(I)%2 else -1
        for r in range(d):
            total[r]+=sign*sum(fac[j]*hist[(r-j)%d] for j in range(d))
    return total

def max_pole_multiplicity(d):
    a,b=214%d,215%d
    u=[p%d for p in (216,217,218)]
    c=[p%d for p in (219,220,221)]
    prefix=u+[0]
    terms=[(prefix+[a,b],[]),(prefix+[a]+c,[]),
           (prefix+[b]+c,[]),(prefix+c+[a,b,(a+b)%d],[])]
    for x in c:
        terms.extend([(prefix+[a,b,x,(b+x)%d],[]),
                      (prefix+[a,b,x,(a+x)%d],[]),
                      (prefix+[a,b,x],[(a+b+x)%d])])
    # At t=exp(2*pi*i*k/(2d)), enumerate exact linear/quadratic zeros.
    return max(sum((k+2*r)%(2*d)==0 for r in linear)
               +sum((k+e)%d==0 for e in quadratic)
               for linear,quadratic in terms for k in range(2*d))

def normalized(p):
    p=list(map(Fraction,p))
    while p and p[-1]==0:p.pop()
    return p

def coprime(p,q):
    p,q=normalized(p),normalized(q)
    while q:
        r=p[:]
        while len(r)>=len(q):
            shift=len(r)-len(q)
            c=r[-1]/q[-1]
            for j,b in enumerate(q):r[shift+j]-=c*b
            r=normalized(r)
        p,q=q,r
    return len(p)==1 and p[0]!=0

def verify_79(d,shared):
    global D
    D=d
    L=2*d
    assert max_pole_multiplicity(d)<=3
    vectors=[cyclo(d,v) for v in numerator_rows(5*L,shared)]
    for m in range(1,6):
        assert vectors[m-1]==cyclo(d,direct_true_intersections(d,m,shared)),(d,m)
    for r in range(2*L):
        v=[vectors[r+i*L] for i in range(4)]
        assert all(v[3][j]-3*v[2][j]+3*v[1][j]-v[0][j]==0 for j in range(6))
    witnesses=[]
    for r in range(L):
        A,B,C=vectors[r],vectors[r+L],vectors[r+2*L]
        if any(A) and all(b==2*a and c==3*a for a,b,c in zip(A,B,C)):
            witnesses.append({'phase':r+1,'type':'positive_multiple',
                              'vector_A':A,'B_equals_2A':True,'C_equals_3A':True})
            continue
        # Q_i(k)=2*B_(r+1+2d*k)[i], quadratic by the rational recurrence.
        polys=[[2*a,4*b-3*a-c,c-2*b+a] for a,b,c in zip(A,B,C)]
        pairs=[(i,j) for i in range(6) for j in range(i+1,6)
               if coprime(polys[i],polys[j])]
        assert pairs,(d,r+1,'missing polynomial witness')
        i,j=pairs[0]
        witnesses.append({'phase':r+1,'type':'coprime_pair','coordinates':[i,j],
                          'integer_polynomials_2B':[polys[i],polys[j]]})
    assert sum(w['type']=='positive_multiple' for w in witnesses)==5
    return {'root_order':d,'shared_price':shared,'pole_multiplicity_bound':3,
            'phase_modulus':L,'direct_checks':[1,2,3,4,5],
            'extra_third_differences':2*L,'witnesses':witnesses}

def verify_5():
    global D
    D=5
    beta=[[4375,0,1100,1100],[-25,0,-2200,-2200],
          [4375,0,1100,1100],[1075,0,0,0],[1075,0,0,0]]
    def prefix_h(prices,n):
        h=seq_h(tuple(prices),n)
        return prefix(h)
    h0=prefix_h(sorted(SETS[0]),15)
    h1=prefix_h(sorted(SETS[1]),15)
    g0=factors(tuple(p for p in sorted(SETS[0]) if p!=215))
    g1=factors(tuple(p for p in sorted(SETS[1]) if p!=220))
    for m in range(1,16):
        c0=mul(g0,h0[m-1])
        c1=mul(g1,h1[m-1])
        v=[215*x+220*y for x,y in zip(c0,c1)]
        reduced=[v[i]-v[4] for i in range(4)]
        assert reduced==[v*(1+(m-1)//5) for v in beta[(m-1)%5]],m
    return {'root_order':5,'first_order_derivative_vectors_r1_to_5':beta,
            'general_term':'B_(5k+r)=(k+1)*beta_r','dp_check_m':'1..15'}

def main():
    candidate=[d for d in range(1,315) if 314//d-213//d>=5]
    assert candidate==list(range(1,21))+[22,24]
    L=lcm(*candidate)
    assert L==232792560
    r24=[sum(p%24==0 for p in S) for S in SETS]
    assert r24==[1,1,1,3,1]
    d5=verify_5()
    d7=verify_79(7,217)
    d9=verify_79(9,216)
    old=[11,13,16,17,19]
    assert lcm(*old,5,7,9)==L
    return {'schema':'R5_ALL_THRESHOLD_EXACT_PERIOD_O3_V1',
            'model':'frozen 101 integer prices, five original joint-load failures',
            'domain':'every integer m >= 1',
            'candidate_orders_k_ge_5':candidate,
            'upper_bound':L,'root24_divisible_price_counts_by_event':r24,
            'primitive_5':d5,'primitive_7':d7,'primitive_9':d9,
            'prior_author_derived_factors':old,'least_period':L,
            'evidence':'exact integer arithmetic; rational pole bounds; no independent review',
            'status':'AUTHOR_EXACT_VERIFIED_NOT_REVIEWED'}

if __name__=='__main__':
    result=main()
    with open('CERTIFICATE.json','w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print('PASS',result['least_period'],'all positive m; 5,7,9 exact phase proof')
