"""D25 double-tail 216/2304 check: integer modular and independent binomial checks."""
import json
from math import isqrt, comb, factorial

def primes(n):
    z=bytearray(b'\x01')*(n+1);z[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if z[p]: z[p*p:n+1:p]=b'\x00'*((n-p*p)//p+1)
    return [p for p in range(5,n+1) if z[p]]

def direct_modular(p):
    mod=p**3
    F=[1]*(4*p)
    for n in range(1,4*p):
        F[n]=F[n-1]*(n if n%p else 1)%mod
    sm=[0,0,0,0]
    for k in range(p):
        d=pow(F[k],-1,mod)
        b=F[2*k]*F[3*k]*factorial(2*k//p)*factorial(3*k//p)*pow(d,5,mod)*pow(216,-k,mod)%mod
        c=F[4*k]*factorial(4*k//p)*pow(d,4,mod)*pow(2304,-k,mod)%mod
        b=b*pow(p,2*k//p+3*k//p,mod)%mod
        c=c*pow(p,4*k//p,mod)%mod
        sm[0]=(sm[0]+(6*k+1)*b)%mod;sm[1]=(sm[1]+(8*k+1)*c)%mod
        if k<=(p-1)//2:
            sm[2]=(sm[2]+(6*k+1)*b)%mod;sm[3]=(sm[3]+(8*k+1)*c)%mod
        if k==(p+1)//2:
            high=(b//p**2%p,c//p**2%p)
    return sm,high

def predicted_high(p):
    h=(p-1)//2
    bounds=(2*p//3-h,3*p//4-h)
    val=[]
    for model,N in enumerate(bounds):
        a=1; acc=0
        for t in range(N):
            acc=(acc+(4+6*t if model==0 else 5+8*t)*a)%p
            if t+1<N:
                j=t+1
                a=a*j*pow(9 if model==0 else 18,-1,p)*pow(2*j+1,-3,p)%p
                if model==0:a=a*(6*j-1)*(6*j+1)%p
                else:a=a*(4*j-1)*(4*j+1)%p
        val.append(acc)
    chi6=1 if pow(6,(p-1)//2,p)==1 else -1
    return bounds,(chi6*pow(9,-1,p)*val[0]%p,pow(36,-1,p)*val[1]%p),chi6

def independent_binomial(p,expect):
    m=p**3;S=[0]*4
    for k in range(p):
        b=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)%m
        c=(factorial(4*k)//factorial(k)**4)*pow(2304,-k,m)%m
        S[0]=(S[0]+(6*k+1)*b)%m;S[1]=(S[1]+(8*k+1)*c)%m
        if k<=(p-1)//2:
            S[2]=(S[2]+(6*k+1)*b)%m;S[3]=(S[3]+(8*k+1)*c)%m
    assert S==expect

def run():
    ps=primes(2000);rows=[]
    for p in ps:
        sm,high=direct_modular(p)
        bounds,(b_tail,c_tail),chi=predicted_high(p)
        assert high==(chi*pow(9,-1,p)%p,pow(36,-1,p))
        assert (sm[0]-sm[2])%p**3==p**2*b_tail
        assert (sm[1]-sm[3])%p**3==p**2*c_tail
        assert (sm[0]-sm[1]-sm[2]+sm[3])%p**3==p**2*((b_tail-c_tail)%p)
        assert c_tail==0, ('finite-range conjecture falsified',p)
        assert (sm[0]-sm[1])%p**3==0,('finite bridge conjecture falsified',p)
        if p in [5,7,11,13,19,37,43,373]:independent_binomial(p,sm)
        if p in [13,19,37,373]:
            rows.append({'p':p,'half':((sm[2]-sm[3])%p**3)//p**2,
                        '216_tail':b_tail,'2304_tail':c_tail,'full':sm[:2],
                        'half_values':sm[2:]})
    assert len(ps)==301 and len([p for p in ps if p%24 in (13,19)])==77
    return {'schema':'D25_216_2304_TWO_TAIL_CHECK_V1','domain':'301 primes 5<=p<=2000',
            'checked':301,'target_checked':77,'exact_tail_identities':'301/301 PASS',
            '2304_tail_zero_finite_conjecture':'301/301 PASS',
            '216_2304_bridge_finite_conjecture':'301/301 PASS',
            'independent_original_binomial_primes':[5,7,11,13,19,37,43,373],
            'selected':rows}
if __name__=='__main__':print(json.dumps(run(),indent=2))
