#!/usr/bin/env python3
"""Independent alphabet-recursion and tuple-prefix set crosscheck for EC49FGQ."""
import json,itertools,collections,os
ALPHABET='acdefg'
STATE_TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
READOUT=(0,0,4,1,16,32,8,2,0)
EXPANDED={ 'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQUIRED={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
LABELS=tuple((h,s) for h in REQUIRED for s in REQUIRED[h])

def key(word):
    h=len(word)
    return (h+1-word.count('g'),h+1-word.count('f')-2*word.count('e'),word.count('e'))

def signed_prefix_set(word):
    seq=[];out=set()
    for c in word:
        for ax in EXPANDED[c]:
            seq.append(ax);out.add(tuple(seq))
    return frozenset(out)

def full_alphabet_paths(h):
    walk=[];pos=[0]*6
    def rec(q):
        if len(walk)==h:
            if READOUT[q] in REQUIRED[h] and pos==[2,0,0,0,0,0]:
                yield (READOUT[q],''.join(walk))
            return
        for j,c in enumerate(ALPHABET):
            qq=STATE_TRANS[q][j]
            if qq==8:continue
            walk.append(c)
            for v in EXPANDED[c]:pos[abs(v)-1]+=1 if v>0 else -1
            yield from rec(qq)
            for v in EXPANDED[c]:pos[abs(v)-1]-=1 if v>0 else -1
            walk.pop()
    yield from rec(0)

def run():
    source=json.load(open(os.path.join(os.path.dirname(__file__),'EC49FGJ_SEVEN_KEY_94_WITNESSES.json')))
    base_profiles=source['profiles']; allowed={p['profile_id']:set(map(tuple,p['allowed_keys'])) for p in base_profiles}
    cand={p['profile_id']:collections.defaultdict(list) for p in base_profiles}
    all_counts={}
    for h in REQUIRED:
        count=collections.Counter()
        for s,w in full_alphabet_paths(h):
            count[s]+=1;k=key(w)
            for profile in base_profiles:
                if k in allowed[profile['profile_id']]:
                    cand[profile['profile_id']][(h,s)].append((k,w,signed_prefix_set(w)))
        all_counts[str(h)]={str(s):count[s] for s in REQUIRED[h]}
    result={'schema':'EC49FGQ_INDEPENDENT_CROSSCHECK_V1','frozen_pin':source['frozen_scientific_pin'],
            'algorithm':'direct six-letter DFA recursion, native endpoint, tuple-of-signed-microsteps prefixes; no keyed-count generator or bitmask',
            'all_legal_word_counts':all_counts,'profiles':[]}
    assert all_counts['2']=={'16':1,'32':1},all_counts['2']
    for profile in base_profiles:
        pid=profile['profile_id']; base={(x['window'],x['signature']):x['word'] for x in profile['demands']}
        basep={l:signed_prefix_set(w) for l,w in base.items()}
        assert len(base)==24
        baseall=set().union(*basep.values());assert len(baseall)==94
        tests=0;screened=0;fixed=0;forced=0
        for i,j in itertools.combinations(LABELS,2):
            F=set().union(*(basep[l] for l in LABELS if l not in (i,j)))
            b=93-len(F)
            if b<0:fixed+=1;continue
            oldkeys={key(base[l]) for l in LABELS if l not in (i,j)}
            if len(oldkeys)<7:
                # Both H2 words have unique realizations, so any absent key
                # must be restored by the selected H2 demand.
                h2=[l for l in (i,j) if l[0]==2]
                assert h2 and (set(allowed[pid])-oldkeys).issubset({key(base[l]) for l in h2})
                assert len(oldkeys|{key(base[l]) for l in h2})==7
                forced+=1
            screened+=1
            opts=[]
            for label in (i,j):
                choices=set()
                for k,w,S in cand[pid][label]:
                    delta=S.difference(F)
                    if len(delta)<=b: choices.add(frozenset(delta))
                opts.append(choices)
            for left in opts[0]:
                for right in opts[1]:
                    tests+=1
                    assert len(left.union(right))>b,(pid,i,j,b,left,right)
        c={'profile':pid,'candidate_count':sum(map(len,cand[pid].values())),
           'pairs_blocked_by_fixed_cost':fixed,'pairs_screened':screened,'forced_H2_key_recovery_pairs':forced,
           'tested_distinct_delta_pairs':tests,'found_93':False}
        result['profiles'].append(c); print(c,flush=True)
    path=os.path.join(os.path.dirname(__file__),'CROSSCHECK_EC49FGQ.json')
    with open(path,'w') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
    print('REPORT',path)
if __name__=='__main__':run()
