#!/usr/bin/env python3
"""Exact all-keys native BRC prefix union for H2/H3 high + H4/H6/H7/H8 low."""
from ec49fgd_mixed_seed_dp import OPS,T,SIG,expand,pref,pool,key,signature,Node
import json
HIGH=('fe','ge','feg','gef')
LOW=(4,6,7,8)
BITS={(h,s):1<<(4*i+j) for i,h in enumerate(LOW) for j,s in enumerate((1,2,4,8))}
def optimize():
 baseline=set().union(*(pref(w) for w in HIGH))
 root=Node();nwords=0
 for h in LOW:
  ps=pool(h);nwords+=len(ps)
  print('input',h,len(ps),flush=True)
  for w,s,k in ps:
   node=root
   for a in expand(w):node=node.children.setdefault(a,Node())
   node.sig |=BITS[h,s];node.word[h,s]=w
 nodes=0;states=0;transitions=0
 def solve(node,pre):
  nonlocal nodes,states,transitions
  nodes+=1
  base={0:(0,{})}
  for label,w in node.word.items():base[BITS[label]]=(0,{label:w})
  for ch,child in node.children.items():
   other=solve(child,pre+(ch,))
   z=0 if pre+(ch,) in baseline else 1
   new={}
   for a,(v,wa) in base.items():
    for b,(w,wb) in other.items():
     transitions+=1
     mask=a|b;score=v+w+(z if b else 0)
     if mask not in new or score<new[mask][0]:new[mask]=(score,wa|wb)
   base=new
  states+=len(base)
  return base
 D=solve(root,())
 cost,ws=D[65535];total=cost+len(baseline)
 pp=set(baseline)
 for (h,s),w in ws.items():
  assert len(w)==h and signature(w)==s and min(key(w))>0
  pp|=pref(w)
 assert len(pp)==total,(total,len(pp))
 return {'model':'H2/H3 high fixed + H4/H6/H7/H8 four low, arbitrary key per low word',
 'baselines':HIGH,'base_prefixes':len(baseline),'pool_words':nwords,
 'trie_nodes':nodes,'dp_states':states,'merges':transitions,
 'extra_edges':cost,'optimum':total,
 'witness':{f'{h}:{s}':w for (h,s),w in sorted(ws.items())},
 'keys':{f'{h}:{s}':key(w) for (h,s),w in sorted(ws.items())}}
if __name__=='__main__':
 d=optimize();print(json.dumps(d,ensure_ascii=False),flush=True)
 with open(__file__.replace('VERIFY_EC49R4_EXACT_DP.py','EXACT_REPORT_EC49R4.json'),'w') as f:json.dump(d,f,indent=2)
