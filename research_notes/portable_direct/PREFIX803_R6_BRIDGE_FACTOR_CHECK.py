#!/usr/bin/env python3
"""PREFIX-803 independent exact integer verifier (Python stdlib only)."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
import json

SHAPES=((2,2,2),(2,3,2),(3,3,1))

def weight(i,j):
    return ((i+2*j)%5-2, (2*i-j+9)%5-2)

def addpoly(out, child, delta):
    for (a,b),n in child.items():
        key=(a+delta[0],b+delta[1]);out[key]=out.get(key,0)+n

def multiply(A,B):
    C={}
    for (a,b),m in A.items():
        for (c,d),n in B.items():
            key=(a+c,b+d);C[key]=C.get(key,0)+m*n
    return C

def table_fibers(b,c,K,observer=None):
    """Independent full Cartesian product enumeration; not the bridge algorithm."""
    groups={}; r=[0]*b;s=[0]*c
    wt=observer if observer is not None else weight
    def rec(k,a,beta):
        if k==len(K):
            key=(tuple(r),tuple(s)); f=groups.setdefault(key,{})
            f[(a,beta)]=f.get((a,beta),0)+1
            return
        i,j=divmod(k,c);u,v=wt(i,j)
        for t in range(K[k]+1):
            r[i]+=t;s[j]+=t
            rec(k+1,a+u*t,beta+v*t)
            r[i]-=t;s[j]-=t
    rec(0,0,0)
    return groups

def solve_bridge(b,c,K,r,s,observer=None):
    E=b*c;edges=[k for k,v in enumerate(K) if v>0]
    wt=observer if observer is not None else weight
    allmask=sum(1<<k for k in edges)
    stats={'memo_states':0,'branch_nodes':0,'bridge_forces':0,'factorizations':0,'candidate_edges':0}
    @lru_cache(None)
    def graph(mask):
        adj=[set() for _ in range(b+c)]
        for e in edges:
            if (mask>>e)&1:
                i,j=divmod(e,c)
                adj[i].add(b+j);adj[b+j].add(i)
        components=[];seen=set()
        for v in range(b+c):
            if v in seen:continue
            stack=[v];seen.add(v);C=set()
            while stack:
                a=stack.pop();C.add(a)
                for z in adj[a]:
                    if z not in seen:seen.add(z);stack.append(z)
            components.append(C)
        return adj,components
    @lru_cache(None)
    def rec(mask,R,S):
        stats['memo_states']+=1
        if min(R+S)<0 or sum(R)!=sum(S):return {}
        if not mask:return {(0,0):1} if all(x==0 for x in R+S) else {}
        adj,components=graph(mask)
        for C in components:
            if not any((mask>>e)&1 and (e//c in C) for e in edges):
                if any(R[i] for i in C if i<b) or any(S[j-b] for j in C if j>=b):return {}
        # Every bridge has a cut-forced integer, before any free branching.
        for e in edges:
            if not (mask>>e)&1:continue
            i,j=divmod(e,c); v=b+j
            # component reachable from row endpoint after removing e
            stack=[i]; reached={i}
            while stack:
                p=stack.pop()
                for n in adj[p]:
                    if (p==i and n==v) or (p==v and n==i):continue
                    if n not in reached:reached.add(n);stack.append(n)
            if v in reached:continue
            t=sum(R[a] for a in reached if a<b)-sum(S[a-b] for a in reached if a>=b)
            stats['bridge_forces']+=1
            if t<0 or t>K[e] or t>R[i] or t>S[j]:return {}
            nr=list(R);ns=list(S);nr[i]-=t;ns[j]-=t
            child=rec(mask ^ (1<<e),tuple(nr),tuple(ns)); out={}
            u,w=wt(i,j);addpoly(out,child,(t*u,t*w));return out
        # A disconnected cyclic suffix factorizes exactly.
        nonempty=[]
        for C in components:
            submask=sum(1<<e for e in edges if ((mask>>e)&1) and (e//c in C))
            if submask:nonempty.append((C,submask))
        if len(nonempty)>1:
            stats['factorizations']+=1
            ans={(0,0):1}
            for C,submask in nonempty:
                nr=tuple(R[i] if i in C else 0 for i in range(b))
                ns=tuple(S[j] if b+j in C else 0 for j in range(c))
                if sum(nr)!=sum(ns):return {}
                ans=multiply(ans,rec(submask,nr,ns))
                if not ans:return {}
            return ans
        stats['branch_nodes']+=1
        e=next(e for e in edges if (mask>>e)&1)
        i,j=divmod(e,c);u,v=wt(i,j)
        out={}
        for t in range(min(K[e],R[i],S[j])+1):
            stats['candidate_edges']+=1
            nr=list(R);ns=list(S);nr[i]-=t;ns[j]-=t
            addpoly(out,rec(mask ^ (1<<e),tuple(nr),tuple(ns)),(t*u,t*v))
        return out
    value=rec(allmask,tuple(r),tuple(s))
    return value,stats

def check():
    report={'schema':'PREFIX803_EXACT_BRIDGE_FACTOR_VERIFICATION_V1', 'arithmetic':'Python arbitrary-precision integers, exact dictionary Laurent histograms', 'shapes':[], 'checks':0}
    total_patterns=total_fibers=total_tables=total_bridges=total_branches=0
    for b,c,capmax in SHAPES:
        N=b*c; n_patterns=n_fibers=n_tables=n_checks=n_bridges=n_branches=0
        for K in product(range(capmax+1),repeat=N):
            n_patterns+=1
            fibers=table_fibers(b,c,K)
            for (r,s),expected in fibers.items():
                out,stats=solve_bridge(b,c,K,r,s)
                assert out==expected, ('hist',b,c,K,r,s,out,expected)
                assert sum(out.values())==sum(expected.values()), ('count',b,c,K,r,s)
                n_checks+=2;n_fibers+=1;n_tables+=sum(expected.values())
                n_bridges+=stats['bridge_forces'];n_branches+=stats['branch_nodes']
        report['shapes'].append({'b':b,'c':c,'capacity_max':capmax,'patterns':n_patterns,'fibers':n_fibers,'tables':n_tables,'checks':n_checks,'bridge_force_events':n_bridges,'unforced_branch_nodes':n_branches})
        total_patterns+=n_patterns;total_fibers+=n_fibers;total_tables+=n_tables
        total_bridges+=n_bridges;total_branches+=n_branches
    b=c=4;K=[0]*16
    for i in (0,1):
        for j in (0,1):K[i*4+j]=1
    for i in (2,3):
        for j in (2,3):K[i*4+j]=1
    K[1*4+2]=1
    r=(1,2,1,1);s=(1,1,2,1)
    def linked_weights(i,j):
        if (i,j)==(0,0):return (1,0)
        if (i,j)==(2,2):return (0,1)
        if (i,j)==(1,2):return (-2,3)
        return (0,0)
    hist,stats=solve_bridge(4,4,K,r,s,linked_weights)
    brute=table_fibers(4,4,K,linked_weights)[(r,s)]
    assert hist==brute and sum(hist.values())==4,('double_block',hist,brute)
    assert stats['bridge_forces']>0 and stats['factorizations']>0,('bridge_factor',stats)
    bad_r=(0,2,1,1); bad_s=(0,0,2,2)
    bad,bstats=solve_bridge(4,4,K,bad_r,bad_s,linked_weights)
    assert not bad,('overflow',bad)
    report['checks']=sum(z['checks'] for z in report['shapes'])+4
    report['totals']={'patterns':total_patterns,'fibers':total_fibers,'tables':total_tables,'bridge_force_events':total_bridges,'unforced_branch_nodes':total_branches}
    report['linked_squares']={'edge_capacities':K,'row_margins':r,'col_margins':s,'table_count':sum(hist.values()),'weights':{'(0,0)':(1,0),'(2,2)':(0,1),'(1,2)':(-2,3)},'histogram':[{'exponent':list(k),'multiplicity':v} for k,v in sorted(hist.items())], 'stats':stats, 'overflow_margins':{'row':bad_r,'col':bad_s,'feasible':False,'stats':bstats}}
    report['result']='ALL_CHECKS_PASS PREFIX803 BRIDGE_FORCED_LAURENT_FACTORIZATION'
    return report

if __name__=='__main__':
    result=check()
    print(json.dumps(result,ensure_ascii=False,indent=2))
