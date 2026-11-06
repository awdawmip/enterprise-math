#!/usr/bin/env python3
"""Exact p-adic Newton separation for the D25 auxiliary labelled source observer.

Python standard library. No floats, no external research runtime, no native EM experiment.
"""
from math import comb, factorial

PRIMES=(7,13,19,31,37,61,73,109,229,373)
DIGITS=(2,3)

def gcomb(n,k):
    if k<0:return 0
    if n>=0:return comb(n,k) if n>=k else 0
    return (-1)**k*comb(k-n-1,k)

def forward_diffs(vals,M):
    row=list(vals)
    ds=[]
    while row:
        ds.append(row[0]%M)
        row=[(row[i+1]-row[i])%M for i in range(len(row)-1)]
    return ds

def check(p,s):
    m=(p-1)//6; a=2*m; b=3*m; c=4*m; M=p**s
    assert p==6*m+1
    inv2=pow(2,-1,M)
    weights=[((6*j+1)*pow(-inv2,j,M)*comb(b,j))%M for j in range(b+1)]
    normal=[]; carry=[]
    for t in range(p):
        terms=[weights[j]*gcomb(t-a,j)*comb(t,j)%M if j<=t else 0 for j in range(b+1)]
        normal.append(sum(terms[:a+1])%M)
        carry.append(sum(terms[a+1:])%M)
    samples=[(x+y)%M for x,y in zip(normal,carry)]
    D=forward_diffs(samples,M)
    n_hat=[]; r_hat=[]
    for t in range(p):
        n_hat.append(sum(D[r]*comb(t,r) for r in range(min(c,t)+1))%M)
        r_hat.append(sum(D[r]*comb(t,r) for r in range(c+1,min(p-1,t)+1))%M)
    assert n_hat==normal,('normal',p,s)
    assert r_hat==carry,('carry',p,s)
    assert all(v==0 for v in carry[:c+1])
    H=[0]*p
    for i in range(1,p):H[i]=(H[i-1]+pow(i,-1,M))%M
    n_der=0; r_der=0
    for j in range(b+1):
        if j<=a:
            deriv=comb(a,j)*comb(c,j)*(H[a]-H[a-j]+H[c]-H[c-j])
            n_der=(n_der+weights[j]*deriv)%M
        else:
            deriv=(factorial(a)*(-1)**(j-a-1)*factorial(j-a-1)*pow(factorial(j),-1,M)*comb(c,j))
            r_der=(r_der+weights[j]*deriv)%M
    n_newton=0; r_newton=0
    for r in range(1,p):
        if r<=c:
            derivative=comb(c,r)*(H[c]-H[c-r])
            n_newton=(n_newton+D[r]*derivative)%M
        else:
            derivative=factorial(c)*(-1)**(r-c-1)*factorial(r-c-1)*pow(factorial(r),-1,M)
            r_newton=(r_newton+D[r]*derivative)%M
    assert (n_der,r_der)==(n_newton,r_newton),(p,s,(n_der,r_der),(n_newton,r_newton))
    tangent=(n_der+r_der)%M
    return {"p":p,"s":s,"M":M,"normal_derivative":n_der,"carry_derivative":r_der,"total_derivative":tangent,"low_digit":tangent%p,"second_digit":(tangent//p)%p if tangent%p==0 else None,"all_samples_reconstructed":True}

def main():
    for p in PRIMES:
        for s in DIGITS:
            x=check(p,s)
            print(x)
    print(f"PASS: {len(PRIMES)*len(DIGITS)} exact prime-power source reconstruction cases")

if __name__=='__main__':main()
