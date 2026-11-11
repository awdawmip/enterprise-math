#!/usr/bin/env python3
"""R78 exact endpoint/integer-crossing latest-source oracle.

Only for nonwrapping original arcs with stable endpoint floors; all arithmetic
is fractions.Fraction. Independent finite-strata reference enumerates R77 cuts
only for small random models. No third-party dependencies.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import floor, ceil
from random import Random
from time import perf_counter
from statistics import median
import json


def frac(v):
    return v - floor(v)


def arc_data(a,b,L,U):
    assert L <= U
    ka,kb=floor(a*L),floor(b*L)
    assert floor(a*U)==ka and floor(b*U)==kb, 'boundary floor crossing; split first'
    AL,AU=a*L-ka,a*U-ka
    BL,BU=b*L-kb,b*U-kb
    assert 0 <= AL < BL < 1 and 0 <= AU < BU < 1, 'unstable or wrapping arc'
    return ka,kb,max(BL-AL,BU-AU)


def direct_present(t,j,x,a,b,theta):
    A=frac(a*theta); B=frac(b*theta); S=frac(x+(t-j)*theta)
    assert A < B
    return A<=S<B


def direct_winner(events,j,x,a,b,theta):
    present=[e for e in events if direct_present(e[0],j,x,a,b,theta)]
    return max(present) if present else None


def one_source(events_identity, j,x,a,b,L,U,ka,kb,wmax):
    t,branch=events_identity
    slope=t-j-a
    def F(theta):return x+slope*theta+ka
    def present(theta): return direct_present(t,j,x,a,b,theta)
    fL,fU=F(L),F(U)
    fmin,fmax=min(fL,fU),max(fL,fU)
    pL,pU=present(L),present(U)
    # Existential IN: endpoint, else one integer value in F(I).
    in_witness = L if pL else (U if pU else None)
    if in_witness is None:
        k=ceil(fmin)
        if k<=fmax:
            assert slope!=0
            in_witness=(Q(k)-x-ka)/slope
            assert L<=in_witness<=U and present(in_witness)
    # Existential OUT: endpoint, else rational point just left of an integer.
    out_witness= L if not pL else (U if not pU else None)
    if out_witness is None:
        k=floor(fmin)+1
        if k<=fmax:
            assert slope!=0
            delta=(1-wmax)/2
            ftarget=(max(fmin,Q(k)-delta)+Q(k))/2
            out_witness=(ftarget-x-ka)/slope
            assert L<=out_witness<=U and not present(out_witness)
    return in_witness,out_witness


def classify(events,j,x,a,b,L,U):
    ka,kb,wmax=arc_data(a,b,L,U)
    # Higher sources are discarded only after exact proof that they are OUT everywhere.
    for e in sorted(events,reverse=True):
        yin,yout=one_source(e,j,x,a,b,L,U,ka,kb,wmax)
        if yin is None:continue
        if yout is None:
            assert direct_winner(events,j,x,a,b,L)==e
            return {'status':'STABLE','winner':e,'witness':str(yin)}
        assert direct_winner(events,j,x,a,b,yin)==e
        other=direct_winner(events,j,x,a,b,yout)
        assert other!=e
        return {'status':'CHANGES','winner_at_in':e,'winner_at_out':other,
                'in_theta':str(yin),'out_theta':str(yout)}
    return {'status':'STABLE_NONE'}


def critical_points(events,j,x,a,b,L,U):
    pts={L,U}
    affines=[(a,Q(0)),(b,Q(0)),(a-b,Q(0))]
    for t,_ in events:
        affines.extend([(t-j,x),(t-j-a,x),(t-j-b,x)])
    for slope,intercept in affines:
        if not slope:continue
        y1=slope*L+intercept;y2=slope*U+intercept
        for k in range(ceil(min(y1,y2)),floor(max(y1,y2))+1):
            theta=(Q(k)-intercept)/slope
            if L<=theta<=U:pts.add(theta)
    return sorted(pts)


def reference(events,j,x,a,b,L,U):
    pts=critical_points(events,j,x,a,b,L,U)
    q=[]
    for i,p in enumerate(pts):
        q.append(p)
        if i+1<len(pts):q.append((p+pts[i+1])/2)
    winners=[direct_winner(events,j,x,a,b,theta) for theta in q]
    if all(w is None for w in winners):return 'STABLE_NONE',None,len(q)
    if all(w==winners[0] for w in winners):return 'STABLE',winners[0],len(q)
    return 'CHANGES',None,len(q)


def check():
    rng=Random(781126)
    models=0; comparisons=0; cells=0; statuses={'STABLE_NONE':0,'STABLE':0,'CHANGES':0}
    for trial in range(330):
        a=rng.randint(1,4);b=rng.randint(a+1,7)
        # choose small rational interval with stable nonwrapping original arc.
        L=Q(rng.randint(1,3),rng.randint(12,23));U=L+Q(rng.randint(0,3),rng.randint(40,90))
        if L>U:continue
        try:arc_data(a,b,L,U)
        except AssertionError:continue
        events=list(set((rng.randint(-19,28),rng.randint(0,4)) for _ in range(rng.randint(0,8))))
        j=rng.randint(-3,5);x=Q(rng.randint(-5,5),rng.randint(1,11))
        res=classify(events,j,x,a,b,L,U)
        status,w,sz=reference(events,j,x,a,b,L,U)
        assert res['status']==status, (trial,res,status)
        if status=='STABLE':assert tuple(res['winner'])==w
        if status=='CHANGES':
            yi=Q(res['in_theta']);yo=Q(res['out_theta'])
            assert direct_winner(events,j,x,a,b,yi)==tuple(res['winner_at_in'])
            assert direct_winner(events,j,x,a,b,yo)!=tuple(res['winner_at_in'])
        statuses[status]+=1;models+=1;cells+=sz
        # extra rational points along cells; direct readout must not contradict status.
        pts=critical_points(events,j,x,a,b,L,U)
        for k in range(len(pts)-1):
            for d in [Q(1,4),Q(3,4)]:
                theta=pts[k]+(pts[k+1]-pts[k])*d
                actual=direct_winner(events,j,x,a,b,theta)
                if status=='STABLE':assert actual==w
                if status=='STABLE_NONE':assert actual is None
                comparisons+=1
    assert models>=180, models

    # Single-source oscillation family: full enumeration expands, direct oracle does not.
    family=[]
    for t in [24,48,96,192,384,768]:
        events=[(t,0)];L,U=Q(1,4),Q(1,3)
        out=classify(events,0,Q(0),1,2,L,U)
        assert out['status']=='CHANGES'
        ref=reference(events,0,Q(0),1,2,L,U)
        assert ref[0]=='CHANGES'
        family.append({'t':t,'explicit_cells':ref[2],'oracle_sources':1,'status':out['status']})

    # Large binary integer time, without enumerating a single phase boundary.
    big=[]
    for exponent in [6,12,24,60,120]:
        t=12*10**exponent
        v=classify([(t,0)],0,Q(0),1,2,Q(1,4),Q(1,3))
        assert v['status']=='CHANGES'
        yi=Q(v['in_theta']);yo=Q(v['out_theta'])
        assert direct_present(t,0,Q(0),1,2,yi) and not direct_present(t,0,Q(0),1,2,yo)
        big.append({'decimal_exponent':exponent,'time_bits':t.bit_length(),
                    'status':v['status'], 'witness_denominator_bits':max(yi.denominator.bit_length(),yo.denominator.bit_length())})

    # Reproducible timing includes algorithm calls and full exhaustive output generation, independent Python paths.
    speed=[]
    for t in [96,384,1536]:
        inp=([(t,0)],0,Q(0),1,2,Q(1,4),Q(1,3))
        rounds=30
        start=perf_counter()
        for _ in range(rounds):classify(*inp)
        lazy_ms=(perf_counter()-start)*1000/rounds
        start=perf_counter()
        for _ in range(rounds):reference(*inp)
        full_ms=(perf_counter()-start)*1000/rounds
        speed.append({'t':t,'lazy_ms':round(lazy_ms,4),'explicit_ms':round(full_ms,4)})
    return {'seed':781126,'independent_valid_random_models':models,'direct_point_comparisons':comparisons,
            'reference_strata_evaluated':cells,'statuses':statuses,'oscillation_family':family,
            'large_integer_witnesses':big,'indicative_timing':speed,'result':'PASS'}

if __name__=='__main__':
    result=check()
    print(json.dumps(result,indent=2,ensure_ascii=False))
    with open('/mnt/data/em_r78/verification.json','w') as f:json.dump(result,f,indent=2,ensure_ascii=False)
