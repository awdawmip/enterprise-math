#!/usr/bin/env python3
"""Exact R674 V29 figure-eight count ledger + declared V17 block coupling.
Uses stdlib only; loop-completion frame update is an explicit model assumption.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

o=(0,0,0,0,0,0)
def e(k): return tuple(int(i==k) for i in range(6))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
A=(o,e(0),plus(e(0),e(1)),e(1),o)
B=(o,e(2),plus(e(2),e(3)),e(3),o)
cycles={'A':A,'B':B}
ports={'A':0,'B':2}
H={(p,p) for p in range(4)}
vertices=set(A)|set(B)
assert len(vertices)==7 and set(A)&set(B)=={o}
assert all(sum(abs(x-y) for x,y in zip(v,w))==1
           for path in (A,B) for v,w in zip(path,path[1:]))
g={'A':(0,2,1),'B':(2,1,0)} # known exact V17 A,B block holonomies
identity=(0,1,2)
def mul(p,q): return tuple(p[q[i]] for i in range(3))
assert mul(g['A'],g['A'])==identity
assert mul(g['B'],g['B'])==identity
assert mul(g['A'],g['B'])==(1,2,0)
assert mul(g['B'],g['A'])==(2,0,1)

def execute(word):
    rin=Counter(); rout=Counter(); M=Counter(); h=identity
    for letter in word:
        path=cycles[letter]; port=ports[letter]
        for x,y in zip(path,path[1:]):
            assert (port,port) in H
            rout[(x,port)]+=1
            rin[(y,port)]+=1
            assert sum(rin.values())==sum(rout.values())
        # After four V29 TRANSFERs, explicitly execute a closed V17 block.
        h=mul(h,g[letter])
    u={(x,p):rin[(x,p)]-rout[(x,p)] for x in vertices for p in range(4)}
    return {'rin':rin,'rout':rout,'M':M,'u':u,
            'Q':sum(u.values()),'h':h}

ab=execute('AB');ba=execute('BA')
assert all(ab[x]==ba[x] for x in ('rin','rout','M','u','Q'))
assert ab['h']==(1,2,0) and ba['h']==(2,0,1)
assert not ab['M'] and not ba['M']
assert all(v==0 for v in ab['u'].values())

def words(m,n):
    for inds in combinations(range(m+n),m):
        w=['B']*(m+n)
        for idx in inds:w[idx]='A'
        yield ''.join(w)

spectra={}; examples={}; checked=0; fiber_tests=0
for m in range(5):
    for n in range(5):
        counts=Counter(); reference=None
        for w in words(m,n):
            checked+=1; state=execute(w)
            signature=tuple(state[k] for k in ('rin','rout','M','u','Q'))
            if reference is None:reference=signature
            else:
                assert signature==reference
                fiber_tests+=1
            assert state['Q']==0 and not any(state['u'].values())
            counts[str(state['h'])]+=1
        assert len(counts)==min(3,min(m,n)+1),(m,n,counts)
        spectra[f'{m},{n}']=len(counts)
        if (m,n) in ((1,1),(2,2),(3,3)):
            examples[f'{m},{n}']=dict(sorted(counts.items()))
assert examples['2,2']=={
    '(0, 1, 2)':4,'(1, 2, 0)':1,'(2, 0, 1)':1}
result={
 'schema':'R674_V29_DOUBLE_LOOP_V17_NONABELIAN_FIBER_V1',
 'scope':'V29 H_diag + two 4-transfer X6 loops sharing one of seven Cells + explicit V17 block-completion frame coupling; no native autonomous V27 scheduler claimed',
 'cells':len(vertices), 'directed_edges':8,
 'loop_A':A,'loop_B':B,
 'H_diag':sorted([list(x) for x in H]),
 'V17_A':g['A'],'V17_B':g['B'],
 'AB_h':ab['h'],'BA_h':ba['h'],
 'full_V29_ledger_AB_BA_identical':True,
 'all_end_of_loop_u_zero':True,
 'network_Q_zero_after_every_transfer':True,
 'spectra_0_to_4':spectra,
 'sample_distributions':examples,
 'exact_words_checked':checked,
 'same_ledger_checks':fiber_tests, 'pass':True}
Path(__file__).with_name('R674_EVIDENCE.json').write_text(
  json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
print('R674_V29_TWO_LOOP_LEDGER_HOLONOMY_FIBER_EXACT_PASS')
print(checked, fiber_tests, examples['2,2'])
