#!/usr/bin/env python3
"""Author-side exact modular check of the Legendre/Clausen Hensel-root transport.
No native H0/B0, Source claim, formal Result, or review is performed.
"""
from math import comb

TARGET_PRIMES=(13,19,37,43,61,67,211,373)

def inv(x,mod):
    return pow(x%mod,-1,mod)

def evaluate(cs,z,mod):
    value=0
    for c in reversed(cs):
        value=(value*z+c)%mod
    return value

def derivative(cs,order=1):
    if order==1:
        return [j*cs[j] for j in range(1,len(cs))]
    return [j*(j-1)*cs[j] for j in range(2,len(cs))]

def root_hensel(cs,p):
    mod=p**3
    z=1
    dcs=derivative(cs)
    assert evaluate(cs,z,p)==0
    assert evaluate(dcs,z,p)!=0
    for _ in range(3):
        z=(z-evaluate(cs,z,mod)*inv(evaluate(dcs,z,mod),mod))%mod
    assert z%p==1
    assert evaluate(cs,z,mod)==0
    return z

def mul_jet(a,b,mod):
    return [sum(a[k]*b[i-k] for k in range(i+1))%mod for i in range(3)]

def one(p):
    m=(p-1)//6
    mod=p**3; P=[];G=[];E=[];F=[]
    inv2=inv(2,mod)
    b=1;u=1;v=1; H=[0]*(2*m+1);H2=[0]*(2*m+1)
    for k in range(1,2*m+1):
        H[k]=(H[k-1]+inv(k,mod))%mod
        H2[k]=(H2[k-1]+inv(k*k,mod))%mod
    for j in range(m+1):
        if j:
            b=b*(m-j+1)*(2*m-j+1)*inv(2*j*j,mod)%mod
            u=u*(1-p*inv2*inv(j,mod))%mod
            v=v*(1-p*inv2*inv(2*m-j+1,mod))%mod
        # G_j / b_j = u^{-1}; P_j / b_j = product over r=2m-j+1..2m(1-p/(2r))=v
        # v recurrence adds r=2m-j+1 at each step.
        h=H[j];h2=H2[j]
        htail=(H[2*m]-H[2*m-j])%mod
        htail2=(H2[2*m]-H2[2*m-j])%mod
        P.append(b*v%mod)
        G.append(b*inv(u,mod)%mod)
        E.append(b*(h+htail)%mod)
        F.append(b*(h*h+h2-htail*htail+htail2)%mod)
        assert (G[j]-P[j]-p*inv2*E[j]-p*p*inv(8,mod)*F[j])%mod==0
    zP=root_hensel(P,p);zG=root_hensel(G,p)
    a=evaluate(derivative(P),zP,mod)
    b2=evaluate(derivative(P,2),zP,mod)
    e=evaluate(E,zP,mod)
    ep=evaluate(derivative(E),zP,mod)
    f=evaluate(F,zP,mod)
    root_delta=(zG-zP)%mod
    first=(-p*e*inv(2*a,mod))%mod
    correction=( -b2*e*e*inv(8*a*a*a,mod)+e*ep*inv(4*a*a,mod)-f*inv(8*a,mod) )%mod
    pred=(first+p*p*correction)%mod
    assert root_delta==pred,(p,root_delta,pred)
    # Legendre's hypergeometric ODE yields P''/P'=-1/2 mod p at the CM root.
    assert (b2*inv(a,mod)+inv(2,mod))%p==0,(p,'ODE')
    simplified=(first+p*p*(e*e*inv(16*a*a,mod)+e*ep*inv(4*a*a,mod)-f*inv(8*a,mod)))%mod
    assert simplified==root_delta,(p,'simplified-root')
    # The G/P roots differ already in the first p-adic digit when E(root) is a unit.
    shift_digit=(root_delta//p)%p
    assert shift_digit==(-e*inv(2*a,p))%p
    # Independently reconstruct original signed 216 sum and all three jet bands.
    W=0
    for n in range(p):
        signed=(6*n+1)*comb(2*n,n)**2*comb(3*n,n)
        W=(W+signed*inv(pow(216,n,mod),mod))%mod
    jets=[0,0,0]
    x=y=z=[1,0,0]
    den=1; C1=C2=0
    for n in range(p):
        if n:
            k=n-1
            x=mul_jet(x,[(k-3*m)%mod,inv(2,mod),0],mod)
            y=mul_jet(y,[(k-2*m)%mod,inv(3,mod),0],mod)
            z=mul_jet(z,[(k-4*m)%mod,2*inv(3,mod)%mod,0],mod)
            den=den*2*n*n*n%mod
        uv=mul_jet(mul_jet(x,y,mod),z,mod)
        terms=[(6*n+1)*q*inv(den,mod)%mod for q in uv]
        for j in range(3):
            jets[j]=(jets[j]+terms[j])%mod
        if n<=2*m:
            C1=(C1+terms[0]*H[n])%mod
            C2=(C2+terms[0]*(9*H[n]*H[n]+5*H2[n]))%mod
    J0,J1,J2=jets
    D1=(J1-3*inv(2,mod)*C1)%mod
    D2=(J2-inv(8,mod)*C2)%mod
    assert (W-J0-p*J1-p*p*J2)%mod==0,(p,'original signed jet')
    assert (W-evaluate(G,1,mod)**2-12*evaluate(G,1,mod)*evaluate(derivative(G),1,mod)-p*D1-p*p*D2)%mod==0,(p,'original Clausen')
    B=evaluate(derivative(P),1,mod)
    h=evaluate(derivative(E),1,mod)
    dL=((zP-1)%mod)//p
    t=((zG-zP)%mod)//p
    new_rhs=(D1-12*(dL+t)*B*B + p*(D2-12*(dL+t)*B*h+4*(dL+t)*(dL+t)*B*B))%(p*p)
    assert W%p==0
    assert new_rhs==(W//p)%(p*p),(p,'original216-source-root-transport')
    return dict(W_mod_p3=W,D1_mod_p2=D1%(p*p),D2_mod_p=D2%p,
                dL_mod_p2=dL,t_mod_p2=t,B_mod_p2=B%(p*p),h_mod_p=h%p,
                original_W_over_p=new_rhs,p=p,zP=zP,zG=zG,delta=root_delta,shift_digit=shift_digit,
                second_total=((root_delta-first)%mod//(p*p))%p,
                p2_curvature=(e*e*inv(16*a*a,p))%p,
                p2_Eprime=(e*ep*inv(4*a*a,p))%p,
                p2_F=(-f*inv(8*a,p))%p,
                E0=e%p,F0=f%p,derivative=a%p)

if __name__=='__main__':
    for p in TARGET_PRIMES:
        print('CERT',one(p))
    print('PASS_D25_ROOT_TRANSPORT_ALL_TARGET_INSTANCES',len(TARGET_PRIMES))
