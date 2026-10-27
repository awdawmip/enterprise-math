#!/usr/bin/env python3
"""Exact exhaustive C4-BRC port orbit enumerator. Integer-pair Gaussian arithmetic."""
from itertools import combinations_with_replacement, product, combinations
from math import isqrt
import json, sys, hashlib, time
Z=(0,0); ONE=(1,0); UNITS=(ONE,(-1,0),(0,1),(0,-1))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def norm(x):return x[0]*x[0]+x[1]*x[1]
def div_exact(x,y):
    d=norm(y)
    if not d:return None
    z=mul(x,conj(y))
    if z[0]%d or z[1]%d:return None
    return (z[0]//d,z[1]//d)
def dot(x,y):
    z=Z
    for a,b in zip(x,y):z=add(z,mul(conj(a),b))
    return z
def matrix_gram(M):
    cols=list(zip(*M));return [[dot(u,v) for v in cols] for u in cols]
def canonical(M):
    rows=[]
    for row in M:
        candidates=[tuple(mul(u,z) for z in row) for u in UNITS]
        rows.append(min(candidates))
    return tuple(sorted(rows))
def first_columns(n):
    options=[(a,b) for a in range(1,isqrt(n)+1) for b in range(isqrt(n)+1) if a*a+b*b<=n]
    options.append(Z)
    options.sort(key=lambda z:(norm(z),z[0],z[1]))
    return [t for t in combinations_with_replacement(options,3) if sum(norm(z) for z in t)==n]
_gauss_cache={}
def gaussian_ball(n):
    if n not in _gauss_cache:
        lim=isqrt(n)
        _gauss_cache[n]=[(a,b) for a in range(-lim,lim+1) for b in range(-lim,lim+1) if a*a+b*b<=n]
    return _gauss_cache[n]
def pair_index(u,v):
    m=[]
    for j,k in combinations(range(3),2):
        d=sub(mul(conj(u[j]),conj(v[k])),mul(conj(u[k]),conj(v[j])))
        m.append((norm(d),j,k,d))
    best=max(m,key=lambda row:row[0])
    assert best[0]>0
    return best

def enumerate_gram(G, save_representatives=True):
    n0,n1,n2=G[0][0][0],G[1][1][0],G[2][2][0]
    inner01,inner02,inner12=G[0][1],G[0][2],G[1][2]
    ucols=first_columns(n0)
    b1=gaussian_ball(n1)
    b2=gaussian_ball(n2)
    reps={}; candidate_uv=0; candidate_full=0; checked=0
    for u in ucols:
        # pivot to minimize the size of the exact search; deterministic tie
        k=max(range(3),key=lambda j:(norm(u[j]),-j))
        oth=[j for j in range(3) if j!=k]
        for x in b1:
            xnorm=norm(x)
            for y in b1:
                if xnorm+norm(y)>n1:continue
                v=[None]*3
                v[oth[0]],v[oth[1]]=x,y
                residual=sub(sub(inner01,mul(conj(u[oth[0]]),x)),mul(conj(u[oth[1]]),y))
                v[k]=div_exact(residual,conj(u[k]))
                if v[k] is None or sum(norm(z) for z in v)!=n1:continue
                candidate_uv+=1
                _,j,h,delta=pair_index(u,v)
                f=next(z for z in range(3) if z not in (j,h))
                for wf in b2:
                    if norm(wf)>n2:continue
                    ru=sub(inner02,mul(conj(u[f]),wf))
                    rv=sub(inner12,mul(conj(v[f]),wf))
                    wj=div_exact(sub(mul(ru,conj(v[h])),mul(conj(u[h]),rv)),delta)
                    if wj is None: continue
                    wh=div_exact(sub(mul(conj(u[j]),rv),mul(ru,conj(v[j]))),delta)
                    if wh is None: continue
                    w=[None]*3;w[f],w[j],w[h]=wf,wj,wh
                    if sum(norm(z) for z in w)!=n2:continue
                    M=list(zip(u,v,w))
                    candidate_full+=1
                    if matrix_gram(M)!=G:raise AssertionError('bad gram')
                    checked+=9
                    key=canonical(M)
                    if save_representatives:reps[key]=key
                    else:reps[key]=True
    row_norms={tuple(sorted(sum(norm(x) for x in row) for row in key)) for key in reps}
    return {"first_columns":len(ucols),"candidate_first_second_columns":candidate_uv,"canonical_first_column_matrices":candidate_full,"distinct_orbits":len(reps),"distinct_row_norm_multisets":len(row_norms),"gram_entries_checked":checked,"representatives":list(reps)}

def gram_for_s(s):
    H=[[3,-1,0],[-1,2,1],[0,1,3]]
    return [[(16*H[i][j]-(s[i] if i==j else 0),0) for j in range(3)] for i in range(3)]
if __name__=='__main__':
    for name,s in [('S3',None),('S4',(1,0,2)),('S7',(2,0,1))]:
        if sys.argv[1:] and name not in sys.argv[1:]:continue
        if name=='S3':G=[[(47,0),(-16,0),(1,0)],[(-16,0),(32,0),(16,0)],[(1,0),(16,0),(47,0)]]
        else:G=gram_for_s(s)
        start=time.monotonic();R=enumerate_gram(G)
        print(name,{k:v for k,v in R.items() if k!='representatives'},'seconds',round(time.monotonic()-start,3),flush=True)
        out={"case":name,"G":G,"summary":{k:v for k,v in R.items() if k!='representatives'},"representatives":R['representatives']}
        p=f'/mnt/data/prefix299_{name}.json';open(p,'w').write(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
        print(p,'sha256',hashlib.sha256(open(p,'rb').read()).hexdigest(),flush=True)
