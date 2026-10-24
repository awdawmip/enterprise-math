#!/usr/bin/env python3
"""Independent ordered-prefix/suffix enumeration and exact endpoint tests.
This shares stage86's inherited selected-action policy; NOT a clean Driver check.
"""
from collections import Counter
from fractions import Fraction as F
from math import factorial
import json
import derive87 as m

def true_prefixes(target):
    n,a,b=target
    out=[]
    def walk(word, pp, qq, a0, b0):
        k=len(word)
        st=(k,a0,b0)
        if st==target:
            out.append((word,pp,qq));return
        if k==n or m.act(st)!='C':return
        for i in range(3):
            walk(word+(i,),pp*m.P[i],qq*m.Q[i],a0+(i==0),b0+(i==1))
    walk(tuple(), F(1),F(1),0,0)
    return out

def suffix_tree(target):
    leaves=Counter();totals=[F(),F(),F(),F()]
    def go(st,p,q,t):
        action=m.act(st)
        if action!='C':
            leaves[(st,action)]+=1
            if action=='Q':totals[0]+=p
            elif action=='P':totals[1]+=q
            else:raise ValueError(action)
            totals[2]+=t*p;totals[3]+=t*q
            return
        for i in range(3):
            go(m.child(st,i),p*m.P[i],q*m.Q[i],t+1)
    go(target,F(1),F(1),0)
    return leaves,tuple(totals)

def main():
    rr=m.main();obs={}
    for label,st in [('A87',m.A),('B',m.B)]:
        prefixes=true_prefixes(st);leaves,tup=suffix_tree(st)
        pmass=sum((x[1] for x in prefixes),F())
        qmass=sum((x[2] for x in prefixes),F())
        assert (pmass,qmass,len(prefixes))==m.firsthit(st)
        assert tup==m.suffix(st)
        assert 0<pmass and 0<qmass and len(leaves)>0
        obs[label]={
            'state':str(st),
            'nominal_ordered_prefix_count':factorial(st[0])//(factorial(st[1])*factorial(st[2])*factorial(st[0]-st[1]-st[2])),
            'true_first_hit_prefixes':len(prefixes),
            'P_first_hit_mass':str(pmass),
            'Q_first_hit_mass':str(qmass),
            'suffix_terminal_words':sum(leaves.values()),
            'terminal_state_classes':len(leaves),
            'truncated_complete_words':len(prefixes)*sum(leaves.values()),
            'continuation_errors_and_extra_times':list(map(str,tup))
        }
    assert obs['A87']['true_first_hit_prefixes']==19795
    assert obs['A87']['truncated_complete_words']==59385
    assert obs['B']['true_first_hit_prefixes']==12
    assert rr['count']==1240 and rr['pos']==1238 and not rr['bad']
    assert set(rr['ties'])=={(m.A,'C','P'),(m.B,'C','Q')}
    assert rr['gap']==F(177199183,4968677376)
    assert rr['root']==m.V0+m.G*m.alpha0
    assert rr['h']==F(3353273,208896000000)
    assert rr['eta']==F(32166875,77605738301620224)
    assert rr['s87']==F(29597133147954427,41779200000000000)
    assert F()<m.S<rr['s87']<1
    assert rr['alpha87']==F(5172378789334355543,14900301753911083008)
    assert rr['V87']==F(24313783684225133729,1862537719238885376)
    assert rr['nxt']==(F(483272799336,245952751),(6,4,0),'C','P') and not rr['errs']
    # The B count state cannot reach A at the next depth, so cones are disjoint: this proves the product term in (u,s) is identically zero.
    assert m.A[0]>m.B[0] and m.A[1]>m.B[1]+(m.A[0]-m.B[0])
    assert rr['eta']==-rr['X']+rr['E']*rr['h']==rr['Y']-rr['H']*rr['h']
    for u in [F(),F(1,101),F(1,7),F(2,5),F(1,2),F(7,9),F(100,101),F(1)]:
        s=m.S+rr['h']*u
        ep,eq,tp,tq=m.forward(u,s)
        assert ep==eq==m.alpha0+rr['eta']*u
        assert tp==m.V0-m.G*rr['eta']*u
        assert tp>tq
        assert tp+m.LP*ep+m.LQ*eq==rr['root']
    assert rr['f0'][2]>rr['f0'][3] and rr['f1'][2]>rr['f1'][3]
    print(json.dumps({
      'status':'PASS_EXACT_ORDERED_DFS_AND_ENDPOINTS_SHARED_PREDECESSOR_POLICY',
      'first_hit_and_suffix':obs,
      'Bellman_ties':str(rr['ties']),
      'minimum_positive_gap':str(rr['gap']),
      'tP_minus_tQ_start':str(rr['f0'][2]-rr['f0'][3]),
      'tP_minus_tQ_end':str(rr['f1'][2]-rr['f1'][3]),
      'h87':str(rr['h']), 'eta87':str(rr['eta']),
      'alpha87':str(rr['alpha87']),'V87':str(rr['V87']),
      'candidate_next_K88':str(rr['nxt'][0]),
      'candidate_next_action':str(rr['nxt'][1:]),
    },indent=2))
if __name__=='__main__':main()
