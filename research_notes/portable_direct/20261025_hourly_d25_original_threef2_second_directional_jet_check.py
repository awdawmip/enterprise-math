#!/usr/bin/env python3
"""Independent p³ original 3F2 directional double jet and Clausen harmonic check."""
def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
def mul(a,b,q):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%q
    return out
def check(p):
    assert p%6==1 and prime(p)
    m=(p-1)//6; q=p**3
    i2=pow(2,-1,q);i3=pow(3,-1,q)
    A=[1];T=[1];D=[0];E=[0]
    for n in range(p-1):
        A.append(A[-1]*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*(n+1)**3,-1,q)%q)
        x=n-2*m; y=n-4*m; z=n-3*m
        a0=x*y*z%q
        a1=(i3*y*z+2*i3*x*z+i2*x*y)%q
        a2=((i3*2*i3)*z+(i3*i2)*y+(2*i3*i2)*x)%q
        d1=(n+1-p*i2)%q;d2=(n+1-p)%q
        b0=d1*d2*(n+1)%q
        b1=(i2*d2+d1)*(n+1)%q
        b2=i2*(n+1)%q
        inv=pow(b0,-1,q)
        r0=a0*inv%q
        r1=(a1-r0*b1)*inv%q
        r2=(a2-r0*b2-r1*b1)*inv%q
        T.append(T[-1]*r0%q)
        D.append((D[-1]*r0+T[-2]*r1)%q)
        E.append((E[-1]*r0+D[-2]*r1+T[-2]*r2)%q)
    assert all((a-t-p*d-p*p*e)%q==0 for a,t,d,e in zip(A,T,D,E)),(p,'p³ source translation')
    assert all(T[n]==0 for n in range(2*m+1,p))
    assert all(D[n]==0 for n in range(3*m+1,p))
    assert all(E[n]==0 for n in range(4*m+1,p))
    assert all(E[n]%p!=0 for n in range(3*m+1,4*m+1)),(p,'two zeros')
    U=[1];H=[0];J=[0];hn=0;h2=0
    for n in range(m):
        U.append(U[-1]*(n-m)*(n-2*m)*pow((n+1)**2,-1,q)%q)
        hn=(hn+pow(n+1,-1,q))%q; h2=(h2+pow((n+1)**2,-1,q))%q
        H.append(U[-1]*hn%q);J.append(U[-1]*(hn*hn+h2)%q)
    if p<=1327:
        U2=mul(U,U,q);UH=mul(U,H,q);H2=mul(H,H,q);UJ=mul(U,J,q)
        predicted=[(U2[n]+p*UH[n]+p*p*i2*i2*(H2[n]+UJ[n]))%q for n in range(2*m+1)]
        assert T[:2*m+1]==predicted,(p,'Clausen p³')
        def obs(a):
            v=0;pw=1;zz=pow(2,-1,q)
            for n,an in enumerate(a):
                v=(v+pw*an*(6*n+1))%q;pw=pw*zz%q
            return v
        rhs=(obs(U2)+p*(obs(UH)+obs(D))+p*p*(i2*i2*(obs(H2)+obs(UJ))+obs(E)))%q
        assert obs(A)==rhs,(p,'original signed observer')
    w=sum(an*(6*n+1)*pow(2,-n,q) for n,an in enumerate(A))%q
    return p,w,E[4*m]%p
if __name__=='__main__':
    cases=[check(p) for p in range(7,374) if p%6==1 and prime(p)]
    cases += [check(1327),check(19963)]
    print('SECOND_DIRECTIONAL_JET_P3_PASS',len(cases))
    print('WITNESSES',[x for x in cases if x[0] in (13,19,37,43,373,1327,19963)])
