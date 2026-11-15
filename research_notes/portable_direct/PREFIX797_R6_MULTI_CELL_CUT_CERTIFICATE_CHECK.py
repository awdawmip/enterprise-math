#!/usr/bin/env python3
"""PREFIX-797 exact integral transportation multi-cell projection checker.
No external packages, no floats, and no randomness.
"""
import itertools
import json


def margins(b,c,x):
    return (tuple(sum(x[i*c+j] for j in range(c)) for i in range(b)),
            tuple(sum(x[i*c+j] for i in range(b)) for j in range(c)))


def projected_feasible_by_flow(b,c,K,rows,cols,targets):
    """Whether a named target assignment extends to a feasible integer table."""
    rr=list(rows); cc=list(cols); blocked=set(targets)
    for e,t in targets.items():
        if not isinstance(t,int) or t<0 or t>K[e]: return False
        i,j=divmod(e,c);rr[i]-=t;cc[j]-=t
    if min(rr)<0 or min(cc)<0 or sum(rr)!=sum(cc):return False
    n=b+c+2; src=b+c; sink=src+1
    residual=[[0]*n for _ in range(n)]
    for i,a in enumerate(rr):residual[src][i]=a
    for j,d in enumerate(cc):residual[b+j][sink]=d
    for i in range(b):
        for j in range(c):
            e=i*c+j
            if e not in blocked: residual[i][b+j]=K[e]
    total=0
    while True:
        previous=[-1]*n;previous[src]=src;q=[src]
        for v in q:
            if previous[sink]>=0:break
            for u,cap in enumerate(residual[v]):
                if cap and previous[u]<0:
                    previous[u]=v;q.append(u)
        if previous[sink]<0:break
        v=sink; f=10**9
        while v!=src:
            u=previous[v];f=min(f,residual[u][v]);v=u
        v=sink
        while v!=src:
            u=previous[v];residual[u][v]-=f;residual[v][u]+=f;v=u
        total+=f
    return total==sum(rr)


def projected_feasible_by_cuts(b,c,K,rows,cols,targets):
    """Complete integral Hall/min-cut inequalities, with exact enumeration of cuts."""
    rr=list(rows);cc=list(cols);blocked=set(targets)
    for e,t in targets.items():
        if not isinstance(t,int) or t<0 or t>K[e]:return False
        i,j=divmod(e,c);rr[i]-=t;cc[j]-=t
    if min(rr)<0 or min(cc)<0 or sum(rr)!=sum(cc):return False
    for rowbits in range(1<<b):
        I=[i for i in range(b) if rowbits>>i&1]
        for colbits in range(1<<c):
            J=[j for j in range(c) if colbits>>j&1]
            cap=sum(K[i*c+j] for i in I for j in range(c)
                    if j not in J and i*c+j not in blocked)
            if sum(rr[i] for i in I)>sum(cc[j] for j in J)+cap:return False
    return True


def fiber(b,c,K,rows,cols):
    for x in itertools.product(*(range(k+1) for k in K)):
        if margins(b,c,x)==(rows,cols):yield x


def run(b,c,maximum,step=1):
    opts=[(k,t) for k in range(maximum+1) for t in range(k+1)]
    count=0; combos=0; checks=0; possible=0; impossible=0
    for index,v in enumerate(itertools.product(opts,repeat=b*c)):
        if index%step:continue
        K=tuple(k for k,_ in v);x=tuple(t for _,t in v)
        rows,cols=margins(b,c,x)
        all_y=list(fiber(b,c,K,rows,cols))
        for e,f in itertools.combinations(range(b*c),2):
            observed={(y[e],y[f]) for y in all_y}
            for a in range(K[e]+1):
                for d in range(K[f]+1):
                    targets={e:a,f:d}
                    actual=(a,d) in observed
                    via_flow=projected_feasible_by_flow(b,c,K,rows,cols,targets)
                    via_cuts=projected_feasible_by_cuts(b,c,K,rows,cols,targets)
                    assert actual==via_flow==via_cuts,(b,c,K,rows,cols,targets,actual,via_flow,via_cuts)
                    checks+=2;possible+=int(actual);impossible+=int(not actual)
            combos+=1
        count+=1
    return dict(grid=f'{b}x{c}',max_capacity=maximum,stride=step,states=count,
                selected_pairs=combos,paired_checks=checks,feasible_candidates=possible,
                infeasible_candidates=impossible)


def main():
    tests=[run(2,2,2),run(2,3,1),run(2,3,2,41)]
    K=(2,2,2,2);rows=(2,2);cols=(2,2)
    pair={(0,0),(1,1),(2,2)}
    fiber_observed={(y[0],y[1]) for y in fiber(2,2,K,rows,cols)}
    assert fiber_observed=={(0,2),(1,1),(2,0)}
    assert projected_feasible_by_flow(2,2,K,rows,cols,{0:0,1:0}) is False
    assert projected_feasible_by_cuts(2,2,K,rows,cols,{0:0,1:0}) is False
    assert pair != fiber_observed  # distinguish diagonal from antidiagonal
    assert {y[0] for y in fiber(2,2,K,rows,cols)}=={0,1,2}
    assert {y[1] for y in fiber(2,2,K,rows,cols)}=={0,1,2}
    result={'name':'PREFIX797_SHARP_INTEGRAL_MULTI_CELL_PROJECTION',
     'scope':'2x2 all (K,x) with 0<=x<=K<=2; 2x3 all with 0<=x<=K<=1; deterministic stride-41 of 2x3 0<=x<=K<=2',
     'arithmetic':'exact Python integers; no randomness or floating point',
     'checks':tests,'witness_assertions':6,
     'assertions_total':sum(z['paired_checks'] for z in tests)+6,
     'status':'ALL_CHECKS_PASS','predecessor':'PREFIX-796'}
    return result

if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
