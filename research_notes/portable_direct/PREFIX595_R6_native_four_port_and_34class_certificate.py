#!/usr/bin/env python3
"""PREFIX-595-R6: exact four-port law and 34-class BRC Markov quotient.
Reuses frozen published PREFIX565 kernel and PREFIX591 exact W3; stdlib only.
"""
from collections import Counter
from fractions import Fraction
import json
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN,PHASES,ACTIONS,ROOTS,ZERO_ROOT,edge
from PREFIX591_R6_unbounded_cubic_observer_invariant_module_certificate import W
assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(ACTIONS)==6 and len(ROOTS)==9
U=W[3]
assert len(U.vectors)==33 and U.contains([1]*96)
group={}
for i in range(96):
    group.setdefault(tuple(v[i] for v in U.vectors),[]).append(i)
classes=sorted(group.values(),key=lambda p:p[0])
assert len(classes)==34
clof={p:k for k,g in enumerate(classes) for p in g}
def outgoing(port,root):
    for a in ACTIONS:
        j,w=edge(port,a,root)
        t=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
        yield j,w,(t,w[0]+w[1],w[2]+w[3]),a
# Exact strong lumpability: 9 roots x 96 ports, with triple rewards.
nchecks=0
for root in ROOTS:
    for k,ports in enumerate(classes):
        ref=Counter((sig,clof[j]) for j,w,sig,a in outgoing(ports[0],root))
        for p in ports:
            assert Counter((sig,clof[j]) for j,w,sig,a in outgoing(p,root))==ref
            nchecks+=1
assert nchecks==864
# Verify rank 33 of the 34 distinct evaluation rows over Q.
piv={}
for ports in classes:
    row=[v[ports[0]] for v in U.vectors]
    for p,r in sorted(piv.items()):
        if row[p]:
            q=row[p]
            row=[x-q*y for x,y in zip(row,r)]
    j=next((j for j,x in enumerate(row) if x),None)
    if j is not None:
        q=row[j];piv[j]=[x/q for x in row]
assert len(piv)==33
assert all(v[6]+v[29]==v[7]+v[28] for v in U.vectors)
# Full native 7-reward and exact destination port, not merely triple law.
# Equality of nonnegative integer kernels => all-length equality by conditioning.
raw_checks=0
for root in ROOTS:
    for a,b in ((6,7),(30,31)):
        left=Counter((j,w) for i in (a,29) for j,w,sig,act in outgoing(i,root))
        right=Counter((j,w) for i in (b,28) for j,w,sig,act in outgoing(i,root))
        assert left==right and sum(left.values())==12
        raw_checks+=1
assert raw_checks==18
# Scope witness: keep action identifier in observed tuple and equality fails.
l=Counter((act,j,w) for i in (6,29) for j,w,sig,act in outgoing(i,ZERO_ROOT))
r=Counter((act,j,w) for i in (7,28) for j,w,sig,act in outgoing(i,ZERO_ROOT))
difference=[(act,j,w,l[act,j,w]-r[act,j,w])
            for act,j,w in sorted(set(l)|set(r)) if l[act,j,w]!=r[act,j,w]]
assert len(difference)==4
out={'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
     'native_ports':96,'actions':6,'allowed_roots':len(ROOTS),
     'strong_lumping_classes':34,'lumpability_checks':nchecks,
     'linear_observer_rank':len(piv),
     'four_class_affine_relation':{'positive_class_indices':[3,15],
                                    'negative_class_indices':[4,14]},
     'full7_next_port_kernel_checks':raw_checks,
     'start_law_A':{'6':'1/2','29':'1/2'},
     'start_law_B':{'7':'1/2','28':'1/2'},
     'action_labeled_difference_terms':len(difference),
     'zero_root_action_difference':[{'action':list(a),'destination_port':j,
         'reward7':list(w),'difference_raw_count':c} for a,j,w,c in difference]}
print('ALL_CHECKS_PASS')
print(json.dumps(out,ensure_ascii=False,indent=2))
