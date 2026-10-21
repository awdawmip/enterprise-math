"""Python-only coverage obstruction check using exact integer tuples (not C++ clauses)."""
from pathlib import Path
from itertools import combinations
from hashlib import sha256
H=Path(__file__).resolve().parent
D={1,2,64}; Q0={0,1,2,3,4,51,64,71,74}; O=sorted(set(range(84))-Q0)
def delta(n):
 return [(a,b,c,n-a-b-c) for a in range(n+1) for b in range(n-a+1) for c in range(n-a-b+1)]
def sup(x):return sum(t>0 for t in x)
X=delta(8);R=[x for x in X if sup(x)<=2 and x!=(4,4,0,0)];X3=[x for x in X if sup(x)==3]
T=[x for x in delta(16) if sup(x)<=3];assert len(T)==514, len(T)
index={x:i for i,x in enumerate(T)}
add=lambda a,b:tuple(a[i]+b[i] for i in range(4))
base=0
for i,a in enumerate(R):
 for b in R[i:]:
  x=add(a,b)
  if x in index:base|=1<<index[x]
one=[0]*84
for j,q in enumerate(X3):
 for r in R:
  x=add(r,q)
  if x in index:one[j]|=1<<index[x]
pair=[[0]*84 for _ in range(84)]
for i,x in enumerate(X3):
 for j in range(i,84):
  y=add(x,X3[j]);v=1<<index[y] if y in index else 0
  pair[i][j]=pair[j][i]=v
full=(1<<len(T))-1
raw=(H/'distance3_remove1264_180.bin').read_bytes(); assert len(raw)==67525*27
out=bytearray();eligible_rows=[];nonfull=0;rows=0;miss_hist={}
for i,A in enumerate(combinations(O,3)):
 q=sorted((Q0-D)|set(A));assert bytes(q)==raw[i*27:i*27+9]
 m=base
 for x in q:m|=one[x]
 for u,x in enumerate(q):
  for y in q[u:]:m|=pair[x][y]
 missing=full & ~m
 if missing:
  nonfull+=1; k=missing.bit_count();miss_hist[k]=miss_hist.get(k,0)+1
 else:
  out.extend(bytes(q)+bytes(18));eligible_rows.append(i)
 rows+=1
assert rows==67525 and nonfull==66879 and len(eligible_rows)==646,(nonfull,len(eligible_rows))
(H/'eligible_no_support_obstruction_180.bin').write_bytes(out)
(H/'eligible_original_row_numbers_180.txt').write_text('\n'.join(map(str,eligible_rows))+'\n')
print('PREFIX180_PYTHON_SUPPORT_OBSTRUCTION_PASS total=67525 unrecoverable_any_W=66879 support_unobstructed=646')
print('target_support_le3=',len(T),'hist=',miss_hist,'eligible_sha256=',sha256(out).hexdigest())
