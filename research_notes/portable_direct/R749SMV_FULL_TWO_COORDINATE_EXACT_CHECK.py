#!/usr/bin/env python3
"""Fully exact 2-parameter continuum certificate for Walsh five-circuit C."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

C=(1,2,4,8,15)
def chi(a,x): return 1-2*((a&x).bit_count()%2)

# Solve exact 6x6 with three RHS, using Fraction. Return affine (a,b,c).
def affine_solve(mat,rhs):
    n=len(mat)
    z=[[F(a) for a in row]+[F(rhs[k][i]) for k in range(3)] for i,row in enumerate(mat)]
    for j in range(n):
        k=next((k for k in range(j,n) if z[k][j]),None)
        if k is None: return None
        z[j],z[k]=z[k],z[j]
        pivot=z[j][j]
        z[j]=[e/pivot for e in z[j]]
        for k in range(n):
            if k==j: continue
            pivot=z[k][j]
            if pivot:z[k]=[a-pivot*b for a,b in zip(z[k],z[j])]
    return [tuple(z[i][-3:]) for i in range(n)]

def fval(co,p): return co[0]+co[1]*p[0]+co[2]*p[1]

def clip(poly,co):
    if not poly: return []
    ret=[]
    for i,cur in enumerate(poly):
        prev=poly[i-1]
        fc=fval(co,cur);fp=fval(co,prev)
        if (fp<0 and fc>0) or (fp>0 and fc<0):
            w=fp/(fp-fc)
            ret.append((prev[0]+w*(cur[0]-prev[0]),prev[1]+w*(cur[1]-prev[1])))
        elif fp<0 and fc==0: pass
        elif fp==0 and fc<0: pass
        if fc>=0: ret.append(cur)
    out=[]
    for p in ret:
        if not out or p!=out[-1]:out.append(p)
    if len(out)>1 and out[0]==out[-1]:out.pop()
    return out

def triangles():
    for e in (-1,1):
        for f in (-1,1):
            yield 'inner',e,f,((F(0),F(0)),(F(e),F(0)),(F(0),F(f)))
            yield 'outer',e,f,((F(e),F(0)),(F(e),F(f)),(F(0),F(f)))

def goal(kind,e,f,t,s):
    return F(3,4) if kind=='inner' else F(3,4)*(2-e*t-f*s)

def center(kind,e,f,t,s):
    z=F(0) if kind=='inner' else e*f*(e*t+f*s-1)
    return [(1+t*chi(1,x)+s*chi(2,x)+z*chi(3,x))/16 for x in range(16)]

def main():
    cols=[[1]+[chi(a,x) for a in C] for x in range(16)]
    count=Counter();seen=set()
    for inds in combinations(range(16),6):
        count['bases']+=1
        A=[[cols[j][i] for j in inds] for i in range(6)]
        sol=affine_solve(A,([1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]))
        if sol is None:continue
        count['nonsingular']+=1
        aff=[(F(0),F(0),F(0)) for x in range(16)]
        for ix,co in zip(inds,sol):aff[ix]=co
        for kind,e,f,triangle in triangles():
            poly=list(triangle)
            for co in aff:
                poly=clip(poly,co)
                if not poly:break
            if not poly:continue
            count['feasible_chamber_polygons']+=1
            for t,s in poly:
                p=[fval(co,(t,s)) for co in aff]
                assert min(p)>=0 and sum(p)==1
                for a in C:
                    req=t if a==1 else s if a==2 else 0
                    assert sum(p[x]*chi(a,x) for x in range(16))==req
                q=center(kind,e,f,t,s)
                assert min(q)>=0 and sum(q)==1
                err=sum(abs(x-y) for x,y in zip(p,q))/2
                target=goal(kind,e,f,t,s)
                assert err<=target, (kind,e,f,str(t),str(s),str(err),str(target),inds)
                count['tested_polygon_vertices']+=1
                seen.add((t,s))
    result={'schema':'R749SMV_2D_FIVE_CIRCUIT_RATIONAL_POLYGON_CERTIFICATE_V1','status':'PASS', 'arithmetic':'fractions.Fraction only', 'partition':'eight closed parameter triangles (quadrant x inner/outer diamond)', 'scope':'all real t,s in [-1,1]; m1=t,m2=s,m4=m8=m15=0', 'counts':dict(count), 'distinct_parameter_vertices':len(seen),'claimed_exact_risk':'(3/4)*min(1,2-|t|-|s|) with separate constructive lower bound'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
