#!/usr/bin/env python3
"""GH-95 exact finite source-tail search and exceptional p^2 witness.
Uses GH-91 standard-library polynomial helpers, not native experiments.
"""
from d25_gh91_uniform_linear_source_check import theta, ev, primes_lt

def r_tail(p, mod=None):
    assert p >= 7 and p % 4 == 3
    m = mod or p
    d = (p - 3) // 4
    h = 1
    zpow = pow(9, d + 1, m)
    tail = 0
    for j in range(d + 1):
        tail = (tail + (8*j + 5)*h*pow(d + 1 + j, -1, m)*zpow) % m
        zpow = zpow*9 % m
        if j < d:
            h = h*pow(4*j + 3, 3, m)*pow((4*j+4)*(4*j+5)*(4*j+6), -1, m) % m
    return tail

def exceptional_witness(p=3347):
    d = (p-3)//4
    m = p*p
    c, h = [1], [1]
    for j in range(d):
        c.append(c[-1]*pow(4*j+1, 3, m)*pow((4*j+2)*(4*j+3)*(4*j+4),-1,m)%m)
        h.append(h[-1]*pow(4*j+3, 3, m)*pow((4*j+4)*(4*j+5)*(4*j+6),-1,m)%m)
    assert c[d]%p and h[d]%p
    S,S1,S2=(ev(m,x,9) for x in (c,theta(m,c),theta(m,theta(m,c))))
    U,U1,U2,U3=(ev(m,x,9) for x in (h,theta(m,h),theta(m,theta(m,h)),theta(m,theta(m,theta(m,h)))))
    k4,k16=(pow(k,-1,m) for k in (4,16))
    def B(y,y1,y2):
        return ((1-9)*(y*S2-y1*S1+y2*S)+(9-3)*k4*y*S1
                +(3-45)*k4*y1*S+(2-63)*k16*y*S)%m
    W=(64*B(U1,U2,U3)+40*B(U,U1,U2))%m
    inv=[0]+[pow(j,-1,m) for j in range(1,2*d+2)]
    zp=[1]*(2*d+2)
    for j in range(1,2*d+2):zp[j]=zp[j-1]*9%m
    naive=5
    for j in range(d+1):
        naive=(naive+c[d]*(8*j+5)*h[j]*inv[d+1+j]*zp[d+1+j])%m
    jweights=[pow(j+3*k4,3,m)*h[j]%m for j in range(d+1)]
    for i in range(d+1):
        conv=sum(jweights[j]*inv[i+j+1]*zp[i+j+1] for j in range(d+1))
        naive=(naive+64*c[i]*conv)%m
    R=r_tail(p,m)
    T=(8*S1+S)%m
    H=(8*U1+5*U)%m
    assert (T,H)==(4659024,9863609)
    assert R%p==0 and (W-naive)%m==0
    # Both computations preserve the original S vs reflected U provenance.
    return dict(p=p,d=d,R_mod_p=R%p,R_mod_p2=R,
                W9_mod_p2=W,naive_W9_mod_p2=naive,
                p2=m,c_d_mod_p=c[d]%p,h_d_mod_p=h[d]%p,
                T9_mod_p2=T,T9_over_p=T//p,
                H9_mod_p2=H,H9_over_p=H//p)

def main():
    ps=primes_lt(30000)
    zeros=[p for p in ps if r_tail(p)==0]
    assert zeros == [3347], ('new zero set',zeros)
    print('PASS_GH95_REFLECTED_TAIL_SEARCH',len(ps),'primes 7<=p<30000 p=3 mod4')
    print('EXACT_ZERO_SET_WITHIN_RANGE',zeros)
    print('PASS_GH95_NONCYCLIC_P2_WITNESS',exceptional_witness())

if __name__=='__main__':main()
