#!/usr/bin/env python3
"""Exact Fraction certificate: N=4 two-law TV compression, global phases to lambda=1.

Author-side portable mathematical research; proof obligations beyond the finite
certificate are documented in PROOF.md. No native-X6 transfer/admission implied.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json

ZERO, ONE = F(0), F(1)
# Ordered positive BRC Q mass, P/Q likelihood ratio, parent
N = {1: {'A': (F(1,2), F(1,2), None), 'B': (F(1,2), F(3,2), None)},
     2: {'AU': (F(1,6), ONE, 'A'), 'AV': (F(1,3), F(1,4), 'A'),
         'BU': (F(1,4), ONE, 'B'), 'BV': (F(1,4), F(2), 'B')}}
for t in (3,4):
    N[t] = {}
    for pa, (q,r,_) in N[t-1].items():
        eps = ({'AU':F(1,10),'AV':ZERO,'BU':F(4,5),'BV':ZERO}[pa]
               if t==3 else ZERO if pa=='AV0' else F(3,50) if pa=='AV1' else F(1,20))
        for i,sgn in enumerate((-1,1)):
            N[t][pa+str(i)] = (q/2, r*(1+sgn*eps), pa)
for t,lev in N.items():
    assert len(lev)==2**t and all(q>0 and r>0 for q,r,_ in lev.values())
    assert sum((q for q,r,_ in lev.values()),ZERO)==1
    assert sum((q*r for q,r,_ in lev.values()),ZERO)==1
    if t<4:
        for h,(q,r,_) in lev.items():
            ch=[(qc,rc) for h2,(qc,rc,pa) in N[t+1].items() if pa==h]
            assert len(ch)==2 and sum(z for z,rr in ch)==q
            assert sum(z*rr for z,rr in ch)==q*r

groups={t:defaultdict(list) for t in (2,3,4)}
for t in groups:
    for h,(q,r,pa) in N[t].items(): groups[t][r].append(h)
assert tuple(len(groups[t]) for t in groups)==(3,6,13)
# For every LR fiber all member histories share their parent (time,LR)
# signature, so their upstream reach-survival is equal when t1=C.
for t in (3,4):
    for r, hs in groups[t].items():
        assert len({N[t-1][N[t][h][2]][1] for h in hs})==1
keys=[]
for t in groups:
    for r in groups[t]:
        for d in ((0,1,2) if t<4 else (0,1)): keys.append((t,r,d))
assert len(keys)==53

def X(data):
    # Compact exact mass-flow ledger: nonzero signatures only, no global seed.
    x={k:ZERO for k in keys}
    for t,rr,letter,value in data:
        key=(t,F(rr),{'P':0,'Q':1,'C':2}[letter])
        assert key in x and x[key]==ZERO and F(value)>0
        x[key]=F(value)
    return x

L0=F(27483,39215)
LC=F(11526,16445)
L2=F(89,125)
END=ONE
assert L0<LC<L2<END and LC-L0==F(27,509795)

endpoint={
L0:X([
(2,'1/4','P','2/253'),(2,'1/4','C','251/253'),(2,'1','P','498/1265'),(2,'1','C','767/1265'),(2,'2','P','1'),
(3,'1/5','C','767/1265'),(3,'1/4','C','251/253'),(3,'9/10','Q','767/1265'),(3,'11/10','Q','767/1265'),
(3,'9/5','Q','4755/7843'),(3,'9/5','C','2/39215'),
(4,'19/100','Q','767/1265'),(4,'21/100','Q','767/1265'),(4,'47/200','Q','251/253'),
(4,'1/4','P','307/78430'),(4,'1/4','Q','77503/78430'),(4,'53/200','P','251/253'),
(4,'171/100','P','2/39215'),(4,'189/100','P','2/39215')]),
LC:X([
(2,'1/4','P','2/253'),(2,'1/4','C','251/253'),(2,'1','P','498/1265'),(2,'1','C','767/1265'),(2,'2','P','1'),
(3,'1/5','C','767/1265'),(3,'1/4','C','251/253'),(3,'9/10','Q','9968/16445'),(3,'9/10','C','3/16445'),
(3,'11/10','Q','767/1265'),(3,'9/5','Q','767/1265'),
(4,'19/100','Q','767/1265'),(4,'21/100','Q','767/1265'),(4,'47/200','Q','251/253'),
(4,'1/4','P','127/32890'),(4,'1/4','Q','32503/32890'),(4,'53/200','P','251/253'),
(4,'171/200','P','3/16445'),(4,'189/200','P','3/16445')]),
L2:X([
(2,'1/4','C','1'),(2,'1','P','2/5'),(2,'1','C','3/5'),(2,'2','P','1'),
(3,'1/5','C','3/5'),(3,'1/4','C','1'),(3,'9/10','Q','3/5'),(3,'11/10','Q','3/5'),(3,'9/5','Q','3/5'),
(4,'19/100','Q','3/5'),(4,'21/100','Q','3/5'),(4,'47/200','Q','1'),(4,'1/4','Q','1'),(4,'53/200','P','1')]),
END:X([
(2,'1/4','C','1'),(2,'1','P','2/5'),(2,'1','C','3/5'),(2,'2','P','1'),
(3,'1/5','C','3/5'),(3,'1/4','C','1'),(3,'9/10','Q','21/95'),(3,'9/10','C','36/95'),
(3,'11/10','Q','3/5'),(3,'9/5','Q','3/5'),
(4,'19/100','P','3/5'),(4,'21/100','Q','3/5'),(4,'47/200','P','1163/2480'),(4,'47/200','Q','1317/2480'),
(4,'1/4','Q','1'),(4,'53/200','Q','1'),
(4,'171/200','P','201/1240'),(4,'171/200','Q','5109/23560'),(4,'189/200','Q','36/95')])
}

def check_flow(x):
    assert set(x)==set(keys) and all(v>=0 for v in x.values())
    for t in groups:
        for r,hs in groups[t].items():
            lhs=sum((x[t,r,d] for d in ((0,1,2) if t<4 else (0,1))),ZERO)
            if t==2: expected=ONE
            else:
                prs={N[t-1][N[t][h][2]][1] for h in hs}
                assert len(prs)==1
                expected=x[t-1,prs.pop(),2]
            assert lhs==expected,(t,r,lhs,expected)

def observations(x):
    out=[ZERO]*16
    for t in groups:
        for r,hs in groups[t].items():
            q=sum((N[t][h][0] for h in hs),ZERO)
            for d in (0,1):
                j=2*(t-1)+d
                out[j]+=q*x[t,r,d]
                out[8+j]+=q*r*x[t,r,d]
    assert sum(out[:8])==sum(out[8:])==1
    return out

def target(lam):
    return [ZERO,ZERO,F(5,12),ZERO,ZERO,F(7,24)-lam/6,F(1,12),F(5,24)+lam/6,
            ZERO,ZERO,F(2,3),ZERO,ZERO,F(4,15)-lam/24,F(53,2400),F(107,2400)+lam/24]

def tvs(vec,ref):
    return (sum((abs(vec[i]-ref[i]) for i in range(8)),ZERO)/2,
            sum((abs(vec[8+i]-ref[8+i]) for i in range(8)),ZERO)/2)

# Independent full-tree evaluation of the full-history F_lambda.
def full_history(lam,t,h,r):
    if t==1:return (ZERO,ZERO,ONE)
    if t==2:return {'AU':(ONE,ZERO,ZERO),'AV':(ZERO,ZERO,ONE),
                    'BU':(ZERO,ZERO,ONE),'BV':(ONE,ZERO,ZERO)}[h]
    if t==3:
        if h=='AV0':return ZERO,1-lam,lam
        return {'AV1':(ZERO,ZERO,ONE),'BU0':(ZERO,ZERO,ONE),
                'BU1':(ZERO,ONE,ZERO)}.get(h,(ONE,ZERO,ZERO))
    return ((ZERO,ONE,ZERO) if 100*r<F(2501,100) else (ONE,ZERO,ZERO))

def original_outcome(lam):
    out=[ZERO]*16
    for leaf,(q,rr4,_) in N[4].items():
        alive=ONE
        for t,h in enumerate((leaf[:1],leaf[:2],leaf[:3],leaf),1):
            ap,aq,ac=full_history(lam,t,h,N[t][h][1])
            assert ap>=0 and aq>=0 and ac>=0 and ap+aq+ac==1
            i=2*(t-1)
            out[i]+=q*alive*ap;out[i+1]+=q*alive*aq
            out[8+i]+=q*rr4*alive*ap;out[8+i+1]+=q*rr4*alive*aq
            alive*=ac
        assert alive==0
    return out

# Three exact duals, each valid even for the larger S2 class.
w0q=list(map(F,['0','0','25/253','0','3/2024','25/253','25/253','-25/253']))
w0p=list(map(F,['0','0','-203/506','0','0','-197/506','-197/506','203/506']))
w1q=list(map(F,['0','0','292/3265','961/9142','961/9142','961/9142','799/9142','-961/9142']))
w1p=list(map(F,['0','0','-1805/4571','1805/4571','1805/4571','-1805/4571','-245/653','1805/4571']))
w2q=list(map(F,['0','0','3/190','9/38','9/38','9/38','-9/38','-9/38']))
w2p=list(map(F,['0','0','-29/190','5/19','5/19','-5/19','5/19','5/19']))

def bellman_S2(wq,wp):
    # S2: only t2 AU and BU must share a P/Q/C decision; t3 unrestricted.
    # Deterministic t1,t2 signatures suffice for linear objectives by
    # multi-affinity in the independent behavioral action probabilities.
    def c(t,r,d):return wq[2*(t-1)+d]+r*wp[2*(t-1)+d]
    t3={}
    for h,(q,r,_) in N[3].items():
        next_cost=sum((qc/q*min(c(4,rr,0),c(4,rr,1)) for hh,(qc,rr,pa) in N[4].items() if pa==h),ZERO)
        t3[h]=(c(3,r,0),c(3,r,1),next_cost)
    best=None;count=0
    for first in product(range(3),repeat=2):
        a1=dict(zip(('A','B'),first))
        for second in product(range(3),repeat=3):
            count+=1
            a2=dict(zip(('U','AV','BV'),second));val=ZERO
            for h,(q,r,_) in N[1].items():
                if a1[h]!=2:val+=q*c(1,r,a1[h])
            for h,(q,r,pa) in N[2].items():
                if a1[pa]!=2:continue
                d=a2['U' if h in ('AU','BU') else h]
                if d!=2:val+=q*c(2,r,d)
                else:
                    for h3,(q3,r3,pa3) in N[3].items():
                        if pa3==h:val+=q3*min(t3[h3])
            if best is None or val<best: best=val
    assert count==243
    return best,count

weights=[(w0q,w0p,-F(153,506)),(w1q,w1p,-F(6981,22855)),(w2q,w2p,-F(85,456))]
for wq,wp,expected in weights:
    assert max(wq)-min(wq)+max(wp)-min(wp)==1
    assert bellman_S2(wq,wp)==(expected,243)
score=lambda idx,lam:sum((wi*vi for wi,vi in zip(weights[idx][0]+weights[idx][1],target(lam))),ZERO)
assert score(0,ZERO)==score(0,ONE)==-F(154,506)
assert score(1,ZERO)==-F(6992,22855)
assert score(1,ONE)-score(1,ZERO)==-F(39,18284)
assert score(2,ZERO)==-F(337,2280)
assert score(2,ONE)-score(2,ZERO)==-F(13,228)

floors=[lambda l:F(1,506),lambda l:F(11,22855)+F(39,18284)*l,
        lambda l:F(13,228)*l-F(11,285)]
assert floors[0](LC)==floors[1](LC)
assert floors[1](L2)==floors[2](L2)==F(1,500)

records={}
for lam,x in endpoint.items():
    check_flow(x)
    assert original_outcome(lam)==target(lam)
    out=observations(x)
    tvq,tvp=tvs(out,target(lam))
    expected=(floors[0](lam) if lam<=LC else floors[1](lam) if lam<=L2 else floors[2](lam))
    assert tvq==tvp==expected,(lam,tvq,tvp,expected)
    dual=[weights[k][2]-score(k,lam) for k in range(3)]
    assert max(dual)==expected and all(x<=expected for x in dual)
    records[str(lam)]={
        'law_tv':[str(tvq),str(tvp)],
        'dual_lower_bounds':list(map(str,dual)),
        'nonzero_occupancy_entries':sum(1 for v in x.values() if v),
        'signed_Q_residual':list(map(str,(out[i]-target(lam)[i] for i in range(8)))),
        'signed_P_residual':list(map(str,(out[8+i]-target(lam)[8+i] for i in range(8))))
    }

# Two independent rational probes in each open phase. Occupancy mixtures
# are genuine shared (t,LR) behavioral policies, not global randomized seeds.
probes={
    'extended-flat':(L0,LC,lambda l:floors[0](l)),
    'rising-first':(LC,L2,lambda l:floors[1](l)),
    'rising-second':(L2,END,lambda l:floors[2](l))
}
for title,(left,right,fun) in probes.items():
    for alpha in (F(1,3),F(2,3)):
        lam=(1-alpha)*left+alpha*right
        x={k:(1-alpha)*endpoint[left][k]+alpha*endpoint[right][k] for k in keys}
        check_flow(x)
        assert original_outcome(lam)==target(lam)
        q,p=tvs(observations(x),target(lam))
        assert max(q,p)<=fun(lam)
        assert max(weights[j][2]-score(j,lam) for j in range(3))==fun(lam)

out={
 'status':'PASS_EXACT_FRACTION_N4_COMPLETE_POST_FLAT_PHASES',
 'global_knowledge_pin':'30a0b3ec845e08a9d5d2ea2bd179c27735398ee2',
 'enterprise_math_input_pin':'d2c0c9157cc89f1c08c9db7c321b4c4702278703',
 'scope':'frozen positive finite N4 two-law tree, F_lambda, S2 and S23 with independent shared (time,LR) behavior; 0<=lambda<=1',
 'new_interval':[str(L0),'1'],
 'true_first_post_flat_switch':str(LC),
 'preceding_witness_boundary':str(L0),
 'phase2_breakpoint':str(L2),
 'piecewise_d2_equals_d23':[
   {'lambda':[str(L0),str(LC)],'value':'1/506'},
   {'lambda':[str(LC),str(L2)],'value':'11/22855+39*lambda/18284'},
   {'lambda':[str(L2),'1'],'value':'13*lambda/228-11/285'}
 ],
 'prior_d3':'(1-lambda)/2000 on [0,1] per prior independent theorem',
 'strict_subadditivity_on_new_range':'(1-lambda)/2000 positive for lambda<1; zero at lambda=1',
 'model_positive_mass_conservation':'PASS',
 'observer_compression_typed_flow':'53 group occupancy variables, 3/6/13 LR fibers at t2/t3/t4',
 'finite_S2_Bellman_prefix_cases_each':243,
 'verified_dual_minima':list(map(str,(v[2] for v in weights))),
 'dual_total_oscillations':['1','1','1'],
 'rational_endpoint_evidence':records,
 'interior_fraction_probes_per_phase':2,
 'universal_real_lambda_argument':'Exact convex occupancy-flow interpolation plus affine F_lambda targets, convex TV, and globally valid S2 Bellman duals',
 'author_status':'AUTHOR_SIDE_EXACT_DERIVATION_UNREVIEWED_NOT_ADMITTED',
 'native_bridge':'P000 X6 future-operation fidelity not established',
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
