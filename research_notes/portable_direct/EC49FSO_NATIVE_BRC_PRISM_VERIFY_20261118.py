#!/usr/bin/env python3
"""EC49FSO exact prism certificate checker.
    
Default: exact rational certificate and sharp-crossing arithmetic.
With --bundle DIR: use source-native original data and lossless named trees.
With --vertex N: additionally run unrestricted 228-observer Bellman for one
of the 16 cases; --independent also invokes separately decoded native oracle.
Bundled parent source: EC49FSN full-evidence archive; no external network.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--bundle',type=Path,default=None)
p.add_argument('--vertex',type=int,default=None)
p.add_argument('--independent',action='store_true')
a=p.parse_args()
cert=json.loads(Path(__file__).with_name(
    'EC49FSO_NATIVE_BRC_PRISM_MACHINE_CERT_20261118.json').read_text())
assert cert['schema']=='EC49FSO_THREE_PRICE_NATIVE_PRISM_V1'
assert len(cert['vertices'])==16
for row in cert['vertices']:
    x,y,z=map(Q,(row['a'],row['b'],row['z']))
    k=10 if row['orientation']=='swapped' else 4
    assert Q(row['bellman_value'])==306-141*x-41*y-k*z
assert -3+9*Q(27,64)-7*Q(51,448)==0
assert -3+9*Q(27,64)-7*Q(1,8)==-Q(5,64)
print('EXACT_CERTIFICATE_ARITHMETIC_PASS',len(cert['vertices']))
if a.bundle is not None:
    root=a.bundle.resolve()
    sys.path.insert(0,str(root/'code'))
    from EC49FSA_THREE_OBSERVER_SOLVER import V, PIN, solve
    assert PIN==cert['frozen_pin'] and len(V)==228 and len(V[0])==141
    def replay(tree):
        counts=[0]*228
        for i in range(141):
            node=tree
            seen=set()
            while 'named_observer' in node:
                q=node['named_observer']
                assert q not in seen and 0<=q<228
                seen.add(q)
                counts[q]+=1
                node=node['children'][str(V[q][i])]
            assert node=={'leaf':i}
        return [sum(counts),counts[32],counts[34],counts[140]]
    for kind,filename in (
        ('direct','full_native_tree_original.json'),
        ('swapped','full_native_tree_swapped.json'),
        ('challenger','full_native_tree_challenger.json')):
        raw=(root/filename).read_text().strip()
        assert hashlib.sha256(raw.encode()).hexdigest()==cert['native_witnesses'][kind]['sha256']
        assert replay(json.loads(raw))==cert['native_witnesses'][kind]['counts']
        print('FULL_NAMED_TREE_PASS',kind)
    if a.vertex is not None:
        row=cert['vertices'][a.vertex]
        x,y,z=map(Q,(row['a'],row['b'],row['z']))
        dx,dy=(y,x) if row['orientation']=='swapped' else (x,y)
        info,_=solve({32:dx,34:dy,140:z})
        value=Q(info['numerator'],info['denominator'])
        assert value==Q(row['bellman_value'])
        print('ALL228_BELLMAN_PASS',a.vertex,str(value))
        if a.independent:
            from EC49FSA_FSB_INDEPENDENT_CHECK import certify
            independent=certify({32:dx,34:dy,140:z})
            assert Q(independent['value'])==value
            print('INDEPENDENT_NATIVE_BELLMAN_PASS',a.vertex,str(value))
elif a.vertex is not None or a.independent:
    p.error('--vertex or --independent requires --bundle')
