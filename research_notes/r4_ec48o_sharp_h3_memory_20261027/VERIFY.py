#!/usr/bin/env python3
"""Exact finite-policy verification for EC48O's four-history BRC witness.
All P,Q leaf numerators use denominator 128. Deterministic normal forms
suffice for linear support because time-indexed stochastic kernels are
separately affine in each of their probability rows.
"""
from fractions import Fraction as F
from itertools import product
import json

NAMES = 'ABCD'
PATTERNS = ((0, 0), (0, 1), (1, 0), (1, 1))
LEAVES = []
for h, bits in enumerate(PATTERNS):
    for x, bit in enumerate(bits):
        if bit:
            LEAVES.extend([(h,x,'+',3,1),(h,x,'-',1,3)])
        else:
            LEAVES.append((h,x,'*',4,4))
    LEAVES.extend([(h,2,'*',16,8),(h,3,'*',8,16)])

assert len(LEAVES) == 20
assert sum(row[3] for row in LEAVES) == 128
assert sum(row[4] for row in LEAVES) == 128
for h in range(4):
    assert sum(p for hh,x,y,p,q in LEAVES if hh == h) == 32
    assert sum(q for hh,x,y,p,q in LEAVES if hh == h) == 32
for h in range(4):
    for x in (0,1):
        assert sum(p for hh,xx,y,p,q in LEAVES if hh == h and xx == x) == 4
        assert sum(q for hh,xx,y,p,q in LEAVES if hh == h and xx == x) == 4

# For a controller, stage one chooses stop or continue and memory message;
# at shared x=0,1 the stage-two action depends on message and x.
# At x=2 accept and x=3 reject immediately, as exactly optimal for all h.
# At x in {0,1}, continued paths optimally accept at terminal iff P/Q>1.
def vector(continues, messages, rules):
    alpha = beta = 0  # numerator /128
    sum_tP = sum_tQ = 128  # E T numerators: baseline t=1
    for h, (b0,b1) in enumerate(PATTERNS):
        if not continues[h]:
            continue
        sum_tP += 32
        sum_tQ += 32
        alpha += 16  # x=2 early acceptance
        beta += 8
        for x, bit in enumerate((b0,b1)):
            if rules[messages[h]][x]:
                sum_tP += 4
                sum_tQ += 4
                if bit:
                    alpha += 3  # terminal + accept, terminal - reject
                    beta += 1
    return (F(alpha,128), F(beta,128), F(sum_tP,128), F(sum_tQ,128))

def score(o,c):
    return o[0]-o[1]-c*(o[2]+o[3])

def envelope(m, c):
    best = None
    witness = None
    checked=0
    # Finiteness: exactly (m+1)^4 choices of stage-one stop or message;
    # 2^(2m) rules for stage-two shared x=0 and x=1.
    for assignments in product(range(-1,m),repeat=4):
        continues=tuple(a >= 0 for a in assignments)
        messages=tuple(max(a,0) for a in assignments)
        for flat in product((0,1),repeat=2*m):
            rules=tuple((flat[2*i],flat[2*i+1]) for i in range(m))
            val=score(vector(continues,messages,rules),c)
            checked+=1
            if best is None or val>best:
                best=val
                witness=(assignments, rules, vector(continues,messages,rules))
    assert checked==(m+1)**4 * 2**(2*m)
    return best, witness, checked

# Named full-history and compressed controllers; no search needed for m=4.
full_o=vector((1,1,1,1),(0,1,2,3),PATTERNS)
three_o=vector((1,1,1,1),(0,0,1,2),((0,1),(1,0),(1,1)))
assert full_o==(F(19,32),F(9,32),F(17,8),F(17,8))
assert three_o==(F(19,32),F(9,32),F(69,32),F(69,32))

out={'scope':'exact auxiliary two-source three-stage BRC, 4 first-stage histories, 20 strictly positive leaves',
     'leaf_count':len(LEAVES),'leaf_masses_numerators_128':LEAVES,
     'full_witness_vector':list(map(str,full_o)),
     'three_state_witness_vector':list(map(str,three_o)),
     'claims':{'c_interval':'0<c<1/9','full':'5/16 - 17*c/4',
               'three_state':'5/16 - 69*c/16','gap':'c/16'},
     'finite_checks':[]}
