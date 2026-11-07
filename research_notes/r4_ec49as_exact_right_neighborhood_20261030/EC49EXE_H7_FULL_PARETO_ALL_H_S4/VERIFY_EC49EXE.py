#!/usr/bin/env python3
"""EC49EXE exact signed native X6 / symbolic BRC witnesses.
Actually executed author-side on 2026-11-03, Python standard library only.
The all-H edge theorem is structural; finite checks do not replace that proof.
"""
import itertools
import json
from fractions import Fraction
from pathlib import Path
OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=(('N',0),('N',1),('N',2),('A',0),('A',2),
       ('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
BASE=('ce','de','ec','ed')
H7_TWO_KEY_WITNESS={
 2:('ce','de','ec','ed'),
 3:('feg','gef'),
 4:('cecc','dedd','eccc','eddd'),
 5:('cecfg','dedgf','eccfg','eddgf'),
 6:('fegfgc','fegfgd','geffgc','geffgd'),
 7:('fegfggf','geffgfg')
}
def path(w):return tuple(s for a in w for s in OPS[a])
def displace(w):
 s=path(w)
 return tuple(s.count(i)-s.count(-i) for i in range(1,7))
def pcount(w):
 s=path(w)
 return tuple(s.count(i) for i in range(1,7))
def signature(w):
 out=[]
 for evt,p in START:
  for t in path(w):
   if p==1 and t==2:
    if evt=='N':evt='A'
    elif evt=='B':evt='BA'
   elif p==2 and t==1:
    if evt=='N':evt='B'
    elif evt=='A':evt='AB'
   p=t
  out.append(BUCKETS.index(evt))
 return tuple(out)
def rank_q(signatures):
 cols=[[int(s[i]==b) for i in range(9)] for s in signatures for b in range(5)]
 if not cols:return 0
 a=[[Fraction(col[i]) for col in cols] for i in range(9)]
 r=0
 for c in range(len(cols)):
  pivot=next((i for i in range(r,9) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  q=a[r][c]
  a[r]=[t/q for t in a[r]]
  for i in range(r+1,9):
   q=a[i][c]
   if q:a[i]=[u-q*v for u,v in zip(a[i],a[r])]
  r+=1
  if r==9:break
 return r
def prefixes(words):
 return {p[:k] for w in words for p in [path(w)] for k in range(1,len(p)+1)}
def witness(H):
 return {h:tuple(w+'g'*(h-2) for w in BASE) for h in range(2,H+1)}
def resources(W):
 ws=[w for v in W.values() for w in v]
 return [len(prefixes(ws)),len({pcount(W[h][0]) for h in W}),len({signature(w) for w in ws})]
def verify():
 assert len(OPS)==7
 first_two={v[:2] for v in OPS.values()}
 assert len(first_two)==7 and all(len(v)>=2 for v in OPS.values())
 positive_op={k:tuple(v.count(i) for i in range(1,7)) for k,v in OPS.items()}
 classes={}
 for k,v in positive_op.items():classes.setdefault(v,[]).append(k)
 assert all(len({OPS[k][0] for k in ks})==len(ks) for ks in classes.values()),classes
 legal2=[''.join(w) for w in itertools.product(sorted(OPS),repeat=2)
         if displace(''.join(w))==(2,0,0,0,0,0)]
 assert len(legal2)==8,(len(legal2),legal2)
 fibers={}
 for w in legal2:fibers.setdefault(pcount(w),[]).append(w)
 rank_fibers={','.join(map(str,k)):rank_q(sorted({signature(w) for w in v}))
              for k,v in fibers.items()}
 p0=pcount('ce');assert set(BASE)==set(fibers[p0]),fibers[p0]
 assert sum(v==9 for v in rank_fibers.values())==1,rank_fibers
 sigs=tuple(signature(w) for w in BASE)
 assert len(set(sigs))==4
 signature_subset_rank={}
 for k in range(1,5):
  vals=[rank_q(x) for x in itertools.combinations(sigs,k)]
  signature_subset_rank[str(k)]=sorted(set(vals))
  assert (k==4)==any(v==9 for v in vals),(k,vals)
 assert len(prefixes(BASE))==28
 sample={}
 for H in range(2,65):
  W=witness(H)
  assert all(all(len(w)==h and displace(w)==(2,0,0,0,0,0) for w in W[h]) for h in W)
  assert all(len({pcount(w) for w in W[h]})==1 for h in W)
  assert all(rank_q([signature(w) for w in W[h]])==9 for h in W)
  r=resources(W);expected=[8*H+12,H-1,4]
  assert r==expected,(H,r,expected)
  if H in (2,3,4,5,6,7,8,16,32,64):sample[str(H)]=r
 W=witness(7)
 h8w={**H7_TWO_KEY_WITNESS,8:tuple(w+'f' for w in H7_TWO_KEY_WITNESS[7])}
 assert resources(H7_TWO_KEY_WITNESS)==[116,2,6]
 assert resources(h8w)==[120,3,6]
 assert all(len({pcount(w) for w in h8w[h]})==1 and
            rank_q({signature(w) for w in h8w[h]})==9 and
            all(displace(w)==(2,0,0,0,0,0) for w in h8w[h]) for h in h8w)
 assert 5+3-1<8
 key_h7={str(h):list(pcount(W[h][0])) for h in W}
 points=[
   (58,5,6),(68,6,4),(72,4,6),(80,5,4),
   (86,3,6),(92,4,4),(116,2,6),(116,3,4)
 ]
 for i,x in enumerate(points):
  assert not any(all(y[j]<=x[j] for j in range(3)) and any(y[j]<x[j] for j in range(3))
                 for k,y in enumerate(points) if k!=i),(i,x)
 return {
  'research_unit':'EC49EXE','status':'PASS',
  'model':'seven prefix-free ordered signed primitive X6 operation codewords',
  'exact_arithmetic':'fractions.Fraction, integer counting, set-trie prefixes',
  'h2_legal_words':legal2,'h2_rank_by_positive_key':rank_fibers,
  'T4_signature_subset_rank_sets':signature_subset_rank,
  'T4_signatures':{w:list(signature(w)) for w in BASE},
  'h2_mandatory_prefix_edges':28,
  'op_positive_step_classes':{str(k):v for k,v in classes.items()},
  'H7_words':{str(h):list(v) for h,v in W.items()},
  'H7_p_by_h':key_h7,
  'H7_resources':resources(W),
  'H8_three_key_witness':{str(h):list(words) for h,words in h8w.items()},
  'H8_resources':resources(h8w),
  'H8_exact_minimum_cache_keys':3,'H8_E_upper_at_M3_S6':120,
  'all_H_witness_checks_H2_to_H64':sample,
  'all_H_family_formula':'(E,M,S)=(8H+12,H-1,4), integer H>=2',
  'H7_nondominated_candidate_points':[list(p) for p in points],
  'inherited_strata_requirements':'Complete H7 frontier also relies on EC49ET,EU,EV,EW,EXC,EXD and EP/EM.'
 }
if __name__=='__main__':
 v=verify()
 out=Path(__file__).with_name('EC49EXE_EXECUTED.json')
 out.write_text(json.dumps(v,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
 print(json.dumps({'status':v['status'],'H7':v['H7_resources'],
 'H2':v['h2_mandatory_prefix_edges'],'tested_upto_H':64,
 'frontier_points':len(v['H7_nondominated_candidate_points']),
 'result_file':str(out)},ensure_ascii=False))
