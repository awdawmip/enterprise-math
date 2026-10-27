#!/usr/bin/env python3
"""Exact finite BRC positive-Q-branch verification, standard-library Fraction only."""
from fractions import Fraction as F
from itertools import product

Y = (F(1, 2), F(1), F(3, 2))
QH = (F(1, 2), F(1, 2))
K = ((F(1, 4), F(1, 2), F(1, 4)), (F(1, 8), F(3, 4), F(1, 8)))
T = 2
U = F(1)
S = F(3, 32)

def four_vector(actions, terminal):
    ep, eq, tp, tq = F(0), F(0), F(0), F(0)
    for h in range(2):
        qh = QH[h]
        ph = qh
        if actions[h] != 'C':
            if actions[h] == 'Q':
                ep += ph
            else:
                eq += qh
            tp += ph*T
            tq += qh*T
        else:
            for j, y in enumerate(Y):
                q = qh*K[h][j]
                p = y*q
                if terminal[h][j] == 'Q':
                    ep += p
                else:
                    eq += q
                tp += p*(T+1)
                tq += q*(T+1)
    return (ep,eq,tp,tq)

def J(v):
    return v[0]+U*v[1]+S*v[3]

def main():
    assert sum(QH)==1
    for kh in K:
        assert all(q>0 for q in kh)
        assert sum(kh)==1
        assert sum(q*y for q,y in zip(kh,Y))==1
    print('BRC_Q_P_positive_normalized: PASS')
    H=tuple(sum(q*min(y,U) for q,y in zip(kh,Y)) for kh in K)
    d=tuple(F(1)-v for v in H)
    assert H==(F(7,8),F(15,16)) and d==(F(1,8),F(1,16))
    print('hinge_H:', ', '.join(map(str,H)))
    print('continuation_value_gains:', ', '.join(map(str,d)))
    full=[]
    for a in product('PQC',repeat=2):
        for labels in product('PQ',repeat=6):
            v=four_vector(a,(labels[:3],labels[3:]))
            full.append(J(v))
    coarse=[]
    for a in 'PQC':
        for lab in product('PQ',repeat=3):
            coarse.append(J(four_vector((a,a),(lab,lab))))
    assert len(full)==576 and len(coarse)==24
    vf=min(full); vc=min(coarse)
    print('full_deterministic_policy_descriptions:',len(full))
    print('coarse_deterministic_policy_descriptions:',len(coarse))
    print('full_value:',vf);print('coarse_value:',vc)
    print('support_gap:',vc-vf)
    assert (vf,vc,vc-vf)==(F(75,64),F(19,16),F(1,64))
    w=four_vector(('C','P'),(('Q','P','P'),('P','P','P')))
    stop=four_vector(('P','P'),(('P',)*3,)*2)
    cont=four_vector(('C','C'),(('Q','P','P'),)*2)
    print('full_witness_four_vector:',', '.join(map(str,w)))
    print('coarse_stop_witness:',', '.join(map(str,stop)))
    print('coarse_continue_witness:',', '.join(map(str,cont)))
    assert w==(F(1,16),F(7,8),F(5,2),F(5,2))
    assert stop==(F(0),F(1),F(2),F(2))
    assert cont==(F(3,32),F(13,16),F(3),F(3))
    assert J(w)==vf and J(stop)==vc and J(cont)==vc
    x=tuple(S-di for di in d)
    pos=sum((QH[h]*x[h] for h in range(2) if x[h]>0),F(0))
    neg=sum((-QH[h]*x[h] for h in range(2) if x[h]<0),F(0))
    print('positive_flow_obstruction:',pos)
    print('negative_flow_obstruction:',neg)
    assert min(pos,neg)==F(1,64)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    main()
