#!/usr/bin/env python3
"""D25 finite Clausen normal-form exact integer verifier (no floating point)."""
import json
from math import comb
from pathlib import Path

def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5)+1):
        if n%d == 0: return False
    return True

def mul(a,b,p):
    v=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): v[i+j]=(v[i+j]+ai*bj)%p
    return v

def rem(a,b,p):
    def trim(x):
        while x and x[-1]==0: x.pop()
        return x
    a=trim(a[:]);b=trim(b[:])
    while a and len(a)>=len(b):
        c=a[-1]*pow(b[-1],-1,p)%p
        offset=len(a)-len(b)
        for j,bj in enumerate(b): a[j+offset]=(a[j+offset]-c*bj)%p
        trim(a)
    return a

def gcd_degree(a,b,p):
    while b: a,b=b,rem(a,b,p)
    return len(a)-1

def invs(p):
    v=[0]*p;v[1]=1
    for i in range(2,p):v[i]=p-(p//i)*v[p%i]%p
    return v

def verify(p):
    assert p>=5 and is_prime(p)
    m=p//6;eps=int(p%6==5);b=2*m+eps
    d=m if not eps else 4*m+3
    iv=invs(p)
    # binomial normal form
    K=[1]
    for k in range(1,m+1):
        K.append(K[-1]*(m-k+1)*(2*m+eps-k+1)*iv[k]**2%p)
    # Gauss c_k = ((1/6)_k (1/3)_k)/(k!)^2
    G=[1]
    for k in range(1,d+1):
        G.append(G[-1]*(k-1+pow(6,-1,p))*(k-1+iv[3])*iv[k]**2%p)
    # 3F2 f_k = ((1/2)_k (1/3)_k (2/3)_k)/(k!)^3
    F=[1]
    for k in range(1,b+1):
        F.append(F[-1]*(k-1+iv[2])*(k-1+iv[3])*(k-1+2*iv[3]%p)*iv[k]**3%p)
    normal=mul(K,K,p)
    if eps: normal=mul([1,p-1],normal,p)
    assert F==normal, ('F',p)
    if eps:
        r=(p+1)//2
        T=[(-1)**j*comb(r,j)%p for j in range(r+1)]
        assert G==mul(T,K,p),('Gtwist',p)
    else: assert G==K,('G',p)
    assert sum(K)%p==comb(3*m+eps,m)%p !=0, ('endpoint',p)
    if m:assert gcd_degree(K,[i*K[i]%p for i in range(1,len(K))],p)==0, ('squarefree',p)
    x=1;W=0
    for k,f in enumerate(F):
        W=(W+(6*k+1)*f*x)%p;x=x*iv[2]%p
    x=1;kv=0;dv=0
    for k,c in enumerate(K):
        kv=(kv+c*x)%p
        if k:dv=(dv+2*k*c*x)%p
        x=x*iv[2]%p
    W2=pow(2,-eps,p)*kv*((1-6*eps)*kv+6*dv)%p
    assert W==W2,('weighted',p)
    return {'p':p,'eps':eps,'m':m,'degree_G':d,'degree_F':b,'K_1':sum(K)%p,
            'K_half':kv,'Kprime_half':dv,'W_half':W,'K_squarefree':True}

def main():
    primes=[p for p in range(5,2000) if is_prime(p)]
    primes += [p for p in [2003,2017,5003,10007,10009] if is_prime(p)]
    rows=[verify(p) for p in primes]
    print('PASS',len(rows),'primes','F-coeff',sum(r['degree_F']+1 for r in rows),
          'G-coeff',sum(r['degree_G']+1 for r in rows))
    print('W !=0:',[r['p'] for r in rows if r['W_half']])
    print('K_half=0:',sum(r['K_half']==0 for r in rows))
    print('second-factor=0:',sum(((1-6*r['eps'])*r['K_half']+6*r['Kprime_half'])%r['p']==0 for r in rows))
    # A local reproducible certificate, not a canonical Source admission.
    Path('d25_clausen_normal_form_certificate.json').write_text(
        json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

if __name__=='__main__':main()
