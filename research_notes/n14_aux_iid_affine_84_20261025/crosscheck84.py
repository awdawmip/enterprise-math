#!/usr/bin/env python3
"""Author-side independent ordered-history DFS and exact endpoint checks.
Shares the previously inherited stopping table with derive83.py: NOT an independent Driver review.
"""
from collections import Counter
from fractions import Fraction as F
from math import factorial
import json
import derive84 as m

def first_hits(target):
    n,a,b=target
    hits=[]
    def walk(path,pp,qq,a0,b0):
        k=len(path);st=(k,a0,b0)
        if st==target:
            hits.append((path,pp,qq)); return
        if k==n or m.act(st)!='C': return
        for i in (0,1,2):
            walk(path+(i,),pp*m.P[i],qq*m.Q[i],a0+(i==0),b0+(i==1))
    walk((),F(1),F(1),0,0)
    return hits

def suffix_words(target):
    endpoints=Counter();totals=[F(),F(),F(),F()]
    def visit(st,pp,qq,nword):
        action=m.act(st)
        if action!='C':
            endpoints[(st,action)]+=1
            if action=='Q':totals[0]+=pp
            else:totals[1]+=qq
            totals[2]+=nword*pp;totals[3]+=nword*qq
            return
        for i in (0,1,2): visit(m.child(st,i),pp*m.P[i],qq*m.Q[i],nword+1)
    visit(target,F(1),F(1),0)
    return endpoints,tuple(totals)

def main():
    observations={}
    for name,st in (('A',m.A),('B',m.B)):
        hits=first_hits(st)
        ends,quad=suffix_words(st)
        pa=sum((p for _,p,q in hits),F());qa=sum((q for _,p,q in hits),F())
        assert (pa,qa,len(hits))==m.firsthit(st)
        assert quad==m.suffix(st)
        assert sum(ends.values())>=1
        assert all(p>0 and q>0 for _,p,q in hits)
        observations[name]={
            "state":str(st),
            "nominal_prefix_count": factorial(st[0])//(factorial(st[1])*factorial(st[2])*factorial(st[0]-st[1]-st[2])),
            "true_first_hit_count":len(hits),
            "P_hit_mass":str(pa),"Q_hit_mass":str(qa),
            "terminal_suffix_words":sum(ends.values()),
            "terminal_decision_state_classes":len(ends),
            "truncated_complete_words":len(hits)*sum(ends.values()),
            "suffix_quadruple":list(map(str,quad))
        }
    r=m.main()
    assert r['ha']==35 and r['hb']==12
    assert r['count']==1240 and r['pos']==1238 and not r['bad']
    assert set(r['ties'])=={(m.A,'C','P'),(m.B,'C','Q')}
    assert 0<m.S<r['s84']<1 and r['eta']>0
    assert r['root']==m.V0+m.G*m.alpha0
    assert r['eta']==-r['X']+r['E']*r['h']==r['Y']-r['H']*r['h']
    assert r['f0'][0]==r['f0'][1]==m.alpha0 and r['f0'][2]==m.V0
    assert r['f1'][0]==r['f1'][1]==r['alpha84'] and r['f1'][2]==r['V84']
    assert r['f0'][2]>r['f0'][3] and r['f1'][2]>r['f1'][3]
    assert r['f1'][2]==m.V0-m.G*r['eta']
    assert r['nxt'][0]<m.K and not r['errs']
    for u in (F(),F(1,97),F(1,7),F(1,2),F(17,23),F(96,97),F(1)):
        ep,eq,tp,tq=m.forward(u,m.S+r['h']*u)
        assert ep==eq==m.alpha0+r['eta']*u
        assert tp==m.V0-m.G*r['eta']*u and tp>tq
        assert tp+m.LP*ep+m.LQ*eq==r['root']
    # An independent proof of the zero mixed coefficient: from A at n=7,a=4;
    # B at n=12,a=0, a is nondecreasing, hence impossible to hit B after A.
    assert m.A[0]<m.B[0] and m.A[1]>m.B[1]
    output={"status":"PASS_AUTHOR_ORDERED_DFS_SHARED_INHERITED_STOP_TABLE","first_hit_suffix_DFS":observations,
            "Bellman_ties":str(r['ties']),"Bellman_min_positive_gap":str(r['gap']),
            "tP_minus_tQ_start":str(r['f0'][2]-r['f0'][3]),
            "tP_minus_tQ_end":str(r['f1'][2]-r['f1'][3]),
            "h84":str(r['h']),"eta84":str(r['eta']),
            "alpha84":str(r['alpha84']),"V84":str(r['V84']),
            "K85_candidate":str(r['nxt'][0]),"A85_candidate":str(r['nxt'][1])}
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
