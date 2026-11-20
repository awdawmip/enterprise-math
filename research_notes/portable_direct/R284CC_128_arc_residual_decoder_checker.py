#!/usr/bin/env python3
"""Exact R284CC 128-arc residual decoder. Requires Python standard library only.

The finite interval sweep establishes its bound for ALL real circular queries:
interval membership is piecewise constant between exact endpoints.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product, permutations
from json import loads
from pathlib import Path

P=17179869143
D0,D3,Z1,Z2,Z3=1120832,1651128,390139,394465,1497639
R=Fraction(59,2)
TWO_RHO=59
N_PREFIX=7
N_SUFFIX=5

def record(L):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=L
    t,s=6-a11,13-a22
    U=t*s-x*w
    V=-r*U-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=U*u3+p1*g+p2*h
    k=(U*D3+V,p1*D3+q1,p2*D3+q2,q3)
    base=(D0*k[0]-Z1*k[1]-Z2*k[2]-Z3*k[3]-sum(k))%P
    return base,k

def word(rec,bits):
    base,k=rec
    return (base-sum(v for j,v in enumerate(k) if bits>>j&1))%P

def arc(points):
    v=sorted(points)
    assert len(set(v))==len(v)
    gaps=[b-a for a,b in zip(v,v[1:])]+[P+v[0]-v[-1]]
    j=max(range(len(gaps)),key=lambda i:gaps[i])
    return v[(j+1)%len(v)],P-gaps[j]

def group_arcs(records):
    out=[]
    for group in range(128):
        words=[word(records[i],b)
               for i in range(group*32,(group+1)*32) for b in range(16)]
        assert len(words)==512
        out.append(arc(words))
    return out

def contains(a,y):
    start,width=a
    return (2*(y-start)+TWO_RHO)%(2*P)<=2*width+2*TWO_RHO

def overlap_certificate(arcs):
    # Circle in doubled coordinates: closed radius=29.5 intervals.
    M=2*P
    events=[]
    for start,width in arcs:
        a=(2*start-TWO_RHO)%M
        length=2*width+2*TWO_RHO
        assert 0<length<M
        end=a+length
        if end<M:
            events.extend(((a,1),(end,-1)))
        elif end>M:
            events.extend(((a,1),(M,-1),(0,1),(end-M,-1)))
        else:
            events.extend(((a,1),(M,-1),(0,1),(0,-1)))
    events.sort(key=lambda v:(v[0],-v[1]))
    active=peak=0
    witness=None
    for x,d in events:
        active+=d
        if active>peak:
            peak,witness=active,x
    assert active==0
    coords={0}|{x for x,d in events if x<M}
    assert peak==max(sum(contains(a,Fraction(x,2)) for a in arcs)
                     for x in coords)
    return peak,witness,len(events),len(coords)

def lift(base,y,span):
    d=(base-y)%P
    if d>span+R:
        d-=P
    return d if -R<=d<=span+R else None

def greedy(delta,k):
    bits=0
    for j,v in enumerate(k):
        bit=int(2*delta>v+sum(k[j+1:]))
        bits|=bit<<j
        delta-=bit*v
    return bits if abs(delta)<R else None

def decode(y,arcs):
    # Only 128 stored index pairs. All lower cofactors reconstructed on demand.
    answers=[]
    group_count=lower_count=0
    for group,a in enumerate(arcs):
        if not contains(a,y):
            continue
        group_count+=1
        prefix=tuple(1+((group>>(6-j))&1) for j in range(7))
        for suffix_index,suffix in enumerate(product((1,2),repeat=5)):
            lower_count+=1
            base,k=record(prefix+suffix)
            d=lift(base,y,sum(k))
            if d is None:
                continue
            bits=greedy(d,k)
            if bits is not None:
                answers.append((group*32+suffix_index,bits))
    return sorted(set(answers)),group_count,lower_count

def direct_determinant(L,bits):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=L
    a=[1+(bits>>j&1) for j in range(4)]
    M=((D0-a[0],-a[1]-Z1,-a[2]-Z2,-a[3]-Z3),
       (-u1,6-a11,-x,-y),(-u2,-w,13-a22,-z),
       (-u3,-g,-h,D3-r))
    total=0
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4)
                       for j in range(i+1,4))
        term=1
        for i,j in enumerate(perm):
            term*=M[i][j]
        total+=(-1 if inversions%2 else 1)*term
    return total%P

def verify():
    all_lower=list(product((1,2),repeat=12))
    records=[record(L) for L in all_lower]
    arcs=group_arcs(records)
    peak,x,nevents,ncoords=overlap_certificate(arcs)
    assert (peak,x,nevents,ncoords)==(8,9292040759,260,257)
    assert (min(w for _,w in arcs),max(w for _,w in arcs))==(270081253,429027781)
    certificate=loads(Path(__file__).with_name(
        "R284CC_128_arc_residual_decoder_verification.json").read_text())
    assert arcs==[tuple(v) for v in certificate["arc_index"]]
    assert certificate["maximum_overlapping_noise_expanded_group_arcs_any_real_query"]==peak
    # Recheck the EXACT original R284CB codeword ordering and SHA-256.
    digest=sha256()
    ordered=[]
    for top in product((1,2),repeat=4):
        bits=sum((a-1)<<j for j,a in enumerate(top))
        for i,rec in enumerate(records):
            val=word(rec,bits)
            digest.update(val.to_bytes(8,"big"))
            ordered.append((val,i,bits))
    assert digest.hexdigest()=="b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"
    ordered.sort()
    assert len({v for v,_,_ in ordered})==65536
    pairs=list(zip(ordered,ordered[1:]))+[(ordered[-1],ordered[0])]
    gaps=[(b[0]-a[0])%P for a,b in pairs]
    assert min(gaps)==59 and gaps.count(59)==64
    assert sum(k[3]==59 for _,k in records)==8
    for (va,ia,ba),(vb,ib,bb) in (p for p,g in zip(pairs,gaps) if g==59):
        assert ia==ib and ba^bb==8 and records[ia][1][3]==59
    assert all(contains(arcs[i>>5],v) for v,i,bits in ordered)
    independent=0
    for i in range(0,4096,17):
        for bits in (0,5,10,15):
            assert direct_determinant(all_lower[i],bits)==word(records[i],bits)
            independent+=1
    total=0
    for val,i,bits in ordered[::113]:
        for noise in (-29,0,29,Fraction(-117,4),Fraction(117,4)):
            answers,ng,nl=decode((val+noise)%P,arcs)
            assert answers==[(i,bits)] and ng<=8 and nl<=256
            total+=1
    assert independent==964 and total==2900
    print({"groups":len(arcs),"all_real_max_overlap":peak,
           "max_lower_checks":256,"max_top_thresholds":1024,
           "complete_codewords":len(ordered),"min_gap":59,
           "gap59_pairs":64,"Leibniz_checks":independent,
           "selected_full_decoder_trials":total,"review":"NOT_REVIEWED"})

if __name__=="__main__":
    verify()
