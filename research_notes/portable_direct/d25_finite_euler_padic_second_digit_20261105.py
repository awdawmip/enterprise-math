#!/usr/bin/env python3
"""Exact finite Gauss/Jacobi p^2 Euler lower discrepancy and upper cutoff."""
from math import comb
def eva(a,x,n):
 z=0
 for c in reversed(a):z=(z*x+c)%n
 return z
def verify(p):
 assert p>=5 and p%8==5
 q=(p-5)//8;ell=(5*p-1)//8;N=(p+1)//2;mod=p*p
 f=[1]
 for k in range(1,ell+1):f.append(f[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,mod)%mod)
 jac=[comb(q,j)*comb(3*q+1,j)%mod for j in range(q+1)]
 ep=[0]*(ell+1)
 for j,b in enumerate(jac):
  for i in range(N+1):ep[i+j]=(ep[i+j]+b*comb(N,i)*(-1)**i)%mod
 diff=[(f[k]-ep[k])%mod for k in range(ell+1)]
 assert all(x%p==0 for x in diff)
 K=[x//p for x in diff]
 assert K[0]==0 and K[1]==(3*(18-p)*pow(64,-1,p))%p
 x=pow(9,-1,mod);u=pow((1-x)%mod,N,mod)
 gv=eva(jac,x,mod);gp=eva([i*jac[i] for i in range(1,len(jac))],x,mod)
 kv=eva(K,x%p,p);kp=eva([i*K[i] for i in range(1,len(K))],x%p,p)
 fv=eva(f,x,mod);fp=eva([i*f[i] for i in range(1,len(f))],x,mod)
 assert (fv-u*gv-p*kv)%mod==0
 assert (fp-u*gp+N*pow((1-x)%mod,N-1,mod)*gv-p*kp)%mod==0
 full=f[:]
 for k in range(ell+1,p):full.append(full[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,mod)%mod)
 second=7*q+5
 assert all(full[k]%p==0 for k in range(ell+1,p))
 assert all(full[k]%mod==0 for k in range(second,p))
 tail=[0]*p
 for k in range(ell+1,min(second,p)):tail[k]=full[k]//p
 if p>5:assert full[ell+1]%mod!=0
 tv=eva(tail,x%p,p);tp=eva([k*tail[k] for k in range(1,p)],x%p,p)
 assert (eva(full,x,mod)-u*gv-p*(kv+tv))%mod==0
 assert (eva([k*full[k] for k in range(1,p)],x,mod)-u*gp+N*pow((1-x)%mod,N-1,mod)*gv-p*(kp+tp))%mod==0
 return {"p":p,"q":q,"ell":ell,"Kvalue":kv,"Kprime":kp,"Uvalue":tv,"Uprime":tp,"full_e0":(kv+tv)%p,"full_theta":((kp+tp)*pow(9,-1,p))%p,"J_at_1":gv,"Gprime":gp}
if __name__=="__main__":
 for p in (5,13,29,37,53,61,101,149,173,197,373):print(verify(p))
 print("PASS: 11 primes, coefficientwise Euler p², full cutoff, value and derivative")
