#!/usr/bin/env python3
"""Stage304-B portable rational witness: S reveal and time-typed port reset.

External finite, positive-mass branch model only. This program is NOT a
native Heartbeat/X6/BRC kernel or physical-model revalidation.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

HALF = F(1, 2)
P = (F(1, 4), F(3, 4))
Q = (F(1, 8), F(7, 8))  # q_s=P(J=1|S=s), all joint branches positive
EPS = (Q[0] + 1 - Q[1]) / 2


def emission(a, y, rate):
    p = HALF if a == 'H' else rate
    return p if y else 1-p


def tv(u, v):
    return sum((abs(u.get(k, F(0))-v.get(k, F(0))) for k in u.keys() | v.keys()), F(0)) / 2


def law(s, policy, kind, joint=False):
    """Conditional-on-S path mass; source s is revealed BETWEEN rounds 1 and 2.

    kind=orig   : J_ref=S, both F rates p_S
    kind=locked : original J persists, both F rates p_J
    kind=reset  : J_old persists in provenance; second F rate resets to p_S

    Policy pre bits depend only on X; post bits depend on (S,X,Y1), never J.
    Action labels are part of the observable trace.
    """
    assert s in (0, 1) and len(policy) == 10
    out = defaultdict(lambda: F(0))
    for x in (0, 1):
        a1 = policy[x]
        js = (s,) if kind == 'orig' else (0, 1)
        for j in js:
            jw = F(1) if kind == 'orig' else ((1-Q[s]) if j == 0 else Q[s])
            pre_rate = P[s] if kind == 'orig' else P[j]
            for y1 in (0, 1):
                p1 = emission(a1, y1, pre_rate)
                a2 = policy[2 + s*4 + x*2 + y1]
                post_rate = P[s] if kind in ('orig','reset') else P[j]
                for y2 in (0, 1):
                    p2 = emission(a2, y2, post_rate)
                    key = (x, a1, y1, s, a2, y2, j) if joint else (x, a1, y1, s, a2, y2)
                    out[key] += HALF*jw*p1*p2
    assert sum(out.values()) == 1
    assert all(v > 0 for v in out.values())
    return dict(out)


def binom_word_law(rate, n):
    return {bits: product_prob(bits, rate) for bits in product((0,1), repeat=n)}


def product_prob(bits, rate):
    v = F(1)
    for b in bits:
        v *= rate if b else (1-rate)
    return v


def allf_risk(n, tau, kind):
    """n F visits, actual S revealed after tau visits, full labelled S+path."""
    risk = F(0)
    joint_risk = F(0)
    for s in (0, 1):
        ref = {}
        out = {}
        refjoint, outjoint = {}, {}
        for bits in product((0,1), repeat=n):
            ref[bits] = product_prob(bits, P[s])
            wrong = (product_prob(bits, P[1-s]) if kind == 'locked'
                     else product_prob(bits[:tau], P[1-s])*product_prob(bits[tau:], P[s]))
            mismatch = Q[0] if s == 0 else 1-Q[1]
            out[bits] = (1-mismatch)*ref[bits] + mismatch*wrong
            refjoint[bits+(s,)] = ref[bits]
            outjoint[bits+(s,)] = (1-mismatch)*ref[bits]
            outjoint[bits+(1-s,)] = mismatch*wrong
        risk += tv(ref,out)/2
        joint_risk += tv(refjoint,outjoint)/2
    return risk,joint_risk


def D(n):
    return tv(binom_word_law(P[0],n),binom_word_law(P[1],n))


def main():
    assert EPS == F(1,8)
    mx = {'locked': F(0), 'reset': F(0)}
    counts = {'locked': 0, 'reset': 0}
    joint_counts = 0
    policy_count = 0
    # Complete coverage: pre action depends on X (2 nodes); post-reveal
    # action depends on S,X,Y1 (8 nodes): 2^10 = 1024 deterministic policies.
    for policy in product('HF',repeat=10):
        policy_count += 1
        original = {s:law(s,policy,'orig') for s in (0,1)}
        orig_joint = {s:law(s,policy,'orig',joint=True) for s in (0,1)}
        for kind in ('locked','reset'):
            observed = {s:law(s,policy,kind) for s in (0,1)}
            observed_joint = {s:law(s,policy,kind,joint=True) for s in (0,1)}
            risk = sum((tv(original[s],observed[s]) for s in (0,1)),F(0))/2
            joint_risk = sum((tv(orig_joint[s],observed_joint[s]) for s in (0,1)),F(0))/2
            assert risk <= EPS*D(2 if kind=='locked' else 1)
            assert joint_risk == EPS
            if risk > mx[kind]:
                mx[kind] = risk
                counts[kind] = 1
            elif risk == mx[kind]:
                counts[kind] += 1
        joint_counts += 1
    assert policy_count == 1024
    assert mx['locked']==EPS*D(2)==F(1,16)
    assert mx['reset']==EPS*D(1)==F(1,16)
    assert D(3)==F(11,16)
    assert allf_risk(3,1,'locked')==(F(11,128),EPS)
    assert allf_risk(3,1,'reset')==(F(1,16),EPS)
    # All-F controls from any side of revelation are admissible; the general
    # all-n, all-real-q theorem is proved in PROOF_STAGE304B.md, not by enumeration.
    print('branch_coupling=q0:1/8,q1:7/8; epsilon=1/8; pre_nodes=2; post_nodes=8')
    print(f'n2_source_revealed_policies_exhaustive={policy_count}; positivity=PASS; normalization=PASS')
    print(f'n2_locked_max={mx["locked"]}; n2_reset_max={mx["reset"]}; n2_joint_read=1/8')
    print(f'n3_allF_locked={allf_risk(3,1,"locked")[0]}; n3_allF_reset={allf_risk(3,1,"reset")[0]}; n3_joint_read=1/8')
    print(f'D1={D(1)}; D2={D(2)}; D3={D(3)}; terminal_joint_checks={joint_counts*2}')
    print('STAGE304B_SOURCE_REVEAL_RESET_EXACT_PASS')

if __name__ == '__main__':
    main()
