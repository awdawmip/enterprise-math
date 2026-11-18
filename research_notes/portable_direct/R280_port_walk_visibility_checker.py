#!/usr/bin/env python3
"""R280 exact BRC labeled Port edit-word visibility certificate; Python stdlib."""
from fractions import Fraction as Q
from itertools import product
from collections import deque
import json

def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))] for i in range(len(a))]

def inverse(a):
    n=len(a); z=[[Q(a[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if z[i][k]); z[k],z[p]=z[p],z[k]
        v=z[k][k]; z[k]=[a/v for a in z[k]]
        for i in range(n):
            if i!=k:
                f=z[i][k]; z[i]=[z[i][j]-f*z[k][j] for j in range(2*n)]
    return [r[n:] for r in z]

def green(w):
    n=len(w)
    return inverse([[Q(i==j)-w[i][j] for j in range(n)] for i in range(n)])

def word_weight(s,r,edges,word):
    if not word:return s[r][r]
    v=s[r][edges[word[0]][0]]
    for i,j in zip(word,word[1:]):v*=s[edges[i][1]][edges[j][0]]
    return v*s[edges[word[-1]][1]][r]

def bfs_depth(s,r,edges):
    m=len(edges)
    starts=[i for i,(u,v) in enumerate(edges) if s[r][u]>0]
    goal={i for i,(u,v) in enumerate(edges) if s[v][r]>0}
    q=deque((i,1) for i in starts); seen=set(starts)
    while q:
        i,d=q.popleft()
        if i in goal:return d
        for j,(u,v) in enumerate(edges):
            if j not in seen and s[edges[i][1]][u]>0:
                seen.add(j);q.append((j,d+1))
    return None

def relevant_edits(s,r,edges):
    m=len(edges)
    start=[i for i,(u,v) in enumerate(edges) if s[r][u]>0]
    end=[i for i,(u,v) in enumerate(edges) if s[v][r]>0]
    arcs=[[j for j,(u,v) in enumerate(edges) if s[edges[i][1]][u]>0] for i in range(m)]
    def reach(seeds,adj):
        seen=set(seeds);todo=list(seeds)
        while todo:
            for nxt in adj[todo.pop()]:
                if nxt not in seen:seen.add(nxt);todo.append(nxt)
        return seen
    rev=[[i for i in range(m) if j in arcs[i]] for j in range(m)]
    return sorted(reach(start,arcs)&reach(end,rev))

def first_degree_containing(s,r,edges,target):
    starts=[i for i,(u,v) in enumerate(edges) if s[r][u]>0]
    goals={i for i,(u,v) in enumerate(edges) if s[v][r]>0}
    q=deque((i,i==target,1) for i in starts)
    seen={(i,i==target) for i in starts}
    while q:
        i,touched,d=q.popleft()
        if i in goals and touched:return d
        for j,(u,v) in enumerate(edges):
            if s[edges[i][1]][u]>0:
                state=(j,touched or j==target)
                if state not in seen:seen.add(state);q.append((j,state[1],d+1))
    return None

def independently_computed_taylor(s,r,edges,weights,degree):
    n=len(s);e=[[Q(0) for j in range(n)] for i in range(n)]
    for (u,v),weight in zip(edges,weights):e[u][v]+=weight
    se=mm(s,e); power=[row[:] for row in s];out=[s[r][r]]
    for d in range(1,degree+1):
        power=mm(se,power);out.append(power[r][r])
    return out

def word_taylor(s,r,edges,weights,degree):
    m=len(edges)
    return [sum((word_weight(s,r,edges,w)*__import__('math').prod(weights[i] for i in w) for w in product(range(m),repeat=d)),Q(0)) for d in range(degree+1)]

def test_model(w,r,edges,weights,max_degree=5):
    s=green(w)
    independent=independently_computed_taylor(s,r,edges,weights,max_degree)
    enumerated=word_taylor(s,r,edges,weights,max_degree)
    assert independent==enumerated
    d=bfs_depth(s,r,edges)
    nonzero=next((i for i,x in enumerate(enumerated[1:],1) if x),None)
    assert d==nonzero
    return {"depth":d,"coefficients":[str(x) for x in enumerated],"ordered_words_tested":sum(len(edges)**k for k in range(max_degree+1)),"relevant_edges":relevant_edits(s,r,edges),"first_degree_by_edge":[first_degree_containing(s,r,edges,i) for i in range(len(edges))]}

# Example 1: same initial star and first derivative, different second derivative and one-edit readout.
def triangular(gamma):
    return [[Q(0),Q(1,4),Q(0)],
            [Q(0),Q(0),Q(0)],
            [Q(1,4),Q(gamma),Q(0)]]
E=[(1,2)]
a=test_model(triangular(Q(0)),0,E,[Q(1)],5)
b=test_model(triangular(Q(1,4)),0,E,[Q(1)],5)
assert a['coefficients'][:3]==['1','1/16','1/256']
assert b['coefficients'][:3]==['1','1/16','5/256']
for gamma,expected in [(Q(0),Q(64,63)),(Q(1,4),Q(60,59))]:
    w=triangular(gamma);w[1][2]=Q(1,4)
    assert green(w)[0][0]==expected
    assert all(sum(row)<1 for row in w)

# Example 2: joint-only two edits; neither singleton makes a difference.
cycle=test_model([[Q(0),Q(0)],[Q(0),Q(0)]],0,[(0,1),(1,0)],[Q(1),Q(1)],5)
assert cycle['depth']==2 and cycle['coefficients'][:5]==['1','0','1','0','1']
# Here for base W=0, only chain 0->1 then 1->0 contributes; hence t^2 coefficient one.

# Example 3: two labels can be discarded from this scalar observer's full future.
w4=[[Q(0),Q(1,4),Q(0),Q(0)],
    [Q(0),Q(0),Q(0),Q(0)],
    [Q(1,4),Q(0),Q(0),Q(0)],
    [Q(0),Q(0),Q(0),Q(0)]]
e4=[(1,2),(3,3),(2,3)]
four=test_model(w4,0,e4,[Q(1),Q(1),Q(1)],5)
assert four['relevant_edges']==[0]
updated=[row[:] for row in w4]
for (u,v),x in zip(e4,[Q(1,4),Q(1,3),Q(1,5)]):updated[u][v]+=x
sparse_star=green(updated)[0][0]
updated[3][3]=Q(0);updated[2][3]=Q(0)
assert green(updated)[0][0]==sparse_star==Q(64,63)

# Example 4: per-edge bound 2m-1 is attained at m=2.
w5=[[Q(0) for j in range(5)] for i in range(5)]
for u,v in [(0,1),(2,0),(2,3),(4,1)]:w5[u][v]=Q(1,8)
five=test_model(w5,0,[(1,2),(3,4)],[Q(1),Q(1)],5)
assert five['depth']==1 and five['first_degree_by_edge']==[1,3]
s5=green(w5)
assert word_weight(s5,0,[(1,2),(3,4)],(0,1,0))==Q(1,4096)
assert sum(word_weight(s5,0,[(1,2),(3,4)],w) for w in product(range(2),repeat=3) if 1 in w)==Q(1,4096)

print('R280 PASS')
print(json.dumps({'triangular_zero':a,'triangular_quarter':b,'two_edge_cycle':cycle,'irrelevant_edit_example':four,'irrelevant_star':str(sparse_star),'sharp_bound_example':five,'sharp_mixed_coefficient':'1/4096'},indent=2))
