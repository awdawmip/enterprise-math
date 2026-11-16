#!/usr/bin/env python3
"""Independent exact verification for PREFIX-837; Python 3 standard library.
Q is the sum of legal weighted removal and addition alternatives, not their
composition. State=(bitmask of named unmarked sources, marked bit).
"""
import json
from collections import defaultdict


def q_histogram(weights, steps, a=1, b=2):
    p=len(weights); cap=p
    states={((1<<p)-1,0):1}
    hist=[]
    for t in range(steps+1):
        buckets=[0]*(cap+1)
        for (mask, marked),m in states.items():
            buckets[mask.bit_count()+marked]+=m
        hist.append(buckets)
        if t==steps:break
        nxt=defaultdict(int)
        for (mask, marked),mass in states.items():
            if not marked and mask.bit_count()<cap:
                nxt[(mask,1)]+=a*mass
            if marked:
                nxt[(mask,0)]+=b*mass
            for i,w in enumerate(weights):
                if mask & (1<<i):
                    nxt[(mask^(1<<i),marked)]+=mass*w
        states=dict(nxt)
    return hist


def min_pair_collision(T, max_weight=200):
    d=T-1; seen={}; visits=0
    for m in range(1,max_weight+1):
        for x in range(1,m+1):
            visits+=1
            val=(d*x*m+x+m)
            if val in seen:
                pair, oldprod=seen[val]
                if oldprod!=x*m:
                    return {'T':T,'M':m,'A':list(pair),'B':[x,m],
                            'delta_product':oldprod-x*m,
                            'examined_pairs':visits}
            else:
                seen[val]=((x,m),x*m)
    raise RuntimeError('search cap insufficient')


def main():
    T_values=list(range(3,52,2))
    finite=[]; hist_checks=0
    for T in T_values:
        rec=min_pair_collision(T,200)
        A,B=rec['A'],rec['B']
        da=sum(A)-sum(B)
        dp=A[0]*A[1]-B[0]*B[1]
        assert da+(T-1)*dp==0 and dp!=0
        ah=q_histogram(A,T+2); bh=q_histogram(B,T+2)
        eq=[i for i,(a,b) in enumerate(zip(ah,bh)) if a==b]
        assert eq == [0,T]
        hist_checks+=len(ah)*3
        finite.append({**rec,'equal_frames_through_T_plus_2':eq,
                       'collision_histogram':ah[T]})
    sq=[]
    for k in [3,5,7,9,11,13]:
        T=k*k; M=T+2*k
        A=[1,M];B=[k+1,k+1]
        assert sum(A)-sum(B)==T-1
        assert A[0]*A[1]-B[0]*B[1]==-1
        ha=q_histogram(A,T+2);hb=q_histogram(B,T+2)
        eq=[j for j in range(T+3) if ha[j]==hb[j]]
        assert eq==[0,T]
        assert M == (k+1)**2-1
        sq.append({'k':k,'T':T,'M_exact':M,'A':A,'B':B,
                   'equal_frames_through_T_plus_2':eq,'collision_histogram':ha[T]})
        hist_checks+=3*(T+3)
    assert [r['M'] for r in finite if r['T'] in (3,5,9,25,49)]==[7,11,15,35,63]
    data={'schema':'PREFIX837_R6_ODD_TWO_SOURCE_RESULTS_V1',
          'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
          'model':'p=q=2; initially two named unmarked sources present, marked absent; Q=R+A; a=1,b=2; unnormalized occupancy counts',
          'status':'ALL_EXACT_ASSERTIONS_PASSED',
          'finite_exact_optima':finite,
          'optimal_odd_square_witnesses':sq,
          'histogram_scalar_comparisons':hist_checks,
          'finite_search_examined_pairs_total':sum(r['examined_pairs'] for r in finite),
          'scope':'25 finite exact integer optima for odd T=3..51, six square witnesses for T=9..169; general mathematical statements require human proof'}
    print(json.dumps(data,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
