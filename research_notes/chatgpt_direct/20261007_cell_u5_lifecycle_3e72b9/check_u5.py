#!/usr/bin/env python3
"""Executed U5 finite certificates. No native force/admission/time claim.

Run python check_u5.py. All scientific propagation and trial composition uses
actual source-pinned BRC. Norm/TV differences below are comparison observers of
positive carriers. The infinite-horizon theorems are proved in README.md; finite
checks do not replace those proofs. Inherited U4 inputs are reconstructed only
as inputs to the NEW two-query and lifecycle certificates.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,gzip,hashlib
import lifecycle as u
c,r,o=u.c,u.r,u.o
ROOT=Path(__file__).resolve().parent; EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def check(test,name):
    global checks
    checks+=1
    if not test: raise AssertionError(name)


def same_total(a,b):
    return c.total_readout(a)==c.total_readout(b)


def canonical_bytes(value):
    return (json.dumps(c.encode(value),ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()

lam=Q(1,48);rho=Q(1,4);epsilon=Q(1,8);kappa=lam
z=r.ZERO;e=r.direction(0);e2=r.direction(2)
X=(z,tuple(2*v for v in e));Y=(e,X[1])
transport=c.RetainedField(rho)
F2=o.marked_pulse(X,2,rho)['layers'][-1]
F3,_=transport.advance(F2,X,3);G3,_=transport.advance(F2,Y,3)
# U4 proved these states reachable at the same labelled coordinates X.
# We do not enumerate its already-published 53 old histories as new progress.
delta3=u.l1_contrast(F3,G3)
check(delta3==Q(1,18432),'inherited comparison input matches source')
left=u.two_query_path_law(F3,X,3,transport,kappa)
right=u.two_query_path_law(G3,X,3,transport,kappa)
for result in (left,right):
    check(r.total(result['first_law'].values()).total==1,'first law normalized')
    check(r.total(result['paths'].values()).total==1,'two-query path law normalized')
    check(r.total(result['final_law'].values()).total==1,'final marginal normalized')
    for history,w in result['paths'].items():
        check(w.total>0,'all retained branches positive')
        for earlier,later in zip((X,)+history,history):
            check(len(set(later))==len(later),'joint exclusion')
            for old,new in zip(earlier,later):
                check(sum(abs(a-b) for a,b in zip(old,new))<=1,'primitive-or-idle successor')
    # Crosscheck the new BRC target-row evaluator against FULL inherited advance.
    keys=sorted(result['first_law']);indices={0,len(keys)//2,len(keys)-1}
    for index in sorted(indices):
        cells=keys[index]
        ff,ret=transport.advance(result['first_field'],cells,5)
        full_rows={key:value for key,value in ff.items()
                   if key[1] in cells and cells.index(key[1])!=key[0]}
        check(full_rows==result['second_arrival_rows'][cells],
              'exact next source-resolved CWM rows, not an approximate propagator')

v1=u.tv_contrast(left['first_law'],right['first_law'])
v2=u.tv_contrast(left['paths'],right['paths'])
vfinal=u.tv_contrast(left['final_law'],right['final_law'])
delta4=u.l1_contrast(left['first_field'],right['first_field'])
check(v1==Q(3,110656),'inherited first query TV')
check(v2==v1,'new exact two-query TRAJECTORY TV')
check(vfinal<=v2,'forgetting the first position cannot increase TV')
check(delta4==Q(1,73728),'whole-field comparison after common propagation')
infinite=u.geometric_budget(delta3,rho,kappa)
finite=u.geometric_budget(delta3,rho,kappa,horizon=2)
refined=v1+(1-v1)*min(Q(1),u.geometric_budget(delta4,rho,kappa))
check(infinite==Q(1,1152),'infinite feedback comparison budget')
check(finite==Q(5,6144),'two-step generic comparison budget')
check(refined==Q(124477,509902848),'exact first-coupling refinement')
check(v2<=refined<=infinite,'executed path law consistent with uniform theorem')

# Infinite no-source motion-tail budgets, computed as actual recurrent BRC.
cutoffs={}
for N in (2,4):
    candidates=[]
    for n in range(16):
        bound=u.geometric_budget(Q(N),rho,kappa,depth=n+1)
        candidates.append(bound)
        check(bound==Q(N)*rho**(n+1)/(kappa*(1-rho)), 'BRC tail equals proved formula')
    n=next(i for i,b in enumerate(candidates) if b<=Q(1,10**6))
    check(n==13,'first certified 1e-6 cutoff in these parameters')
    cutoffs[str(N)]={'after_stage':n,'future_any_motion_bound':str(candidates[n]),
                     'previous_bound':str(candidates[n-1])}
check(cutoffs['2']['future_any_motion_bound']=='1/2097152','two-source tail')
check(cutoffs['4']['future_any_motion_bound']=='1/1048576','four-source tail')

# NEW local, debit-before-credit dormant release. Detailed finite field tests.
square=(z,e,tuple(a+b for a,b in zip(e,e2)),e2)
recycle={}
for name,cells in (('pair',X),('square_221',square)):
    seed=r.edge(Q(1,12))
    active={(b,cell,p):seed for b,cell in enumerate(cells) for p in r.PORTS}
    dormant={};N=len(cells);history=[]
    scalars,_=u.two_sector_budget(N,0,rho,epsilon,4)
    for stage in range(1,5):
        oldA,oldD=active,dormant
        # Pair material may change location, but its old deposits stay put.
        layout=Y if name=='pair' and stage==2 else cells
        active,dormant,part=u.local_release_step(oldA,oldD,layout,stage,transport,epsilon)
        at,dt=c.total_readout(active),c.total_readout(dormant)
        check(at+dt==N,'no new source / full response total conserved')
        check(at==scalars[stage][0].total and dt==scalars[stage][1].total,
              'full X6 circuit agrees with proved sector recurrence')
        check(at==Q(N,7)+Q(6*N,7)*Q(1,8)**stage,'closed positive sector identity')
        check(set(part['released'])==set(oldD),'release at same absolute key')
        for key,value in oldD.items():
            released=part['released'][key];held=part['held_old'][key]
            check(released.total==epsilon*value.total,'release is debited old budget')
            check(released.total+held.total==value.total,'no double counting of one dormant share')
        check(all(n==stage for n,s,zz,p in part['retired']),'retirement stage preserved in receipt')
        history.append({'stage':stage,'layout':layout,'active':active,'dormant':dormant,'partitions':part})
    recycle[name]=history

# Finite BRC validation of sector formula across separately stated trial parameters.
sector_checks=[]
for rr,ee,N in ((Q(1,4),Q(1,8),2),(Q(1,3),Q(1,6),4),
                (Q(1,5),Q(1,5),1),(Q(1,8),Q(1,4),3)):
    states,releases=u.two_sector_budget(N,0,rr,ee,32)
    fixed=Q(N)*ee/(1-rr+ee)
    for n,(a,d) in enumerate(states):
        check(a.total+d.total==N,'closed two-sector budget')
        # The alternating signed term, when ee>rr, is only a comparison formula.
        check(a.total==fixed+(N-fixed)*(rr-ee)**n,'exact recurrence all stated n')
    sector_checks.append({'rho':rr,'release':ee,'N':N,'active_limit':fixed,
                          'active_at32':states[-1][0].total,
                          'cumulative_released_at32':r.total(releases).total})

# New lifecycle makes an ACTIVE-FIELD-only error bound invalid.
# These are declared test inputs of the new circuit, not spontaneous U4 states.
Dplus={(1,z,0):r.edge(lam)};Dminus={(1,z,1):r.edge(lam)}
AP,DP,pp=u.local_release_step({},Dplus,X,1,transport,epsilon)
AM,DM,pm=u.local_release_step({},Dminus,X,1,transport,epsilon)
LP,_=u.probe_law(AP,X,1,kappa);LM,_=u.probe_law(AM,X,1,kappa)
reactivated_tv=u.tv_contrast(LP,LM)
check(u.l1_contrast({}, {})==0,'same current active field')
check(c.total_readout(Dplus)==c.total_readout(Dminus),'same total dormant response')
check(reactivated_tv==Q(1,9),'new directionally stored response changes next occupancy')
check(LP[(e,X[1])].total==Q(1,9),'positive-axis target')
check(LM[(r.direction(1),X[1])].total==Q(1,9),'negative-axis target')
# No release is carried to a moving source's current position.
check(set(pp['released'])=={(1,z,0)} and X[1]!=z,'source identity is not release location')

summary={
 'status':'CONDITIONAL_U4_EXTENSION_AND_NEW_LOCAL_RELEASE_CIRCUIT',
 'checks':checks,'actual_BRC_calls':dict(r.CALLS),
 'inputs':{'lambda':str(lam),'rho':str(rho),'waiting':str(kappa),'release_NEW_MODEL':str(epsilon)},
 'two_query':{'left_first_outcomes':len(left['first_law']),
              'right_first_outcomes':len(right['first_law']),
              'left_path_outcomes':len(left['paths']),
              'right_path_outcomes':len(right['paths']),
              'left_second_resolution_branches':left['second_resolution_branches'],
              'right_second_resolution_branches':right['second_resolution_branches'],
              'first_TV':str(v1),'path_TV':str(v2),'final_TV':str(vfinal),
              'delta3_l1':str(delta3),'delta4_l1':str(delta4),
              'uniform_infinite_future_TV_bound':str(infinite),
              'uniform_two_query_TV_bound':str(finite),
              'first_step_refined_infinite_TV_bound':str(refined)},
 'no_source_motion_cutoffs':cutoffs,
 'new_local_release':{'sector_active_limit_fraction':'1/7',
                     'steps_full_X6':4,'full_X6_preparations':['pair','square_221'],
                     'zero_active_field_comparison_next_TV':str(reactivated_tv),
                     'sector_parameter_checks':c.encode(sector_checks)},
 'bound_scope':'ALL_FUTURE_LABELLED_OCCUPANCY_LAWS_OF_NO_SOURCE_FRESH_ONLY_U4;NOT_FULL_HIDDEN_STATE',
 'inherited_U4_recovered_not_new':True,
 'native_force':False,'primitive_triad_lift':False,'physical_time':False,
 'physical_probability':False,'physical_energy':False,'sustained_local_motion_proved':False,
 'prime_claim':False,'new_release_is_hypothesis_not_U4_consequence':True}

trace={'old_input':{'F3':F3,'G3':G3},'left':left,'right':right,
       'recycle':recycle,'new_release_counterexample':{'Dplus':Dplus,'Dminus':Dminus,'LP':LP,'LM':LM}}
raw=canonical_bytes(trace);compressed=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(compressed)
summary['trace_sha256']=hashlib.sha256(raw).hexdigest()
summary['trace_compressed_sha256']=hashlib.sha256(compressed).hexdigest()
summary['trace_uncompressed_bytes']=len(raw)
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
