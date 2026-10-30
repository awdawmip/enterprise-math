"""Independent exact modular coefficient certificate for terminating Gauss two-jets.

Portable author-side arithmetic only. This is not native D25 or a project admission.
"""
from math import isqrt


def primes(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit - 1) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * (((limit-1-d*d)//d) + 1)
    return (p for p in range(7,limit) if sieve[p] and p%6==1)


def check(p):
    assert p >= 7 and p%6==1
    m=(p-1)//6
    M=p**3
    fac=[1]*p
    for k in range(1,p):
        fac[k]=fac[k-1]*k%M
    invfac=[1]*p
    invfac[-1]=pow(fac[-1],-1,M)
    for k in range(p-1,0,-1):
        invfac[k-1]=invfac[k]*k%M
    h=[0]*p
    h2=[0]*p
    for j in range(1,p):
        x=pow(j,-1,M)
        h[j]=(h[j-1]+x)%M
        h2[j]=(h2[j-1]+x*x)%M
    inv2=pow(2,-1,M); inv3=pow(3,-1,M)
    inv6=pow(6,-1,M); inv9=pow(9,-1,M)
    inv18=pow(18,-1,M); inv36=pow(36,-1,M)
    invpow2=1
    c0=[];c1=[];c2=[];blocks=[0,0,0]
    for k in range(p):
        denom=(invpow2*invfac[k]*invfac[k])%M
        if k<=m:
            b=fac[m]*invfac[m-k]%M*fac[2*m]%M*invfac[2*m-k]%M*denom%M
            A=(- (h[m]-h[m-k])*inv6 - (h[2*m]-h[2*m-k])*inv3)%M
            T=((h2[m]-h2[m-k])*inv36+(h2[2*m]-h2[2*m-k])*inv9)%M
            v0=b
            v1=b*A%M
            v2=b*(A*A-T)*inv2%M
            block=0
        elif k<=2*m:
            sign=-1 if (m+k)%2 else 1
            b=(sign*fac[m]*fac[k-m-1]*fac[2*m]*invfac[2*m-k]*denom*inv6)%M
            A=((h[k-m-1]-h[m])*inv6-(h[2*m]-h[2*m-k])*inv3)%M
            v0=0;v1=b;v2=b*A%M
            block=1
        else:
            sign=-1 if m%2 else 1
            v0=v1=0
            v2=(sign*fac[m]*fac[2*m]*fac[k-m-1]*fac[k-2*m-1]*denom*inv18)%M
            block=2
        lead = (v0 if block==0 else v1 if block==1 else v2)
        assert lead % p, (p,k,'non-unit leading parameter jet')
        c0.append(v0);c1.append(v1);c2.append(v2)
        blocks[block]=(blocks[block]+v2)%M
        invpow2=invpow2*inv2%M
    # Independent recurrence: no harmonic input and no factorial input.
    r0=[1]+[0]*(p-1);r1=[0]*p;r2=[0]*p
    for k in range(p-1):
        rr=(k-m)*(k-2*m)
        d=(3*k-4*m)*inv6%M
        invd=pow(2*(k+1)**2,-1,M)
        r0[k+1]=rr*r0[k]*invd%M
        r1[k+1]=(rr*r1[k]+d*r0[k])*invd%M
        r2[k+1]=(rr*r2[k]+d*r1[k]+inv18*r0[k])*invd%M
    assert (c0,c1,c2)==(r0,r1,r2), (p,'full-polynomial jets')
    s0=sum(c0)%M;s1=sum(c1)%M;s2=sum(c2)%M
    q0=sum((1+12*k)*v for k,v in enumerate(c0))%M
    q1=sum((1+12*k)*v for k,v in enumerate(c1))%M
    # Independent original Gauss coefficients, ensures our t=p deformation is faithful.
    b=1;g=0;W=0
    for k in range(p):
        g=(g+b)%M
        W=(W+(1+12*k)*b)%M
        if k+1<p:
            b=(b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,M))%M
    assert g==(s0+p*s1+p*p*s2)%M, (p,'Gauss-specialization')
    assert W==(q0+p*q1+p*p*sum((1+12*k)*v for k,v in enumerate(c2)))%M
    ans={"p":p,"m":m,"P2_blocks_mod_p":tuple(x%p for x in blocks),
         "S0_over_p_mod_p":(s0//p)%p if s0%p==0 else None,
         "S1_mod_p":s1%p,"S2_mod_p":s2%p,"Q0_mod_p":q0%p,"Q1_mod_p":q1%p}
    if p%24 in (13,19):
        assert s0%p==0
        U=(s0//p+s1)%(p*p)
        assert (U*q0-1)%p==0
        tail=0
        for i in range(m+1):
            for j in range(max(2*m+1,p-i),p):
                tail=(tail+2*(1+6*(i+j))*c0[i]*c2[j])%p
        carry=((U*q0-1)%(p*p))//p
        jet=(s2*q0+U*q1)%p
        ans.update(carry=carry,jet=jet,projection=tail,residual=(carry+jet-tail)%p)
        # Different input: original 216 coefficients, independent of all Gauss-jet paths.
        a=1;A=0
        for k in range(p):
            A=(A+(6*k+1)*a)%M
            if k+1<p:
                a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
        assert (A-p)%M==((carry+jet-tail)%p)*p*p%M,(p,'original scalar')
    return ans


if __name__=='__main__':
    ps=list(primes(5000));t=0
    for p in ps:
        res=check(p)
        if 'carry' in res:t+=1
        if p in (7,13,19,37,157,373,1327): print('ANCHOR',res)
    print('SUMMARY primes_mod6_1',len(ps),'target',t,'full_jet_coefficients_checked',sum(ps),
          'modulus_each_p_cubed')
    print('PASS_D25_EXACT_HARMONIC_BLOCKS_INDEPENDENT_RAW_216')
