from pathlib import Path
from collections import Counter
from geom import reps,G,image,pieces
D=Path(__file__).resolve().parent
U=(1<<50)-1; Z=(1<<25)-1
P=[int(l.split()[0])>>25 for l in open('pdecomp.txt')];assert len(P)==500
R=[]
for l in (D/'fix4.txt').open():
 r,n,*a=map(int,l.split());R.append((r,a));assert len(a)==n
FAMILIES={r:a for r,a in R};WEIGHT={r:max(v.bit_count() for v in f) for r,f in R}
# cost capacity independently of disjoint fixed points; when 7 sets chosen, choose allowed maxima and take any disjoint ownership.
node=0;complete=0;tried=0;weightsPrunes=0

def cover_fixed(rows, fixed):
 if not rows:return fixed==Z
 if (Z ^ fixed).bit_count()>sum(WEIGHT[r] for r in rows):return False
 r=rows[0]
 for s in FAMILIES[r]:
  if cover_fixed(rows[1:],fixed|s):return True
 return False

def dfs(rem,rows,tw,gaps):
 global node,complete,weightsPrunes
 node+=1
 if gaps==0:
  complete+=1
  return tw>=25 and cover_fixed(tuple(sorted(rows,key=lambda r:len(FAMILIES[r]))),0)
 cand=[r for r in FAMILIES if r&rem==r]
 # Count upper bound on total possible weight of remaining disjoint rows
 if tw+sum(sorted((WEIGHT[r] for r in cand),reverse=True)[:gaps])<25:
  weightsPrunes+=1;return False
 best=None
 for j in pieces(rem):
  a=[r for r in cand if r>>j&1]
  if best is None or len(a)<len(best):best=a
  if not a:return False
 for r in best:
  if dfs(rem^r,rows+[r],tw+WEIGHT[r],gaps-1):return True
 return False

for p,n in [(int(l.split()[0])>>25,int(l.split()[1])) for l in (D/'p11_reps.txt').open()]:
 pairreps=[];todo=set(q<<25 for q in P if not p&q);stab=[g for g in G if image(p<<25,g)==p<<25]
 while todo:
  q=min(todo);orb={image(q,g) for g in stab};assert orb<=todo;todo-=orb;pairreps.append(q>>25)
 for q in pairreps:
  tried+=1
  if dfs(U^(p|q),[],0,7):print('FOUND',p,q);raise SystemExit
 print(tried,node,complete,weightsPrunes,flush=True)
print('no pattern k=2')
