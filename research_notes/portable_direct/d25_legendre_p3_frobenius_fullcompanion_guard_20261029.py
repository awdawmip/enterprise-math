#!/usr/bin/env python3
"""Exact finite p^3 Frobenius and full companion check (external arithmetic only).

No remote calls. Author-side evidence; not the native H0/B0 divided-power benchmark.
Uses Z/p^3[x]/(x^2-8/9) and integer binomial expansions, with distinct
Frobenius Q and Q^2 ports and complete n<p parameter jets.
"""
from math import comb

def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00' * len(sieve[d*d::d])
    return [p for p in range(5, limit) if sieve[p]]

def add(u, v, m):
    return ((u[0]+v[0])%m, (u[1]+v[1])%m)

def mul(u, v, m, q):
    return ((u[0]*v[0]+q*u[1]*v[1])%m,
            (u[0]*v[1]+u[1]*v[0])%m)

def scale(u, c, m):
    return (u[0]*c % m, u[1]*c % m)

def xpow(a, m, q):
    z = pow(q, a//2, m)
    return (z, 0) if a%2 == 0 else (0, z)

def a_power_coeffs(k, nmax, m, q):
    """Coefficients of (1-2*x*T+T*T)^k in the exact quadratic ring."""
    out = []
    qpow = [pow(q,j,m) for j in range(k+1)]
    for n in range(nmax+1):
        v0, v1 = 0, 0
        for b in range(max(0,n-k), n//2 + 1):
            a = n - 2*b
            if a+b > k:
                continue
            term = comb(k,b) * comb(k-b,a) * (-2)**a * qpow[a//2]
            if a % 2:
                v1 += term
            else:
                v0 += term
        out.append((v0%m,v1%m))
    return out

def conv_value(left, right, n, m, q):
    z = (0,0)
    for i in range(max(0,n-(len(right)-1)), min(n,len(left)-1)+1):
        z=add(z,mul(left[i],right[n-i],m,q),m)
    return z

def direct_legendre(n, m, q):
    """Independent exact binomial closed form, valid when p divides n."""
    s=(0,0)
    for j in range(n//2+1):
        c=(-1)**j * comb(n,j) * comb(2*n-2*j,n)
        s=add(s,scale(xpow(n-2*j,m,q),c,m),m)
    return scale(s,pow(pow(2,n,m),-1,m),m)

def frobenius_ports(p, e):
    m=p**3
    q=8*pow(9,-1,m)%m
    N=p+e
    k=(p-1)//2
    B=a_power_coeffs(k,min(N,p-1),m,q)
    Ap=a_power_coeffs(p,N,m,q)
    xp=xpow(p,m,q)
    A0=[(0,0)]*(N+1)
    A0[0]=(1,0)
    A0[p]=scale(xp,-2,m)
    # Q coefficients live in Z/p^2: lift p-multiples uniquely from Z/p^3.
    Q=[]
    for a,b in zip(Ap,A0):
        d=((a[0]-b[0])%m,(a[1]-b[1])%m)
        assert d[0]%p==0 and d[1]%p==0, (p,d)
        Q.append((d[0]//p,d[1]//p))
    cq=p*p
    c_e=conv_value(B,Q,e,cq,q%cq)
    c_N=conv_value(B,Q,N,cq,q%cq)
    first_carry=scale(add(c_N,scale(mul(xp,c_e,m,q),3,m),m), -p*pow(2,-1,m),m)
    q1=[(a%p,b%p) for a,b in Q]
    QQ=[conv_value(q1,q1,j,p,q%p) for j in range(N+1)]
    d_e=conv_value(B,QQ,e,p,q%p)
    d_N=conv_value(B,QQ,N,p,q%p)
    second_carry=scale(add(d_N,scale(mul(xp,d_e,m,q),5,m),m),3*p*p*pow(8,-1,m),m)
    first_term=mul(xp,B[e],m,q)
    value=add(add(first_term,first_carry,m),second_carry,m)
    exact=direct_legendre(N,m,q)
    assert value==exact, ('frobenius-p3',p,e,value,exact)
    assert add(first_term,first_carry,p*p)==(exact[0]%(p*p),exact[1]%(p*p))
    return dict(p=p,e=e,N=N,legendre=exact,first_term=first_term,
                carry_Q=first_carry,carry_Q2=second_carry,
                c_e=c_e,c_N=c_N,d_e=d_e,d_N=d_N)

def companion_ports(p):
    m=p**3
    z=pow(9,-1,m)
    half=pow(2,-1,m)
    h1=next(h for h in range(p) if (8*h+1)%p==0)
    h3=next(h for h in range(p) if (8*h+3)%p==0)
    r,b=sorted((h1,h3))
    lam=5 if p%8 in (5,7) else 1
    delta=lam*p*pow(8,-1,m)%m
    a=[0]*p; g=[0]*p; j=[0]*p
    a[0]=1
    for n in range(p-1):
        mul_a=(n-r)*(n+r+half)%m
        mul_l=(2*r+half)%m
        inv=pow((n+1)**2,-1,m)
        a[n+1]=(mul_a*a[n]*inv)%m
        g[n+1]=(mul_a*g[n]+mul_l*a[n])*inv%m
        j[n+1]=(mul_a*j[n]+mul_l*g[n]-a[n])*inv%m
    zp=1
    f_val=g_val=j_val=0
    t=1; direct_full=0; direct_cut=0; direct_theta=0; tail_theta=0
    for n in range(p):
        f_val=(f_val+zp*a[n])%m
        g_val=(g_val+zp*g[n])%m
        j_val=(j_val+zp*j[n])%m
        direct_full=(direct_full+t)%m
        direct_theta=(direct_theta+n*t)%m
        if n<=b: direct_cut=(direct_cut+t)%m
        else: tail_theta=(tail_theta+n*t)%m
        if n<p-1:
            t=t*(8*n+1)*(8*n+3)*pow(576*(n+1)**2,-1,m)%m
            zp=zp*z%m
    jet1=delta*g_val%m
    jet2=delta*delta*j_val%m
    full=(f_val+jet1+jet2)%m
    assert full==direct_full, ('companion-full',p,full,direct_full)
    assert a[r+1]==0 and all(a[t]==0 for t in range(r+1,p))
    if p>=11:
        assert (direct_full-direct_cut)%m% (p*p)==0
    return dict(p=p,h1=h1,h3=h3,r=r,b=b,lambda_=lam,F=f_val,
                parameter_G=jet1,parameter_J=jet2,full=direct_full,
                cutoff=direct_cut,tail=(direct_full-direct_cut)%m,
                theta=direct_theta,tail_theta=tail_theta)

def run():
    samples=[p for p in primes_below(200) if p%8 in (5,7)] + [229,373]
    for p in samples:
        c=companion_ports(p)
        e=(p-1)//4
        assert 2*c['r']==p+e
        f=frobenius_ports(p,e)
        assert f['legendre']==(c['F'],0), (p,f['legendre'],c['F'])
        assert (f['legendre'][0]+c['parameter_G']+c['parameter_J'])%(p**3)==c['full']
        if p in (13,23,37,373):
            print('SOURCE_CERT',p, 'p3',p**3,'r,b',(c['r'],c['b']),
                  'F',c['F'],'Q',f['carry_Q'],'Q2',f['carry_Q2'],
                  'G',c['parameter_G'],'J',c['parameter_J'],
                  'Kfull',c['full'],'Kcut',c['cutoff'],'tail',c['tail'],
                  'theta_tail',c['tail_theta'])
    for p in (5,7,11,13,17,19,23,29):
        for e in sorted({0,1,(p-1)//2,p-1}):
            frobenius_ports(p,e)
    print('PASS_P3_FROBENIUS_AND_FULL_ORIGINAL_JET',len(samples),'p=5,7 mod8 samples')
    print('PASS_ALL_E_BRANCHES',8*4)

if __name__=='__main__':
    run()
