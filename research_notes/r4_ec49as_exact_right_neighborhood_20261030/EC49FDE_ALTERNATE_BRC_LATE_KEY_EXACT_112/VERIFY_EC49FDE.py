"""Independent Python full-language signed-prefix builder + sparse-mask DP.

This checker constructs a fresh literal-string trie from frozen primitive words
without the C++ builder's serialized parent/edge format and independently solves
all twenty H4..H9 label choices under an explicitly changed late cache key. It checks EXACTLY the typed objective with L=(4,2,1), changed M=(6,4,1).
"""
from functools import lru_cache
from time import perf_counter
import json,hashlib,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128'))
import frozen_model as fm
# EC49FDE changed-key experiment, retaining all source observer / primitive laws.
# The original frozen-model source is imported unchanged by the upstream verifier.
NEW_LATE_KEY=(6,4,1)
def changed_candidates(h):
    x,y,z=(4,2,1) if h<=5 else NEW_LATE_KEY
    b=x+y-h-1; a=z-1; f=x-b-2*z; g=y-b
    if min(a,b,f,g)<0: return {sig:[] for sig in fm.REQ[h]}
    out={sig:[] for sig in fm.REQ[h]}
    for count_c in range(b+1):
        m={'a':a,'c':count_c,'d':b-count_c,'e':z,'f':f,'g':g}
        def visit(word,state):
            if len(word)==h:
                if fm.SIG[state] in out: out[fm.SIG[state]].append(word)
                return
            for j,op in enumerate(fm.OPS):
                if m[op] and fm.T[state][j]!=8:
                    m[op]-=1
                    visit(word+op,fm.T[state][j])
                    m[op]+=1
        visit('',0)
    return out
fm.candidates=lru_cache(None)(changed_candidates)


CH={f'{h}:{fm.observe(w)}':w for h,ws in fm.W.items() for w in ws}
assert len(CH)==24
keys=[f'{h}:{sig}' for h in (4,5,6,7,8,9) for sig in fm.REQ[h]]
assert len(keys)==20
fixed=set().union(*(set(fm.primpref(word)) for k,word in CH.items() if k not in keys))
assert len(fixed)==16
original=set().union(*(set(fm.primpref(w)) for w in CH.values()))
assert len(original)==158
# Exact 24-label witness: H2/H3 stay original, all H4..H9 labels choose
# words admissible under the changed key. 112 = count of native prefixes.
WITNESS={"4:1":"gefd","4:2":"fegd","4:4":"fegc","4:8":"gefc","5:16":"feggf","5:32":"geffg","6:1":"gefddd","6:2":"fegddd","6:4":"fegccc","6:8":"gefccc","7:1":"gefddgf","7:2":"fegddgf","7:4":"fegccfg","7:8":"gefccfg","8:1":"geffggfd","8:2":"feggffgd","8:4":"feggffgc","8:8":"geffggfc","9:16":"feggffgfg","9:32":"geffggffg"}
assert len(WITNESS)==20
for lab,w in WITNESS.items():
    h,sig=map(int,lab.split(':'))
    assert len(w)==h and fm.observe(w)==sig and w in fm.candidates(h)[sig]
all_witness=dict((k,w) for k,w in CH.items() if k.startswith('2:') or k.startswith('3:'))
all_witness.update(WITNESS)
assert len(all_witness)==24
witness_prefixes=set().union(*(set(fm.primpref(w)) for w in all_witness.values()))
assert len(witness_prefixes)==112

children=[{}];ends=[0];edge=[0];pool={}
start=perf_counter()
for i,key in enumerate(keys):
    h,sig=map(int,key.split(':')); words=fm.candidates(h)[sig]
    assert words
    pool[key]=len(words)
    for w in words:
        node=0
        for prefix in fm.primpref(w):
            c=prefix[-1]
            nxt=children[node].get(c)
            if nxt is None:
                nxt=len(children)
                children[node][c]=nxt
                children.append({});ends.append(0);edge.append(int(prefix not in fixed))
            node=nxt
        ends[node]|=1<<i
print('INDEPENDENT_TRIE',len(children), 'fixed',len(fixed),'candidate_words',sum(pool.values()),'build_s',round(perf_counter()-start,3),flush=True)
assert len(children)==26705

# dictionary-cost dynamic programming, no C++ bitset arrays or parent serialisation
# Node v stores the best distinct-prefix edge cost for every subset of its labels.
states=[None]*len(children)
comb_checks=0; disjoint=0; peak=0
for v in range(len(children)-1,-1,-1):
    t=ends[v]
    base={}
    x=t
    while True:
        base[x]=0
        if x==0: break
        x=(x-1)&t
    for child in children[v].values():
        rhs=states[child]
        result={}
        for a,ca in base.items():
            for b,cb in rhs.items():
                comb_checks+=1
                if a&b: continue
                disjoint+=1
                z=a|b
                score=ca+cb+(edge[child] if b else 0)
                if score<result.get(z,10**9): result[z]=score
        base=result
        states[child]=None
    states[v]=base
    if len(base)>peak:peak=len(base)
opt=len(fixed)+states[0][(1<<len(keys))-1]
print('INDEPENDENT_RESULT',opt,'root',len(states[0]),'comb_checks',comb_checks,'disjoint',disjoint,'peak',peak,'wall_s',round(perf_counter()-start,3),flush=True)
assert opt==112
report={'schema':'EC49FDE_ALTERNATIVE_LATE_KEY_PYTHON_FULL20_EXACT_V1','late_key':[6,4,1],'prior_late_key':[7,3,2],'early_key':[4,2,1],'explicit_witness':WITNESS,'explicit_witness_edges':112,'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','fixed_edges':len(fixed),'original_edges':len(original),'keys':keys,'candidate_count':sum(pool.values()),'pool_sizes':pool,'trie_nodes':len(children),'optimal_edges':opt,'root_state_count':len(states[0]),'inspected_state_pairs':comb_checks,'disjoint_state_pairs':disjoint,'peak_node_states':peak,'runtime_seconds':round(perf_counter()-start,4)}
raw=json.dumps(report,sort_keys=True,indent=2)+'\n'
(HERE/'EC49FDE_INDEPENDENT_PYTHON_REPORT.json').write_text(raw)
print('REPORT_SHA256',hashlib.sha256(raw.encode()).hexdigest(),flush=True)
