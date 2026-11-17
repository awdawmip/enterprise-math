#!/usr/bin/env python3
"""PREFIX-856 exact finite checks for the typed named-BRC modular observer.
No floating point, external packages, or native X6 attribution.
"""
import json, math
P=5
X=range(1<<P)
FULL=(1<<len(X))-1
Q4=(3,5,7,9,11,13,15)
MOVES=tuple(tuple([x]+[x^(1<<i) for i in range(P)]) for x in X)
MASKS={q:tuple(sum(1<<x for x in X if x%q==r) for r in range(q)) for q in range(1,65)}
def coeff(a,b,t):
    assert t>=1
    return pow(a,t//2)*pow(b,(t-1)//2)
def effective_modulus(m,c):return m//math.gcd(m,c)
def post(B):
    out=0
    while B:
        bit=B&-B
        x=bit.bit_length()-1
        B-=bit
        for z in MOVES[x]:out|=1<<z
    return out
def children(B,q):
    Z=post(B)
    return tuple(z for mask in MASKS[q] if (z:=Z&mask))
# Exact rederivation of PREFIX-855 odd-only finite feedback certificate.
states=[FULL]; idx={FULL:0}; edges=[]
for state in states:
    row=[]
    for q in Q4:
        kids=children(state,q)
        row.append(tuple(kids))
        for child in kids:
            if child not in idx:
                idx[child]=len(states)
                states.append(child)
    edges.append(tuple(row))
assert len(states)==1944
winning={b for b in states if b.bit_count()==1}
layers=[len(winning)]
while True:
    new={b for b,row in zip(states,edges) if b not in winning and any(all(c in winning for c in cs) for cs in row)}
    if not new:break
    winning|=new
    layers.append(len(winning))
assert layers==[32,48]
losing=set(states)-winning
assert FULL in losing and len(losing)==1896
assert all(any(c in losing for c in cs) for b,row in zip(states,edges) if b in losing for cs in row)
# Exact observer response isomorphism, with both conversion directions.
checks=0
for a,b in ((2,1),(2,3),(6,5),(1,1)):
    for t in range(1,17):
        c=coeff(a,b,t)
        for m in range(1,65):
            g=math.gcd(m,c)
            q=m//g
            inv=pow(c//g,-1,q) if q>1 else 0
            for S in (0,7):
                for u in X:
                    raw=(c*(S+u))%m
                    assert raw%g==0
                    normalized=((raw//g)*inv-S)%q if q>1 else 0
                    assert normalized==u%q
                    raw_reconstruction=(c*(S+normalized))%m
                    assert raw_reconstruction==raw
                    checks+=1
# Sharp two-adic saturation threshold for a=2,b=1.
saturation_checks=0
for B in range(1,7):
    for t in range(2*B,2*B+5):
        c=coeff(2,1,t)
        for m in range(1,(1<<B)+1):
            q=effective_modulus(m,c)
            odd=m
            while odd%2==0:odd//=2
            assert q==odd
            saturation_checks+=1
    assert effective_modulus(1<<B,coeff(2,1,2*B-1))==2
def terminal_collisions(q0,q1):
    distinct_terminal=0
    for x in X:
        for y in X:
            if x%q0!=y%q0:continue
            for u in MOVES[x]:
                for v in MOVES[y]:
                    if u%q1==v%q1 and u!=v:
                        distinct_terminal+=1
    return distinct_terminal
assert terminal_collisions(17,31)==0
assert terminal_collisions(31,17)>0
assert all(len({y%11 for y in MOVES[x]})==6 for x in X)
for t in range(8,17):
    assert {effective_modulus(m,coeff(2,1,t)) for m in range(1,17)}=={1,*Q4}
result={
 'schema':'PREFIX856_R6_EXACT_INTEGER_EVIDENCE_V1',
 'status':'ALL_EXACT_ASSERTIONS_PASSED',
 'frozen_science':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'model':'five named binary BRC scalar states U=0..31, no-op/one named bit flip, c_t=2^floor(t/2) and known S',
 'quotient_identity':'q_t(m)=m/gcd(m,c_t); raw observation c_t(S+U) mod m is bijective to U mod q_t(m)',
 'generalization':'for a,b>=1 and bounded m<=2^B, all primes dividing ab are eventually absent from q_t, uniformly in m',
 'finite_checks':{'raw_normalized_inverse_pairs':checks,'two_adic_saturation_m_t_pairs':saturation_checks,'odd_only_game_states':len(states),'odd_only_game_action_rows':len(states)*len(Q4),'winning_layers':layers,'losing_states':len(losing),'all_losing_actions_witnessed':True},
 'p5_B4_late_threshold_heartbeat':8,
 'sharp_raw_modulus_saturation_example':{'at_t7_m16_effective_q':effective_modulus(16,coeff(2,1,7)),'at_t8_m16_effective_q':effective_modulus(16,coeff(2,1,8))},
 'p5_cold_start':{'late_four_bit_feedback_possible':False,'optimal_width_bits':5,'two_reading_moduli':[17,31],'two_reading_terminal_collisions':0,'reverse_terminal_collisions':terminal_collisions(31,17),'known_state_tracking_modulus':11},
 'scope':'Author-side exact typed named-source BRC observer; P000 and native X6 dynamics unchanged; no external physical bridge'
}
with open('PREFIX856_R6_ASYMPTOTIC_MODULUS_ERASURE_RESULTS.json','w') as f:
    f.write(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
