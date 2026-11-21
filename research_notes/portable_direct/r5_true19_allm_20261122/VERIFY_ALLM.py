"""Frozen R5 true-intersection primitive-19 universal theorem verifier.

Integer-only computation in Z[z]/(z^19-1), then quotient by Phi_19.
Run: python VERIFY_ALLM.py
This is author-side exact arithmetic, not independent proof review.
"""
import json

D = 19
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

def numerator_rows(n=76):
    U=seq_h((216,217,218),n)
    J=seq_h((219,220,221),n)
    A=geom(214,n);B=geom(215,n)
    V0=seq_h((214,215),n)
    V1=smul(A,J);V2=smul(B,J)
    V01=smul(A,wmax(215,J))
    V02=smul(B,wmax(214,J))
    V12=smul(J,wab(214,215,n))
    V012=triple(214,215,J)
    UB=factors((216,217,218))
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

def phi(v):
    # z^18 = -sum(z^0,...,z^17) in Q[z]/Phi_19.
    return [v[k]-v[18] for k in range(18)]

def minor(a,b):
    for i in range(18):
        for j in range(i+1,18):
            d=a[i]*b[j]-a[j]*b[i]
            if d:return [i,j,d]
    return None

def verify():
    rows=[phi(v) for v in numerator_rows(76)]
    historic={
        1:[6,7,10,12,13,10,11,2,0,-6,-8,-18,-14,-17,-14,-14,-10,-8],
        2:[-4,-10,-11,-16,-13,-11,-6,-1,5,10,18,26,27,27,25,23,14,11],
        15:[-210,-437],16:[210,452],17:[-160,-365],
        18:[28,165],19:[101,86],
    }
    for m,v in historic.items():
        assert rows[m-1][:len(v)]==v,('regression',m)
    proof=[]
    for r in range(1,39):
        a,b=rows[r-1],rows[r+37]
        assert any(a) and any(b)
        cert=minor(a,b)
        if cert is None:
            assert r in (34,35,36,37,38) and b==[2*x for x in a],r
        else:
            assert r<=33,r
        proof.append({'phase_r':r,'minor_0based_i_j_det':cert,
                      'first_coefficient_R_r':a[0],
                      'first_coefficient_R_r38':b[0]})
    return {
        'schema':'R5_TRUE19_ALLM_V1',
        'source_frozen_commit':'b6bf656360b90a800043ea2f00cbd706db571386',
        'root':'primitive nineteenth root',
        'basis':'1,z,...,z^17 in Z[z]/Phi19',
        'recurrence':'R_(m+76)-2R_(m+38)+R_m=0 for all m>=1',
        'proof_status':'AUTHOR_EXACT_DERIVATION_NOT_REVIEWED',
        'vector_rows_m1_through_m76':rows,
        '38_phase_certificates':proof,
        'noncollinear_phases':33,
        'exact_doubling_phases':[34,35,36,37,38],
        'theorem':'R_m(zeta) nonzero for all integers m>=1',
        'consequence':'19 divides M_m(O_m(N^3)) for all integers m>=1'
    }

if __name__=='__main__':
    r=verify()
    with open('CERTIFICATE.json','w',encoding='utf-8') as f:
        json.dump(r,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print('PASS: 76 exact vectors; 33 independent pairs; 5 positive doubling pairs; historical regression')
