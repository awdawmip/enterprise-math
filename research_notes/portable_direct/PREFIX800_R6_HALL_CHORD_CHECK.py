"""PREFIX-800: exact integer capacity-cut pruning for BRC source-count fibers.
Run: python PREFIX800_R6_HALL_CHORD_CHECK.py (stdlib only).
"""
from itertools import product
from collections import Counter
import json

def margins(K):
    b,c=len(K),len(K[0]); found=set()
    for x in product(*(range(v+1) for row in K for v in row)):
        found.add((tuple(sum(x[i*c+j] for j in range(c)) for i in range(b)),
                   tuple(sum(x[i*c+j] for i in range(b)) for j in range(c))))
    return sorted(found)

def forest(K):
    b,c=len(K),len(K[0]); p=list(range(b+c)); T=[]; C=[]
    def root(v):
        while p[v]!=v:v=p[v]
        return v
    edges=sorted(((i,j) for i in range(b) for j in range(c) if K[i][j]),
                 key=lambda e:(-K[e[0]][e[1]],e))
    for i,j in edges:
        a,d=root(i),root(b+j)
        if a==d:C.append((i,j))
        else:p[a]=d;T.append((i,j))
    return T,C

def direct(K,r,s):
    b,c=len(K),len(K[0]); left=list(s); x=[0]*(b*c)
    def walk(i):
        if i==b:
            if not any(left):yield tuple(x)
            return
        for row in product(*(range(min(K[i][j],left[j])+1) for j in range(c))):
            if sum(row)!=r[i]:continue
            for j,v in enumerate(row):x[i*c+j]=v;left[j]-=v
            yield from walk(i+1)
            for j,v in enumerate(row):left[j]+=v
    return sorted(walk(0))

def leaf(K,r,s,T,C,values):
    b,c=len(K),len(K[0]);R=list(r);S=list(s);x=[0]*(b*c);edges=set(T)
    for (i,j),v in zip(C,values):R[i]-=v;S[j]-=v;x[i*c+j]=v
    if min(R+S)<0:return None
    while edges:
        degree=Counter(v for i,j in edges for v in (i,b+j))
        i,j=min((i,j) for i,j in edges if degree[i]==1 or degree[b+j]==1)
        v=R[i] if degree[i]==1 else S[j]
        if not 0<=v<=K[i][j]:return None
        R[i]-=v;S[j]-=v;x[i*c+j]=v;edges.remove((i,j))
    return tuple(x) if not any(R+S) else None

def hall(K,r,s,fixed):
    b,c=len(K),len(K[0]);R=list(r);S=list(s)
    for (i,j),v in fixed.items():R[i]-=v;S[j]-=v
    if min(R+S)<0 or sum(R)!=sum(S):return False
    for mask in range(1,1<<b):
        demand=sum(R[i] for i in range(b) if mask>>i&1)
        capacity=sum(min(S[j],sum(K[i][j] for i in range(b)
                    if mask>>i&1 and (i,j) not in fixed)) for j in range(c))
        if demand>capacity:return False
    return True

def enumerate_chords(K,r,s,T,C,prune,stats):
    fixed={};values=[]
    def walk(d):
        stats['nodes']+=1
        if prune and not hall(K,r,s,fixed):
            stats['pruned']+=1;return
        if d==len(C):
            stats['leaves']+=1
            x=leaf(K,r,s,T,C,values)
            if x is not None:yield x
            return
        i,j=C[d]
        for v in range(K[i][j]+1):
            fixed[i,j]=v;values.append(v)
            yield from walk(d+1)
            values.pop();del fixed[i,j]
    return sorted(walk(0))

def hist(tables,b,c):
    ans=Counter()
    for x in tables:
        a=sum(x[i*c+j]*(i+1)*(j+2) for i in range(b) for j in range(c))
        d=sum(x[i*c+j]*(-1)**(i+j)*(i+2*j+1) for i in range(b) for j in range(c))
        ans[a,d]+=1
    return ans

def main():
    total=Counter();records=[]
    for b,c,vals in [(2,3,(0,1,2)),(3,3,(0,1)),(2,4,(1,))]:
        z=Counter()
        for flat in product(vals,repeat=b*c):
            K=[flat[i*c:(i+1)*c] for i in range(b)];T,C=forest(K)
            z['capacities']+=1
            for r,s in margins(K):
                z['fibers']+=1;n=Counter();p=Counter()
                a=direct(K,r,s);u=enumerate_chords(K,r,s,T,C,False,n)
                v=enumerate_chords(K,r,s,T,C,True,p)
                assert a==u==v
                assert hist(a,b,c)==hist(v,b,c)
                z['assertions']+=2;z['tables']+=len(a)
                z['naive_nodes']+=n['nodes'];z['naive_leaves']+=n['leaves']
                z['cut_nodes']+=p['nodes'];z['cut_leaves']+=p['leaves']
                z['cut_prunes']+=p['pruned']
                z['strict_savings']+=p['nodes']<n['nodes']
        records.append({'domain':f'{b}x{c} K in {vals}','counters':dict(z)})
        total.update(z)
    K=[[1]*4,[1]*4]
    assert not hall(K,(1,3),(1,1,1,1),{(1,1):0,(1,2):0})
    total['assertions']+=1
    print(json.dumps({'status':'ALL_CHECKS_PASS','families':records,'total':dict(total)},sort_keys=True,indent=2))
if __name__=='__main__':main()
