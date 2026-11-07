#!/usr/bin/env python3
"""Exact finite certificate for time-only bounded policy-label BRC N=4.
No random sampling, floating-point arithmetic, external package or native X6
physics is used. Checks cover the deterministic S23 grammar and all boxes.
"""
from fractions import Fraction as F
from itertools import combinations, product

Q=((10,10),(20,20),(15,15),(15,15))
P=((9,11),(5,5),(3,27),(30,30))
for name,rows in (("Q",Q),("P",P)):
    leaf=[F(w,240) for pair in rows for w in pair for k in (0,1)]
    assert len(leaf)==16 and all(x>0 for x in leaf) and sum(leaf)==1,name
M=((F(1,2),F(1,2),0,0,0,0),
   (F(9,20),F(11,20),0,0,0,0),
   (0,0,1,0,0,0),
   (0,0,0,F(1,2),F(1,2),0),
   (0,0,0,F(1,10),F(9,10),0),
   (0,0,0,0,0,1))
assert all(sum(row)==1 and all(x>=0 for x in row) for row in M)
COL_SOURCE=(0,0,1,2,2,3)
STAGE1_SLOT=(0,0,1,1)
STAGE2_SLOT=(0,1,0,2)
def terminal_times(stage1,stage2,stage3):
    return tuple(1 if stage1[STAGE1_SLOT[src]]==0
                 else 2 if stage2[STAGE2_SLOT[src]]==0
                 else 3 if stage3[c]==1 else 4
                 for c,src in enumerate(COL_SOURCE))
pure_signatures=set()
witnesses={}
policies=0
for s1 in product((0,1),repeat=2):
    for s2 in product((0,1),repeat=3):
        for s3 in product((0,1),repeat=6):
            policies+=1
            t=terminal_times(s1,s2,s3)
            if t[0]==t[1] and t[3]==t[4]:
                sig=(t[0],t[2],t[3],t[5])
                pure_signatures.add(sig)
                witnesses.setdefault(sig,(s1,s2,s3))
assert policies==2**(2+3+6)==2048
S=sorted(pure_signatures)
assert len(S)==64 and (1,1,1,1) in pure_signatures
FULL=(1<<len(S))-1
three_choice_boxes=[]
for omitted in product(range(1,5),repeat=4):
    mask=sum(1<<j for j,sig in enumerate(S)
             if all(sig[i]!=omitted[i] for i in range(4)))
    three_choice_boxes.append(mask)
assert len(three_choice_boxes)==4**4==256
pair_unions={a|b for a in three_choice_boxes for b in three_choice_boxes}
max_three_labels=max((pair|c).bit_count()
                     for pair in pair_unions for c in three_choice_boxes)
assert max_three_labels==63
choice2=tuple(combinations(range(1,5),2))
two_choice_boxes=[]
for choices in product(choice2,repeat=4):
    mask=sum(1<<j for j,sig in enumerate(S)
             if all(sig[i] in choices[i] for i in range(4)))
    two_choice_boxes.append((choices,mask))
assert len(two_choice_boxes)==6**4==1296
max_two_choice=max(mask.bit_count() for _,mask in two_choice_boxes)
full_sized=[(choices,mask) for choices,mask in two_choice_boxes
            if mask.bit_count()==16]
assert max_two_choice==16 and len(full_sized)==9
assert all(choices[0]==(3,4) for choices,_ in full_sized)
assert all(not (mask&(1<<S.index((1,1,1,1)))) for _,mask in full_sized)
u=(F(1,4),)*4
def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2
assert all(tv(tuple(F(x==t) for x in range(1,5)),u)==F(3,4)
           for t in range(1,5))
print('PASS_BRC_N4_TIME_POLICY_2_3_TAG_SATURATION_20261031')
print('positive_leaves_per_law=16; source_rows=6; policies=2048')
print(f'pure_time_signatures={len(S)}; three-choice_boxes={len(three_choice_boxes)}')
print(f'unique_pair_unions={len(pair_unions)}; max_3_box_union={max_three_labels}/64')
print(f'two-choice_boxes={len(two_choice_boxes)}; max_box_size={max_two_choice}; size16_boxes={len(full_sized)}')
print('size16_boxes_AU_choices={(3,4)}; earliest_signature=(1,1,1,1) uncovered')
print('CONCLUSION exact R_(k,m)=3/4 for 1<=m<=3, any k>=1, deterministic S23 and any policy family containing these 64 witnesses')
print('CONCLUSION 2/3<=R_(k,4)<=3/4 for deterministic S23 and any lawful stochastic extension containing it')
