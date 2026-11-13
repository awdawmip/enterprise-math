#!/usr/bin/env python3
"""Exact independent verification from frozen BRC master input.
Usage: python CHECK_EC49FNMA.py master_and_radius3_cases.txt
"""
import sys,hashlib,collections,itertools
FROZEN='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
Q=(5,7,11,13,15,17,19,21); INF=10**9
raw=open(sys.argv[1],'rb').read();assert hashlib.sha256(raw).hexdigest()==FROZEN
tokens=iter(raw.decode().split()); nk,nw,nc=(int(next(tokens)) for _ in range(3));assert(nk,nw,nc)==(94,178850,38169)
needed={0,4,5,11,34,61,64,65,66}; words={k:[] for k in needed}; nread=0
for k in range(nk):
 n=int(next(tokens)); nread+=n
 for _ in range(n):
  lab=int(next(tokens));path=next(tokens)
  if k in needed: words[k].append((lab,bytes.fromhex(path)))
assert nread==nw
cases={}
for i in range(nc):
 keys=[int(next(tokens)) for _ in range(7)]
 if i in (31502,31503,31504): cases[i]=keys
try:next(tokens);raise AssertionError('trailing input')
except StopIteration:pass

def root_table(group):
 labs=sorted({lab for lab,_ in group});idx={x:j for j,x in enumerate(labs)}
 edges=[{}]; terminal=[0]
 for lab,path in group:
  v=0
  for b in path[1:]:
   if b not in edges[v]:
    edges[v][b]=len(edges);edges.append({});terminal.append(0)
   v=edges[v][b]
  terminal[v]|=1<<idx[lab]
 def visit(v):
  out={0:0}
  if terminal[v]:out[terminal[v]]=0
  for child in edges[v].values():
   nxt={}; rhs=visit(child)
   for a,x in out.items():
    for b,y in rhs.items():
     m=a|b;z=x+y
     if z<nxt.get(m,INF):nxt[m]=z
   out=nxt
  return {m:c+(m!=0) for m,c in out.items()}
 f=[INF]*(1<<len(labs))
 for m,c in visit(0).items():f[m]=c
 for j in range(len(labs)):
  for m in range(len(f)):
   if not m&(1<<j): f[m]=min(f[m],f[m|(1<<j)])
 return labs,f

def cost(d,r,subset):
 labs,f=d[r];ind={x:j for j,x in enumerate(labs)}
 return f[sum(1<<ind[x] for x in subset)]

def assignments(d):
 opts={lab:[r for r,(labs,_) in d.items() if lab in labs] for lab in range(24)}
 assert all(opts.values()) and tuple(k for k,v in opts.items() if len(v)>1)==Q
 fixed={x:v[0] for x,v in opts.items() if len(v)==1}
 hist=collections.Counter(); min03=INF; hist03=collections.Counter();maskcost={}
 for a in itertools.product(*(opts[x] for x in Q)):
  buckets={r:[] for r in d}
  for x,r in fixed.items():buckets[r].append(x)
  for x,r in zip(Q,a):buckets[r].append(x)
  v=sum(cost(d,r,buckets[r]) for r in d);hist[v]+=1
  if 3 in a:min03=min(min03,v);hist03[v]+=1
  else:
   m=sum(1<<j for j,r in enumerate(a) if r==7)
   assert m not in maskcost;maskcost[m]=v
 assert len(maskcost)==256
 B=maskcost[0];gap=min(v-B for m,v in maskcost.items() if m)
 sharp=sorted(m for m,v in maskcost.items() if m and v==B+gap)
 return B,gap,sharp,hist,min03,hist03,maskcost

D={}
for i,keys in cases.items():
 grouped=collections.defaultdict(list)
 for k in keys:
  for lab,path in words[k]:grouped[path[0]].append((lab,path))
 D[i]={r:root_table(g) for r,g in sorted(grouped.items())}
base={i:assignments(d) for i,d in D.items()}
assert [base[i][0] for i in (31502,31503,31504)]==[108,106,108]
assert [base[i][1] for i in (31502,31503,31504)]==[8,8,8]
assert [base[i][2] for i in (31502,31503,31504)]==[[21,85,170,191,255],[85,138,170,223,255],[21,85,170,191,255]]
assert [sum(base[i][3].values()) for i in (31502,31503,31504)]==[256,256,1296]
assert [base[i][3][base[i][0]] for i in (31502,31503,31504)]==[1,1,1]
assert base[31504][4]==127 and sum(base[31504][5].values())==1040
assert base[31504][5][127]==2
out={}
for r in (5,6,7):
 a=D[31502][r];b=D[31503][r];c=D[31504][r]
 assert a[0]==b[0] and a==c
 hist=collections.Counter(y-x for x,y in zip(a[1],b[1]))
 assert min(hist)<0 and max(hist)==0
 out[r]=dict(sorted(hist.items()))
assert out=={5:{-3:32,-2:274,-1:580,0:3210},6:{-3:32,-2:273,-1:575,0:3216},7:{-3:4,-2:31,-1:49,0:172}}
diffs=collections.Counter(y-x for x,y in zip(base[31502][6].values(),base[31503][6].values()))
assert diffs=={-4:4,-3:24,-2:63,-1:101,0:64}
print('PASS 31502=108 31503=106 31504=108; unique each')
print('PASS root weak dominance 8448 masks, 1850 strictly improved')
print('PASS 256/256 transfers gap=8 for 31502 and 31503')
print('PASS root03 usage 1040 assignments, min=127, 31504 global min=108')

