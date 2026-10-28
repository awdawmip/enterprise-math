#!/usr/bin/env python3
"""EC49A: exact positivity, non-R and raw four-vector LP projection certificate.
Python stdlib only. All arithmetic is fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

H=(0,1); Z=(0,1); W=(0,1)
QZ={0:F(3,4),1:F(1,4)}
PZ={0:F(1,4),1:F(3,4)}
KW={0:{0:F(3,4),1:F(1,4)},1:{0:F(1,4),1:F(3,4)}}
ACTIONS=['acc','rej','cont']

def fmt(x): return str(x)
def leaf_table():
    rows=[]
    for h,z,w in product(H,Z,W):
        q=F(1,2)*QZ[z]*KW[h][w]
        p=F(1,2)*PZ[z]*KW[h][w]
        rows.append(dict(h=h,z=z,w=w,P=str(p),Q=str(q),LR=str(p/q)))
    assert all(F(r['P'])>0 and F(r['Q'])>0 for r in rows)
    assert sum((F(r['P']) for r in rows),F(0)) == 1
    assert sum((F(r['Q']) for r in rows),F(0)) == 1
    for r in rows: assert F(r['LR']) == PZ[r['z']]/QZ[r['z']]
    return rows

def direct(pi1,pi2,pi3):
    # pi1[h], pi2 are dicts with accept/reject/continue probability.
    # pi3[z,w] is probability of accepting at terminal time.
    alpha=sum((F(1,2)*pi1[h]['acc'] for h in H),F(0))
    beta=alpha
    x2=sum((F(1,2)*pi1[h]['cont'] for h in H),F(0))
    alpha+=x2*pi2['acc']; beta+=x2*pi2['acc']
    x3=x2*pi2['cont']
    for h,z,w in product(H,Z,W):
        live=F(1,2)*pi1[h]['cont']*pi2['cont']*KW[h][w]
        alpha+=live*PZ[z]*pi3[z,w]
        beta+=live*QZ[z]*pi3[z,w]
    et=1+x2+x3
    return (alpha,beta,et,et)

def coarse_from_fine(pi1,pi2,pi3):
    # Q-averaging of terminal control in the source-ancillary W fiber.
    x2=sum((F(1,2)*pi1[h]['cont'] for h in H),F(0))
    x3=x2*pi2['cont']
    a1=sum((F(1,2)*pi1[h]['acc'] for h in H),F(0))
    a2=x2*pi2['acc']
    alpha=beta=a1+a2
    mu={}
    for z in Z:
        mu[z]=(sum((F(1,2)*pi1[h]['cont']*KW[h][w]*pi3[z,w]
                 for h in H for w in W),F(0))/x2 if x2>0 else F(0))
        assert F(0)<=mu[z]<=1
        alpha+=x3*PZ[z]*mu[z]
        beta+=x3*QZ[z]*mu[z]
    et=1+x2+x3
    return (alpha,beta,et,et),mu

def deterministic(action):
    return {a:F(int(a==action)) for a in ACTIONS}

def rand_simplex(rng):
    cuts=sorted([0,rng.randint(0,24),rng.randint(0,24),24])
    return {a:F(cuts[i+1]-cuts[i],24) for i,a in enumerate(ACTIONS)}

def main():
    leaves=leaf_table()
    assert len(leaves)==8
    # Different reachably induced kernels at the exact SAME t2 readout
    # with identical x2=1/2 and LR=1.  t2 always continues.
    pi2=deterministic('cont')
    p0={0:deterministic('cont'),1:deterministic('rej')}
    p1={0:deterministic('rej'),1:deterministic('cont')}
    def kernel_w1(pi1):
        qlive=sum((F(1,2)*pi1[h]['cont'] for h in H),F(0))
        return sum((F(1,2)*pi1[h]['cont']*KW[h][1] for h in H),F(0))/qlive
    assert kernel_w1(p0)==F(1,4)
    assert kernel_w1(p1)==F(3,4)
    # Exact next-readout (Z=1,W=1) kernel is 1/16 versus 3/16.
    assert QZ[1]*kernel_w1(p0)==F(1,16)
    assert QZ[1]*kernel_w1(p1)==F(3,16)
    checked_det=0
    for a_h0,a_h1,a2, bits in product(ACTIONS,ACTIONS,ACTIONS,product((0,1),repeat=4)):
        pi1={0:deterministic(a_h0),1:deterministic(a_h1)}
        pi2=deterministic(a2)
        pi3={pair:F(bit) for pair,bit in zip(product(Z,W),bits)}
        o=direct(pi1,pi2,pi3)
        co,mu=coarse_from_fine(pi1,pi2,pi3)
        assert o==co,(a_h0,a_h1,a2,bits,o,co)
        # Reverse realization: ignore W and choose mu_z at t3.
        pi3_ignored={(z,w):mu[z] for z,w in product(Z,W)}
        assert direct(pi1,pi2,pi3_ignored)==co
        checked_det+=1
    assert checked_det==432
    rng=Random(4901)
    checked_random=0
    for _ in range(1200):
        pi1={h:rand_simplex(rng) for h in H}
        pi2=rand_simplex(rng)
        pi3={(z,w):F(rng.randint(0,24),24) for z,w in product(Z,W)}
        o=direct(pi1,pi2,pi3)
        co,mu=coarse_from_fine(pi1,pi2,pi3)
        assert o==co
        ignored={(z,w):mu[z] for z,w in product(Z,W)}
        assert direct(pi1,pi2,ignored)==co
        checked_random+=1
    special3={(z,w):F(z) for z,w in product(Z,W)}
    special=direct(p0,deterministic('cont'),special3)
    assert special==(F(3,8),F(1,8),F(2),F(2))
    # An explicitly LP-feasible rational target, described by original strategy.
    # The quotient constraints are: sum_a u[h,a]=1/2, x2=sum_h u[h,cont];
    # sum_a v[a]=x2, x3=v[cont]; 0<=w[z]<=x3*QZ[z].
    # alpha=sum_h u[h,acc]+v[acc]+sum_z (PZ[z]/QZ[z])*w[z];
    # beta=sum_h u[h,acc]+v[acc]+sum_z w[z]; ET=1+x2+x3.
    summary={
        'result':'PASS','model':'8 strict-positive rational terminal leaves / 3 decision times',
        'source_probabilities':{'QZ':{str(k):str(v) for k,v in QZ.items()},'PZ':{str(k):str(v) for k,v in PZ.items()},'KW':{str(h):{str(w):str(v) for w,v in KW[h].items()} for h in H}},
        'leaf_table':leaves,
        'non_R_w1_kernels':['1/4','3/4'],
        'non_R_next_readout_z1_w1':['1/16','3/16'],
        'non_R_kernel_gap':'1/8',
        'exact_deterministic_policies':checked_det,
        'seeded_rational_policies':checked_random,
        'exact_controller_vector_reconstructed':checked_det+checked_random,
        'reverse_W_ignoring_policy_checks':checked_det+checked_random,
        'special_four_vector':[str(x) for x in special],
        'arithmetic':'stdlib fractions.Fraction, no float',
        'scope':'fixed 1-state erased-history updater; source-neutral behavioral policies; terminal W ancillary given Z; four O coordinates only',
    }
    print(json.dumps(summary,indent=2,sort_keys=True,ensure_ascii=False))
if __name__=='__main__': main()
