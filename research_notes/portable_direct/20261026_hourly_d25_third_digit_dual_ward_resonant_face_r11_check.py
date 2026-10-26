#!/usr/bin/env python3
"""Exact author-only checks for the third-digit dual-Ward source filtration.
No native Enterprise Math experiments or external-network access.
"""
from __future__ import annotations
from collections import defaultdict

CH = ((0, 2), (1, 2), (0, 3), (2, 2), (1, 3), (0, 4))


def inv(x, modulus):
    return pow(x % modulus, -1, modulus)


def run_prime(p):
    assert p >= 7 and p % 6 == 1
    m=(p-1)//6
    mod=p**3
    mod5=p**5
    i2=inv(2,mod); i6=inv(6,mod);i18=inv(18,mod);i36=inv(36,mod);i72=inv(72,mod)
    jets=[[0]*p for _ in range(5)]
    jets[0][0]=1
    for n in range(1,p):
        lhs=inv(n*(n-p*i2),mod)
        for a in range(5):
            v=(n-1-m)*(n-1-2*m)*jets[a][n-1]
            if a>=1:
                v+=3*n*jets[a-1][n]-(3*(n-1)-4*m)*jets[a-1][n-1]
            if a>=2:
                v+=2*jets[a-2][n-1]
            jets[a][n]=(v*lhs)%mod
    U={ch:0 for ch in CH};K=U.copy();R=U.copy();T=U.copy()
    for j in range(1,2*m+1):
        for ell in range(1,j+1):
            n=ell-j
            w=pow(2,n,mod)
            for ab in CH:
                a,b=ab
                mass=w*jets[a][j]*jets[b][p-ell]%mod
                U[ab]=(U[ab]+mass)%mod
                K[ab]=(K[ab]+j*mass)%mod
                R[ab]=(R[ab]+(j-(p-n)*i2)*mass)%mod
                T[ab]=(T[ab]+(1-6*n)*mass)%mod
    for ch in CH:
        assert T[ch]==((1-6*p)*U[ch]+12*(K[ch]-R[ch]))%mod,(p,ch,'T')
    # exact p-unit backward adjoint, with genuine leftmost rank moments
    L=1-2*m
    lam={0:0}
    for k in range(0,L,-1):
        lam[k-1]=((p-2*k)*lam[k]-pow(2,k,mod))*inv(p-2*k+1,mod)%mod
    delta=(pow(2,L,mod)-(p-2*L)*lam[L])%mod
    C={ch:(-2*m*delta*jets[ch[0]][2*m]*jets[ch[1]][p-1])%mod for ch in CH}
    assert C[(0,2)]==C[(0,3)]==C[(0,4)]==0
    # construct the precise full third-digit scalar bracket
    B=(T[(0,2)] +p*(6*U[(0,2)]-(T[(1,2)]+T[(0,3)])*i6)
      +p*p*((T[(2,2)]+T[(1,3)]+T[(0,4)])*i36-(U[(1,2)]+U[(0,3)])))%mod
    # Ward source bulk, no left faces; inherited genuine J/E source sum is R-C
    S={ch:(R[ch]-C[ch])%mod for ch in CH}
    source=(U[(0,2)]+12*(K[(0,2)]-S[(0,2)])
         -p*i6*(U[(1,2)]+U[(0,3)])
         -2*p*(K[(1,2)]+K[(0,3)]-S[(1,2)]-S[(0,3)])
         +p*p*i36*(U[(2,2)]+U[(1,3)]+U[(0,4)])
         +(p*p*i6*2)*(K[(2,2)]+K[(1,3)]+K[(0,4)]-S[(2,2)]-S[(1,3)]-S[(0,4)]))%mod
    face=(2*p*C[(1,2)]-p*p*inv(3,mod)*(C[(2,2)]+C[(1,3)]))%mod
    assert B==(source+face)%mod,(p,'ward')
    # Positive-rank/infinity counterpart for all six exact Hasse channels.
    N=2*m-1
    I0={ch:0 for ch in CH};I1=I0.copy();KP=I0.copy()
    YY={ch:[0]*(N+2) for ch in CH}
    for j in range(1,2*m+1):
        for ell in range(j+1,2*m+1):
            n=ell-j
            weight=pow(2,n,mod)
            for ch in CH:
                a,b=ch
                mass=jets[a][j]*jets[b][p-ell]%mod
                I0[ch]=(I0[ch]+weight*mass)%mod
                I1[ch]=(I1[ch]+weight*(6*n-1)*mass)%mod
                KP[ch]=(KP[ch]+weight*j*mass)%mod
                YY[ch][n]=(YY[ch][n]+(j-(p-n)*i2)*mass)%mod
    mu=[0]*(N+1)
    if N:
        mu[1]=2*inv(p-2,mod)%mod
        for n in range(2,N+1):
            mu[n]=(pow(2,n,mod)+(p-2*n+1)*mu[n-1])*inv(p-2*n,mod)%mod
    ZP={}
    for ch in CH:
        z=sum(mu[n]*((p-2*n)*YY[ch][n]-(p-2*n-1)*YY[ch][n+1]) for n in range(1,N+1))%mod
        assert z==sum(pow(2,n,mod)*YY[ch][n] for n in range(1,N+1))%mod,(p,ch,'positive source')
        assert I1[ch]==((6*p-1)*I0[ch]-12*KP[ch]+12*z)%mod,(p,ch,'I1')
        ZP[ch]=z
    I3=(I1[(0,2)] +p*(-6*I0[(0,2)]-i6*(I1[(1,2)]+I1[(0,3)]))
        +p*p*(i36*(I1[(2,2)]+I1[(1,3)]+I1[(0,4)])+I0[(1,2)]+I0[(0,3)]))%mod
    I3src=(-I0[(0,2)]-12*(KP[(0,2)]-ZP[(0,2)])
          +p*i6*(I0[(1,2)]+I0[(0,3)])
          +2*p*(KP[(1,2)]+KP[(0,3)]-ZP[(1,2)]-ZP[(0,3)])
          -p*p*i36*(I0[(2,2)]+I0[(1,3)]+I0[(0,4)])
          -p*p*inv(3,mod)*(KP[(2,2)]+KP[(1,3)]+KP[(0,4)]-ZP[(2,2)]-ZP[(1,3)]-ZP[(0,4)]))%mod
    assert I3==I3src,(p,'positive third-digit')
    # high-high population, independently constructed from high jets
    f=[0]*p
    for a in range(2*m+1,p):
        f[a]=jets[2][a]*pow(2,-a,p)%p
    suf0=[0]*(p+1);suf1=[0]*(p+1)
    for a in range(p-1,-1,-1):
        suf0[a]=(suf0[a+1]+f[a])%p
        suf1[a]=(suf1[a+1]+a*f[a])%p
    HH=0
    for a in range(2*m+1,p):
        low=max(2*m+1,p-a)
        HH=(HH+f[a]*((6*a+1)*suf0[low]+6*suf1[low]))%p
    # independent original Q modulo p^5, using original hypergeometric recurrence
    orig=[0]*p;orig[0]=1
    for n in range(p-1):
        orig[n+1]=orig[n]*(6*n+1)*(3*n+1)*inv(36*(n+1)**2,mod5)%mod5
    suf0q=[0]*(p+1);suf1q=[0]*(p+1)
    for a in range(p-1,-1,-1):
        suf0q[a]=(suf0q[a+1]+orig[a])%mod5
        suf1q[a]=(suf1q[a+1]+a*orig[a])%mod5
    Q=sum(orig[a]*((6*a+1)*suf0q[p-a]+6*suf1q[p-a]) for a in range(1,p))%mod5
    assert Q%(p*p)==0,(p,'not divisible',Q)
    actual=(Q//(p*p))%mod
    gamma=pow(2,-p,mod)*i18%mod
    predicted=(gamma*B+(p*p)*inv(1296,mod)*HH)%mod
    assert actual==predicted,(p,'original Q',actual,predicted)
    low_high=gamma*B%mod;high_high=(p*p)*inv(1296,mod)*HH%mod
    assert actual==(low_high+high_high)%mod
    face_scalar=gamma*face%mod
    if p==733:
        assert delta%(p*p)==p*241
        assert C[(1,2)]%(p*p)==p*410
        assert C[(2,2)]%p==0 and C[(1,3)]%p==0
        assert face%(p**3)==p*p*87
        assert face_scalar==p*p*430
        assert actual==99531942
        assert high_high==71459437
    return {'p':p,'m':m,'delta_mod_p2':delta%(p*p),'C12_mod_p2':C[(1,2)]%(p*p),
            'C22_mod_p':C[(2,2)]%p,'C13_mod_p':C[(1,3)]%p,'B3':B,
            'face_B3':face,'face_original':face_scalar,'source_without_faces':source,
            'Q_div_p2_mod_p3':actual,'low_high':low_high,'high_high':high_high,
            'HH_mod_p':HH,'infinity_third_digit':I3}


def main():
    primes=[]
    for p in range(7,212):
        if p%6==1 and all(p%d for d in range(2,int(p**0.5)+1)):
            primes.append(p)
    primes.append(733)
    out=[run_prime(p) for p in primes]
    print('PASS',len(out),'target primes; all original-Q and independent high-high/third-digit Ward identities')
    for x in out:
        if x['p'] in (7,13,19,733):
            print(x)
if __name__=='__main__':main()
