#!/usr/bin/env python3
"""Exact named-source/BRC count regression for PREFIX-824. Standard Python 3.

The scientific model is the explicitly typed positive branch-count Q=R+A
on finite named subsets, with removal weights beta_i and marked-source
insertion weight a. No classical propagator, pi, or native X6 time is used.
"""
from __future__ import annotations
from itertools import combinations
from math import comb
from fractions import Fraction
import json
from collections import Counter


def states(q, m):
    return [s for k in range(q+1) for s in combinations(range(m+1), k)]


def q_step(state, q, a, b, betas):
    out=Counter()
    for item in state:
        smaller=tuple(x for x in state if x!=item)
        out[smaller]+=b if item==0 else betas[item-1]
    if 0 not in state and len(state)<q:
        out[tuple(sorted((0,)+state))]+=a
    return {s:w for s,w in out.items() if w}


def rows_from_named(q,m,a,b,betas):
    S=states(q,m)
    # row value y[l,j](s) for every terminal cardinality and word depth
    horizon=q+2 if b==0 else 2*q+1
    rows={(l,j):[] for l in range(q+1) for j in range(horizon+1)}
    for s in S:
        dist={s:1}
        for j in range(horizon+1):
            card=[0]*(q+1)
            for state,mass in dist.items():
                card[len(state)]+=mass
            for l in range(q+1):
                rows[(l,j)].append(card[l])
            nxt=Counter()
            for state,mass in dist.items():
                for target,weight in q_step(state,q,a,b,betas).items():
                    nxt[target]+=mass*weight
            dist=dict(nxt)
    return S,rows


def coordinate_index_b0(q):
    coords=[(0,j) for j in range(q+1)]
    for l in range(1,q+1):
        for j in range(q-l+3):
            if (l,j) not in [(1,q),(1,q+1)]:
                coords.append((l,j))
    return coords


def transition_b0(q,coords):
    index={c:i for i,c in enumerate(coords)}
    def apply(x,a):
        ans=[0]*len(coords)
        for i,(l,j) in enumerate(coords):
            if l==0:
                if j<q:ans[i]=x[index[(0,j+1)]]
            elif l==1 and j==q-1:
                ans[i]=a*q*x[index[(0,q-1)]]
            elif j<q-l+2:
                ans[i]=x[index[(l,j+1)]]
        return ans
    return apply


def moments(s,q,betas):
    marked=0 in s
    k=len(s)-int(marked)
    e=[1]+[0]*k
    for idx in s:
        if idx==0:continue
        w=betas[idx-1]
        for h in range(k,0,-1):e[h]+=w*e[h-1]
    return {("V" if marked else "U",k,h):e[h] for h in range(k+1)}


def small_carrier(s,q,a,b,betas):
    M=moments(s,q,betas)
    def u(k,h):return M.get(("U",k,h),0)
    def v(k,h):return M.get(("V",k,h),0)
    if q==1:
        return [u(0,0),u(1,0)+v(0,0),u(1,1)+b*v(0,0)]
    if q==2:
        return [u(0,0),u(1,0),u(1,1),u(2,2),v(0,0),v(1,1),u(2,0)+v(1,0),u(2,1)+b*v(1,0)]
    raise ValueError(q)


def small_update(x,q,a,b):
    if q==1:
        u0,z0,z1=x
        return [z1,a*u0,a*b*u0]
    u00,u10,u11,u22,v00,v11,z0,z1=x
    return [u11+b*v00,z1,2*u22+b*v11,0,v11+a*u00,a*u11,a*u10,a*b*u10]


