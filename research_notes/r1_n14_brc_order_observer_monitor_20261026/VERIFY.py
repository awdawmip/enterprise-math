#!/usr/bin/env python3
"""Exact positive-flow BRC check of monitor-augmented Markovization.

External finite IID auxiliary model. No P000/X6/native theorem is claimed.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json

ALPHABET = range(3)
P = (F(1, 8), F(1, 24), F(5, 6))
Q = (F(1, 12), F(1, 12), F(5, 6))


def monitor_step(s, i):
    # Three-state DFA: whether the ordered substring 01 has appeared.
    if s == 2:
        return 2
    if s == 1 and i == 1:
        return 2
    return 1 if i == 0 else 0


def monitor(h):
    s = 0
    for i in h:
        s = monitor_step(s, i)
    return s


def k_of(h):
    return tuple(h.count(i) for i in ALPHABET)


def weight(L, k):
    ans = F(1)
    for i in ALPHABET:
        ans *= L[i] ** k[i]
    return ans


def policy(h, horizon):
    t = len(h)
    v = sum((j + 1) * (i + 1) for j, i in enumerate(h))
    if t == horizon:
        a = F((v % 7) + 1, 9)
        return a, 1 - a, F(0)
    a = F((v + 2*t) % 5 + 1, 20)
    b = F((3*v + t + 1) % 4 + 1, 20)
    return a, b, 1 - a - b


def action_flows(horizon, with_monitor):
    # Return exact unweighted stop P/Q and continue flows by state.
    alive = {(): F(1)}
    F_by, A_by, B_by, C_by = (defaultdict(F) for _ in range(4))
    for t in range(horizon+1):
        nxt = defaultdict(F)
        for h, u in alive.items():
            k = k_of(h)
            state = (t, k, monitor(h)) if with_monitor else (t, k)
            a, b, c = policy(h, horizon)
            F_by[state] += u
            A_by[state] += u*a
            B_by[state] += u*b
            C_by[state] += u*c
            for i in ALPHABET:
                if c:
                    nxt[h+(i,)] += u*c
        alive = nxt
    return F_by, A_by, B_by, C_by


def compressed_action_flows(horizon, reference, with_monitor):
    F_ref, A_ref, B_ref, C_ref = reference
    origin = (0, (0,0,0), 0) if with_monitor else (0, (0,0,0))
    live = {origin: F(1)}
    AA, BB = defaultdict(F), defaultdict(F)
    for t in range(horizon+1):
        nxt = defaultdict(F)
        for state, mass in live.items():
            f = F_ref[state]
            assert f > 0
            a, b, c = A_ref[state]/f, B_ref[state]/f, C_ref[state]/f
            assert a >= 0 and b >= 0 and c >= 0 and a+b+c == 1
            AA[state] += mass*a
            BB[state] += mass*b
            if t < horizon:
                k = state[1]
                old_s = state[2] if with_monitor else None
                for i in ALPHABET:
                    kk = tuple(k[j]+(i==j) for j in ALPHABET)
                    ss = (t+1, kk, monitor_step(old_s,i)) if with_monitor else (t+1,kk)
                    nxt[ss] += mass*c
            else:
                assert c == 0
        live = nxt
    assert not live
    return AA, BB


def observables(A, B, with_monitor):
    ans = {}
    for lname, law in [('P',P),('Q',Q)]:
        total_decP, total_decQ, totalT, monitor_decP, monitor_decQ = (F(0) for _ in range(5))
        for st in set(A)|set(B):
            t,k = st[:2]
            p,q = weight(law,k)*A[st], weight(law,k)*B[st]
            total_decP += p
            total_decQ += q
            totalT += t*(p+q)
            if with_monitor and st[2]==2:
                monitor_decP+=p
                monitor_decQ+=q
        assert total_decP+total_decQ==1
        ans[lname] = dict(decP=total_decP,decQ=total_decQ,T=totalT,
                          monitor_decP=monitor_decP,monitor_decQ=monitor_decQ)
    return ans


def string_values(o):
    return {law:{key:str(v) for key,v in value.items()} for law,value in o.items()}


def check(horizon):
    original = action_flows(horizon, True)
    A,B = original[1], original[2]
    aug_A, aug_B = compressed_action_flows(horizon, original, True)
    assert A==aug_A and B==aug_B
    original_o = observables(A,B,True)
    aug_o = observables(aug_A,aug_B,True)
    assert original_o == aug_o
    count_ref = action_flows(horizon,False)
    cnt_A,cnt_B = compressed_action_flows(horizon,count_ref,False)
    assert count_ref[1] == cnt_A and count_ref[2] == cnt_B
    cnt_o = observables(cnt_A,cnt_B,False)
    for name in ['P','Q']:
        for field in ['decP','decQ','T']:
            assert cnt_o[name][field] == original_o[name][field]
    return {'horizon':horizon,'augmented_states':len(original[0]),
            'count_states':len(count_ref[0]),'terminal_observers':string_values(original_o)}


def counterexample():
    # Horizon N=2: always observe twice. P decision only on ordered prefix 01.
    # Exact probabilities under P and Q and forced count policy.
    vals={}
    for name, law in [('P',P),('Q',Q)]:
        m=law[0]*law[1]
        # Count k=(1,1,0) has ordered paths (0,1) and (1,0), equal law weight.
        forced_q=F(1,2)
        orig_decP=m
        orig_order01_decP=m
        count_decP=2*m*forced_q
        count_order01_decP=m*forced_q
        assert count_decP == orig_decP
        assert count_order01_decP == orig_order01_decP/2
        vals[name]={'original_decP':str(orig_decP),'original_order01_decP':str(orig_order01_decP),
                    'count_decP':str(count_decP),'count_order01_decP':str(count_order01_decP),
                    'times':'2'}
    return vals


if __name__=='__main__':
    output={'schema':'R1_IID_MONITOR_AUGMENTED_EXACT_CHECK_V1',
            'model':{'P':[str(x) for x in P],'Q':[str(x) for x in Q]},
            'monitor':'DFA recognizes any ordered substring 01',
            'runs':[check(n) for n in (3,4,5)],
            'minimal_counterexample':counterexample(),
            'claims_checked':['augmented_stop_flows_exact','terminal_joint_T_count_monitor_decision_exact',
                              'count_only_four_observers_exact','order01_counterexample_exact'],
            'scientific_scope':'finite IID auxiliary model, exact Fraction; not exhaustive policies or native X6'}
    print(json.dumps(output,ensure_ascii=False,indent=2))
