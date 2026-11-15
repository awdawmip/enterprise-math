"""PREFIX-801: exact incremental Hall-slack certificate for named bounded source-count fibers.
Run: python PREFIX801_R6_INCREMENTAL_HALL_CHECK.py [--quick]
Python 3 standard library. Timing is diagnostic, not a platform-independent theorem.
"""
from collections import Counter
from itertools import product
from time import perf_counter_ns
import json, sys

def forest(K):
    b,c=len(K),len(K[0]);p=list(range(b+c)); T=[];C=[]
    def root(v):
        while p[v]!=v:v=p[v]
        return v
    edges=sorted(((i,j) for i in range(b) for j in range(c) if K[i][j]),key=lambda e:(-K[e[0]][e[1]],e))
    for i,j in edges:
        a,d=root(i),root(b+j)
        if a==d:C.append((i,j))
        else:p[a]=d;T.append((i,j))
    return T,C

def margin_fibers(K):
    b,c=len(K),len(K[0]);seen=set()
    for x in product(*(range(v+1) for row in K for v in row)):
        seen.add((tuple(sum(x[i*c+j] for j in range(c)) for i in range(b)),
                  tuple(sum(x[i*c+j] for i in range(b)) for j in range(c))))
    return sorted(seen)

def leaf(K,r,s,T,C,values):
    b,c=len(K),len(K[0]);R=list(r);S=list(s);x=[0]*(b*c);E=set(T)
    for (i,j),v in zip(C,values):R[i]-=v;S[j]-=v;x[i*c+j]=v
    if min(R+S)<0:return None
    while E:
        deg=Counter(v for i,j in E for v in (i,b+j))
        i,j=min((i,j) for i,j in E if deg[i]==1 or deg[b+j]==1)
        v=R[i] if deg[i]==1 else S[j]
        if not 0<=v<=K[i][j]:return None
        R[i]-=v;S[j]-=v;x[i*c+j]=v;E.remove((i,j))
    return tuple(x) if not any(R+S) else None

def hall_recompute(K,r,s,fixed):
    b,c=len(K),len(K[0]);R=list(r);S=list(s)
    for (i,j),v in fixed.items():R[i]-=v;S[j]-=v
    if min(R+S)<0 or sum(R)!=sum(S):return False
    for A in range(1,1<<b):
        d=sum(R[i] for i in range(b) if A>>i&1)
        u=sum(min(S[j],sum(K[i][j] for i in range(b) if A>>i&1 and (i,j) not in fixed)) for j in range(c))
        if d>u:return False
    return True

class IncrementalHall:
    """Maintains exact H_A slacks; O(2^b) per edge assignment or rollback."""
    def __init__(self,K,r,s):
        self.K=K;self.b=len(K);self.c=len(K[0]);self.R=list(r);self.S=list(s)
        self.masks=list(range(1,1<<self.b))
        self.C=[[sum(K[i][j] for i in range(self.b) if A>>i&1) for j in range(self.c)] for A in self.masks]
        self.D=[sum(r[i] for i in range(self.b) if A>>i&1) for A in self.masks]
        self.slack=[sum(min(s[j],self.C[k][j]) for j in range(self.c))-self.D[k] for k in range(len(self.masks))]
        self.stack=[]

    def feasible(self):
        return min(self.R)>=0 and min(self.S)>=0 and min(self.slack)>=0

    def push(self,i,j,t):
        k=self.K[i][j];s=self.S[j];deltas=[]
        for a,A in enumerate(self.masks):
            hit=bool((A>>i)&1); old=self.C[a][j]
            delta=min(s-t,old-(k if hit else 0))-min(s,old)+(t if hit else 0)
            self.slack[a]+=delta
            if hit:self.C[a][j]-=k;self.D[a]-=t
            deltas.append(delta)
        self.R[i]-=t;self.S[j]-=t
        self.stack.append((i,j,t,deltas))

    def pop(self):
        i,j,t,deltas=self.stack.pop();k=self.K[i][j]
        self.R[i]+=t;self.S[j]+=t
        for a,A in enumerate(self.masks):
            self.slack[a]-=deltas[a]
            if (A>>i)&1:self.C[a][j]+=k;self.D[a]+=t

