#!/usr/bin/env python3
"""R130 sparse, exact one-parameter S23 event log.

No floating-point. All rational operations use fractions.Fraction.
Proof obligations and complexity scope in PROOF.md.
"""
from fractions import Fraction as F
from collections import defaultdict
from random import Random
from pathlib import Path
import json

def frac(z):
    return z - (z.numerator // z.denominator)

def indicator(x,A,d,E,i,t):
    return int(frac(x+(A+i*d)*t) < frac(E*t))

def word(x,A,d,E,m,t):
    return tuple(indicator(x,A,d,E,i,t) for i in range(m))

def integer_roots(b,s,l,h):
    if s == 0:
        return ()
    lo,hi=sorted((b+s*l,b+s*h))
    first=(lo.numerator//lo.denominator)+1
    last=((hi.numerator+hi.denominator-1)//hi.denominator)-1
    return tuple((F(z)-b)/s for z in range(first,last+1))

def sparse_sweep(x,A,d,E,m,l,h):
    assert m>=1 and l<h
    affected=defaultdict(set)
    for p in integer_roots(F(0),E,l,h):
        affected[p].update(range(m))
    for i in range(m):
        si=A+i*d
        for p in integer_roots(x,si,l,h):
            affected[p].add(i)
        for p in integer_roots(x,si-E,l,h):
            affected[p].add(i)
    cuts=sorted(affected)
    first=(l+cuts[0])/2 if cuts else (l+h)/2
    state=list(word(x,A,d,E,m,first))
    init=state[:]
    events=[]
    evaluations=m
    for k,p in enumerate(cuts):
        right=(p+(cuts[k+1] if k+1<len(cuts) else h))/2
        changed=sorted(affected[p])
        cut_delta=[]
        right_delta=[]
        for i in changed:
            c=indicator(x,A,d,E,i,p)
            r=indicator(x,A,d,E,i,right)
            evaluations += 2
            if c != state[i]:
                cut_delta.append([i,c])
            if r != state[i]:
                right_delta.append([i,r])
        for i,new in right_delta:
            state[i]=new
        events.append({'theta':str(p),'cut_delta':cut_delta,'right_delta':right_delta,'affected':changed})
    return {'initial_word':init,'events':events,'evaluations':evaluations,'cuts':len(cuts),
            'total_incidence':sum(len(s) for s in affected.values()),
            'total_saved_deltas':sum(len(e['cut_delta'])+len(e['right_delta']) for e in events)}

def verify_instance(x,A,d,E,m,l,h):
    log=sparse_sweep(x,A,d,E,m,l,h)
    events=log['events']; cutlist=[F(e['theta']) for e in events]
    initial_pt=(l+cutlist[0])/2 if cutlist else (l+h)/2
    state=log['initial_word'][:]
    assert tuple(state)==word(x,A,d,E,m,initial_pt)
    signatures={tuple(state)}
    checked=1
    for k,e in enumerate(events):
        cut=F(e['theta'])
        cut_state=state[:]
        for i,v in e['cut_delta']:
            cut_state[i]=v
        assert tuple(cut_state)==word(x,A,d,E,m,cut)
        signatures.add(tuple(cut_state))
        for i,v in e['right_delta']:
            state[i]=v
        midpoint=(cut+(cutlist[k+1] if k+1<len(cutlist) else h))/2
        assert tuple(state)==word(x,A,d,E,m,midpoint)
        signatures.add(tuple(state))
        checked+=2
    assert log['evaluations']==m+2*log['total_incidence']
    return {'cuts':log['cuts'],'signatures':len(signatures),'positions_checked':checked,
            'sparse_evaluations':log['evaluations'],'dense_evaluations':m*checked,
            'delta_count':log['total_saved_deltas'],'incidences':log['total_incidence']}

def main():
    rng=Random(13020261113)
    instances=[]
    edges=[(F(0),0,0,0,8,F(0),F(1)),(F(0),0,1,1,10,F(0),F(1)),
           (F(1,7),-5,5,10,6,F(-2),F(-3,2)),(F(0),2,0,0,7,F(-3),F(3)),
           (F(0),0,0,1,6,F(-1),F(1)),(F(1,2),2,-1,0,8,F(-1,2),F(3,2)),
           (F(0),10,1,2,12,F(0),F(1)),(F(0),1,0,1,20,F(0),F(1))]
    for vals in edges:
        instances.append(verify_instance(*vals))
    for _ in range(250):
        m=rng.randint(1,10)
        x=F(rng.randint(-7,7),rng.randint(1,9))
        A,d,E=[rng.randint(-8,8) for _ in range(3)]
        l=F(rng.randint(-9,5),rng.randint(1,7))
        h=l+F(rng.randint(1,10),rng.randint(1,6))
        instances.append(verify_instance(x,A,d,E,m,l,h))
    B=10**100
    large=verify_instance(F(1,13),B+2,-B-1,2*B+3,5,F(0),F(1,B))
    scalable=[]
    for m in (16,32,64):
        scalable.append({'m':m,**verify_instance(F(0),0,1,1,m,F(0),F(1))})
    report={'status':'R130_SPARSE_SWEEP_PASS','seed':13020261113,'random_instances':250,
            'edge_instances':len(edges),'all_instances':len(instances)+1+len(scalable),
            'exact_representatives_verified':sum(x['positions_checked'] for x in instances)+large['positions_checked']+sum(x['positions_checked'] for x in scalable),
            'summary':{k:sum(x[k] for x in instances) for k in ['cuts','positions_checked','sparse_evaluations','dense_evaluations','delta_count','incidences']},
            'large_100_digit':large,'scaling':scalable}
    print(json.dumps(report,indent=2,sort_keys=True))
    with Path(__file__).with_name('verification_r130.json').open('w') as f:
        json.dump(report,f,indent=2,sort_keys=True)

if __name__=='__main__':main()
