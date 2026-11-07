"""Finite Fricke two-jet transfer; portable original 216/2304 sums, not native H0/B0."""
from math import comb

def frac(a,b,m):return a*pow(b,-1,m)%m

def verify(p):
    m=p**4; da=pow(216,-1,m);db=pow(2304,-1,m)
    A=Au=B=Bu=0;ap=bp=1
    for k in range(p):
        x=comb(2*k,k)**2*comb(3*k,k)*ap%m
        y=comb(2*k,k)**2*comb(4*k,2*k)*bp%m
        A=(A+x)%m;Au=(Au+k*x)%m
        B=(B+y)%m;Bu=(Bu+k*y)%m
        ap=ap*da%m;bp=bp*db%m
    W=(A+6*Au)%m;V=(B+8*Bu)%m
    E=(A,-frac(3,4,m)*B%m)
    E1=((-2*Au+frac(7,8,m)*B+4*Bu)%m,
        (frac(3,2,m)*Au-frac(5,8,m)*B-3*Bu)%m)
    real=(E[0]+24*E1[0]+36*E1[1])%m
    imag=(E[1]+24*E1[1]+18*E1[0])%m
    assert imag==0 and real==(W-frac(3,2,m)*V)%m
    chi=1 if p%3==1 else -1
    assert (2*V-W-p*chi)%m==(frac(1,2,m)*V-p*chi-real)%m
    return dict(p=p,modulus=m,E=E,E_prime=E1,weighted_jet=real,W=W,V=V,
                bridge_residual=(2*V-W-p*chi)%m)

if __name__=="__main__":
    for p in (5,7,11,13,19,373):print(verify(p))
