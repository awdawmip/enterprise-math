"""Exact all-prime complementary valuation/leading-unit laws for W216 and V2304."""
from math import comb, factorial
P=[5,7,11,13,17,19,23,29,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373]
def raw(n,p,s,k):
    mod=p**k
    if s=='W': val=comb(2*n,n)**2*comb(3*n,n); den=216
    else: val=comb(4*n,2*n)*comb(2*n,n)**2; den=2304
    return val*pow(den,-n,mod)%mod
def unit(n,p,s,v):
    z=raw(n,p,s,v+1)
    assert z%p**v==0
    out=z//p**v
    assert out%p !=0
    return out
ans=[]
for p in P:
    count=0
    for q in range(1,p):
        i=2*q//p;j=3*q//p;k=4*q//p
        w=i+j;v=k
        assert w + ((2*(p-q))//p+(3*(p-q))//p)==3
        assert v+4*(p-q)//p==3
        expect_W=(-1)**(w+1)*factorial(j)*factorial(2-j)*pow(36*q**3,-1,p)%p
        expect_V=(-1)**(k+1)*factorial(k)*factorial(3-k)*pow(576*q**3,-1,p)%p
        actual_W=unit(q,p,'W',w)*unit(p-q,p,'W',3-w)%p
        actual_V=unit(q,p,'V',v)*unit(p-q,p,'V',3-v)%p
        assert actual_W==expect_W,('W',p,q,w,actual_W,expect_W)
        assert actual_V==expect_V,('V',p,q,v,actual_V,expect_V)
        count+=1
    ans.append((p,count))
print('primes',len(P),'checked q for both models',sum(n for _,n in ans),'total comparisons',2*sum(n for _,n in ans))
print(ans)
