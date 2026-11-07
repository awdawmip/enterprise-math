from pathlib import Path
from itertools import combinations

import json,time,sys
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ENC={-1:'a',1:'A',-2:'b',2:'B',-3:'c',3:'C'}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
W={2:('fe','ge'),3:('feg','gef'),4:('degf','fegd','cefg','gefc'),5:('feggf','geffg'),6:('aeeddd','dedead','aeeccc','ceceac'),7:('aeeddgf','dedeagf','aeeccfg','ceceafg'),8:('feggfead','geffgaed','geffgaec','feggfeac'),9:('feggfeafg','geffgaegf')}
def observe(w):
 s=0
 for op in w:
  s=T[s][OPS.index(op)]
  if s==8:return None
 return SIG[s]
def primpref(w):
 s=''.join(ENC[i] for op in w for i in STEPS[op]);return tuple(s[:k] for k in range(1,len(s)+1))
def candidates(h):
 x,y,z=(4,2,1) if h<=5 else (7,3,2)
 b=x+y-h-1; a=z-1;f=x-b-2*z;g=y-b
 assert min(a,b,f,g)>=0
 out={sig:[] for sig in REQ[h]}
 for c in range(b+1):
  m={'a':a,'c':c,'d':b-c,'e':z,'f':f,'g':g}
  def visit(word,state):
   if len(word)==h:
    if SIG[state] in out:out[SIG[state]].append(word)
    return
   for k,op in enumerate(OPS):
    if m[op] and T[state][k]!=8:
     m[op]-=1;visit(word+op,T[state][k]);m[op]+=1
  visit('',0)
 return out

def build():
 t=time.perf_counter()
 chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
 early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
 late=[f'{h}:{s}' for h in (7,8,9) for s in REQ[h]]
 pools={}
 for h in range(4,10):
  for sig,words in candidates(h).items():
   pools[f'{h}:{sig}']=words
   assert chosen[f'{h}:{sig}'] in words
 allwords=set(chosen.values())|{w for p in pools.values() for w in p}
 prefs={w:primpref(w) for w in allwords}
 prefix_ids={p:i for i,p in enumerate(sorted({p for ps in prefs.values() for p in ps}))}
 bits={w:sum(1<<prefix_ids[p] for p in prefs[w]) for w in allwords}
 witness=0
 for w in chosen.values():witness|=bits[w]
 assert witness.bit_count()==158
 masks={key:[bits[w] for w in words] for key,words in pools.items()}
 single={key:bits[w] for key,w in chosen.items()}
 print('BUILT',len(allwords),len(prefix_ids),'time',round(time.perf_counter()-t,2),flush=True)
 return chosen,early,late,masks,single

FROZEN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
SOURCE='452ba5628c4c0fb9c2e67d6dead3d74b53a10cf4'
BASELINE=158
def run():
    t=time.perf_counter()
    chosen,early,late,pools,single=build()
    assert len(chosen)==24 and len(early)==10 and len(late)==10
    sizes={k:len(pools[k]) for k in sorted(pools)}
    assert sizes=={'4:1':12,'4:2':12,'4:4':12,'4:8':12,
      '5:16':12,'5:32':12,'6:1':30,'6:2':30,'6:4':30,'6:8':30,
      '7:1':540,'7:2':720,'7:4':540,'7:8':720,
      '8:1':1890,'8:2':3150,'8:4':1890,'8:8':3150,
      '9:16':1680,'9:32':1680}
    combined=[(*e,*l) for e in combinations(early,1) for l in combinations(late,2)] + list(combinations(late,3))
    assert len(combined)==570
    summary=[]
    all_raw=0; all_reduced=0; all_pair_pruned=0;empty_slot=0;min_cost=10**9; improved=[]
    for idx,slots in enumerate(combined):
        rest=0
        for key,v in single.items():
            if key not in slots:rest|=v
        base=rest.bit_count(); cut=BASELINE-base
        filtered=[[(v & ~rest) for v in pools[key] if (v & ~rest).bit_count()<cut] for key in slots]
        raw=1
        for key in slots:raw*=len(pools[key])
        all_raw+=raw
        order=sorted(range(3),key=lambda j:len(filtered[j]))
        a,b,c=(filtered[j] for j in order)
        checked=0;pairpruned=0;best=BASELINE
        for x in a:
            for y in b:
                q=x|y
                if q.bit_count()>=cut:
                    pairpruned+=1
                    continue
                for z in c:
                    checked+=1
                    cost=base+(q|z).bit_count()
                    if cost<best: best=cost
        min_cost=min(min_cost,best)
        if best<BASELINE: improved.append({'slots':slots,'cost':best})
        all_pair_pruned+=pairpruned
        all_reduced+=checked
        if not (a and b and c):empty_slot+=1
        summary.append({'slots':list(slots),'rest_edges':base,'cut':cut,
            'original_candidate_counts':[len(pools[key]) for key in slots],
            'strict_improvement_candidates':[len(x) for x in filtered],
            'filtered_pair_pruned':pairpruned,'filtered_triples_evaluated':checked,
            'local_minimum':best})
        if (idx+1)%100==0:print('progress',idx+1,'seconds',round(time.perf_counter()-t,1),flush=True)
    data={'schema':'EC49FBY_ALL_REMAINING_TRIPLES_EXACT_V1',
          'date':'2026-11-06','frozen_science_pin':FROZEN,'source_branch_head':SOURCE,
          'baseline_source_commit':'b3b43ef6abe2fd816d979792d18a67ee5d0aad50',
          'model':'9-state DFA over acdefg, native signed X6 primitive prefixes, exact positive BRC keys',
          'cache_keys':{'H4_H5':[4,2,1,0,0,0],'H6_H9':[7,3,2,0,0,0]},
          'baseline_edges':BASELINE,'source_witness_words':{str(k):list(v) for k,v in W.items()},
          'candidate_counts':sizes,'groups':len(combined),
          'all_cartesian_combinations':all_raw,
          'after_single_and_pair_pruning_evaluated':all_reduced,
          'filtered_candidate_pairs_pruned':all_pair_pruned,
          'groups_with_empty_strict_candidate_slot':empty_slot,
          'minimum_over_all_groups':min_cost,'improvements':improved,
          'proof_scope':'Fixed 24 signature slots, H2/H3, L/M keys and frozen DFA. Exactly three replaced slots with at least two late slots.',
          'per_group':summary}
    out=Path(__file__).with_name('EXACT_REPORT_EC49FBY.json')
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('SUMMARY',json.dumps({k:v for k,v in data.items() if k not in ('source_witness_words','per_group')},ensure_ascii=False,indent=2),flush=True)
    print('TOTAL_SEC',round(time.perf_counter()-t,3),flush=True)
    return data
if __name__=='__main__':run()
