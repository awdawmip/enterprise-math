#!/usr/bin/env python3
"""Exact finite proof check for lattice triangles of doubled area <=3."""
from math import gcd
from itertools import combinations
import json
from pathlib import Path

def det(v,w):
    return v[0]*w[1]-v[1]*w[0]

def primitive(v):
    return gcd(abs(v[0]),abs(v[1]))==1

def canonical(v):
    return v if v>(0,0) else (-v[0],-v[1])

def enumerate_cases():
    out=[]
    for n in range(1,4):
        for d in range(1,n+1):
            if n%d: continue
            h=n//d
            for r in range(h):
                u,v=(d,0),(r,h)
                points=[]
                for x in range(max(d,r)+1):
                    for y in range(h+1):
                        # barycentric coefficients y/h and (xh-ry)/(dh)
                        if x*h-r*y>=0 and x*h-r*y+d*y<=d*h:
                            points.append((x,y))
                for source in points:
                    actual=[(x-source[0],y-source[1]) for x,y in points
                            if primitive((x-source[0],y-source[1]))]
                    direction_count=len({canonical(w) for w in actual})
                    b1=sum(abs(det(w,z))==1 for w,z in combinations(actual,2))
                    # C_1 counts ordered positive-det pairs with -w present.
                    actual_set=set(actual)
                    c1=sum(det(w,z)==1 and (-w[0],-w[1]) in actual_set
                           for w in actual for z in actual)
                    x,y=source
                    interior=int(y>0 and x*h-r*y>0 and x*h-r*y+d*y<d*h)
                    assert 1-direction_count+b1-c1-interior==0
                    if interior:
                        assert len(actual)==3
                        assert tuple(map(sum,zip(*actual)))==(0,0)
                        assert all(abs(det(w,z))==1 for w,z in combinations(actual,2))
                    out.append(dict(doubled_area=n,vertices=[(0,0),u,v],
                                    source=source,D=direction_count,B1=b1,C1=c1,
                                    interior=interior))
    return out

if __name__=='__main__':
    cases=enumerate_cases()
    result={"status":"PASS","arithmetic":"exact integers",
            "normal_form":"(0,0),(d,0),(r,h); dh in {1,2,3}; 0<=r<h",
            "case_count":len(cases),"triangle_count":len({tuple(map(tuple,c['vertices'])) for c in cases}),
            "identity":"1-D+B1-C1-interior=0", "cases":cases}
    Path(__file__).with_name('small_triangle_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
