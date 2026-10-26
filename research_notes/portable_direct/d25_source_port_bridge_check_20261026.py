#!/usr/bin/env python3
"""Author-only exact arithmetic check of frozen R_p / Clausen boundary / LIFT ports.
This is neither a native H0/B0 experiment nor a mathematical proof.
"""

def calc(p):
    assert p % 24 in (13, 19) and p >= 13
    mod = p**3
    b, c = 1, 1
    M = N = W = 0
    bs = []
    ball = []
    for k in range(p):
        ball.append(b)
        M = (M + b) % mod
        N = (N + k*b) % mod
        W = (W + (6*k+1)*c) % mod
        if k <= (p-1)//6:
            bs.append(b%p)
        if k < p-1:
            b = b*(6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, mod) % mod
            c = c*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, mod) % mod
    h=(M+12*N)%mod
    Q=(M*h-W)%mod
    # Independent direct signed Clausen cutoff convolution: no use of W or h.
    Qdirect = sum((6*(i+j)+1)*ball[i]*ball[j]
                  for i in range(p) for j in range(p-i,p)) % mod
    assert Q==Qdirect
    assert M%p == 0 and Q%(p*p) == 0 and W%(p*p) == p
    G=M//p
    assert (G*h-1)%p == 0
    Delta=((G*h-1)%(p*p))//p
    m=(p-1)//6

    # Reflection: recurrence independently proved for high-rank coefficients.
    v=pow(10,-1,p)
    V=J=R_ref=0
    for i in range(1,m+1):
        if i>1:
            j=i-1
            v=v*36*j*j*pow((6*j+5)*(3*j+2),-1,p)%p
        V=(V+v)%p
        J=(J+i*v)%p
        R_ref=(R_ref+2*bs[i]*((6*i+1)*V-6*J))%p

    # Original frozen R uses the factorial/Pochhammer product C_a, NOT v.
    # C_a=36^(a-1)*((a-1)!)^2 / product_{j=0}^{a-1}(6j+5)(3j+2).
    Cs=[]
    fac=1
    den=1
    for a in range(1,m+1):
        if a>1: fac=fac*(a-1)%p
        den=den*(6*a-1)*(3*a-1)%p
        Cs.append(pow(36,a-1,p)*fac*fac*pow(den,-1,p)%p)
    R_classic=2*sum(bs[i]*sum((1+6*(i-a))*Cs[a-1]
                               for a in range(1,i+1))
                    for i in range(1,m+1)) % p
    assert R_classic == R_ref
    q=Q//(p*p)
    e=(W-p)%(p**3)
    assert e%(p*p)==0
    e=e//(p*p)
    assert q==R_classic and (Delta-R_classic)%p==e
    return {'p':p,'M_mod_p3':M,'h_mod_p2':h%(p*p),'W_mod_p3':W,
            'Q_div_p2_mod_p':q,'R_original':R_classic,
            'R_reflection':R_ref,'Delta_original':Delta,
            'Delta_minus_R':(Delta-R_classic)%p,'W_minus_p_div_p2':e}

if __name__=='__main__':
    for p in [13,19,37,43,211,373]:
        print(calc(p))
