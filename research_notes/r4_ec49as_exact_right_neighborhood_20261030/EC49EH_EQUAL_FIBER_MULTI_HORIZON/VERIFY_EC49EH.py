#!/usr/bin/env python3
"""EC49EH: self-contained exact native-X6 certificates and exhaustive h<=3 frontier.
No external dependencies; only returns claims explicitly checked.  Python 3.10+.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from collections import defaultdict

OP = {
    'a': (-1, -1), 'b': (-2, -2),
    'c': (1, 2, -1, -2), 'd': (2, 1, -2, -1),
    'e': (3, 1, 1, -3), 'f': (1, -1), 'g': (2, -2)
}
ATOMS = [('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0)]
BUCKETS = ('N','A','B','AB','BA')
MOD = 1000003

def native(w: str) -> tuple[int, ...]:
    return tuple(v for c in w for v in OP[c])

def counts(p: tuple[int,...]) -> tuple[int,...]:
    return tuple(p.count(i) for i in range(1,7))

def displacement(p: tuple[int,...]) -> tuple[int,...]:
    return tuple(p.count(i)-p.count(-i) for i in range(1,7))

def update_state(steps: tuple[int,...], status='N', last=0) -> tuple[str,int]:
    for v in steps:
        a = last==1 and v==2
        b = last==2 and v==1
        if status=='N':
            if a: status='A'
            elif b: status='B'
        elif status=='A' and b: status='AB'
        elif status=='B' and a: status='BA'
        last=v
    return status,last

def atom(steps:tuple[int,...]) -> tuple[str,int]:
    status,last=update_state(steps)
    if status=='N': return ('N', last if last in (1,2) else 0)
    if status=='A': return ('A',2 if last==2 else 0)
    if status=='B': return ('B',1 if last==1 else 0)
    return (status,0)

def histories() -> list[tuple[int,...]]:
    needed={}
    pool=(-2,)*2+(-1,)*4+(1,)*2+(2,)*2
    for p in set(itertools.permutations(pool)):
        a=atom(p)
        if a not in needed: needed[a]=p
        if len(needed)==9: break
    assert len(needed)==9
    return [needed[a] for a in ATOMS]

def transfer(p:tuple[int,...]) -> tuple[int,...]:
    return tuple(BUCKETS.index(update_state(p, s, last)[0]) for s,last in ATOMS)

def columns(t:tuple[int,...]) -> tuple[int,...]:
    return tuple(sum(1<<row for row,val in enumerate(t) if val==b) for b in range(5))

def rank_mod(cols: list[int]) -> int:
    pivots={}
    for bitcol in cols:
        v=[(bitcol>>i)&1 for i in range(9)]
        for j in range(9):
            if not v[j]: continue
            if j in pivots:
                q=pivots[j]; a=v[j]
                for k in range(j,9):v[k]=(v[k]-a*q[k])%MOD
            else:
                inv=pow(v[j],-1,MOD)
                pivots[j]=[(a*inv)%MOD for a in v]
                break
    return len(pivots)

def bareiss(A:list[list[int]]) -> int:
    n=len(A); a=[list(map(int,r)) for r in A]
    sign=1;d=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]!=0),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign*=-1
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numer%d==0
                a[i][j]=numer//d
            a[i][k]=0
        d=pivot
    return sign*a[n-1][n-1]

def det_witness(words:list[str]) -> tuple[int,list[tuple[str,str]]]:
    labels=[];cs=[]
    for w in words:
        c=columns(transfer(native(w)))
        for j,v in enumerate(c): labels.append((w,BUCKETS[j]));cs.append(v)
    chosen=[]; basis=[]
    for k,c in enumerate(cs):
        if rank_mod(basis+[c])>len(basis):
            chosen.append(k);basis.append(c)
            if len(basis)==9:break
    if len(basis)<9:return 0,[]
    matrix=[[(cs[k]>>i)&1 for k in chosen] for i in range(9)]
    return bareiss(matrix),[labels[k] for k in chosen]

def prefixes(path:tuple[int,...]) -> set[tuple[int,...]]:
    return {path[:k] for k in range(1,len(path)+1)}

def trie_cost(words:list[str]) -> int:
    return len(set().union(*(prefixes(native(w)) for w in words)))

def weighted(p:tuple[int,...],weights:tuple[int,...])->int:
    product=1
    for i,exponent in enumerate(counts(p)):product*=weights[i]**exponent
    return product

def groups(h:int):
    ans=defaultdict(list)
    for chars in itertools.product('acdefg', repeat=h):
        w=''.join(chars)
        if w.count('e')-w.count('a')!=1:continue
        p=native(w)
        if displacement(p)!=(2,0,0,0,0,0):continue
        ans[counts(p)].append(w)
    return ans

def full_rank(words:list[str])->bool:
    return rank_mod([c for w in words for c in columns(transfer(native(w)))])==9

def exact_h3():
    base=('ce','de','ec','ed')
    baseline=set().union(*(prefixes(native(w)) for w in base))
    assert len(baseline)==28 and full_rank(list(base))
    groups2=groups(2)
    assert sum(len(v) for v in groups2.values())==8
    assert {k for k,words in groups2.items() if full_rank(words)}=={(3,1,1,0,0,0)}
    for size in range(0,4):
        for ss in itertools.combinations(base,size): assert not full_rank(list(ss))
    groups3=groups(3)
    assert sum(len(v) for v in groups3.values())==51
    best=999; argmin=[]; tested=0; ranked=0
    fibermin={}
    for f,words in groups3.items():
        local=999
        for mask in range(1,1<<len(words)):
            tested+=1
            sel=[w for i,w in enumerate(words) if mask>>i&1]
            if not full_rank(sel):continue
            ranked+=1
            pp=baseline.copy()
            for w in sel:pp.update(prefixes(native(w)))
            cost=len(pp)
            local=min(local,cost)
            if cost<best:best=cost;argmin=[(f,sel)]
            elif cost==best:argmin.append((f,sel))
        fibermin[str(f)]=None if local==999 else local
    assert best==36
    return {'H2':28,'H3':best,'return_words_h2':8,'return_words_h3':51,
            'fiber_h2_counts':{str(k):len(v) for k,v in groups2.items()},
            'fiber_h3_counts':{str(k):len(v) for k,v in groups3.items()},
            'subset_masks_tested':tested,'rank9_subsets':ranked,
            'fiber_minima_H3':fibermin,'number_of_optimal_H3_subsets':len(argmin),
            'optimal_H3_examples':[{'fiber':list(f),'words':words} for f,words in argmin[:10]]}

def run():
    H=histories()
    assert all(len(h)==10 and displacement(h)==(-2,0,0,0,0,0) and counts(h)==(2,2,0,0,0,0) for h in H)
    assert [atom(h) for h in H]==ATOMS
    x=(2,3,5,7,11,13);y=(3,4,7,11,13,17)
    certificates=[]
    base=['ce','de','ec','ed']
    assert len({counts(native(w)) for w in base})==1
    det,cols=det_witness(base)
    assert abs(det)==1
    certificates.append({'kind':'base_h2','words':base,'positive_counts':list(counts(native(base[0]))),'determinant':det,'selected_columns':cols,'cost':trie_cost(base)})
    for h in range(3,33):
        same=['feg'+'f'*(h-3),'gef'+'f'*(h-3)]
        assert all(displacement(native(w))==(2,0,0,0,0,0) for w in same)
        assert len({counts(native(w)) for w in same})==1
        assert counts(native(same[0]))==(h,1,1,0,0,0)
        assert all(len(native(w))==2*h+2 for w in same)
        det,cols=det_witness(same)
        assert abs(det)==1
        for hist in H:
            for future in same:
                for weights in (x,y):
                    assert weighted(hist+native(future),weights)==weighted(hist,weights)*weighted(native(future),weights)
        if h<=6 or h==32:
            joint=base+[w for z in range(3,h+1) for w in ('feg'+'f'*(z-3),'gef'+'f'*(z-3))]
            assert trie_cost(joint)==4*h+30
            certificates.append({'kind':'equal_two_branch','h':h,'words':same,'positive_counts':list(counts(native(same[0]))),'determinant':det,'selected_columns':cols,'joint_trie_cost':trie_cost(joint)})
    for h in range(2,33):
        ws=[w+'f'*(h-2) for w in base]
        assert len({counts(native(w)) for w in ws})==1
        assert counts(native(ws[0]))==(h+1,1,1,0,0,0)
        det,cols=det_witness(ws)
        assert abs(det)==1
        if h<=6 or h==32:
            joint=[w+'f'*(z-2) for z in range(2,h+1) for w in base]
            assert trie_cost(joint)==8*h+12
            certificates.append({'kind':'equal_four_branch','h':h,'positive_counts':list(counts(native(ws[0]))),'determinant':det,'joint_trie_cost':trie_cost(joint)})
    return {'status':'PASS','domain':'native six-axis signed primitive ordered path; A/B first-event five buckets; two positive BRC factors','actual_histories':[list(h) for h in H],
      'exact_h2_h3_exhaustive':exact_h3(),'unimodular_certificates':certificates,
      'all_H_analytic_upper':{'for_H_ge_2':'8H+12','for_H_ge_3':'4H+30','combined':'min(8H+12,4H+30), H>=3'},
      'inference_scope':'h2-h3 exhaustive; h>=2 constructive certificates plus analytic prefix counting; no claim that general-H upper is optimal'}

if __name__=='__main__':
    obj=run()
    print(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True))
