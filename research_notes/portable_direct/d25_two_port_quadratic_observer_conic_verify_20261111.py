#!/usr/bin/env python3
"""Direct finite-field two-port conic check; independent of the Lucas L,J,H recurrence."""
def primes_up_to(n):
    s=bytearray([1])*(n+1);s[0]=s[1]=0
    for k in range(2,int(n**.5)+1):
        if s[k]:s[k*k:n+1:k]=bytes((n-k*k)//k+1)
    return (p for p in range(7,n+1) if s[p])
def inv(a,p):return pow(a%p,-1,p)
def one(p):
    eps=0 if p%6==1 else 1;m=(p-1-4*eps)//6
    N=-inv(pow(2,2*m+eps,p),p)%p
    seen=set();count=fixed=0
    for t in range(p):
        if t in (0,p-1,p-2) or t in seen: continue
        v=-2*(t+1)*inv(t+2,p)%p
        orbit={t,v};seen.update(orbit)
        lam=(t+v)%p;delta=((lam+4)**2-8)%p
        nu=inv(2,p) if len(orbit)==1 else 1;c=N*nu%p
        A=B=0
        for x in orbit:
            u=(x+1)*(x+2)**2*inv(x,p)%p
            V=pow(u,m,p)*pow(x+2,eps,p)%p
            w=(2-12*eps-(3+10*eps)*x)*inv(x+2,p)%p
            A=(A+N*V)%p;B=(B+N*V*w)%p
        if eps==0:
            lhs=(B-(2*lam+5)*A)**2%p
            rhs=4*delta*(A*A-c*c*pow(2,m+2,p))%p
        else:
            lhs=(32*A-(lam+4)*(B+13*A))**2%p
            rhs=delta*((B+13*A)**2-c*c*pow(2,m+10,p))%p
        assert lhs==rhs,(p,lam,A,B,lhs,rhs)
        fixed+=len(orbit)==1;count+=1
    return count,fixed
if __name__=="__main__":
    n=orbits=fixed=0
    for p in primes_up_to(2500):
        a,b=one(p);n+=1;orbits+=a;fixed+=b
    assert (n,orbits,fixed)==(364,210031,352)
    print({"primes":n,"checked_orbits":orbits,"fixed":fixed,"result":"PASS"})
