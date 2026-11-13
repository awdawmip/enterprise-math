#!/usr/bin/env python3
"""EC49B: exact four-stage BRC auxiliary observation counterexample and LR-spectrum sufficiency.
All arithmetic Fraction; no numerical tolerance, no external dependencies.
"""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

H = (0, 1); Z = (0, 1); W = (0, 1); V = (0, 1)
A = ('acc', 'rej', 'cont')
PZ = {0:F(1,4), 1:F(3,4)}
QZ = {0:F(3,4), 1:F(1,4)}
KW = {0:{0:F(3,4),1:F(1,4)}, 1:{0:F(1,4),1:F(3,4)}}
# Counterexample: marginals V | H under P and Q coincide across H,
# even though (W,V) interacts with H and W predicts continuation value.
PV = {0:{0:{0:F(7,24),1:F(17,24)},1:{0:F(1,8),1:F(7,8)}},
      1:{0:{0:F(5,8),1:F(3,8)},1:{0:F(1,8),1:F(7,8)}}}
QV = {0:{0:{0:F(17,24),1:F(7,24)},1:{0:F(7,8),1:F(1,8)}},
      1:{0:{0:F(3,8),1:F(5,8)},1:{0:F(7,8),1:F(1,8)}}}
# Sufficiency example: same Q-LR spectrum but different V outcome labels by W.
PS = {w:{0:(F(1,4) if w==0 else F(3,4)),1:(F(3,4) if w==0 else F(1,4))} for w in W}
QS = {w:{0:(F(3,4) if w==0 else F(1,4)),1:(F(1,4) if w==0 else F(3,4))} for w in W}
C = F(1,16)

def leaves(pv,qv, by_h=True):
    out=[]
    for h,z,w,v in product(H,Z,W,V):
        pp=pv[h][w][v] if by_h else pv[w][v]
        qq=qv[h][w][v] if by_h else qv[w][v]
        p=F(1,2)*PZ[z]*KW[h][w]*pp
        q=F(1,2)*QZ[z]*KW[h][w]*qq
        out.append({'h':h,'z':z,'w':w,'v':v,'P':p,'Q':q,'LR':p/q})
    assert len(out)==16 and all(x['P']>0 and x['Q']>0 for x in out)
    assert sum((x['P'] for x in out),F(0))==1
    assert sum((x['Q'] for x in out),F(0))==1
    return out

def basis_simplex(action): return {a:F(int(a==action)) for a in A}

def random_simplex(rng):
    cuts=sorted([0,rng.randrange(17),rng.randrange(17),16])
    return {a:F(cuts[i+1]-cuts[i],16) for i,a in enumerate(A)}

def direct(pi1,pi2,pi3,pi4, model, coarse=False):
    """pi4(z,w,v,h,p/q) returns terminal accept prob, respecting stated readout."""
    alpha=beta=F(0)
    eP=eQ=F(1)
    for h in H:
        a1=pi1[h]
        alpha+=F(1,2)*a1['acc'];beta+=F(1,2)*a1['acc']
        eP+=F(1,2)*a1['cont'];eQ+=F(1,2)*a1['cont']
        alpha+=F(1,2)*a1['cont']*pi2['acc'];beta+=F(1,2)*a1['cont']*pi2['acc']
        eP+=F(1,2)*a1['cont']*pi2['cont'];eQ+=F(1,2)*a1['cont']*pi2['cont']
        for z,w in product(Z,W):
            bp=F(1,2)*a1['cont']*pi2['cont']*PZ[z]*KW[h][w]
            bq=F(1,2)*a1['cont']*pi2['cont']*QZ[z]*KW[h][w]
            a3=pi3[z] if coarse else pi3[z,w]
            alpha+=bp*a3['acc'];beta+=bq*a3['acc']
            eP+=bp*a3['cont'];eQ+=bq*a3['cont']
            for v in V:
                if model=='counter':
                    cp=PV[h][w][v]; cq=QV[h][w][v]
                else:
                    cp=PS[w][v]; cq=QS[w][v]
                lr=PZ[z]*cp/(QZ[z]*cq)
                a4=pi4(z,w,v,h,lr)
                alpha+=bp*a3['cont']*cp*a4
                beta+=bq*a3['cont']*cq*a4
    return alpha,beta,eP,eQ