def histogram(tables,b,c):
    q=Counter()
    for x in tables:
        a=sum(x[i*c+j]*(i+1)*(j+2) for i in range(b) for j in range(c))
        d=sum(x[i*c+j]*(-1)**(i+j)*(i+2*j+1) for i in range(b) for j in range(c))
        q[(a,d)]+=1
    return q

def enumerate_fiber(K,r,s,T,C,mode,stats):
    vals=[];fixed={};inc=IncrementalHall(K,r,s) if mode=='incremental' else None
    def walk(depth):
        stats['nodes']+=1
        if mode=='recompute':ok=hall_recompute(K,r,s,fixed)
        elif mode=='incremental':ok=inc.feasible()
        else:ok=True
        if not ok:stats['prunes']+=1;return
        if depth==len(C):
            stats['leaves']+=1
            x=leaf(K,r,s,T,C,vals)
            if x is not None:yield x
            return
        i,j=C[depth]
        for t in range(K[i][j]+1):
            fixed[i,j]=t;vals.append(t)
            if inc:inc.push(i,j,t)
            yield from walk(depth+1)
            if inc:inc.pop()
            vals.pop();del fixed[i,j]
    return sorted(walk(0))

def main():
    quick='--quick' in sys.argv
    families=[(2,3,(0,1,2)),(3,3,(0,1)),(2,4,(1,))]
    if quick: families=[(2,3,(0,1))]
    full=Counter();rows=[];timing={m:0 for m in ('recompute','incremental')}
    for b,c,vals in families:
        stats=Counter();case=0
        for flat in product(vals,repeat=b*c):
            K=[flat[i*c:(i+1)*c] for i in range(b)];T,C=forest(K)
            for r,s in margin_fibers(K):
                case+=1;compared={}
                for mode in ('recompute','incremental'):
                    local=Counter();start=perf_counter_ns()
                    tbl=enumerate_fiber(K,r,s,T,C,mode,local)
                    timing[mode]+=perf_counter_ns()-start
                    compared[mode]=tbl
                    for key,v in local.items():stats[mode+'_'+key]+=v
                assert compared['recompute']==compared['incremental'],(K,r,s)
                stats['comparisons']+=1;stats['tables']+=len(compared['incremental'])
                if b==2 and c==4 and K==[[1]*4,[1]*4] and r==(1,3) and s==(1,1,1,1):
                    h=IncrementalHall(K,r,s)
                    h.push(1,1,0);h.push(1,2,0)
                    assert not h.feasible()
                    assert not hall_recompute(K,r,s,{(1,1):0,(1,2):0})
                    h.pop();h.pop();assert h.feasible()
                    stats['witness_assertions']+=3
                if case%10==0:
                    assert histogram(compared['incremental'],b,c)==histogram(compared['recompute'],b,c)
                    stats['histogram_comparisons']+=1
            stats['capacities']+=1
        stats['fibers']=case;rows.append({'family':f'{b}x{c},K in {list(vals)}','stats':dict(stats)})
        full.update(stats)
    expected={'capacities':1242,'fibers':57395,'tables':66595,
              'recompute_nodes':194900,'recompute_leaves':66595,'recompute_prunes':62390}
    if not quick:
        for k,v in expected.items():assert full[k]==v,(k,full[k],v)
    assert full['incremental_nodes']==full['recompute_nodes']
    assert full['incremental_leaves']==full['recompute_leaves']
    assert full['incremental_prunes']==full['recompute_prunes']
    output={'status':'ALL_CHECKS_PASS PREFIX801 INCREMENTAL_HALL',
            'mode':'QUICK' if quick else 'FULL','families':rows,
            'total':dict(full),'timings_seconds':{k:round(v/1e9,6) for k,v in timing.items()},
            'timing_scope':'sequential within one Python process, methods called in fixed order; illustrative only',
            'verification':'both algorithms independently evaluate exact Hall predicates and reconstruct identical sorted integer tables'}
    print(json.dumps(output,indent=2,sort_keys=True))

if __name__=='__main__':main()
