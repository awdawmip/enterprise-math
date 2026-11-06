"""Exact mod p^4 integer certificate for p5113 three-digit outer fibre.
Chosen integer lifts of original source vector v are explicitly retained.
"""
from math import isqrt

def full_sum_mod_p4(p, vv):
    n=p**4; m=(p-1)//6; s=(2*m,3*m,4*m)
    inv=[0]+[pow(j,-1,n) for j in range(1,p)]
    coeff=[1,1,1]; ph=1; ans=0; minus_half=pow(-2,-1,n)
    for j in range(p):
        ans=(ans+(6*j+1)*ph*coeff[0]*coeff[1]*coeff[2])%n
        if j<p-1:
            for k in range(3):
                coeff[k]=coeff[k]*(s[k]+p*vv[k]-j)*inv[j+1]%n
            ph=ph*minus_half%n
    return ans

p=5113
assert all(p%i for i in range(2,isqrt(p)+1))
v=(-pow(3,-1,p))%p,(-pow(2,-1,p))%p,(-2*pow(3,-1,p))%p
n=p**4
base=full_sum_mod_p4(p,v)
cache={0:base}
for lam in (1,-1,2,3,5,17,53):
    v2=(v[0]+lam,v[1],v[2]+lam)
    cache[lam]=full_sum_mod_p4(p,v2)
    assert (cache[lam]-base)%n%(p*p)==0
u=(cache[1]-base)%n//(p*p)
vminus=(cache[-1]-base)%n//(p*p)
w=(cache[2]-base)%n//(p*p)
mod=p*p
inv2=pow(2,-1,mod);inv6=pow(6,-1,mod)
B=(u+vminus)*inv2%mod
s=(u-vminus)*inv2%mod
C=(w-2*s-4*B)*inv6%mod
A=(s-C)%mod
assert A%p==3118 and B%p==0 and C%p==0
assert C//p==3783,(C,C//p)
for lam in cache:
    q=(cache[lam]-base)%n//(p*p)
    assert q==(A*lam+B*lam**2+C*lam**3)%mod,(lam,q)
print('p',p,'v_lift',v,'p4',n,'base_p4',base)
print('Q(lambda)=[F(p(v+lambda*d))-F(pv)]/p^2 modulo p^2')
print('A',A,'B',B,'C',C,'B/p',B//p,'C/p',C//p)
print('matches 8 integer-lift samples (0,+/-1,2,3,5,17,53)')
for lam in cache:
 print('lambda',lam,'full_sum',cache[lam],'q',(cache[lam]-base)%n//(p*p))

# Independent coefficient-domain calculation: no interpolation from lambda samples.
def coefficient_sum(p, vv):
    n=p**4;m=(p-1)//6; s=(2*m,3*m,4*m)
    inv=[0]+[pow(j,-1,n) for j in range(1,p)]
    vectors=[[1,0,0,0] for _ in range(3)]
    ans=[0,0,0,0]
    phase=1;mh=pow(-2,-1,n)
    def mul(a,b):
        return [sum(a[k]*b[r-k] for k in range(r+1))%n for r in range(4)]
    for j in range(p):
        prod=mul(mul(vectors[0],vectors[1]),vectors[2])
        for r in range(4):ans[r]=(ans[r]+(6*j+1)*phase*prod[r])%n
        if j<p-1:
            for i in range(3):
                u=(s[i]+p*vv[i]-j)%n
                e=(p if i!=1 else 0)
                old=vectors[i]
                vectors[i]=[(u*old[r]+(e*old[r-1] if r else 0))*inv[j+1]%n for r in range(4)]
            phase=phase*mh%n
    return ans

poly=coefficient_sum(p,v)
assert poly[0]==base
assert [c//(p*p) for c in poly[1:]] == [A,B,C]
assert all(c%(p*p)==0 for c in poly[1:])
print('independent_coefficient_form',poly,'PASS')
