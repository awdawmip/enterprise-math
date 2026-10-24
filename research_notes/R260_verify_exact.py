#!/usr/bin/env python3
"""R260: independent author-side exact finite BRC model checker (not native module)."""
from collections import defaultdict
from itertools import product
import json

# q -> branch-selector a -> (target q, affine multiplier eta, translation b e1).
EDGES = (
    ((2, -1, -1), (2, 1, -1)),
    ((0, -1, -1), (0, 1, -1)),
    ((1, 1, 1), (2, 1, -1)),
)
# DFA modes: 0=not seen '00', last!=0; 1=not seen '00', last=0; 2=seen '00'.
DELTA = ((1, 0), (2, 0), (2, 2))
MODES = {0: (0, 2), 1: (1, 2), 2: (0, 1, 2)}
BASE = {
    (0, 6): {0: '101101', 2: '000000'},
    (0, 7): {0: '0101101', 2: '0011101'},
    (0, 8): {0: '01011101', 2: '00111101'},
    (1, 5): {1: '10110', 2: '00010'},
    (1, 6): {1: '010110', 2: '001110'},
    (1, 7): {1: '0101110', 2: '0011110'},
    (2, 7): {0: '1110101', 1: '1011010', 2: '0000000'},
    (2, 8): {0: '11110101', 1: '10111010', 2: '00011010'},
    (2, 9): {0: '101101011', 1: '010101010', 2: '000000011'},
}
SMALL_LOOP='101'
EQUAL_LOOPS=('1011101','1101101')

def eval_word(word):
    q,r,e,k = 0,0,1,0
    for ch in word:
        a = int(ch)
        target,eta,b = EDGES[q][a]
        q,r,e,k = target,DELTA[r][a],eta*e,eta*k+b
    return q,r,e,k

def base_test():
    effects={}
    for (q,j), words in BASE.items():
        assert set(words) == set(MODES[q])
        assert all(len(w)==j for w in words.values())
        observed={eval_word(w) for w in words.values()}
        assert all(z[0]==q for z in observed)
        assert {z[1] for z in observed}==set(MODES[q])
        assert len({z[2:] for z in observed})==1
        effects[f'{q},{j}']=list(next(iter(observed))[2:])
    assert eval_word(SMALL_LOOP)==(0,0,1,-1)
    assert eval_word(EQUAL_LOOPS[0])==(0,0,1,-3)
    assert eval_word(EQUAL_LOOPS[1])==(0,0,1,-3)
    return effects

def construct(q, m, mode, bits=None):
    assert m>=7 and mode in MODES[q]
    j=next(j for qq,j in BASE if qq==q and j<=m and (m-j)%3==0)
    h=(m-j)//3
    K,r=divmod(h,7)
    if bits is None: bits='0'*(3*K)
    assert len(bits)==3*K and set(bits)<=set('01')
    pre=''.join(EQUAL_LOOPS[int(b)] for b in bits)+SMALL_LOOP*r
    path=pre+BASE[q,j][mode]
    assert len(path)==m
    q0,mode0,e0,k0=eval_word(BASE[q,j][mode])
    assert (q0,mode0)==(q,mode)
    expected=(q,mode,e0,k0-e0*(9*K+r))
    assert eval_word(path)==expected
    return path,expected,K,r,j

def states_step(d):
    out=defaultdict(int)
    for (q,r,e,k),n in d.items():
        for a,(t,eta,b) in enumerate(EDGES[q]):
            out[t,DELTA[r][a],eta*e,eta*k+b]+=n
    return dict(out)

def fibers_at(d):
    ff=defaultdict(dict)
    for (q,r,e,k),n in d.items():
        ff[q,e,k][r]=n
    return ff

def dp_test(limit=160):
    d={(0,0,1,0):1}; maxima=[]
    for m in range(limit+1):
        assert sum(d.values())==2**m
        ff=fibers_at(d)
        max_per_q={q:max([len(v) for (qq,*_),v in ff.items() if qq==q] or [0]) for q in range(3)}
        if m<=9: maxima.append({'depth':m,'mode_counts_by_q':max_per_q})
        if m>=7:
            assert all(any(qq==q and set(MODES[q]).issubset(v) for (qq,*_),v in ff.items()) for q in range(3))
        if m<=13:
            brute=defaultdict(int)
            for t in product('01',repeat=m):
                brute[eval_word(t)]+=1
            assert dict(brute)==d
        d=states_step(d)
    assert maxima[6]['mode_counts_by_q'][2]<3
    assert maxima[7]['mode_counts_by_q']=={0:2,1:2,2:3}
    return maxima

def construction_test(limit=511):
    probes=0
    for m in range(7,limit+1):
        for q in range(3):
            for mode in MODES[q]:
                _,effect,K,r,j=construct(q,m,mode)
                assert r in range(7)
                probes+=1
    # All 2^3 prefix alternatives for m=28, q=2 and all 3 source modes.
    exact_collision=[]
    for bits in product('01',repeat=3):
        for mode in MODES[2]:
            word,e,K,r,j=construct(2,28,mode,''.join(bits))
            exact_collision.append((word,e))
    assert len({w for w,_ in exact_collision})==24
    assert len({(a,c,d) for _,(a,b,c,d) in exact_collision})==1
    assert {e[1] for _,e in exact_collision}=={0,1,2}
    return {'tested_depths':[7,limit],'constructed_word_checks':probes,'depth28_raw_paths':24}

def main():
    base_effects=base_test()
    maxima=dp_test()
    constructive=construction_test()
    print(json.dumps({'schema':'EM_R260_AUTHOR_EXACT_VERIFICATION_V1',
       'result':'PASS','maxima_0_9':maxima,'base_effects':base_effects,
       'constructive':constructive,'source_equivalence':'UNVERIFIED_NATIVE',
       'R193_contract':'NOT_LOCATED','independent_review':False},indent=2,sort_keys=True))

if __name__=='__main__': main()
