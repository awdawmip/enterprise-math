#!/usr/bin/env python3
"""Exact author-side certificate: four-label full-support BRC sharp tail t=690.
No floats. Exact finite checks supplement, not replace, the analytic proof.
"""
import json
from fractions import Fraction as F
from itertools import product
from math import comb, prod
from pathlib import Path

Q = {'0': (1, 665, 1, 333), '2': (333, 333, 1, 333),
     '3': (1, 1, 1, 997)}
GOOD = ((0, 1), (1, 2), (1, 3), (2, 3))
MASKS = frozenset((1 << i) | (1 << j) for i, j in GOOD)
assert all(min(q) > 0 and sum(q) == 1000 for q in Q.values())

def H(s, b):
    return (1 + b)**s - 1 - b**s

s = 690
h1, h665, h997 = F(1000), F(3,2), F(333,334)
assert 2**s - 2 > h1
assert F(690,665)+F(comb(690,2),665**2) == F(139311,88445) > h665
sum6 = sum((F(comb(s,j),997**j) for j in range(1,7)), F(0))
assert sum6 == F(979335790836921651,982134461213542729)
assert 334*979335790836921651 - 333*982134461213542729 == 47378555422102677 > 0
assert sum6 > h997 and H(s,F(1,997)) >= sum6

odds = {(0,(0,1)):F(1), (1,(0,1)):F(1,665),
        (1,(1,2)):F(1,665), (2,(1,2)):F(1),
        (3,(1,3)):F(1,997), (3,(2,3)):F(1,997)}
for (i,edge),b in odds.items():
    j = edge[0] if edge[1]==i else edge[1]
    assert min(F(q[j],q[i]) for q in Q.values()) == b

C = {}
L = {}
for a,q in Q.items():
    C[a] = [sum(q[j] for i,j in GOOD if i==v)
            +sum(q[i] for i,j in GOOD if j==v) for v in range(4)]
    L[a] = {edge:1000-q[edge[0]]-q[edge[1]] for edge in GOOD}
assert C['0']==[665,335,998,666]
assert C['2']==[333,667,666,334]
assert C['3']==[1,999,998,2]

# Nine independent edge/group charge comparisons.
checks = {
 '0:01': F(665)/h1+F(335)/h665<L['0'][(0,1)],
 '0:12': F(998)/h1<L['0'][(1,2)],
 '0:13+23': (L['0'][(1,3)]+L['0'][(2,3)])*h997==C['0'][3],
 '2:01': F(333)/h1<L['2'][(0,1)],
 '2:12': F(667)/h665+F(666)/h1<L['2'][(1,2)],
 '2:23': F(334)/h997<L['2'][(2,3)],
 '3:01': F(1)/h1+F(999)/h665<L['3'][(0,1)],
 '3:12': F(998)/h1<L['3'][(1,2)],
 '3:13+23': (L['3'][(1,3)]+L['3'][(2,3)])*h997>C['3'][3],
}
assert len(checks)==9 and all(checks.values()),checks

def delta_num(counts, next_action):
    A=[prod(Q[a][i]**counts.get(a,0) for a in Q) for i in range(4)]
    P={(i,j):prod((Q[a][i]+Q[a][j])**counts.get(a,0) for a in Q)
       -A[i]-A[j] for i,j in GOOD}
    return sum(C[next_action][i]*A[i] for i in range(4)) \
        -sum(L[next_action][ij]*P[ij] for ij in GOOD)

def D(t):
    return 4002+1334*997**t-668*998**t-668*2**t

assert D(689)==delta_num({'3':689},'0')>0
assert D(690)==delta_num({'3':690},'0')<0

t=689
r=F(t-3,4*997)
upper = F(t,997)+F(comb(t,2),997**2) + F(comb(t,3),997**3)/(1-r)
assert r==F(343,1994)
assert upper==F(125691779,126239143)<F(249,250)
assert H(t,F(1,997))<upper
assert F(84,125)*997**t+3334-668*2**t>0

def pure3_num(t):
    return 2*(2**t+998**t-997**t-3)

assert 100*pure3_num(400)>29*1000**400
end_num=1000*pure3_num(689)+D(689)
assert 50*end_num<13*1000**690

def dp_num(word):
    state=[0]*16
    state[0]=1
    for a in word:
        nxt=[0]*16
        for mask,count in enumerate(state):
            if count:
                for i,weight in enumerate(Q[a]):
                    nxt[mask|(1<<i)]+=count*weight
        state=nxt
    return sum(state[m] for m in MASKS)

def prod_num(word):
    if not word:
        return 0
    A=[prod(Q[a][i] for a in word) for i in range(4)]
    return sum(prod(Q[a][i]+Q[a][j] for a in word)-A[i]-A[j]
               for i,j in GOOD)

checked=0
for length in range(9):
    for letters in product(Q,repeat=length):
        w=''.join(letters)
        assert dp_num(w)==prod_num(w),w
        checked+=1
assert checked==9841

result = {
 'schema':'EM_BRC_SHARP_TAIL_690_AUTHOR_CERT_V1',
 'model':'auxiliary_four_label_full_support',
 'fixed_actions':{a:list(q) for a,q in Q.items()},
 'good_pairs':list(map(list,GOOD)),
 'strict_negative_occupancy_delta_from_round':691,
 'last_possible_positive_occupancy_and_residual_round':690,
 'positive_witness':'3^689 0',
 'H690_six_term_lower':str(sum6),
 'H690_1_over_997_threshold':str(h997),
 'H690_cross_multiplication_difference':'47378555422102677',
 'H689_upper_certificate':str(upper),
 'edge_or_group_comparisons':checks,
 'exact_short_words_checked':checked,
 'witness_delta690_sign':'POSITIVE',
 'witness_delta691_for_3pow690_then0_sign':'NEGATIVE',
 'witness_prior_delta400_gt_29_over_100':True,
 'witness_final_delta690_lt_13_over_50':True,
 'review_status':'AUTHOR_CHECK_ONLY / DRIVER_UNREVIEWED / NOT_ADMITTED',
}
if __name__=='__main__':
    Path(__file__).with_name('EXACT_EVIDENCE.json').write_text(
        json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',
        encoding='utf-8')
    print('PASS: 3 exact thresholds, 6 ratio directions, 9 flow comparisons')
    print('PASS: 690th-round positive witness and 400th-round historic peak')
    print('PASS: 9841 words of length 0..8, mask DP vs pair product')
    print('AUTHOR THEOREM: sharp negative tail starts round 691')
