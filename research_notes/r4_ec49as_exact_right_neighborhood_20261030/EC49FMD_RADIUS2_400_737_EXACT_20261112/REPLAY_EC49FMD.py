#!/usr/bin/env python3
"""Frozen BRC radius-two exact scan indices 400..737; Python 3 + g++ C++17.
Default: verify finite input census & stored 338-row vector.
--run-all: additionally reproduce all 338 exact prefix-trie optima.
"""
import base64,collections,hashlib,itertools,json,subprocess,sys,tempfile,zlib
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parent
sys.path.insert(0,str(ROOT/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,pref,raw_key
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
E=json.loads((P/'EXACT_VECTOR_EC49FMD.json').read_text())
assert E['model_pin']==PIN and E['global_slice']==[400,738] and E['count']==338
raw=zlib.decompress(base64.b64decode(E['rows_zlib_b64']))
assert hashlib.sha256(raw).hexdigest()==E['rows_sha256']
rows=[tuple(map(int,line.split())) for line in raw.decode().splitlines()]
assert len(rows)==338 and [r[0] for r in rows]==list(range(338))
assert min(r[1] for r in rows)==98 and max(r[1] for r in rows)==184
assert collections.Counter(str(r[1]) for r in rows)==E['histogram']
assert [400+i for i,c,*_ in rows if c==98]==[588,673]

cat=list(all_words());labs=sorted({x for x,_ in cat})
assert len(cat)==178850 and len(labs)==24
label_id={x:i for i,x in enumerate(labs)}
by_key=collections.defaultdict(list);support=collections.defaultdict(int)
for label,w in cat:
 k=raw_key(w);i=label_id[label]
 by_key[k].append((i,pref(w)[-1].hex()));support[k]|=1<<i
assert len(support)==94 and BASE.issubset(support)
outside=sorted(set(support)-BASE);old=sorted(BASE);full=(1<<24)-1
sets=[]
for dropped in itertools.combinations(old,2):
 for added in itertools.combinations(outside,2):
  K=sorted(BASE-set(dropped)|set(added))
  mask=0
  for k in K:mask|=support[k]
  if mask==full:sets.append(K)
assert len(sets)==6315
print('EC49FMD_INDEX_AND_VECTOR_PASS',len(cat),len(support),len(sets),len(rows),flush=True)
if '--run-all' in sys.argv:
 with tempfile.TemporaryDirectory() as td:
  td=Path(td)
  with (td/'input.txt').open('w') as f:
   f.write('338\n')
   for K in sets[400:738]:
    words=[r for k in K for r in by_key[k]]
    f.write(str(len(words))+'\n')
    for i,path in words:f.write(f'{i} {path}\n')
  solver=ROOT/'EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112'/'SCAN_7KEY_GENERAL.cpp'
  subprocess.run(['g++','-O3','-std=c++17',str(solver),'-o',str(td/'scan')],check=True)
  with (td/'input.txt').open('rb') as inp, (td/'out.txt').open('wb') as out:
   subprocess.run([str(td/'scan')],stdin=inp,stdout=out,check=True)
  got=[]
  for line in (td/'out.txt').read_text().splitlines():
   z=line.split()
   assert len(z)==5 and z[-1].endswith(',') and len(z[4].split(','))-1==int(z[3])
   got.append(tuple(map(int,z[:4])))
  assert got==rows,(len(got),next((i for i,(a,b) in enumerate(zip(got,rows)) if a!=b),None))
  print('EC49FMD_ALL_338_EXACT_REPLAY_PASS',flush=True)
