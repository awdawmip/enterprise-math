from fractions import Fraction as F
S0=(214,215,216,217,218)
S1=(214,216,217,218,219,220,221)
S2=(215,216,217,218,219,220,221)
SETS=(set(S0),set(S1),set(S2))

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return a[0]*c,a[1]*c
def rotate(v,k):
 x,y=v
 return ((x,y),(-y,x),(-x,-y),(y,-x))[k%4]
zero=(0,0)
def event_moments(S,m):
 dp={0:((1,0),zero,zero)}
 for p in S:
  nd={}
  for cnt,(A,B,C) in dp.items():
   for n in range(m-cnt):
    cost=n*p
    a=rotate(A,cost)
    b=add(rotate(B,cost),scale(a,-cost))
    c=add(rotate(C,cost),add(scale(rotate(B,cost),-2*cost),scale(a,cost*(cost-1))))
    old=nd.get(cnt+n,(zero,zero,zero))
    nd[cnt+n]=(add(old[0],a),add(old[1],b),add(old[2],c))
  dp=nd
 A=B=C=zero
 for a,b,c in dp.values():A=add(A,a);B=add(B,b);C=add(C,c)
 return A,B,C
def overlap_moments(m):
 dp={(0,0,0):((1,0),zero)}
 for p in range(214,222):
  membership=[int(p in S) for S in SETS];nd={}
  for vec,(u,d) in dp.items():
   for n in range(m):
    vv=tuple(min(m,vec[j]+n*membership[j]) for j in range(3))
    if sum(x<m for x in vv)<2:continue
    co=n*p;a=rotate(u,co);b=add(rotate(d,co),scale(a,-co))
    old=nd.get(vv,(zero,zero))
    nd[vv]=(add(old[0],a),add(old[1],b))
  dp=nd
 u=d=zero
 for vec,(a,b) in dp.items():
  mult=max(sum(x<m for x in vec)-1,0)
  u=add(u,scale(a,mult));d=add(d,scale(b,mult))
 return u,d
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def calc_E(m):
 (u0,d0,v0),(u1,d1,_),(u2,d2,_)= [event_moments(S,m) for S in (S0,S1,S2)]
 uh,dh=overlap_moments(m)
 assert u0==zero
 b0=(F(12780)+F(23,2),F(-24));b1=(F(12558)+F(23,2),F(169,2))
 b2=(F(25115,2)+F(23,2),F(-23));bh=(F(24901,2)+F(23,2),F(-23))
 ex=scale(v0,F(1,2))
 ex=add(ex,cmul(b0,d0))
 ex=add(ex,cmul((220,-220),add(cmul(b1,u1),d1)))
 ex=add(ex,scale(add(cmul(b2,u2),d2),220))
 ex=add(ex,scale(add(cmul(bh,uh),dh),-440))
 assert ex[0].denominator==ex[1].denominator==1
 return int(ex[0]),int(ex[1])
R=[(-110,0),(8033772,-41446),(10499950,4893440),(-7284728,59598),(-12770418,-6606800),(-3019732,-22442),(-110,0),(0,-110)]
def gf_terms(K):
 seq=[]
 for k in range(K+1):
  x=R[k] if k<len(R) else zero
  for j,v in enumerate((-4,6,-4,1),start=1):
   if k>=2*j:x=add(x,scale(seq[k-2*j],-v))
  seq.append(x)
 return [add(seq[k],scale(rotate((1,0),k),110)) for k in range(K+1)]
if __name__=='__main__':
 import sys,time
 K=int(sys.argv[1]) if len(sys.argv)>1 else 12
 expected=gf_terms(K)
 for k in range(1,K+1):
  m=2*k;t=time.time();got=calc_E(m)
  assert got==expected[k],(m,got,expected[k])
  print('PASS',m,got,round(time.time()-t,3),flush=True)
 print('PASS independent integer DP and generating function recurrence',K)
