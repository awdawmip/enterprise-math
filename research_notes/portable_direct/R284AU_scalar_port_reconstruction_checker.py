#!/usr/bin/env python3
"""R284AU calibrated scalar Port reconstruction. Standard Python only; exact."""
from fractions import Fraction
from math import factorial
from random import Random
import json
import sys

def det_bareiss(a):
    n = len(a)
    if not n: return 1
    a = [list(map(int, r)) for r in a]
    sign, previous = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            t = next((i for i in range(k+1,n) if a[i][k]), None)
            if t is None: return 0
            a[k],a[t] = a[t],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = pivot
    return sign*a[n-1][n-1]

def reconstruct(A, tree):
    """A is used ONLY to simulate the calibrated hidden determinant oracle."""
    n = len(A)
    B = max(abs(v) for row in A for v in row)
    K = factorial(n)*(2**n)*(B+1)**n
    T = 4*K+3
    f_values, h_values = {}, {}
    queries = 0
    def raw(S, edge=None):
        nonlocal queries
        S = frozenset(S)
        d = [0 if i in S else T for i in range(n)]
        m = [[(d[i] if i==j else 0)-A[i][j] for j in range(n)] for i in range(n)]
        if edge is not None:
            u,v = edge
            m[u][v] -= 1
        queries += 1
        return det_bareiss(m)
    def f(S):
        S = frozenset(S)
        if S not in f_values: f_values[S] = raw(S)
        return f_values[S]
    def h(S,edge):
        key = (frozenset(S),edge)
        if key not in h_values: h_values[key] = raw(S,edge)
        return h_values[key]
    def leading(S,edge=None):
        m = n-len(S)
        v = f(S) if edge is None else h(S,edge)-f(S)
        scale = T**m
        coefficient = (2*v+scale)//(2*scale)
        assert 2*abs(v-coefficient*scale)<scale
        return coefficient
    diag = [-leading([i]) for i in range(n)]
    pair = {}
    for i in range(n):
        for j in range(i+1,n):
            pair[i,j] = diag[i]*diag[j]-leading([i,j])
    def p(i,j): return pair[min(i,j),max(i,j)]
    values = [[None]*n for _ in range(n)]
    for i in range(n): values[i][i] = Fraction(diag[i])
    orient, adj = {}, [[] for _ in range(n)]
    for u,v in tree:
        key = tuple(sorted((u,v)))
        assert u!=v and key not in orient
        orient[key] = (u,v)
        adj[u].append(v); adj[v].append(u)
        reverse = -leading([u,v],(u,v))
        assert reverse != 0
        values[v][u] = Fraction(reverse)
        values[u][v] = Fraction(p(u,v),reverse)
    for root in range(n):
        parent, order = {root:None}, [root]
        for x in order:
            for y in adj[x]:
                if y not in parent: parent[y]=x; order.append(y)
        assert len(order)==n
        for y in order[1:]:
            x = parent[y]
            if x==root: continue
            u,v = orient[tuple(sorted((x,y)))]
            signed = leading([u,v,root],(u,v))
            q = values[v][u]*diag[root]-signed
            if (u,v)==(x,y):
                # q = A[y,root] * A[root,x]
                a = q/values[root][x]
                assert values[y][root] is None or values[y][root]==a
                values[y][root] = a
                b = Fraction(p(root,y),1)/a
                assert values[root][y] is None or values[root][y]==b
                values[root][y] = b
            else:
                # q = A[x,root] * A[root,y]
                a = q/values[x][root]
                assert values[root][y] is None or values[root][y]==a
                values[root][y] = a
                b = Fraction(p(root,y),1)/a
                assert values[y][root] is None or values[y][root]==b
                values[y][root] = b
    assert values==[[Fraction(v) for v in row] for row in A]
    budget = n+n*(n-1)//2+(n-1)+2*(n-1)*(n-2)
    assert queries<=budget
    return dict(n=n,B=B,T_bits=T.bit_length(),queries=queries,budget=budget,
        response_bits=max(abs(v).bit_length() for v in list(f_values.values())+list(h_values.values())),
        tree=tree,pass_recovery=True)

def run():
    rng = Random(28420261119)
    cases = []
    for n in range(2,7):
        for trial in range(12):
            if trial==0: A=[[1]*n for _ in range(n)]
            elif trial==1: A=[[(i+1)*(j+2) for j in range(n)] for i in range(n)]
            else: A=[[rng.randint(1,6) for _ in range(n)] for _ in range(n)]
            edges=[]
            for child in range(1,n):
                parent=rng.randrange(child)
                edges.append((parent,child) if rng.randrange(2) else (child,parent))
            cases.append(reconstruct(A,edges))
    cases.append(reconstruct([[1,2,1],[1,1,2],[2,1,1]],[(0,1),(2,1)]))
    assert len(cases)==61
    return dict(schema="R284AU_SCALAR_PORT_EXACT_VERIFICATION_V1",
        seed=28420261119, cases=61, cases_by_n={str(n):sum(x["n"]==n for x in cases) for n in range(2,7)},
        total_oracle_calls=sum(x["queries"] for x in cases),
        maximum_T_bits=max(x["T_bits"] for x in cases),
        maximum_response_bits=max(x["response_bits"] for x in cases),
        data=cases,status="PASS",independent_review="NOT_REVIEWED",
        excluded_claims=["analog robustness","real-open lower-bound proof","unknown Q or B","native X6 dynamics"])

if __name__=="__main__":
    result=run()
    if len(sys.argv)>1:
        with open(sys.argv[1],"w",encoding="utf8") as f: json.dump(result,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:v for k,v in result.items() if k!="data"},indent=2))
