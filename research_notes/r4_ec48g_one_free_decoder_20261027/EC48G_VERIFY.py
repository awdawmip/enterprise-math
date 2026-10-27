#!/usr/bin/env python3
"""EC48G exact rational verification of 1-free-decoder and <=2 tied histories constructions.
Author-side auxiliary positive BRC observer model, no native-X6 physical claim.
Requires only Python standard library; no randomness or float arithmetic.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import json

S = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]

def model(P,Q):
    H=len(P); Y=len(P[0]); assert H>0 and Y>0 and len(Q)==H
    assert all(len(r)==Y and all(type(a)==int and a>0 for a in r) for r in P+Q)
    ps=sum(map(sum,P));qs=sum(map(sum,Q))
    p=[[F(a,ps) for a in r] for r in P]
    q=[[F(a,qs) for a in r] for r in Q]
    return H,Y,p,q

def bits_of(r,p,q):
    H=len(p);Y=len(p[0]);
    return tuple(tuple(int(p[h][y]>r*q[h][y]) for y in range(Y)) for h in range(H))

def hull_size(p,q):
    vals=sorted({p[h][y]/q[h][y] for h in range(len(p)) for y in range(len(p[0]))})
    probes=[vals[0]/2]+[(a+b)/2 for a,b in zip(vals,vals[1:])]+[vals[-1]+1]
    return max(len(set(bits_of(z,p,q))) for z in probes),vals

def crit(r,p,q):
    H=len(p);Y=len(p[0]);h_t=[h for h in range(H) if any(p[h][y]==r*q[h][y] for y in range(Y))]
    non=[h for h in range(H) if h not in h_t]
    C={bits_of(r,p,q)[h] for h in non}
    a={h:tuple(int(p[h][y]>=r*q[h][y]) for y in range(Y)) for h in h_t}
    b={h:tuple(int(p[h][y]>r*q[h][y]) for y in range(Y)) for h in h_t}
    return non,h_t,C,a,b

def interpol(a,b,s):
    return tuple((1-s)*F(x)+s*F(y) for x,y in zip(a,b))

def build_one_free(non,tied,C,a,b,Y):
    """List of (stage, interpolation variable, decoder rows, stochastic encoder maps).
    Each consecutive stage is continuous in its scalar parameter.
    The free decoder moves between b* and a* only while unused.
    """
    C=sorted(C);cidx={x:i for i,x in enumerate(C)}
    a_out={a[h] for h in tied if a[h] not in cidx};b_out={b[h] for h in tied if b[h] not in cidx}
    assert len(a_out)<=1 and len(b_out)<=1
    a_star=next(iter(a_out),None);b_star=next(iter(b_out),None)
    free=len(C) if a_out or b_out else None
    def decoders(u):
        return tuple(tuple(F(i) for i in v) for v in C)+( (tuple(F(x) for x in u),) if free is not None else () )
    def distribution(word):
        return {cidx[word]:F(1)} if word in cidx else {free:F(1)}
    def combine(d1,d2,s):
        d={}
        for i,v in d1.items():d[i]=d.get(i,F(0))+(1-s)*v
        for i,v in d2.items():d[i]=d.get(i,F(0))+s*v
        return {i:v for i,v in d.items() if v}
    # Caller sets all non-tied encoders separately, since c(h) depends on threshold.
    base={h:distribution(b[h]) for h in tied}
    ans=[]
    def snapshot(label,t,u,enc):
        ans.append((label,str(t),decoders(u),{h:dict(d) for h,d in enc.items()}))
    # Stage I: those with an available C endpoint finish, one at a time.
    if b_star is not None: u=b_star
    elif a_star is not None: u=a_star
    else: u=tuple(F(0) for _ in range(Y))
    enc={h:dict(v) for h,v in base.items()}
    for h in [h for h in tied if a[h] in cidx]:
        left=distribution(b[h]);right=distribution(a[h])
        for t in S:
            enc[h]=combine(left,right,t); snapshot(f'I-h{h}',t,u,enc)
        enc[h]=right
    # Stage II: all both-outside pairs share identical b* and a* and can ride the free row.
    both=[h for h in tied if a[h] not in cidx and b[h] not in cidx]
    if a_star is not None and b_star is not None:
        for t in S:
            u=interpol(b_star,a_star,t)
            for h in both: enc[h]={free:F(1)}
            snapshot('II-shared-free',t,u,enc)
    if a_star is not None: u=a_star
    # Stage III: previously C-coded histories move to a* via encoders.
    for h in [h for h in tied if a[h] not in cidx and b[h] in cidx]:
        left=distribution(b[h]);right=distribution(a[h])
        for t in S:
            enc[h]=combine(left,right,t);snapshot(f'III-h{h}',t,u,enc)
        enc[h]=right
    if not ans: snapshot('no-change',F(0),u,enc)
    return ans

def build_two_tied(non,tied,C,a,b,Y):
    C=sorted(C);cidx={w:i for i,w in enumerate(C)}
    decoder0=tuple(tuple(F(x) for x in w) for w in C)
    res=[]
    for t in S:
        ds=decoder0+tuple(interpol(b[h],a[h],t) for h in tied)
        enc={h:{len(C)+i:F(1)} for i,h in enumerate(tied)}
        res.append(('private-rows',str(t),ds,enc))
    return res

def check_case(P,Q,verbose=False):
    H,Y,p,q=model(P,Q); K,rs=hull_size(p,q); checks=0;faces=0;max_d=0;double_sigs=0;applicable=True
    summaries=[]
    for r in rs:
        non,tied,C,a,b=crit(r,p,q)
        c=len(C);t=K-c
        aout={a[h] for h in tied if a[h] not in C}
        bout={b[h] for h in tied if b[h] not in C}
        D={(a[h],b[h]) for h in tied if a[h] not in C or b[h] not in C}
        max_d=max(max_d,len(D))
        if len(D)>=2:double_sigs+=1
        if len(aout)<=1 and len(bout)<=1:
            plan=build_one_free(non,tied,C,a,b,Y);route='one_free'
        elif len(tied)<=t:
            plan=build_two_tied(non,tied,C,a,b,Y);route='private_rows'
        else:
            applicable=False
            continue
        fixed={h:tuple(int(p[h][y]>r*q[h][y]) for y in range(Y)) for h in non}
        tied_Q=sum(q[h][y] for h in tied for y in range(Y) if p[h][y]==r*q[h][y]);
        target=sum(max(p[h][y]-r*q[h][y],F(0)) for h in range(H) for y in range(Y))
        prev=None;origin=None;last=None
        for label,tstr,ds,enc in plan:
            assert len(ds)<=K
            actual_enc={h:enc[h] for h in tied}
            for h,w in fixed.items():
                assert w in C
                actual_enc[h]={sorted(C).index(w):F(1)}
            alpha=beta=F(0)
            for h in range(H):
                assert sum(actual_enc[h].values())==1
                for y in range(Y):
                    w=sum(prob*ds[j][y] for j,prob in actual_enc[h].items())
                    assert 0<=w<=1
                    if p[h][y]>r*q[h][y]: assert w==1
                    if p[h][y]<r*q[h][y]: assert w==0
                    alpha+=p[h][y]*w;beta+=q[h][y]*w
                    checks+=1
            assert alpha-r*beta==target
            z=beta-sum(q[h][y] for h in range(H) for y in range(Y) if p[h][y]>r*q[h][y])
            assert F(0)<=z<=tied_Q
            if prev is not None: assert z>=prev,(r,route,label,prev,z)
            if origin is None:origin=z
            prev=z;last=z
        assert origin==0 and last==tied_Q,(r,origin,last,tied_Q,route)
        faces+=1
        if verbose:
            summaries.append({'r':str(r),'C':sorted(C),'a_out':sorted(aout),'b_out':sorted(bout),'D':len(D),'tied':len(tied),'route':route,'Q_r':str(tied_Q),'steps':len(plan)})
    return {'K_hull':K,'faces':faces,'arithmetic_checks':checks,'max_D':max_d,'multi_D_faces':double_sigs,'all_faces_supported':applicable,'summaries':summaries if verbose else []}

def main():
    # A critical face with TWO distinct unabsorbed transition signatures and K_hull=2.
    P=[[4,1],[2,1],[4,2]];Q=[[2,2],[2,2],[2,2]]
    example=check_case(P,Q,True)
    assert example['K_hull']==2 and example['max_D']==2 and example['all_faces_supported']
    P3=[[4,1],[2,1],[4,2],[2,2]]; Q3=[[2,2]]*4
    triple=check_case(P3,Q3,True)
    assert triple['K_hull']==2 and triple['max_D']==3 and triple['all_faces_supported']
    assert any(row['r']=='8/9' and row['D']==3 for row in triple['summaries'])
    all_models=0;eligible=0;checks=0;faces=0;multi=0;triple_sig=0
    # Exhaustive declared integer-input box: both 3x2 and 4x2 matrices;
    # P entries in {1,2,4}, Q entries always 2: 3^6 + 3^8 = 7290.
    for H0 in (3,4):
      for seq in product((1,2,4),repeat=H0*2):
        P0=[list(seq[2*h:2*h+2]) for h in range(H0)]
        Q0=[[2,2] for _ in range(H0)]
        ans=check_case(P0,Q0)
        all_models+=1
        if ans['all_faces_supported']:
            eligible+=1;checks+=ans['arithmetic_checks'];faces+=ans['faces'];multi+=ans['multi_D_faces']
            if ans['max_D']>=3:triple_sig+=1
    report={'schema':'EC48G_EXACT_CHECK_V1','date':'2026-10-27',
        'model':'strict positive separately normalized 2-stage finite BRC source/decision law',
        'arithmetic':'Python fractions.Fraction only, integer input, no floating point',
        'witness':{'P_raw':P,'Q_raw':Q,'P_total':sum(map(sum,P)),'Q_total':sum(map(sum,Q)),
                   'critical_ratio':'6/7','K_hull':2,'K_seed':2,'example_check':example},
        'triple_signature_witness':{'P_raw':P3,'Q_raw':Q3,'P_total':sum(map(sum,P3)),
              'Q_total':sum(map(sum,Q3)),'critical_ratio':'8/9',
              'K_hull':2,'K_seed':2,'example_check':triple},
        'finite_test':{'family':'P entries in {1,2,4} all 3x2 and 4x2 matrices; Q entries all equal 2',
                       'models_tested':all_models,'models_matching_proved_criterion':eligible,
                       'critical_faces_checked':faces,'cell_arithmetic_checks':checks,
                       'faces_with_D_ge_2':multi,'eligible_models_with_max_D_ge_3':triple_sig},
        'proof_scope':'All finite positive models satisfying per-face single-free or enough-private-state conditions; this checker tests finite instances only.',
        'next_problem':'Two-or-more free decoder slots with more tied histories than free slots: certify critical-face reachability or give a rational gap.'}
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
