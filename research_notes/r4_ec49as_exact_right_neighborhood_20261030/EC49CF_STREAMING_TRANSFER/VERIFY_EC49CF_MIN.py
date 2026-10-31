"""EC49CF executable exact certificate. Run in EC49CF_STREAMING_TRANSFER.
Uses preceding PR's original native BRC; only Python integer arithmetic.
"""
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49CA_CRT'))
from native_signed_brc import endpoint_weight,endpoint_multiplicity
S=(1,2,3,4,5,6,-6,-5,-4,-3,-2,-1)
G=((0,0),(1,0),(0,1),(1,1));Z=(0,)*6
W0=(2,3,3,2,1,1);W1=(3,2,3,2,1,1)
W={a:(W0[a-1],W1[a-1],1) if a>0 else (1,1,1) for a in S}
def letter(a,g):
 i=abs(a)
 if g[0] and i in (1,2):i=3-i
 if g[1] and i in (5,6):i=11-i
 return i if a>0 else -i
def sub(q,a):return 2 if q==2 or (q==1 and a==2) else int(a==1)
SW=tuple(q%3*3+q//3 for q in range(9))
ATOM=tuple(2*(q//3==2)+(q%3==2) for q in range(9))
D={a:tuple(3*sub(q//3,a)+sub(q%3,letter(a,(1,0))) for q in range(9)) for a in S}
def act(k,g):
 z,q=k
 if g[0]:z=(z[1],z[0],z[2],z[3],z[4],z[5]);q=SW[q]
 if g[1]:z=z[:4]+(z[5],z[4])
 return z,q
def swap(v,g):return (v[1],v[0],v[2]) if g[0] else v
def step(k,a):
 z,q=k;i=abs(a)-1
 return z[:i]+(z[i]+(1 if a>0 else -1),)+z[i+1:],D[a][q]
def norm(k):return sum(abs(v) for v in k[0])
def add(out,k,v):
 old=out.get(k,(0,0,0));out[k]=(old[0]+v[0],old[1]+v[1],old[2]+v[2])
def full(src,rem):
 out={}
 for k,v in src.items():
  for a in S:
   d=step(k,a)
   if norm(d)>rem:continue
   w=W[a];add(out,d,(w[0]*v[0],w[1]*v[1],v[2]))
 return out
def stream(src,rem):
 out={}
 for r,v in src.items():
  Hr=tuple(g for g in G if act(r,g)==r);seen_letters=set()
  for a in S:
   if a in seen_letters:continue
   seen_letters.update(letter(a,h) for h in Hr)
   y=step(r,a)
   if norm(y)>rem:continue
   candidates=[(act(y,g),g) for g in G]
   d=min(k for k,g in candidates)
   E=tuple(h for h in Hr if letter(a,h)==a)
   seen_g=set();w=W[a]
   weighted=(w[0]*v[0],w[1]*v[1],v[2])
   for k,g in candidates:
    if k!=d or g in seen_g:continue
    seen_g.update((g[0]^e[0],g[1]^e[1]) for e in E)
    add(out,d,swap(weighted,g))
 return out
def lift(src):
 out={}
 for r,v in src.items():
  for g in G:
   k=act(r,g);w=swap(v,g)
   assert k not in out or out[k]==w
   out[k]=w
 return out
def terminal(src):
 t=[[0,0,0] for _ in range(4)]
 for (z,q),v in src.items():
  assert z==Z
  for i in range(3):t[ATOM[q]][i]+=v[i]
 return t
rows=[]
for n in range(0,17,2):
 f={(Z,0):(1,1,1)};r=dict(f);peak=(1,1)
 for j in range(n+1):
  assert lift(r)==f,(n,j)
  peak=(max(peak[0],len(f)),max(peak[1],len(r)))
  if j<n:
   f=full(f,n-j-1);r=stream(r,n-j-1)
 t=terminal(f)
 nw=int(endpoint_weight(n,Z,W0,(1,)*6));nc=endpoint_multiplicity(n,Z)
 assert tuple(sum(row[i] for row in t) for i in range(3))==(nw,nw,nc)
 rows.append(dict(n=n,all_layers_equal=True,terminal=t,peak_full=peak[0],peak_orbit=peak[1],native_weight=nw,native_count=nc))
 print('PASS',n,peak,flush=True)
p=(Z,0)
for a in (3,3):p=step(p,a)
assert p[0]!=(0,)*6
prefix={p:(9,9,1)}
assert {k:v for k,v in prefix.items() if k[0]==Z}=={}
for a in (-3,-3):
 k,v=next(iter(prefix.items()));prefix={step(k,a):v}
assert prefix=={(Z,0):(9,9,1)}
report={'schema':'EC49CF_EXACT_STREAMING_CERTIFICATE_V1','scope':'fixed n, exact signed X6, 9-state AB DFA, two covariant BRC instruments plus count, K=C2xC2',
 'cases':rows,'future_horizon_counterexample':{'prefix':'+E3,+E3','suffix':'-E3,-E3','same_closed_projection_as_empty':True,'suffix_counts':[9,9,1]}}
(P/'EXACT_REPORT_EC49CF_MIN.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('EC49CF_ALL_PASS')
