"""Exact source-jet audit of the inert Jacobi self-Green identity.

This is an author test, not independent mathematical review or native CM work.
"""
def primes_upto(n):
    sieve=bytearray(b"\x01")*(n+1); sieve[:2]=b"\x00\x00"
    for d in range(2,int(n**0.5)+1):
        if sieve[d]: sieve[d*d:n+1:d]=b"\x00"*((n-d*d)//d+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]


def check(p):
    mod=p*p
    m=(p-1)//6
    inv2=pow(2,-1,mod)
    a,b,c=1,0,0
    zpow=1
    U=U1=U2=V=V1=Y=Y1=Y2=0

    # Taylor jets for b_n(m+t)=(a+b*t+c*t^2) mod t^3,
    # with original denominator (n!)^2 a p-unit for n<p.
    for n in range(p):
        U=(U+a*zpow)%mod
        U1=(U1+n*a*zpow)%mod
        U2=(U2+n*n*a*zpow)%mod
        V=(V+b*zpow)%mod
        V1=(V1+n*b*zpow)%mod
        Y=(Y+2*c*zpow)%mod
        Y1=(Y1+2*n*c*zpow)%mod
        Y2=(Y2+2*n*n*c*zpow)%mod
        if n==p-1:
            terminal_half_second_jet=c
            break
        d=pow((n+1)**2,-1,mod)
        P=(n-m)*(n-2*m)
        L=-(3*n-4*m)
        a,b,c=(P*a*d)%mod,((P*b+L*a)*d)%mod,((P*c+L*b+2*a)*d)%mod
        zpow=zpow*inv2%mod

    K=(-40*m*m*terminal_half_second_jet)%mod
    # Evaluate the Wronskian polynomial differential operator at z=1/2.
    green=(U*(Y2+3*m*Y1)-Y*(U2+3*m*U1))%mod
    rhs_port=(-2*(3*V1-4*m*V)+4*U+K*pow(2,1-p,mod))%mod
    assert (U2+3*m*U1-2*m*m*U)%mod==0
    assert green==U*rhs_port%mod

    # This pairing is the original endpoint second-jet ODE times U.
    assert (Y2+3*m*Y1-2*m*m*Y-rhs_port)%mod==0
    if p%24 in (13,19):
        assert U%p==0, (p,U)
        assert green%p==0
        lifted=(green//p)%p
        predicted=(U//p)*(-2*(3*V1-4*m*V)-4)%p
        assert lifted==predicted,(p,lifted,predicted)
        return p,(U//p)%p,lifted
    return None


if __name__=="__main__":
    all_primes=primes_upto(373)
    targets=[x for x in (check(p) for p in all_primes) if x]
    assert len(all_primes)==35 and len(targets)==19
    print("PASS",len(all_primes),"eligible p-local checks and",len(targets),"target-class normalized ports")
    for row in targets:
        if row[0] in (13,19,37,43,373): print(row)
