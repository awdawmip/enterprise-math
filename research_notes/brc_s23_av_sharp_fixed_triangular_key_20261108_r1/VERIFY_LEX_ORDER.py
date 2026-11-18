#!/usr/bin/env python3
"""Sharp two-level exact triangular threshold order with ties; integer only.

Requires the companion VERIFY_TRIANGULAR_KEY.py (same research directory).
"""
from random import Random
from VERIFY_TRIANGULAR_KEY import P,D,N,LO,HI,Q,count_below,divceil

M2=2*N+510

def fibers(H,key):
    v0=(key*pow(P,-1,D))%D
    j0=(P*v0-key)//D
    t0=max(0,divceil(-j0,P))
    t1=(H-v0-j0)//N
    return [(v0+D*t,j0+P*t) for t in range(t1,t0-1,-1)]

def rank_lex(H,v,j):
    assert 0<=v and 0<=j and v+j<=H
    key=P*v-D*j
    v0=(key*pow(P,-1,D))%D
    j0=(P*v0-key)//D
    t=(v-v0)//D
    t1=(H-v0-j0)//N
    return count_below(H,key)+t1-t

def select_lex(H,rank):
    assert 0<=H<M2
    total=(H+1)*(H+2)//2
    assert 0<=rank<total
    lo=-D*H
    hi=P*H+1
    while lo<hi:
        mid=(lo+hi)//2
        if count_below(H,mid)>rank:
            hi=mid
        else:
            lo=mid+1
    key=lo-1
    bucket=fibers(H,key)
    idx=rank-count_below(H,key)
    assert 0<=idx<len(bucket)
    return key,bucket[idx],len(bucket)

def strict_less(x,y):
    # Certify t(x)<t(y) using rational interval, NOT the lex comparator.
    a=y[0]-x[0]
    b=y[1]-x[1]
    low=(LO if a>=0 else HI)*a-Q*b
    high=(HI if a>=0 else LO)*a-Q*b
    assert low<=high
    return low>0

def verify():
    assert 79*P-431*D==1
    # eta=P-rD and epsilon=79*r-431 satisfy 0<eta<epsilon<2eta.
    assert P*Q>D*HI
    assert 79*LO>431*Q
    assert (79+D)*LO>(431+P)*Q
    assert (2*P+431)*Q>(2*D+79)*HI
    print('EXACT_PERTURBATION: 0<eta<epsilon<2eta certified')
    for H in range(1,65):
        brute=sorted(((v,j) for v in range(H+1) for j in range(H-v+1)),
            key=lambda z:(P*z[0]-D*z[1],-z[0]))
        for i,point in enumerate(brute):
            key,selected,size=select_lex(H,i)
            assert point==selected and size==1
            assert rank_lex(H,*point)==i
            if i+1<len(brute):
                assert strict_less(point,brute[i+1])
    print('SMALL_DOMAIN_EXHAUSTIVE: H=1..64 complete exact rank/select and real-order checks PASS')
    r=Random(512945)
    for H in [D-1,D,N-1,N,N+1,2*N-1,2*N,M2-1]:
        total=(H+1)*(H+2)//2
        ranks={0,1,2,3,total//4,total//2,(3*total)//4,total-3,total-2,total-1}
        ranks.update(r.randrange(total) for _ in range(45))
        max_group=0
        for index in sorted(ranks):
            k,p,sz=select_lex(H,index)
            assert P*p[0]-D*p[1]==k
            assert rank_lex(H,*p)==index
            max_group=max(sz,max_group)
            if index+1<total:
                _,nxt,_=select_lex(H,index+1)
                assert strict_less(p,nxt),(H,index,p,nxt)
        for _ in range(50):
            v=r.randrange(H+1); j=r.randrange(H-v+1)
            idx=rank_lex(H,v,j)
            _,p,_=select_lex(H,idx)
            assert p==(v,j)
        print('LARGE_LEX_PASS',H,'points',total,'largest_sampled_fiber',max_group)
    assert fibers(N,0)==[(D,P),(0,0)]
    assert fibers(2*N,0)==[(2*D,2*P),(D,P),(0,0)]
    # At H=M2, u+2w has positive key 1 but *negative* exact real score.
    w2=(79+2*D,431+2*P)
    assert sum(w2)==M2 and P*w2[0]-D*w2[1]==1
    assert strict_less(w2,(0,0))
    print('SHARP_FAILURE_AT_H',M2,'integer_key(u+2w)=1 but real threshold(u+2w)<0')
    print('PASS_S23_AV_SHARP_LEX_ORDER_THROUGH_H4910647')

if __name__=='__main__':
    verify()
