#!/usr/bin/env python3
"""Independent finite S23 labelled-source sweep using R54 Farey cut order.
No R53 treap dependence; all source owners are audited from raw phase enclosures.
"""
from bisect import bisect_right
from pathlib import Path
from VERIFY_R54_PUBLISHED import order
import json, hashlib

A=262204504569236716045286
B=A+1
D=10**24
m,H=128,225
K=m+H-1
P,Q=A+B,2*D
cuts, (a,i,c,j), blocks=order(P,Q,K,K)
assert len(cuts)==K==352 and len(set(cuts))==K

# Three-gap cyclic step law in the exact frozen rational enclosure.
u_num=i*P-a*Q
v_num=c*Q-j*P
assert u_num>0 and v_num>0 and j*u_num+i*v_num==Q
kind_counts={'u':0,'v':0,'u+v':0}
for idx,s in enumerate(cuts):
    nxt=cuts[(idx+1)%len(cuts)]
    if s>i:
        kind='u'
    elif s+j<=K:
        kind='v'
    else:
        kind='u+v'
    kind_counts[kind]+=1
    step={ 'u':u_num, 'v':v_num,'u+v':u_num+v_num }[kind]
    assert ((-nxt*P)-(-s*P))%Q==step%Q
assert kind_counts=={'u':K-i,'v':K-j,'u+v':i+j-K}
assert kind_counts['u']*u_num+kind_counts['v']*v_num+kind_counts['u+v']*(u_num+v_num)==Q

# Full historical intervals indexed by original z=0..m-1.
history=sorted(((z*P)%Q,z) for z in range(m))
hphase=[ph for ph,z in history]
pred={z:history[ii-1][1] for ii,(_,z) in enumerate(history)}
assert len(set(hphase))==m

def reconstruct(s,t,den):
    hh=sorted(((z*t)%den,z) for z in range(m))
    pt=[v for v,z in hh]
    return [-1]+[hh[bisect_right(pt, ((s-r)*t)%den)-1][1] for r in range(1,H+1)]

owners=reconstruct(cuts[0],P,Q)
assert owners==reconstruct(cuts[0],A,D)==reconstruct(cuts[0],B,D)
moves=0
changes=0
last_vector=None
for idx,s in enumerate(cuts):
    # The source owner depends on the observation cell (s theta) and age r.
    assert owners==reconstruct(s,P,Q)
    assert owners==reconstruct(s,A,D)
    assert owners==reconstruct(s,B,D)
    v=[None]*m
    for r in range(1,H+1):
        z=owners[r]
        if v[z] is None: v[z]=r
    if last_vector is not None and v!=last_vector: changes+=1
    last_vector=v
    # Cross this exact cut in descending order.
    for z in range(max(0,s-H), min(m-1,s-1)+1):
        r=s-z
        assert owners[r]==z,(idx,s,z,r,owners[r])
        owners[r]=pred[z]
        moves+=1
# all K cuts; total events sum mH and cyclic return exactly
assert moves==m*H==28800
assert owners==reconstruct(cuts[0],P,Q)

cert={'schema':'R54_S23_EXACT_SWEEP_V1','frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','enclosure':[str(A),str(B),str(D)],'m':m,'H':H,'K':K,'farey_bracket':[a,i,c,j], 'batch_blocks':blocks,'gap_types':kind_counts,'gap_numerators':[str(u_num),str(v_num)],'gap_denominator':str(Q),'cuts_verified':len(cuts),'moves':moves,'changes':changes,'starting_ten':cuts[:10], 'complete_order_sha256':hashlib.sha256(','.join(map(str,cuts)).encode()).hexdigest(),'result':'PASS'}
with open(Path(__file__).with_name('R54_SWEEP_CERTIFICATE.json'),'w') as f:json.dump(cert,f,indent=2,ensure_ascii=False)
print('PASS_R54_S23_352_CUT_SWEEP', 'moves',moves,'changes',changes,'gaps',kind_counts,'farey', [a,i,c,j])
