#!/usr/bin/env python3
"""R284CI exact compiler and sharp-radius certificate for frozen 34-bit Port observer."""
from bisect import bisect_right
from hashlib import sha256
from itertools import product
from math import comb
import json
P=17179869143
D=(1120832,6,13,1651128)
Z=(0,390139,394465,1497639)
SEL=(0,1,2,4,5,6)
SUP=(0,1,2,4,8,10,12,16,17,20,32,33,34)
FROZEN_SHA="b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4"
PRIOR_SHA="af2d3ec14228af03eb9658a3301c732e3025d69f007e7e971da404f80c5fb155"
PACK_SHA="61a0f876e1d007231c044894ffa251dce607ea2019a6942d5979ab439094870d"

def det(lo,top):
    u1,a11,x,y,u2,w,a22,z,u3,g,h,r=lo
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

def lower(key,fill):
    lo=[fill]*12
    for j,pos in enumerate(SEL):
        lo[pos]=1+((key>>(5-j))&1)
    return lo

def arcs():
    arr=[]
    for key in range(64):
        start=det(lower(key,2),15)
        width=det(lower(key,1),0)-start
        assert 0<width<P//2
        arr.append((start%P,width))
    return arr

def mobius(values,mod=None):
    v=list(values)
    for bit in range(6):
        for mask in range(64):
            if mask&(1<<bit):
                v[mask]-=v[mask^(1<<bit)]
                if mod:v[mask]%=mod
    return v

def compile100(aa):
    a=mobius([s for s,w in aa],P)
    b=mobius([w for s,w in aa])
    assert tuple(i for i in range(64) if a[i] or b[i])==SUP
    data=0;shift=0
    for mask in SUP:
        width=29 if mask==0 else 27
        assert 0<=a[mask]<(1<<34)
        assert 0<=b[mask]<(1<<29) if mask==0 else -(1<<26)<=b[mask]<(1<<26)
        data|=(a[mask] | ((b[mask]&((1<<width)-1))<<34))<<shift
        shift+=34+width
    assert shift==795
    blob=data.to_bytes(100,"little")
    assert sha256(blob).hexdigest()==PACK_SHA
    return blob

def decode100(blob):
    assert len(blob)==100
    value=int.from_bytes(blob,"little");shift=0;pairs=[]
    for mask in SUP:
        width=29 if mask==0 else 27
        x=(value>>shift)&((1<<(34+width))-1)
        a=x&((1<<34)-1)
        b=(x>>34)&((1<<width)-1)
        if mask!=0 and b&(1<<26):b-=1<<27
        assert 0<=a<P
        pairs.append((a,b))
        shift+=34+width
    assert shift==795 and value>>shift==0
    return [(sum(a for m,(a,b) in zip(SUP,pairs) if (k&m)==m)%P,
             sum(b for m,(a,b) in zip(SUP,pairs) if (k&m)==m))
             for k in range(64)]

def direct(aa,y2,rho2):
    mask=0
    for k,(a,w) in enumerate(aa):
        d=(y2-2*a)%(2*P)
        if d<=2*w+rho2 or d>=2*P-rho2:mask|=1<<k
    return mask

def sweep(aa):
    events=sorted([(a,-1,k,1) for k,(a,w) in enumerate(aa)]+
                  [((a+w)%P,1,k,-1) for k,(a,w) in enumerate(aa)])
    assert len({e[0] for e in events})==128
    state=direct(aa,0,0);after=[]
    for base,sign,key,action in events:
        if action==1:state|=1<<key
        else:state&=~(1<<key)
        after.append(state)
    assert state==direct(aa,0,0)
    return events,after

def rank(mask):
    bits=[j for j in range(64) if (mask>>j)&1]
    return sum(comb(64,j) for j in range(len(bits)))+sum(comb(v,i+1) for i,v in enumerate(bits))

def prior_blob(events,after):
    endpoints=b"".join(x.to_bytes(5,"little") for x,s,k,a in events)
    shifts=sum(1<<i for i,e in enumerate(events) if e[1]==1).to_bytes(16,"little")
    codes=sum(rank(m)<<(20*i) for i,m in enumerate(after)).to_bytes(320,"little")
    return endpoints+shifts+codes

def lookup(events,after,y2,rho2):
    y2%=2*P
    boundaries=[2*x+s*rho2 for x,s,k,action in events]
    j=(bisect_right(boundaries,y2)-1)%128
    ans=after[j]
    if boundaries[j]==y2:ans|=after[(j-1)%128]
    return ans

def check():
    aa=arcs()
    blob=compile100(aa)
    rebuilt=decode100(blob)
    assert rebuilt==aa
    events,after=sweep(rebuilt)
    assert sha256(prior_blob(events,after)).hexdigest()==PRIOR_SHA
    closing=[((events[(i+1)%128][0]-events[i][0])%P,i)
             for i in range(128)
             if events[i][1]==1 and events[(i+1)%128][1]==-1]
    assert len(closing)==40 and min(closing)==(4226124,43)
    assert (events[43][0],events[43][2],events[44][0],events[44][2])==(6594783455,45,6599009579,8)
    cut=min([e[0] for e in events if e[1]==-1]+
            [P-e[0] for e in events if e[1]==1])
    assert cut==23581912>2113062
    digest=sha256();queries=0;boundary=0
    radii2=(0,1182,4226122,4226123)
    for topbits in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(topbits))
        for lo in product((1,2),repeat=12):
            word=det(lo,top)%P
            digest.update(word.to_bytes(8,"big"))
            for r2 in radii2:
                assert lookup(events,after,2*word,r2)==direct(rebuilt,2*word,r2)
                queries+=1
    assert digest.hexdigest()==FROZEN_SHA and queries==262144
    for r2 in radii2:
        for pos,sign,key,action in events:
            y2=2*pos+sign*r2
            assert lookup(events,after,y2,r2)==direct(rebuilt,y2,r2)
            boundary+=1
    assert boundary==512
    bad=lookup(events,after,13193793034,4226126)
    actual=direct(rebuilt,13193793034,4226126)
    assert bad==0x8100 and actual==0x200000008100
    return {
        "schema":"R284CI_EXACT_RECALCULATION_V1",
        "frozen_codeword_sha256":digest.hexdigest(),
        "compiled_index_sha256":sha256(prior_blob(events,after)).hexdigest(),
        "coefficient_payload_sha256":sha256(blob).hexdigest(),
        "coefficient_payload_bytes":len(blob),
        "coefficient_payload_hex":blob.hex(),
        "first_collision_half_integer_radius":2113062,
        "first_collision_event_positions":[events[43][0],events[44][0]],
        "first_collision_keys_exit_entry":[45,8],
        "tested_codewords":65536,"lookup_checks":queries,
        "exact_boundary_checks":boundary,
        "sharpness_counterexample":{"rho":2113063,"y":6596896517,
                                   "fixed_template_mask":hex(bad),
                                   "direct_mask":hex(actual)},
        "scientific_review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
