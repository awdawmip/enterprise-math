#!/usr/bin/env python3
"""EC49FTF finite certificate verifier. Uses the self-contained evidence archive root.

Usage:
 python EC49FTF_NATIVE_BRC_LOWER_SATURATION_FAN_VERIFY_20261119.py --evidence-root DIR
 python ...py --evidence-root DIR --full --anchor-start 0 --anchor-stop 12
 python ...py --evidence-root DIR --full --independent --anchor-start 12 --anchor-stop 23

The --full mode runs unrestricted original-index 228-observer exact Bellman.
"""
import argparse
import gc
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def vertices(c):
    out=set()
    for r in itertools.combinations(c,3):
        a=[[Q(v) for v in x[1:]] for x in r]
        d=det(a)
        if d==0: continue
        b=[-Q(x[0]) for x in r]
        p=tuple(det([[b[i] if j==k else a[i][j] for j in range(3)]
                       for i in range(3)])/d for k in range(3))
        if all(Q(x[0])+sum(Q(x[j+1])*p[j] for j in range(3))>=0 for x in c):
            out.add(p)
    return sorted(out)

def proof_geometry(cert):
    bounds=[tuple(map(Q,cert['domain'][n])) for n in ('a','b','z')]
    (a0,a1),(b0,b1),(z0,z1)=bounds
    box=[(-a0,1,0,0),(a1,-1,0,0),(-b0,0,1,0),
         (b1,0,-1,0),(-z0,0,0,1),(z1,0,0,-1)]
    dc={'Dmid':(Q(4),-4,-2,0),'Dhi':(Q(-4),4,2,0)}
    sc={'Smain':(Q(7),-36,1,26),'T115':(Q(-7),36,-1,-26)}
    co={'Dmid':(Q(329),-36,-68,-141),
        'Dhi':(Q(333),-40,-70,-141),
        'Smain':(Q(333),-105,-9,-141),
        'T115':(Q(340),-141,-8,-115)}
    def cost(name,p):return co[name][0]+sum(co[name][i+1]*p[i] for i in range(3))
    anchor_key={(r['orientation'],r['a'],r['b'],r['z']) for r in cert['bellman_anchors']}
    assert len(anchor_key)==23
    for orient,regions in [('D',dc),('S',sc)]:
        pts=set()
        for name,h in regions.items():
            v=vertices(box+[h])
            assert len(v)==cert['cell_vertices'][name]
            pts.update(v)
        known={(Q(r['a']),Q(r['b']),Q(r['z'])) for r in cert['bellman_anchors'] if r['orientation']==orient}
        assert pts==known
        for r in cert['bellman_anchors']:
            if r['orientation']!=orient:continue
            p=(Q(r['a']),Q(r['b']),Q(r['z']))
            assert Q(r['optimum'])==min(cost(name,p) for name in regions)
    gaps=[]
    joint={}
    for d,hd in dc.items():
        for s,hs in sc.items():
            v=vertices(box+[hd,hs])
            joint[d,s]=len(v)
            gaps.extend((cost(d,p)-cost(s,p),p) for p in v)
    assert joint=={('Dmid','Smain'):8,('Dmid','T115'):0,
                   ('Dhi','Smain'):9,('Dhi','T115'):6}
    assert min(v for v,p in gaps)==Q(cert['gap_min']['value'])==Q(2749,128)
    assert max(v for v,p in gaps)==Q(cert['gap_max']['value'])==Q(511,20)
    print('GEOMETRY_PASS 23_ANCHORS 3_NONEMPTY_JOINT_CELLS 2749/128 511/20',flush=True)

def run():
    p=argparse.ArgumentParser()
    p.add_argument('--evidence-root',required=True)
    p.add_argument('--full',action='store_true')
    p.add_argument('--independent',action='store_true')
    p.add_argument('--anchor-start',type=int,default=0)
    p.add_argument('--anchor-stop',type=int,default=None)
    a=p.parse_args()
    root=Path(a.evidence_root).resolve()
    cert=json.loads((Path(__file__).with_name('EC49FTF_NATIVE_BRC_LOWER_SATURATION_FAN_CERT_20261119.json')).read_text())
    proof_geometry(cert)
    sys.path.insert(0,str(root))
    sys.path.insert(0,str(root/'native_code'))
    from VERIFY import check_inputs,check_trees
    outcomes=check_inputs()
    check_trees(outcomes)
    if a.full:
        from EC49FSA_THREE_OBSERVER_SOLVER import solve
        for r in cert['bellman_anchors'][a.anchor_start:a.anchor_stop]:
            q32,q34,q140=map(Q,(r['a'],r['b'],r['z']))
            ds={32:q32,34:q34,140:q140} if r['orientation']=='D' else {32:q34,34:q32,140:q140}
            info,_=solve(ds,return_tree=False)
            assert Q(info['numerator'],info['denominator'])==Q(r['optimum'])
            print('PRIMARY_PASS',r['orientation'],r['a'],r['b'],r['z'],r['optimum'],flush=True)
            del info
            gc.collect()
    if a.independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for r in cert['independent_checks']:
            aa,bb,zz=map(Q,(r['a'],r['b'],r['z']))
            ans=certify({32:bb,34:aa,140:zz})
            assert Q(ans['value'])==Q(r['value'])
            print('INDEPENDENT_RAW94_PASS',r['a'],r['b'],r['z'],r['value'],flush=True)
    print('EC49FTF_VERIFICATION_COMPLETE',flush=True)

if __name__=='__main__':
    run()
