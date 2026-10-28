#!/usr/bin/env python3
"""Independent exact modular guard: Clausen G versus rational Legendre polynomial.
Author-side finite checks only; no native H0/B0 evaluator or source admission.
"""
from math import comb

PRIMES=(7,13,19,31,37,43,61,67,73,211,373)
TARGET={13,19,37,43,61,67,211,373}

def inv(x,N): return pow(x%N,-1,N)

def mul_jet(a,b,M):
    return [sum(a[k]*b[i-k] for k in range(i+1))%M for i in range(3)]

def one(p):
    m=(p-1)//6;M=p**3;N=p**2
    assert p==6*m+1 and p>3
    I2=inv(2,M);I8=inv(8,M)
    H=[0]*(2*m+1);H2=[0]*(2*m+1)
    for k in range(1,2*m+1):
        H[k]=(H[k-1]+inv(k,M))%M
        H2[k]=(H2[k-1]+inv(k*k,M))%M
    A=[];P=[];G=[];E=[];F=[];V=[]
    gg=1;pp=1
    for j in range(m+1):
        if j:
            gg=gg*(j-1-m)*(j-1-2*m)*inv(j*(2*j-p),M)%M
            pp=pp*(j-1-m)*(2*m+2*j-1)*inv(4*j*j,M)%M
        b=comb(m,j)*comb(2*m,j)*inv(pow(2,j,M),M)%M
        h=H[j]; h2=H2[j];r=(H[2*m]-H[2*m-j])%M;r2=(H2[2*m]-H2[2*m-j])%M
        e=b*(h+r)%M
        f=b*(h*h+h2-r*r+r2)%M
        assert (gg-pp-p*I2*e-p*p*I8*f)%M==0,(p,j,'third-digit coefficient')
        # Verify both individual ports against independent products rather than only their difference.
        prod_num=1;prod_den=1
        for k in range(1,j+1): prod_den=prod_den*(1-p*I2*inv(k,M))%M
        for k in range(2*m-j+1,2*m+1):prod_num=prod_num*(1-p*I2*inv(k,M))%M
        assert gg==b*inv(prod_den,M)%M and pp==b*prod_num%M,(p,j,'individual products')
        A.append(b);P.append(pp);G.append(gg);E.append(e);F.append(f)
    def val(c):return sum(c)%M
    def deriv(c):return sum(j*c[j] for j in range(len(c)))%M
    g,gd=val(G),deriv(G); a,ad=val(P),deriv(P);e,ed=val(E),deriv(E);f=val(F)
    assert (g-a-p*I2*e-p*p*I8*f)%M==0
    assert (gd-ad-p*I2*ed)%N==0
    # Independent Legendre recurrence at x0=sqrt(2)/2 in the exact
    # quadratic algebra Z/(p^3)[T]/(T^2-2); no floating roots or guessed signs.
    def qa(x,y):return ((x[0]+y[0])%M,(x[1]+y[1])%M)
    def qs(x,y):return ((x[0]-y[0])%M,(x[1]-y[1])%M)
    def qm(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%M,(x[0]*y[1]+x[1]*y[0])%M)
    def qscale(x,k):return (x[0]*k%M,x[1]*k%M)
    x0=(0,I2)
    prev=(1,0);curr=x0
    for k in range(1,2*m):
        nxt=qscale(qs(qscale(qm(x0,curr),2*k+1),qscale(prev,k)),inv(k+1,M))
        prev,curr=curr,nxt
    assert curr==(a,0),(p,'independent rational Legendre recurrence')
    derivative_q=qscale(qm((0,I2),qs(prev,qm(x0,curr))),-2*m)
    assert derivative_q==(ad,0),(p,'independent Legendre derivative identity')
    # Independent exact original signed W (full cutoff), including valuation bands.
    W=0
    for n in range(p):
        tn=comb(2*n,n)**2*comb(3*n,n)%M
        W=(W+(6*n+1)*tn*inv(pow(216,n,M),M))%M
    # Triple-factor original jet; source-separate evaluation of D1,D2.
    x=[1,0,0];y=[1,0,0];z=[1,0,0];den=1
    J=[0,0,0];C1=C2=0
    a0=1
    for n in range(p):
        if n:
            k=n-1
            x=mul_jet(x,[(k-3*m)%M,I2,0],M)
            y=mul_jet(y,[(k-2*m)%M,inv(3,M),0],M)
            z=mul_jet(z,[(k-4*m)%M,(2*inv(3,M))%M,0],M)
            den=den*2*n*n*n%M
        xyz=mul_jet(mul_jet(x,y,M),z,M)
        t=[(6*n+1)*v*inv(den,M)%M for v in xyz]
        for i in range(3):J[i]=(J[i]+t[i])%M
        if n<=2*m:
            h=H[n];h2=H2[n]
            C1=(C1+t[0]*h)%M
            C2=(C2+t[0]*(9*h*h+5*h2))%M
    J0,J1,J2=J
    D1=(J1-3*I2*C1)%M; D2=(J2-I8*C2)%M
    assert (J0+p*J1+p*p*J2-W)%M==0,(p,'old-original-jet')
    assert (g*g+12*g*gd+p*D1+p*p*D2-W)%M==0,(p,'Clausen-original')
    result={'p':p,'m':m,'E_mod_p2':e%N,'F_mod_p':f%p,'Eprime_mod_p':ed%p,'G_mod_p3':g,'P_mod_p3':a,'Gp_mod_p2':gd%N,'Pp_mod_p2':ad%N,'W_mod_p3':W}
    if p in TARGET:
        assert g%p==a%p==0,(p,'CM0')
        q=(a//p)%N
        gamma=(g//p)%N
        gamma_from_leg=(q+I2*e+p*I8*f)%N
        assert gamma==gamma_from_leg,(p,'p2 gamma port')
        U=(12*gamma*gd+D1+p*(gamma*gamma+D2))%N
        assert U==(W//p)%N,(p,'existing Clausen p3')
        U_leg=(12*gamma_from_leg*(ad+p*I2*ed)+D1+p*((q+I2*e)**2+D2))%N
        assert U_leg==U,(p,'new Legendre p3')
        # Since G' is a unit at the CM0 root, construct the unique Hensel
        # lift z_p=1+p*d modulo p^3.  The derivative is independent of W.
        assert gd%p, (p,'simple CM0 root required')
        zroot=1
        for _ in range(3):
            gv=sum(G[j]*pow(zroot,j,M) for j in range(m+1))%M
            gpv=sum(j*G[j]*pow(zroot,j-1,M) for j in range(1,m+1))%M
            zroot=(zroot-gv*inv(gpv,M))%M
        assert zroot%p==1
        assert sum(G[j]*pow(zroot,j,M) for j in range(m+1))%M==0
        d=((zroot-1)%M)//p
        gpp=sum(j*(j-1)*G[j] for j in range(2,m+1))%M
        assert (gpp-3*m*gd-2*m*m*g)%M==0,(p,'hypergeometric ODE')
        gamma_root=(-d*gd-p*inv(2,N)*d*d*gpp)%N
        assert gamma_root==gamma,(p,'root-displacement expansion')
        U_root=(D1-12*d*gd*gd+p*(D2+4*d*d*gd*gd))%N
        assert U_root==U_leg,(p,'Hensel root p3 source bridge')
        result.update(q_mod_p2=q,gamma_mod_p2=gamma,delta_gamma_mod_p=(gamma-q)%p,
                      U_leg=U_leg,D1_mod_p2=D1%N,D2_mod_p=D2%p,
                      zroot_mod_p3=zroot,d_mod_p2=d,U_root=U_root,gpp_mod_p=gpp%p)
    return result

if __name__=='__main__':
    for p in PRIMES:
        r=one(p)
        print('CASE',r)
    print('PASS_D25_TRIPLE_PORT_LEGENDRE_CLAUSEN_EXACT_P3',len(PRIMES),'primes')
