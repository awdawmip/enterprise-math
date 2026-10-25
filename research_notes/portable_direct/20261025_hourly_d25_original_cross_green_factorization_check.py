#!/usr/bin/env python3
"""Author's independent modular source/jet point check for D25 original-Jacobi cross-Green."""
def prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))

def zhalf(c,q):
    z=pow(2,-1,q);power=1;v=d=d2=theta=0
    for n,a in enumerate(c):
        t=a*power%q;v=(v+t)%q;theta=(theta+n*t)%q;d2=(d2+n*(n-1)*t)%q
        power=power*z%q
    return v,2*theta%q,4*d2%q,theta

def check(p):
    m,N=(p-1)//6,p-1;q=p**3
    jets=[[1,0,0]];original=[1]
    for n in range(N):
        a,b=(n-m)*(n-2*m),-(3*n-4*m)
        inv=pow((n+1)**2,-1,q);old=jets[-1]
        jets.append([(a*old[k]+(b*old[k-1] if k>=1 else 0)
            +(2*old[k-2] if k>=2 else 0))*inv%q for k in range(3)])
        original.append(original[-1]*(6*n+1)*(3*n+1)*pow(18*(n+1)**2,-1,q)%q)
    u=[r[0] for r in jets];v=[r[1] for r in jets];y=[2*r[2]%q for r in jets]
    h=p*pow(6,-1,q)%q
    assert all(original[n]==(u[n]-h*v[n]+h*h*pow(2,-1,q)*y[n])%q for n in range(p)),p
    U,Up,Upp,Ut=zhalf(u,q);S,Sp,Spp,St=zhalf(original,q)
    V,Vp,_,_=zhalf(v,q);Y,Yp,_,_=zhalf(y,q)
    W=(U*Sp-S*Up)%q;Wp=(U*Spp-S*Upp)%q
    C=(6*p-5)*(3*p-2)*pow(18,-1,q)*original[-1]%q
    rhs=U*(h*(3*St-4*m*S+2*h*S)-C*pow(2,-(p-1),q))%q
    lhs=(pow(4,-1,q)*Wp+(1+(3*m-1)*pow(2,-1,q))*W)%q
    assert lhs==rhs,(p,"exact Green point equation")
    assert W%p==0
    normalized=(-pow(6,-1,p*p)*(U*Vp-V*Up)+p*pow(72,-1,p*p)*(U*Yp-Y*Up))%(p*p)
    assert W//p%(p*p)==normalized,(p,"second digit W/p")
    if p%24 in (13,19):
        assert U%p==0 and S%p==0
        assert lhs%(p*p)==0 and ((Wp+W)//p)%p==0
        assert W//p%p==V*Up*pow(6,-1,p)%p
    return (p,W//p%p,lhs%(p*p))
if __name__=="__main__":
    cases=[check(p) for p in range(7,374) if p%6==1 and prime(p)]
    print("POINT_GREEN_P3_PASS",len(cases))
    print("TARGET_WITNESSES",[r for r in cases if r[0] in (13,19,37,43,373)])
