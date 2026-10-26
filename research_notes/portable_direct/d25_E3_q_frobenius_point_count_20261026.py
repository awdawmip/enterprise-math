#!/usr/bin/env python3
"""Exact E_3(t) Frobenius-q point count, not the native H0/B0 [X]U test.

Original curve (Chisholm et al., Sec. 2):
  y^2 + x*y + (t/27)*y = x^3, t=(2-T)/4, T^2=2 in F_(p^2).
"""
def model(p):
    assert p > 3 and p % 24 in (13, 19)
    assert pow(2, (p-1)//2, p) == p-1
    i4=pow(4,-1,p); i27=pow(27,-1,p)
    t=(2*i4%p,-i4%p)
    c=(t[0]*i27%p,t[1]*i27%p)
    return t,c

def mul(x,y,p):
    return ((x[0]*y[0]+2*x[1]*y[1])%p,
            (x[0]*y[1]+x[1]*y[0])%p)

def add(x,y,p):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)

def norm_count(p):
    t,c=model(p);q=p*p
    leg=[0]*p
    for z in range(1,p):
        leg[z] = 1 if pow(z,(p-1)//2,p)==1 else -1
    s=0
    for a in range(p):
        for b in range(p):
            u=(a+c[0])%p;v=(b+c[1])%p
            re=(u*u+2*v*v+4*(a*a*a+6*a*b*b))%p
            im=(2*u*v+4*(3*a*a*b+2*b*b*b))%p
            s += leg[(re*re-2*im*im)%p]
    return {"p":p,"t":t,"q":q,"character_sum":s,"points":q+1+s,
            "frobenius_trace":-s}

def power(x,n,p):
    r=(1,0)
    while n:
        if n&1:r=mul(r,x,p)
        x=mul(x,x,p);n//=2
    return r

def independent_euler_count(p):
    """Full finite-field exponentiation, independent of norm/Legendre table."""
    _,c=model(p);q=p*p;s=0
    for a in range(p):
        for b in range(p):
            x=(a,b)
            v=add(x,c,p)
            x3=mul(mul(x,x,p),x,p)
            v2=mul(v,v,p)
            d=add(v2,(4*x3[0]%p,4*x3[1]%p),p)
            if d==(0,0):continue
            sign=power(d,(q-1)//2,p)
            if sign==(1,0):s+=1
            elif sign==(p-1,0):s-=1
            else:raise AssertionError((p,x,sign))
    return q+1+s

def brute_y_count(p):
    """Independently count solutions (x,y) for small primes."""
    assert p in (13,19)
    _,c=model(p)
    ff=[(a,b) for a in range(p) for b in range(p)]
    total=1
    for x in ff:
        x3=mul(mul(x,x,p),x,p)
        L=add(x,c,p)
        for y in ff:
            if add(mul(y,y,p),mul(L,y,p),p)==x3:total+=1
    return total

def main():
    for p in (13,19,373):
        r=norm_count(p)
        other=brute_y_count(p) if p<100 else independent_euler_count(p)
        assert r["points"] == other == (p-1)**2, (r,other)
        assert r["frobenius_trace"] == 2*p
        print("PASS",r,"independent_points",other)
    print("H0/B0 [X]U = NOT_EXECUTED; D25/LIFT = OPEN")

if __name__=="__main__":main()
