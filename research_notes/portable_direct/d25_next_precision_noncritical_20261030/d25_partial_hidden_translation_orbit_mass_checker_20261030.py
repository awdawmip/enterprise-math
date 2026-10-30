#!/usr/bin/env python3
"""Exact author-side enumerator for partial hidden translations and BRC masses.

Finite auxiliary ring only; not an Enterprise Math native X6 experiment.
No external libraries are needed.  All arithmetic is exact integer modular arithmetic.
"""
from __future__ import annotations

import json
import itertools
from collections import Counter, defaultdict
from pathlib import Path


def polynomial(name, x):
    if name == 'xyy1':
        assert len(x) == 2
        return x[0] * x[1] * (x[1] - 1)
    if name == 'x2_plus_y':
        assert len(x) == 2
        return x[0]**2 + x[1]
    if name == 'xy_plus_x2':
        assert len(x) == 2
        return x[0]*x[1] + x[0]**2
    if name == 'zero':
        return 0
    if name == 'three_variable':
        assert len(x) == 3
        return x[0]*x[1] + x[2]**2 + x[0]*x[2]
    raise ValueError(name)


def case(p,n,e,strides,name,raw_check):
    assert p in (3,5,7) and n>=1 and e>=1
    r = len(strides)
    modulus=p**n
    L=n+e
    full_mod=p**L
    t=tuple(min(s,n) for s in strides)
    periods=tuple(p**v for v in t)
    hlist=list(itertools.product(*(range(0,modulus,step) for step in periods)))
    hset=set(hlist)
    assert len(hset)==len(hlist)
    group=list(itertools.product(range(modulus),repeat=r))
    shift=lambda a,v: tuple((ai+vi)%modulus for ai,vi in zip(a,v))
    sig={}
    for a in group:
        sig[a]=tuple(polynomial(name,shift(a,v))%modulus for v in hlist)
    direct_mod=Counter(sig.values())
    assert sum(direct_mod.values())==modulus**r
    direct_full=Counter({k * p**(e*r):sum(1 for v in direct_mod.values() if v==k)
                         for k in set(direct_mod.values())})
    # Compute H-orbit of signatures independently, by orbit-stabilizer.
    coset_reps=list(itertools.product(*(range(step) for step in periods)))
    orbit_data={}
    for a in coset_reps:
        orbit_signatures=[sig[shift(a,u)] for u in hlist]
        orbit_key=min(orbit_signatures)
        stabilizer=sum(1 for ss in orbit_signatures if ss==sig[a])
        assert stabilizer>=1 and len(hlist)%stabilizer==0
        if orbit_key not in orbit_data:
            orbit_data[orbit_key]={'m':0,'stabilizer':stabilizer}
        row=orbit_data[orbit_key]
        assert row['stabilizer']==stabilizer
        row['m']+=1
    predicted=Counter()
    for row in orbit_data.values():
        m,stab=row['m'],row['stabilizer']
        predicted[m*stab*p**(e*r)] += len(hlist)//stab
    assert predicted==direct_full, (p,n,e,strides,name,predicted,direct_full)
    assert sum(multiplicity*count for multiplicity,count in predicted.items()) == full_mod**r
    raw_evaluations=0
    raw_sources=0
    if raw_check:
        # Enumerate full labeled sources h in (Z/p^L)^r, not merely residues.
        grouped=defaultdict(int)
        for h in itertools.product(range(full_mod),repeat=r):
            hred=tuple(v%modulus for v in h)
            by_probe=[]
            for v in hlist:
                advanced=tuple((hi+vi)%full_mod for hi,vi in zip(h,v))
                q0=2
                q1=(q0+p**e*polynomial(name,advanced))%full_mod
                readout=(q1-q0)%full_mod
                assert readout%(p**e)==0
                by_probe.append(readout//p**e)
                raw_evaluations+=1
            raw_signature=tuple(by_probe)
            assert raw_signature==sig[hred]
            grouped[raw_signature]+=1
            raw_sources+=1
        assert Counter(grouped.values())==predicted
        assert raw_sources==full_mod**r
    return {
        'p':p,'L':L,'e':e,'n':n,'r':r,'strides':list(strides),'t':list(t),
        'polynomial':name,'H_size':len(hlist),'cosets':len(coset_reps),
        'distinct_signature_orbits':len(orbit_data),
        'future_observer_fiber_spectrum':[{ 'sources_per_fiber':size,'fiber_count':ct}
                                           for size,ct in sorted(predicted.items())],
        'labeled_sources_per_fixed_q':full_mod**r,
        'residue_sources_exhausted':len(sig),
        'residue_probe_evaluations':len(sig)*len(hlist),
        'full_labeled_sources_actually_checked':raw_sources,
        'full_raw_probe_operations':raw_evaluations,
        'checks':'PASS'
    }


def main():
    cases=[
        (3,1,1,(1,0),'xyy1',True),
        (5,1,1,(1,0),'xyy1',True),
        (7,1,1,(1,0),'xyy1',True),
        (3,1,2,(1,0),'xyy1',True),
        (5,1,2,(1,0),'xyy1',True),
        (3,2,1,(1,0),'xyy1',True),
        (3,2,1,(0,0),'xyy1',True),
        (3,2,1,(2,0),'xyy1',True),
        (5,2,1,(1,0),'xyy1',False),
        (3,2,1,(1,1),'x2_plus_y',True),
        (3,1,1,(1,0),'xy_plus_x2',True),
        (3,1,1,(1,0),'zero',True),
        (3,1,1,(1,0,1),'three_variable',False),
        (3,2,1,(2,1,0),'three_variable',False),
    ]
    out=[case(*c) for c in cases]
    # General closed-form result for n=1, (s_X>=1,s_Y=0), x*y*(y-1).
    for row in out:
        if row['polynomial']=='xyy1' and row['n']==1 and row['strides']==[1,0]:
            p,e=row['p'],row['e']
            target=Counter({p**(2*e):p*(p-1),p**(2*e+1):1})
            actual=Counter({s['sources_per_fiber']:s['fiber_count'] for s in row['future_observer_fiber_spectrum']})
            assert actual==target, (row,actual,target)
            row['closed_form_checked']=True
    # For p=3, two fixed resettable j-probes at different residues cannot suffice.
    p=3
    values={ (x,y):tuple((x*(y+j)*(y+j-1))%p for j in range(p))
             for x,y in itertools.product(range(p),repeat=2)}
    for i,j in itertools.combinations(range(p),2):
        limited=defaultdict(set)
        for a,signature in values.items():
            limited[(signature[i],signature[j])].add(signature)
        assert any(len(b)>1 for b in limited.values()), (i,j)
    assert len(set(values.values()))==7
    certificate={
      'schema':'D25_PARTIAL_HIDDEN_TRANSLATION_ORBIT_MASS_AUTHOR_EXACT_CHECK_V1',
      'model':'AUXILIARY_FINITE_RING_ONLY_NOT_NATIVE_X6',
      'arithmetic':'exact_integer_modular_no_floats',
      'algorithm':'direct full signature grouping vs independent coset-H-orbit stabilizers; selected full labeled source readouts',
      'cases':out,
      'totals':{
        'configs':len(out),
        'residue_sources_exhausted':sum(x['residue_sources_exhausted'] for x in out),
        'residue_probe_evaluations':sum(x['residue_probe_evaluations'] for x in out),
        'full_labeled_sources_actually_checked':sum(x['full_labeled_sources_actually_checked'] for x in out),
        'full_raw_probe_operations':sum(x['full_raw_probe_operations'] for x in out),
      },
      'p3_two_probe_lower_bound':'ALL_THREE_PAIRS_OF_DISTINCT_J_MOD_3_HAVE_COLLISION',
      'result':'PASS',
      'review':'AUTHOR_SIDE_ONLY_UNREVIEWED_NOT_ADMITTED',
    }
    path=Path(__file__).with_name('d25_partial_hidden_translation_orbit_mass_author_check_20261030.json')
    path.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'result':'PASS',**certificate['totals'],'out':str(path)},ensure_ascii=False))
    for x in out:
        print(x['p'],x['n'],x['e'],x['r'],x['strides'],x['polynomial'],
              [(v['sources_per_fiber'],v['fiber_count']) for v in x['future_observer_fiber_spectrum']])

if __name__=='__main__':
    main()
