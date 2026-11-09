"""D25 original 216/2304 weighted tangent through p^2. Exact finite observation."""
from math import comb, isqrt

def primes(bound):
    sieve=bytearray(b'\1')*bound
    sieve[:2]=b'\0\0'
    for k in range(2,isqrt(bound-1)+1):
        if sieve[k]:sieve[k*k:bound:k]=b'\0'*((bound-1-k*k)//k+1)
    return (p for p in range(5,bound) if sieve[p])

def derivative(p,mod):
    a=b=1; dA=dB=0
    for n in range(p):
        dA=(dA+n*(6*n+1)*a)%mod
        dB=(dB+n*(8*n+1)*b)%mod
        if n+1<p:
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod)%mod
            b=b*(2*n+1)*(4*n+1)*(4*n+3)*pow(288*(n+1)**3,-1,mod)%mod
    return dA,dB

def exact_binomial_derivative(p,mod):
    ia=pow(216,-1,mod);ib=pow(2304,-1,mod)
    dA=dB=0
    for n in range(p):
        dA=(dA+n*(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(ia,n,mod))%mod
        dB=(dB+n*(8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pow(ib,n,mod))%mod
    return dA,dB

ps=list(primes(4000))
for p in ps:
    chi=1 if p%3==1 else -1
    a,b=derivative(p,p*p)
    expected=(2 if chi==1 else -1)*p
    assert (3*a+8*chi*b-expected)%(p*p)==0,(p,a,b,expected)
anchors={}
for p in (5,7,11,13,17,19,23,31,37,43,73,373):
    a,b=derivative(p,p**3)
    assert (a,b)==exact_binomial_derivative(p,p**3)
    chi=1 if p%3==1 else -1
    eta=2 if chi==1 else -1
    third=((3*a+8*chi*b-eta*p)%(p**3))//(p*p)
    anchors[p]={'chi':chi,'p2_lift_coefficient':eta,'next_digit_mod_p':third}
print('PASS_D25_AFFINE_TANGENT_SECOND_DIGIT',len(ps),'primes 5<=p<4000',len(anchors),'independent exact binomial modp3')
print(anchors)
