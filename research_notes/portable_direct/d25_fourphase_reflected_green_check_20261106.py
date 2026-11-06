"""Full D25 p-adic four-phase Green reciprocity test, Python stdlib only."""
from math import comb,isqrt

def gamma(k): return comb(2*k,k)**2*comb(3*k,k)

def remove_p(x,p):
    v=0
    while x%p==0: x//=p;v+=1
    return v,x%p

def check(p):
    m=(p-1)//6;P=p**5
    b=[1]*p
    for n in range(1,p):
        b[n]=b[n-1]*6*(6*n-5)*(3*n-2)*pow(n*n,-1,P)%P
    h=[None]*p
    h[1]=(0,pow(24,-1,p))
    for r in range(1,p-1):
        an=remove_p(r*r*(6*r+1),p)
        de=remove_p((r+1)*(2*r+1)*(3*r+2),p)
        h[r+1]=(h[r][0]+an[0]-de[0],h[r][1]*an[1]*pow(de[1],-1,p)%p)
    for r in range(1,p):
        expect=0 if r<=m else 1 if r<=3*m else 0 if r<=4*m else -1
        assert h[r][0]==expect,(p,r,'h valuation',h[r][0],expect)
    for k in range(1,p):
        c=-12 if k<=2*m else 6 if k<=3*m else -6 if k<=4*m else 12
        pair=gamma(k)*gamma(p-k)
        assert pair%p**3==0
        assert pair//p**3%p==c*pow(k,-3,p)%p,(p,k,'reflection')
        r=p-k
        coefficient=(12*c*pow(k,-1,p)*h[r][1])%p
        actual=gamma(k)*b[r]%P
        exponent=3+h[r][0]
        assert actual%p**exponent==0
        assert actual//p**exponent%p==coefficient,(p,k,'transport',exponent)
    return p

if __name__=='__main__':
    ps=[p for p in range(7,998) if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]
    for p in ps: check(p)
    print('PASS',len(ps),'primes; reflections/transfers',sum(p-1 for p in ps))
