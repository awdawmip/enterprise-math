#!/usr/bin/env python3
"""Original frozen D25 scalar-port exact fixture, not native H0/B0 computation."""
import json
from math import factorial

def scalar_ports(p):
    assert p > 3 and all(p % j for j in range(2, int(p**0.5)+1))
    assert p % 24 in (13, 19)
    p2, p3 = p*p, p*p*p
    rec_B = [1]
    for k in range(p-1):
        den = 36*(k+1)**2
        rec_B.append(rec_B[-1]*(6*k+1)*(3*k+1)*pow(den, -1, p3) % p3)
    prod_B = []
    num6, num3, den = 1,1,1
    for k in range(p):
        if k:
            num6 *= 6*(k-1)+1
            num3 *= 3*(k-1)+1
            den *= 36*k*k
        prod_B.append((num6%p3)*(num3%p3)*pow(den%p3,-1,p3)%p3)
    assert rec_B == prod_B
    g = sum(rec_B) % p3
    h = sum((12*k+1)*x for k,x in enumerate(rec_B)) % p3
    assert g % p == 0
    G = (g//p) % p2
    product = (G*h) % p2
    assert (product-1)%p==0
    delta = (product-1)//p % p
    a = [1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,p3)%p3)
    W1=sum((6*k+1)*v for k,v in enumerate(a))%p3
    W2=0
    for k in range(p):
        v=(pow(216,-k,p3)*
           ( (factorial(2*k)//(factorial(k)**2))**2 ) *
            (factorial(3*k)//(factorial(k)*factorial(2*k))) )%p3
        assert v==a[k], (p,k,v,a[k])
        W2+=(6*k+1)*v
    W2%=p3
    assert W1==W2
    Qsum=0
    for i in range(p):
        for j in range(p-i,p):
            Qsum+=(6*(i+j)+1)*rec_B[i]*rec_B[j]
    Qsum%=p3
    conv=[0]*(2*p-1)
    for i in range(p):
        for j in range(p):
            conv[i+j]=(conv[i+j]+rec_B[i]*rec_B[j])%p3
    Qconv=sum((6*n+1)*conv[n] for n in range(p,2*p-1))%p3
    assert Qsum == Qconv
    assert Qsum%p2==0
    R=Qsum//p2
    assert R==delta
    assert (g*h-Qsum)%p3==W1
    assert W1==p
    m=(p-1)//6
    C=[0, pow(10,-1,p)]
    for a_idx in range(1,m):
        den=(6*a_idx+5)*(3*a_idx+2)
        C.append(C[-1]*36*a_idx**2*pow(den,-1,p)%p)
    Rref=2*sum((rec_B[i]%p)*sum((1+6*(i-a_idx))*C[a_idx] for a_idx in range(1,i+1)) for i in range(1,m+1))%p
    assert Rref==R
    g0, h0 = G % p, h % p
    g1, h1 = G // p, (h % p2) // p
    carry = ((g0*h0-1)//p) % p
    from_G_second = g1*h0 % p
    from_h_second = g0*h1 % p
    assert (carry + from_G_second + from_h_second) % p == delta
    wrong_reflection_plus = (delta + Rref) % p
    assert (g*h+Qsum-p) % p2 == 0
    if p == 373:
        assert (carry, from_G_second, from_h_second) == (11, 256, 302)
        assert wrong_reflection_plus == 19
        assert ((g*h + Qsum) % p3) == 2643824
    return dict(carry=carry, from_G_second=from_G_second, from_h_second=from_h_second,
                negative_control_zero_filled=carry, negative_control_wrong_reflection_sign=wrong_reflection_plus,
                p=p,p2=p2,p3=p3,g_mod_p3=g,h_mod_p3=h,G_mod_p2=G,h_mod_p2=h%p2,
                Gh_mod_p2=product,Delta=delta,Q_mod_p3=Qsum,R_frozen_reflection=Rref,
                W_mod_p3=W1,linear_signed_remainder=(W1-p)//p2 %p,
                W_mod_p2=W1%p2,first_digit_G=G%p,first_digit_h=h%p)

if __name__=='__main__':
    rows=[scalar_ports(p) for p in [13,19,109,139,157,373]]
    for x in rows:
        print(json.dumps(x,ensure_ascii=False,sort_keys=True))
