#!/usr/bin/env python3
"""Independent p^3 L/M/U Gauss and Clausen tests, p=8k+3."""
def direct_g(p):
    M=p**3;g=[1]
    for n in range(p-1):g.append(g[-1]*(8*n+1)*(8*n+3)*pow(64*(n+1)**2,-1,M)%M)
    return g

def lift_g(p):
    k=(p-3)//8;a=3*k+1;M=p**3
    f=[1]*p
    for j in range(1,p):f[j]=f[j-1]*j%M
    invf=[1]*p;invf[-1]=pow(f[-1],-1,M)
    for j in range(p-1,0,-1):invf[j-1]=invf[j]*j%M
    H=[0]*p;Q=[0]*p
    for j in range(1,p):
        v=pow(j,-1,M);H[j]=(H[j-1]+v)%M;Q[j]=(Q[j-1]+v*v)%M
    e=pow(8,-1,M);half=pow(2,-1,M);out=[]
    for n in range(p):
        z=invf[n]**2%M
        if n<=k:
            b=f[a]*f[k]*invf[a-n]*invf[k-n]*z%M
            A=(H[a]-H[a-n])%M;B=(H[k]-H[k-n])%M
            A2=(Q[a]-Q[a-n])%M;B2=(Q[k]-Q[k-n])%M
            U=-(3*A+B)*e%M;V=(9*A2+B2)*e*e%M
            out.append(b*(1+p*U+p*p*(U*U-V)*half)%M)
        elif n<=a:
            b=(-1)**(n+k)*f[a]*f[k]*f[n-k-1]*invf[a-n]*z*e%M
            U=(-3*(H[a]-H[a-n])+H[n-k-1]-H[k])*e%M
            out.append(p*b*(1+p*U)%M)
        else:
            b=-3*f[a]*f[k]*f[n-a-1]*f[n-k-1]*z*e*e%M
            out.append(p*p*b%M)
    return out

def direct_b(p):
    M=p**3;b=[1]
    for n in range(p-1):
        b.append(b[-1]*(4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)*pow(256*(n+1)**4,-1,M)%M)
    return b

def cauchy(g,p):
    k=(p-3)//8;a=3*k+1;M=p**3;out=[]
    for n in range(p):
        s=0
        for i in range(n+1):
            j=n-i
            vi=0 if i<=k else (1 if i<=a else 2)
            vj=0 if j<=k else (1 if j<=a else 2)
            if vi+vj<3:s+=g[i]*g[j]
        out.append(s%M)
    return out

def check():
    ps=[11,19,43,59,67,83,107,139,163,179,211,227,251,283,307,331,379,419,443,467,491]
    for p in ps:
        assert p%8==3 and all(p%d for d in range(2,int(p**.5)+1))
        g=lift_g(p);assert g==direct_g(p),(p,"Gauss")
        k=(p-3)//8;a=3*k+1;M=p**3
        assert all(g[n]%p for n in range(k+1))
        assert all(g[n]%p==0 and g[n]%(p*p) for n in range(k+1,a+1))
        assert all(g[n]%(p*p)==0 and g[n]%M for n in range(a+1,p))
        assert cauchy(g,p)==direct_b(p),(p,"Cauchy")
    print("PASS",len(ps),"p^3 Gauss, valuations and full finite Clausen")

if __name__=="__main__":check()
