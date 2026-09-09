#!/usr/bin/env python3
"""Exact labeled lifts and observable budgets for frozen X6-DENSITY-PORT-1.

Neither a physical force law nor an NS solver. Both imported parent checkers are
used unchanged. All computations use integer or Fraction arithmetic.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path
from ns_native_density_port_d5c00d import (
    D, DIRS, ZERO, EMPTY, BACKGROUND, C, unit, add, actual, config_counts,
    local_collision, collision, stream, step, seed, norm, invariants,
    transformed_counts, transformed_field, act_vec,
)


def dot(x, y): return sum(a*b for a,b in zip(x,y))
def sub(x, y): return tuple(a-b for a,b in zip(x,y))
def ch(i, s): return 2*i + int(s==1)
def jfrac(x): return {'numerator':x.numerator,'denominator':x.denominator}


def matching(event, kind):
    """Channel-to-channel matching, independent of particle IDs.

    Covariance is asserted for S6 and global sign/space reversal, NOT arbitrary
    independent reversals of the six signed basis choices.
    """
    j,s,l,m=event
    if kind==2:
        return {ch(j,s):ch(j,s),ch(l,s):ch(m,s),ch(l,-s):ch(m,-s)}
    if kind==3:
        return {ch(j,s):ch(m,s),ch(l,s):ch(j,s),ch(l,-s):ch(m,-s)}
    raise ValueError('kind must be 2 or 3')


def counts_of(particles):
    out={}
    for pos,v in particles.values():
        if pos not in out: out[pos]=[0]*(2*D)
        out[pos][v]+=1
    return {pos:tuple(c) for pos,c in out.items()}


def labeled_step(particles, kind):
    """One autonomous update on unique tags. Tags are never used for selection."""
    field=counts_of(particles)
    col,events=collision(field,EMPTY)
    routes={z:matching(e,kind) for z,e,_ in events}
    updated={}; budget=0; changed=0
    for tag,(z,v) in particles.items():
        w=routes[z][v] if z in routes else v
        updated[tag]=(add(z,DIRS[w]),w)
        impulse=sub(DIRS[w],DIRS[v])
        budget+=dot(impulse,impulse)
        changed+=v!=w
    assert counts_of(updated)==stream(col)
    assert set(updated)==set(particles)
    return updated, {'events':len(events),'changed_packets':changed,'turn_square':budget}


def moment(c):
    p=tuple(c[2*i+1]-c[2*i] for i in range(D))
    q=tuple(c[2*i+1]+c[2*i] for i in range(D))
    return sum(c),p,q


def mean(c):
    rho,p,_=moment(c)
    return tuple(Fraction(x,rho) if rho else Fraction(0) for x in p)


def moment_record(field, t):
    ub=mean(BACKGROUND)
    rho_l1=p_l1=off=phi2=0
    u_l2=Fraction(0)
    for z,d in field.items():
        c=actual(field,z,BACKGROUND)
        rho_l1+=abs(sum(d))
        p_l1+=sum(abs(d[2*i+1]-d[2*i]) for i in range(D))
        off+=sum(c[2*i]+c[2*i+1] for i in range(2,D))
        phi2+=sum(a*a-b*b for a,b in zip(c,BACKGROUND))
        u_l2+=sum((a-b)**2 for a,b in zip(mean(c),ub))
        assert all(abs(x)<=1 for x in d)
        assert dot(mean(c),mean(c))<=1
    assert phi2==2
    assert norm(field)==2+2*off
    assert rho_l1>=32*t+2 and p_l1>=16*t+2
    assert u_l2>=Fraction(40*t,9)
    if t:
        for age in range(1,t+1):
            for axis in range(2,D):
                for eps,s in product((-1,1),repeat=2):
                    z=list(add(unit(axis,eps),tuple(s*age if k==1 else 0 for k in range(D))));z[0]=t-age;z=tuple(z)
                    c=actual(field,z,BACKGROUND)
                    expected=list(BACKGROUND);expected[ch(1,s)]-=1
                    assert c==tuple(expected)
                    assert sum((a-b)**2 for a,b in zip(mean(c),ub))==Fraction(5,18)
    return {'tick':t,'channel_l1':norm(field),'density_l1':rho_l1,
            'moment_l1':p_l1,'mean_velocity_l2_squared':jfrac(u_l2),
            'transverse_population':off,'transverse_kinetic_readout':jfrac(Fraction(off,2)),
            'relative_square_occupation':phi2}


def exact_moment_step(field,bg):
    """Independent q/p streaming formula, using the parent collision once."""
    col,_=collision(field,bg)
    sites=set()
    for z in col:
        for v in DIRS:sites.add(add(z,v))
    out={}
    _,pb,qb=moment(bg)
    for z in sites:
        vec=[]
        for i in range(D):
            _,pm,qm=moment(actual(col,add(z,unit(i,-1)),bg))
            _,pp,qp=moment(actual(col,add(z,unit(i,1)),bg))
            p1=Fraction(qm[i]-qp[i]+pm[i]+pp[i],2)
            q1=Fraction(qm[i]+qp[i]+pm[i]-pp[i],2)
            minus=Fraction(q1-p1,2);plus=Fraction(q1+p1,2)
            assert minus.denominator==plus.denominator==1
            vec.extend((int(minus)-bg[2*i],int(plus)-bg[2*i+1]))
        if any(vec):out[z]=tuple(vec)
    assert out==stream(col)
    return out


def run(steps=5):
    # Complete local matching census, all 240 typed ports and all 6 bijections.
    census=Counter(); equalities=0; work_equalities=0; exchange_equalities=0
    for j,l,m in permutations(range(D),3):
        for s in (-1,1):
            ev=(j,s,l,m); ins=(ch(j,s),ch(l,s),ch(l,-s))
            outs=(ch(j,s),ch(m,s),ch(m,-s))
            local=Counter()
            for perm in permutations(outs):
                ds=[sub(DIRS[w],DIRS[v]) for v,w in zip(ins,perm)]
                a=sum(v!=w for v,w in zip(ins,perm))
                cost=sum(dot(d,d) for d in ds)
                assert all(sum(d[i] for d in ds)==0 for i in range(D))
                assert sum(dot(DIRS[w],DIRS[w]) for w in perm)==3
                cross=sum(dot(DIRS[v],d) for v,d in zip(ins,ds))
                assert 2*cross+cost==0
                assert (a,cost) in ((2,4),(3,6))
                local[a,cost]+=1;census[a,cost]+=1;work_equalities+=1
            assert local=={(2,4):2,(3,6):4}
            # Three-edge additive incidence ledger for the L3 assignment.
            route=matching(ev,3)
            ds=[sub(DIRS[route[v]],DIRS[v]) for v in ins]
            q_ab=unit(j,s);q_bc=unit(l,s);q_ca=unit(m,s)
            assert ds==[sub(q_ca,q_ab),sub(q_ab,q_bc),sub(q_bc,q_ca)]
            exchange_equalities+=1
            for kind in (2,3):
                mp=matching(ev,kind)
                for k in range(D-1):
                    p=list(range(D));p[k],p[k+1]=p[k+1],p[k];p=tuple(p)
                    e2=(p[j],s,p[l],p[m]);mq=matching(e2,kind)
                    def cp(v):return 2*p[v//2]+v%2
                    assert {cp(v):cp(w) for v,w in mp.items()}==mq
                    equalities+=1
                rev=matching((j,-s,l,m),kind)
                assert {v^1:w^1 for v,w in mp.items()}==rev
    # Full matching-history multiplicities, not distinct terminal-state counts.
    poly={0:1}
    for _ in range(8):
        nxt=Counter()
        for cost,mul in poly.items():
            nxt[cost+4]+=2*mul;nxt[cost+6]+=4*mul
        poly=dict(nxt)
    assert sum(poly.values())==6**8 and poly[32]==2**8 and poly[48]==4**8
    # Both rules on the exact same finite-particle count histories.
    # The fourth packet makes axis 3 the unique density-selected output port.
    initial={'A':(ZERO,ch(0,1)),'B':(ZERO,ch(1,1)),
             'C':(ZERO,ch(1,-1)),'D':(unit(2),ch(0,1))}
    a=dict(initial);b=dict(initial);field=counts_of(initial);trace=[]
    for tick in range(1,9):
        a,ba=labeled_step(a,2);b,bb=labeled_step(b,3);field,ev=step(field,EMPTY)
        assert counts_of(a)==counts_of(b)==field
        assert ba['turn_square']==4*len(ev) and bb['turn_square']==6*len(ev)
        trace.append({'tick':tick,'L2':ba,'L3':bb,'same_counts':True,'same_labels':a==b})
    assert trace[0]['L2']['turn_square']==4 and trace[0]['L3']['turn_square']==6
    # More than one event, 2,187 packets, free boundary, four complete updates.
    bulk={};num=0
    for z in product(range(-1,2),repeat=D):
        for v in (ch(0,1),ch(1,1),ch(1,-1)):
            bulk[num]=(z,v);num+=1
    # A neutral move of one existing tag creates the same kind of density seed.
    tag=next(tag for tag,(z,v) in bulk.items() if z==unit(0) and v==ch(0,1))
    bulk[tag]=(ZERO,ch(0,1))
    a=dict(bulk);b=dict(bulk);field=counts_of(bulk);bulk_trace=[]
    initial_hist=Counter(x for c in field.values() for x in c if x)
    for tick in range(1,5):
        a,ba=labeled_step(a,2);b,bb=labeled_step(b,3);field,ev=step(field,EMPTY)
        assert counts_of(a)==counts_of(b)==field
        assert Counter(x for c in field.values() for x in c if x)==initial_hist
        assert ba['turn_square']==4*len(ev) and bb['turn_square']==6*len(ev)
        bulk_trace.append({'tick':tick,'events':len(ev),'L2_cost':ba['turn_square'],
                          'L3_cost':bb['turn_square'],'different_tag_states':sum(a[k]!=b[k] for k in a)})
    # The exact p,q state is lossless, with parity and positivity constraints.
    recon=0
    for c in product(range(3),repeat=6):
        # A finite test slice in channel coordinates, with remaining six zero.
        c=c+(0,)*6;rho,p,q=moment(c)
        back=tuple(x for pi,qi in zip(p,q) for x in ((qi-pi)//2,(qi+pi)//2))
        assert back==c and rho==sum(q)
        assert all(qi>=abs(pi) and (qi-pi)%2==0 for pi,qi in zip(p,q))
        recon+=1
    # Explicit failure of (rho,P)-only closure: two isolated ternary states.
    x={ZERO:config_counts(C(0,1,1))};y={ZERO:config_counts(C(0,1,2))}
    assert moment(x[ZERO])[:2]==moment(y[ZERO])[:2]
    xx,ex=step(x,EMPTY);yy,ey=step(y,EMPTY)
    assert not ex and not ey and xx!=yy
    assert sum(xx.get(unit(1),EMPTY))==1 and sum(yy.get(unit(1),EMPTY))==0
    exact_moment_step(x,EMPTY);exact_moment_step(y,EMPTY)
    # Continue the frozen trajectory, now testing genuinely different observers.
    field=seed();records=[moment_record(field,0)];event_counts=[];fluxes=[];net_flux=0
    for tick in range(1,steps+1):
        if tick<=3: exact_moment_step(field,BACKGROUND)
        field,ev=step(field,BACKGROUND);event_counts.append(len(ev))
        forward=sum(e[2]==1 and e[3]>=2 for z,e,scores in ev)
        backward=sum(e[2]>=2 and e[3]==1 for z,e,scores in ev)
        assert all(e[0]==0 and e[2]!=0 and e[3]!=0 for z,e,scores in ev)
        net_flux+=forward-backward
        rec=moment_record(field,tick)
        assert rec['transverse_population']==2*net_flux
        fluxes.append({'tick':tick,'axis2_to_transverse':forward,
                       'transverse_to_axis2':backward,
                       'transverse_rerouting':len(ev)-forward-backward,
                       'cumulative_net_energy_transfer':net_flux})
        records.append(rec)
    return {'schema':'EM_NATIVE_EXCHANGE_LIFT_RESULTS_V1',
            'event_id':'NS-NATIVE-EXCHANGE-LIFT-20260909-D5C00D-11',
            'status':'ORDINARY_FINITE_PROOFS_AND_EXACT_CHECKS_NOT_FORCE_ADMISSION',
            'frozen_count_law':'X6-DENSITY-PORT-1',
            'parent_commit':'6f119ea99021f83141321a5241dcb33b70f5af44',
            'local':{'typed_ports':240,'matchings':sum(census.values()),
                     'two_changed_cost_four':census[2,4],'three_changed_cost_six':census[3,6],
                     'work_identities':work_equalities,'exchange_cycles':exchange_equalities,
                     'S6_generator_covariance_checks':equalities,'global_sign_reversal_checks':480},
            'eight_event_history_polynomial':{str(k):v for k,v in sorted(poly.items())},
            'eight_event_history_count':sum(poly.values()),
            'four_packet_lift':trace,'finite_population':num,'finite_lift':bulk_trace,
            'integer_moment_reconstruction_checks':recon,'rho_P_closure_counterexample':True,
            'observer_trajectory':records,'collisions':event_counts,'directional_energy_flux':fluxes,
            'proved_all_time':{'density_l1_min':'32*t+2','moment_l1_min':'16*t+2',
                              'mean_velocity_l2_squared_min':'40*t/9',
                              'transverse_kinetic_readout_min':'8*t',
                              'speed_squared_max':1,'relative_square_occupation':2,
                              'finite_horizon_mean_square_gain_min':'32*T',
                              'initial_mean_square_defect':'5/36'},
            'nonclaims':['No primitive TRIADIC_CLOSURE_E admission',
                         'No physical force, viscosity, or classical NS theorem',
                         'Turning-square ledger is not dissipated energy',
                         'S6/global reversal covariance is not arbitrary signed-frame covariance',
                         'No one fixed finite population has unbounded discrepancy',
                         'No independent review, Lean validation, or novelty claim']}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--steps',type=int,default=5)
    ap.add_argument('--output',type=Path,default=Path('results.json'))
    args=ap.parse_args()
    if not 1<=args.steps<=7:ap.error('--steps must lie between 1 and 7')
    result=run(args.steps)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
