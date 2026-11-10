"""AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED.
Exact O(p)-time, O(1)-auxiliary-space signed original Clausen Delta2/R2 certificate.
No native H0/B0 inference. Python integer modular arithmetic, denominator units checked.
"""
from math import comb, isqrt

def original_signed_stream(p):
    assert p > 3 and p % 6 == 1
    m, mod4, mod2 = (p-1)//6, p**4, p**2
    B, M, N = 1, 1, 0
    for k in range(p-1):
        B = B*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod4)%mod4
        M = (M+B)%mod4
        N = (N+(k+1)*B)%mod4
    h = (M+12*N)%mod4
    assert B%mod2 == 0
    v = B//mod2
    assert v%p == pow(10,-1,p)
    B, s, t, L, C = 1, 0, 0, 0, 0
    for i in range(1,2*m+1):
        B = B*(6*i-5)*(3*i-2)*pow(36*i*i,-1,mod4)%mod4
        if i>1:
            a = i-1
            v = v*36*(p-a)**2*pow((6*p-6*a-5)*(3*p-3*a-2),-1,mod2)%mod2
        s = (s+v)%mod2
        t = (t+i*v)%mod2
        if i<=m:
            L = (L + 2*B*((6*p+6*i+1)*s-6*t))%mod2
        else:
            assert B%p==0
            C = (C + 2*p*(B//p)*((6*i+1)*(s%p)-6*(t%p)))%mod2
    return M,N,h,(L+C)%mod2,L,C

def independent_suffix_and_3f2(p):
    mod4=p**4
    B=[1]*p
    for k in range(p-1):
        B[k+1]=B[k]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod4)%mod4
    Q=S=T=0
    for i in range(1,p):
        j=p-i
        S=(S+B[j])%mod4
        T=(T+j*B[j])%mod4
        Q=(Q+B[i]*((6*i+1)*S+6*T))%mod4
    a,W=1,0
    for k in range(p):
        W=(W+(6*k+1)*a)%mod4
        if k<p-1:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod4)%mod4
    return Q,W,B

def check(p,raw_double=False):
    assert p>3 and p%6==1
    assert all(p%d for d in range(2,isqrt(p)+1))
    mod4=p**4;mod2=p*p
    M,N,h,R2,L,C=original_signed_stream(p)
    Q,W,B=independent_suffix_and_3f2(p)
    assert Q%mod2==0 and Q//mod2==R2
    assert (M*h-Q)%mod4==W
    if raw_double:
        assert p<=373
        assert sum((6*(i+j)+1)*B[i]*B[j] for i in range(p) for j in range(p-i,p))%mod4==Q
        assert sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod4) for k in range(p))%mod4==W
    result=dict(p=p,p_mod24=p%24,R2=R2,L=L,C=C,W_mod_p4=W)
    if p%24 in (13,19):
        assert M%p==0 and W%mod2==p
        Delta2=((M//p*h-1)%p**3)//p
        assert (Delta2-R2)%mod2==((W-p)%mod4)//mod2
        result.update(Delta2=Delta2,Delta_minus_R_mod_p=(Delta2-R2)%p)
        if W%p**3==p:
            dD=(Delta2-Delta2%p)//p
            dR=(R2-R2%p)//p
            assert (dD-dR)%p==((W-p)%mod4)//p**3
            result.update(next_digit_bulk=dD,next_digit_cutoff=dR,next_digit_difference=(dD-dR)%p)
    return result

if __name__=="__main__":
    for p in (7,13,19,37,43,373,10069,10099):
        print(check(p,raw_double=(p<=373)))
    print("PASS exact original observer / constant-space streamed Q / independent source")
