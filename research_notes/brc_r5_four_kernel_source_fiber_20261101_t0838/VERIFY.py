#!/usr/bin/env python3
"""Exact checks for the four-kernel time/LR stopping classification.
All-real conclusions are proved analytically in RESEARCH.md; grid checks are
regression evidence, not parameter sampling promoted to a universal proof.
"""
from fractions import Fraction as F
from itertools import product, permutations

Z, O, H = F(0), F(1), F(1, 2)


def observation(a, b, policy):
    """a=(Q_low_A,Q_low_B), b=(P_low_A,P_low_B).
    policy=(pA,pB,lA,hA,lB,hB), where 1 means stop.
    Returns (eP,eQ,TP,TQ) with both priors (1/2,1/2).
    """
    v = [Z, Z, Z, Z]
    for i in range(2):
        p = F(policy[i]); lo = F(policy[2+2*i]); hi = F(policy[3+2*i])
        v[1] += H*p
        v[2] += H*p
        v[3] += H*p
        for branch, pq, qq, stop in ((0,b[i],a[i],lo),
                                      (1,O-b[i],O-a[i],hi)):
            mp = H*(O-p)*pq
            mq = H*(O-p)*qq
            if branch == 0:
                v[0] += mp*(O-stop)
                v[1] += mq*stop
            else:
                v[0] += mp*stop
                v[1] += mq*(O-stop)
            v[2] += mp*(3-stop)
            v[3] += mq*(3-stop)
    return tuple(v)


def lr_key_groups(a, b):
    keys = [(2,b[i]/a[i]) for i in range(2)]
    keys += [(2,(O-b[i])/(O-a[i])) for i in range(2)]
    ordered = list(dict.fromkeys(keys))
    return keys, ordered


def all_lr(a, b):
    keys, distinct = lr_key_groups(a,b)
    for bits in product((Z,O), repeat=len(distinct)+1):
        lookup = dict(zip(distinct,bits[1:]))
        yield bits, observation(a,b,(bits[0],bits[0],lookup[keys[0]],
                                     lookup[keys[2]],lookup[keys[1]],lookup[keys[3]]))


def all_full(a,b):
    for bits in product((Z,O),repeat=6):
        yield bits,observation(a,b,bits)


def det(matrix):
    n=len(matrix)
    return sum(((-O if sum(perm[i]>perm[j] for i in range(n)
               for j in range(i+1,n))%2 else O)
            *prod(matrix[i][perm[i]] for i in range(n)))
            for perm in permutations(range(n)))


def prod(it):
    ans=O
    for x in it: ans*=x
    return ans


def four_kernel_check(a,b):
    assert all(Z<x<O for x in (*a,*b))
    for i in range(2):
        assert a[i]+(O-a[i]) == O and b[i]+(O-b[i]) == O
    theta_q=sum(a)/2; theta_p=sum(b)/2
    full=list(all_full(a,b)); lr=list(all_lr(a,b))
    assert len(full)==64 and 2<=len(lr)<=32
    for _,v in full+lr:
        assert Z<=v[0]<=O and Z<=v[1]<=O
        assert O<=v[2]<=3 and O<=v[3]<=3
    cq=lambda v:v[3]+(O+theta_q)*v[1]
    cp=lambda v:v[2]-(O+theta_p)*v[0]
    fq=min(cq(v) for _,v in full)
    lq=min(cq(v) for _,v in lr)
    fp=min(cp(v) for _,v in full)
    lp=min(cp(v) for _,v in lr)
    assert fq == 2+theta_q-abs(a[0]-a[1])/4
    assert lq == 2+theta_q
    assert fp == O-abs(b[0]-b[1])/4
    assert lp == O
    return len(lr),lq-fq,lp-fp


def equal_kernel_real_check(a,b):
    assert a!=b
    # All sources have the same low probabilities under each law.
    # For arbitrary real stop probabilities, aggregate source survival.
    probs=(Z,F(1,3),H,F(2,3),O)
    n=0
    for pA,pB,lA,hA,lB,hB in product(probs,repeat=6):
        survival=(O-pA)+(O-pB)
        p=(pA+pB)/2
        lo=((O-pA)*lA+(O-pB)*lB)/survival if survival else Z
        hi=((O-pA)*hA+(O-pB)*hB)/survival if survival else Z
        assert Z<=p<=O and Z<=lo<=O and Z<=hi<=O
        assert observation((a,a),(b,b),(pA,pB,lA,hA,lB,hB)) == \
               observation((a,a),(b,b),(p,p,lo,hi,lo,hi))
        n+=1
    return n


