from itertools import combinations, product
from math import gcd
from functools import reduce,lru_cache
from fractions import Fraction as Q
V=[(1,0,0),(1,3,-1),(4,-4,1),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(6,-1,0),(7,-1,0),(9,-5,1)]
W=[0,3,5,6,7,9]; MASK=[30,51,42,21,58,51,20,7,23,30]
E=[(17,1,0),(39,0,0),(17,0,1),(22,1,0),(0,1,1),(22,0,1)]
J=list(combinations(range(4),2))
def gaps(v):
 x,y,z=v;h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z);return tuple(abs(h[i]-h[j]) for i,j in J)
G=list(map(gaps,V)); T=sorted({(j,g) for i in W for j,g in enumerate(G[i]) if g and MASK[i]>>j&1}); H=sorted({(j,g) for row in G for j,g in enumerate(row) if g})
def line(a,b,k=1,l=1):
 j,g=a;h,f=b;return tuple(k*g*E[h][i]-l*f*E[j][i] for i in range(3))
def norm(v):
 d=reduce(gcd,v);return tuple(x//d for x in v) if d else v
def canon(v):
 v=norm(v);return tuple(-x for x in v) if next((x for x in v if x),1)<0 else v
def dot(a,b):return sum(x*y for x,y in zip(a,b))
L=sorted({canon(line(a,b)) for a,b in combinations(T,2)}|{canon(line(a,h,3,2)) for a in T for h in H}); L=[l for l in L if min(l)<0<max(l)]
P=L+[tuple(-x for x in l) for l in L]
def split(c,l):
 vv=[dot(p,l) for p in c]
 if not min(vv)<0<max(vv):return [c]
 out=[[],[]]
 for i,p in enumerate(c):
  q=c[(i+1)%len(c)];v,w=vv[i],vv[(i+1)%len(c)]
  if v>=0:out[0].append(p)
  if v<=0:out[1].append(p)
  if v*w<0:
   r=norm(tuple(abs(w)*a+abs(v)*b for a,b in zip(p,q)))
   out[0].append(r);out[1].append(r)
 return [tuple(x) for x in out]
def points():
 polys=[((1,0,0),(0,1,0),(0,0,1))]
 for l in L:polys=[z for c in polys for z in split(c,l)]
 pts=set()
 for c in polys:
  pts.update(c);pts.add(norm(tuple(map(sum,zip(*c)))))
  for a,b in zip(c,c[1:]+c[:1]):pts.add(norm(tuple(x+y for x,y in zip(a,b))))
 return sorted(p for p in pts if min(p)>0)
def label(p):
 s=[dot(e,p) for e in E];z=[Q(g,s[j]) for j,g in T];fs=[max(Q(g,s[j]) for j,g in enumerate(row)) for row in G];eta=min(fs[i] for i in W);mask=sum(1<<i for i,v in enumerate(z) if v==eta);near=sum(1<<i for i,v in enumerate(fs) if 2*v<3*eta);assert mask;return mask,near

def search(pts,depth=6,budget=1000000):
 N=len(pts);ALL=(1<<N)-1;qm=[0]*len(P);om={};nm={};single={}
 for i,p in enumerate(pts):
  a,b=label(p);bit=1<<i
  for j,l in enumerate(P):
   if dot(l,p)>0:qm[j]|=bit
  nm[b]=nm.get(b,0)|bit
  for j in range(len(T)):
   if a>>j&1:om[j,b]=om.get((j,b),0)|bit
  if a.bit_count()==1:single[a,b]=single.get((a,b),0)|bit
 sm_by_n={b:[m for (a,c),m in single.items() if c==b] for b in nm}
 qm=sorted({min(m,ALL^m) for m in qm if m and m!=ALL})
 @lru_cache(None)
 def lb(s):return sum(max(1,sum(bool(s&m) for m in sm_by_n[b])) for b,u in nm.items() if s&u)
 @lru_cache(None)
 def leaf(s):return next((k for k,m in om.items() if s&m==s),None)
 calls=0
 class Budget(Exception):pass
 @lru_cache(None)
 def solve(s,d):
  nonlocal calls
  calls+=1
  if calls>budget:raise Budget
  if lb(s)>2**d:return False
  if leaf(s) is not None:return True
  if d==0:return False
  if d==1:
   return any(a and a!=s and leaf(a) is not None and leaf(s^a) is not None for m in qm for a in [s&m])
  opts=[];seen=set()
  for m in qm:
   a=s&m;b=s^a;k=min(a,b)
   if not a or not b or k in seen:continue
   seen.add(k);x=lb(a);y=lb(b)
   if max(x,y)>2**(d-1):continue
   if x<y:a,b,x,y=b,a,y,x
   opts.append((x,x+y,max(a.bit_count(),b.bit_count()),a,b))
  for _,__,___,a,b in sorted(opts):
   if solve(a,d-1) and solve(b,d-1):return True
  return False
 try: result=solve(ALL,depth)
 except Budget:result=None
 print('points',N,'splits',len(qm),'lb',lb(ALL),'depth',depth,'feasible',result,'calls',calls,flush=True)
 return result
if __name__=='__main__':
 pts=points(); print('lines',len(L),'predicates',len(P),'arrangement points',len(pts),flush=True)
 ids=list(map(int, "49 87 171 189 195 198 199 200 204 206 209 336 407 414 424 426 428 473 484 508 560 574 657 662 666 667 668 687 696 699 710 717 718 823 826 828 832 834 838 913 945 951 988 1027 1028 1069 1080 1102 1111 1179 1196 1238 1270 1283 1307 1308 1310 1354 1359 1380 1462 1492 1564 1569 1586 1589 1692 1728 1797 1913 1963 1977 1995 2008 2013 2032 2093 2149 2200 2222 2368 2506 2786 2794 2847 2927 3055 3493 3520 3746 3785 3804 3806 3808 3809 3814 8950 8964 8976 9002 9012 9014 9064 9080 9121 9141 9172 9173 9505 9508 9520 9549 9604 9788 9835 9947 9980 10020 10028 10046 10093 10133 10135 10141 10231 10256 10323 10390 12686 12742 12743 12794 12812 12897 12959 12961 12963 12970 13031 13047 13112 13115 13153 13158 13165 13192 13205 13206 13212 13214 13219 13264 13275 13300 13346 13350 13352 13394 13510 13525 13595 13637 13663 13701 13807 13989 14008 14022 14064 14219 14658 14762 14895 14927 15134 15197 15294 15339 15346 15437 15524 15586 15924 16160 16227 16242 16256 16285 16312 16315 16400 16636 16707 16749 16812 16815 16902 17222 17524 17536 17560 17698 17741 18054 18063 18145 18481 18526 18554 19000 19318 19428 19447 19467 19491 19547 19870 19886 19892 19900 19971 20261 20331 20333 20701 20776 20792 20795 20798 20839 20848 20951 21002 21042 21065 21203 21286 21378 21474 21816 21872 21960 22084 22288 22291 22445 22658 22683 23171 23533 24054 24066 24068 24119 24160 24169 24281 24313 24315 24332 24426 24528 24622 24904 24924 24961 24998 25010 25047 25373 25383 25645 25691 25832 26021 26117 26351 26376 26384 26423 26565 26642 26643 26941 27032 27099 27105 27229 27412 27543 27572 27619 27730 27734 27851 27975 28405 28873 28980 29010 29076 29183 29189 29323 29492 29531 29623 29690 29699 29725 29785 29842 29986 30129 30172 30194 30195 30241 30640 31375 37312 37403 37787 37932 38192 38291 38449 38546 38827 38835 38875 39089 39262 39329 39467 39716 39883 40127 40202 40234 40235 40360 40462 40464 40474 40577 40728 40809 41123 41139 41224 41277 41600 42173 42348 42602 42665 42933 43001 43391".split()))
 assert len(ids)==len(set(ids))==360
 witness=[pts[i] for i in ids]
 full=[v for v in product(range(-10,11),repeat=3) if next((a for a in v if a),0)>0 and max(sum(max(a,0) for a in v),sum(max(-a,0) for a in v))<=10]
 assert len(full)==1935
 raw=list(map(gaps,full))
 for p in witness:
  s=[dot(e,p) for e in E]
  scores=[max(Q(g,s[j]) for j,g in enumerate(row)) for row in raw]
  eta=min(scores); near={v for v,f in zip(full,scores) if 2*f<3*eta}
  a,b=label(p)
  assert a==sum(1<<i for i,(j,g) in enumerate(T) if Q(g,s[j])==eta)
  assert near=={v for i,v in enumerate(V) if b>>i&1}
 print('full directions',len(full),'exact evaluations',len(full)*len(witness),'PASS',flush=True)
 r=search(witness,budget=1000000)
 assert r is False
 print('EXPANDED SIX-COMPARISON OBSTRUCTION PASS')
