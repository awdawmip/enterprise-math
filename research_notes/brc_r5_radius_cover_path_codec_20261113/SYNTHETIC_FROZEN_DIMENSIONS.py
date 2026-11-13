"""Conditional synthetic wall sequence built from published R5 56B centers.
This is NOT the real pinned rational-wall event frequency. It shares only dims,
event total, maximum multiplicity, and exact published center list.
"""
from VERIFY_RADIUS_COVER_CODEC import index, covers, rank_centers, unrank
from collections import Counter
from hashlib import sha256
import json

OLD56 = 'd500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
raw=bytes.fromhex(OLD56)
assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
bits=int.from_bytes(raw[2:],'little')
center=[bits&3];bits>>=2
for _ in range(212):
    d=bits&3;bits>>=2
    assert d<3
    center.append(center[-1]+3+d)
assert len(center)==213 and center[0]==1 and center[-1]==952 and bits==0
h=Counter(b-a for a,b in zip(center,center[1:]))
assert h=={3:16,4:77,5:119}
inc=[1]*953
first_four=True
for p,q in zip(center,center[1:]):
    if q-p==3:inc[p+1]+=2  # [1,3,1]
    elif q-p==4:
        inc[p+1]+=1      # [1,2,1,1]
        if first_four:
            inc[p+1]+=1  # once [1,3,1,1]
            first_four=False
inc[0]+=1
inc[-1]+=1
assert Counter(inc)=={1:858,2:78,3:17} and sum(inc)==1065
x=[0]
for f in inc:x.append(x[-1]+f)
assert len(x)==954 and covers(x,center,2)
cache=index(x,2,213)
T=cache[3]
assert T>0
rank=rank_centers(cache,213,tuple(center))
assert unrank(cache,213,rank)==tuple(center)
out={'source_centers_sha256':sha256(raw).hexdigest(),
     'source_center_count':213,'source_gap_hist':dict(sorted(h.items())),
     'synthetic_frequency_hist':dict(sorted(Counter(inc).items())),
     'synthetic_total_events':x[-1], 'synthetic_boundaries':len(x),
     'same_centers_cover_radius_2':True,'radius_2_exact_feasible_class_count':str(T),
     'radius_2_feasible_class_bits':(T-1).bit_length(),
     'radius_2_feasible_class_bytes':((T-1).bit_length()+7)//8,
     'published_centers_class_rank':str(rank),
     'rank_roundtrip':True,
     'scope':'CONSTRUCTED synthetic E; not the pinned rational E; capacity is specific to this constructed E'}
print(json.dumps(out,indent=2,sort_keys=True))
