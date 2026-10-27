#!/usr/bin/env python3
"""Exact author-level verifier of the N=2 LR-fiber occupancy polytope witness.

External two-measure finite rational tree. Standard-library fractions only.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json

D = ('P', 'Q')
A = ('C', 'P', 'Q')
ZERO, ONE = F(0), F(1)
Q1 = {'a':F(1,3), 'b':F(2,3)}
P1 = {'a':F(2,3), 'b':F(1,3)}
Q2 = {'ax':F(1,6),'ay':F(1,6),'bx':F(4,9),'by':F(2,9)}
P2 = {'ax':F(1,6),'ay':F(1,2),'bx':F(1,9),'by':F(2,9)}
S = ('2','1/2')
Z = ('1/4','1','3')
L1 = {'a':'2','b':'1/2'}
L2 = {'ax':'1','ay':'3','bx':'1/4','by':'1'}
L2_val = {z:F(z) for z in Z}

def det_action(a):
    return {k:(ONE if k==a else ZERO) for k in A}

def prob_action(c=0,p=0,q=0):
    ans={'C':F(c),'P':F(p),'Q':F(q)}
    assert all(v>=0 for v in ans.values()) and sum(ans.values())==1
    return ans

def policy(root, t1, t2):
    assert set(t1)==set(S) and set(t2)==set(Z)
    assert sum(root.values())==1 and all(sum(x.values())==1 for x in t1.values())
    assert all(ZERO<=v<=ONE for v in t2.values())
    return {'root':root,'t1':t1,'t2':t2}

def Y(pol):
    y={(m,t,d):ZERO for m in ('P','Q') for t in (0,1,2) for d in D}
    for m in ('P','Q'):
        at1=P1 if m=='P' else Q1
        at2=P2 if m=='P' else Q2
        for d in D:
            y[m,0,d]=pol['root'][d]
        r=pol['root']['C']
        for h,w in at1.items():
            s=L1[h]; ac=pol['t1'][s]
            for d in D:
                y[m,1,d]+=r*w*ac[d]
            for leaf,v in at2.items():
                if not leaf.startswith(h): continue
                z=L2[leaf]
                y[m,2,'Q']+=r*ac['C']*v*pol['t2'][z]
                y[m,2,'P']+=r*ac['C']*v*(1-pol['t2'][z])
        assert sum(y[m,t,d] for t in (0,1,2) for d in D)==ONE
    return y

def O(y):
    return (sum(y['P',t,'Q'] for t in (0,1,2)),
            sum(y['Q',t,'P'] for t in (0,1,2)),
            sum(t*y['P',t,d] for t in (0,1,2) for d in D),
            sum(t*y['Q',t,d] for t in (0,1,2) for d in D))

K={ (s,z):sum(v for leaf,v in Q2.items() if L1[leaf[0]]==s and L2[leaf]==z)
    for s in S for z in Z }

def flows(pol):
    r=pol['root']['C']
    c={s:r*pol['t1'][s]['C'] for s in S}
    zs={(s,d):r*pol['t1'][s][d] for s in S for d in D}
    arrived={z:sum((c[s]*K[s,z] for s in S),ZERO) for z in Z}
    v={(z,d):arrived[z]*((pol['t2'][z]) if d=='Q' else (1-pol['t2'][z])) for z in Z for d in D}
    return {'r':r,'root':{d:pol['root'][d] for d in D},'c':c,'z':zs,'arrived':arrived,'v':v}

def mix(a,b,lam):
    va,vb=flows(a),flows(b)
    r=lam*va['r']+(1-lam)*vb['r']
    root={d:lam*va['root'][d]+(1-lam)*vb['root'][d] for d in D}
    c={s:lam*va['c'][s]+(1-lam)*vb['c'][s] for s in S}
    z={(s,d):lam*va['z'][s,d]+(1-lam)*vb['z'][s,d] for s in S for d in D}
    arrived={l:lam*va['arrived'][l]+(1-lam)*vb['arrived'][l] for l in Z}
    v={(l,d):lam*va['v'][l,d]+(1-lam)*vb['v'][l,d] for l in Z for d in D}
    assert root['P']+root['Q']+r==1
    assert all(c[s]+z[s,'P']+z[s,'Q']==r for s in S)
    assert all(arrived[l]==sum((c[s]*K[s,l] for s in S),ZERO) for l in Z)
    assert all(v[l,'P']+v[l,'Q']==arrived[l] for l in Z)
    out=policy(prob_action(r,root['P'],root['Q']),
               {s:prob_action(c[s]/r,z[s,'P']/r,z[s,'Q']/r) if r else det_action('P') for s in S},
               {l:v[l,'Q']/arrived[l] if arrived[l] else ZERO for l in Z})
    ya,yb,yo=Y(a),Y(b),Y(out)
    assert all(yo[k]==lam*ya[k]+(1-lam)*yb[k] for k in ya)
    return out

def serialize(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {str(k):serialize(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)): return [serialize(x) for x in v]
    return v

if __name__=='__main__':
    for h in Q1:
        assert Q1[h]>0 and P1[h]>0
    assert sum(Q1.values())==sum(P1.values())==ONE
    for h in Q2:
        assert Q2[h]>0 and P2[h]>0
        assert F(L2[h])==P2[h]/Q2[h]
    assert sum(Q2.values())==sum(P2.values())==ONE
    assert all(sum(v for h,v in Q2.items() if h[0]==a)==Q1[a] for a in Q1)
    assert all(sum(v for h,v in P2.items() if h[0]==a)==P1[a] for a in P1)
    assert all(F(L1[h])==P1[h]/Q1[h] for h in Q1)
    assert K['2','1']>0 and K['1/2','1']>0
    assert all(sum(K[s,z] for z in Z)==sum(v for h,v in Q1.items() if L1[h]==s) for s in S)
    # Pair of explicitly randomized policies; root and two upstream states differ.
    pa=policy(prob_action(F(3,4),0,F(1,4)),
              {'2':prob_action(F(3,4),0,F(1,4)), '1/2':prob_action(F(1,4),F(3,4),0)},
              {'1/4':F(1,3),'1':ONE,'3':F(1,4)})
    pb=policy(prob_action(F(1,2),F(1,2),0),
              {'2':prob_action(F(1,4),F(3,4),0),'1/2':prob_action(F(3,4),0,F(1,4))},
              {'1/4':ONE,'1':ZERO,'3':F(3,4)})
    lam=F(2,5)
    pc=mix(pa,pb,lam)
    ya,yb,yc=Y(pa),Y(pb),Y(pc)
    assert all(yc[k]==lam*ya[k]+(1-lam)*yb[k] for k in ya)
    strategies=[]
    for ar,aa,ab,d0,d1,d3 in product(A,A,A,(ZERO,ONE),(ZERO,ONE),(ZERO,ONE)):
        strategies.append(policy(det_action(ar),{'2':det_action(aa),'1/2':det_action(ab)},
                                 {'1/4':d0,'1':d1,'3':d3}))
    assert len(strategies)==216
    tested=0
    for i,p in enumerate(strategies):
        # 12 different mates per deterministic strategy; exact 3 mixture weights.
        for off in range(12):
            q=strategies[(i*19+off*37+11)%len(strategies)]
            for alpha in (F(1,2), F(2,5),F(7,11)):
                mix(p,q,alpha);tested+=1
    result={
        'schema':'EM_R5T11_N2_LR_TERMINAL_POLYTOPE_V1',
        'status':'EXACT_FRACTION_PASS',
        'model':{'P_t1':P1,'Q_t1':Q1,'P_t2':P2,'Q_t2':Q2,'t1_LR':L1,'t2_LR':L2,
                 'Q_transition_kernel':{f'{s} -> {z}':K[s,z] for s in S for z in Z}},
        'terminal_fiber_collision':['ax','by'],
        'test':{'lambda':lam,'O_A':O(ya),'O_B':O(yb),
                'O_expected_mixture':tuple(lam*a+(1-lam)*b for a,b in zip(O(ya),O(yb))),
                'O_constructed':O(yc),'constructed_policy':pc,
                'full_two_law_time_decision_image':{f'{m},{t},{d}':v for (m,t,d),v in yc.items()}},
        'deterministic_policies':len(strategies),
        'verified_rational_policy_pair_mixtures':tested,
        'proof_scope':'The all-real finite-model theorem is algebraic. These tests verify only specified finite rational instances.',
        'upstream_fiber_strong_lumpability_required':False,
        'no_native_X6_or_P000_transfer':True
    }
    print(json.dumps(serialize(result),indent=2,ensure_ascii=False,sort_keys=True))
