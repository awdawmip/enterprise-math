#!/usr/bin/env python3
"""D25 author-side independent p-adic source-port check for carry-normalized first reflection digit.

Exact integer modular ring Z/(p^4); no floating point or native Enterprise Math experiment.
"""
from math import comb, isqrt


def primes_bound(n):
    return [p for p in range(7, n+1) if p % 6 == 1 and all(p % d for d in range(2,isqrt(p)+1))]


def check(p):
    m=(p-1)//6
    mod2=p*p
    mod4=mod2*mod2
    inv=lambda x:pow(x%p,-1,p)
    # Exact finite b coefficients modulo p^4. Every denominator is a unit for k<p.
    b=[1]
    for k in range(p-1):
        b.append(b[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod4)%mod4)
    c=[0]*(2*m+1)
    c[1]=pow(10,-1,mod2)
    for a in range(1,2*m):
        c[a+1]=c[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,mod2)%mod2
    q=[comb(m,i)*comb(2*m,i)*pow(2,-i,mod2)%mod2 for i in range(m+1)]
    # Independent Fermat quotient and residue carries for factors 6j+1 and 3j+1.
    q36=(pow(36,p-1,mod2)-1)//p
    carry6=sum((6*j+1)//p * inv((6*j+1)%p) for j in range(p-1) if j!=m)%p
    carry3=sum((3*j+1)//p * inv((3*j+1)%p) for j in range(p-1) if j!=2*m)%p
    beta=(7*inv(10)+carry6+carry3-q36)%p
    B1=b[p-1]//mod2 # b[p-1] divisible p^2 (stored mod p^4).
    beta_direct=(10*B1-1)//p%p if (10*B1-1)%p==0 else None
    assert beta==beta_direct,(p,beta,beta_direct)
    L=[0]*(m+1)
    for i in range(1,m+1):
        j=i-1
        L[i]=(L[i-1]+inv(6*j+1)+inv(3*j+1))%p
        assert (b[i]-q[i])%p==0
        d=((b[i]%mod2-q[i])%mod2)//p %p
        assert d==(q[i]*L[i])%p,('low-lift',p,i,d,q[i]*L[i]%p)
    T=[0]*(2*m+1)
    for a in range(2,2*m+1):
        r=a-1
        T[a]=(T[a-1]-2*inv(r)+6*inv(6*r+5)+3*inv(3*r+2))%p
    for a in range(1,2*m+1):
        assert b[p-a]%mod2==0,('high-band',p,a)
        direct=(b[p-a]//mod2)%mod2
        assert (direct-c[a])%p==0,('base',p,a)
        v=((direct-c[a])%mod2)//p
        predicted=(c[a]*(beta+T[a]))%p
        assert v==predicted,('backward-lift',p,a,v,predicted)
    # The source-resolved S_low has a global beta*R plus local low/backward harmonics.
    S_old=0;S_new=0;R=0;S_loc=0
    for i in range(1,m+1):
        for a in range(1,i+1):
            w=1+6*(i-a)
            d=((b[i]%mod2-q[i])%mod2)//p %p
            v=((b[p-a]//mod2-c[a])%mod2)//p
            S_old+=(2*(w*(d*c[a]+q[i]*v)+6*q[i]*c[a]))
            R+=2*w*q[i]*c[a]
            S_loc+=2*q[i]*c[a]*(w*(L[i]+T[a])+6)
            S_new+=2*q[i]*c[a]*(w*(L[i]+T[a]+beta)+6)
    assert S_old%p==S_new%p==(beta*R+S_loc)%p,('source',p)
    # Independent O(m) Hasse/adjoint prefix-moment evaluator.
    A = AT = B = BT = 0
    linear_low = 0
    H = [0] * (2*m+1)
    for i in range(1, 2*m+1):
        A = (A+c[i])%p
        B = (B+i*c[i])%p
        AT = (AT+c[i]*T[i])%p
        BT = (BT+i*c[i]*T[i])%p
        H[i] = ((1+6*i)*A-6*B)%p
        if i<=m:
            HT=((1+6*i)*AT-6*BT)%p
            linear_low=(linear_low+2*q[i]*(L[i]*H[i]+HT+6*A))%p
    assert linear_low==S_loc%p,('prefix-low',p)
    # Independently compare the known middle-high normalized K-H port.
    K=1
    middle_KH=0
    for r in range(1,m+1):
        middle_KH+=K*H[m+r]
        if r<m:
            K=K*3*r*(6*r+1)*inv((6*r+5)**2)%p
    mid_normalized=q[m]*inv(25)*middle_KH%p
    mid_direct=0
    for i in range(m+1,2*m+1):
        assert b[i]%p==0
        ui=(b[i]//p)%p
        for a in range(1,i+1):
            mid_direct+=2*(1+6*(i-a))*ui*c[a]
    assert mid_normalized==mid_direct%p,('middle',p)
    # Independent complete Clausen tail via suffix zeroth/first moments, mod p^4.
    suffix0=[0]*(p+1);suffix1=[0]*(p+1)
    for j in range(p-1,-1,-1):
        suffix0[j]=(suffix0[j+1]+b[j])%mod4
        suffix1[j]=(suffix1[j+1]+j*b[j])%mod4
    Q=sum(b[i]*((6*i+1)*suffix0[p-i]+6*suffix1[p-i]) for i in range(p))%mod4
    assert Q%mod2==0,('Clausen valuation',p)
    R_mod2=R%mod2
    assert (Q//mod2-R_mod2)%p==0,('first-reflection',p)
    port=( (Q//mod2-R_mod2)%mod2 )//p%p
    total=(beta*R_mod2+linear_low+mid_normalized)%p
    assert port==total==(S_old+mid_direct)%p,('complete second reflection',p,port,total)
    return {'p':p,'m':m,'beta':beta,'carry6':carry6,'carry3':carry3,
            'q36':q36,'R':R%p,'S_low':S_old%p,'S_local':S_loc%p,
            'S_mid':mid_normalized,'S_total':total,'reflected_next_digit':port}

if __name__=='__main__':
    ps=primes_bound(2000)
    for p in ps:
        r=check(p)
        if p in (7,13,19,37,43,67,211,373,997): print(r)
    print('PASS all',len(ps),'primes p<=2000 and p=1 (mod6); low/high lift every index; source port identity.')
    target=[p for p in ps if p%24 in (13,19)]
    print('TARGET coverage:',len(target))
