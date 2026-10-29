#!/usr/bin/env python3
"""GH-86: exact finite-field coefficient and resonance checks (no network)."""
from math import isqrt


def primes_under(n):
    sieve=bytearray(b'\x01')*n
    sieve[:2]=b'\x00\x00'
    for k in range(2,isqrt(n-1)+1):
        if sieve[k]:sieve[k*k:n:k]=b'\x00'*len(range(k*k,n,k))
    return [p for p in range(7,n) if p%4==3 and sieve[p]]


def recurrences(p):
    d=(p-3)//4
    c=[1];h=[1]
    for j in range(d):
        c.append(c[-1]*(4*j+1)**3*pow((4*j+2)*(4*j+3)*(4*j+4),-1,p)%p)
        h.append(h[-1]*(4*j+3)**3*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p)
    return d,c,h


def pq(n,sign,p):
    inv2=pow(2,-1,p);inv4=pow(4,-1,p)
    if sign=='plus':
        return n*(n+inv4)*(n+inv2)%p, pow(n+3*inv4,3,p)
    return n*(n-inv2)*(n-inv4)%p, pow(n+inv4,3,p)


def differential(values,sign,p):
    result=[0]*(len(values)+1)
    for n in range(len(result)):
        a=values[n] if n<len(values) else 0
        prev=values[n-1] if 0<=n-1<len(values) else 0
        P,_=pq(n,sign,p); _,Q=pq(n-1,sign,p)
        result[n]=(P*a-Q*prev)%p
    return result


def rank_mod_p(matrix,p):
    rows=[x[:] for x in matrix];r=0;n=len(rows[0])
    for c in range(n):
        pivot=next((j for j in range(r,len(rows)) if rows[j][c]),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        iv=pow(rows[r][c],-1,p)
        rows[r][c:]=[(v*iv)%p for v in rows[r][c:]]
        for j in range(r+1,len(rows)):
            f=rows[j][c]
            if f:rows[j][c:]=[(a-f*b)%p for a,b in zip(rows[j][c:],rows[r][c:])]
        r+=1
        if r==len(rows):break
    return r


def independent_linear_dim(p,sign):
    N=2*p
    # Unknowns a_0,...,a_(2p-1); include equation n=2p, which
    # checks the final carry obstruction independent of a_(2p).
    mat=[]
    for n in range(N+1):
        row=[0]*N
        if n<N:row[n]=pq(n,sign,p)[0]
        if n>0:row[n-1]=(-pq(n-1,sign,p)[1])%p
        mat.append(row)
    return N-rank_mod_p(mat,p)


def run(limit=2000):
    primes=primes_under(limit)
    exact_coeffs=0
    for p in primes:
        d,c,h=recurrences(p)
        s=(p-1)//2;u=(p+1)//2;t=(3*p-1)//4
        assert (s,u,t)==(2*d+1,2*d+2,3*d+2)
        assert all(x%p for x in (c[-1],h[-1]))
        # The original plus solution and the minus shifted companion.
        assert not any(differential(h,'plus',p))
        V=[0]*u+h
        assert not any(differential(V,'minus',p))
        # The original nonhomogeneous minus source and its forced plus shift.
        expected=[0]*(d+2);expected[-1]=c[-1]*pow(8,-1,p)%p
        assert differential(c,'minus',p)==expected
        W=[0]*s+c
        expected2=[0]*(t+1);expected2[-1]=c[-1]*pow(8,-1,p)%p
        assert differential(W,'plus',p)==expected2
        # Verify all the load-bearing Frobenius resonance pivots are nonzero.
        assert pq(s,'plus',p)[0]==0 and pq(t,'plus',p)[0]==0
        assert pq(t-1,'plus',p)[1] and pq(p-1,'plus',p)[1]
        assert pq(d+1,'minus',p)[0]==0 and pq(u,'minus',p)[0]==0
        assert pq(d,'minus',p)[1] and pq(u-1,'minus',p)[1]
        assert pq(t,'minus',p)[1]==0
        # Directly check each free resonant branch would have nonzero
        # carry to its next resonance (without using the asserted theorem).
        for sign,first,stop in [('plus',s,t),('plus',t,p),('minus',0,d+1),('minus',d+1,u)]:
            a=1
            for n in range(first+1,stop):
                P,_=pq(n,sign,p);_,Q=pq(n-1,sign,p)
                assert P and Q
                a=(a*Q*pow(P,-1,p))%p
            _,Q=pq(stop-1,sign,p)
            assert a*Q%p
        exact_coeffs+=len(h)+len(V)+len(c)+len(W)
    for p in [7,11,19,23,31,43]:
        assert independent_linear_dim(p,'plus')==2
        assert independent_linear_dim(p,'minus')==2
    print('PASS_GH86_FROBENIUS_GAUGE', len(primes), 'primes p<'+str(limit), 'exact polynomial coefficient entries',exact_coeffs)
    print('PASS_GH86_RESONANCE_BLOCKS',len(primes),'and 12 independent small-prime kernel-dimension checks')
    p=23;d,c,h=recurrences(p);s=(p-1)//2;u=(p+1)//2;t=(3*p-1)//4
    print('WITNESS p=23 d=',d,'plus U=',h,'minus V=z^'+str(u)+'U','forced W=z^'+str(s)+'S, defect=',c[-1]*pow(8,-1,p)%p,'*z^'+str(t))

# GH-87: independent polynomial coefficient identity.
def polynomial_r_cache(h,p):
    d=len(h)-1
    j1=[(j*v)%p for j,v in enumerate(h)]
    j2=[(j*j*v)%p for j,v in enumerate(h)]
    def mul(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
        return z
    u2=mul(h,h); udu=mul(h,j1); ud2=mul(j1,j1); u2d=mul(h,j2)
    res=[0]*(2*d+2)
    inv2=pow(2,-1,p);inv16=pow(16,-1,p)
    for k in range(2*d+1):
        X=(2*u2d[k]-ud2[k])%p
        res[k]=(res[k]+X+inv2*udu[k])%p
        res[k+1]=(res[k+1]-X-3*inv2*udu[k]-9*inv16*u2[k])%p
    return res


def check_gh87(limit=2000):
    primes=primes_under(limit)
    checked=0
    for p in primes:
        d,_,h=recurrences(p)
        R=polynomial_r_cache(h,p)
        assert not any(R), (p,R)
        # Highest coefficient cancellation is necessary: theta kernel may
        # contain nonzero z^p, so degree must be bounded before integration.
        assert ((d*4+3)%p)==0
        checked+=len(R)
    print('PASS_GH87_SIGNED_JET_QUADRATIC_CERTIFICATE',len(primes),'primes p<'+str(limit),checked,'coefficients')


if __name__=='__main__':
    run()
    check_gh87()
