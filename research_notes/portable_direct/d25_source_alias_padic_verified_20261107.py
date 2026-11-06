"""D25 labelled port aliases and p-adic recovery; exact integer checker."""
from collections import defaultdict
from math import comb, isqrt

def prime(p):
    return p > 1 and all(p % d for d in range(2, isqrt(p) + 1))

def port(p, j, z, digits=1):
    m = (p-1)//6
    q = p**digits
    return ((6*j+1)*pow(-2, -j, q)*comb(3*m, j)
            *comb(2*m+z, j)*comb(4*m+z, j)) % q

def check(p):
    assert prime(p) and p % 6 == 1
    m = (p-1)//6
    L, R, j = 4*m+1, 2*m+1, 2*m+1
    assert L != R
    assert port(p,0,L)==port(p,0,R)==1
    assert all(port(p,k,L)==port(p,k,R)==0 for k in range(1,3*m+1))
    diff = (port(p,1,L,2)-port(p,1,R,2)) % (p*p)
    assert diff == (-42*m*m*p)%(p*p)
    left, right = port(p,j,L,3), port(p,j,R,3)
    assert left%(p*p)==0 and left%(p**3)!=0
    assert right%p==0 and right%(p*p)!=0
    a = (-(6*j+1)*pow(2,-j,p)*comb(3*m,j)*pow(j,-2,p))%p
    b = (-(6*j+1)*pow(2,-j,p)*comb(3*m,j)*comb(4*m+1,j)*pow(j,-1,p))%p
    assert left//(p*p)==a!=0 and right//p%p==b!=0
    if p >= 13:
        v1 = [port(p,1,z) for z in range(p)]
        w1 = [port(p,1,z,2) for z in range(p)]
        assert len(set(v1))==(p+1)//2 and len(set(w1))==p
        assert all(v1[z]==v1[(1-z)%p] for z in range(p))
        if p>=19:
            fibres=defaultdict(list)
            for z in range(p):
                fibres[(v1[z],port(p,2,z))].append(z)
            assert len(fibres)==p-1
            assert [sorted(v) for v in fibres.values() if len(v)==2]==[[R,L]]
    return (p,L,R,j,diff//p,left//(p*p),right//p%p)

if __name__ == '__main__':
    vals=[check(p) for p in range(7,1001) if p%6==1 and prime(p)]
    for row in vals:
        if row[0] in (7,13,19,31,109,211): print('EXACT',row)
    print('ALL_CHECKS_PASS',len(vals),'prime inputs through 1000')
