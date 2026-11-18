"""Independent direct-string enumeration cross-check for 64 small frozen BRC seven-slot submodels.
For each selected signature, restrict each legal candidate pool to its first and last word;
then compare brute-force 2^7 labelled choices and common-prefix trie DP.
The exact 128 full-language results are separately certified by RUN_EC49FCZ.py.
"""
from itertools import product
from pathlib import Path
import json, subprocess
from frozen_model import W,observe,primpref,candidates,ENC,STEPS

HERE=Path(__file__).resolve().parent
CH={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
P={key:set(primpref(w)) for key,w in CH.items()}
assert len(CH)==24 and len(set().union(*P.values()))==158

def signed(w):return ''.join(ENC[s] for op in w for s in STEPS[op])
def check(keys,outfile):
 fixed=set().union(*(v for k,v in P.items() if k not in keys))
 pools=[]
 for key in keys:
  h,s=map(int,key.split(':'))
  source=candidates(h)[s]
  assert CH[key] in source and len(source)>=2
  pools.append((source[0],source[-1]))
 brute=min(len(fixed.union(*(primpref(w) for w in ws))) for ws in product(*pools))
 parents=[-1]; costs=[0]; ends=[0]; children=[{}]; strings=['']
 for j,words in enumerate(pools):
  for w in words:
   v=0
   for c in signed(w):
    if c not in children[v]:
     u=len(parents);children[v][c]=u
     parents.append(v); p=strings[v]+c;strings.append(p)
     costs.append(int(p not in fixed));ends.append(0);children.append({})
    v=children[v][c]
   ends[v]|=(1<<j)
 with outfile.open('w') as f:
  f.write(f'{len(parents)} {len(keys)} {len(fixed)}\n')
  for p,c,e in zip(parents,costs,ends): f.write(f'{p} {c} {e}\n')
 got=json.loads(subprocess.check_output([str(HERE/'exact_dp'),str(outfile)],text=True))
 outfile.unlink()
 assert got['total_exact_optimum']==brute,(keys,got,brute)
 return brute

def main():
 results=[];scratch=HERE/'submodel.trie.txt'
 for branch in ('A','B'):
  base=(['5:16','8:2','8:4','9:16'] if branch=='A' else
        ['5:32','8:1','8:8','9:32'])
  for h4 in (1,8):
   for h6 in (1,2,4,8):
    for h7 in (1,2,4,8):
     keys=[f'4:{h4}',base[0],f'6:{h6}',f'7:{h7}',*base[1:]]
     optimum=check(keys,scratch)
     results.append({'branch':branch,'h4':h4,'h6':h6,'h7':h7,'subset_pool_size':2,'brute_optimum':optimum,'trie_matches':True})
 out={'schema':'EC49FCZ_64_RESTRICTED_CROSSCHECK_V1','model':'64 seven-slot submodels, two candidates per selected slot (first and last), independent literal prefix enumeration versus compiled trie DP','cases':results}
 (HERE/'EC49FCZ_64_SUBMODEL_CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n')
 print('ALL_MATCH',len(results),'brute_optima',sorted(set(z['brute_optimum'] for z in results)))
if __name__=='__main__':main()
