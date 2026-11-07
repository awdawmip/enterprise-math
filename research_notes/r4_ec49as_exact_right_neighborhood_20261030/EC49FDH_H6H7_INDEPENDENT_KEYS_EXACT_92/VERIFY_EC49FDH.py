#!/usr/bin/env python3
"""Check EC49FDH literal signed-native witness and exact 20-label key-pair model."""
from pathlib import Path
import sys,json,hashlib,tempfile,subprocess,argparse
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FDG_WINDOW_SPLIT_LATE_KEY_800_106'))
import VERIFY_EC49FDG as V
fixed=set().union(*(V.prefixes(w) for w in V.FIXED.values()))
assert len(fixed)==16
data=json.loads((P/'WITNESS_92.json').read_text())
words=data['label_words']
keys={int(h):tuple(k) for h,k in data['keys'].items()}
assert len(words)==24
for label,w in words.items():
 h,s=map(int,label.split(':'))
 assert len(w)==h and V.observe(w)==s
 if h<=3: assert V.FIXED[label]==w
 else: assert w in V.language(h,keys[h])[s]
pre=set().union(*(V.prefixes(w) for w in words.values()))
assert len(pre)==92
assert hashlib.sha256(('\n'.join(sorted(pre))+'\n').encode()).hexdigest()==data['direct_prefix_sha256']
print('verified signed-native 24-label witness: 92 distinct nonempty prefixes')
ap=argparse.ArgumentParser();ap.add_argument('--solver');ap.add_argument('--all',action='store_true')
a=ap.parse_args()
if a.solver:
 def cost(k6,k7):
  pool={f'{h}:{s}':ww for h in range(4,10) for s,ww in
        V.language(h,{4:V.L,5:V.L,6:k6,7:k7,8:(6,5,1),9:V.M}[h]).items()}
  assert len(pool)==20 and all(pool.values())
  parent,weight,term=V.build(pool,fixed)
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/'trie'
   with p.open('w') as out:
    out.write(f'{len(parent)} 20 16\n')
    for x,y,z in zip(parent,weight,term):out.write(f'{x} {y} {z}\n')
   cp=subprocess.run([a.solver,str(p),'500'],capture_output=True,text=True,check=True)
   report=json.loads(cp.stdout)
  return report['total_exact_optimum'],report['inspected_pairs'],len(parent),sum(map(len,pool.values()))
 v=cost((5,3,1),(6,4,1))
 assert v==(92,25815852,30059,5612),v
 print('verified complete exact 20-label instance:',v)
 if a.all:
  ks6=[k for k,_ in V.feasible_keys(6)]
  ks7=[k for k,_ in V.feasible_keys(7)]
  assert len(ks6)==22 and len(ks7)==34
  rows=['H7='+' '.join(','.join(map(str,k)) for k in ks7)]
  total=0;maxnodes=0;best=999;minima=[]
  for k6 in ks6:
   values=[]
   for k7 in ks7:
    value,checks,nodes,_=cost(k6,k7)
    values.append(value);total+=checks;maxnodes=max(maxnodes,nodes)
    if value<best:best=value;minima=[(k6,k7)]
    elif value==best:minima.append((k6,k7))
   rows.append(','.join(map(str,k6))+' '+' '.join(map(str,values)))
  table='\n'.join(rows)+'\n'
  import gzip,base64
  original=gzip.decompress(base64.b64decode((P/'MATRIX_H6_H7_748.txt.gz.b64').read_text()))
  assert table.encode()==original
  assert total==12424911386 and maxnodes==52372 and best==92 and len(minima)==2
  print('verified full 748 table; minima:',minima,'inspected:',total)
