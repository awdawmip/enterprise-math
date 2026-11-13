#!/usr/bin/env python3
"""Exact Fraction proof checker: 553 distinct S23 gaps through total n=1270."""
from collections import defaultdict
from fractions import Fraction as Q

LO=Q(262204504569236716045286,10**24)
HI=Q(262204504569236716045287,10**24)
M=128
END=1270

def gap(p,i,j):
    x=p[j]-p[i]
    return x if x>0 else x+1

def owner_risk(owners,p):
    return 1-sum(max(gap(p,x,y) for x,y in zip(seq,seq[1:])) for seq in owners.values())

def direct_risk(n,p):
    circle=sorted(range(n),key=p.__getitem__)
    history=sorted(range(M),key=p.__getitem__)
    grouped=defaultdict(list)
    for ix,x in enumerate(circle):
        y=circle[(ix+1)%n]
        g=gap(p,x,y)
        midpoint=(p[x]+g/2)%1
        owner=max((j for j in history if p[j]<=midpoint),
                  key=p.__getitem__,default=history[-1])
        grouped[owner].append(g)
    assert len(grouped)==M
    return 1-sum(max(v) for v in grouped.values())

def check(theta):
    p=[(i*theta)%1 for i in range(END)]
    a=164*theta-43
    e=145-553*theta
    f=a-e
    assert 0<f<e<a
    owners={}
    for k in range(M):
        if k<25:
            seq=[k,k+164,k+328,k+492,k+656,k+103]
            lengths=[a,a,a,a,e]
        elif k<61:
            seq=[k,k+164,k+328,k+492,k+656,k+103,k+267,k+431,k+595,k+42]
            lengths=[a,a,a,a,e,a,a,a,e]
        else:
            seq=[k,k+164,k+328,k+492,k-61]
            lengths=[a,a,a,e]
        owners[k]=seq
        assert [gap(p,x,y) for x,y in zip(seq,seq[1:])]==lengths
    assert sorted({x for seq in owners.values() for x in seq})==list(range(717))
    left_owner={}
    remaining={}
    for k,seq in owners.items():
        starts=[x for x,y in zip(seq,seq[1:]) if gap(p,x,y)==a]
        assert len(starts)==(4 if k<25 else 7 if k<61 else 3)
        remaining[k]=len(starts)
        for x in starts:
            assert x not in left_owner
            left_owner[x]=k
    assert sorted(left_owner)==list(range(553))
    val=owner_risk(owners,p)
    assert val==1-128*a==direct_risk(717,p)
    counts={'zero_first':0,'positive_C':0,'zero_B':0,'positive_AB':0}
    checkpoints={717:val}
    for t in range(717,1270):
        j=t-717
        k=left_owner[j]
        seq=owners[k]
        indexes=[ix for ix in range(len(seq)-1) if seq[ix:ix+2]==[j,j+164]]
        assert len(indexes)==1
        assert gap(p,j,t)==f and gap(p,t,j+164)==e
        seq.insert(indexes[0]+1,t)
        remaining[k]-=1
        if j<=388:
            kind='zero_first'; expected=0
            assert remaining[k]>=1
        elif j<=455:
            kind='positive_C'; expected=f
            assert 61<=k<=127 and remaining[k]==0
        elif j<=491:
            kind='zero_B'; expected=0
            assert 25<=k<=60 and remaining[k]==1
        else:
            kind='positive_AB'; expected=f
            assert remaining[k]==0 and k<=60
        assert max(gap(p,x,y) for x,y in zip(seq,seq[1:]))==(a if remaining[k] else e)
        val+=expected
        counts[kind]+=1
        if t+1 in (718,800,1106,1107,1173,1209,1234,1270):
            assert val==owner_risk(owners,p)==direct_risk(t+1,p)
            checkpoints[t+1]=val
    assert counts=={'zero_first':389,'positive_C':67,'zero_B':36,'positive_AB':61}
    assert all(v==0 for v in remaining.values())
    assert sorted({x for seq in owners.values() for x in seq})==list(range(END))
    assert val==1-128*e==-18559+70784*theta
    assert checkpoints[1106]==1-128*a
    assert checkpoints[1173]==1-128*a+67*f
    assert checkpoints[1209]==checkpoints[1173]
    return checkpoints,counts

r1,c1=check(LO)
r2,c2=check(HI)
assert c1==c2
assert all((i*LO)//1==(i*HI)//1 for i in range(END))
assert sorted(range(END),key=lambda i:(i*LO)%1)==sorted(range(END),key=lambda i:(i*HI)%1)
print('PASS_S23_SOURCE_LABEL_SYNC_717_1270')
print('initial_a_gaps=553; owners_A=25_B=36_C=67; rational_interval_endpoints=2')
print('substitution_counts=',c1)
for n in sorted(r1):
    print('cut_n=%d risk_approx=%.15f'%(n,float((r1[n]+r2[n])/2)))
print('R(128,L=1142)=-18559+70784*theta')
