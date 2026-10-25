#!/usr/bin/env python3
"""Exact original 3F2 / resonant Clausen first directional jet author checks."""
def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))
def point(c,q,weighted=False):
    v=0;z=1;half=pow(2,-1,q)
    for n,a in enumerate(c):
        v=(v+z*a*(6*n+1 if weighted else 1))%q
        z=z*half%q
    return v
def check(p):
    assert prime(p) and p%6==1
    m=(p-1)//6;q=p*p
    iv2=pow(2,-1,q);iv3=pow(3,-1,q)
    acoeff=[1];tcoeff=[1];dcoeff=[0]
    for n in range(p-1):
        acoeff.append(acoeff[-1]*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*(n+1)**3,-1,q)%q)
        a=(n-2*m)*(n-4*m)*(n-3*m)%q
        d1=(n+1-p*iv2)%q;d2=(n+1-p)%q
        den=d1*d2*(n+1)%q
        ap=(iv3*(n-4*m)*(n-3*m)+2*iv3*(n-2*m)*(n-3*m)+iv2*(n-2*m)*(n-4*m))%q
        dp=(iv2*d2*(n+1)+d1*(n+1))%q
        f=a*pow(den,-1,q)%q
        fp=(ap*den-a*dp)*pow(den,-2,q)%q
        tcoeff.append(tcoeff[-1]*f%q)
        dcoeff.append((dcoeff[-1]*f+tcoeff[-2]*fp)%p)
    assert all((a-t-p*d)%q==0 for a,t,d in zip(acoeff,tcoeff,dcoeff))
    assert all(tcoeff[n]==0 for n in range(2*m+1,p))
    assert all(dcoeff[n]==0 for n in range(3*m+1,p))
    assert all(dcoeff[n]!=0 for n in range(2*m+1,3*m+1))
    uw=[1];hh=[0];h=0
    for n in range(m):
        uw.append(uw[-1]*(n-m)*(n-2*m)*pow((n+1)**2,-1,q)%q)
        h=(h+pow(n+1,-1,p))%p
        hh.append(uw[-1]*h%p)
    def conv(x,y):
        res=[0]*(len(x)+len(y)-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y):res[i+j]=(res[i+j]+a*b)%q
        return res
    u2=conv(uw,uw);uh=conv(uw,hh)
    w=point(acoeff,q,True);wt=point(tcoeff,q,True);wd=point(dcoeff,q,True)
    direct=(point(u2,q,True)+p*(point(uh,q,True)+wd))%q
    assert w==(wt+p*wd)%q==direct,(p,'signed weighted source bridge')
    if p%24 in (13,19):
        assert point(uw,q)%p==0 and w==p%q,(p,'accepted first-digit check')
    return p,w,wt,wd,point(uw,q),point(u2,q,True),point(uh,q,True)
if __name__=='__main__':
    cases=[check(p) for p in range(7,374) if p%6==1 and prime(p)]
    cases += [check(1327),check(19963)]
    print('FULL_SOURCE_COEFFICIENTWISE_P2_PASS',len(cases))
    print('WITNESSES',[x for x in cases if x[0] in (13,19,37,43,373,1327,19963)])
