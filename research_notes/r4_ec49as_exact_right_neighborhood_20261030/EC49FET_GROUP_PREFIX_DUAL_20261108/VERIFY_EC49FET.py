#!/usr/bin/env python3
"""Fully exact self-contained reviewer for EC49FET stronger group/prefix dual certificates.
No LP solver, SciPy, NumPy, floats, or source-specific optimistic acceptance logic.
"""
import sys, json
from collections import defaultdict, Counter
from WORD_MODEL_EC49FET import words_with_label, native_prefixes, OPERATIONS, NEXT, OBS, ALPHABET

def verify(path):
    C=json.load(open(path));assert C['schema']=='EC49FET_STRONG_GROUP_PREFIX_DUAL_V1'
    Q=int(C['Q']);assert Q>0
    K={tuple(k) for k in C['keys']};high=set(C['high'])
    pair_to_idx={};pair_list=[];words=[];word_groups=[];incidences=[];labels=[]
    for h in range(2,10):
        ss=(1,8,16) if h==3 else ((16,32) if h in high else (1,2,4,8))
        for s in ss:
            gid=len(labels);labels.append((h,s))
            group_words=sorted({w for k in K for obs,w in words_with_label(h,k) if obs==s})
            assert group_words
            for w in group_words:
                path=tuple(step for ch in w for step in OPERATIONS[ch]);ct=Counter(path)
                assert len(w)==h
                assert tuple(ct[i]-ct[-i] for i in range(1,7))==(2,0,0,0,0,0)
                assert tuple(ct[i] for i in range(1,4)) in K
                state=0
                for ch in w:state=NEXT[state][ALPHABET.index(ch)]
                assert OBS[state]==s
                local=[]
                for p in native_prefixes(w):
                    pair=(gid,p)
                    if pair not in pair_to_idx:
                        pair_to_idx[pair]=len(pair_list);pair_list.append(pair)
                    local.append(pair_to_idx[pair])
                words.append(w);word_groups.append(gid);incidences.append(local)
    assert len(labels)==23
    weights=dict((int(i),int(v)) for i,v in C['t_sparse'])
    assert len(weights)==len(C['t_sparse']) and all(v>0 for v in weights.values())
    assert all(0<=i<len(pair_list) for i in weights)
    per_prefix=defaultdict(int)
    for i,v in weights.items():per_prefix[pair_list[i][1]]+=v
    assert all(v<=Q for v in per_prefix.values()),'prefix dual capacity overrun'
    gamma=[int(t) for t in C['gamma']]
    assert len(gamma)==23 and all(t>=0 for t in gamma)
    for wid,w in enumerate(words):
        tot=sum(weights.get(i,0) for i in incidences[wid])
        assert tot>=gamma[word_groups[wid]],('word constraint',wid)
    S=sum(gamma)
    assert S>97*Q, ('failed to certify strict >97',S,Q)
    return {'case':C['case'],'groups':len(labels),'candidate_words':len(words),'group_prefix_pairs':len(pair_list),
            'nonzero_integer_weights':len(weights),'lower_numerator':S,'denominator':Q,'lower_bound':S/Q,
            'proves_C_native_ge_98':True,'verification':'PASS integer-only'}
if __name__=='__main__':
    for f in sys.argv[1:]: print(json.dumps(verify(f)),flush=True)