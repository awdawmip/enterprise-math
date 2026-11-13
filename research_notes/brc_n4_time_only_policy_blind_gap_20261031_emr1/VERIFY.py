#!/usr/bin/env python3
"""Exact audit of the finite BRC N=4 time-only k=2/3 decoder quantifier gap.
All scores are rational; no external packages or random samples are needed.
This is a finite-model audit, not a native Heartbeat dynamics simulation.
"""
from fractions import Fraction as F
from itertools import product

# LR history classes: AU0, AU1, AV, BU0, BU1, BV.
M = (
    (F(1,2),F(1,2),F(0),F(0),F(0),F(0)),
    (F(9,20),F(11,20),F(0),F(0),F(0),F(0)),
    (F(0),F(0),F(1),F(0),F(0),F(0)),
    (F(0),F(0),F(0),F(1,2),F(1,2),F(0)),
    (F(0),F(0),F(0),F(1,10),F(9,10),F(0)),
    (F(0),F(0),F(0),F(0),F(0),F(1)),
)
# Conditioned preparations: source AU/AV/BU/BV, law Q or P.
input_rows=(0,1,2,2,3,4,5,5)
input_sources=('AU','AU','AV','AV','BU','BU','BV','BV')
# Fixed encoder: AU/AV->L, BU/BV->R; these reference class laws depend on neither true P/Q nor policy.
D_L=(F(1,4),F(1,4),F(1,2),F(0),F(0),F(0))
D_R=(F(0),F(0),F(0),F(1,10),F(2,5),F(1,2))
assert all(sum(row)==1 and all(x>=0 for x in row) for row in M+(D_L,D_R))
assert len(M)==6 and all(len(row)==6 for row in M)

# Reconstruct the unchanged 16 positive leaves in each original source law,
# with independent fair K. Numerators per K over 240 (S,J).
Q=((10,10),(20,20),(15,15),(15,15))
P=((9,11),(5,5),(3,27),(30,30))
leaves={}
for name, weights in [('Q',Q),('P',P)]:
    leaf=[F(w,240) for pair in weights for w in pair for _k in range(2)]
    assert len(leaf)==16 and sum(leaf)==1 and all(x>0 for x in leaf)
    leaves[name]=leaf

def tv(p,q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

for i, source in enumerate(input_sources):
    d=D_L if source.startswith('A') else D_R
    assert tv(M[input_rows[i]],d)==F(1,2),(i,tv(M[input_rows[i]],d))

# A deterministic policy: stage 1 two A/B continue bits; stage 2 three stop/continue bits
# (AU/BU tied, AV, BV); stage 3 six LR-class stop bits. Surviving paths terminate at 4.
# '1' in first/second action means CONTINUE, in third action means STOP.
COL_SOURCE=(0,0,1,2,2,3) # source AU,AV,BU,BV for each six LR class
SOURCE_PREFIX=(0,0,1,1) # A=0, B=1
STAGE2_ACTION_SLOT=(0,1,0,2) # AU and BU share stage-two action

def terminal_times(stage1,stage2,stage3):
    out=[]
    for c,source_idx in enumerate(COL_SOURCE):
        if stage1[SOURCE_PREFIX[source_idx]]==0:
            out.append(1)
        elif stage2[STAGE2_ACTION_SLOT[source_idx]]==0:
            out.append(2)
        elif stage3[c]==1:
            out.append(3)
        else:
            out.append(4)
    return out

def time_law(class_mass,terminal):
    return tuple(sum(p for p,t in zip(class_mass,terminal) if t==time) for time in (1,2,3,4))

max_adaptive=F(0)
max_fixed=F(0)
policy_count=0
comparisons=0
uniform=(F(1,4),)*4
for first in product((0,1),repeat=2):
    for second in product((0,1),repeat=3):
        for third in product((0,1),repeat=6):
            t=terminal_times(first,second,third)
            l=time_law(D_L,t)
            r=time_law(D_R,t)
            policy_count+=1
            for row,source in zip(input_rows,input_sources):
                actual=time_law(M[row],t)
                approx=l if source.startswith('A') else r
                da=tv(actual,approx)
                df=tv(actual,uniform)
                assert da<=F(1,2),(first,second,third,row,da)
                assert df<=F(3,4),(first,second,third,row,df)
                max_adaptive=max(max_adaptive,da)
                max_fixed=max(max_fixed,df)
                comparisons+=1
assert (policy_count,comparisons)==(2048,16384)
assert max_adaptive==F(1,2),max_adaptive
assert max_fixed==F(3,4),max_fixed

# Four pure time policies realize delta_t identically on all six conditioned rows.
for target in (1,2,3,4):
    decisions= {1:((0,0),(0,0),(0,)*6),
                2:((1,1),(0,0,0),(0,)*6),
                3:((1,1),(1,1,1),(1,)*6),
                4:((1,1),(1,1,1),(0,)*6)}[target]
    assert terminal_times(*decisions)==[target]*6
    delta=tuple(F(time==target) for time in (1,2,3,4))
    assert tv(delta,uniform)==F(3,4)

# The 64 time-bit policies emit time=3 with probability M b for every preparation.
shattering=0
for b in product((0,1),repeat=6):
    t=terminal_times((1,1),(1,1,1),b)
    for row in M:
        observed_3=time_law(row,t)[2]
        asserted=sum(row[j]*b[j] for j in range(6))
        assert observed_3==asserted
        shattering+=1
assert shattering==64*6

# Four mutually disjoint source prototypes give the exact dual isometry in the lower proof.
prototypes=(M[0],M[2],M[3],M[5])
assert all(sum(min(x,y) for x,y in zip(prototypes[i],prototypes[j]))==0
           for i in range(4) for j in range(i))
# Sample integer zero-sum left-null witnesses are an audit of the isometry, not a
# replacement for the analytic arbitrary-stochastic-encoder dimension argument.
null_isometry=0
for a,b,c in product(range(-3,4),repeat=3):
    w=(a,b,c,-a-b-c)
    if w==(0,0,0,0):
        continue
    r=[sum(w[i]*prototypes[i][j] for i in range(4)) for j in range(6)]
    assert sum(r)==0
    assert sum(map(abs,r))==sum(map(abs,w))
    max_bit=max(abs(sum(r[j]*bit[j] for j in range(6)))
                for bit in product((0,1),repeat=6))
    assert max_bit==F(sum(map(abs,w)),2)
    null_isometry+=1

print('PASS_BRC_N4_TIME_ONLY_K2K3_FIXED_DECODER_GAP_20261031')
print('Leaves: 16 positive per law, P/Q sums=1')
print('Input rows: 8; LR classes: 6; two-code reference TV=1/2 for all inputs')
print(f'S23 deterministic timing policies: {policy_count}; exact (policy,input) checks: {comparisons}')
print(f'Max witnessed adaptive two-code error: {max_adaptive}; fixed uniform error: {max_fixed}')
print('Pure all-source stop times: 1,2,3,4 (four dirac witnesses)')
print(f'Time-shattering equalities: {shattering} (=64 policies x 6 distinct rows)')
print(f'Integer witness isometries audited: {null_isometry}')
print('Theorem scope: arbitrary randomized encoders/decoders and lawful behavioral policies via analytic proof')
print('Conclusion: policy-dependent R2=R3=1/2; policy-independent Rk=3/4 for all k>=1')
