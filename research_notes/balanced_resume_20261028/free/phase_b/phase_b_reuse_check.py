"""Phase B reuse of existing T0/T6; no new general tool family.
Finite totalization at H is only used from layer t with horizon H-t.
"""
import sys,json
from pathlib import Path
sys.path.insert(0,'/workspace/enterprise-math/src')
from enterprise_math.brc_contact_horizon import ContactState,DIRECTIONS,ZERO,distinguishing_contact_word
from enterprise_math.predictive_quotient import finite_horizon_partition,restricted_block_count
from math import comb

def add(x,s): return tuple(a+b for a,b in zip(x,s))
def count(r): return 0 if r<0 else sum(comb(5,j)*comb(r-j+6,6) for j in range(min(5,r)+1))
rows=[]
for H in range(6):
    layers=[{ZERO}]
    for t in range(H): layers.append({add(x,s) for x in layers[-1] for s in DIRECTIONS})
    states=tuple((t,x) for t,layer in enumerate(layers) for x in sorted(layer))
    actions={str(i):(lambda state,s=s: (state[0]+1,add(state[1],s)) if state[0]<H else state)
             for i,s in enumerate(DIRECTIONS)}
    for t,layer in enumerate(layers):
        h=H-t
        classes={ContactState.encode(x,h) for x in layer}
        radius=min(t,h)-((min(t,h)-t)%2)
        expected=count(radius)+int(t>h)
        assert len(classes)==expected
        partition=finite_horizon_partition(states,actions,lambda state:state[1]==ZERO,h)
        n=restricted_block_count(states,partition,tuple((t,x) for x in layer))
        assert n==expected
        # Verify canonical T0's actual transition, without reimplementing it.
        if h:
            for x in layer:
                for s in DIRECTIONS:
                    assert ContactState.encode(x,h).advance(s)==ContactState.encode(add(x,s),h-1)
        # Test the canonical separating-word implementation for every pair of
        # retained classes in this bounded instance, using contact outputs.
        cls=list(classes)
        pairs=0
        for i,a in enumerate(cls):
            for b in cls[i+1:]:
                w=distinguishing_contact_word(a,b)
                aa,bb=a,b
                for s in w:aa,bb=aa.advance(s),bb.advance(s)
                assert aa.contact != bb.contact
                pairs+=1
        rows.append({'H':H,'t':t,'T0_classes':len(classes),'T6_restricted_classes':n,
                     'formula':expected,'canonical_distinguishing_pairs':pairs})
print(json.dumps({'status':'PASS_BOUNDED_REUSE_EXECUTED','modules':['enterprise_math.brc_contact_horizon','enterprise_math.predictive_quotient'],'horizons':list(range(6)),'rows':rows,'universal_proof':'Phase A paper proof; these checks are finite.'},indent=2))
