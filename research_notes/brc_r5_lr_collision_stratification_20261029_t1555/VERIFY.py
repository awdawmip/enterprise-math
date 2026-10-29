#!/usr/bin/env python3
"""Exact, dependency-free exhaustive verifier for an external two-law stopping model.

Finite exhaustive scope: 144 FULL deterministic policies, 48 LR policies at
eta=0, 144 LR policies at each nonzero checked eta; 25 fixed-collision kernel
perturbations. Arbitrary-real optimality and image equality use the accompanying
mathematical proof, not numerical sampling.
"""
from fractions import Fraction as F
from itertools import product

A, B = 0, 1
STOP_P, STOP_Q, CONT = 'P', 'Q', 'C'
ACTIONS = (STOP_P, STOP_Q, CONT)
Y = (1, 0)
BASE_P = (F(9,10), F(3,5))
W = (F(1),F(1),F(1,8),F(1,8))


def laws(eta, alpha=F(0), beta=F(0)):
    assert -F(1,20) < eta < F(1,20)
    p_source = (F(1,2)+eta, F(1,2)-eta)
    q_source = (F(1,2), F(1,2))
    p_plus = (BASE_P[0]+alpha, BASE_P[1]+beta)
    assert all(F(0)<p<F(1) for p in p_source+p_plus)
    return p_source, q_source, p_plus


def lr_keys(eta, alpha=F(0), beta=F(0)):
    pp, qq, plus = laws(eta,alpha,beta)
    first = tuple(pp[i]/qq[i] for i in (A,B))
    second = tuple((first[i]*(2*plus[i]), first[i]*(2*(1-plus[i]))) for i in (A,B))
    return first, second


def obs(eta, first_actions, terminal, alpha=F(0), beta=F(0)):
    pp,qq,plus=laws(eta,alpha,beta)
    eP=eQ=F(0)
    TP=TQ=F(1)
    for i in (A,B):
        act=first_actions[i]
        if act==STOP_P:
            eQ+=qq[i]
        elif act==STOP_Q:
            eP+=pp[i]
        else:
            assert act==CONT
            TP+=pp[i]
            TQ+=qq[i]
            for y in Y:
                py=plus[i] if y==1 else 1-plus[i]
                qy=F(1,2)
                decl=terminal[2*i+(0 if y==1 else 1)]
                if decl==STOP_Q:
                    eP+=pp[i]*py
                elif decl==STOP_P:
                    eQ+=qq[i]*qy
                else:
                    raise AssertionError('terminal declaration must stop')
    return eP,eQ,TP,TQ


def score(o):
    return sum(w*x for w,x in zip(W,o))


def enumerate_observations(eta, alpha=F(0), beta=F(0)):
    first_lr, terminal_lr=lr_keys(eta,alpha,beta)
    full=[]
    compressed=[]
    for acts in product(ACTIONS,repeat=2):
        for dec in product((STOP_P,STOP_Q), repeat=4):
            o=obs(eta,acts,dec,alpha,beta)
            full.append((o,acts,dec))
            class_consistent=(first_lr[A]!=first_lr[B] or acts[A]==acts[B])
            decisions={(i,y):dec[2*i+(0 if y else 1)] for i in (A,B) for y in Y}
            for i in (A,B):
                for y in Y:
                    for j in (A,B):
                        for z in Y:
                            if (i,y)<(j,z) and terminal_lr[i][0 if y else 1]==terminal_lr[j][0 if z else 1]:
                                class_consistent &= decisions[(i,y)]==decisions[(j,z)]
            if class_consistent:
                compressed.append((o,acts,dec))
    return full,compressed


def minval(policies):
    return min(map(lambda x:score(x[0]),policies))


def check_collision():
    first, last=lr_keys(F(0))
    assert first==(F(1),F(1))
    assert last==((F(9,5),F(1,5)),(F(6,5),F(4,5)))
    full,lr=enumerate_observations(F(0))
    assert len(full)==144 and len(lr)==48
    assert minval(full)==F(47,40), minval(lr)==F(5,4)
    assert minval(lr)-minval(full)==F(3,40)
    witness=obs(F(0),(CONT,STOP_P),(STOP_P,STOP_Q,STOP_P,STOP_Q))
    assert witness==(F(1,20),F(3,4),F(3,2),F(3,2))
    assert score(witness)==F(47,40)
    assert all(8*(o[0]+o[1])+o[2]+o[3]>=10 for o,_,_ in lr)
    assert 8*(witness[0]+witness[1])+witness[2]+witness[3]==F(47,5)
    print('eta=0 FULL=144 LR=48 min_FULL=47/40 min_LR=5/4 gap=3/40')
    print('FULL_witness=(1/20,3/4,3/2,3/2) integer_plane_LR>=10 witness=47/5 Linf_bound>=1/30')


def check_splitting():
    etas=(F(-1,100),F(-1,1000),F(-1,10000),F(1,10000),F(1,1000),F(1,100))
    for eta in etas:
        f,l=enumerate_observations(eta)
        keys1,keys2=lr_keys(eta)
        assert keys1[0]!=keys1[1]
        assert len(set(keys2[0]+keys2[1]))==4
        assert len(f)==len(l)==144
        assert {o for o,*_ in f}=={o for o,*_ in l}
        assert minval(f)==minval(l)
    print(f'nonzero_eta_cases={len(etas)} ALL_144_FULL_LR_POLICIES_MATCH EXACT_ACTUAL_IMAGES')
    print('P(full_path)_TV_at_eta_to_eta0=abs(eta); Q_TV=0')


def check_fixed_stratum():
    c=0
    deltas=(F(-1,20),F(-1,40),F(0),F(1,40),F(1,20))
    for alpha,beta in product(deltas,repeat=2):
        p_source,q_source,p_plus=laws(F(0),alpha,beta)
        first,second=lr_keys(F(0),alpha,beta)
        assert first==(1,1) and len(set(second[0]+second[1]))==4
        full,lr=enumerate_observations(F(0),alpha,beta)
        assert len(full)==144 and len(lr)==48
        predicted=F(3,40)+min(alpha,-beta)/2
        assert minval(full)==F(47,40)-alpha/2
        assert minval(lr)==min(F(5,4),F(5,4)-(alpha+beta)/2)
        assert minval(lr)-minval(full)==predicted
        assert predicted>=F(1,20)
        c+=1
    print(f'fixed_collision_kernel_grid={c} exact_gap=3/40+min(alpha,-beta)/2 >=1/20')


if __name__=='__main__':
    check_collision()
    check_splitting()
    check_fixed_stratum()
    print('PASS_EXACT_R5_STRATIFIED_COLLISION_DISCONTINUITY')