"""Build labelled prefix trie for frozen EC49FCS BRC model, varying H6 signature."""
import json,sys
from pathlib import Path
from frozen_model import W,STEPS,ENC,observe,candidates,primpref
HERE=Path(__file__).resolve().parent
CH={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
assert len(CH)==24
P={k:set(primpref(w)) for k,w in CH.items()}
assert len(set().union(*P.values()))==158

def signed(word):return ''.join(ENC[s] for op in word for s in STEPS[op])

def build(keys,output):
 F=set().union(*(v for k,v in P.items() if k not in keys))
 parent,edge,terminal,children,prefixes=[-1],[0],[0],[{}],['']
 pools={}
 for i,key in enumerate(keys):
  h,sig=map(int,key.split(':'))
  words=candidates(h)[sig]
  assert CH[key] in words
  pools[key]=len(words)
  for word in words:
   v=0
   for ch in signed(word):
    if ch not in children[v]:
     u=len(parent)
     children[v][ch]=u
     parent.append(v);edge.append(int(prefixes[v]+ch not in F))
     terminal.append(0);children.append({});prefixes.append(prefixes[v]+ch)
    v=children[v][ch]
   terminal[v] |= 1<<i
 output.parent.mkdir(exist_ok=True,parents=True)
 with output.open('w') as f:
  f.write(f'{len(parent)} {len(keys)} {len(F)}\n')
  for p,e,t in zip(parent,edge,terminal):f.write(f'{p} {e} {t}\n')
 return dict(keys=keys,fixed_edges=len(F),trie_nodes=len(parent),pool_sizes=pools,input_file=output.name)

def run(out):
 out.mkdir(exist_ok=True,parents=True)
 rows=[]
 # 2 branches x 4 H4 signatures x H6=2; later can extend to 4,8.
 for branch in ['A','B']:
  base=['5:16','7:1','8:2','8:4','9:16'] if branch=='A' else ['5:32','7:1','8:1','8:8','9:32']
  for r in (1,2,4,8):
   keys=[f'4:{r}',base[0],'6:2',*base[1:]]
   rows.append(build(keys,out/f'{branch}_H4_{r}_H6_2.trie.txt'))
 (out/'build_summary.json').write_text(json.dumps(rows,indent=2)+'\n')
 return rows
if __name__=='__main__':print(json.dumps(run(Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'generated'),indent=2))
