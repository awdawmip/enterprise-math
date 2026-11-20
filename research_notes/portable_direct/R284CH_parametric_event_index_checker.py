#!/usr/bin/env python3
"""R284CH: exact parametric circle-event index for the frozen R284BZ Port model.
No third-party dependencies; exhaustive finite verification with integer/rational arithmetic.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb
import json

P=17179869143
D=(1120832,6,13,1651128)
Z=(0,390139,394465,1497639)
SELECTED=(0,1,2,4,5,6)
FROZEN_SHA="b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"


def determinant(lower,top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=lower
    t,s=6-a11,13-a22
    u=t*s-x*w
    v=-r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2=s*u1+x*u2,t*u2+w*u1
    q1=-r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2=-r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3=u*u3+p1*g+p2*h
    k=(u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base=D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top&(1<<j))


def lower_for_key(key,fill):
    v=[fill]*12
    for j,pos in enumerate(SELECTED):v[pos]=1+((key>>(5-j))&1)
    return v


def arcs():
    out=[]
    for key in range(64):
        low=determinant(lower_for_key(key,2),15)
        high=determinant(lower_for_key(key,1),0)
        assert 0<high-low<P/2
        out.append((low%P,high-low))
    return out


def direct_mask(arc_list,y2,rho2):
    mask=0
    for j,(a,w) in enumerate(arc_list):
        d=(y2-2*a)%(2*P)
        if d<=2*w+rho2 or d>=2*P-rho2:
            mask|=1<<j
    return mask


def build_index(arc_list):
    # The signed boundary is a-rho for entry, a+w+rho for exit.
    entries=[]
    for key,(a,w) in enumerate(arc_list):
        entries.extend([(a,-1,key,1),((a+w)%P,1,key,-1)])
    entries.sort()
    bases=[e[0] for e in entries]
    assert len(set(bases))==128
    gaps=[bases[i+1]-bases[i] for i in range(127)]+[bases[0]+P-bases[-1]]
    assert min(gaps)==4226124
    assert min(bases[0],P-bases[-1])==23581912
    mask=direct_mask(arc_list,0,0)
    after=[]
    for base,shift,key,action in entries:
        if action==1:mask|=1<<key
        else:mask&=~(1<<key)
        after.append(mask)
    assert mask==direct_mask(arc_list,0,0)
    assert max(v.bit_count() for v in after)==4
    return entries,after,gaps


def lookup(entries,after,y2,rho2):
    # y2=2*y, rho2=2*rho: integers or exact Fraction values.
    y2%=2*P
    lo,hi=0,len(entries)
    while lo<hi:
        mid=(lo+hi)//2
        base,shift,_,_=entries[mid]
        if 2*base+shift*rho2<=y2:lo=mid+1
        else:hi=mid
    j=(lo-1)%128
    answer=after[j]
    base,shift,_,_=entries[j]
    if 2*base+shift*rho2==y2:
        answer|=after[(j-1)%128]
    return answer


def rank(mask):
    bits=[j for j in range(64) if mask>>j&1]
    k=len(bits)
    assert k<=4
    return sum(comb(64,j) for j in range(k))+sum(comb(v,i+1) for i,v in enumerate(bits))


def unrank(r):
    for k in range(5):
        offset=sum(comb(64,j) for j in range(k))
        if r<offset+comb(64,k):break
    else:raise ValueError(r)
    r-=offset
    v=63
    bits=[]
    for j in range(k,0,-1):
        while comb(v,j)>r:v-=1
        bits.append(v)
        r-=comb(v,j)
        v-=1
    assert r==0
    return sum(1<<i for i in bits)


def pack_index(entries,after):
    # 128*5B integer circle endpoints + 128 shift bits + 128*20-bit colex codes.
    coords=b''.join(base.to_bytes(5,'little') for base,_,_,_ in entries)
    shifts=sum((1<<i) for i,e in enumerate(entries) if e[1]==1).to_bytes(16,'little')
    codes=sum(rank(mask)<<(20*i) for i,mask in enumerate(after)).to_bytes(320,'little')
    for v in after:assert unrank(rank(v))==v
    assert len(coords+shifts+codes)==976
    return coords+shifts+codes


def verify():
    aa=arcs()
    entries,after,gaps=build_index(aa)
    binary=pack_index(entries,after)
    assert len(set(after))==115
    assert sum(v==0 for v in after)==14
    assert dict(sorted(Counter(v.bit_count() for v in after).items()))=={0:14,1:43,2:46,3:21,4:4}
    for rho2 in (0,59,1182):
        for base,shift,_,_ in entries:
            x2=2*base+shift*rho2
            assert lookup(entries,after,x2,rho2)==direct_mask(aa,x2,rho2)
    seen=set()
    digest=sha256()
    word_hist=Counter()
    tested=0
    for topbits in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(topbits))
        for lower in product((1,2),repeat=12):
            x=determinant(lower,top)%P
            digest.update(x.to_bytes(8,'big'))
            baseline=direct_mask(aa,2*x,0)
            for rho2 in (0,59,1182):
                assert lookup(entries,after,2*x,rho2)==baseline
                tested+=1
            seen.add(baseline)
            word_hist[baseline.bit_count()]+=1
    assert digest.hexdigest()==FROZEN_SHA
    assert len(seen)==114 and seen==set(after)-{0}
    assert dict(word_hist)=={1:23178,2:23094,3:16964,4:2300}
    return {
        'schema':'R284CH_PARAMETRIC_EVENT_INDEX_EXACT_V1',
        'source':'Frozen R284BZ/R284CG 34-bit Port observer',
        'model':{'p':P,'d':D,'z':Z,'selected_lower_positions':SELECTED},
        'frozen_codeword_sha256':FROZEN_SHA,
        'codewords_verified':65536,
        'radius_values_tested_rho2':[0,59,1182],
        'codeword_lookup_tests':tested,
        'boundary_lookup_tests':128*3,
        'events':len(entries),'distinct_event_positions':len(set(e[0] for e in entries)),
        'minimum_circular_raw_boundary_gap':min(gaps),
        'minimum_distance_raw_event_to_origin':min(entries[0][0],P-entries[-1][0]),
        'maximum_event_cell_overlap':max(v.bit_count() for v in after),
        'event_cell_overlap_histogram':dict(sorted(Counter(v.bit_count() for v in after).items())),
        'distinct_cell_signatures':len(set(after)),
        'zero_signature_cells':sum(v==0 for v in after),
        'codeword_realized_signatures':len(seen),
        'word_signature_count_histogram':dict(sorted(word_hist.items())),
        'signature_space_for_max_four':sum(comb(64,k) for k in range(5)),
        'signature_rank_bits':20,
        'packed_index_bytes':len(binary),
        'packed_index_sha256':sha256(binary).hexdigest(),
        'packed_index_hex':binary.hex(),
        'certificate_note':'Full real-rho correctness from endpoint order/no-crossing and closed-boundary union; tests are exact integer endpoints and full codeword domain.',
        'review':'NOT_REVIEWED'
    }


if __name__=='__main__':
    print(json.dumps(verify(),indent=2,ensure_ascii=False))
