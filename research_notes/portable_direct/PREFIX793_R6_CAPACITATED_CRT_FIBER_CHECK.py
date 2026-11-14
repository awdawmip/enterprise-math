"""PREFIX-793: exact integer checks for a capacitated 2 x b x c CRT fiber.
Python 3.9+ standard library only; deterministic and no external network.
"""
from itertools import product
from collections import defaultdict
from functools import lru_cache
import json

def maximum_flow(capacity, source, sink):
    residual = defaultdict(int)
    for (u,v), cap in capacity.items():
        assert cap >= 0
        residual[u,v] += cap
        residual[v,u] += 0
    total = 0
    while True:
        parent = {source:None}
        queue = [source]
        for u in queue:
            for (a,b), cap in list(residual.items()):
                if a == u and cap > 0 and b not in parent:
                    parent[b] = u
                    queue.append(b)
            if sink in parent: break
        if sink not in parent: return total
        cur = sink
        delta = None
        while parent[cur] is not None:
            pre = parent[cur]
            w = residual[pre,cur]
            delta = w if delta is None else min(delta,w)
            cur = pre
        assert delta is not None and delta > 0
        cur = sink
        while parent[cur] is not None:
            pre = parent[cur]
            residual[pre,cur] -= delta
            residual[cur,pre] += delta
            cur = pre
        total += delta

def hall_feasible(R,r,s):
    B,C = len(R),len(R[0])
    if sum(r) != sum(s) or min(r+s) < 0: return False
    for mask in range(1<<B):
        S = [i for i in range(B) if (mask>>i)&1]
        if sum(r[i] for i in S) > sum(min(s[j],sum(R[i][j] for i in S)) for j in range(C)):
            return False
    return True

def source_flow_feasible(R,r,s):
    B,C = len(R),len(R[0])
    cap = {}
    for i in range(B):
        cap['src',('b',i)] = r[i]
        for j in range(C): cap[('b',i),('c',j)] = R[i][j]
    for j in range(C): cap[('c',j),'sink'] = s[j]
    return sum(r)==sum(s) and maximum_flow(cap,'src','sink')==sum(r)

def residual_endpoints(R,x,i,j):
    B,C = len(R),len(R[0])
    arcs = {}
    for b in range(B):
        for c in range(C):
            if (b,c)==(i,j): continue
            arcs[('b',b),('c',c)] = R[b][c]-x[b][c]
            arcs[('c',c),('b',b)] = x[b][c]
    up=min(R[i][j]-x[i][j],maximum_flow(arcs,('c',j),('b',i)))
    down=min(x[i][j],maximum_flow(arcs,('b',i),('c',j)))
    return x[i][j]-down,x[i][j]+up

def enumerate_matrices(R):
    B,C = len(R),len(R[0])
    for flat in product(*(range(R[i][j]+1) for i in range(B) for j in range(C))):
        x=tuple(tuple(flat[i*C+j] for j in range(C)) for i in range(B))
        r=tuple(sum(x[i]) for i in range(B))
        s=tuple(sum(x[i][j] for i in range(B)) for j in range(C))
        yield x,r,s

def regression(B,C,levels):
    cases=feasible=infeasible=endpoints=max_fiber=0
    for flat in product(levels,repeat=B*C):
        R=tuple(tuple(flat[i*C+j] for j in range(C)) for i in range(B))
        observed=defaultdict(list)
        for x,r,s in enumerate_matrices(R): observed[r,s].append(x)
        rc=[sum(row) for row in R]
        cc=[sum(R[i][j] for i in range(B)) for j in range(C)]
        for r in product(*(range(t+1) for t in rc)):
            for s in product(*(range(t+1) for t in cc)):
                if sum(r)!=sum(s): continue
                cases+=1
                ww=observed.get((r,s),[])
                h=hall_feasible(R,r,s)
                f=source_flow_feasible(R,r,s)
                assert h==f==bool(ww),(R,r,s,h,f)
                if not ww:
                    infeasible+=1
                    continue
                feasible+=1
                max_fiber=max(max_fiber,len(ww))
                for i in range(B):
                    for j in range(C):
                        lo,hi=residual_endpoints(R,ww[0],i,j)
                        actual=sorted({w[i][j] for w in ww})
                        assert actual==list(range(lo,hi+1)),(R,r,s,i,j,actual,lo,hi)
                        endpoints+=1
    return dict(shape=[B,C],capacity_alphabet=list(levels),margin_cases=cases,
                feasible=feasible,infeasible=infeasible,target_cell_interval_checks=endpoints,
                max_fiber_count=max_fiber)

def uniform_count():
    rows=[a for a in product(range(3),repeat=5) if sum(a)==5]
    @lru_cache(None)
    def dp(b,col):
        if b==3: return int(col==(3,)*5)
        return sum(dp(b+1,tuple(col[j]+a[j] for j in range(5)))
                   for a in rows if all(col[j]+a[j]<=3 for j in range(5)))
    via_rows=dp(0,(0,)*5)
    cols=[v for v in product(range(3),repeat=3) if sum(v)==3]
    via_cols=sum(1 for items in product(cols,repeat=5)
                 if all(sum(items[j][i] for j in range(5))==5 for i in range(3)))
    assert via_rows==via_cols==991
    return len(rows),via_rows,len(cols)

def main():
    a=regression(2,2,(0,1,2))
    b=regression(2,3,(0,1))
    R=((2,)*5,)*3
    x=((1,)*5,)*3
    assert all(residual_endpoints(R,x,i,j)==(0,2)
               for i in range(3) for j in range(5))
    rows,count,cols=uniform_count()
    badR=((1,0),(0,1)); badr=(1,0); bads=(0,1)
    assert sum(badr)==sum(bads) and not hall_feasible(badR,badr,bads)
    res={'status':'ALL_CHECKS_PASS PREFIX793 CAPACITATED_CRT_MAXFLOW_FIBER',
         'tests':[a,b],
         'two_by_three_by_five':{'R_all':2,'row0_sums':[5]*3,'col0_sums':[3]*5,
             'base_x_all':1,'each_cell_sharp_interval':[0,2],
             'independent_real_residual_dimension':8,'row_patterns':rows,
             'column_patterns':cols,'integer_fiber_size':count},
         'counterexample':{'R':badR,'row0':badr,'col0':bads,'feasible':False}}
    print(json.dumps(res,indent=2,sort_keys=True))
    print(res['status'])
    return res

if __name__=='__main__': main()
