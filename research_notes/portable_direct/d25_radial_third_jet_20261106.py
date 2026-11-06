#!/usr/bin/env python3
"""Exact 3rd-order labelled-source jet; pure modular arithmetic (no float)."""
from math import comb

def invtable(p):
    inv=[0]*p
    inv[1]=1
    for n in range(2,p): inv[n]=-(p//n)*inv[p%n]%p
    return inv

def degree3(p):
    assert p>3 and p%6==1
    m=(p-1)//6; a,b,c=2*m,3*m,4*m
    inv=invtable(p)
    u=[1,0,0,0]; v=[1,0,0,0]
    Cbj=1; power=1; direct=[0,0,0,0]
    invneg2=(-inv[2])%p
    for j in range(b+1):
        w=((6*j+1)*Cbj*power)%p
        for k in range(4):
            direct[k]=(direct[k]+w*sum(u[q]*v[k-q] for q in range(k+1)))%p
        if j==b: break
        def step(t,n):
            return [((n-j)*t[k]+(t[k-1] if k else 0))*inv[j+1]%p for k in range(4)]
        u=step(u,a); v=step(v,c)
        Cbj=Cbj*(b-j)*inv[j+1]%p
        power=power*invneg2%p
    head=tail=0
    u0=v0=cb=power=1
    for j in range(b+1):
        weight=(6*j+1)*cb*power%p
        if j<=a:
            ls=[inv[a-t] for t in range(j)]+[inv[c-t] for t in range(j)]
            e1=e2=e3=0
            for t in ls:
                e3=(e3+t*e2)%p
                e2=(e2+t*e1)%p
                e1=(e1+t)%p
            head=(head+weight*u0*v0*e3)%p
        else:
            E=(-1)**(j-a-1)*pow(j*comb(j-1,a),-1,p)%p
            ls=[pow(a-t,-1,p) for t in range(j) if t!=a]+[inv[c-t] for t in range(j)]
            e1=e2=0
            for t in ls:
                e2=(e2+t*e1)%p; e1=(e1+t)%p
            tail=(tail+weight*E*v0*e2)%p
        if j==b:break
        if j<a: u0=u0*(a-j)*inv[j+1]%p
        else:u0=0
        v0=v0*(c-j)*inv[j+1]%p
        cb=cb*(b-j)*inv[j+1]%p
        power=power*invneg2%p
    assert direct[3]==(head+tail)%p,(p,direct,head,tail)
    return {"p":p,"m":m,"jet":direct,"cubic_head":head,"cubic_carry":tail}

if __name__=="__main__":
    for p in [7,13,19,109,211,229,373,1093,3511,5113]:
        print(degree3(p))
    assert degree3(5113)=={"p":5113,"m":852,"jet":[0,0,0,3783],"cubic_head":4774,"cubic_carry":4122}
    print("TEN PRIME CHECKS PASS")
