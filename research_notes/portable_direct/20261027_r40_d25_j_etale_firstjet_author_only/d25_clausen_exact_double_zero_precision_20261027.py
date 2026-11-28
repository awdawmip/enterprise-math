"""Author-only exact finite Clausen sharp-double-zero/Legendre/signed valuation checker.
No native H0/B0 execution; pure Python stdlib F_p and Z/p^7 arithmetic.
"""
from math import comb

PS=[7,13,19,31,37,43,61,67,73,79,103,109,211,373,997,1213]
ROOT_PS=[13,19,37,43,373,997]
def coeff(r,m):
    return [comb(r,k)*comb(2*r,k)*pow(2,-k,m)%m for k in range(r+1)]
def deriv(a,m):
    return [i*a[i]%m for i in range(1,len(a))] or [0]
def val(a,x,m):
    v=0
    for b in a[::-1]: v=(v*x+b)%m
    return v
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def mul(a,b,p):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
    return trim(z)
def rem(a,b,p):
    a=trim(a[:]);b=trim(b[:])
    while len(a)>=len(b) and a!=[0]:
        t=len(a)-len(b); c=a[-1]*pow(b[-1],-1,p)%p
        for i,z in enumerate(b):a[i+t]=(a[i+t]-c*z)%p
        trim(a)
    return a
def gcd_deg(a,b,p):
    while b!=[0]:a,b=b,rem(a,b,p)
    return len(a)-1
def legendre_even(p,r):
    old=[1]; cur=[0,1]
    for n in range(1,2*r):
        xx=[0]+cur; N=max(len(xx),len(old))
        nxt=[((2*n+1)*(xx[i] if i<len(xx) else 0)
             -n*(old[i] if i<len(old) else 0))*pow(n+1,-1,p)%p
             for i in range(N)]
        old,cur=cur,trim(nxt)
    assert all(cur[i]==0 for i in range(1,len(cur),2))
    return cur[::2]
def substitute(poly,p):
    a=[0]; half=pow(2,-1,p)
    for c in reversed(poly):
        b=[0]*(len(a)+1)
        for i,x in enumerate(a):
            b[i]=(b[i]+x)%p;b[i+1]=(b[i+1]-half*x)%p
        b[0]=(b[0]+c)%p;a=trim(b)
    return a
def hyper_c(p,r):
    z=[1]
    for k in range(1,2*r+1):
        num=(3*k)*(3*k-1)*(3*k-2)*(2*k)*(2*k-1)
        z.append(z[-1]*num*pow(216*k**5,-1,p)%p)
    return z
def vp(x,p):
    if x==0:return None
    n=0
    while x%p==0:n+=1;x//=p
    return n
def hensel(a,p,m):
    x=1; q=p; da=deriv(a,m)
    while q<m:
        assert val(a,x,m)%q==0
        v=val(a,x,q*p)//q
        d=val(da,x,p)
        x+=q*(-v*pow(d,-1,p)%p);q*=p
    assert val(a,x,m)==0
    return x
def check(p):
    r=(p-1)//6;a=coeff(r,p);d=deriv(a,p);dd=deriv(d,p)
    assert len(a)==r+1 and a[0]==1 and a[-1]!=0
    assert val(a,2,p)==comb(3*r,r)%p!=0
    assert gcd_deg(a,d,p)==0
    assert mul(a,a,p)==hyper_c(p,r)
    assert substitute(legendre_even(p,r),p)==a
    inv2=pow(2,-1,p)
    for k in range(r+1):
        ddk1=dd[k-1] if 1<=k<=len(dd) else 0
        ddk2=dd[k-2] if 2<=k<=len(dd)+1 else 0
        dk=d[k] if k<len(d) else 0
        dk1=d[k-1] if 1<=k<=len(d) else 0
        assert (2*ddk1-ddk2+2*dk-3*inv2*dk1-2*r*r*a[k])%p==0
    A1=val(a,1,p)
    row={'p':p,'A1':A1,'gcd_degree':0,'Legendre':True,'Clausen':True}
    if A1==0:
        d1=val(d,1,p);d2=val(dd,1,p)
        assert d1!=0 and (2*d2+d1)%p==0
        row.update(Aprime1=d1,Csecond1=2*d1*d1%p)
    if p in ROOT_PS:
        assert A1==0
        modulus=p**7;A=coeff(r,modulus)
        root=hensel(A,p,modulus); unit=val(deriv(A,modulus),root,p)
        vals=[]
        for n in (1,2):
            dp=p**n; ap=val(A,root+dp,modulus);am=val(A,root-dp,modulus)
            cp=ap*ap%modulus; cm=am*am%modulus; diff=(cp-cm)%modulus
            assert vp(cp,p)==2*n and vp(cm,p)==2*n and vp(diff,p)==3*n
            residue=(diff//p**(3*n))%p
            assert residue==(-unit*unit)%p
            vals.append([n,2*n,3*n,residue])
        row.update(root_mod_p7=root,unit=unit, valuations=vals)
    return row
if __name__=='__main__':
    import json
    rs=[check(p) for p in PS]
    print(json.dumps({'status':'PASS','test_kind':'AUTHOR_EXACT_AUXILIARY',
      'prime_count':len(rs),'hensel_primes':ROOT_PS,'results':rs},indent=2))
