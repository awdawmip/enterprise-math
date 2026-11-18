#!/usr/bin/env python3
"""Independent arbitrary-precision interval intersection checks of the 18-chamber quotient witness.
Full quotient computation is by R5_COMPLETE_18_CHAMBER_QUOTIENT.cpp; this checks construction, thresholds,
and a fixed deterministic sample across every chamber and physical action.
"""
import json, hashlib, random, itertools, re
from pathlib import Path
P=Path(__file__).resolve().parent
raw=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
expect='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256(raw).hexdigest()==expect
D=json.loads(raw)['counts_and_cohorts']; rows=[tuple(map(int,D[str(k)]['counts'])) for k in range(214,315)]
meta=json.loads((P/'stages_18.json').read_text()); taus=list(map(int,meta['stage_taus']))
L,U=int(meta['L']),int(meta['U'])
assert len(taus)==18 and taus[0]==L and taus[-1]<U
assert hashlib.sha256((P/'onset_18.bin').read_bytes()).hexdigest()=='ca175a4655b045d6427b9171c80198e548a8bc27f939a3b5e8f78a1c7f6b12bf'
H=(18,24,82,34,17,144,208)

def maximal(seq):
    masks=set(seq)
    return tuple(sorted(s for s in masks if not any(s!=t and (s&t)==s for t in masks)))

def direct_sweep(c,tau):
    # z=2*y, endpoints e=2*c+/-tau are exact integers. Test each endpoint plus open cells.
    endpoints=sorted(set(z for x in c for z in (2*x-tau,2*x+tau)))
    masks=[sum(1<<i for i,x in enumerate(c) if abs(z-2*x)<=tau) for z in endpoints]
    masks.extend(sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*tau)
                 for a,b in zip(endpoints,endpoints[1:]))
    return maximal(masks)

def center_windows(c,tau):
    return maximal(sum(1<<i for i,x in enumerate(c) if v<=x<=v+tau) for v in c)

def profile(p,tau):
    slots=(18,24,82,34,17,p[0],144,208,p[1])
    return tuple(center_windows(tuple(row[h] for h in slots),tau) for row in rows)

# This first witness is discovered by the exhaustive C++ program, not chosen to obtain a desired outcome.
a=(7,11);b=(11,14);st=2; k=220
paL,pbL=profile(a,L),profile(b,L)
paU,pbU=profile(a,U-1),profile(b,U-1)
paM,pbM=profile(a,taus[st]),profile(b,taus[st])
assert paL==pbL and paU==pbU and paM!=pbM
assert paM[k-214]==(2,13,16,32,192,256)
assert pbM[k-214]==(2,13,16,192,288)
print('WITNESS_CONFIRMED',a,b,'stage',st,'tau',taus[st],'budget',k,flush=True)

cand=[i for i in range(256) if i not in H]
allpairs=list(itertools.combinations(cand,2))
rng=random.Random(20261119)
sample=[a,b]+rng.sample([p for p in allpairs if p not in (a,b)],64)
checks=0
for idx,pair in enumerate(sample):
    slot=(18,24,82,34,17,pair[0],144,208,pair[1])
    for ki,row in enumerate(rows):
        c=tuple(row[h] for h in slot)
        for tau in taus:
            assert center_windows(c,tau)==direct_sweep(c,tau),(pair,ki,tau)
            checks+=1
    if idx%16==0:print('CHECKED_PAIRS',idx+1,flush=True)
# Last threshold and U-1 are guaranteed equivalent for all 256 centers by exhaustive onset construction;
# explicitly check 66*101 support families on U-1 against the last included threshold.
for p in sample:
    assert profile(p,taus[-1])==profile(p,U-1)
log=(P/'18chamber_run.log').read_text()
records=[]
for line in log.splitlines():
    if line.startswith('STAGE '):
        m=re.fullmatch(r'STAGE (\d+) GROUPS (\d+) SPLIT_PREVIOUS (\d+) EXTRA (\d+) EQUIV_INSTANCE_PAIRS (\d+)',line)
        assert m, line
        records.append(dict(stage=int(m[1]),classes=int(m[2]),split_previous=int(m[3]),extra=int(m[4]),equivalent_pair_of_pairs=int(m[5])))
assert len(records)==18 and records[0]['classes']==1460 and records[1]['classes']==2563 and records[-1]['classes']==2711
assert records[1]['equivalent_pair_of_pairs']-records[-1]['equivalent_pair_of_pairs']==620
summary={
 'schema':'R5_18_CHAMBER_QUOTIENT_CERT_V1',
 'science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
 'center_input_sha256':expect,
 'onset_sha256':hashlib.sha256((P/'onset_18.bin').read_bytes()).hexdigest(),
 'stages':[{'index':x['stage'],'tau':str(taus[x['stage']]),'classes':x['classes'],'split_previous':x['split_previous'],'extra':x['extra'],'equal_pair_of_pairs':x['equivalent_pair_of_pairs']} for x in records],
 'pair_instances':30876,'endpoint_joint_classes':2563,'whole_chamber_classes':2711,
 'endpoint_joint_classes_split_interior':108,'endpoint_joint_class_daughters_distribution':{'1':2455,'2':68,'3':40},
 'endpoint_joint_equivalent_instance_pairs_lost_interior':620,
 'first_interior_counterexample':{'A':list(a),'B':list(b),'tau':str(taus[st]),'stage_index':st,'query_budget':k,'supports_A':list(paM[k-214]),'supports_B':list(pbM[k-214]),'equal_at_L':True,'equal_at_U_minus_1':True},
 'independent_crosscheck':{'pair_representatives':len(sample),'actions':101,'stages':18,'center_window_vs_interval_cell_comparisons':checks,'last_threshold_vs_U_minus_1_pairs':len(sample),'status':'PASS'}
}
(P/'RESULT_R5_COMPLETE_18_CHAMBER_QUOTIENT.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print('PASS_R5_COMPLETE_18_CHAMBERS',checks,'crosschecks', 'endpoint_joint',2563,'whole_chamber',2711,'lost',620)
