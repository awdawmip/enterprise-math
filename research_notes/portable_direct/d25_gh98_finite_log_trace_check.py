#!/usr/bin/env python3
"""GH-98 exact integer-only finite-log trace for the D25 reflected source.
No native MCP execution or theorem admission is asserted by this verifier.
"""

def reflected_h(p):
    assert p >= 7 and p % 4 == 3
    d = (p - 3) // 4
    h = [1]
    for j in range(d):
        num = pow(4*j + 3, 3, p)
        den = (4*j+4)*(4*j+5)*(4*j+6) % p
        h.append(h[-1] * num * pow(den, -1, p) % p)
    return h

def finite_log_coeff(t, p):
    acc = 0
    power = 1
    for n in range(1, p):
        power = power*t % p
        acc = (acc + power*pow(n, -1, p)) % p
    return acc

def finite_log_binomial(t, p):
    # Integer exact evaluation of (1-t^p-(1-t)^p)/p mod p.
    mod = p*p
    val = (1 - pow(t, p, mod) - pow(1-t, p, mod)) % mod
    assert val % p == 0
    return val//p

def fermat_q(u,p):
    if u % p == 0:
        return None
    z = (pow(u, p-1, p*p)-1) % (p*p)
    assert z % p == 0
    return z//p

def finite_log_fermat(t,p):
    a = 0 if t % p == 0 else t*fermat_q(t,p)
    b = 0 if (1-t) % p == 0 else (1-t)*fermat_q(1-t,p)
    return (-a-b) % p

def poly_h_value(h,x,p):
    v = 0
    for j in range(len(h)-1,-1,-1):
        v = (v*x + (8*j+5)*h[j]) % p
    return v

def direct_tail(h,p,a):
    d=len(h)-1
    s=0
    for j,hj in enumerate(h):
        n=d+1+j
        s=(s+(8*j+5)*hj*pow(a,n,p)*pow(n,-1,p)) % p
    return s

def trace(h,p,a,kernel=finite_log_binomial):
    d=len(h)-1
    inva=pow(a,-1,p)
    acc=0
    for x in range(1,p):
        t=x*inva % p
        acc=(acc+pow(x,d,p)*poly_h_value(h,x,p)*kernel(t,p))%p
    return a*acc%p

def trace_pair(h,p,a):
    d=len(h)-1
    inva=pow(a,-1,p)
    acc=0
    for x in range(p):
        y=(a-x)%p
        qx=pow(x,d,p)*poly_h_value(h,x,p)%p
        qy=pow(y,d,p)*poly_h_value(h,y,p)%p
        acc=(acc+(qx+qy)*finite_log_binomial(x*inva%p,p))%p
    return a*acc*pow(2,-1,p)%p

def verify():
    tested=0
    all_a=0
    for p in (7,11,19,23,31,43,47,59,67,71,83,103,167,3347):
        assert p>=7 and all(p%q for q in range(2,int(p**0.5)+1))
        h=reflected_h(p)
        alist=range(1,p) if p<100 else [9]
        for a in alist:
            aa=a%p
            v=direct_tail(h,p,aa)
            v1=trace(h,p,aa,finite_log_binomial)
            v2=trace(h,p,aa,finite_log_fermat)
            v3=trace_pair(h,p,aa)
            assert v==v1==v2==v3,(p,a,v,v1,v2,v3)
            all_a+=1
        tested+=1
        sample=9%p
        print('p',p,'d',len(h)-1,'R(9)',direct_tail(h,p,sample),'trace',trace(h,p,sample,finite_log_fermat))
        if p<100:
            for t in range(p):
                l=finite_log_coeff(t,p)
                assert l==finite_log_binomial(t,p)==finite_log_fermat(t,p)
                assert l==finite_log_binomial((1-t)%p,p)
                if t:
                    assert (l+t*finite_log_binomial(pow(t,-1,p),p))%p==0
    assert direct_tail(reflected_h(3347),3347,9)==0
    assert direct_tail(reflected_h(7),7,9)==1
    print('PASS_GH98_FINITE_LOG_FERMAT_AND_SYMMETRIC_TRACE; primes',tested,'specializations',all_a)

if __name__=='__main__':
    verify()
