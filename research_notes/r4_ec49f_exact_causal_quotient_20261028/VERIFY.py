#!/usr/bin/env python3
"""EC49F auxiliary dual-source conditional-kernel quotient checks.

Only standard-library Fraction arithmetic; no native signed BRC or X6 simulation.
Run: python VERIFY.py > EXACT_REPORT.json
"""
from __future__ import annotations
import itertools
import json
from collections import defaultdict
from fractions import Fraction as F
from random import Random

ACTIONS = ('reject', 'accept', 'continue')

def safe_model():
    p, q = {}, {}
    for w, a, b in itertools.product((0, 1), repeat=3):
        k = F(1, 3) if w == 0 else F(2, 3)
        p[(w, a, b)] = k * (F(3, 4) if a else F(1, 4)) * (F(3, 4) if b else F(1, 4))
        q[(w, a, b)] = k * (F(1, 4) if a else F(3, 4)) * (F(1, 4) if b else F(3, 4))
    return p, q

def obstructed_model():
    # Unconditional masses /40, exactly as EC49E immutable PROOF.md.
    rows = [
       ((0,1,1),14,4), ((0,1,0),1,1), ((0,0,1),1,1), ((0,0,0),4,14),
       ((1,1,1),11,1), ((1,1,0),4,4), ((1,0,1),4,4), ((1,0,0),1,11),
    ]
    return ({h:F(a,40) for h,a,b in rows}, {h:F(b,40) for h,a,b in rows})

def model_data(p, q):
    assert set(p)==set(q)==set(itertools.product((0,1),repeat=3))
    assert sum(p.values())==sum(q.values())==1
    assert all(a>0 and q[h]>0 for h,a in p.items())
    nodes = {t: sorted({h[:t] for h in p}) for t in (1,2,3)}
    mass = {'P':{}, 'Q':{}}
    for name, source in [('P',p),('Q',q)]:
        for t in (1,2,3):
            for h in nodes[t]:
                mass[name][h]=sum(v for leaf,v in source.items() if leaf[:t]==h)
    lr={h:mass['P'][h]/mass['Q'][h] for t in (1,2,3) for h in nodes[t]}
    return nodes, mass, lr

def quotient(p,q):
    nodes,mass,lr=model_data(p,q)
    cls={}; signatures={}; classes={}
    # Backward refinement of observable clock+complete-prefix-LR classes.
    for t in (3,2,1):
        for h in nodes[t]:
            if t==3:
                sig=(t,lr[h])
            else:
                d=defaultdict(F)
                for y in (0,1):
                    nxt=h+(y,)
                    d[cls[nxt]] += mass['Q'][nxt]/mass['Q'][h]
                sig=(t,lr[h],tuple(sorted(d.items())))
            signatures[h]=sig
        distinct=sorted({signatures[h] for h in nodes[t]}, key=repr)
        map_id={sig:f't{t}c{i}' for i,sig in enumerate(distinct)}
        for h in nodes[t]:
            c=map_id[signatures[h]]
            cls[h]=c
            classes.setdefault(c,[]).append(h)
    kr={}
    for s, hs in classes.items():
        h=hs[0]
        if len(h)==3: continue
        for measure in ('Q','P'):
            kernel=defaultdict(F)
            for y in (0,1):
                nxt=h+(y,)
                kernel[cls[nxt]] += mass[measure][nxt]/mass[measure][h]
            kr[(measure,s)]=dict(kernel)
            for other in hs[1:]:
                test=defaultdict(F)
                for y in (0,1):
                    nxt=other+(y,)
                    test[cls[nxt]] += mass[measure][nxt]/mass[measure][other]
                assert dict(test)==dict(kernel)
    assert all(len(set(lr[h] for h in hs))==1 for hs in classes.values())
    for (measure,s),kernel in kr.items():
        if measure != "Q": continue
        h=classes[s][0]
        for dest,prob in kernel.items():
            assert kr[("P",s)].get(dest,F(0)) == prob * (lr[classes[dest][0]]/lr[h])
    return nodes,mass,lr,cls,classes,kr

