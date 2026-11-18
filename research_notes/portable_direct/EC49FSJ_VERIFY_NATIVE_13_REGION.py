#!/usr/bin/env python3
"""EC49FSJ exact 13-region BRC original-native certificate checker (stdlib only).

The 13 full trees and rational geometry are checked directly; --solver-dir invokes
the exhaustive 228-native-observer Bellman DP on every vertex, while
--independent-dir additionally checks the seven new interior vertices.
Supply the frozen BRC source module with V[228][141] at --native-data-dir.
"""
import argparse, base64, hashlib, json, sys, zlib
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def area(poly):
    return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2 if len(poly)>2 else F(0)

def clip(poly, A, B, C):
    def f(p): return A*p[0]+B*p[1]+C
    out=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        p,q=f(u),f(v)
        if p<=0: out.append(u)
        if p<0<q or q<0<p:
            out.append(tuple((q*x-p*y)/(q-p) for x,y in zip(u,v)))
        elif p>0 and q==0: out.append(v)
    unique=[]
    for item in out:
        if not unique or item!=unique[-1]: unique.append(item)
    if len(unique)>1 and unique[0]==unique[-1]: unique.pop()
    return unique

def price(r,a,z):
    return F(r['U'])-F(r['Q'])*a-F(r['K'])*z

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--certificate',default='EC49FSJ_EXACT_NATIVE_BRC_13_REGION_MACHINE_CERTIFICATE.json')
    ap.add_argument('--trees',default='EC49FSJ_THIRTEEN_NATIVE_TREES_JSON_ZLIB_BASE64.txt')
    ap.add_argument('--native-data-dir',required=True)
    ap.add_argument('--solver-dir')
    ap.add_argument('--independent-dir')
    args=ap.parse_args()
    cert=json.loads(Path(args.certificate).read_text())
    assert cert['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
    sys.path.insert(0,args.native_data_dir)
    from EC49FQI_NATIVE_DATA import V,PIN
    assert PIN==cert['science_pin'] and len(V)==228 and all(len(v)==141 for v in V)
    trees=json.loads(zlib.decompress(base64.b64decode(Path(args.trees).read_text().strip())))
    regions=cert['regions']
    assert len(regions)==13 and len(trees)==13
    low,high=F(3,8),F(7,16)
    box=[(low,F(0)),(high,F(0)),(high,F(1)),(low,F(1))]
    allverts=set()
    positive=0
    for r in regions:
        U,Q,K=r['U'],r['Q'],r['K']
        key=f'{U}_{Q}_{K}'
        tree=trees[key]
        encoded=json.dumps(tree,sort_keys=True,separators=(',',':')).encode()
        assert hashlib.sha256(encoded).hexdigest()==r['tree_sha256'], key
        counts=Counter()
        for state in range(141):
            node=tree;seen=set()
            while 'named_observer' in node:
                q=node['named_observer']
                assert isinstance(q,int) and 0<=q<228 and q not in seen
                seen.add(q);counts[q]+=1
                node=node['children'][str(V[q][state])]
            assert node=={'leaf':state}
        assert (sum(counts.values()),counts[32]+counts[34],counts[140])==(U,Q,K)
        poly=box[:]
        for t in regions:
            if t is r:continue
            poly=clip(poly,t['Q']-Q,t['K']-K,U-t['U'])
            if not poly:break
        a=area(poly)
        assert a==F(r['area']) and a>0,(key,a,r['area'])
        positive+=a;allverts.update(poly)
        for x,z in poly:
            assert low<=x<=high and 0<=z<=1
            assert price(r,x,z)==min(price(t,x,z) for t in regions)
    assert positive==high-low==F(cert['area_sum'])
    assert len(allverts)==25
    points={(F(p['alpha']),F(p['z'])):F(p['value']) for p in cert['vertex_bellman']}
    assert len(points)==25 and allverts==set(points)
    for (alpha,z),value in points.items():
        assert value==min(price(t,alpha,z) for t in regions)
    alpha=F(7,16)
    slice_cert=cert['alpha_7_16_slice']
    assert len(slice_cert)==8 and slice_cert[0]['z'][0]=='0' and slice_cert[-1]['z'][1]=='1'
    for i,seg in enumerate(slice_cert):
        lo,hi=map(F,seg['z'])
        assert lo<hi and (i==0 or slice_cert[i-1]['z'][1]==seg['z'][0])
        U,Q,K=seg['plane'];mid=(lo+hi)/2
        assert F(U)-Q*alpha-K*mid==min(price(t,alpha,mid) for t in regions)
    print('PASS: 13 complete trees x 141 profiles; 228 named observers; 25 rational vertices; total area 1/16; 8 exact 7/16 phases',flush=True)
    if args.solver_dir:
        sys.path.insert(0,args.solver_dir)
        from EC49FSA_THREE_OBSERVER_SOLVER import solve
        for (alpha,z),target in points.items():
            info,_=solve({32:alpha,34:alpha,140:z})
            assert F(info['numerator'],info['denominator'])==target,(alpha,z,target,info)
            print('PRIMARY BELLMAN',alpha,z,target,flush=True)
    if args.independent_dir:
        sys.path.insert(0,args.independent_dir)
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for pt in cert['independent_checks']['interior_points']:
            a,z=F(pt['alpha']),F(pt['z'])
            res=certify({32:a,34:a,140:z})
            assert F(res['value'])==F(pt['value'])
            print('INDEPENDENT',a,z,pt['value'],flush=True)
    print('EC49FSJ exact finite certificate verification complete; human independent mathematical review pending')

if __name__=='__main__':
    main()
