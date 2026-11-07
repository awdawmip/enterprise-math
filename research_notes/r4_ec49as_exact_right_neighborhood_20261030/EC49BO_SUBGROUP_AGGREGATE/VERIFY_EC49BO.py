#!/usr/bin/env python3
"""Exact EC49BO audit. Run from an Enterprise Math checkout (SymPy required).
This is an author-side finite audit, not native research admission.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha1
from itertools import combinations_with_replacement
from pathlib import Path
import importlib.util
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

NATIVE_SHA='300a96e3dc24bf6fff73743037a0347a8bc83176'
Q=(2,3,3,2,1,1)
Q_SWAP=(3,2,3,2,1,1)
D=(0,)*6
M=Matrix([[1,0,0,1,0],[0,1,1,0,0],[0,1,0,1,0],[1,0,1,0,0]])
assert M.rank()==3
SNF=smith_normal_form(M,domain=ZZ)
assert tuple(SNF[i,i] for i in range(4))==(1,1,1,0)
assert M*Matrix([1,1,-1,-1,0])==Matrix([0,0,0,0])
assert M*Matrix([0,0,0,0,1])==Matrix([0,0,0,0])

def load_native():
    file=Path(__file__).resolve()
    candidates=[file.parents[3]/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',file.with_name('signed_brc.py')]
    for p in candidates:
        if p.is_file():
            data=p.read_bytes()
            oid=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            assert oid==NATIVE_SHA,(oid,NATIVE_SHA)
            spec=importlib.util.spec_from_file_location('verified_native_brc',p)
            mod=importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    raise FileNotFoundError('Pinned native signed_brc.py required')

native=load_native()

def k_vectors(K,axis=6):
    if axis==1:
        yield (K,)
    else:
        for j in range(K+1):
            for rest in k_vectors(K-j,axis-1):
                yield (j,)+rest

def words(k):
    counts=Counter({s:n for i,v in enumerate(k,1) for s,n in ((i,v),(-i,v)) if n})
    seq=[]
    def rec():
        if len(seq)==2*sum(k):
            yield tuple(seq)
        else:
            for s in sorted(counts):
                if counts[s]:
                    counts[s]-=1;seq.append(s)
                    yield from rec()
                    seq.pop();counts[s]+=1
    yield from rec()

def weight(word,q=Q):
    out=Fraction(1)
    for s in word:
        if s>0:out*=q[s-1]
    return out

def sig(k):
    return tuple(Fraction(1) if not k else __import__('math').prod(Fraction(q[i])**v for i,v in enumerate(k)) for q in (Q,Q_SWAP))

kv=list(k_vectors(3))
assert len(kv)==56
pairs=0
for i,a in enumerate(kv):
    for b in kv[i:]:
        z=tuple(x-y for x,y in zip(a,b))
        zero=(z[0]==z[1] and z[2]==z[3]==-z[0] and z[4]==-z[5])
        assert (sig(a)==sig(b))==zero
        pairs+=1
assert pairs==1596
bases=set();current=set();orbit=set();hist=set()
total=0;weight_total=Fraction(0)
for k in kv:
    for w in words(k):
        assert len(w)==6 and all(w.count(j)==w.count(-j) for j in range(1,7))
        s=sig(k)
        assert weight(w)==s[0]
        swapped=tuple((2 if t==1 else 1 if t==2 else -2 if t==-1 else -1 if t==-2 else t) for t in w)
        assert weight(swapped)==s[1]
        bd=(w[0],w[-1]);bases.add(bd)
        current.add((bd,s[0]));orbit.add((bd,s));hist.add((bd,k))
        total+=1;weight_total+=s[0]
assert total==native.endpoint_multiplicity(6,D)==19920
assert weight_total==native.endpoint_weight(6,D,tuple(map(Fraction,Q)),(1,)*6)==152640
assert (len(bases),len(current),len(orbit),len(hist))==(144,468,828,1044)

U=(5,1,-1,3,-3,-5);V=(5,2,-2,4,-4,-5)
assert (weight(U),weight(V))==(6,6)
assert (weight(U,Q_SWAP),weight(V,Q_SWAP))==(9,4)
A1=(5,1,-1,1,-1,-5); A2=(5,2,-2,2,-2,-5)
B1=(5,3,-3,3,-3,-5); B2=(5,4,-4,4,-4,-5)
S=(A1,A2);T=(B1,B2)
assert all(len(t)==6 and t[0]==5 and t[-1]==-5 for t in S+T)
aggregate=lambda ensemble:(sum(weight(w) for w in ensemble),sum(weight(w,Q_SWAP) for w in ensemble))
assert aggregate(S)==aggregate(T)==(13,13)
assert sorted((weight(w),weight(w,Q_SWAP)) for w in S)!=sorted((weight(w),weight(w,Q_SWAP)) for w in T)
filter1=lambda E:sum(weight(w) for w in E if 1 in w or -1 in w)
assert (filter1(S),filter1(T))==(4,0)
print(json.dumps({'unit':'EC49BO','source_git_blob':NATIVE_SHA,'K3_histograms':len(kv),'kernel_pairs_checked':pairs,'smith_diag':[int(SNF[i,i]) for i in range(4)],'smith_rank':int(M.rank()),'all_words':total,'boundary_classes':len(bases),'current_weight_classes':len(current),'orbit_weight_classes':len(orbit),'histogram_classes':len(hist),'native_endpoint_multiplicity':total,'native_endpoint_weight':str(weight_total),'single_weight_UV':['6','6'],'post_swap_UV':['9','4'],'aggregate_S_T':['13','13'],'path_filter_S_T':['4','0'],'status':'AUTHOR_EXACT_FINITE_AUDIT_PASS / UNREVIEWED / NOT_ADMITTED'},sort_keys=True,indent=2))
