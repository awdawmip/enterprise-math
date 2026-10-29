#!/usr/bin/env python3
"""Portable exact p-adic check for the GH-95 reflected-tail exceptional prime.

Uses source-labelled c/h recurrences; no native Research CLAIM or experiment.
"""

from math import isqrt


def prime(n: int) -> bool:
    if n < 2:
        return False
    for q in range(2, isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def coefficients(p: int, modulus: int):
    assert prime(p) and p >= 7 and p % 4 == 3
    d = (p - 3) // 4
    c, h = [1], [1]
    for j in range(d):
        cden = (4*j + 2)*(4*j + 3)*(4*j + 4)
        hden = (4*j + 4)*(4*j + 5)*(4*j + 6)
        c.append(c[-1]*pow(4*j + 1, 3, modulus)*pow(cden, -1, modulus) % modulus)
        h.append(h[-1]*pow(4*j + 3, 3, modulus)*pow(hden, -1, modulus) % modulus)
    return c, h


def evaluate_source(p: int, modulus: int, z: int, c, h):
    d = (p - 3)//4
    z %= modulus
    powers = [1]
    for k in range(2*d+1):
        powers.append(powers[-1]*z % modulus)
    S = [sum(pow(i, k, modulus)*c[i]*powers[i] for i in range(d+1)) % modulus for k in range(3)]
    U = [sum(pow(j, k, modulus)*h[j]*powers[j] for j in range(d+1)) % modulus for k in range(4)]
    H = (8*U[1]+5*U[0])%modulus
    J = (8*U[2]+5*U[1])%modulus
    H_derivative = sum(j*(8*j+5)*h[j]*powers[j-1] for j in range(1,d+1)) % modulus
    assert J == z*H_derivative % modulus
    R = sum((8*j+5)*h[j]*powers[d+1+j]*pow(d+1+j,-1,modulus) for j in range(d+1))%modulus
    R_derivative = sum((8*j+5)*h[j]*powers[d+j] for j in range(d+1)) % modulus
    assert R_derivative == powers[d]*H%modulus
    return dict(S=S,U=U,H=H,J=J,H_derivative=H_derivative,R=R,R_derivative=R_derivative,powers=powers)


def concomitant(modulus,z,S,Y):
    inv4 = pow(4,-1,modulus)
    inv16 = pow(16,-1,modulus)
    s0,s1,s2 = S
    y0,y1,y2 = Y
    return ((1-z)*(y0*s2-y1*s1+y2*s0)
        +(z-3)*inv4*y0*s1
        +(3-5*z)*inv4*y1*s0
        +(2-7*z)*inv16*y0*s0)%modulus


def reconstructed_W_naive(p,modulus,c,h,powers):
    d = (p - 3)//4
    invs = [0]+[pow(k,-1,modulus) for k in range(1,2*d+2)]
    inv4 = pow(4,-1,modulus)
    R = sum((8*j+5)*h[j]*invs[d+1+j]*powers[d+1+j] for j in range(d+1)) % modulus
    weighted = [(j+3*inv4)**3*h[j] % modulus for j in range(d+1)]
    conv = 0
    for i in range(d+1):
        left=c[i]
        for j in range(d+1):
            conv += left*weighted[j]*invs[i+j+1]*powers[i+j+1]
        conv %= modulus
    return (5+64*conv+c[d]*R)%modulus


def main():
    p=3347
    d=(p-3)//4
    mod2=p*p
    mod3=p**3
    c,h=coefficients(p,mod3)
    o=evaluate_source(p,mod3,9,c,h)
    H2=o['H']%mod2
    R2=o['R']%mod2
    assert (H2,R2)==(9863609,3969542)
    assert c[d]%p==2034 and h[d]%p==1200
    assert o['H']%p==0 and o['R']%p==0
    Hder=o['H_derivative']%p
    assert Hder!=0
    t=(-((H2//p)*pow(Hder,-1,p)))%p
    lifted=9+p*t
    lift=evaluate_source(p,mod2,lifted,c,h)
    assert lift['H']==0 and lift['R']==R2
    assert (o['J']%p)==(9*Hder)%p
    assert o['R_derivative']%p==0
    # R''(9) ≡ 9^d H'(9) in F_p since H(9) ≡ 0.
    Rsecond_modp=(pow(9,d,p)*Hder)%p
    assert Rsecond_modp!=0
    S=o['S']; U=o['U']
    W=(64*concomitant(mod3,9,S,U[1:4]) +40*concomitant(mod3,9,S,U[:3]))%mod3
    naive=reconstructed_W_naive(p,mod3,c,h,o['powers'])
    delta=(W-naive)%mod3
    alpha_coeff=(-3*pow(2,-1,p)*(c[d]%p)*(R2//p))%p
    assert alpha_coeff==2968
    assert delta==p*p*alpha_coeff
    # Exact GH-93 p-local finite-source correction modulo p^3.
    gh93=(-3*p*pow(2,-1,mod3)*c[d]*o['R'] + 3*p*p*pow(4,-1,mod3)*c[d]*o['R'])%mod3
    assert delta==gh93
    assert delta%mod2==0 and delta!=0
    # Second-order p-adic jet at the unique lifted reflected-H root.
    lifted3=evaluate_source(p,mod3,lifted,c,h)
    r_prime_over_p=(o['R_derivative']%mod2)//p
    half_second=(Rsecond_modp*pow(2,-1,p))%p
    jet_coefficient=(t*r_prime_over_p+t*t*half_second)%p
    assert lifted3['R']==(o['R']+mod2*jet_coefficient)%mod3
    print('PASS_GH96_INDEPENDENT_SOURCE_RECURRENCE_AND_OBSERVERS')
    print('p',p,'d',d,'p2',mod2,'p3',mod3)
    print('c_d_mod_p',c[d]%p,'h_d_mod_p',h[d]%p)
    print('R(9)_mod_p2',R2,'R(9)/p_mod_p',R2//p)
    print('H(9)_mod_p2',H2,'H(9)/p_mod_p',H2//p)
    print('Hprime(9)_mod_p',Hder,'J(9)_mod_p',o['J']%p)
    print('Rprime(9)_mod_p',o['R_derivative']%p,'Rsecond(9)_mod_p',Rsecond_modp)
    print('unique_H_root_mod_p2',lifted,'shift_t',t,'H(lift)_mod_p2',lift['H'],'R(lift)_mod_p2',lift['R'])
    print('W(9)_mod_p3',W,'naive_W(9)_mod_p3',naive,'difference',delta,'difference/p2',alpha_coeff)
    print('R(9)_mod_p3',o['R'],'Rprime(9)/p_mod_p',r_prime_over_p,
          'half_Rsecond(9)_mod_p',half_second,'jet_shift_coefficient',jet_coefficient,
          'R(lifted_H)_mod_p3',lifted3['R'],'H(lifted_H)_mod_p3',lifted3['H'])
    print('PASS_GH96_DOUBLE_MODP_ROOT_NONLIFTABILITY_AND_EXACT_P2_DEFECT')

if __name__ == '__main__':
    main()
