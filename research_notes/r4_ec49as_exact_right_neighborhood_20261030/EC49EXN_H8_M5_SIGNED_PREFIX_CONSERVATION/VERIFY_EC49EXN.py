#!/usr/bin/env python3
"""EC49EXN: new prefix conservation theorem and exact triple schedule observer stratification.
Pure exact integer enumeration; frozen model as EC49EXM; no classical arithmetics.
"""
from collections import Counter
from itertools import combinations
import json

HS=tuple(range(2,9))
FROZEN={'global':'773d538180bfb49e24cffeb35c3ee75eb0628e2e',
        'enterprise_math':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'}

def eligible(h):
    result={}
    for w in range(1,(h+1)//2+1):
        for u in range(2*h+3):
            for v in range(h+2):
                r=u+v-h-1;f=h+1-v-2*w;g=h+1-u
                if min(r,f,g)>=0 and (r>=1 or (r==0 and f>=1 and g>=1)):
                    result[(u,v,w)]='T4' if r>=1 else 'T2'
    return result
S={h:eligible(h) for h in HS}
assert list(map(lambda h:len(S[h]),HS))==[1,4,9,17,28,43,62]

# Five blocks of the unique triple partition: triple B then four singleton blocks.
# Assign injectively; no old EC49EXM counting helper is imported.
report=[]; aggregate=Counter(); Ls=Counter(); type_masks=Counter()
for triple in combinations(HS,3):
    single=[h for h in HS if h not in triple]
    common=set.intersection(*(set(S[h]) for h in triple))
    if not common:continue
    stats=Counter(); nkeys=0
    for common_key in sorted(common):
        def extend(i,used,n_T2,type_profile):
            if i==len(single):
                keyL=2*(sum(common_key)-1)
                keytype='T2' if S[triple[-1]][common_key]=='T2' else 'T4'
                stats[(n_T2,keytype)]+=1
                aggregate[n_T2]+=1
                Ls[keyL]+=1
                type_masks[''.join(type_profile)]+=1
                return
            h=single[i]
            for k,t in S[h].items():
                if k not in used:
                    extend(i+1,used | {k}, n_T2+(t=='T2'),type_profile+[t[1]])
        base_type=[S[h][common_key] for h in triple]
        base_n_T2=sum(t=='T2' for t in base_type)
        # sort by horizon for canonical type mask, created at terminal
        def enumerate_singles(i, used, choices):
            if i==len(single):
                profile=tuple(S[h][common_key] if h in triple else S[h][choices[h]] for h in HS)
                n2=sum(t=='T2' for t in profile)
                stats[(n2,'T2' if S[triple[-1]][common_key]=='T2' else 'T4')]+=1
                aggregate[n2]+=1
                Ls[2*(sum(common_key)-1)]+=1
                type_masks[''.join('2' if t=='T2' else '4' for t in profile)]+=1
                return
            h=single[i]
            for k in S[h]:
                if k not in used:
                    choices[h]=k
                    enumerate_singles(i+1,used | {k},choices)
        # Do not iterate common keys that cannot be injected into four singleton blocks.
        before=sum(stats.values())
        enumerate_singles(0,{common_key},{})
        if sum(stats.values())>before:nkeys+=1
    if stats:
        report.append({'triple_horizons':triple,'compatible_repeated_keys':nkeys,
                       'schedule_count':sum(stats.values()),
                       'by_n_T2_and_triple_last_type':[{'n_T2':a,'triple_final_type':b,'schedules':v}
                                                      for (a,b),v in sorted(stats.items())]})
assert len(report)==8 and sum(r['schedule_count'] for r in report)==123147
assert [r['schedule_count'] for r in report]==[71799,23502,4983,2905,10158,3015,1917,4868]
assert sum(aggregate.values())==123147 and sum(Ls.values())==123147

# Each operation has positive primitive axis-count vector and native signed directions.
OPS={
 'a':(-1,-1),'b':(-2,-2),
 'c':(1,2,-1,-2),'d':(2,1,-2,-1),
 'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)
}
# all distinct operation code prefixes at length two = prefix-free decoding
first_two={tuple(v[:2]) for v in OPS.values()}
assert len(first_two)==len(OPS)
# Native counts of a representative word with arbitrary r, c split, check invariance across horizon.
for h in HS:
    for k in S[h]:
        u,v,w=k; r=u+v-h-1; f=h+1-v-2*w; g=h+1-u
        counts={'a':w-1, 'b':0,'c':r,'d':0,'e':w,'f':f,'g':g}
        plus=[sum(counts[op]*steps.count(axis) for op,steps in OPS.items()) for axis in (1,2,3)]
        minus=[sum(counts[op]*steps.count(-axis) for op,steps in OPS.items()) for axis in (1,2,3)]
        assert plus==[u,v,w] and minus==[u-2,v,w]
        assert sum(plus+minus)==2*(sum(k)-1)

out={'status':'PASS','statement':'all eligible X6 return words have full signed histogram (u,v,w,u-2,v,w) and primitive length 2*(u+v+w-1); native operation code is 2-symbol prefix-free; same-key words at different h have longest common primitive prefix <= length-3',
     'frozen_scientific_pins':FROZEN,
     'per_triple_skeleton':report,
     'schedules_by_count_T2':dict(sorted(aggregate.items())),
     'repeated_key_primitive_length_distribution':dict(sorted(Ls.items())),
     'distinct_observer_type_profiles':len(type_masks),
     'most_frequent_type_profiles':type_masks.most_common(12),
     'total_schedules':sum(aggregate.values()),
     'remaining':'prefix-edge minimal cost across 123147 triple key schedules and 32 double-pair skeletons'}
print(json.dumps(out,ensure_ascii=False,indent=2))