def rank_fraction(rows):
    rows=[list(map(Fraction,r)) for r in rows]
    if not rows:return 0
    m,n=len(rows),len(rows[0]);rank=0
    for c in range(n):
        pivot=next((r for r in range(rank,m) if rows[r][c]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        scale=rows[rank][c]
        for k in range(c,n):rows[rank][k]/=scale
        for i in range(rank+1,m):
            if rows[i][c]:
                scale=rows[i][c]
                for k in range(c,n):rows[i][k]-=scale*rows[rank][k]
        rank+=1
        if rank==m:break
    return rank


def run():
    cases=0; state_checks=0; update_checks=0; identity_checks=0; rank_checks=0
    rank_by_q={}; examples={}
    # q=1..6, distinct unmarked beta, a=1..3. Full rank via exact rational for q<=6.
    for q in range(1,7):
        d=(q+1)*(q+2)//2+2*q-2
        coords=coordinate_index_b0(q)
        assert len(coords)==d
        rank_by_q[str(q)]=[]
        for a in (1,2,3):
            m=q+1; betas=list(range(1,m+1))
            S,Y=rows_from_named(q,m,a,0,betas)
            index={s:i for i,s in enumerate(S)}
            T=transition_b0(q,coords)
            F={s:[Y[c][index[s]] for c in coords] for s in S}
            for s in S:
                vals=F[s]
                assert [vals[coords.index((l,0))] for l in range(q+1)]==[int(len(s)==l) for l in range(q+1)]
                next_f=[sum(w*F[t][i] for t,w in q_step(s,q,a,0,betas).items()) for i in range(d)]
                assert T(vals,a)==next_f,(q,a,s)
                state_checks+=1;update_checks+=d
                z=vals
                for j in range(q+3):
                    assert [z[coords.index((l,0))] for l in range(q+1)]==[Y[(l,j)][index[s]] for l in range(q+1)]
                    identity_checks+=q+1
                    z=T(z,a)
            for k in range(len(S)):
                assert Y[(1,q)][k]==a*q*Y[(0,q-1)][k]
                assert Y[(1,q+1)][k]==a*q*Y[(0,q)][k]
                identity_checks+=2
            if a==1:
                rank=rank_fraction([Y[c] for c in coords])
                assert rank==d,(q,rank,d)
                rank_checks+=1
                rank_by_q[str(q)].append(rank)
            cases+=1
        examples[str(q)]={"dimension":d,"named_state_count":len(S),"coordinates":len(coords),"future_step_bound":q+2}

    small_cases=0;small_states=0;small_update_coords=0;small_rank_checks=0;small_hist_checks=0
    for q in (1,2):
        d=(q+1)**2-((q+1)//2)
        for a in (1,2,3):
            for b in (1,2,3):
                m=q+1;betas=list(range(1,m+1))
                S,Y=rows_from_named(q,m,a,b,betas)
                F={s:small_carrier(s,q,a,b,betas) for s in S}
                for s in S:
                    vals=F[s]
                    assert len(vals)==d and all(int(x)==x and x>=0 for x in vals)
                    assert ([vals[0],vals[1]] if q==1 else [vals[0],vals[1]+vals[4],vals[6]])==[int(len(s)==l) for l in range(q+1)]
                    nxt=[sum(w*F[t][i] for t,w in q_step(s,q,a,b,betas).items()) for i in range(d)]
                    assert small_update(vals,q,a,b)==nxt,(q,a,b,s,vals,nxt)
                    z=vals
                    for j in range(2*q+2):
                        y=([z[0],z[1]] if q==1 else [z[0],z[1]+z[4],z[6]])
                        assert y==[Y[(l,j)][S.index(s)] for l in range(q+1)],(q,a,b,s,j)
                        small_hist_checks+=q+1
                        z=small_update(z,q,a,b)
                    small_states+=1;small_update_coords+=d
                if a==1 and b==1:
                    fr=[[F[s][i] for s in S] for i in range(d)]
                    assert rank_fraction(fr)==d
                    small_rank_checks+=1
                small_cases+=1
    out={"schema":"PREFIX824_R6_POSITIVE_CARRIER_REGRESSION_V1","model":"positive_branch_named_subset_Q_equals_R_plus_A","b0":{"q_range":[1,6],"a_values":[1,2,3],"cases":cases,"initial_named_state_checks":state_checks,"carrier_update_coordinate_checks":update_checks,"output_and_dependency_checks":identity_checks,"full_exact_rational_rank_checks":rank_checks,"dimensions_by_q":examples,"rank_by_q":rank_by_q},"b_positive_q1_q2":{"q_values":[1,2],"a_values":[1,2,3],"b_values":[1,2,3],"cases":small_cases,"named_state_checks":small_states,"carrier_update_coordinate_checks":small_update_coords,"histogram_checks":small_hist_checks,"full_exact_rank_checks":small_rank_checks},"all_exact_assertions":"PASSED","native_X6_admission":"NOT_TESTED","independent_review":"NOT_PERFORMED"}
    print(json.dumps(out,indent=2,ensure_ascii=False))


if __name__=="__main__":run()
