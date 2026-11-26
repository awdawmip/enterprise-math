from fractions import Fraction as F
from math import floor,ceil
from hashlib import sha256
import json,random
G=10**85;E=400000
B0=[(214400367204046439832747905320189591538351105920951930768238591471336985753828331576226,214400367204046439832747905320189591538351105920951930768238591471337016618243377672837),(991410104376806546245006442360370506919542722555360711737697284896267798454119146866295,991410104376806546245006442360370506919542722555360711737697284896271170423247861515800),(96908626596415488199625924806903600960651737707918479478269855624901489595100026049591,96908626596415488199625924806903600960651737707918479478269855625221421002362182677574)]
B1=[(214400367204046439832747905320189591538351105920951930768238591471337001196109386645552,214400367204046439832747905320189591538351105920951930768238591471337001196656728356815),(991410104376806546245006442360370506919542722555360711737697284896269484458469127177428,991410104376806546245006442360370506919542722555360711737697284896269484518264379180719),(96908626596415488199625924806903600960651737707918479478269855625061452448312226656203,96908626596415488199625924806903600960651737707918479478269855625061458121669367665141)]
def convergents(x):
 n,d=x.numerator,x.denominator;pp,qq,p,q=0,1,1,0
 while d:
  a,n,d=n//d,d,n%d;pp,p=p,a*p+pp;qq,q=q,a*q+qq
  yield p,q
def solve(box,L,H):
 (rl,ru),(cl,cu),(dl,du)=box
 assert dl*L>3*E*G
 assert F((ru-rl)*H+cu-cl,G)+F(du-dl,G*L)+F(2*E,L*L)<1
 def limits(p,q):
  al=rl*q-p*G;au=ru*q-p*G
  lo=F(min(al*L,al*H)+q*cl,G)+F(q*dl,G*H)-F(q*E,L*L)
  hi=F(max(au*L,au*H)+q*cu,G)+F(q*du,G*L)+F(q*E,L*L)
  return ceil(lo),floor(hi)
 _,p,q,lo,hi=min((max(0,b-a+1),p,q,a,b) for p,q in convergents(F(rl+ru,2*G)) if q<=H for a,b in [limits(p,q)])
 inv=pow(p,-1,q) if q>1 else 0
 out=[];calls=0
 def first(a,b,pred):
  while a<=b:
   mid=(a+b)//2
   if pred(mid):b=mid-1
   else:a=mid+1
  return a
 for h in range(lo,hi+1):
  r=(-inv*h)%q; l=ceil(F(L-r,q)); u=(H-r)//q
  if l>u:continue
  def interval(a,b,rr,cc,dd,ee,strict):
   if a>b:return None
   A=rr*q-p*G;B=cc*q-h*G;C=dd*q;D=ee*E*G*q
   def poly(n):
    nonlocal calls
    calls+=1;m=r+q*n
    return ((A*m+B)*m+C)*m+D
   def rising(n):
    m=r+q*n
    return poly(n+1)*m*m>=poly(n)*(m+q)**2
   k=first(a,b-1,rising)
   def good(n):return poly(n)<0 if strict else poly(n)<=0
   if not good(k):return None
   x=first(a,k,good);y=first(k,b,lambda n:not good(n))-1
   return x,y
  a=interval(l,u,rl,cl,dl,-1,False)
  if a is None:continue
  b=interval(*a,ru,cu,du,1,True)
  runs=[a] if b is None else [(a[0],b[0]-1),(b[1]+1,a[1])]
  for x,y in runs:
   if x<=y:
    m=r+q*x;j=(p*m+h)//q
    out.append((m,j,q,p,y-x+1))
 return out,max(0,hi-lo+1),calls
def expand(runs):return sorted((m+q*i,j+p*i) for m,j,q,p,n in runs for i in range(n))
def digest(x):return sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest()
def window(box,start,end):
 result=[];rows=[]
 for k in range(start,end):
  L=10**8*2**k;H=2*L-1
  runs,lines,calls=solve(box,L,H)
  rows.append((k+1,sum(r[-1] for r in runs),lines,calls,len(runs)))
  result.extend(runs)
 return result,rows
if __name__=='__main__':
 random.seed(1116)
 for _ in range(500):
  L=random.randrange(10**8,10**8+10000);H=L+random.randrange(0,60)
  r=random.randrange(-100,101)*G//random.randrange(1,21);c=random.randrange(-10,11)*G//7;d=random.randrange(1,20)*G
  box=[(r,r+G//10**12),(c,c+G//1000),(d,d+G//100)]
  runs,_,_=solve(box,L,H)
  truth=[]
  for m in range(L,H+1):
   low=F(box[0][0]*m+box[1][0],G)+F(box[2][0],G*m)-F(E,m*m)
   high=F(box[0][1]*m+box[1][1],G)+F(box[2][1],G*m)+F(E,m*m)
   truth.extend((m,j) for j in range(ceil(low),floor(high)+1))
  assert expand(runs)==truth
 for box,start,end in [(B0,0,90),(B1,0,90),(B1,90,100)]:
  runs,rows=window(box,start,end)
  pts=expand(runs);print('audit',start,end,len(pts),digest(pts),sum(r[2] for r in rows),sum(r[3] for r in rows))
  if box==B0:assert digest(pts)=='c000cf55b3d47848c40c44c1054616a8de93606fb5033268f57bcc2d19ee96e5'
  elif start==0:assert not pts
  else:assert digest(pts)=='82eb8fcf442e49134b6d8703dee9bb15d247a22b333e787cd1c3744d1698ff21'
 runs,rows=window(B1,100,110)
 assert digest(runs)=='c19e92aaf0b8f695e1dfa8678125cfdd932bd714adf6d190832e56e38e3fdd54'
 print('extension',rows,'total',sum(r[1] for r in rows),'lines',sum(r[2] for r in rows),'calls',sum(r[3] for r in rows),'runs',len(runs),'digest',digest(runs))
