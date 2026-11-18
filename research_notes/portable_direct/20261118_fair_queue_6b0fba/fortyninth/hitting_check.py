"""Exact finite checks of the layered representation and the frozen positive BRC adapter."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from math import factorial, isqrt
from pathlib import Path
import json
import sys
import types
from urllib.request import urlopen

PATCH_SHA='8b74d37eec97457b71e5873426db6b800a5001039da0f48e813a73b6870da96c'
PATCH_PATH='research_notes/chatgpt_direct/20261007_residual_algebra_patch_7c2e8a/BRC_PATCH.py'
PATCH_URL='https://raw.githubusercontent.com/awdawmip/enterprise-math/bed9964bd6a31dc926e67f759dac66bd83797342/'+PATCH_PATH
PORTS=(1,2,3,4,5,6,-1,-2,-3,-4,-5,-6)


def read_patch(override):
    if override is not None:
        data=Path(override).read_bytes()
    else:
        candidates=[p / PATCH_PATH for p in Path(__file__).resolve().parents]
        candidates.append(Path('/workspace/enterprise-math') / PATCH_PATH)
        found=next((p for p in candidates if p.is_file()),None)
        data=found.read_bytes() if found else urlopen(PATCH_URL,timeout=20).read()
    if sha256(data).hexdigest()!=PATCH_SHA:
        raise ValueError('Frozen BRC patch hash mismatch')
    mod=types.ModuleType('frozen_typed_brc_patch')
    mod.__file__=PATCH_PATH
    sys.modules[mod.__name__]=mod
    exec(compile(data,PATCH_PATH,'exec'),mod.__dict__)
    return mod


def words(n,d):
    return (w for k in range(d+1) for w in product(range(n),repeat=k))


def signature(w,d):
    return Counter(tuple(w[i] for i in chosen) for k in range(min(len(w),d)+1)
                   for chosen in combinations(range(len(w)),k))


def ceil_two_root(u):
    return isqrt(4*u-1)+1


def layer_graph(n,d):
    k=d//2
    odd=d%2
    S=ceil_two_root(n)
    s,t=(S//2,S-S//2) if odd else (1,1)
    # Vertices are layers of words on the two sides; the even central roots are shared.
    levels={}
    def node(side,i,w):
        v=(side,i,w) if odd or w else ('center',0,())
        levels[v]=k-len(w) if side=='L' else k+odd+len(w)
        return v
    edges=[defaultdict(list) for _ in range(n)]
    for i in range(s):
        for w in words(n,k):
            v=node('L',i,w)
            if w:
                edges[w[0]][v].append(node('L',i,w[1:]))
    for j in range(t):
        for w in words(n,k):
            v=node('R',j,w)
            if w:
                edges[w[-1]][node('R',j,w[:-1])].append(v)
    if odd:
        for a in range(n):
            i,j=divmod(a,t)
            edges[a][node('L',i,())].append(node('R',j,()))
    assert all(levels[v]+1==levels[u] for graph in edges for v,us in graph.items() for u in us)
    def private(w):
        if not w:
            v=next(iter(levels))
            return v,v
        if odd:
            idx=min(k,len(w)-1)
            i,j=divmod(w[idx],t)
            return node('L',i,w[:idx]), node('R',j,w[idx+1:])
        cut=min(k,len(w))
        return node('L',0,w[:cut]),node('R',0,w[cut:])
    return levels,edges,private


def mat_times_letter(matrix,edges):
    out=Counter()
    for (u,v),w in matrix.items():
        for y in edges.get(v,()):
            out[u,y]+=w
    return out


def layer_check(n,d):
    levels,edges,private=layer_graph(n,d)
    ident=Counter({(v,v):1 for v in levels})
    all_words=list(words(n,d))
    targets={private(w):w for w in all_words}
    assert len(targets)==len(all_words)
    distinct=0
    def visit(w,M):
        nonlocal distinct
        assert [(targets[e],v) for e,v in M.items() if e in targets]==[(w,1)]
        distinct+=1
        if len(w)==d:
            for edge in edges:
                assert not mat_times_letter(M,edge)
            return
        for a,edge in enumerate(edges):
            visit(w+(a,),mat_times_letter(M,edge))
    visit((),ident)
    hs=[sum(z==j for z in levels.values()) for j in range(d+1)]
    assert all(hs[i]*hs[j]>=n**(j-i) for i in range(d+1) for j in range(i+1,d+1))
    lower=sum(ceil_two_root(n**(d-2*i)) for i in range((d+1)//2))+(d%2==0)
    return dict(letters=n,max_degree=d,widths=hs,matrix_dimension=sum(hs),
                proved_dimension_lower=lower,certified_rank=distinct,
                zero_products_checked=n**(d+1))


def word_matrix(w,levels,edges):
    M=Counter({(v,v):1 for v in levels})
    for a in w:
        M.update(mat_times_letter(M,edges[a]))
    return M


def patch_check(mod):
    levels,edges,get=layer_graph(12,3)
    checked=0
    for w in words(12,3):
        ports=tuple(PORTS[i] for i in w)
        native=mod.signature(ports,3)
        explicit=signature(w,3)
        M=word_matrix(w,levels,edges)
        assert len(native)==len(explicit)
        for u,c in explicit.items():
            v=native[tuple(PORTS[i] for i in u)]
            assert (v.count,v.total,v.dominant)==(c,c,1) and M[get(u)]==c
        checked+=1
    for d in (2,3):
        u,v=(1,2,2,1),(2,1,1,2)
        M,N=(word_matrix(tuple(x-1 for x in w),*layer_graph(12,d)[:2]) for w in (u,v))
        assert (M==N)==(d==2)
        a,b=mod.signature(u,d),mod.signature(v,d)
        assert (a==b)==(d==2)
    p=mod.cwm_recoalesce(mod.cwm_edge(1),mod.cwm_edge(3))
    q=mod.cwm_recoalesce(mod.cwm_edge(2),mod.cwm_edge(2))
    assert p.total==q.total and p.count==q.count and p.dominant!=q.dominant
    return dict(source_sha256=PATCH_SHA,word_signatures_checked=checked,
                b_original_cases={'C2_equal':True,'coefficient_122_degree3':['1','0']},
                positive_weighted_counterexample=['(2,4,3)','(2,4,2)'],
                typed_calls=dict(mod.CALLS))


def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]


def int_matrix(a,D):
    return [[F((-1)**(r-q-1),r*a**(r-q)) if q<r else 0 for q in range(D)] for r in range(D)]


def pole_checks():
    out=[]
    for a,b in combinations(range(1,8),2):
        D=7
        A,B=int_matrix(a,D),int_matrix(b,D)
        for i in range(D):
            A[i][i]=B[i][i]=1
        P,Q=mm(mm(mm(A,B),B),A),mm(mm(mm(B,A),A),B)
        u,v=F(1,a),F(1,b)
        expected=u*v*(v-u)*(v*v-4*u*v+u*u)/120
        assert expected and P[5][0]-Q[5][0]==expected
        assert all(P[i][j]==Q[i][j] for i in range(D) for j in range(D) if i-j<5)
        out.append([a,b,str(expected)])
    return out


def integral_check():
    rows=[]
    for D in range(1,10):
        J=[int_matrix(a,D) for a in (1,2)]
        eye=[[int(i==j) for j in range(D)] for i in range(D)]
        step=[[[v+eye[i][j] for j,v in enumerate(row)] for i,row in enumerate(A)] for A in J]
        def matrix_word(w):
            out=eye
            for a in w:
                out=mm(out,step[a-1])
            return out
        X,Y=matrix_word((1,2)),matrix_word((2,1))
        A,B=matrix_word((1,2,2,1)),matrix_word((2,1,1,2))
        first=next(([i,j,str(A[i][j]-B[i][j])] for i in range(D) for j in range(D)
                    if A[i][j]!=B[i][j]),None)
        for a,V in enumerate(J,1):
            P=eye
            for _ in range(D-1):
                P=mm(P,V)
            assert P==[[F(1,factorial(D-1)*a**(D-1)) if (i,j)==(D-1,0) else 0
                        for j in range(D)] for i in range(D)]
            assert not any(any(row) for row in mm(P,V))
        rows.append(dict(taylor_dimension=D,ordered12_vs21_equal=(X==Y),witness1221_vs2112=first))
    assert rows[2]['ordered12_vs21_equal'] and not rows[3]['ordered12_vs21_equal']
    return rows


def main():
    par=argparse.ArgumentParser(description=__doc__)
    par.add_argument('--patch',help='use a local copy of the frozen hash-checked BRC_PATCH.py')
    args=par.parse_args()
    audit=patch_check(read_patch(args.patch))
    rows=[layer_check(n,d) for n,d in [(2,k) for k in range(1,7)]
          +[(3,3),(4,3),(4,4),(12,1),(12,2),(12,3)]]
    print(json.dumps(dict(patch=audit,layer_rank=rows,integral_truncations=integral_check(),pole_pair_fifth_coefficients=pole_checks()),
                     sort_keys=True,indent=2))
if __name__=='__main__':
    main()
