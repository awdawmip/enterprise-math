"""EC49FDA author-side exact 228-case certificate verification/replay.
Usage: python REPLAY_EC49FDA.py --check [--literal]
       python REPLAY_EC49FDA.py --recompute [--limit 4]
No external Python libraries. --recompute requires g++ and sibling immutable EC49FCZ sources.
"""
import argparse,base64,gzip,hashlib,itertools,json,subprocess,sys,tempfile
from pathlib import Path
from functools import lru_cache
HERE=Path(__file__).resolve().parent
FCZ=HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'
if not FCZ.is_dir(): FCZ=HERE  # local executed-source staging
sys.path.insert(0,str(FCZ))
import frozen_model as fm
try: import BUILD_EC49FCZ_TRIES as builder
except ImportError: import build as builder
builder.candidates=lru_cache(None)(fm.candidates)
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
SHA256='81c8151d72979553fc044e985d70b132971342085a82f3779ddcfced3f6b34cf'

def slot_keys(row):
 b,r,s,t,fam,ext=(row[x] for x in ('b','r','s','t','family','extra'))
 assert b in ('A','B') and fam in ('H6','H7')
 assert r in (1,2,4,8) and s in (1,2,4,8) and t in (1,2,4,8)
 assert ext in (1,2,4,8) and ext!=(s if fam=='H6' else t)
 base=['5:16',f'6:{s}',f'7:{t}','8:2','8:4','9:16'] if b=='A' else ['5:32',f'6:{s}',f'7:{t}','8:1','8:8','9:32']
 keys=[f'4:{r}',*base,f'{fam[1:]}:{ext}']
 assert len(keys)==8 and len(set(keys))==8
 return keys

def load():
 raw=gzip.decompress(base64.b64decode((HERE/'EC49FDA_228_EXACT_REPORT.json.gz.b64').read_text().strip()))
 assert hashlib.sha256(raw).hexdigest()==SHA256
 report=json.loads(raw)
 assert report['scientific_pin']==PIN
 rows=report['rows']
 assert len(rows)==228
 indices=set()
 for row in rows:
  slot_keys(row)
  assert row['opt']==158 and row['nodes']>0 and row['transitions']>0
  ix=(row['b'],row['r'],row['s'],row['t'],row['family'],row['extra'])
  assert ix not in indices
  assert row['r']==1 or (row['s']==1 and row['t']==1)
  indices.add(ix)
 expected={(b,r,s,t,fam,e) for b in ('A','B') for r in (1,2,4,8)
   for s in (1,2,4,8) for t in (1,2,4,8)
   if (r==1 or (s==1 and t==1))
   for fam in ('H6','H7') for e in (1,2,4,8)
   if e != (s if fam=='H6' else t)}
 assert indices==expected
 return rows

def recompute(rows):
 src=FCZ/'EXACT_PREFIX_TRIE_DP.cpp'
 if not src.exists():src=HERE/'exact_dp.cpp'
 with tempfile.TemporaryDirectory(prefix='ec49fda_') as tmp:
  out=Path(tmp); exe=out/'exact_dp'
  subprocess.run(['g++','-O3','-std=c++17',str(src),'-o',str(exe)],check=True)
  for i,row in enumerate(rows,1):
   path=out/'input.txt'; meta=builder.build(slot_keys(row),path)
   result=json.loads(subprocess.check_output([str(exe),str(path)],text=True))
   assert (result['total_exact_optimum'],result['fixed_edges'],result['trie_nodes'],result['dp_transitions'])==(row['opt'],row['fixed'],row['nodes'],row['transitions'])
   assert list(meta.get('pool_sizes',meta.get('candidate_counts')).values())==row['pool']
   if i%32==0:print('recomputed',i,flush=True)
 print('FULL-LANGUAGE EXACT REPLAY PASS',len(rows))

def literal(rows):
 ch={f'{h}:{fm.observe(w)}':w for h,ws in fm.W.items() for w in ws}
 p={k:frozenset(fm.primpref(w)) for k,w in ch.items()}
 assert len(frozenset().union(*p.values()))==158
 pool={k:fm.candidates(int(k.split(':')[0]))[int(k.split(':')[1])] for k in ch if int(k.split(':')[0])>=4}
 opts={k:[frozenset(fm.primpref(w)) for w in ([ch[k]]+[w for w in words if w!=ch[k]][:2])] for k,words in pool.items()}
 assert all(len(v)==3 for v in opts.values())
 checked=0
 for row in rows:
  keys=slot_keys(row)
  fixed=frozenset().union(*(v for k,v in p.items() if k not in keys))
  assert len(fixed)==row['fixed']
  best=1000000
  for choices in itertools.product(range(3),repeat=8):
   z=fixed
   for key,i in zip(keys,choices):z=z|opts[key][i]
   best=min(best,len(z));checked+=1
  assert best==158
 print('RESTRICTED LITERAL AUDIT PASS',checked,'combinations (not full-language independent proof)')

if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--check',action='store_true');p.add_argument('--recompute',action='store_true')
 p.add_argument('--literal',action='store_true');p.add_argument('--limit',type=int,default=None)
 args=p.parse_args()
 rows=load();print('CERTIFICATE HASH AND COVERAGE PASS:',len(rows))
 if args.literal:literal(rows)
 if args.recompute:recompute(rows[:args.limit] if args.limit else rows)