def exact_policy(p,q,policy,partition):
    nodes,mass,lr,cls,classes,kr=partition
    reach={h:F(1) for h in nodes[1]}
    q_flow=defaultdict(F); q_occup=defaultdict(F)
    o=[F(0),F(0),F(0),F(0)]
    for t in (1,2,3):
        for h in nodes[t]:
            if t>1:
                reach[h]=reach[h[:-1]]*policy[h[:-1]]['continue']
            s=cls[h]
            rp=mass['P'][h]*reach[h]
            rq=mass['Q'][h]*reach[h]
            q_occup[s]+=rq
            pp=policy[h]
            assert set(pp)==(set(ACTIONS) if t<3 else {'reject','accept'})
            assert all(x>=0 for x in pp.values()) and sum(pp.values())==1
            accept=pp['accept']; stop=pp['accept']+pp['reject']
            o[0]+=rp*accept; o[1]+=rq*accept
            o[2]+=t*rp*stop; o[3]+=t*rq*stop
            for a,u in pp.items():q_flow[(s,a)]+=rq*u
    reconstructed={}
    for s,hs in classes.items():
        den=q_occup[s]
        actions=ACTIONS if len(hs[0])<3 else ('reject','accept')
        reconstructed[s]={a:q_flow[(s,a)]/den if den else F(int(a=='reject')) for a in actions}
        assert sum(reconstructed[s].values())==1
    return tuple(o), reconstructed

def evaluate_quotient(partition,policy):
    nodes,mass,lr,cls,classes,kr=partition
    qm=defaultdict(F)
    for h in nodes[1]:qm[cls[h]]+=mass['Q'][h]
    o=[F(0)]*4
    for t in (1,2,3):
        for s,hs in classes.items():
            if len(hs[0])!=t:continue
            q_mass=qm[s]; p_mass=lr[hs[0]]*q_mass
            a=policy[s]['accept']; stop=policy[s]['accept']+policy[s]['reject']
            o[0]+=p_mass*a; o[1]+=q_mass*a
            o[2]+=t*p_mass*stop; o[3]+=t*q_mass*stop
            if t<3:
                for nxt,prob in kr[('Q',s)].items():qm[nxt]+=q_mass*policy[s]['continue']*prob
    return tuple(o)

def weights(r, options):
    v=[F(r.randint(0,8), 9) for _ in options]
    if sum(v)==0: v=[F(1)]*len(options)
    return dict(zip(options,[x/sum(v) for x in v]))

def test_random(p,q,part,seed,n):
    r=Random(seed)
    for i in range(n):
        pol={h:weights(r,ACTIONS if len(h)<3 else ('reject','accept')) for t in (1,2,3) for h in part[0][t]}
        original,rebuilt=exact_policy(p,q,pol,part)
        assert evaluate_quotient(part,rebuilt)==original,(i,original,rebuilt)
    return n

def test_deterministic(p,q,part):
    # Exhaust all 3^6 prefix decision patterns for eight diverse terminal maps.
    nodes=part[0]
    pre=nodes[1]+nodes[2]; terminal=nodes[3]
    n=0
    terminal_masks=(0,255,170,85,15,240,51,204)
    for choices in itertools.product(range(3),repeat=len(pre)):
        pbase={h:{a:F(int(a==ACTIONS[j])) for a in ACTIONS} for h,j in zip(pre,choices)}
        for mask in terminal_masks:
            bits=tuple((mask>>i)&1 for i in range(len(terminal)))
            policy=dict(pbase)
            for h,b in zip(terminal,bits):policy[h]={'reject':F(1-b),'accept':F(b)}
            original,rebuilt=exact_policy(p,q,policy,part)
            assert evaluate_quotient(part,rebuilt)==original,(choices,bits)
            n+=1
    assert n==3**6 * len(terminal_masks)
    return n

def fstr(v):
    return str(v)

