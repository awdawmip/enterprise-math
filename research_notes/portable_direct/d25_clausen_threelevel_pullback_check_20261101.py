"""Author-only exact p-adic source checker; not the native H0/B0 experiment."""
from fractions import Fraction

def primes(limit):
    b=bytearray(b'\x01')*(limit+1); b[0]=b[1]=0
    for i in range(2,int(limit**0.5)+1):
        if b[i]:
            b[i*i::i]=b'\x00'*len(b[i*i::i])
    return [p for p in range(7,limit+1) if b[p] and p%6==1]

def vp(x,p,k=5):
    if not x: return k
    t=0
    while t<k and x%p==0:
        x//=p; t+=1
    return t

def check(p):
    r=(p-1)//6; s=(p-1)//3; m=p**5
    u=[1]
    for n in range(1,p):
        u.append(u[-1]*(6*n-5)*(3*n-2)*pow(18*n*n,-1,m)%m)
        assert vp(u[n],p)==(n>r)+(n>s)
    k=[0]*(2*p)
    for n in range(p,2*p-1):
        k[n]=sum(u[i]*u[n-i] for i in range(n-p+1,p))%m
        d=2 if n<p+r else 3 if n<p+s else 4
        assert k[n]%p**d==0,('K',p,n)
    assert u[-1]//p**2%p==pow(10,-1,p)
    assert k[p+r-1]//p**2%p==u[r]*pow(5,-1,p)%p
    assert k[p+s-1]//p**3%p==(u[s]//p)*pow(5,-1,p)%p
    assert k[2*p-2]//p**4%p==pow(100,-1,p)
    e=-(6*p-5)*(3*p-2)*pow(18,-1,m)*u[-1]%m
    assert vp(e,p)==2 and e//p**2%p==-pow(18,-1,p)%p
    count=[0,0,0]
    for j in range(1,p):
        n=p+j
        L=(n**3*k[n]-(2*n-1)*(3*n-1)*(3*n-2)*pow(18,-1,m)*k[n-1])%m
        R=2*e*(p+3*j)*u[j]%m
        assert L==R,('source',p,j)
        d=2+(j>r)+(j>s)
        assert vp(L,p)==d,('level',p,j)
        assert L//p**d%p==(-j*pow(3,-1,p)*(u[j]//p**(d-2)))%p
        count[d-2]+=1
    return p, k[p+r-1]//p**2%p, k[p+s-1]//p**3%p, k[2*p-2]//p**4%p, count

def fraction_endpoints():
    for p in (7,13,19):
        r=(p-1)//6; s=(p-1)//3
        u=[Fraction(1)]
        for n in range(1,p):
            u.append(u[-1]*Fraction((6*n-5)*(3*n-2),18*n*n))
        for n,d,goal in ((p+r-1,2,u[r]/5),(p+s-1,3,u[s]/(5*p)),(2*p-2,4,Fraction(1,100))):
            v=sum((u[i]*u[n-i] for i in range(n-p+1,p)),Fraction(0))/p**d
            assert v.numerator*pow(v.denominator,-1,p)%p==goal.numerator*pow(goal.denominator,-1,p)%p

def main():
    fraction_endpoints()
    assert all(Fraction(1,4) not in {e*Fraction(1,d) for d in (2,6,1)} for e in range(1,100))
    assert all(Fraction(1,6) not in {e*Fraction(1,d) for d in (2,4,1)} for e in range(1,100))
    rows=[check(p) for p in primes(997)]
    for v in rows:
        if v[0] in (13,19,37,373): print('CERT',v)
    print('PASS',len(rows),'primes p<=997; full high cutoff mod p^5; exact rational endpoints')

if __name__=='__main__': main()
