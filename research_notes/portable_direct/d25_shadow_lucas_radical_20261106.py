"""Exact Lucas factorization for the signed integer shadow C_n; ordinary arithmetic only."""
from math import comb

def C_mod(n, m):
    s=0
    factor=pow(2,2*n,m)
    half=pow(2,-1,m) if m>1 else 0
    x=1
    for k in range(2*n+1):
        if k:
            x=x*(-half)%m
        t=(6*k+1)*x*comb(2*n,k)*comb(3*n,k)*comb(4*n,k)
        s=(s+t)%m
    return factor*s %m

def lucas_local(n,q):
    assert (6*n+1)%q==0 and q>=5
    N,n0=divmod(n,q)
    r=[]; M=[]
    for a in (2,3,4):
        c,rr=divmod(a*n0,q)
        r.append(rr); M.append(a*N+c)
    v=pow(2,-1,q)
    z=1
    low=0
    for j in range(q):
        if j: z=z*(-v)%q
        low=(low+(6*j+1)*z*comb(r[0],j)*comb(r[1],j)*comb(r[2],j))%q
    z=1; high=0
    for t in range(min(M)+1):
        if t: z=z*(-v)%q
        high=(high+z*comb(M[0],t)*comb(M[1],t)*comb(M[2],t))%q
    return {'q':q,'n0':n0,'N':N,'low':low,'high':high,
            'factored':pow(2,2*(n0+N),q)*low*high%q,
            'direct':C_mod(n,q), 'r':r,'M':M}

def main():
    checks=0
    for q,ns in [(5,[4,9,14,24]),(7,[1,8,15,22]),(11,[9,20,31]),
                 (13,[2,15,28,41]),(19,[3,22,41,60]),(23,[19,42]),(37,[6,43,80])]:
        for n in ns:
            assert (6*n+1)%q==0, (n,q)
            d=lucas_local(n,q)
            assert d['factored']==d['direct']==0,d
            checks+=1
    print('LUCAS_FACTOR_CHECKS',checks,'PASS')
    for m,ps in [(13*19,(13,19)),(13*37,(13,37)),(19*43,(19,43))]:
        assert m%6==1
        n=(m-1)//6
        d=C_mod(n,m)
        assert d==0,(m,n,d)
        print('COMPOSITE',m,'n',n,'C_n mod m',d,'prime_factors',ps)
    def distinct_prime_factors(v):
        ps=[];d=2
        while d*d<=v:
            if v%d==0:
                ps.append(d)
                while v%d==0:v//=d
            d+=1
        if v>1:ps.append(v)
        return ps
    for n in range(1,201):
        m=6*n+1
        assert C_mod(n,m)==0,(n,m)
        rad=1
        for q in distinct_prime_factors(m):rad*=q
        assert C_mod(n,rad)==0
    print('INTEGER_SHADOW',200,'PASS')
    for n in [4,8,28]:
        m=6*n+1
        print('REPEATED_PRIME',m,'n',n,'C_n mod m',C_mod(n,m))

if __name__=='__main__':
    main()
