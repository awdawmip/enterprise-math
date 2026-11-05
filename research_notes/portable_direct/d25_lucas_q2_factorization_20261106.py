"""D25 2026-11-06: exact q² signed Lucas/two-moment verification.
Pure standard library; compares to original integer-binomial C_n.
Ordinary arithmetic only; native H0/B0 experiment NOT_RUN.
"""
from math import comb, factorial

def primes(limit):
    s=bytearray(b'\x01')*(limit+1)
    s[:2]=b'\x00\x00'
    for i in range(2,int(limit**0.5)+1):
        if s[i]:s[i*i:limit+1:i]=b'\x00'*((limit-i*i)//i+1)
    return [i for i in range(5,limit+1) if s[i]]

def original_shadow(n,m):
    a=-pow(2,-1,m)%m
    x=pow(2,2*n,m)
    val=0
    for k in range(2*n+1):
        val=(val+(6*k+1)*x*comb(2*n,k)*comb(3*n,k)*comb(4*n,k))%m
        x=x*a%m
    return val

def two_digit_certificate(n,q):
    assert n>=0 and q>=5 and all(q%d for d in range(2,int(q**0.5)+1))
    mod=q*q
    N,r=divmod(n,q)
    s=[i*r%q for i in (2,3,4)]
    M=[i*N+(i*r)//q for i in (2,3,4)]
    a=-pow(2,-1,mod)%mod
    phi=((pow(2,q-1,mod)-1)//q)%q
    h=[0]*q
    for j in range(1,q):h[j]=(h[j-1]+pow(j,-1,q))%q
    T=T1=0
    for ell in range(min(M)+1):
        v=pow(a,ell,mod)
        for m in M:v=v*comb(m,ell)%mod
        T=(T+v)%mod
        T1=(T1+ell*v)%mod
    L=Z=A=B=0
    for j in range(min(s)+1):
        u=pow(a,j,mod)
        for t in s:u=u*comb(t,j)%mod
        L=(L+(6*j+1)*u)%mod
        Z=(Z+u)%q
        for i in range(3):
            A=(A+(6*j+1)*u*M[i]*(h[s[i]]-h[s[i]-j]))%q
            B=(B+(6*j+1)*u*(h[s[i]-j]-h[j]))%q
    A=(A+2*N*phi*L)%q
    B=(B+6*Z-phi*L)%q
    K=[]
    for i in range(3):
        ki=0
        cap=min(s[t] for t in range(3) if t!=i)
        for j in range(s[i]+1,cap+1):
            d=j-s[i]
            tau=(-1)**(d+1)*factorial(s[i])*factorial(d-1)*pow(factorial(j),-1,q)%q
            z=(6*j+1)*pow(a,j,q)*tau%q
            for t in range(3):
                if t!=i:z=z*comb(s[t],j)%q
            ki=(ki+z)%q
        K.append(ki)
        A=(A+M[i]*ki)%q
        B=(B-ki)%q
    res=pow(2,2*(N+r),mod)*(L*T+q*(A*T+B*T1))%mod
    return dict(result=res,q=q,n=n,N=N,r=r,s=s,M=M,L=L,T=T,T1=T1,A=A,B=B,K=K,phi=phi)

def main():
    count=0
    for q in (5,7,11,13,17,19,23,29,31):
        for n in range(min(4*q+5,90)):
            x=two_digit_certificate(n,q)
            direct=original_shadow(n,q*q)
            assert direct==x['result'],(q,n,direct,x)
            if (6*n+1)%q==0:
                assert sum(bool(v) for v in x['K'])<=1
                if q%6==1:assert x['s'][0]<x['s'][1]<x['s'][2]
                else:assert x['s'][2]<x['s'][1]<x['s'][0]
            count+=1
    print('DIRECT_FULL_INTEGER_COMPARISON PASS',count)
    count=0
    for q in primes(41):
        n=(q*q-1)//6
        direct=original_shadow(n,q*q)
        cert=two_digit_certificate(n,q)
        assert direct==cert['result']==0,(q,direct,cert)
        count+=1
    print('DIRECT_PRIME_SQUARE_CHECK PASS',count)
    for q,n in ((5,9),(7,15),(13,2),(13,28),(19,3),(19,60),(37,80)):
        x=two_digit_certificate(n,q)
        print('WITNESS',q,n,'m',6*n+1,'C_mod_q2',x['result'],
              'L',x['L'],'T',x['T'],'T1',x['T1'],
              'A',x['A'],'B',x['B'],'K',x['K'])
    count=0
    for q in primes(1000):
        n=(q*q-1)//6
        assert two_digit_certificate(n,q)['result']==0,q
        count+=1
    print('FACTORIZATION_ONLY_PRIME_SQUARE_CHECK PASS',count)

if __name__=='__main__':main()
