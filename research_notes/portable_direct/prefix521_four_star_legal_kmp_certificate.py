#!/usr/bin/env python3
"""Exact PREFIX-521 certificate: four-STAR legal macro-language KMP/source readouts.
Pure Python standard library, integer K4, explicit BRC branch words.
"""
import json
from itertools import permutations
from collections import Counter

# Axis index: 0=L1=AB,1=L2=CD,2=L3=AC,3=L4=BD,4=L5=BC,5=L6=AD
AXES=((0,1),(2,3),(0,2),(1,3),(1,2),(0,3))
STARS=({0,2,5},{0,3,4},{1,2,4},{1,3,5})
PERMS=list(permutations(range(4)))
MAPS=[tuple(AXES.index(tuple(sorted((g[u],g[v])))) for u,v in AXES) for g in PERMS]

def neighbors(star,phase):
    return {(-1 if phase>0 else 1)*(a+1) for a in STARS[star] if a!=abs(phase)-1}

def successors(s):
    star,prev,now=s
    stay=neighbors(star,now)-{prev}
    new_star=[i for i in range(4) if i!=star and abs(now)-1 in STARS[i]]
    assert len(stay)==1 and len(new_star)==1
    options=sorted((star,now,z) for z in stay)+sorted((new_star[0],now,z) for z in neighbors(new_star[0],now))
    assert len(options)==3
    return options

STATES=[(s,prev,phase) for s in range(4) for a in sorted(STARS[s])
        for sign in (-1,1) for phase in [sign*(a+1)] for prev in sorted(neighbors(s,phase))]
assert len(STATES)==len(set(STATES))==48

def micro(old,new,branch):
    assert old*new<0 and abs(old)!=abs(new)
    # inner via pivot or outer via sum; both primitive native two-step BRC alternatives.
    return (-old,new) if branch==0 else (new,-old)

def color(signed_axis,amap):
    axis=amap[abs(signed_axis)-1]
    if axis==0: return 0 if signed_axis>0 else 4
    if axis==1: return 1 if signed_axis>0 else 2
    if axis==2: return 3
    return 4

def kmp_table(pattern):
    tab={}
    for q in range(4):
        for c in range(5):
            z=pattern[:q]+(c,)
            # prefix-suffix matcher with full-match q=3 retained as a state.
            tab[q,c]=next(k for k in range(3,-1,-1)
                      if k==0 or z[-k:]==pattern[:k])
    return tab
TABS={"aab":kmp_table((0,0,1)),"aba":kmp_table((0,1,0))}

def orders(word):
    first=tuple(dict.fromkeys(abs(x)-1 for x in word))
    last=tuple(dict.fromkeys(abs(x)-1 for x in word[::-1]))
    return first,last

def merge_uniq(a,b):
    return a+tuple(x for x in b if x not in a)

def expected_source(order,amap):
    # source B is L2, C is L3, both signs; after relabeling by amap.
    for i in order:
        if amap[i]==1: return 'B'
        if amap[i]==2: return 'C'
    return 'N'

def direct_source(word,amap,reverse=False):
    seq=word[::-1] if reverse else word
    return expected_source(tuple(abs(x)-1 for x in seq),amap)

summary=Counter()
by_depth=Counter()
witnesses={}

# Enumerate all 48 starts and all 0..3 legal macrochoices (3 exits x 2 BRC branches).
# Exhaustively compare direct KMP with proposed 6-axis first/last-order quotient for all 24 frames.
def examine(start,state,word,first,last,depth):
    summary['histories']+=1
    by_depth[depth]+=1
    assert orders(word)==(first,last)
    summary['order_reconstruction_checks']+=1
    if word:
        l=word[-1]
        assert l in range(-6,0) or l in range(1,7)
    else:l=None
    for h,amap in enumerate(MAPS):
        source_first=expected_source(first,amap)
        source_last=expected_source(last,amap)
        assert source_first==direct_source(word,amap)
        assert source_last==direct_source(word,amap,True)
        summary['first_last_frame_checks']+=1
        colors=tuple(color(x,amap) for x in word)
        # The crucial legality facts are absence of every a-b adjacent pair
        # and every a-a adjacent pair, so both gates are unreachable from q0.
        assert all(colors[i:i+2]!=(0,0) and colors[i:i+2]!=(0,1)
                   for i in range(len(colors)-1))
        assert all(colors[i:i+3] not in ((0,0,1),(0,1,0))
                   for i in range(len(colors)-2))
        expected=1 if l is not None and l>0 and amap[abs(l)-1]==0 else 0
        for gate,tab in TABS.items():
            q=0
            for c in colors:q=tab[q,c]
            assert q==expected and q in (0,1)
            summary['KMP_gate_frame_checks']+=1
    if depth==3:return
    for next_state in successors(state):
        for beta in range(2):
            chunk=micro(state[2],next_state[2],beta)
            cf,cl=orders(chunk)
            newfirst=merge_uniq(first,cf)
            newlast=merge_uniq(cl,last)
            assert orders(word+chunk)==(newfirst,newlast)
            summary['legal_extension_checks']+=1
            examine(start,next_state,word+chunk,newfirst,newlast,depth+1)

for s in STATES:
    examine(s,s,(),(),(),0)

# Independent checks: across all 288 primitive microchoices, every block has same sign,
# two distinct axes from one STAR, and opposite sign relative to subsequent block.
for s in STATES:
    for t in successors(s):
        for beta in range(2):
            x,y=micro(s[2],t[2],beta)
            assert x*y>0 and abs(x)!=abs(y)
            assert abs(x)-1 in STARS[t[0]] and abs(y)-1 in STARS[t[0]]
            summary['native_BRC_microbranch_checks']+=1

# Explicit nontrivial witness showing the theorem has reachable q=1 and B/C,
# so it is not merely empty-language vacuity.
for s in STATES:
    for t in successors(s):
        for b in range(2):
            word=micro(s[2],t[2],b)
            fs,ls=orders(word)
            if word[-1]==1 and any(expected_source(fs,a)!='N' for a in MAPS):
                witnesses={'start':list(s),'next':list(t),'branch':b,'microtrace':list(word),
                           'first_axis_order_L1_based':[i+1 for i in fs],
                           'last_axis_order_L1_based':[i+1 for i in ls]}
                break
        if witnesses:break
    if witnesses:break
assert witnesses
assert summary['histories']==48*(1+6+6**2+6**3)
assert summary['KMP_gate_frame_checks']==summary['histories']*24*2
assert summary['first_last_frame_checks']==summary['histories']*24
assert summary['native_BRC_microbranch_checks']==48*6
report={
  'status':'ALL_CHECKS_PASS',
  'theorem':'for all legal phase-aligned four-STAR microtrace words and all 24 S4 frames: KMP(q0) for both aab/aba is 1 iff last signed step becomes +L1, else 0; first/last B/C sources factor through ordered first/last occurrences of the six native axes',
  'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  'scope':'PREFIX-518 candidate directed phase-switch groupoid, native signed X6 inner/outer shortest microbranches; arbitrary legal future macroedge concatenation; initial KMP q0 only',
  'exact_arithmetic':True,
  'full_KMP_arbitrary_initial_maps_retained_for_other_operation_horizons':True,
  'branch_history_retained_when_indexed_intermediate_Cell_queries_are_requested':True,
  'phase_states':len(STATES),'frames':len(MAPS),'gate_patterns':list(TABS),
  'max_macrosteps_enumerated':3,
  'counts':dict(summary),'by_depth':dict(sorted(by_depth.items())),
  'witness':witnesses
}
print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
