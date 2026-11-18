#!/usr/bin/env python3
"""EC49FFR: exact finite signed-X6/DFA suffix certificate for an all-h theorem.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Frozen native model original Git blob 6350340fbe869f17b5a50bd1ba30640db44a3a99.
Python 3 standard library, no floating point.
"""
from collections import Counter, defaultdict
from itertools import combinations
import json

A='acdefg'; SIGS=(1,2,4,8)
S=(0,0,4,1,16,32,8,2,0)
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
VEC={'a':(1,0,0,0,0),'c':(0,1,0,0,0),'d':(0,1,0,0,0),
     'e':(0,0,1,0,0),'f':(0,0,0,1,0),'g':(0,0,0,0,1)}
assert len({OPS[o][:2] for o in A})==6
assert all(len(OPS[o]) in (2,4) for o in A)
assert 0 not in [T[i][j] for i in range(9) for j in range(6)]

def full_tails(rem):
    if rem==0:
        yield '';return
    for o in A:
        if len(OPS[o])<=rem:
            for s in full_tails(rem-len(OPS[o])):
                yield o+s

def count_vec(word):
    return tuple(sum(VEC[c][j] for c in word) for j in range(5))

def signature(word,start_state=0):
    s=start_state
    for o in word:s=T[s][A.index(o)]
    return S[s]

def catalogue(r):
    """All overapproximate demand masks of a single common native prefix L-r.
    A suffix vector (a,c+d,e,f,g) changes by (0,-1,0,1,1) from Hh to H(h+1).
    Include single-horizon masks. State 0 is impossible at these noninitial cuts.
    """
    phases=[('boundary',None)]
    phases += [('first',v) for v in sorted({OPS[c][0] for c in A})]
    phases += [(name,c) for name in ('second','third') for c in 'cde']
    out={}
    for phase,kind in phases:
        candidates=(A if phase=='boundary' else
                    tuple(c for c in A if OPS[c][0]==kind) if phase=='first' else
                    (kind,))
        offset={'boundary':0,'first':1,'second':2,'third':3}[phase]
        for st in range(1,9):
            groups=defaultdict(int)
            for op in candidates:
                left=r-(len(OPS[op])-offset)
                if left<0 or left%2:continue
                for rest in full_tails(left):
                    word=op+rest
                    sig=signature(word,st)
                    if sig in SIGS:
                        groups[count_vec(word)] |= 1<<SIGS.index(sig)
            masks=set()
            for v,lower in groups.items():
                masks.add(lower)
                masks.add(lower<<4)
                later=(v[0],v[1]-1,v[2],v[3]+1,v[4]+1)
                if later in groups:masks.add(lower | (groups[later]<<4))
            if masks:out[(phase,str(kind),st)]=masks
    return out

def mincover(masks):
    dp={0:0}
    for m in set(masks):
        for old,cnt in list(dp.items()):
            new=old|m
            if cnt+1<dp.get(new,99):dp[new]=cnt+1
    return dp.get(255,99)

def certificate():
    rows=[]
    for r in range(1,8):
        d=catalogue(r);masks=set.union(set(),*d.values())
        rows.append({'suffix_microsteps':r,'decoder_state_cases':len(d),
                     'distinct_possible_demand_masks':len(masks),
                     'max_demands_at_one_prefix':max(map(int.bit_count,masks)),
                     'cover_lower_bound':mincover(masks)})
    assert [x['cover_lower_bound'] for x in rows]==[8,8,4,4,4,4,3]
    assert [x['max_demands_at_one_prefix'] for x in rows]==[1,1,2,2,2,2,3]
    d=catalogue(7);masks=sorted(set.union(set(),*d.values()))
    triples=[c for c in combinations(masks,3) if c[0]|c[1]|c[2]==255]
    expected=(0b00001010,0b01100100,0b10010001)
    assert triples==[expected],triples
    states=[]
    for mask in expected:
        states.append(sorted({key[2] for key,ms in d.items() if mask in ms}))
    assert states==[[1],[4],[5]],states
    assert [T[0][A.index(c)] for c in A]==[1,2,3,1,4,5]
    for state,initials in ((1,('a','e')),(4,('f',)),(5,('g',))):
        assert {c for c in A if T[0][A.index(c)]==state}==set(initials)
        assert all(T[q][i]!=state or q==state for q in range(1,9) for i in range(6))
    return {'suffix_depth_certificates':rows,
            'three_prefix_cover_at_L_minus_7':{
                'unique_abstract_cover_masks':[format(v,'08b') for v in expected],
                'required_dfa_states':states,
                'forced_distinct_native_first_steps':3},
            'analytic_lower_bound':'C_native >= 2L+28 >= 4h+40 for all integer h>=5',
            'minimum_legal_L':'2h+6'}

def family(h):
    q=h-4;key=(5,h-2,1)
    w={(h,1):'g'*q+'efdd',(h,2):'f'+'g'*q+'edd',
       (h,4):'f'+'g'*q+'ecc',(h,8):'g'*q+'efcc',
       (h+1,1):'g'*q+'efdgf',(h+1,2):'f'+'g'*q+'edgf',
       (h+1,4):'f'+'g'*q+'ecfg',(h+1,8):'g'*q+'efcfg'}
    assert set(w)=={(i,s) for i in (h,h+1) for s in SIGS}
    prefixes=set()
    for (window,sig),word in w.items():
        assert signature(word)==sig,(h,window,sig,word)
        ct=Counter(word)
        assert ct['a']==key[2]-1 and ct['e']==key[2]
        assert ct['c']+ct['d']==sum(key[:2])-window-1
        assert ct['f']==window+1-key[1]-2*key[2]
        assert ct['g']==window+1-key[0]
        signed=tuple(z for op in word for z in OPS[op])
        assert len(signed)==2*(sum(key)-1)
        sc=Counter(signed)
        assert tuple(sc[j] for j in (1,2,3))==key
        assert tuple(sc[j]-sc[-j] for j in range(1,7))==(2,0,0,0,0,0)
        for j in range(1,len(signed)+1):prefixes.add(signed[:j])
    profile=Counter(map(len,prefixes));L=2*h+6
    assert all(profile[j]==2 for j in range(1,L-7))
    assert all(profile[j]==4 for j in range(L-7,L-2))
    assert all(profile[j]==8 for j in range(L-2,L+1))
    assert len(prefixes)==4*h+40
    return len(prefixes)

def main():
    result=certificate()
    result.update(schema='EC49FFR_UNIVERSAL_ONE_KEY_ADJACENT_EXACT_V1',
        frozen_scientific_pin='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        native_model_git_blob='6350340fbe869f17b5a50bd1ba30640db44a3a99',
        exact_theorem='For all integers h>=5, C_min_one_key(Hh,H(h+1))=4h+40',
        witness_audit_h=[5,64],witness_audit_cases=60,
        witness_costs={str(h):family(h) for h in range(5,65)},
        scope='Original nine-state BRC observer and ordered signed six-axis code; eight low-signature demands; one identical full key',
        admission_status='AUTHOR_FINITE_SUFFIX_CERTIFICATE_AND_ANALYTIC_EXACT_THEOREM; DRIVER_PENDING')
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
