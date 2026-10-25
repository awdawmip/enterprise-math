#!/usr/bin/env python3
"""Author-side exact third-digit Clausen tail certificate; not native benchmark."""
from math import isqrt
from fractions import Fraction

def primes_below(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[0:2]=b'\x00\x00'
    for q in range(2,isqrt(limit)+1):
        if sieve[q]:sieve[q*q::q]=b'\x00'*((limit-q*q)//q+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]

def r_sequence(p):
    mod=p**3
    r=[1]
    for n in range(p-1):
        r.append((r[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,mod))%mod)
    return r

def a_sequence(p):
    mod=p**3
    a=1; w=0
    for n in range(p):
        w=(w+(6*n+1)*a)%mod
        if n+1 < p:
            # ((1/2)+n)((1/3)+n)((2/3)+n) / [2(n+1)^3]
            a=(a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod))%mod
    return w

def reflected_tail(p,r):
    m=(p-1)//6
    v=pow(10,-1,p) # v_h = r_(p-h) / p^2 mod p, h=1 first
    T=0; V=0; H=0
    for j in range(1,m+1):
        if j>1:
            h=j-1
            v=v*36*h*h*pow((6*h+5)*(3*h+2),-1,p)%p
        assert r[p-j] % (p*p) == 0
        assert r[p-j]//(p*p)%p == v, (p,j,"reflected_rank")
        V=(V+v)%p;H=(H+j*v)%p
        T=(T+2*(r[j]%p)*((6*j+1)*V-6*H))%p
    return T

def direct_tail(p,r):
    mod=p**3
    accum=0
    for j in range(p):
        for k in range(p-j,p):
            accum=(accum+(6*(j+k)+1)*r[j]*r[k])%mod
    assert accum%p**2==0
    return accum//p**2

def check_fraction(m):
    p=6*m+1
    rs=[Fraction(1)]
    aa=[Fraction(1)]
    for n in range(p-1):
        rs.append(rs[-1]*Fraction((6*n+1)*(3*n+1),36*(n+1)**2))
        aa.append(aa[-1]*Fraction((2*n+1)*(3*n+1)*(3*n+2),36*(n+1)**3))
    for n in range(p):
        assert sum((rs[j]*rs[n-j] for j in range(n+1)),Fraction(0))==aa[n],(m,n)
    return p

def main():
    checked=primes_below(1200)
    for p in checked+[19963]:
        m=(p-1)//6
        mod=p**3
        r=r_sequence(p)
        W=a_sequence(p)
        R=sum(r)%mod;D=sum(n*x for n,x in enumerate(r))%mod
        T=reflected_tail(p,r)
        Hasse=1
        z=1
        for k in range(m):
            z=z*(m-k)*(2*m-k)*pow(2*(k+1)**2,-1,p)%p
            Hasse=(Hasse+z)%p
        assert Hasse==R%p,("Hasse",p)
        assert (R*R+12*R*D-p*p*T-W)%mod==0,('clausen',p)
        assert r[p-1]%(p*p)==0
        assert r[p-1]//(p*p)%p==pow(10,-1,p)
        if p<=139:
            assert T==direct_tail(p,r),('tail',p)
        if p%24 in (13,19):
            assert R%p==0,('R_supsing',p)
            U=(R//p)%(p*p)
            assert (W//p-(12*U*D+p*(U*U-T)))%(p*p)==0,('conditional_joint',p)
            assert (12*U*D)%p==1,('second_digit',p)
        if p in (7,13,19,37,43,211,19963):
            print('sample',{'p':p,'class':p%24,'W_mod_p3':W,'R_mod_p':R%p,'D_mod_p':D%p,'tail_coeff':T,'R_div_p_mod_p':(R//p)%p if R%p==0 else None})
    fractions=[check_fraction(m) for m in range(1,5)]
    print('PASS',{'all_p_eq_1_mod_6_le_1200':len(checked),'plus_large_p':19963,'full_Q_double_sum_checked_for_p_le_139':len([p for p in checked if p<=139]),'exact_Fraction_Clausen_checks':fractions})
    print('scope','Author-side exact rational identity and modular cross-check; no Source claim, native benchmark, independent review, or universal LIFT proof')
if __name__=='__main__':main()