for c in (F(1,32),F(1,16),F(1,10)):
    expected_full=F(5,16)-F(17,4)*c
    expected_m3=expected_full-c/F(16)
    assert score(full_o,c)==expected_full
    assert score(three_o,c)==expected_m3
    top3, win3,n3 = envelope(3,c)
    assert top3 == expected_m3, (c, top3, expected_m3)
    out['finite_checks'].append({'c':str(c),'full_support':str(expected_full),
      'three_state_support':str(top3),'gap':str(expected_full-top3),
      'candidate_controllers_checked':n3,
      'optimal_message_assignments':list(win3[0]),
      'optimal_rules':[list(u) for u in win3[1]]})
assert out['finite_checks'][1]['three_state_support']=='11/256'

def generic_tree(k):
    """Give positive (h,x,y,P,Q) leaf masses as exact rationals."""
    assert k >= 2
    s = (k-1).bit_length()
    codes = [0,1] + [a for a in range(2,2**s)][:k-2]
    assert len(codes)==k and len(set(codes))==k
    mu = F(1,4*k*s)
    rows=[]
    for h, code in enumerate(codes):
        for j in range(s):
            if (code>>j)&1:
                rows.extend([(h,j,'+',3*mu/4,mu/4),(h,j,'-',mu/4,3*mu/4)])
            else:
                rows.append((h,j,'*',mu,mu))
        rows.extend([(h,s,'*',F(1,2*k),F(1,4*k)),
                     (h,s+1,'*',F(1,4*k),F(1,2*k))])
    return s,codes,mu,rows

def generic_observation(k,merged):
    s,codes,mu,rows=generic_tree(k)
    # Full history always continues at t1; at shared j it continues iff bit=1.
    # Merge h=0 and h=1 in the k-1-state policy. This forces the neutral
    # h=0 at shared j=0 to continue, while every other decision is unchanged.
    alpha=beta=F(0)
    ep=eq=F(2)
    for h, j, y, p, q in rows:
        if j == s:  # strong private positive signal at t2
            alpha += p
            beta += q
        elif j < s:
            cont=((codes[h]>>j)&1) or (merged and h == 0 and j == 0)
            if cont:
                ep += p
                eq += q
                if y == '+':
                    alpha += p
                    beta += q
    return (alpha,beta,ep,eq)

out['generic_family_checks']=[]
for k in range(2,33):
    s,codes,mu,rows=generic_tree(k)
    assert all(p>0 and q>0 for h,j,y,p,q in rows)
    assert sum(p for h,j,y,p,q in rows)==sum(q for h,j,y,p,q in rows)==1
    assert all(sum(p for hh,j,y,p,q in rows if hh==h)==F(1,k) for h in range(k))
    assert all(sum(q for hh,j,y,p,q in rows if hh==h)==F(1,k) for h in range(k))
    B=sum(code.bit_count() for code in codes)
    for c in (F(1,32),F(1,16),F(1,11)):
        full=generic_observation(k,False)
        merged=generic_observation(k,True)
        vf=F(1,4)-4*c + B*mu*(F(1,2)-2*c)
        gap=2*c*mu
        assert score(full,c)==vf
        assert score(merged,c)==vf-gap
        assert gap>0
    out['generic_family_checks'].append({'k':k,'s':s,'leaf_count':len(rows),
        'B':B,'c_1_16_full':str(score(generic_observation(k,False),F(1,16))),
        'c_1_16_kminus1':str(score(generic_observation(k,True),F(1,16))),
        'gap':str(F(1,16)/(2*k*s))})

# k=1 witness: x=0 has one neutral leaf P=Q=1/2. At x=1 two
# informative leaves: (P,Q)=(3/8,1/8),(1/8,3/8). Both x have LR=1.
c=F(1,32)
vfull=F(1,4)-5*c
# A one-state machine either stops at t1, stops at t2 after all x,
# or continues all x; it cannot split x=0 vs x=1 at time 2.
vone=max(-2*c,-4*c,F(1,4)-6*c)
assert vfull==F(3,32) and vone==F(1,16) and vfull-vone==F(1,32)
out['k1_case']={'c':str(c),'full':str(vfull),'one_state':str(vone),
  'gap':str(vfull-vone),'positive_terminal_leaves':3}
print(json.dumps(out,ensure_ascii=False,indent=2))
