#!/usr/bin/env python3
"""Exact H2/Hh BRC native-prefix costs, h=3..8; frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab."""
from collections import Counter
O='acdefg'
X={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0); SIGN=(1,2,4,8)

def keys(h):
 for z in range(1,(h+1)//2+1):
  for x in range(2*z,h+2):
   for y in range(h+2-2*z):
    if x+y>=h+2:yield (x,y,z)

def words(h,key):
 x,y,z=key; n=[z-1,0,0,z,h+1-y-2*z,h+1-x]
 d=x+y-h-1
 def rec(w,q):
  if not any(n):
   if S[q] in SIGN:yield w,S[q]
  else:
   for j in range(6):
    if n[j]:
     n[j]-=1
     yield from rec(w+O[j],T[q][j])
     n[j]+=1
 for c in range(d+1):
  n[1],n[2]=c,d-c
  yield from rec('',0)

def native(word):return tuple(x for a in word for x in X[a])
def signature(word):
 q=0
 for a in word:q=T[q][O.index(a)]
 return S[q]
def prefix_count(words):
 p=set()
 for w in words:
  a=native(w)
  for j in range(1,len(a)+1):p.add(a[:j])
 return len(p)

def optimal(h):
 children=[{}]; ends=[0]; count=Counter()
 for window in (2,h):
  for key in keys(window):
   for w,s in words(window,key):
    p=native(w); c=Counter(p)
    assert len(p)==2*(sum(key)-1)
    assert tuple(c[a] for a in (1,2,3))==key
    assert tuple(c[a]-c[-a] for a in range(1,7))==(2,0,0,0,0,0)
    count[window]+=1; u=0
    for a in p:
     if a not in children[u]:
      children[u][a]=len(children)
      children.append({});ends.append(0)
     u=children[u][a]
    ends[u]|=1<<((0 if window==2 else 4)+SIGN.index(s))
 dp=[None]*len(children)
 for u in range(len(children)-1,-1,-1):
  q=ends[u];d={0:0};a=q
  while a:d[a]=0;a=(a-1)&q
  for v in children[u].values():
   out=d.copy()
   for i,ci in d.items():
    for j,cj in dp[v].items():
     if j and not (i&j):
      z=i|j;val=ci+cj+1
      if val<out.get(z,10**9):out[z]=val
   d=out
  dp[u]=d
 return dp[0][255],len(children),dict(count)

def witness(h,route):
 r=h-2;base=['ce','ec','ed','de']
 later=([w+'g'*r for w in base] if route=='extend' else
        ['ce'+'g'*r,'e'+'g'*r+'c','e'+'g'*r+'d','de'+'g'*r])
 for i,w in enumerate(later):
  assert signature(w)==[4,8,2,1][i]
  c=Counter(native(w))
  assert tuple(c[a] for a in (1,2,3))==(3,h-1,1)
 return prefix_count(base+later)

def main():
 for h in range(3,9):
  exact,nodes,counts=optimal(h)
  x,y=witness(h,'extend'),witness(h,'reroute')
  assert (x,y)==(8*h+12,6*h+23)
  assert exact==min(x,y)
  print(h,exact,x,y,nodes,counts)
 for h in (9,16,32,64,100):
  assert witness(h,'extend')==8*h+12
  assert witness(h,'reroute')==6*h+23
 full=['ce'+'g'*r for r in range(4)]+['ec'+'g'*r for r in range(4)]+['ed'+'g'*r for r in range(4)]+['de'+'g'*r for r in range(4)]
 assert prefix_count(full)==52
 assert all(signature(w)==s for s,b in ((4,'ce'),(8,'ec'),(2,'ed'),(1,'de')) for w in (b+'g'*r for r in range(4)))
 print('H2-H5 interval:',prefix_count(full),'with keys',[(3,h-1,1) for h in range(2,6)])
if __name__=='__main__':main()
