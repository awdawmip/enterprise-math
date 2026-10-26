#!/usr/bin/env python3
"""Exact verifier for EC48E's single-tied-history constructive lemma.
Arithmetic is Fraction throughout. No external dependencies.
"""
from fractions import Fraction as F
from random import Random
from collections import Counter
import json

rng=Random(480527)
stats=Counter()
examples=[]

def verify_model(P,Q,H,Y):
    # P and Q are positive integer matrices, row-major. Normalization is separate.
    assert len(P)==len(Q)==H*Y and min(P)>0 and min(Q)>0
    rat=[F(p,q) for p,q in zip(P,Q)]
    values=sorted(set(rat))
    ties={r:{i//Y for i,x in enumerate(rat) if x==r} for r in values}
    if any(len(s)>1 for s in ties.values()):
        stats['cross_history_collision_models']+=1
        return None
    stats['eligible_models']+=1
    # Every open gap has a rational sample (0,first), (adjacent midpoint), (last,infinity).
    probes=[values[0]/2]+[(u+v)/2 for u,v in zip(values,values[1:])]+[values[-1]+1]
    kh=max(len({tuple(int(rat[h*Y+y]>lam) for y in range(Y)) for h in range(H)}) for lam in probes)
    assert 1<=kh<=min(H,2**Y)
    stats[f'K_hull_{kh}']+=1
    sumP=sum(P); sumQ=sum(Q)
    p=[F(x,sumP) for x in P];q=[F(x,sumQ) for x in Q]
    for r in values:
        # Raw ratio r is normalized to r_norm for the p,q support objective.
        r_norm = r * F(sumQ,sumP)
        tied_hist=next(iter(ties[r]))
        a=[tuple(int(rat[h*Y+y]>=r) for y in range(Y)) for h in range(H)]
        b=[tuple(int(rat[h*Y+y]> r) for y in range(Y)) for h in range(H)]
        assert len(set(a))<=kh and len(set(b))<=kh
        common={a[h] for h in range(H) if h!=tied_hist}
        assert all(a[h]==b[h] for h in range(H) if h!=tied_hist)
        mix_bank=(a[tied_hist] in common and b[tied_hist] in common)
        if mix_bank:
            decoder_words=list(sorted(common))
            case='encoder_mixing'
        else:
            decoder_words=list(sorted(common))+['variable']
            case='private_decoder_row'
        assert len(decoder_words)<=kh
        stats[case]+=1
        for s in [F(0),F(1,7),F(1,2),F(6,7),F(1)]:
            # Actual factorization into K or fewer decoder rows and conditional
            # encoder probabilities, not merely checking the target w directly.
            dec=[([F(x) for x in word] if word!='variable'
                  else [s*aa+(1-s)*bb for aa,bb in zip(a[tied_hist],b[tied_hist])])
                 for word in decoder_words]
            enc=[]
            for h in range(H):
                probabilities=[F(0)]*len(decoder_words)
                if h!=tied_hist:
                    probabilities[decoder_words.index(a[h])]=F(1)
                elif mix_bank:
                    probabilities[decoder_words.index(a[h])]+=s
                    probabilities[decoder_words.index(b[h])]+=1-s
                else:
                    probabilities[-1]=F(1)
                assert sum(probabilities)==1
                enc.append(probabilities)
            w=[sum(enc[h][m]*dec[m][y] for m in range(len(dec)))
               for h in range(H) for y in range(Y)]
            expected=[s*aa+(1-s)*bb for aa,bb in zip(a[tied_hist],b[tied_hist])]
            assert w[tied_hist*Y:(tied_hist+1)*Y]==expected
            for h in range(H):
                if h!=tied_hist: assert w[h*Y:(h+1)*Y]==[F(x) for x in a[h]]
            alpha=sum(p[i]*w[i] for i in range(H*Y))
            beta=sum(q[i]*w[i] for i in range(H*Y))
            support=sum(max(p[i]-r_norm*q[i], F(0)) for i in range(H*Y))
            tied_q=sum(q[i] for i in range(H*Y) if rat[i]==r)
            assert alpha-r_norm*beta==support
            assert sum(q[i]*w[i] for i in range(H*Y) if rat[i]==r)==s*tied_q
            stats['fraction_certificates']+=1
        stats['critical_faces']+=1
    return (kh,len(values))

# Explicit example with repeated ratios WITHIN each history, but never ACROSS histories.
P0=[2,2,7, 3,6,3, 5,10,5, 11,11,22]
Q0=[1,1,1, 1,2,1, 1,2,1, 1,1,2]
e=verify_model(P0,Q0,4,3)
assert e is not None
examples.append({'case':'intra_history_ties_without_cross_history_collision','H':4,'Y':3,'raw_P':P0,'raw_Q':Q0,'hull_states':e[0], 'critical_values':e[1]})

for H,Y,rounds in [(2,2,50),(3,2,70),(3,3,90),(4,3,120),(5,4,80),(7,4,40)]:
    for _ in range(rounds):
        Q=[rng.randint(1,17) for _ in range(H*Y)]
        P=[rng.randint(1,59) for _ in range(H*Y)]
        verify_model(P,Q,H,Y)
        stats['total_models']+=1

print(json.dumps({'schema':'EC48E_EXACT_VERIFICATION_V1',
 'seed':480527,'mode':'exact_rational_constructive_verification',
 'status':'PASS','stats':dict(sorted(stats.items())),'examples':examples,
 'scope':'Only cross-history collision-free models are tested; algebraic theorem covers all such finite positive laws.'},ensure_ascii=False,indent=2))
