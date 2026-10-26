"""Exact author check: Ward cokernel witness and 733-adic observer lift."""
from math import comb

def coeff(p):
    M=(p-1)//3-1
    c=[1]
    for t in range(1,M+1):
        c.append(c[-1]*(2*t-1)*pow(2*t,-1,p)%p)
        assert c[-1]==comb(2*t,t)*pow(4,-t,p)%p
    return c

def residue(p,c,kind):
    return sum(c[t]*pow(2,-t,p)*({'geo':1,'rank':-t,'signed':1+6*t}[kind])
               for t in range(len(c)))%p

def xi_left(p,z,q):
    M=(p-1)//3-1
    nu=0
    for n in range(-M,0):
        nu=(pow(z,n,q)+(p-2*n+1)*nu)*pow(p-2*n,-1,q)%q
    return (1+(p+1)*nu)%q

def xi_product(p,z,q):
    M=(p-1)//3-1
    A=pow(p+2,-1,q); power=1; zin=pow(z,-1,q);total=0
    for t in range(1,M+1):
        if t>1: A=A*(p+2*t-1)*pow(p+2*t,-1,q)%q
        power=power*zin%q
        total=(total+power*A)%q
    return (1+(p+1)*total)%q

def verify():
    ps=[p for p in range(7,998) if p%6==1 and
        all(p%d for d in range(2,int(p**.5)+1))]
    assert len(ps)==80
    zeros=[]
    for p in ps:
        M=(p-1)//3-1;c=coeff(p)
        v={n:0 for n in range(-M,M+2)}
        v[0]=1
        for t in range(1,M+1):v[-t]=c[t]
        assert all(((p-2*n)*v[n]-(p-2*n-1)*v[n+1])%p==0
                   for n in range(-M,M+1))
        g=residue(p,c,'geo');d=residue(p,c,'rank');s=residue(p,c,'signed')
        assert s==(g-6*d)%p
        assert [g,0,0,0,0,0]==[(a*g)%p for a in
             [1,-p,-p,p*p,p*p,p*p]]
        if g==0:zeros.append(p)
        if p==13:assert (g,d,s)==(9,3,4)
        if p==733:assert (g,d,s)==(0,211,200)
    assert zeros==[733]  # finite sample only
    p=733;q2=p*p;q3=p**3
    c=coeff(p)
    deriv=residue(p,c,'rank')*pow(2,-1,p)%p
    assert deriv==472
    b=xi_left(p,2,q3)
    assert b==xi_product(p,2,q3)==137318021
    h1=(-(b//p)*pow(deriv,-1,p))%p
    z1=2+p*h1
    assert (h1,z1)==(729,534359)
    t=xi_left(p,z1,q3)
    assert t==xi_product(p,z1,q3)==356222607
    assert t%q2==0
    h2=(-(t//q2)*pow(deriv,-1,p))%p
    z2=z1+q2*h2
    assert (h2,z2)==(289,155810880)
    assert xi_left(p,z2,q3)==xi_product(p,z2,q3)==0
    print('PASS: 80 primes, kernel witnesses; p13=(9,3,4), p733=(0,211,200)')
    print('PASS: Xi733(2)=137318021; derivative=472; Hensel z=155810880 mod 733^3')

if __name__=='__main__':verify()
