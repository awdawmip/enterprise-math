#!/usr/bin/env python3
"""PREFIX-538 exact certificate for four-STAR rooted axis-one BRC support."""
from collections import defaultdict
from json import dump
S=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple((-1 if c>0 else 1)*x for x in S[a] if x!=abs(c))
P=tuple((a,p,e*x) for a in range(4) for x in S[a] for e in (-1,1) for p in near(a,e*x))
I={x:i for i,x in enumerate(P)}
def suc(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S[b]);return tuple(I[x] for x in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(suc(i) for i in range(48));sig=lambda i: (1 if P[i][2]>0 else -1) if abs(P[i][2])==1 else 0
eps=lambda i:int(sig(i)!=0)
T=I[(0,1,-3)]
assert len(P)==48 and all(len(x)==3 for x in N)
assert all(not eps(j) and all(not eps(k) for k in N[j]) for i in range(48) if eps(i) for j in N[i])
C=[I[x] for x in [(0,-6,3),(0,3,-1),(0,-1,6),(0,6,-3),(0,-3,1),(0,1,-6)]]
assert all(C[(j+1)%6] in N[C[j]] for j in range(6))
assert [sig(i) for i in C]==[0,-1,0,0,1,0]
def pcount(path):
 k=sum(eps(path[j])+eps(path[j+1]) for j in range(len(path)-1));delta=abs(sig(path[0])-sig(path[-1]))
 return (k-delta)//2
assert all(pcount([C[j%6] for j in range(d+1)])==(d+1)//3 for d in range(241))
def cap(d,m):
 h=(d+2)//4
 return (h+1)*(m+1)-h*(h+1)//2
rows=[]
for d in range(25):rows.append({'depth':d,'max_p':-1,'max_h':-1,'max_terms':0,'total_terms':0,'new_cap':cap(d,(d+1)//3),'old_cap':cap(d,d),'fibers':set()})
for r in range(48):
 st={(r,0,0,0):1}
 for d in range(25):
  poly=defaultdict(int)
  for (i,b,k,h),v in st.items():
   delta=abs(sig(i)-sig(r)); assert k>=delta and (k-delta)%2==0
   p=(k-delta)//2; assert 0<=p<=(d+1)//3 and 0<=h<=(d+2)//4 and h<=p
   poly[(p,h)]+=v
  assert sum(poly.values())==6**d and len(poly)<=rows[d]['new_cap']
  row=rows[d];row['max_p']=max(row['max_p'],max(p for p,h in poly));row['max_h']=max(row['max_h'],max(h for p,h in poly));row['max_terms']=max(row['max_terms'],len(poly));row['total_terms']+=len(poly);row['fibers'].add(tuple(sorted(poly.items())))
  if d==24:break
  nx=defaultdict(int)
  for (i,b,k,h),v in st.items():
   for j in N[i]:
    kk=k+eps(i)+eps(j);nx[(j,0,kk,h)]+=v;nx[(j,1,kk,h+int(b and j==T))]+=v
  st=nx
for row in rows:row['fibers']=len(row['fibers']);assert row['max_p']==(row['depth']+1)//3
assert rows[24]=={'depth':24,'max_p':8,'max_h':6,'max_terms':41,'total_terms':1876,'new_cap':42,'old_cap':154,'fibers':26}
report={'status':'ALL_CHECKS_PASS','roots':48,'depths':'0..24','root_depth_equalities':1200,'pumped_witness':'0..240','model':'four-STAR directed native X6, 3 successors and 2 Cell labels per step','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','by_depth':rows,'review':'UNREVIEWED / NOT_ADMITTED'}
with open('PREFIX538_EXACT_EXECUTION.json','w') as f:dump(report,f,indent=2)
print(report['status'],rows[24])
