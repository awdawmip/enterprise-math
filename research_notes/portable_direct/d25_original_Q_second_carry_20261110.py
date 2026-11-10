"""D25 author-side: original Clausen cutoff Q/p² through the next digit.
Finite exact arithmetic; not native H0/B0 or Source acceptance.
"""
from math import comb

def primes(limit):
    s = bytearray(b'\1') * (limit+1)
    s[:2] = b'\0\0'
    for d in range(2,int(limit**.5)+1):
        if s[d]:
            s[d*d:limit+1:d] = b'\0'*((limit-d*d)//d+1)
    return [p for p in range(7,limit+1) if s[p] and p%6==1]

def check(p, independent=False):
    assert p>3 and p%6==1
    m,mod4,mod2=(p-1)//6,p**4,p**2
    B=[1]
    for k in range(p-1):
        B.append(B[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod4)%mod4)
    M=sum(B)%mod4
    N=sum(k*b for k,b in enumerate(B))%mod4
    h=(M+12*N)%mod4
    A=[1]
    for k in range(p-1):
        A.append(A[-1]*(2*k+1)*(3*k+1)*(3*k+2)
                 *pow(36*(k+1)**3,-1,mod4)%mod4)
    W=sum((6*k+1)*a for k,a in enumerate(A))%mod4
    Q=(M*h-W)%mod4
    assert Q%p**2==0
    v=[None]*(2*m+1)
    v[1]=(B[p-1]//p**2)%mod2
    assert v[1]%p==pow(10,-1,p)
    for a in range(1,2*m):
        v[a+1]=(v[a]*36*(p-a)**2
                 *pow((6*p-6*a-5)*(3*p-3*a-2),-1,mod2))%mod2
        assert v[a+1]==(B[p-a-1]//p**2)%mod2
    L=2*sum(B[i]*(6*p+6*(i-a)+1)*v[a]
            for i in range(1,m+1) for a in range(1,i+1))%mod2
    C=2*p*sum((B[i]//p)*(6*(i-a)+1)*(v[a]%p)
              for i in range(m+1,2*m+1) for a in range(1,i+1))%mod2
    R2=(L+C)%mod2
    assert R2==Q//p**2
    if independent:
        raw=[comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod4)%mod4 for k in range(p)]
        assert sum((6*k+1)*raw[k] for k in range(p))%mod4==W
        q_direct=sum((6*(i+j)+1)*B[i]*B[j]
                     for i in range(p) for j in range(p-i,p))%mod4
        assert q_direct==Q
    out=dict(p=p,v1=v[1],signed_low=L,signed_middle=C,R2=R2,R=R2%p,W_mod_p4=W)
    if p%24 in (13,19):
        assert M%p==0 and W%p**2==p
        G=M//p
        Delta2=((G*h-1)%p**3)//p
        assert (Delta2-R2)%mod2==((W-p)%mod4)//p**2
        out['Delta2']=Delta2
        out['Delta']=Delta2%p
        if W%p**3==p:
            out['fourth_digit']=((W-p)%mod4)//p**3
            out['Delta_carry']=(Delta2-out['Delta'])//p
            out['R_carry']=(R2-out['R'])//p
            assert out['fourth_digit']==(out['Delta_carry']-out['R_carry'])%p
    return out

if __name__=='__main__':
    pp=primes(1000)
    for p in pp:
        r=check(p, p in (13,19,37,43,373,997))
        if p in (13,19,37,43,373,997): print(r)
    print('PASS',len(pp),'primes (p<=1000, p=1 mod6)')
