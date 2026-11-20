#!/usr/bin/env python3
"""Stage420-B native-X6 future-quotient: exact finite cross-check.

Requires Python >=3.9 standard library. All endpoints/J/K are integer/categorical.
Mathematical all-horizon scope is established by PROOF_STAGE420B.md, not by
this bounded search. No native task/Driver acceptance is implied.
"""
from collections import defaultdict, deque
from itertools import combinations
from json import dumps

D = tuple(x for j in range(1, 7) for x in (j, -j))
A, B = 1, -1
GROUPS = ((0,1,2,3),(4,5,12,13),(6,14,20),(7,15,21),
          (8,16,22),(9,17),(10,18,24),(11,19),
          (23,),(25,),(26,),(27,),(28,),(29,),(30,),(31,))
TESTS = (
    (('APP',B,B),('CANCEL',),('POP',),('POP',),('APP',B,B),('CANCEL',)),
    (('APP',B,B),('CANCEL',),('APP',B,A),('POP',),('POP',),('CANCEL',)),
    (('APP',B,B),('CANCEL',),('CANCEL',),('POP',),('POP',)),
)

def fiber(n):
    for r in range(2,n-2):
        for s in range(r+2,n):
            for i in (r,s):
                P = (A,)*(i-1)+(B,)+(A,)*(n-i)
                Q = (A,)*(r-1)+(B,)+(A,)*(s-r-1)+(B,)+(A,)*(n-s)
                yield (r,s,i,P,Q)

def O(P,Q):
    def side(X):
        j = defaultdict(int)
        for edge in zip(X,X[1:]): j[edge]+=1
        return len(X),tuple(X.count(k)-X.count(-k) for k in range(1,7)),tuple(sorted(j.items()))
    return side(P),side(Q),sum(p==q for p,q in zip(P,Q))

def action(state, op):
    P,Q,pop,cancel,apps = state
    kind = op[0]
    if kind=='APP':
        if apps == 0: return None
        a,b = op[1:]
        assert a in D and b in D
        return (P+(a,),Q+(b,),pop,cancel,apps-1)
    if kind=='POP':
        if pop==0 or not Q: return None
        return (P,Q[:-1],pop-1,cancel,apps)
    if kind=='CANCEL':
        if cancel==0 or len(P)<2 or len(Q)<2 or P[-2]!=-P[-1] or Q[-2]!=-Q[-1]:
            return None
        return (P[:-2],Q[:-2],pop,cancel-1,apps)
    raise ValueError(kind)

def trace(h,operations):
    state=(h[3],h[4],2,2,len(operations))
    snapshots=[('INITIAL',O(*state[:2]))]
    for op in operations:
        state=action(state,op)
        if state is None:
            snapshots.append(('DENIED',op))
            break
        snapshots.append(('OK',O(*state[:2])))
    return tuple(snapshots)

def key(h): return h[3][-6:],h[4][-7:]

def compact(w):
    return ''.join('A' if j==A else 'B' if j==B else str(j) for j in w)

def bounded_equal(h1,h2,maxapps=3,letters=(1,-1,2,-2)):
    start=((h1[3],h1[4],2,2,maxapps),(h2[3],h2[4],2,2,maxapps))
    queue=deque([start]);seen={start}
    while queue:
        x,y=queue.popleft()
        moves=[('POP',),('CANCEL',)]
        if x[-1]:moves += [('APP',a,b) for a in letters for b in letters]
        for m in moves:
            xx,yy=action(x,m),action(y,m)
            assert (xx is None)==(yy is None),('enabledness mismatch',m)
            if xx is None:continue
            assert O(*xx[:2]) == O(*yy[:2]),('observable mismatch',m)
            nxt=xx,yy
            if nxt not in seen:
                seen.add(nxt);queue.append(nxt)
    return len(seen)

def main():
    f11=list(fiber(11))
    representatives={}
    for h in f11:representatives.setdefault(key(h),h)
    reps=list(representatives.values()); keys=list(representatives.keys())
    assert len(reps)==32
    signatures=defaultdict(list)
    for idx,h in enumerate(reps):signatures[tuple(trace(h,t) for t in TESTS)].append(idx)
    found=tuple(tuple(g) for g in sorted(signatures.values(),key=lambda v:v[0]))
    assert found==GROUPS,('signature partition mismatch',found)
    lookup={keys[i]:j for j,grp in enumerate(GROUPS) for i in grp}
    total_histories=0
    for n in range(11,41):
        f=list(fiber(n));total_histories+=len(f)
        assert len(f)==(n-3)*(n-4)
        initial={O(h[3],h[4]) for h in f}
        assert len(initial)==1,('initial observation fiber',n)
        counts=[0]*16
        for h in f:counts[lookup[key(h)]]+=1
        expect=[(n-7)*(n-8),2*(n-7),n-6,n-6,n-6,n-7,n-6,n-7]+[1]*8
        assert counts==expect,(n,counts,expect)
        for j in range(4,8):
            subset=[h for h in f if lookup[key(h)]==j]
            s=n-2 if j in (4,5) else n-1
            assert all(h[1]==s for h in subset)
            if j in (4,6):assert all(h[2]==h[0] and 2<=h[0]<=n-5 for h in subset)
            else:assert all(h[2]==s and 2<=h[0]<=n-6 for h in subset)
    visited=[];one_step_full_d=0
    for g in GROUPS[4:8]:
        for i,j in combinations(g,2):
            h1,h2=reps[i],reps[j]
            assert O(h1[3],h1[4])==O(h2[3],h2[4])
            for a in D:
                for b in D:
                    assert trace(h1,(('APP',a,b),))==trace(h2,(('APP',a,b),))
                    one_step_full_d+=1
            visited.append({'pair':[i,j], 'visited_exact_pair_states':bounded_equal(h1,h2)})
    signatures_n11=[tuple(trace(reps[g[0]],t) for t in TESTS) for g in GROUPS]
    assert len(set(signatures_n11))==16
    return {
        'marker':'STAGE420B_PARAMETRIC_EXACT_SIXTEEN_CLASS_PASS',
        'model':'Native signed-X6 (12 APP directions per source), 2 Q POP and 2 paired CANCEL; full integer O=(length, z, directed J, absolute K)',
        'frozen_science':{'global':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
          'enterprise_math':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
          'p000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
        'parameter_count_check':{'n_min':11,'n_max':40,'histories_checked':total_histories,'n11':56,'n16':156,
            'classes':16, 'n16_class_sizes':[72,18,10,10,10,9,10,9]+[1]*8},
        'signature_groups_by_raw_suffix_index':GROUPS,
        'new_groups_4_to_7':{
          'n11_representative_indices':GROUPS[4:8],
          'n11_pair_bfs_3_APP_full_two_destructive_budgets_4_directions':visited,
          'full_12x12_one_APP_pair_equalities_checked':one_step_full_d,
        },
        'method_note':'Finite exact BFS is a cross-check. Universal all-direction/all-finite-future equivalence follows from deletion-frontier arguments in the proof; lower bound from three explicit traces with distinct signatures and front-padding invariance.',
        'proof_status':'AUTHOR_SIDE_COMPLETE / INDEPENDENT_REVIEW_PENDING / NATIVE_RESULT_PENDING'
    }

if __name__=='__main__':
    print(dumps(main(),indent=2,ensure_ascii=False))
