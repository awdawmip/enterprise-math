#!/usr/bin/env python3
"""Independent finite root/terminal grouping from complete original BRC profile CSV."""
import csv,hashlib,itertools,collections
from pathlib import Path
P=Path(__file__).resolve().parent
source=P/'master_and_radius3_cases.txt'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
roots=(3,5,6,7)
with source.open() as f:
 nk,nw,nc=map(int,f.readline().split());assert (nk,nw,nc)==(94,178850,38169)
 fam=[]
 for _ in range(nk):
  n=int(f.readline());d={r:0 for r in roots}
  for _ in range(n):
   label,word=f.readline().split();d[int(word[:2],16)]|=1<<int(label)
  fam.append(d)
 cases=[tuple(map(int,f.readline().split())) for _ in range(nc)]
assert len(set(cases))==nc

def domain(c):
 e=[0]*24
 for key in c:
  for j,r in enumerate(roots):
   mask=fam[key][r]
   while mask:
    bit=mask&-mask; e[bit.bit_length()-1]|=1<<j;mask^=bit
 return tuple(e)
base=set(cases[32315]);expected=domain(cases[32315]);ids={i for i,c in enumerate(cases) if len(base-set(c))<=3 and domain(c)==expected}
assert len(ids)==966
choices={i:tuple(roots[j] for j in range(4) if expected[i]>>j&1) for i in range(24) if expected[i].bit_count()>1}
assert choices=={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),17:(3,6,7),19:(3,5,7),21:(3,6,7)}
rows=collections.defaultdict(dict)
with (P/'EC49FOQ_PROFILES.csv').open() as f:
 for row in csv.DictReader(f):
  c,r,m,o,s,v=(int(row[k]) for k in ('config','root','must','opt','subset','cost'))
  assert c in ids and r in roots
  a=rows[(c,r)];assert s not in a
  a[s]=v
assert len(rows)==966*4 and sum(map(len,rows.values()))==162288
all_assign=list(itertools.product(*(choices[i] for i in choices)))
assert len(all_assign)==648
terms=collections.defaultdict(list);profiles=collections.defaultdict(list)
for c in sorted(ids):
 p=tuple((r,s,v) for r in roots for s,v in sorted(rows[(c,r)].items()))
 assert len(p)==168
 t=[]
 for assignment in all_assign:
  masks={r:0 for r in roots}
  for label,r in zip(choices,assignment):masks[r]|=1<<label
  t.append(sum(rows[(c,r)][masks[r]] for r in roots))
 terms[tuple(t)].append(c);profiles[p].append(c)
assert len(terms)==len(profiles)==427
assert sum(len(v)*(len(v)-1)//2 for v in terms.values())==10702
assert sum(len(v)*(len(v)-1)//2 for v in profiles.values())==10702
for members in terms.values():
 assert len({tuple((r,s,v) for r in roots for s,v in sorted(rows[(c,r)].items())) for c in members})==1
assert len(next(m for m in terms.values() if 32315 in m))==38
print('PASS 966 configs; 162288 exact root entries; 648 assignments; 427 groups; 10702 equal pairs; 0 gauges')
