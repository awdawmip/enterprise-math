#!/usr/bin/env python3
"""Exact p² bridge: Gauss S vs CM Legendre P, with separated signed contributions."""
def primes(n):
    a = [True]*(n+1); a[0]=a[1]=False
    for q in range(2,int(n**0.5)+1):
        if a[q]:
            for t in range(q*q,n+1,q): a[t]=False
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def S_mod_p2(p):
    m=(p-1)//6; M=p*p
    c=1; s=1
    for n in range(2*m):
        c=c*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,M)%M
        s=(s+c)%M
    return s

def P_even_mod_p2(p):
    m=(p-1)//6; M=p*p; h2=pow(2,-1,M)
    a=(1,0); b=(0,1)
    for n in range(1,2*m):
        a0=(2*n+1)*b[1]*h2-n*a[0]
        a1=(2*n+1)*b[0]-n*a[1]
        inv=pow(n+1,-1,M)
        a,b=b,(a0*inv%M,a1*inv%M)
    assert b[1]==0
    return b[0]

def correction(p):
    m=(p-1)//6
    factorials=[1]
    for n in range(1,2*m+1): factorials.append(factorials[-1]*n%p)
    h=[0]*(2*m+1)
    for n in range(1,2*m+1):h[n]=(h[n-1]+pow(n,-1,p))%p
    ans1=0
    for n in range(m+1):
        fn=(factorials[m]*pow(factorials[n]*factorials[m-n],-1,p)%p)
        fn=fn*factorials[2*m]*pow(factorials[n]*factorials[2*m-n],-1,p)%p
        fn=fn*pow(2,-n,p)%p
        d=(h[2*m]-h[2*m-n]-h[m]+h[m-n])%p
        ans1=(ans1+fn*d*pow(6,-1,p))%p
    ans2=0
    for n in range(m+1,2*m+1):
        bn=(-1)**(m+n)*factorials[m]*factorials[2*m]*factorials[n-m-1]
        bn=bn*pow(6*factorials[2*m-n]*pow(2,n,p)*factorials[n]**2,-1,p)%p
        ans2=(ans2+bn)%p
    return ans1,ans2,(ans1+ans2)%p

ps=primes(997)
assert len(ps)==80
for p in ps:
    s=S_mod_p2(p); P=P_even_mod_p2(p)
    a,b,c=correction(p)
    assert (s-P)%p==0,(p,s,P)
    assert (s-P)//p%p==c,(p,s,P,a,b,c)
print('p² bridge PASS for',len(ps),'primes p≡1 mod6 through 997')
for p in [7,13,19,31,67,139,373,997]:
    a,b,c=correction(p)
    print(p,'S',S_mod_p2(p),'P',P_even_mod_p2(p),
          'C_param',a,'C_tail',b,'total',c)
