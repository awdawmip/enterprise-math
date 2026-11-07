"""Pure integer verification of D25 exact p^3 Picard--Fuchs boundary sources."""
from math import comb

def check(p):
    m=p**4
    C=[comb(2*k,k)**2*comb(3*k,k)*pow(108,-k,m)%m for k in range(p+1)]
    D=[comb(2*k,k)**2*comb(4*k,2*k)*pow(256,-k,m)%m for k in range(p+1)]
    out={}
    for name, a, denominator, xden, source_den in (('U',C,18,2,18),('B',D,32,9,96)):
        def q(j):
            return ((2*j+1)*(3*j+1)*(3*j+2) if name=='U'
                    else (4*j+1)*(2*j+1)*(4*j+3))
        coeff=[((k**3*a[k] if k<p else 0)
                -q(k-1)*pow(denominator,-1,m)*a[k-1])%m
               for k in range(1,p+1)]
        assert all(v==0 for v in coeff[:-1])
        assert coeff[-1]==-p**3*a[p]%m
        special=coeff[-1]*pow(xden,-p,m)%m
        assert special==(-p**3*pow(source_den,-1,m))%m
        out[name]=dict(high_coeff=coeff[-1],special=special)
    return {'p':p,'modulus':m,'coefficients':out}

if __name__=='__main__':
    for p in (5,7,11,19,373):
        print(check(p))
