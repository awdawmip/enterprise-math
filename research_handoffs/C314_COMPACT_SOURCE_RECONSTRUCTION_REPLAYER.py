"""C314 author replay: exact source-side reconstruction; stdlib Fraction only.
Unpack the C314 portable ZIP; run python C314_COMPACT_REPLAYER.py.
The frozen C301 input files remain under EM_C301_EXACT_PORTABLE/.
"""
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
from collections import Counter
import hashlib,json,os,sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'EM_C301_EXACT_PORTABLE'
sys.path.insert(0,str(BASE));os.chdir(BASE)
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as p
import C298_SHARED_DENOMINATOR_EXACT as c

def pm(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return tuple(out)
def pe(a,t):
 v=F(0)
 for x in reversed(a):v=v*t+x
 return v
def trim(a):
 a=tuple(map(F,a))
 while len(a)>1 and not a[-1]:a=a[:-1]
 return a
def pair(n,d,lo,hi):
 z=pe(d,lo);v=pe(d,hi)
 assert z and v and (z>0)==(v>0)
 return trim(n),trim(d if z>0 else tuple(-x for x in d))
def direct(path,lo,hi,W):
 w,d=path['w'],path['d']; rows=[]
 for j in s.J:
  a=F(W[j],s.Q);fac=[]
  for k in range(4):
   a*=abs(s.U[j]-s.U[s.I[k]])/(s.Z-s.U[s.I[k]])
   fac.append(pair((s.Z-w[k],-d[k]),(s.U[j]-w[k],-d[k]),lo,hi))
  rows.append((a,fac))
 for k in range(4):
  x=(w[k],d[k]);sq=pm(x,x)
  a=(F(2)-sq[0],-sq[1],-sq[2]);b=(F(3)-sq[0],-sq[1],-sq[2]);q=pm(a,b)
  fac=[pair((s.A/s.H,),pm(pm(q,q),q),lo,hi)]
  for j in s.J:fac.append(pair((s.Z-s.U[j],),(w[k]-s.U[j],d[k]),lo,hi))
  for m in range(4):
   if m!=k:fac.append(pair((s.Z-w[m],-d[m]),(w[k]-w[m],d[k]-d[m]),lo,hi))
  rows.append((F(1),fac))
 assert len(rows)==79
 return rows

def primitive(d):
 if len(d)!=2 or not d[1]:return None
 L=lcm(*(x.denominator for x in d));z=[int(x*L) for x in d];g=gcd(abs(z[0]),abs(z[1]))
 return tuple(x//g for x in z)
def residue(rows,q):
 t=F(-q[0],q[1]);ans=[]
 for j,(a,fs) in enumerate(rows):
  hit=[h for h,(_,den) in enumerate(fs) if (lambda z:z is not None and (z==q or z==(-q[0],-q[1])))(primitive(den))]
  if not hit:continue
  assert len(hit)==1
  h=hit[0];r=a*F(q[1],fs[h][1][1])
  for z,(n,d) in enumerate(fs):
   r*=pe(n,t)
   if z!=h:r/=pe(d,t)
  ans.append((j,r))
 return ans

def evaluate(rows,t):
 total=F(0)
 for c,fs in rows:
  term=c
  for n,d in fs:term*=pe(n,t)/pe(d,t)
  total+=term
 return total

def run():
 cert=json.loads((BASE/'C293_125_REFINED_BRACKETS.json').read_text())
 raw=json.dumps(cert['records'],separators=(',',':'),ensure_ascii=False).encode()
 assert hashlib.sha256(raw).hexdigest()==cert['records_sha256']
 paths,_=p.build_paths();W,_=s.floor_fixed_masses()
 checked=zeros=midpoints=0;lines=[]
 for i,path in enumerate(paths):
  assert cert['records'][i][0]==i
  lo=F(int(cert['records'][i][1]),1<<24);hi=lo+F(1,1<<24);t=(lo+hi)/2
  original=direct(path,lo,hi,W);candidate=c.make_terms(path,lo,hi,W)
  for (a,aa),(b,bb) in zip(original,candidate):
   assert a==b and len(aa)==len(bb)
   for (n,d),(N,D) in zip(aa,bb):
    assert trim(pm(n,D))==trim(pm(N,d))
    checked+=1
  vv=tuple(w+t*d for w,d in zip(path['w'],path['d']))
  assert s.original_F(vv,W)/s.Q==evaluate(original,t)==evaluate(candidate,t)
  midpoints+=1
  for a,b in ((0,2),(1,3)):
   q=primitive(pair((F(1),),(path['w'][a]-path['w'][b],path['d'][a]-path['d'][b]),lo,hi)[1]);assert q
   rs=residue(original,q)
   assert [j for j,_ in rs]==([75,77] if a==0 else [76,78])
   assert rs[0][1] and rs[0][1]==-rs[1][1]
   zeros+=1
   lines.append([i,list(q),[rs[0][0],rs[1][0]]])
 assert (len(paths),checked,zeros,midpoints)==(125,77000,250,125)
 print('C314_PASS paths=125 labels=79 factor_cross_products=77000 exact_cancellations=250 C275_midpoints=125')
 return lines
if __name__=='__main__':run()
