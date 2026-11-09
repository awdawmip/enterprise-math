"""Exact finite-field audit of the Legendre-second-kind Wronskian
and the CM(-24) p-adic unit-derivative candidate. No floating point.
This auxiliary experiment is author-side / unreviewed, not a native H0/B0 run.
"""
from math import comb

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1);sieve[:2]=b'\x00\x00'
    for k in range(2,int(n**.5)+1):
        if sieve[k]:sieve[k*k:n+1:k]=b'\x00'*(((n-k*k)//k)+1)
    return [p for p in range(n+1) if sieve[p]]

def add(x,y,m):return ((x[0]+y[0])%m,(x[1]+y[1])%m)
def mul(x,y,m):return ((x[0]*y[0]+2*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def inverse(x,p):
    d=(x[0]**2-2*x[1]**2)%p
    if d==0:raise ZeroDivisionError
    v=pow(d,-1,p)
    return (x[0]*v%p, -x[1]*v%p)
def eval_poly(c,x,m):
    res=(0,0)
    for a in c[::-1]:res=add(mul(res,x,m),(a,0),m)
    return res

def cm_test(p, full_poly=False):
    assert p%24==13
    q=(p-1)//4
    C=[(-1)**k*comb(q,k)*comb(q+k,k)%p for k in range(q+1)]
    U=[sum(C[k]*pow(k-r,-1,p) for k in range(r+1,q+1))%p for r in range(q)]
    # Legendre-second-kind polynomial exact Wronskian over F_p
    if full_poly:
        def convolution(a,b):
            z=[0]*(len(a)+len(b)-1)
            for i,c in enumerate(a):
                for j,d in enumerate(b):z[i+j]=(z[i+j]+c*d)%p
            return z
        W1=convolution(C,[(k*U[k])%p for k in range(1,q)]) if q>1 else [0]
        W2=convolution([(k*C[k])%p for k in range(1,q+1)],U)
        W=[(a-b)%p for a,b in __import__('itertools').zip_longest(W1,W2,fillvalue=0)]
        lhs=convolution([0,1,-1],W)
        rhs=convolution(C,C)
        rhs[0]=(rhs[0]-1)%p
        assert not any((a-b)%p for a,b in __import__('itertools').zip_longest(lhs,rhs,fillvalue=0))
    s=(pow(2,-1,p),-pow(3,-1,p))
    ps=eval_poly(C,s,p)
    assert ps==(0,0), (p,'CM root',ps)
    deriv=eval_poly([k*C[k]%p for k in range(1,len(C))],s,p)
    assert deriv[0] and deriv[1]==0
    # Independent logarithmic convolution, no U-tail formula used here.
    A=[0]*p
    invs=[0]+[pow(i,-1,p) for i in range(1,p)]
    for k,c in enumerate(C):
        if c:
            for j in range(1,p-k):A[k+j]=(A[k+j]+c*invs[j])%p
    aval=eval_poly(A,s,p)
    wr_val=inverse(mul(s,deriv,p),p)
    assert aval==wr_val,(p,aval,wr_val)
    assert (2*aval[0])%p==36*pow(deriv[0],-1,p)%p
    assert aval[1]*3%p==(2*aval[0])%p
    # Independent p^2 Gauss hypergeometric recurrence at s, using no P/U.
    m=p*p
    s2=(pow(2,-1,m),-pow(3,-1,m))
    val=(0,0);term=(1,0)
    for k in range(p):
        val=add(val,term,m)
        if k<p-1:
            c=((4*k+1)*(4*k+3)*pow(16*(k+1)**2,-1,m))%m
            term=mul(term,mul((c,0),s2,m),m)
    assert val[0]==0 and val[1]%p==0,(p,'Gauss odd p-adic',val)
    g=(val[1]//p)%p
    predict=(3*pow(2*deriv[0],-1,p))%p
    assert g==predict,(p,g,predict)
    return p,q,(2*aval[0])%p,aval[1],deriv[0],g

if __name__=='__main__':
    sample=[p for p in primes_upto(1000) if p%24==13]
    rows=[cm_test(p, full_poly=True) for p in sample]
    print('verified target primes:',len(rows))
    for row in rows:
        if row[0] in (13,37,61,109,373,613,997):print(row)
    print('Wronskian identity, p-adic Gauss and CM derivative candidate: all checks PASS')

def cm_derivative_fast(p):
    """Extra finite-window check of only the open CM unit-derivative criterion.
    Unlike cm_test, no finite-log convolution or U polynomial is formed.
    """
    q=(p-1)//4
    s=(pow(2,-1,p),-pow(3,-1,p))
    term=(1,0); P=(1,0); DP=(0,0); c=1
    for k in range(1,q+1):
        c=c*(-(q-k+1)*(q+k)*pow(k*k,-1,p))%p
        DP=add(DP,mul((k*c%p,0),term,p),p)  # currently term = s^(k-1)
        term=mul(term,s,p)
        P=add(P,mul((c,0),term,p),p)
    assert P==(0,0) and DP[1]==0 and DP[0]
    mod=p*p
    s2=(pow(2,-1,mod),-pow(3,-1,mod))
    total=(0,0);c=(1,0)
    for k in range(p):
        total=add(total,c,mod)
        if k<p-1:
            v=((4*k+1)*(4*k+3)*pow(16*(k+1)**2,-1,mod))%mod
            c=mul(c,mul((v,0),s2,mod),mod)
    assert total[0]==0 and total[1]%p==0
    g=total[1]//p
    expected=3*pow(2*DP[0],-1,p)%p
    assert g==expected,(p,g,expected)
    return g

if __name__=='__main__':
    longer=[p for p in primes_upto(10000) if p%24==13]
    for p in longer:cm_derivative_fast(p)
    print('independent CM unit-derivative test p<=10000:',len(longer),'PASS')
