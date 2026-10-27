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
# EC48P extension: a neutral source-independent root shifts both times by +1.
# All assertions below retain EXACT rational arithmetic and finite normal forms.
def ec48p_lift(o):
    return (o[0],o[1],o[2]+1,o[3]+1)

def ec48p_3vector(assignment, rules):
    s,codes,mu,rows=generic_tree(3)
    a=b=F(0); ep=eq=F(2)
    ep += F(sum(v>=0 for v in assignment),3)
    eq += F(sum(v>=0 for v in assignment),3)
    for h,j,y,p,q in rows:
        m=assignment[h]
        if m<0: continue
        if j==s:  # private plus, stop and accept
            a+=p; b+=q
        elif j<s and rules[m][j]:
            ep+=p; eq+=q
            if y=='+': a+=p; b+=q
    return a,b,ep,eq

def ec48p_3envelope(c):
    best=-2*c; count=0
    for assignment in product(range(-1,2),repeat=3):
        for flat in product((0,1),repeat=4):
            rules=(flat[:2],flat[2:]);count+=1
            best=max(best,score(ec48p_3vector(assignment,rules),c))
    assert count==432
    return best,count

out['EC48P']={'model':'one neutral initial root + EC48O k-stage original family (horizon four)',
 'theorem':'M*_H4(k)=max(k,2); for k>=2 gap c/(2*k*ceil(log2(k))) for 0<c<=1/16',
 'constructive_checks':[],'exhaustive_k3':[],'k4_crosschecks':[]}
for k in range(2,33):
    s,codes,mu,rows=generic_tree(k)
    B=sum(code.bit_count() for code in codes)
    full=ec48p_lift(generic_observation(k,False))
    merged=ec48p_lift(generic_observation(k,True))
    for cc in (F(1,64),F(1,32),F(1,16)):
        vf=F(1,4)-6*cc+B*mu*(F(1,2)-2*cc)
        d=2*cc*mu
        assert score(full,cc)==vf
        assert score(merged,cc)==vf-d
        assert vf-d > -2*cc  # free early-stop at the neutral root
    out['EC48P']['constructive_checks'].append({'k':k,'s':s,'leaves':len(rows),'gap_at_c_1_16':str(F(1,16)/(2*k*s))})
for cc in (F(1,64),F(1,32),F(1,16)):
    old_full=F(1,4)-4*cc+sum(code.bit_count() for code in generic_tree(3)[1])*F(1,24)*(F(1,2)-2*cc)
    observed,n=ec48p_3envelope(cc)
    assert observed==old_full-2*cc-cc/F(12)
    out['EC48P']['exhaustive_k3'].append({'c':str(cc),'full':str(old_full-2*cc),'two_state':str(observed),'gap':str(cc/F(12)),'controllers':n})
for r in out['finite_checks']:
    if F(r['c'])>F(1,16): continue  # root may optimally stop at larger costs
    cc=F(r['c']); old_full=F(r['full_support']); old_three=F(r['three_state_support'])
    new_full=old_full-2*cc
    new_three=max(-2*cc,old_three-2*cc)
    assert new_full-new_three == cc/F(16)
    out['EC48P']['k4_crosschecks'].append({'c':str(cc),'full':str(new_full),'three_state':str(new_three),'gap':str(cc/F(16)),'inherited_exhaustive_controllers':r['candidate_controllers_checked']})
cc=F(1,16)
vf=ec48p_lift(generic_observation(3,False))
vm=ec48p_lift(generic_observation(3,True))
assert vf==(F(9,16),F(13,48),F(37,12),F(37,12))
assert vm==(F(9,16),F(13,48),F(25,8),F(25,8))
assert score(vf,cc)==-F(3,32) and score(vm,cc)==-F(19,192)
out['EC48P']['14_leaf_instance']={'k':3,'cost':'1/16','full_vector':list(map(str,vf)),
  'two_state_vector':list(map(str,vm)),'gap':'1/192','terminal_leaves':14,
  'leaf_masses':[[h,j,y,str(p),str(q)] for h,j,y,p,q in generic_tree(3)[3]]}
# k=1: neutral root followed by EC48O's 3-leaf k=1 example.
cc=F(1,32)
old_full=F(1,4)-5*cc
old_one=max(-2*cc,-4*cc,F(1,4)-6*cc)
new_full=-2*cc+max(0,old_full)
new_one=-2*cc+max(0,old_one)
assert new_full==F(1,32) and new_one==0
out['EC48P']['k1']={'cost':'1/32','full':'1/32','one_state':'0','gap':'1/32',
 'three_positive_leaf_masses':[['neutral','1/2','1/2'],['up','3/8','1/8'],['down','1/8','3/8']]}
out['EC48P']['exact_controller_evaluations']=3*16384+3*432

print(json.dumps(out,ensure_ascii=False,indent=2))
