#!/usr/bin/env python3
"""Exact six-state maximum-likelihood S23 lower bound; standard library only.
All integer arithmetic.  Every (U,S) word type is included through exact intervals.
"""
from fractions import Fraction as F
from math import comb, lcm
from decimal import Decimal, localcontext

N=1000
Q=(F(1,28), F(65126,1000000), F(102302,1000000), F(146248,1000000), F(195886,1000000), F(1,4))
D=lcm(4, *(q.denominator for q in Q))
Z=D//4
B=tuple(int(D*q) for q in Q)  # stop4 weights
A=tuple(D-Z-b for b in B)       # stop1 weights
assert all(a>0 for a in A) and all(b>0 for b in B)
BPOW=tuple(tuple(b**u for u in range(N+1)) for b in B)
APOW=tuple(tuple(a**v for v in range(N+1)) for a in A)

checks=0

def winner(u,s):
    """Exact likelihood maximizer; common multinomial/stop3 factors cancel."""
    v=N-u-s
    vals=[BPOW[j][u]*APOW[j][v] for j in range(6)]
    return max(range(6), key=lambda j:vals[j])


def intervals(u):
    """The argmax index is nondecreasing in S; find exact breakpoints."""
    m=N-u
    begin=0
    result=[]
    while begin<=m:
        j=winner(u,begin)
        if winner(u,m)==j:
            last=m
        else:
            left,right=begin+1,m
            while left<right:
                mid=(left+right)//2
                if winner(u,mid)==j:
                    left=mid+1
                else:
                    right=mid
            last=left-1
        assert winner(u,last)==j
        if last<m:
            assert winner(u,last+1)>j
        result.append((j,begin,last))
        begin=last+1
    assert result[0][1]==0 and result[-1][2]==m
    assert all(result[i][2]+1==result[i+1][1] and result[i][0]<result[i+1][0] for i in range(len(result)-1))
    return result


def interval_mass_num(j,u,lo,hi):
    """Mass times D**N, integer via multinomial recurrence."""
    m=N-u
    term=comb(m,lo)*Z**lo*APOW[j][m-lo]
    total=0
    for s in range(lo,hi+1):
        total+=term
        if s<hi:
            numerator=term*(m-s)*Z
            denominator=(s+1)*A[j]
            assert numerator%denominator==0
            term=numerator//denominator
    return comb(N,u)*BPOW[j][u]*total


def main():
    assert D%4==0
    for j,q in enumerate(Q):
        a=F(3,4)-q
        c=1/(1+4*q)
        assert F(1,2)<=a<=F(7,8)
        assert F(1,2)<=c<=F(7,8)
        assert (1-a)*c==F(1,4)
        assert F(A[j],D)==a and F(B[j],D)==q
    mass_num=0
    n_intervals=0
    change_u=0
    class_counts=[0]*6
    for u in range(N+1):
        intervals_u=intervals(u)
        n_intervals+=len(intervals_u)
        if len(intervals_u)>1: change_u+=1
        for j,lo,hi in intervals_u:
            class_counts[j]+=hi-lo+1
            mass_num+=interval_mass_num(j,u,lo,hi)
    assert sum(class_counts)==(N+1)*(N+2)//2
    den=D**N
    assert den<mass_num<6*den
    R_num=mass_num-den
    R_den=6*den
    # Rational optimized candidate: stronger than original fixed-six-state ML bound.
    assert R_num*1000000 > 808199*R_den
    assert R_num*1000000 < 808201*R_den
    with localcontext() as ctx:
        ctx.prec=45
        R=Decimal(R_num)/Decimal(R_den)
        print('PASS_S23_N1000_OPT_SIX_STATE_FULL_ML_INTEGER_20261106')
        print('N=',N,'D=',D,'weight_stop3=',Z)
        print('types=',sum(class_counts),'intervals=',n_intervals,'u_with_switches=',change_u)
        print('class_type_counts=',class_counts)
        print('exact_lower_threshold: delta_1000 > 808199/1000000')
        print('six_hypothesis_ml_lower=',R)
        print("numerator_bits=",R_num.bit_length())
        print("denominator_bits=",R_den.bit_length())
        print('certificate: exact integer argmax + pairwise monotone ratio + exact multinomial sums')
        print('status=author-side exact arithmetic; independent review pending')

if __name__=='__main__': main()
