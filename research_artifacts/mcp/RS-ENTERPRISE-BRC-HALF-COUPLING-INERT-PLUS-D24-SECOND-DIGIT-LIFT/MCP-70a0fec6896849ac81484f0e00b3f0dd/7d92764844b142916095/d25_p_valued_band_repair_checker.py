from math import isqrt

def inv(a,m): return pow(a%m,-1,m)
def primes(n): return [x for x in range(2,n) if all(x%d for d in range(2,isqrt(x)+1))]
def Bseq(p):
 M=p**3; B=[1]; c=1
 for k in range(p-1):
  c=c*((6*k+1)*(3*k+1)%M)*inv(36*(k+1)*(k+1),M)%M; B.append(c)
 return B
def la(p,s): return s*s*(6*s+1)%p*inv((s+1)*(2*s+1)*(3*s+2),p)%p
def mu(p,s): return ((2*s+1)*(3*s+1)*(3*s+2)*(6*s+7)**2%p)*inv(36*(s+1)*(6*s+1)*(s+2)*(2*s+3)*(3*s+5),p)%p
def rx(p,s): return 3*s*(6*s+1)%p*inv((6*s+5)**2,p)%p
def ru(p,s): return 3*s*(6*s+1)*(12*s+11)%p*inv((6*s+5)**2*(12*s-1),p)%p
def ee(p,s):
 r=ru(p,s); return (r*((ru(p,s+1)-la(p,s+1))%p)-mu(p,s)*((r-la(p,s))%p))%p
def q(p,G,h):
 d=(G%(p*p))*(h%(p*p))-1; d%=p*p; assert d%p==0; return d//p%p
def check(p):
 m=(p-1)//6; M=p**3; B=Bseq(p)
 for k,b in enumerate(B):
  if k<=m: assert b%p
  elif k<=2*m: assert b%p==0 and b%(p*p)
  else: assert b%(p*p)==0
 g=sum(B)%M; h=sum(((12*k+1)%M)*B[k] for k in range(p))%M; assert g%p==0
 G=(g//p)%(p*p); hb=h%p; Gb=G%p; assert Gb*hb%p==1
 band=[m+r for r in range(1,m+1)]; gs=(g-sum(B[k] for k in band))%M; hs=(h-sum(((12*k+1)%M)*B[k] for k in band))%M
 qs=[q(p,G,hs)]; Is=[((gs//p)%p)*(hs%p)%p]; xs={}
 for s,k in enumerate(band,1):
  x=(B[k]//p)%p; assert x; old=Is[-1]; xs[s]=x; gs=(gs+B[k])%M; hs=(hs+(12*k+1)*B[k])%M
  new=((gs//p)%p)*(hs%p)%p; assert (new-old)%p==hb*x%p and new!=old; Is.append(new); qs.append(q(p,G,hs))
 assert Is[-1]==1
 for s in range(1,m): assert xs[s+1]*inv(xs[s],p)%p==rx(p,s)
 U={s:(qs[s]-qs[s-1])%p for s in range(1,m+1)}
 for s in U: assert U[s]==Gb*(12*s-1)%p*xs[s]%p
 if m>=3:
  V={s:(U[s+1]-la(p,s)*U[s])%p for s in range(1,m)}; D={s:(V[s+1]-mu(p,s)*V[s])%p for s in range(1,m-1)}
  for s in D: assert D[s]==U[s]*ee(p,s)%p
  assert D[m-2]==(-42062*inv(343,p))%p*Gb%p*xs[m]%p and D[m-2]!=0

def main():
 assert 42062==2*21031 and all(21031%d for d in range(2,isqrt(21031)+1)) and 21031%24==7
 T=[p for p in primes(5000) if p%24 in (13,19)]; assert len(T)==166
 for p in T: check(p)
 print('targets',len(T),'failures',0)
if __name__=='__main__': main()
