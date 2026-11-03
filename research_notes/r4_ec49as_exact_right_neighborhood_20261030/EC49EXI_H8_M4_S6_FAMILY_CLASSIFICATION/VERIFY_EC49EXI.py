"""EC49EXI exact finite native X6 BRC key + signature-family classification.
Full original returning-word enumeration and independent analytic key counting.
Run from GitHub checkout; requires only Python 3 and predecessor EC49EXH source.
"""
import sys
import json
from itertools import combinations, product
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/'EC49EXH_H8_M4_S6_E90'))
# For local evidence replay, sibling EC49EXH source can be provided in this folder.
try:
    from BUILD_EC49EXH_FIXED_DP import eligible_words, T4, T2
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from BUILD_EC49EXH_FIXED_DP import eligible_words, T4, T2


def count_keys(h):
    for w in range(1, (h+1)//2+1):
        for r in range(h-2*w+2):
            for f in range(h-2*w-r+2):
                g=h-(2*w-1)-r-f
                yield (r+2*w+f,r+g,w)


def expected_families(key,h):
    u,v,w=key
    r=u+v-h-1
    a=w-1
    f=u-r-2*w
    g=v-r
    if min(r,a,f,g)<0:return ()
    # Finite h=2..8 transfer-fiber identity, checked against every raw word below.
    if r>=1:return (4,)
    if f>=1 and g>=1:return (2,)
    return ()


def build():
    all_rows={}; native_words=0; observed_signatures=set(); schedules={}
    for h in range(2,9):
        row={}; n=0; types=Counter()
        for key in count_keys(h):
            mask=0
            for word,st,sig in eligible_words(h,key):
                n+=1;observed_signatures.add(sig)
                if sig in T4: mask|=1<<T4.index(sig)
                if sig in T2: mask|=1<<(4+T2.index(sig))
            family=tuple([4] if mask&15==15 else [])+tuple([2] if mask&48==48 else [])
            assert family==expected_families(key,h),(h,key,mask,family)
            if family:row[key]=family
        all_rows[h]=row;native_words+=n
        types.update(t for fs in row.values() for t in fs)
        schedules[h]={'returning_words':n,'eligible_keys':len(list(count_keys(h))),
                      'full_rank_T4_keys':types[4], 'full_rank_T2_keys':types[2]}
    assert [schedules[h]['returning_words'] for h in range(2,9)] == [8,51,304,1770,10224,58947,340064]
    assert len(observed_signatures)==11
    return all_rows,schedules,native_words


def main():
    fiber,summary,total_words=build()
    keys=sorted(set().union(*(fiber[h].keys() for h in fiber)))
    baseline=(3,1,1)
    assert len(keys)==84 and fiber[2]=={baseline:(4,)}
    key_quartets=0; assignments=0; typed=Counter(); frontier=Counter()
    for triple in combinations((k for k in keys if k!=baseline),3):
        quartet=(baseline,)+triple
        options=[[(idx,t) for idx,k in enumerate(quartet) for t in fiber[h].get(k,())]
                 for h in range(2,9)]
        assert options[0]==[(0,4)]
        if any(not a for a in options):continue
        n=0
        for seq in product(*options):
            used={i for i,t in seq}
            if len(used)!=4:continue
            n+=1
            type_pattern=''.join(str(t) for i,t in seq)
            typed[type_pattern]+=1
            prior={i for i,t in seq[:-1]}
            phase='new_key_at_h8' if len(prior)==3 else 'four_keys_by_h7'
            frontier[(phase,seq[-1][1])]+=1
        if n:key_quartets+=1;assignments+=n
        # Independent inclusion-exclusion over three extra key identities.
        ie=0
        for bs in range(8):
            subset=(baseline,)+tuple(triple[i] for i in range(3) if bs>>i&1)
            p=1
            for h in range(3,9):p*=sum(len(expected_families(k,h)) for k in subset)
            ie+=(-1)**(3-bs.bit_count())*p
        assert n==ie,(quartet,n,ie)
    assert (key_quartets,assignments,len(typed))==(14092,55493,42)
    assert sum(frontier.values())==assignments
    results={'status':'PASS', 'horizon':8,'M':4,'S_limit':6,'returning_words':total_words,
     'distinct_signatures':len({v for v in T2+T4}),
     'signature_universe_size':11,'eligible_distinct_keys':len(keys),
     'qualified_four_key_sets':key_quartets,'family_level_assignments':assignments,
     'type_patterns':len(typed),
     'by_number_T2_horizons':dict(sorted(Counter({n:sum(v for pat,v in typed.items() if pat.count('2')==n) for n in range(7)}).items())),
     'frontier':{phase:{'T2':frontier[(phase,2)],'T4':frontier[(phase,4)]}
                 for phase in ('new_key_at_h8','four_keys_by_h7')},
     'per_horizon':summary}
    out=Path(__file__).with_name('EC49EXI_EXECUTED.json')
    out.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:results[k] for k in ('status','returning_words','eligible_distinct_keys','qualified_four_key_sets','family_level_assignments','type_patterns','frontier')},ensure_ascii=False))
if __name__=='__main__': main()