def support(o): return o[0]-o[1]-C*(o[2]+o[3])

def exhaustive():
    best={False:(F(-1000),None,None),True:(F(-1000),None,None)}
    tested={False:0,True:0}
    def accept_terminal(z,w,v,h,lr): return F(int(lr>1))
    for coarse in (True,False):
        obs = Z if coarse else tuple(product(Z,W))
        for choices in product(A, repeat=3+len(obs)):
            p1={h:basis_simplex(choices[h]) for h in H}
            p2=basis_simplex(choices[2])
            p3={obs[i]:basis_simplex(choices[3+i]) for i in range(len(obs))}
            o=direct(p1,p2,p3,accept_terminal,'counter',coarse)
            s=support(o)
            if s>best[coarse][0]: best[coarse]=(s,choices,o)
            tested[coarse]+=1
    assert tested[True]==243 and tested[False]==2187
    assert best[True][0]==F(1,8),best[True]
    assert best[False][0]==F(3,16),best[False]
    return {'coarse':{'value':str(best[True][0]),'argmax':best[True][1], 'vector':[str(x) for x in best[True][2]]},
            'refined':{'value':str(best[False][0]),'argmax':best[False][1], 'vector':[str(x) for x in best[False][2]]},
            'policy_counts':{'coarse':tested[True],'refined':tested[False]}}

def analytic_table():
    out=[]
    for tup in ((),(0,),(1,),(0,1)):
        wt={w:sum((F(1,2)*KW[h][w] for h in tup),F(0)) for w in W}
        def d(z,w):return wt[w]*(PZ[z]-QZ[z])
        def g(z,w):
            profit=sum((max(F(0),F(1,2)*KW[h][w]*(PZ[z]*PV[h][w][v]-QZ[z]*QV[h][w][v])) for h in tup for v in V),F(0))
            return profit-C*wt[w]*(PZ[z]+QZ[z])
        base=-2*C-2*C*len(tup)
        fine=base+sum((max(F(0),d(z,w),g(z,w)) for z,w in product(Z,W)),F(0))
        coarse=base+sum((max(F(0),sum((d(z,w) for w in W),F(0)),sum((g(z,w) for w in W),F(0))) for z in Z),F(0))
        out.append({'H_survives':list(tup),'coarse':str(coarse),'refined':str(fine)})
    assert [F(x['coarse']) for x in out]==[F(-1,8),F(0),F(1,32),F(1,8)]
    assert [F(x['refined']) for x in out]==[F(-1,8),F(1,64),F(3,64),F(3,16)]
    return out

def random_terminal_policy(rng):
    # Valid terminal action maps are keyed by the *actual* readout (z,v,full LR).
    m={}
    for z,w,v in product(Z,W,V):
        r=PS[w][v]/QS[w][v]
        m[z,v,(PZ[z]/QZ[z])*r]=F(rng.randrange(17),16)
    return m

