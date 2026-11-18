#!/usr/bin/env python3
"""EC49FTG exact-native 3D price-fan verifier.

Place this file beside EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_CERT_20261119.json;
extract the separately supplied source/tree/code archive and run:
 python EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_VERIFY_20261119.py --evidence-root ROOT
 python EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_VERIFY_20261119.py --evidence-root ROOT --full --start 0 --stop 12
 python EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_VERIFY_20261119.py --evidence-root ROOT --full --start 12 --stop 18
 python EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_VERIFY_20261119.py --evidence-root ROOT --full --start 18 --stop 24 --independent

--full invokes unrestricted exact Bellman on each rational vertex in an isolated
process, allowing bounded batches. The independent raw94 check is separate.
"""
from fractions import Fraction as Q
from itertools import combinations
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pathlib import Path
from hashlib import sha256
import argparse, json, subprocess, sys

CERT_NAME = "EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_CERT_20261119.json"

def det(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
          - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
          + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def verts(constraints):
    found=set()
    for r in combinations(constraints, 3):
        matrix=[[Q(v) for v in x[1:]] for x in r]
        denominator=det(matrix)
        if denominator==0: continue
        rhs=[-Q(x[0]) for x in r]
        p=tuple(det([[rhs[i] if j==k else matrix[i][j] for j in range(3)]
                     for i in range(3)])/denominator for k in range(3))
        if all(Q(h[0])+sum(Q(h[j+1])*p[j] for j in range(3))>=0
               for h in constraints):
            found.add(p)
    return sorted(found)

def geometry(cert):
    (a0,a1),(b0,b1),(z0,z1)=[tuple(map(Q,cert['domain'][k]))
                                for k in ('a','b','z')]
    box=[(-a0,1,0,0),(a1,-1,0,0),(-b0,0,1,0),(b1,0,-1,0),
         (-z0,0,0,1),(z1,0,0,-1)]
    direct={'Dmid':(5,-105,6,96),'D45':(-5,105,-6,-96)}
    swapped={'Smain':(-1,-36,1,36),'S105':(1,36,-1,-36)}
    def cost(name,p):
        u,n32,n34,n140=cert['original_index_tree_usage'][name]
        a,b,z=p
        return (Q(u)-n32*a-n34*b-n140*z if name.startswith('D') else
                Q(u)-n34*a-n32*b-n140*z)
    expected={(r['o'],Q(r['a']),Q(r['b']),Q(r['z'])):Q(r['expected'])
              for r in cert['anchors']}
    assert len(expected)==len(cert['anchors'])==24
    actual=set()
    for orientation,parts in (('D',direct),('S',swapped)):
        for name,halfspace in parts.items():
            vertices=verts(box+[halfspace])
            assert len(vertices)==cert['region_vertex_counts'][name]
            for p in vertices:
                actual.add((orientation,*p))
                assert cost(name,p)==min(cost(k,p) for k in parts)
    assert actual==set(expected)
    for (orientation,a,b,z),value in expected.items():
        names=direct if orientation=='D' else swapped
        assert min(cost(k,(a,b,z)) for k in names)==value
    gap_vertices=[]
    for dn,dh in direct.items():
        for sn,sh in swapped.items():
            vv=verts(box+[dh,sh])
            assert len(vv)==cert['joint_vertex_counts'][dn+':'+sn]
            gap_vertices.extend((cost(dn,p)-cost(sn,p),p) for p in vv)
    assert min(x[0] for x in gap_vertices)==Q(cert['gap_min']['value'])
    assert max(x[0] for x in gap_vertices)==Q(cert['gap_max']['value'])
    for key in ('gap_min','gap_max'):
        p=tuple(map(Q,cert[key]['attained_at']))
        g=min(cost(k,p) for k in direct)-min(cost(k,p) for k in swapped)
        assert g==Q(cert[key]['value'])
    print('EXACT_GEOMETRY_PASS 24_ANCHORS 3_NONEMPTY_JOINT_CELLS')

def source_and_trees(cert,root):
    for name,h in cert['source_sha256'].items():
        assert sha256((root/'source'/name).read_bytes()).hexdigest()==h
    sys.path.insert(0,str(root/'native_code'))
    from EC49FSA_THREE_OBSERVER_SOLVER import V,PIN
    assert PIN==cert['frozen_scientific_source'].split('@')[-1]
    assert len(V)==228 and all(len(v)==141 for v in V)
    for name,expected in cert['original_index_tree_usage'].items():
        f=root/'trees'/(name+'.json')
        assert sha256(f.read_bytes()).hexdigest()==cert['tree_sha256'][name]
        tree=json.loads(f.read_text());ct=Counter()
        for profile in range(141):
            n=tree;seen=set()
            while 'named_observer' in n:
                q=n['named_observer']
                assert 0<=q<228 and q not in seen
                seen.add(q);ct[q]+=1
                n=n['children'][str(V[q][profile])]
            assert n=={'leaf':profile}
        vector=[sum(ct.values()),ct[32],ct[34],ct[140]]
        assert vector==expected,(name,vector,expected)
        print('NATIVE_IDENTIFYING_TREE_PASS',name,vector)

def full_recalculate(cert,root,start,stop,workers):
    script=root/'native_code'/'EC49FSA_THREE_OBSERVER_SOLVER.py'
    def one(entry):
        i,r=entry;a,b,z=r['a'],r['b'],r['z']
        aa,bb=(a,b) if r['o']=='D' else (b,a)
        args=[sys.executable,str(script),'--a',aa,'--b',bb,'--z',z]
        output=subprocess.run(args,capture_output=True,text=True,
                              timeout=90,check=True)
        result=json.loads(output.stdout)
        assert Q(result['numerator'],result['denominator'])==Q(r['expected'])
        return i,r
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for i,r in ex.map(one,list(enumerate(cert['anchors']))[start:stop]):
            print('UNRESTRICTED_228_BELLMAN_PASS',i,r['o'],r['a'],r['b'],
                  r['z'],r['expected'],flush=True)

def independent(cert,root):
    sys.path.insert(0,str(root/'native_code'))
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    for r in cert['independent_raw94']:
        a,b,z=Q(r['a']),Q(r['b']),Q(r['z'])
        discounts={32:a,34:b,140:z} if r['o']=='D' else {32:b,34:a,140:z}
        ans=certify(discounts)
        assert Q(ans['value'])==Q(r['value'])
        print('INDEPENDENT_RAW94_PASS',r['o'],r['a'],r['b'],
              r['z'],r['value'])

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--evidence-root',required=True)
    ap.add_argument('--full',action='store_true')
    ap.add_argument('--independent',action='store_true')
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int,default=24)
    ap.add_argument('--workers',type=int,default=3)
    args=ap.parse_args()
    cert=json.loads(Path(__file__).with_name(CERT_NAME).read_text())
    root=Path(args.evidence_root).resolve()
    geometry(cert)
    source_and_trees(cert,root)
    if args.full:full_recalculate(cert,root,args.start,args.stop,args.workers)
    if args.independent:independent(cert,root)
    print('EC49FTG_CERTIFICATE_VERIFIED',flush=True)
