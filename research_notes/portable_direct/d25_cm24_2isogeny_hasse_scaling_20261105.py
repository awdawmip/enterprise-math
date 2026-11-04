"""D25 exact CM(-24) 2-isogeny, Frobenius, Hasse scaling checks."""
from math import isqrt, comb
Q=(1,-140,294,-140,1)
def mul(a,b,p):
 r=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]=(r[i+j]+x*y)%p
 while len(r)>4:
  z=r.pop();k=len(r)-4
  for i in range(4):r[k+i]=(r[k+i]-z*Q[i])%p
 return tuple((r+[0]*4)[:4])
def powr(a,n,p):
 r=(1,0,0,0)
 while n:
  if n&1:r=mul(r,a,p)
  a=mul(a,a,p);n>>=1
 return r
def plus(a,b,p):return tuple((a[i]+b[i])%p for i in range(4))
def times(a,k,p):return tuple((v*k)%p for v in a)
def prime_list(n):
 s=bytearray([1])*(n+1);s[:2]=b'\0\0'
 for k in range(2,isqrt(n)+1):
  if s[k]:s[k*k:n+1:k]=bytes((n-k*k)//k+1)
 return [p for p in range(5,n+1) if s[p] and p%8==5]
count=split=inert=0
for p in prime_list(3000):
 count+=1;m=(p-1)//2;one=(1,0,0,0);t=(0,1,0,0)
 F=powr(t,p,p)
 den=times(plus(one,t,p),2,p)
 den_inv=powr(den,p*p-2,p)
 assert mul(den,den_inv,p)==one
 s=mul(times(plus(one,F,p),-1,p),den_inv,p)
 s2=mul(s,s,p)
 assert mul(s,times(plus(one,t,p),2,p),p)==times(plus(one,F,p),-1,p)
 assert mul(s2,(1%p,(-2)%p,1%p,0),p)==F
 assert mul(s,powr(s,p,p),p)==(pow(4,-1,p),0,0,0)
 H=(0,0,0,0)
 for k in range(m,-1,-1):
  H=plus(mul(H,t,p),(comb(m,k)**2%p,0,0,0),p)
 assert powr(H,p,p)==mul(powr(s,m,p),H,p)
 if p%24==5:
  split+=1
  assert H!=(0,0,0,0)
  assert powr(H,p-1,p)==powr(s,m,p)
 else:
  inert+=1
  assert H==(0,0,0,0)
assert (count,split,inert)==(110,57,53)
print('PASS p<=3000 n=110 split=57 inert=53 isomorphism_scaling_norm=PASS Hasse_scaling=PASS')
