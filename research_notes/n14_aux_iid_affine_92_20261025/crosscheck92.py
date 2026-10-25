#!/usr/bin/env python3
"""Independent ordered-word DFS and minimizing Bellman recurrence for auxiliary iid stage92.
Shares inherited deterministic actions with derive92; no independent Driver status.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
import json
import derive92 as m

def ordered_first_hits(target):
    n,a,b=target;hits=[]
    def walk(word,p,q,a0,b0):
        k=len(word)
        if (k,a0,b0)==target:
            hits.append((word,p,q));return
        if k==n or m.act((k,a0,b0))!='C':return
        for i in range(3):
            walk(word+(i,),p*m.P[i],q*m.Q[i],a0+(i==0),b0+(i==1))
    walk(tuple(),F(1),F(1),0,0)
    return hits

def ordered_suffix_tree(target):
    leaves=Counter();T=[F(),F(),F(),F()]
    def walk(st,p,q,t):
        z=m.act(st)
        if z!='C':
            leaves[(st,z)]+=1
            if z=='Q':T[0]+=p
            elif z=='P':T[1]+=q
            else:raise ValueError(z)
            T[2]+=p*t;T[3]+=q*t
            return
        for i in range(3):walk(m.child(st,i),p*m.P[i],q*m.Q[i],t+1)
    walk(target,F(1),F(1),0)
    return leaves,tuple(T)

def independent_min_bellman():
    @lru_cache(None)
    def val(st):
        n,a,b=st
        opts=[m.K*F(2**(a+b),3**a),m.LP]
        if n<m.N:opts.append(F(1)+sum((m.P[i]*val(m.child(st,i)) for i in range(3)),F()))
        return min(opts)
    root=val((0,0,0));return root,val.cache_info().currsize

def main():
    d=m.main();stats={}
    for key,st in [('A92',m.A),('B',m.B)]:
        hits=ordered_first_hits(st)
        leaves,cont=ordered_suffix_tree(st)
        p=sum((item[1] for item in hits),F())
        q=sum((item[2] for item in hits),F())
        assert (p,q,len(hits))==m.firsthit(st)
        assert cont==m.suffix(st)
        assert p>0 and q>0
        n,a,b=st
        nominal=factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))
        stats[key]=dict(state=st,nominal_prefix_words=nominal,actual_first_hit_words=len(hits),
            p_mass=str(p),q_mass=str(q),terminal_suffix_words=sum(leaves.values()),
            terminal_action_state_classes=len(leaves),full_truncated_words=len(hits)*sum(leaves.values()),
            continuation_qp_errors_and_extra_times=list(map(str,cont)))
    assert m.A[0]==m.B[0] and m.A!=m.B # depth-12 disjoint path cones
    root,nstates=independent_min_bellman()
    assert root==d['root']==m.V0+m.G*m.alpha0
    assert nstates==680
    assert d['count']==1240 and d['pos']==1238 and d['bad']==[]
    assert set(d['ties'])=={(m.A,'C','P'),(m.B,'C','Q')}
    assert m.act(m.A)=='C' and m.act(m.B)=='C'
    assert d['h']==(d['X']+d['Y'])/(d['E']+d['H'])
    assert d['eta']==-d['X']+d['E']*d['h']==d['Y']-d['H']*d['h']>0
    assert 0<m.S<d['s92']<1
    assert d['alpha92']==m.alpha0+d['eta']
    assert d['V92']==m.V0-m.G*d['eta']
    f0=d['f0'];f1=d['f1']
    assert f0[0]==f0[1]==m.alpha0 and f1[0]==f1[1]==d['alpha92']
    assert f0[2]==m.V0 and f1[2]==d['V92']
    assert f0[2]>f0[3] and f1[2]>f1[3]
    for u in [F(),F(1,127),F(1,11),F(1,3),F(1,2),F(9,13),F(127,128),F(1)]:
        s=m.S+d['h']*u
        ep,eq,tp,tq=m.forward(u,s)
        assert ep==eq==m.alpha0+d['eta']*u
        assert tp==m.V0-m.G*d['eta']*u and tp>tq
        assert tp+m.LP*ep+m.LQ*eq==root
    assert d['nxt']==(F(36260219477628,21860934947),(5,4,0),'C','P')
    assert d['errs']==[]
    return dict(status='PASS_EXACT_ORDERED_DFS_MIN_BELLMAN_CONTINUUM_ENDS',
        first_hits_and_suffixes=stats,Bellman_min_root=str(root),Bellman_states=nstates,
        nonselected_comparisons=d['count'],strict_positive_gaps=d['pos'],
        negative_gaps=len(d['bad']),zero_ties=str(d['ties']),minimum_positive_gap=str(d['gap']),
        tP_minus_tQ_start=str(f0[2]-f0[3]),tP_minus_tQ_end=str(f1[2]-f1[3]),
        h92=str(d['h']),eta92=str(d['eta']),s92=str(d['s92']),alpha92=str(d['alpha92']),
        V92=str(d['V92']),K92=str(m.K),Gamma92=str(m.G),next_candidate=str(d['nxt']))

if __name__=='__main__':print(json.dumps(main(),indent=2))
