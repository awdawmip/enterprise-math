#!/usr/bin/env python3
"""R744 exact exhaustive checker. Only Python standard library, all-integer state."""
import json
from itertools import product
from collections import Counter

ROOT='012'
NETWORKS={
 'A':{
  'I':('012','014','013','012'),
  'P':('012','023','013','012'),
  'Q':('012','023','123','012')},
 'B':{
  'I':('012','123','124','012'),
  'P':('012','023','013','012'),
  'Q':('012','123','013','012')},
}
# Canonical R741 named V17 generator maps; array p[i] of images of 0,1,2.
PERM={
 'A':{'I':(0,1,2),'P':(0,2,1),'Q':(1,0,2)},
 'B':{'I':(0,1,2),'P':(0,2,1),'Q':(2,1,0)},
}
WITNESSES=('III','IIP','IIQ','IPQ','IQP','PQP')
EXPECTED={
 'A':('012','021','102','201','120','210'),
 'B':('012','021','210','120','201','102'),
}

def cmp(p,q): return tuple(p[q[i]] for i in range(3))
def pword(network,word):
 p=(0,1,2)
 for c in word: p=cmp(p,PERM[network][c])
 return ''.join(map(str,p))

def pulse(b, direction):
 a,z=b
 if direction=='F': a,z=a-1,z+1
 else: a,z=a+1,z-1
 assert 0<=a<=2 and 0<=z<=2
 return (a,z)

def graphs(name):
 loops=NETWORKS[name]
 arcs=sorted({(loop[i],loop[i+1]) for loop in loops.values() for i in range(3)})
 assert len(arcs)==7
 assert all(len(set(loop[:3]))==3 and loop[-1]==ROOT for loop in loops.values())
 out=Counter(a for a,b in arcs)
 assert sum(v==2 for v in out.values())==2
 assert len(arcs)==7
 # Two sources have two outgoing arcs; the other three sources have one.
 assert sorted(out.values())==[1,1,1,2,2], (name,dict(out))
 roots={loop[1] for loop in loops.values()}
 assert len(roots)==2
 # No generator nonbacktracking at a seam: first targets and last sources disjoint.
 assert set(loop[-2] for loop in loops.values()).isdisjoint(roots)
 return loops,arcs

def source_injective(arcs,labs):
 by={}
 for (a,b),d in zip(arcs,labs):
  by.setdefault(a,[]).append(d)
 return all(len(x)==len(set(x)) for x in by.values())

def stock_blind_generator(seq,code):
 # One identity PASS after arc 1: its label is inverse of the first PASS,
 # irrespective of which next arc will be selected.
 dirs=[code[(seq[i],seq[i+1])] for i in range(3)]
 helper={'F':'R','R':'F'}[dirs[0]]
 pulses=(dirs[0],helper,dirs[1],dirs[2])
 b=(1,1); states=[b]
 for p in pulses:
  b=pulse(b,p)
  states.append(b)
 assert b==(1,1)
 assert Counter(pulses)==Counter({'F':2,'R':2})
 return pulses,states

def main():
 outcome={'schema':'R744_BRANCH_BLIND_STOCK_ONLY_VERIFY_V1','result':'PASS','integer_semantics':'exact','cases':{}}
 for name in 'AB':
  loops,arcs=graphs(name)
  candidate=[]; valid=[]
  for bits in product('FR', repeat=7):
   if not source_injective(arcs,bits): continue
   candidate.append(bits)
   code=dict(zip(arcs,bits))
   # Arc 2 and arc 3 must be opposite after the first arc/helper cancel.
   good=all(code[(seq[1],seq[2])]!=code[(seq[2],seq[3])] for seq in loops.values())
   if not good: continue
   valid.append(code)
  assert len(candidate)==32, (name,len(candidate))
  assert len(valid)==4, (name,len(valid))
  local={'arcs':['>'.join(a) for a in arcs], 'injective_codebooks':32,'stock_blind_codebooks':4,
         'verified_history_count':0,'codebooks':[]}
  for code in valid:
   gen={g:stock_blind_generator(seq,code)[0] for g,seq in loops.items()}
   first={g:gen[g][0] for g in 'IPQ'}
   assert len({first['I'],first['P'],first['Q']})==2
   assert {gen[g][0] for g in 'IPQ'}=={'F','R'}
   first_hop_to_helper={}
   for g,seq in loops.items():
    node=seq[1]; h=gen[g][1]
    if node in first_hop_to_helper: assert first_hop_to_helper[node]==h
    first_hop_to_helper[node]=h
   assert len(first_hop_to_helper)==2
   assert {g:gen[g][1] for g in 'IPQ'} == {g: {'F':'R','R':'F'}[gen[g][0]] for g in 'IPQ'}
   checked=0
   for k in range(9):
    for word in product('IPQ',repeat=k):
     w=''.join(word); b=(1,1); M={'F':0,'R':0}; s=(0,1,2)
     for g in word:
      s=cmp(s,PERM[name][g])
      for d in gen[g]:
       b=pulse(b,d);M[d]+=1
      assert b==(1,1)
     assert M=={'F':2*k,'R':2*k}
     assert s==tuple(int(c) for c in pword(name,w))
     checked+=1
   assert checked==sum(3**k for k in range(9))==9841
   local['verified_history_count']+=checked
   local['codebooks'].append({
     'arc_labels':{'>'.join(a):code[a] for a in arcs},
     'generator_pass_words':{g:''.join(gen[g]) for g in 'IPQ'},
     'first_hop_vertex_helper':first_hop_to_helper,
     'histories_0_to_8':checked})
  assert local['verified_history_count']==4*9841
  rels=tuple(pword(name,w) for w in WITNESSES)
  assert rels==EXPECTED[name]
  assert len(set(rels))==6
  local['twelve_PASS_six_relation_witnesses']=dict(zip(WITNESSES,rels))
  local['common_ledger_for_three_generators']={'M01':6,'M10':6,'b0':1,'b1':1,'Gamma':12}
  outcome['cases'][name]=local
 outcome['total_codebooks']=8
 outcome['total_histories_checked']=sum(x['verified_history_count'] for x in outcome['cases'].values())
 assert outcome['total_histories_checked']==78728
 return outcome

if __name__=='__main__':
 print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
