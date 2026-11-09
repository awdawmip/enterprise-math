#!/usr/bin/env python3
"""EC49FFZ: exact signed-X6 BRC low-word separation and high-seed absorption.
Frozen model: EC49FFC/FFD via EC49FFX/FFY; no external numerical model.
"""
from collections import Counter
from itertools import product
import json

CODES = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
         'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ORDER = 'acdefg'
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
     (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
     (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
LOWS = (1,2,4,8)


def label(word):
    q=0
    for u in word: q=T[q][ORDER.index(u)]
    return SIG[q]


def native(word):
    return tuple(s for c in word for s in CODES[c])


def fullkey(word):
    cnt=Counter(word); h=len(word); E=cnt['e']
    if E<1 or cnt['a']+1!=E: return None
    key=(h+1-cnt['g'],h+1-2*E-cnt['f'],E)
    return key if min(key)>0 else None


def validate_word(word,sig,h,allow_nonpositive_seed=False):
    assert len(word)==h and label(word)==sig and (allow_nonpositive_seed or fullkey(word) is not None),(h,sig,word)
    st=native(word)
    assert len(st)>=2*h+4 or sig in (16,32)
    cc=Counter(st)
    assert tuple(cc.get(j,0)-cc.get(-j,0) for j in range(1,7))==(2,0,0,0,0,0)
    if not allow_nonpositive_seed: assert tuple(cc[j] for j in (1,2,3)) == fullkey(word)
    else: assert min(tuple(cc[j] for j in (1,2,3)))>=0
    return st


def witness(h, suffix=None):
    assert h>=4
    if suffix is None: suffix='f'*(h-4)
    assert len(suffix)==h-4 and set(suffix)<={'f','g'}
    words={4:'feg'+suffix+'c',2:'feg'+suffix+'d',
           8:'gef'+suffix+'c',1:'gef'+suffix+'d'}
    seed={'H2_16':'fe','H2_32':'ge','H3_16':'feg','H3_32':'gef'}
    ps=set()
    for sig,w in words.items():
        st=validate_word(w,sig,h)
        ps.update(st[:i] for i in range(1,len(st)+1))
    for nm,w in seed.items():
        sig=int(nm.split('_')[1]); hh=int(nm[1])
        st=validate_word(w,sig,hh,allow_nonpositive_seed=True)
        assert all(st[:i] in ps for i in range(1,len(st)+1)),(h,nm)
    keys=sorted({fullkey(w) for w in words.values()})
    t=suffix.count('g'); expected=(h-t,t+2,1)
    assert keys==[expected],(h,keys,expected)
    assert len(ps)==4*h+16,(h,len(ps),4*h+16)
    return {'h':h,'key':expected,'native_prefix_cost':len(ps),
            'low_observation_words':{str(k):v for k,v in sorted(words.items())}}


def suffix_separation_exhaustive(h):
    """Independent finite literal-word test, not used as proof of the universal result."""
    by_sig={sig:[] for sig in LOWS}
    for tup in product(ORDER,repeat=h):
        w=''.join(tup)
        if fullkey(w) is None: continue
        s=label(w)
        if s in by_sig: by_sig[s].append(native(w))
    prefix_sets={s:set() for s in LOWS}
    for s,li in by_sig.items():
        for st in li:
            prefix_sets[s].update(st[:j] for j in range(1,len(st)+1))
    for s,li in by_sig.items():
        others=set().union(*(prefix_sets[t] for t in LOWS if t!=s))
        for st in li:
            assert st[:-3] not in others, (h,s,st)
    return {'h':h,'legal_low_word_count':sum(map(len,by_sig.values())),
            'by_signature':{str(k):len(v) for k,v in by_sig.items()},
            'suffix_separation':'PASS'}


def reachability_first_step():
    # An exact, automaton-only audit of the lemma's local assumptions.
    assert len({v[:2] for v in CODES.values()})==6
    first={}
    for op in ORDER:
        states={T[0][ORDER.index(op)]}
        for _ in range(9):
            states|={T[q][ORDER.index(v)] for q in tuple(states) for v in ORDER}
        first[op]=sorted({SIG[q] for q in states if SIG[q] in LOWS})
    assert first['c']==[4] and first['f']==[2,4]
    assert first['d']==[1] and first['g']==[1,8]
    assert first['a']==[2,8] and first['e']==[2,8]
    for q in (2,3,6,7):
        for letter in 'aefg': assert T[q][ORDER.index(letter)]==q
        for letter in 'cd': assert T[q][ORDER.index(letter)] in (q,8)
    return first


def main():
    first=reachability_first_step()
    explicit=[witness(h) for h in range(4,151)]
    suffix_family_count=0
    for h in range(4,13):
        for suffix in map(''.join,product('fg',repeat=h-4)):
            witness(h,suffix)
            suffix_family_count+=1
    for h in (16,31,70,100,150):
        witness(h,'g'*(h-4))
        witness(h,('fg'*((h-3)//2))[:h-4])
    literal=[suffix_separation_exhaustive(h) for h in range(2,8)]
    report={'name':'EC49FFZ high-seed absorption','frozen_scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'theorem':'for every integer h>=4, native-prefix optimum of H2/H3 fixed high seeds + Hh four low signatures, with arbitrary positive full keys, equals 4h+16',
            'code_prefix_2_unique':True,'first_operation_reachable_lows':first,
            'witness_range':[4,150],'witness_count':len(explicit),'all_suffix_h4_to_h12':suffix_family_count,
            'witness_sample':[explicit[i-4] for i in (4,5,9,20,100,150)],
            'literal_suffix_tests':literal,'finite_check_limitation':'finite tests audit model; the stated proof uses a general suffix lemma'}
    with open('EC49FFZ_REPORT.json','w') as f: json.dump(report,f,ensure_ascii=False,indent=2)
    print(json.dumps({'theorem':'PASS','witnesses':len(explicit),
        'literal_counts':[x['legal_low_word_count'] for x in literal],
        'exhaustive_suffix_family_count':suffix_family_count,
        'suffix_separation':'PASS','sample_h9':explicit[5]['native_prefix_cost']},sort_keys=True))

if __name__=='__main__':main()