def sufficiency_checks():
    for w in W:
        sr={}
        for v in V:
            lr=PS[w][v]/QS[w][v]
            sr[lr]=sr.get(lr,F(0))+QS[w][v]
        assert sr=={F(1,3):F(3,4),F(3):F(1,4)}
    assert PS[0]!=PS[1] and QS[0]!=QS[1]  # raw future law differs by W
    rng=Random(4902)
    checks=0
    for _ in range(800):
        p1={h:random_simplex(rng) for h in H}
        p2=random_simplex(rng)
        p3={(z,w):random_simplex(rng) for z,w in product(Z,W)}
        p4=random_terminal_policy(rng)
        def fine4(z,w,v,h,lr):return p4[z,v,lr]
        o=direct(p1,p2,p3,fine4,'sufficient')
        x2=sum((F(1,2)*p1[h]['cont'] for h in H),F(0))
        bar3={}
        for z in Z:
            for a in A:
                num=sum((F(1,2)*p1[h]['cont']*KW[h][w]*p3[z,w][a] for h in H for w in W),F(0))
                bar3.setdefault(z,{})[a]=num/x2 if x2 else (F(int(a=='rej')))
            assert sum(bar3[z].values())==1
        bar4={}
        for z in Z:
            for r in (F(1,3),F(3)):
                numerator=F(0); denominator=F(0)
                for h,w,v in product(H,W,V):
                    if PS[w][v]/QS[w][v]!=r: continue
                    qwt=F(1,2)*p1[h]['cont']*p2['cont']*KW[h][w]*p3[z,w]['cont']*QS[w][v]
                    denominator+=qwt
                    numerator+=qwt*p4[z,v,(PZ[z]/QZ[z])*r]
                bar4[z,r]=numerator/denominator if denominator else F(0)
                assert 0<=bar4[z,r]<=1
        def coarse4(z,w,v,h,lr):return bar4[z,lr/(PZ[z]/QZ[z])]
        co=direct(p1,p2,bar3,coarse4,'sufficient',coarse=True)
        assert o==co,(o,co)
        checks+=1
    return {'random_realizations_checked':checks,'conditional_Q_LR_distribution':{'1/3':'3/4','3':'1/4'},'raw_V_kernel_differs':True}

def main():
    counter_leaves=leaves(PV,QV)
    suff_leaves=leaves(PS,QS,by_h=False)
    # Source-neutral W and reachably different conditional W kernels, as in EC49A.
    assert KW[0][1]==F(1,4) and KW[1][1]==F(3,4)
    assert QZ[1]*KW[0][1]==F(1,16) and QZ[1]*KW[1][1]==F(3,16)
    # Genuine causal V information, and V|Z,H marginal equals fixed P and Q laws.
    marg={}
    for h in H:
        marg[h]={s:sum((KW[h][w]*kernel[h][w][1] for w in W),F(0)) for s,kernel in (('P',PV),('Q',QV))}
        assert marg[h]=={'P':F(3,4),'Q':F(1,4)}
    assert any(PV[h][w][v]!=QV[h][w][v] for h,w,v in product(H,W,V))
    opt=exhaustive(); table=analytic_table()
    assert F(opt['refined']['value'])-F(opt['coarse']['value'])==F(1,16)
    def opt4(z,w,v,h,lr):return F(int(lr>1))
    p1={h:basis_simplex('cont') for h in H};p2=basis_simplex('cont')
    p3={(0,0):basis_simplex('rej'),(0,1):basis_simplex('cont'),(1,0):basis_simplex('acc'),(1,1):basis_simplex('cont')}
    witness=direct(p1,p2,p3,opt4,'counter')
    assert witness==(F(13,16),F(3,16),F(7,2),F(7,2)) and support(witness)==F(3,16)
    suff=sufficiency_checks()
    report={
      'schema':'ENTERPRISE_MATH_EC49B_EXACT_REPORT_V1','date':'2026-10-28',
      'result':'PASS','arithmetic':'Python fractions.Fraction, exact rational',
      'counterexample':{
        'leaf_count':len(counter_leaves),'leaf_table':[{k:str(v) for k,v in row.items()} for row in counter_leaves],
        'source_mass_normalized_and_strictly_positive':True,
        'V_given_H_marginals':{str(h):{s:str(x) for s,x in d.items()} for h,d in marg.items()},
        'EC49A_same_Z_W_reachable_Q_kernel_values':['1/16','3/16'],
        'deterministic_policy_enumeration':opt,'analytic_H_subset_table':table,
        'support_function':'alpha-beta-(E_PT+E_QT)/16',
        'gap':'1/16','explicit_refined_witness':[str(x) for x in witness],
        'scope':'one fixed erased-history memory state, four decisions; W observed at t3 only in refined; exact full-history LR at t4; source-neutral behavioral policies'},
      'sufficient_example':{'leaf_count':len(suff_leaves),**suff},
      'proof_scope':'analytic all-real-policy support certificate via multiaffine extreme-point property; sufficiency via Q LR-fiber averaging; finite checks validate examples; no native X6 transfer'
    }
    print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':main()