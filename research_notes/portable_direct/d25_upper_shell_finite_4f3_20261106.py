#!/usr/bin/env python3
"""Exact author-side D25 upper-shell and complementary-index checks."""
import math, json
def primes(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
def run():
    P=primes(997); upper=[]; pairs=0; count=0
    for p in P:
        # Independent p-free factorial-unit computation of all paired ratios.
        unit=[1]*(3*p); val=[0]*(3*p)
        for t in range(1,3*p):
            x=t; e=0
            while x%p==0:x//=p;e+=1
            unit[t]=unit[t-1]*x%p; val[t]=val[t-1]+e
        def au(k):
            v=val[2*k]+val[3*k]-5*val[k]
            r=unit[2*k]*unit[3*k]*pow(unit[k],-5,p)*pow(216,-k,p)%p
            return v,r
        for k in range(p//3+1,(p-1)//2+1):
            v,a=au(k);w,b=au(p-k)
            assert (v,w)==(1,2) and a*b%p==pow(36*k**3,-1,p)
            pairs+=1
        if p%6!=1:continue
        count+=1; m=(p-1)//6;s=(p+1)//2;h=(p-1)//2;L=4*m;J=m-1
        eps=1 if pow(6,h,p)==1 else -1
        mod=p**3
        def orig(k):
            n=math.comb(2*k,k)**2*math.comb(3*k,k)
            return n*pow(pow(216,k,mod),-1,mod)%mod
        A=[orig(s+j)//p**2 for j in range(m)]
        assert all(orig(s+j)%p**2==0 for j in range(m))
        top=eps*pow(9,-1,p)%p;assert A[0]==top
        Q=[1];M=[1]
        for j in range(J):
            num=(j+1)*(6*j+5)*(6*j+7)*(6*j+9)
            den=27*(2*j+3)**4
            Q.append(Q[-1]*num*pow(den,-1,p)%p)
            M.append(M[-1]*9*(2*j+1)**3*pow((j+1)*(6*j+5)*(6*j+7),-1,p)%p)
        for j in range(m):
            assert A[j]%p==top*Q[j]%p
            assert M[j]*Q[j]*(2*j+1)**3%p==1
            mid=orig(h-j)
            assert mid%p==0 and mid//p%p==(-2*eps*M[j])%p
            assert (mid//p)*A[j]%p==pow(36*(h-j)**3,-1,p)
        U=sum((6*(s+j)+1)*A[j] for j in range(m))%p
        assert U==top*sum((6*j+4)*Q[j] for j in range(m))%p
        for j in range(m+1):
            lhs=9*j*(2*j+1)**3*Q[j] if j<m else 0
            rhs=j*j*(6*j-1)*(6*j+1)*Q[j-1] if j else 0
            assert (lhs-rhs)%p==0
        upper.append({"p":p,"eps":eps,"a_s_over_p2":top,"U_mod_p":U})
    ans={"date":"2026-11-06","mode":"author_exact_integer","reciprocity_primes":len(P),
         "reciprocity_pairs":pairs,"upper_4f3_primes":count,"all_passed":True,
         "upper_results":upper}
    with open("20261106_d25_upper_shell_finite_4f3_results.json","w") as f:json.dump(ans,f,indent=2)
    print(len(P),pairs,count,"all_assertions_passed")
if __name__=="__main__":run()
