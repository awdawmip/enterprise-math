#!/usr/bin/env python3
"""R284AW. Exact Fraction simulation of adversarial finite scalar readout error.
Run alongside R284AU_scalar_port_reconstruction_checker.py; standard library only.
"""
from R284AU_scalar_port_reconstruction_checker import det_bareiss
from fractions import Fraction
from math import factorial
from random import Random
import json
import sys

def validate(A, edges, Q=37):
    n=len(A)
    M=max(max(row) for row in A)
    K=factorial(n)*2**n*(M+1)**n
    T=8*K+3
    calls=0
    F,H={},{}
    def scalar(S,edge=None):
        nonlocal calls
        S=frozenset(S)
        m=[[(T if i==j and i not in S else 0)-A[i][j] for j in range(n)]
           for i in range(n)]
        if edge is not None: m[edge[0]][edge[1]]-=1
        calls+=1
        # The physical oracle reads the rational determinant with an error
        # |error|=1/(16 Q^n), signs alternating to test opposing pair errors.
        error=Fraction(1 if calls%2 else -1,16*Q**n)
        noisy=Fraction(det_bareiss(m),Q**n)+error
        return Q**n*noisy
    def f(S):
        S=frozenset(S)
        if S not in F:F[S]=scalar(S)
        return F[S]
    def h(S,edge):
        key=(frozenset(S),edge)
        if key not in H:H[key]=scalar(S,edge)
        return H[key]
    def leading(S,edge=None):
        reading=f(S) if edge is None else h(S,edge)-f(S)
        scale=T**(n-len(S))
        got=int((2*reading+scale)//(2*scale))
        assert 2*abs(reading-got*scale)<scale
        return got
    diagonals=[-leading([i]) for i in range(n)]
    pairs={}
    for i in range(n):
        for j in range(i+1,n):
            pairs[i,j]=diagonals[i]*diagonals[j]-leading([i,j])
    def p(i,j):return pairs[min(i,j),max(i,j)]
    entries=[[None]*n for _ in range(n)]
    for i in range(n):entries[i][i]=Fraction(diagonals[i])
    adj=[[] for _ in range(n)]
    orientation={}
    for u,v in edges:
        key=min(u,v),max(u,v)
        assert key not in orientation
        orientation[key]=u,v
        adj[u].append(v);adj[v].append(u)
        entries[v][u]=Fraction(-leading([u,v],(u,v)))
        assert entries[v][u]>0
        entries[u][v]=Fraction(p(u,v))/entries[v][u]
    paths={}
    for root in range(n):
        parent={root:None}; queue=[root]
        for x in queue:
            for y in adj[x]:
                if y not in parent:parent[y]=x;queue.append(y)
        assert len(queue)==n
        for y in range(root+1,n):
            path=[y];node=y
            while node!=root:
                node=parent[node]
                path.append(node)
            path.reverse()
            paths[root,y]=path
    for (x,y),path in sorted(paths.items(),key=lambda v:len(v[1])):
        if len(path)==2:continue
        a=path[-2]
        u,v=orientation[min(a,y),max(a,y)]
        delta=leading([u,v,x],(u,v))
        q=entries[v][u]*diagonals[x]-delta
        if (u,v)==(a,y):
            got=q/entries[x][a]
            assert entries[y][x] is None or entries[y][x]==got
            entries[y][x]=got
            entries[x][y]=Fraction(p(x,y))/got
        else:
            got=q/entries[a][x]
            assert entries[x][y] is None or entries[x][y]==got
            entries[x][y]=got
            entries[y][x]=Fraction(p(x,y))/got
    assert entries==[[Fraction(v) for v in row] for row in A]
    budget=3*n*(n-1)//2+1
    assert calls<=budget
    return {"n":n,"calls":calls,"call_bound":budget,"Q":Q,
            "T_bits":T.bit_length(),
            "max_scaled_numerator_bits":max(abs(v.numerator).bit_length()
                                          for v in list(F.values())+list(H.values()))}

def run():
    rng=Random(28420261119)
    results=[]
    for n in range(2,7):
        for trial in range(12):
            if trial==0:A=[[1]*n for _ in range(n)]
            elif trial==1:A=[[(i+1)*(j+2) for j in range(n)] for i in range(n)]
            else:A=[[rng.randrange(1,7) for _ in range(n)] for _ in range(n)]
            tree=[]
            for child in range(1,n):
                parent=rng.randrange(child)
                tree.append((parent,child) if rng.randrange(2) else (child,parent))
            results.append(validate(A,tree))
    results.append(validate([[1,2,1],[1,1,2],[2,1,1]],[(0,1),(2,1)]))
    assert len(results)==61
    return {
      "schema":"R284AW_FINITE_NOISE_EXACT_VALIDATION_V1","status":"PASS",
      "seed":28420261119,"cases":len(results),
      "by_n":{str(n):sum(x["n"]==n for x in results) for n in range(2,7)},
      "total_scalar_reads":sum(x["calls"] for x in results),
      "maximum_T_bits":max(x["T_bits"] for x in results),
      "maximum_scaled_response_numerator_bits":max(x["max_scaled_numerator_bits"] for x in results),
      "denominator":37,
      "error":"adversarial alternating +/- 1/(16*Q**n); exact Fraction",
      "data":results,"review":"NOT_REVIEWED"
    }

if __name__=="__main__":
    result=run()
    if len(sys.argv)>1:
        with open(sys.argv[1],"w",encoding="utf8") as fp:
            json.dump(result,fp,ensure_ascii=False,indent=2)
            fp.write("\n")
    print(json.dumps({k:v for k,v in result.items() if k!="data"},indent=2))
