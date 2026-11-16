"""Exact timing-only FULL versus seedless LR convex-support witness.
Python standard library only. All arithmetic is Fraction.
"""
from fractions import Fraction as Q
from itertools import product

w=(Q(1,2),Q(1,2))
r=(Q(1,2),Q(1),Q(3,2))
s=(Q(1,8),Q(1),Q(15,8))
K=((Q(1,4),Q(1,2),Q(1,4)),(Q(5,16),Q(6,16),Q(5,16)))
M=((Q(37,56),Q(14,56),Q(5,56)),
   (Q(21,56),Q(14,56),Q(21,56)),
   (Q(5,56),Q(14,56),Q(37,56)))
Mprime=(M[0],tuple(x+Q(d,56) for x,d in zip(M[1],(1,-2,1))),M[2])
n=(-82,73)

def valid_kernels():
    assert sum(w)==1
    for row in K:
        assert all(x>0 for x in row)
        assert sum(row)==1
        assert sum(x*t for x,t in zip(row,r))==1
    for kernel in (M,Mprime):
        for j,row in enumerate(kernel):
            assert all(x>0 for x in row)
            assert sum(row)==1
            assert sum(x*t for x,t in zip(row,s))==r[j]
            assert all(s[l]*row[l]/r[j]>0 for l in range(3))

def full_times(first, second):
    tp=tq=Q(0)
    for h in range(2):
        tp+=w[h];tq+=w[h]
        if first[h]:
            tp+=w[h];tq+=w[h]
            for j in range(3):
                if second[h][j]:
                    tp+=w[h]*K[h][j]*r[j]
                    tq+=w[h]*K[h][j]
    return tp,tq

def lr_times(first, second):
    tp=tq=Q(1)
    if first:
        tp+=1;tq+=1
        for j in range(3):
            if second[j]:
                mass=sum(w[h]*K[h][j] for h in range(2))
                tp+=r[j]*mass;tq+=mass
    return tp,tq

def score(ts):
    return sum(x*y for x,y in zip(n,ts))

def full_enumeration():
    return [(score(full_times(first,second)),first,second)
      for first in product((0,1),repeat=2)
      for v in product((0,1),repeat=6)
      for second in ((v[:3],v[3:]),)]

def lr_enumeration():
    return [(score(lr_times(first,second)),first,second)
      for first in (0,1) for second in product((0,1),repeat=3)]

def analytic_support():
    z=[]
    for h in range(2):
        G=sum(K[h][j]*max(Q(0),n[1]+n[0]*r[j]) for j in range(3))
        z.append(sum(n)+G)
    full=sum(n)+sum(w[h]*max(Q(0),z[h]) for h in range(2))
    lr=sum(n)+max(Q(0),sum(w[h]*z[h] for h in range(2)))
    return z,full,lr

if __name__=='__main__':
    valid_kernels()
    full=full_enumeration(); lr=lr_enumeration()
    fs=max(x[0] for x in full);ls=max(x[0] for x in lr)
    z,fa,la=analytic_support()
    assert len(full)==256 and len(lr)==16
    assert z==[Q(-1),Q(1)]
    assert (fs,ls,fa,la)==(Q(-17,2),Q(-9),Q(-17,2),Q(-9))
    assert fs-ls==Q(1,2)
    witness=full_times((0,1),((0,0,0),(1,0,0)))
    assert witness==(Q(101,64),Q(53,32))
    assert score(witness)==fs
    witness_o4=(Q(0),Q(1),*witness)
    assert Q(1,310)==(fs-ls)/sum(abs(k) for k in n)
    print('FULL_RAW_DETERMINISTIC_SCHEDULES=256')
    print('LR_RAW_DETERMINISTIC_SCHEDULES=16 (9 distinct effective first/second schedules)')
    print('FULL_TIMING_SUPPORT=',fs,'LR_TIMING_SUPPORT=',ls,'GAP=',fs-ls)
    print('SOURCE_THRESHOLD_VALUES=',tuple(z))
    print('FULL_WITNESS_O4=',witness_o4)
    print('DIST_INFINITY_LOWER_BOUND=',Q(1,310))
    print('AFFINE_AND_NONAFFINE_M_KERNEL_VALIDATED=True')
    print('PASS_EXACT_R5_TWO_GATE_TIMING_JENSEN_SEPARATION')