def equal_law_check(alpha):
    # When both laws coincide, (time,LR)=(2,1) for both signal
    # branches. LR must reuse the time-2 stop probability.
    assert Z < alpha < O
    a=(alpha,alpha); b=(alpha,alpha)
    vs=[v for _,v in all_lr(a,b)]
    assert len(vs)==4
    m=min(alpha,O-alpha)
    h=lambda v:v[2]-2*v[0]/m
    assert max(h(v) for v in vs)==O
    witness=observation(a,b,(0,0,1,0,1,0))
    assert witness[0]==Z and witness[2]==3-alpha
    assert h(witness)>O
    # LR eP/T points at (p,q)=(1,*),(0,0),(0,1).
    # Determinant of two differences is 3 alpha - 2.
    p1=observation(a,b,(1,1,0,0,0,0))
    q0=observation(a,b,(0,0,0,0,0,0))
    q1=observation(a,b,(0,0,1,1,1,1))
    d=det([[q0[k]-p1[k] for k in (0,2)],
           [q1[k]-p1[k] for k in (0,2)]])
    assert d==3*alpha-2
    return d,witness


def run():
    sample=(F(1,4),F(1,2)),(F(1,8),F(1,3))
    a,b=sample
    count,gq,gp=four_kernel_check(a,b)
    assert (count,gq,gp)==(32,F(1,16),F(5,96))
    full_witness=observation(a,b,(0,1,0,1,0,0))
    assert full_witness==(H,H,F(25,16),F(13,8))
    lvs=[v for _,v in all_lr(a,b)]
    base=lvs[0]
    # bit order is time1, A-low, B-low, A-high, B-high.
    vlist=list(all_lr(a,b))
    rows=[]
    for j in (0,1,3,2):
        bits=tuple(int(k==j) for k in range(5))
        v=next(v for q,v in vlist if q==bits)
        rows.append([v[k]-base[k] for k in range(4)])
    assert det(rows)==F(1,2048)
    # Exhaustive exact regression on source pairs and both laws, including
    # LR key collisions such as P=Q and cross-source LR key coincidences.
    vals=(F(1,5),F(2,5),F(3,5))
    cases=0;collision_cases=0
    for aa,ab,ba,bb in product(vals,repeat=4):
        n,_,_=four_kernel_check((aa,ab),(ba,bb))
        cases+=1
        collision_cases+=int(n<32)
    identical_checks=0
    for aa,bb in ((F(1,5),F(2,5)),(F(1,4),H),(F(3,4),F(1,8))):
        identical_checks+=equal_kernel_real_check(aa,bb)
        # For the three independent aggregate flows (p,f_low,f_high),
        # a 3x3 minor in (eP,eQ,TP) is (a-b)(2-b).
        M=[[-bb,aa,-2],[-bb,aa,-bb],
           [O-bb,-(O-aa),-(O-bb)]]
        assert det(M)==(aa-bb)*(2-bb)!=Z
    degeneracies={}
    for alpha in (F(1,5),F(1,2),F(2,3),F(4,5)):
        degeneracies[str(alpha)]=str(equal_law_check(alpha)[0])
    print('PASS_EXACT_R5_FOUR_KERNEL_SOURCE_FIBER_COMPLETE_NO_GO')
    print('all_real_support_gaps: Q=abs(aA-aB)/4, P=abs(bA-bB)/4')
    print('independent_rational_kernel_cases=',cases)
    print('with_LR_key_collisions=',collision_cases)
    print('equal_kernel_real_aggregation_checks=',identical_checks)
    print('sample_LR_vertices=',count)
    print('sample_Q_support_gap=',gq)
    print('sample_P_support_gap=',gp)
    print('sample_FULL_witness=',full_witness)
    print('sample_LR_rank4_determinant=',F(1,2048))
    print('equal_law_LR_two_coordinate_rank_determinants=',degeneracies)


if __name__=='__main__': run()
