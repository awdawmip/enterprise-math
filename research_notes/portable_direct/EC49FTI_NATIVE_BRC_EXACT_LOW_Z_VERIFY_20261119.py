#!/usr/bin/env python3
"""Verify EC49FTI against its separately supplied self-contained native evidence archive.

Extract EC49FTI_NATIVE_BRC_2D_LOW_Z_FAN_EVIDENCE_20261119.tar.xz.
Then run:
    python EC49FTI_NATIVE_BRC_EXACT_LOW_Z_VERIFY_20261119.py --evidence-root <extracted-dir>
    python EC49FTI_NATIVE_BRC_EXACT_LOW_Z_VERIFY_20261119.py --evidence-root <extracted-dir> --full --start 0 --stop 6
    python EC49FTI_NATIVE_BRC_EXACT_LOW_Z_VERIFY_20261119.py --evidence-root <extracted-dir> --independent
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter

p=argparse.ArgumentParser()
p.add_argument('--evidence-root',default='.')
p.add_argument('--full',action='store_true')
p.add_argument('--start',type=int,default=0)
p.add_argument('--stop',type=int,default=18)
p.add_argument('--independent',action='store_true')
args=p.parse_args()
root=Path(args.evidence_root).resolve()
sys.path.insert(0,str(root/'native_code'))
from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN,solve
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
cert=json.loads((root/'EC49FTI_CERT.json').read_text())
assert len(V)==228 and all(len(v)==141 for v in V)
assert len(cert['anchors'])==18 and len(cert['usage'])==7
assert cert['source_pin'].endswith(PIN)

for f,digest in cert['source_sha256'].items():
    assert hashlib.sha256((root/'source'/f).read_bytes()).hexdigest()==digest
    print('SOURCE_SHA256_MATCH',f,flush=True)

for name,usage in cert['usage'].items():
    tf=root/'trees'/f'{name}.json'
    assert hashlib.sha256(tf.read_bytes()).hexdigest()==cert['tree_sha256'][name]
    node=json.loads(tf.read_text());count=Counter()
    for state in range(141):
        curr=node;used=set()
        while 'named_observer' in curr:
            q=curr['named_observer']
            assert 0<=q<228 and q not in used
            used.add(q);count[q]+=1
            curr=curr['children'][str(V[q][state])]
        assert curr=={'leaf':state}
    actual=[sum(count.values()),count[32],count[34],count[140]]
    assert actual==usage,(name,actual,usage)
    print('NATIVE_141_PROFILE_TREE_MATCH',name,usage,flush=True)

A=Q(3,4);lo,hi=Q(7,16),Q(57,128);zl,zh=Q(3,8),Q(3,5)

def cost(name,b,z):
    u,n32,n34,n140=cert['usage'][name]
    return Q(u)-n32*(A if name[0]=='D' else b)-n34*(b if name[0]=='D' else A)-n140*z

def exact(o,b,z):
    return min(cost(k,b,z) for k in cert['usage'] if k.startswith(o))

cell_vertices={
    'D20':[(lo,zl),(hi,zl),(lo,lo),(hi,hi)],
    'D24':[(lo,lo),(hi,hi),(lo,Q(1,2)),(hi,Q(1,2))],
    'D30':[(lo,Q(1,2)),(hi,Q(1,2)),(lo,zh),(hi,zh)],
    'S46':[(lo,zl),(hi,zl),(lo,Q(2,5)),(hi,Q(2,5))],
    'S51':[(lo,Q(2,5)),(hi,Q(2,5)),(lo,lo),(hi,hi)],
    'S69':[(lo,lo),(hi,hi),(lo,Q(1,2)),(hi,Q(1,2))],
    'S77':[(lo,Q(1,2)),(hi,Q(1,2)),(lo,zh),(hi,zh)]
}
for key,pts in cell_vertices.items():
    for b,z in pts:
        assert cost(key,b,z)==exact(key[0],b,z),(key,b,z)
    print('CELL_FOUR_VERTEX_WITNESS',key,flush=True)

assert {(r['orientation'],r['b'],r['z']) for r in cert['anchors']} == {
    (key[0],str(b),str(z)) for key,pts in cell_vertices.items() for b,z in pts
}
for i,r in enumerate(cert['anchors']):
    o,b,z=r['orientation'],Q(r['b']),Q(r['z'])
    assert exact(o,b,z)==Q(r['value']),(o,b,z,r['value'])
    print('RECORDED_BELLMAN_VERTEX_MATCH',i,o,str(b),str(z),r['value'],flush=True)
    if args.full and args.start<=i<args.stop:
        d={32:A if o=='D' else b,34:b if o=='D' else A,140:z}
        info,_=solve(d)
        assert Q(info['numerator'],info['denominator'])==Q(r['value'])
        print('UNRESTRICTED_ALL_228_BELLMAN_MATCH',i,info['states'],flush=True)

# On each convex cell, concavity and a feasible affine witness imply
# global equality for every real parameter from exact anchor equalities.
joint_cells=[
 ('D20','S46',[(lo,zl),(hi,zl),(lo,Q(2,5)),(hi,Q(2,5))]),
 ('D20','S51',[(lo,Q(2,5)),(hi,Q(2,5)),(lo,lo),(hi,hi)]),
 ('D24','S69',[(lo,lo),(hi,hi),(lo,Q(1,2)),(hi,Q(1,2))]),
 ('D30','S77',[(lo,Q(1,2)),(hi,Q(1,2)),(lo,zh),(hi,zh)])
]
gaps=[]
for d,s,pts in joint_cells:
    for b,z in pts:
        assert cost(d,b,z)==exact('D',b,z)
        assert cost(s,b,z)==exact('S',b,z)
        gaps.append((cost(d,b,z)-cost(s,b,z),(b,z),d,s))
    assert len(pts)==4
mn=min(gaps);mx=max(gaps)
assert mn[0]==Q(677,128) and mx[0]==Q(1181,80)
assert mn[1]==(hi,zl) and mx[1]==(lo,zh)
print('SHARP_GAP_MATCH',str(mn[0]),str(mx[0]),flush=True)

if args.independent:
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    for o,b,z in [('D',hi,zl),('S',hi,Q(2,5)),('D',lo,Q(1,2)),('S',lo,zh)]:
        d={32:A if o=='D' else b,34:b if o=='D' else A,140:z}
        r=certify(d)
        assert Q(r['value'])==exact(o,b,z)
        print('INDEPENDENT_RAW94_BELLMAN_MATCH',o,str(b),str(z),r['value'],flush=True)
print('EC49FTI_EXACT_CERTIFICATE_VERIFIED',flush=True)
