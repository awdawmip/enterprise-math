#!/usr/bin/env python3
"""Exact Fraction verification of source-labelled S23/AV risk through n=1107.

Inherited S23 theta enclosure is strictly open. Every assertion uses exact
rationals and phase labels; the last float conversion is display-only.
"""
from collections import defaultdict
from fractions import Fraction as Q

LO = Q(262204504569236716045286, 10**24)
HI = Q(262204504569236716045287, 10**24)
M = 128
END = 1107

def gap(x, y):
    z = y-x
    return z if z>0 else z+1

def risk(owners, p):
    return 1-sum(max(gap(p[i],p[j]) for i,j in zip(seq,seq[1:])) for seq in owners.values())

def direct(n, p):
    """Independent full circle ordering and owner grouping."""
    hist=sorted(range(M), key=p.__getitem__)
    circ=sorted(range(n), key=p.__getitem__)
    groups=defaultdict(list)
    for pos,i in enumerate(circ):
        j=circ[(pos+1)%n]
        length=gap(p[i],p[j])
        middle=(p[i]+length/2)%1
        h=max((q for q in hist if p[q]<=middle), key=p.__getitem__, default=hist[-1])
        groups[h].append(length)
    assert len(groups)==M
    return 1-sum(max(g) for g in groups.values())

def certify(theta):
    p=[(i*theta)%1 for i in range(END)]
    a=164*theta-43
    d=16-61*theta
    b=d-a
    c=b-a
    e=c-a
    f=a-e
    assert 0<f<e<a<c<b<d
    owners={}
    for k in range(M):
        if k<25:
            seq=[k,k+164,k+328,k+492,k+103]
            lengths=[a,a,a,c]
        elif k<61:
            seq=[k,k+164,k+328,k+492,k+103,k+267,k+431,k+595,k+42]
            lengths=[a,a,a,c,a,a,a,e]
        else:
            seq=[k,k+164,k+328,k+492,k-61]
            lengths=[a,a,a,e]
        owners[k]=seq
        assert [gap(p[x],p[y]) for x,y in zip(seq,seq[1:])]==lengths
    assert sorted({i for seq in owners.values() for i in seq})==list(range(656))
    val=risk(owners,p)
    assert val==(-2047+7808*theta)+256*a+67*e
    assert val==direct(656,p)
    for t in range(656,717):
        k=t-656
        seq=owners[k]
        left,right=k+492,k+103
        where=[i for i in range(len(seq)-1) if seq[i:i+2]==[left,right]]
        assert len(where)==1
        assert (gap(p[left],p[t]),gap(p[t],p[right]))==(a,e)
        before=max(gap(p[x],p[y]) for x,y in zip(seq,seq[1:]))
        assert before==c
        seq.insert(where[0]+1,t)
        after=max(gap(p[x],p[y]) for x,y in zip(seq,seq[1:]))
        assert after==a and before-after==e
        val+=e
    assert sorted({i for seq in owners.values() for i in seq})==list(range(717))
    assert val==1-128*a==direct(717,p)
    left_label_owner={}
    counts=defaultdict(int)
    for owner,seq in owners.items():
        for left,right in zip(seq,seq[1:]):
            length=gap(p[left],p[right])
            assert length in (a,e)
            if length==a:
                assert right==left+164 and left not in left_label_owner
                left_label_owner[left]=owner
                counts[owner]+=1
    assert sorted(left_label_owner)==list(range(553))
    assert all(counts[k]==(4 if k<25 else 7 if k<61 else 3) for k in range(M))
    for t in range(717,1106):
        j=t-717
        owner=left_label_owner[j]
        seq=owners[owner]
        loc=[i for i in range(len(seq)-1) if seq[i:i+2]==[j,j+164]]
        assert len(loc)==1
        assert (gap(p[j],p[t]),gap(p[t],p[j+164]))==(f,e)
        assert counts[owner]>=2
        seq.insert(loc[0]+1,t)
        counts[owner]-=1
        assert max(gap(p[x],p[y]) for x,y in zip(seq,seq[1:]))==a
        if t+1 in (718,800,1000,1106):
            assert risk(owners,p)==1-128*a==direct(t+1,p)
    assert all(counts[k]>=1 for k in range(M))
    assert sorted({i for seq in owners.values() for i in seq})==list(range(1106))
    assert val==1-128*a==direct(1106,p)
    t=1106
    j=t-717
    owner=left_label_owner[j]
    assert owner==61 and counts[owner]==1
    seq=owners[owner]
    where=next(i for i in range(len(seq)-1) if seq[i:i+2]==[j,j+164])
    assert (gap(p[j],p[t]),gap(p[t],p[j+164]))==(f,e)
    seq.insert(where+1,t)
    assert max(gap(p[x],p[y]) for x,y in zip(seq,seq[1:]))==e
    assert risk(owners,p)==1-128*a+f==direct(1107,p)
    assert risk(owners,p)==5317-20275*theta
    return 1-128*a,1-128*a+f

left=certify(LO)
right=certify(HI)
assert all((i*LO)//1==(i*HI)//1 for i in range(END))
assert sorted(range(END),key=lambda i:(i*LO)%1)==sorted(range(END),key=lambda i:(i*HI)%1)
print("PASS_S23_SOURCE_GAP_SYNCHRONIZE_PLATEAU_1107")
print("new_positive_e=61, flat_389=389, post_plateau_positive_f=1")
print("max_gap_left_labels_at_n717=553 (exact consecutive 0..552)")
print("R(128,717-128)=R(128,1106-128)=5505-20992*theta")
print("R(128,1107-128)=5317-20275*theta")
print("R_n717_approx=%.15f" % float(sum(x[0] for x in (left,right))/2))
print("R_n1107_approx=%.15f" % float(sum(x[1] for x in (left,right))/2))
