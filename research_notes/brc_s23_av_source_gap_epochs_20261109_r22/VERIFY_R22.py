#!/usr/bin/env python3
"""Exact-Fraction validation of the S23 phase-arc cascade up to n=656.

Certifies all theta in (lo,hi) via affine comparison stability at both
rational endpoints; no floating point enters any assertion.
"""
from fractions import Fraction as F
from collections import defaultdict

LO = F(262204504569236716045286,10**24)
HI = F(262204504569236716045287,10**24)
M = 128
END = 656
# t_start,t_end_inclusive,owner_first,source_gap_offset_pair,delta_type,split_type
EPOCHS = [
 (225,291,61,(0,-61),'a','ab','C1'),
 (292,327,25,(103,42),'z','ab','B1'),
 (328,352,0,(164,103),'a','ab','A1'),
 (353,388,25,(164,103),'a','ab','B2'),
 (389,455,61,(164,-61),'a','ac','C2'),
 (456,491,25,(267,42),'z','ac','B3'),
 (492,516,0,(328,103),'a','ac','A2'),
 (517,552,25,(328,103),'a','ac','B4'),
 (553,619,61,(328,-61),'e','ae','C3'),
 (620,655,25,(431,42),'z','ae','B5'),
]

def circ_diff(x,y):
    z=y-x
    return z if z>0 else z+1

def check(theta):
    p = [(i*theta)%1 for i in range(END)]
    a=164*theta-43
    d=16-61*theta
    b=d-a
    c=b-a
    e=c-a
    assert 0<e<a<c<b<d
    assert 1-128*d== -2047+7808*theta
    h=sorted(range(M),key=p.__getitem__)
    actual_h_succ={h[i]:h[(i+1)%M] for i in range(M)}
    candidates={}
    for k in range(M):
        j=k+103 if k<25 else k+42 if k<61 else k-61
        candidates[k]=j
        want= d+a if k<25 else a+2*d if k<61 else d
        assert circ_diff(p[k],p[j])==want
    assert candidates==actual_h_succ
    assert 25*(a+d)+36*(a+2*d)+67*d==1
    # Directly reconstruct P_225 using these three exhaustive families.
    arcs={}
    for k in range(M):
        if k<25:
            arcs[k]=[k,k+164,k+103]
            lengths=[a,d]
        elif k<61:
            arcs[k]=[k,k+164,k+103,k+42]
            lengths=[a,d,d]
        else:
            arcs[k]=[k,k-61]
            lengths=[d]
        assert [circ_diff(p[x],p[y]) for x,y in zip(arcs[k],arcs[k][1:])]==lengths
    assert sorted({x for seq in arcs.values() for x in seq})==list(range(225))
    risk=1-128*d
    assert risk == 1-sum(max(circ_diff(p[i],p[j]) for i,j in zip(z,z[1:])) for z in arcs.values())
    counters=defaultdict(int)
    samples={225:risk}
    for lo,hi,owner_first,(off1,off2),delta_tag,split_tag,tag in EPOCHS:
        for t in range(lo,hi+1):
            k=owner_first+t-lo
            seq=arcs[k]
            src,dst=k+off1,k+off2
            edge_positions=[z for z in range(len(seq)-1) if seq[z:z+2]==[src,dst]]
            assert len(edge_positions)==1,(tag,k,src,dst)
            z=edge_positions[0]
            left=circ_diff(p[src],p[t]); right=circ_diff(p[t],p[dst])
            if split_tag=='ab': assert (left,right)==(a,b)
            elif split_tag=='ac': assert (left,right)==(a,c)
            else: assert (left,right)==(a,e)
            old_max=max(circ_diff(p[i],p[j]) for i,j in zip(seq,seq[1:]))
            seq.insert(z+1,t)
            new_max=max(circ_diff(p[i],p[j]) for i,j in zip(seq,seq[1:]))
            delta=old_max-new_max
            expected = {'z':F(0),'a':a,'e':e}[delta_tag]
            assert delta==expected,(tag,t,k,delta,expected)
            risk+=delta
            counters[tag]+=1
            # Independent all-historical-interval recomputation at checkpoints
            if t+1 in (292,328,456,492,553,620,656):
                direct=1-sum(max(circ_diff(p[i],p[j]) for i,j in zip(q,q[1:])) for q in arcs.values())
                assert risk==direct
                # Independent circular sort/owner assignment, not using arcs[k].
                n=t+1
                circle=sorted(range(n),key=p.__getitem__)
                grouped=defaultdict(list)
                for ix,i in enumerate(circle):
                    j=circle[(ix+1)%n]
                    length=circ_diff(p[i],p[j])
                    mid=(p[i]+length/2)%1
                    # Historical owners are clockwise predecessors of mid.
                    owner=max((h0 for h0 in range(M) if p[h0]<=mid),
                              key=lambda h0:p[h0],default=h[-1])
                    grouped[owner].append(length)
                assert len(grouped)==M
                independent=1-sum(max(v) for v in grouped.values())
                assert independent==risk
                samples[t+1]=risk
    assert sorted({x for seq in arcs.values() for x in seq})==list(range(END))
    for k,n in [('C1',67),('B1',36),('A1',25),('B2',36),('C2',67),('B3',36),('A2',25),('B4',36),('C3',67),('B5',36)]:
        assert counters[k]==n
    base=-2047+7808*theta
    expect={225:base,292:base+67*a,328:base+67*a,456:base+195*a,
            492:base+195*a,553:base+256*a,620:base+256*a+67*e,
            656:base+256*a+67*e}
    assert samples==expect
    return samples,counters

l_samples,l_counts=check(LO)
h_samples,h_counts=check(HI)
assert l_counts==h_counts
# For every i<656, the wrapped phase floor and full P_656 circular
# order are stable across the whole strict open theta interval.
assert all((i*LO).__floor__()==(i*HI).__floor__() for i in range(END))
assert sorted(range(END),key=lambda i:(i*LO)%1)==sorted(range(END),key=lambda i:(i*HI)%1)
# Every gap, risk and comparison used by the claimed symbolic schedule is
# affine once these floors are fixed; endpoint signs/equalities certify
# the entire interval.
print('PASS_S23_EXACT_SOURCE_LABEL_EPOCHS_225_656')
print('certified_theta_open_interval=',str(LO),'..',str(HI))
print('initial_history_arcs=128', 'insertions=431', 'endpoint_certifications=2')
print('epochs=',','.join('%s:%d'%item for item in l_counts.items()))
for n in sorted(l_samples):
    print('R_128_n n=%d approx=%.15f' % (n,float((l_samples[n]+h_samples[n])/2)))
print('R(128,656-128) = -3340 + 12741*theta')
