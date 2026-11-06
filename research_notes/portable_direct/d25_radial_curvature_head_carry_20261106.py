#!/usr/bin/env python3
"""Exact D25 radial second jet: independent modular harmonic and polynomial checks."""
from math import comb

def inverses(p):
    z = [0]*p
    z[1] = 1
    for n in range(2,p):
        z[n] = (-(p//n)*z[p%n]) % p
    return z

def certificate(p):
    assert p >= 7 and p % 6 == 1
    m=(p-1)//6; a,b,c=2*m,3*m,4*m
    inv=inverses(p); half=inv[2]; neg_half=(-half)%p
    h=[0]*p; h2=[0]*p
    for n in range(1,p):
        h[n]=(h[n-1]+inv[n])%p
        h2[n]=(h2[n-1]+inv[n]*inv[n])%p
    head=tail=0
    for j in range(b+1):
        w=(6*j+1)*pow(neg_half,j,p)%p
        if j<=a:
            u=comb(a,j)*comb(b,j)*comb(c,j)%p
            L=(h[a]-h[a-j]+h[c]-h[c-j])%p
            R=(h2[a]-h2[a-j]+h2[c]-h2[c-j])%p
            head=(head+w*u*(L*L-R)*half)%p
        else:
            # Coefficient z of C(a+z,j), with j<p
            E=pow((-1)**(j-a-1)*j*comb(j-1,a),-1,p)
            M=(h[a]-h[j-a-1]+h[c]-h[c-j])%p
            tail=(tail+w*comb(b,j)*comb(c,j)*E*M)%p

    # Independent truncated degree-2 binomial polynomial recurrence
    u=[1,0,0]; v=[1,0,0]
    middle=power=1; poly=tangent=0
    for j in range(b+1):
        w=(6*j+1)*middle*power%p
        poly=(poly+w*(u[0]*v[2]+u[1]*v[1]+u[2]*v[0]))%p
        tangent=(tangent+w*(u[1]*v[0]+u[0]*v[1]))%p
        if j==b: break
        def step(t,n):
            return [((n-j)*t[k]+(t[k-1] if k else 0))*inv[j+1]%p for k in range(3)]
        u=step(u,a); v=step(v,c)
        middle=middle*(b-j)*inv[j+1]%p
        power=power*neg_half%p
    assert (head+tail)%p==poly, (p,head,tail,poly)
    return p,head,tail,poly,tangent

if __name__=="__main__":
    expected={
       7:(0,3,3),13:(3,2,5),19:(7,3,10),
       109:(56,76,23),211:(69,62,131),229:(151,140,62),
       373:(158,282,67),1093:(309,452,761),
       3511:(2533,2735,1757),5113:(3519,1594,0)
    }
    for p, want in expected.items():
        actual=certificate(p)
        assert actual[1:4]==want, (actual,want)
        assert actual[4]==0, actual
        print(f"p={p} head={actual[1]} tail={actual[2]} c={actual[3]} tangent={actual[4]} PASS")
