"""Exact F_p verification: D25 weighted 216/2304 first and second jets."""
from math import comb
def primes_under(n):
    for p in range(5,n):
        if all(p%d for d in range(2,int(p**0.5)+1)): yield p
def ev(cs,x,p):
    return tuple(sum((1 if r==0 else i if r==1 else i*(i-1))*c*pow(x,i-r,p)
                     for i,c in enumerate(cs) if i>=r)%p for r in (0,1,2))
def hg(p,kind):
    cs=[1]
    for j in range(p-1):
        if kind=="A":
            num=(2*j+1)*(3*j+1)*(3*j+2); den=18*(j+1)**3
        else:
            num=(4*j+1)*(2*j+1)*(4*j+3); den=32*(j+1)**3
        cs.append(cs[-1]*(num%p)*pow(den,-1,p)%p)
    return cs
def square(h):
    q=[0]*(len(h)*2-1)
    for i,x in enumerate(h):
        for j,y in enumerate(h):q[i+j]+=x*y
    return q
def test():
    n13=n19=0
    for p in primes_under(1200):
        if p%24 not in (13,19):continue
        m=(p-1)//6; f=[comb(m,i)*comb(2*m,i)%p for i in range(m+1)]
        a=hg(p,"A"); zz=pow(2,-1,p)
        assert [x%p for x in square(f)]+[0]*(p-2*m-1)==a
        fv,fd,_=ev(f,zz,p)
        assert fv==0 and fd!=0
        av,ad,add=ev([(6*i+1)*c%p for i,c in enumerate(a)],zz,p)
        assert av==0 and ad==6*fd*fd%p and add==8*fd*fd%p
        if p%24==19:n19+=1;continue
        n13+=1
        k=(p-5)//8; h=[comb(3*k+1,i)*comb(k,i)%p for i in range(k+1)]
        sh=square(h); rhs=[0]*p
        for i,x in enumerate(sh):
            rhs[i]=(rhs[i]+x)%p;rhs[i+1]=(rhs[i+1]-x)%p
        b=hg(p,"B");assert rhs==b
        w=pow(9,-1,p);hv,hd,hdd=ev(h,w,p)
        assert hv==0 and hd!=0 and (16*hdd+117*hd)%p==0
        bv,bd,bdd=ev([(8*i+1)*c%p for i,c in enumerate(b)],w,p)
        assert bv==0 and bd==128*pow(81,-1,p)*hd*hd%p
        assert bdd==(-88*pow(9,-1,p)*hd*hd)%p
        assert bdd*pow(bd,-1,p)%p==(-99*pow(16,-1,p))%p
        diff=(add*pow(ad,-1,p)-(2*pow(9,-1,p))*bdd*pow(bd,-1,p))%p
        assert diff==65*pow(24,-1,p)%p and ((diff==0)==(p==13))
    print("PASS: exact 3F2 square/fold and two-jet checks; p<1200; class counts",n13,n19)
if __name__=="__main__":test()