def main():
    p,q=safe_model();part=quotient(p,q)
    nodes,mass,lr,cls,classes,kr=part
    safe_counts={str(t):sum(len(v[0])==t for v in classes.values()) for t in (1,2,3)}
    assert safe_counts=={'1':1,'2':2,'3':3},safe_counts
    assert all(len({cls[h] for h in nodes[t] if lr[h]==r})==1 for t in (1,2,3) for r in {lr[h] for h in nodes[t]})
    # Explicit rational-history-dependent full policy.
    pol={}
    for h in nodes[1]+nodes[2]+nodes[3]:
        if len(h)==1:
            pol[h]= {'reject':F(0) if h[0]==0 else F(1,6),
                     'accept':F(0) if h[0]==0 else F(1,3),
                     'continue':F(1) if h[0]==0 else F(1,2)}
        elif len(h)==2:
            pol[h]= {
                (0,1):{'reject':F(0),'accept':F(0),'continue':F(1)},
                (1,1):{'reject':F(1,3),'accept':F(1,3),'continue':F(1,3)},
                (0,0):{'reject':F(1,4),'accept':F(1,2),'continue':F(1,4)},
                (1,0):{'reject':F(1,8),'accept':F(1,8),'continue':F(3,4)},
            }[h]
        else:
            w,a,b=h
            acc=(F(1) if w==0 else F(1,2)) if a+b==2 else ((F(1,4) if w==0 else F(3,4)) if a+b==1 else (F(0) if w==0 else F(1,2)))
            pol[h]={'reject':1-acc,'accept':acc}
    explicit_o,reconstructed=exact_policy(p,q,pol,part)
    assert explicit_o==evaluate_quotient(part,reconstructed)
    reps={s: str(hs[0]) for s,hs in classes.items()}
    visible={reps[s]:{a:fstr(x) for a,x in acts.items()} for s,acts in reconstructed.items()}
    # EC49E exact source masses: countercheck the cost-significant fibers.
    u,v=obstructed_model();bad=quotient(u,v)
    bcounts={str(t):sum(len(hs[0])==t for hs in bad[4].values()) for t in (1,2,3)}
    assert bcounts=={'1':2,'2':4,'3':5},bcounts
    bad_nodes,bmass,blr,bcls,bclasses,bkernel=bad
    assert any(len({bcls[h] for h in bad_nodes[t] if blr[h]==r})>1 for t in (1,2) for r in {blr[h] for h in bad_nodes[t]})
    assert blr[(0,1)]==blr[(1,1)]==3
    assert blr[(0,0)]==blr[(1,0)]==F(1,3)
    cond={}
    for h in ((0,1),(1,1),(0,0),(1,0)):
        cond[str(h)]={str(blr[h+(y,)]):str(bmass['Q'][h+(y,)]/bmass['Q'][h]) for y in (0,1)}
    assert cond['(0, 1)']=={'1':'1/5','7/2':'4/5'}
    assert cond['(1, 1)']=={'1':'4/5','11':'1/5'}
    assert cond['(0, 0)']=={'2/7':'14/15','1':'1/15'}
    assert cond['(1, 0)']=={'1/11':'11/15','1':'4/15'}
    tv_y1_1=F(4,5)
    tv_y1_0=F(14,15)
    # For the historical c=1/8 witness: coarse max 0, fine max 3/80.
    def pos(x):return max(F(0),x)
    c=F(1,8)
    vcoarse=pos(F(1,4)-2*c+pos(F(1,8)-c))
    vfine=(pos(F(1,4)-2*c+pos(F(1,20)-c)) + pos(F(1,4)-2*c+pos(F(1,5)-c)))/2
    assert (vcoarse,vfine,vfine-vcoarse)==(0,F(3,80),F(3,80))
    # Validate many real policies by explicit rational sample and ALL deterministic full histories.
    all_deterministic=test_deterministic(p,q,part)
    random_count=test_random(p,q,part,seed=4906,n=1000)
    result={
      'schema':'EC49F_EXACT_FRACTION_REPORT_V1',
      'model_kind':'auxiliary dual-source positive-rational BRC observation tree (not native X6 or signed BRC)',
      'safe_model':{'leaves':8,'uncompressed_history_nodes':14,'quotient_classes_by_stage':safe_counts,
                    'all_leaf_masses_strictly_positive':True,'P_sum':'1','Q_sum':'1',
                    'sample_fine_policy_observation':[fstr(x) for x in explicit_o],
                    'sample_reconstructed_policy':visible,
                    'deterministic_full_history_policies_verified':all_deterministic,
                    'rational_random_full_history_policies_verified':random_count,
                    'all_reconstructions_exact':True,
                    'quotient_state_observable_as_stage_and_exact_LR':True},
      'ec49e_obstruction':{'source':'EC49E PROOF.md @ 4cc5c0407d499562b7f3039a51454c53dc438c82',
                          'quotient_classes_by_stage':bcounts,'initial_nodes_split':True,
                          'quotient_state_observable_as_stage_and_exact_LR':False,
                          'conditional_Q_spectra':cond,
                          'stage_2_TV_for_Y1_1':fstr(tv_y1_1),
                          'stage_2_TV_for_Y1_0':fstr(tv_y1_0),
                          'historical_c_1_8_coarse_support':fstr(vcoarse),
                          'historical_c_1_8_fine_support':fstr(vfine),
                          'historical_gap':fstr(vfine-vcoarse)},
      'proof_scope':'finite positive-rational trees, exact current LR, action-conditioned Q kernel, source-neutral behavioral policies; general equivalence theorem proved separately in PROOF.md',
      'verification_scope':'all 729 deterministic two-stage decision patterns crossed with eight stated terminal masks, 1000 rational random policies; complete finite quotient signatures for safe and EC49E models',
    }
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()