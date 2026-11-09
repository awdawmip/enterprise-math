#!/usr/bin/env python3
"""Exact author-side S23/AV circle risk certificate, frozen pin 43ec6098... .
All ordering, maximum and insertion decisions are certified on an open
rational theta interval by testing affine signs at both endpoints.
Requires Python 3 stdlib only. No floating point or sampling of theta.
"""
from bisect import bisect_right
from fractions import Fraction
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
from random import Random
import json

D=10**24
THETA_LOW=Fraction(262204504569236716045286,D)
THETA_HIGH=Fraction(262204504569236716045287,D)
THETA_MID=(THETA_LOW+THETA_HIGH)/2
M=128
N=7621
BASE=1270
DIRECT_CHECKS=(128,492,717,1106,1173,1174,1209,1270,1271,1823,1824,1890,1891,1926,1927,1987,1988,3093,3094,3160,3161,3196,3197,3257,3258,4363,4364,4430,4431,4466,4467,4527,4528,7620,7621)
# (first new cut count, last new cut count, affine delta A+B theta)
EXPECTED_EPOCHS=[
(1271,1823,(0,0)),
(1824,1890,(333,-1270)),
(1891,1926,(0,0)),
(1927,1987,(333,-1270)),
(1988,3093,(0,0)),
(3094,3160,(333,-1270)),
(3161,3196,(0,0)),
(3197,3257,(333,-1270)),
(3258,4363,(0,0)),
(4364,4430,(-854,3257)),
(4431,4466,(0,0)),
(4467,4527,(-854,3257)),
(4528,7620,(0,0)),
(7621,7621,(-854,3257)),
]

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def value(x,theta):return x[0]+x[1]*theta

def certify_nonnegative(x):
    lo=value(x,THETA_LOW);hi=value(x,THETA_HIGH)
    assert lo>=0 and hi>=0, ('not nonnegative throughout interval',x,lo,hi)

def certify_positive(x):
    lo=value(x,THETA_LOW);hi=value(x,THETA_HIGH)
    assert lo>0 and hi>0, ('not positive throughout interval',x,lo,hi)

def phase_affine(i):
    # because i*theta has stable floor at both certified enclosure endpoints
    floor_lo=i*THETA_LOW.numerator//THETA_LOW.denominator
    floor_hi=i*THETA_HIGH.numerator//THETA_HIGH.denominator
    assert floor_lo==floor_hi,('floor unstable',i)
    return (-floor_lo,i)

# use exact midpoint integer residue as a *sorting witness* only; endpoint
# inequalities certify every decision for the full open theta interval
p,q=THETA_MID.numerator,THETA_MID.denominator
key=lambda i:(i*p)%q

def initial_historical_arcs():
    hist=sorted(range(M),key=key)
    keys=[key(i) for i in hist]
    arcs={}
    for k,left in enumerate(hist):
        right=hist[(k+1)%M]
        leftkey=keys[k]
        wrap=key(right)<leftkey
        gap=sub(add(phase_affine(right),(int(wrap),0)),phase_affine(left))
        certify_positive(gap)
        arcs[left]={'left':left,'right':right,'labels':[left,right],
                    'keys':[leftkey,key(right)+(q if wrap else 0)],
                    'max':gap,'anchor_key':leftkey}
    return hist,keys,arcs

def unwrapped(i,arc):
    return add(phase_affine(i),(int(key(i)<arc['anchor_key']),0))

def direct_partition(n):
    # Fully independent one-shot circular sort and interval-max calculation.
    hist,hkeys,_=initial_historical_arcs()
    cuts=sorted(range(n),key=key)
    max_by_owner={}
    for j,u in enumerate(cuts):
        v=cuts[(j+1)%n]
        wrap=int(j==n-1)
        gap=sub(add(phase_affine(v),(wrap,0)),phase_affine(u))
        certify_positive(gap)
        h=hist[(bisect_right(hkeys,key(u))-1)%M]
        if h not in max_by_owner or value(gap,THETA_MID)>value(max_by_owner[h],THETA_MID):
            max_by_owner[h]=gap
    assert len(max_by_owner)==M
    risk=(1,0)
    for g in max_by_owner.values():
        certify_positive(g)
        risk=sub(risk,g)
    certify_nonnegative(risk)
    certify_nonnegative(sub((1,0),risk))
    return risk

def build():
    hist,hkeys,arcs=initial_historical_arcs()
    risk=(0,0);risk_by_n={M:risk}
    rows=[]
    unique_order_checks=0; maxima_checks=0
    for t in range(M,N):
        pk=key(t)
        pos=(bisect_right(hkeys,pk)-1)%M
        h=hist[pos]
        arc=arcs[h]
        unwrapped_key=pk+(q if pk<arc['anchor_key'] else 0)
        spot=bisect_right(arc['keys'],unwrapped_key)
        assert 0<spot<len(arc['keys'])
        labels_before=tuple(arc['labels'])
        x,y=labels_before[spot-1:spot+1]
        oldgap=sub(unwrapped(y,arc),unwrapped(x,arc))
        leftgap=sub(unwrapped(t,arc),unwrapped(x,arc))
        rightgap=sub(unwrapped(y,arc),unwrapped(t,arc))
        certify_positive(leftgap);certify_positive(rightgap)
        assert add(leftgap,rightgap)==oldgap
        unique_order_checks+=2
        oldmax=arc['max']
        arc['labels'].insert(spot,t);arc['keys'].insert(spot,unwrapped_key)
        gaps=tuple(sub(unwrapped(v,arc),unwrapped(u,arc)) for u,v in zip(arc['labels'],arc['labels'][1:]))
        newmax=max(gaps,key=lambda v:value(v,THETA_MID))
        for g in gaps:
            certify_nonnegative(sub(newmax,g))
            maxima_checks+=1
        delta=sub(oldmax,newmax)
        certify_nonnegative(delta)
        arc['max']=newmax
        risk=add(risk,delta)
        risk_by_n[t+1]=risk
        rows.append({'t':t, 'left':h,'right':arc['right'], 'labels':labels_before,
                     'split':(x,y),'gap':oldgap,'new_parts':(leftgap,rightgap),'delta':delta})
    return risk_by_n, rows, unique_order_checks,maxima_checks

def group_translated_fibres(rows):
    # translate within one history adjacency orbit preserving the COMPLETE
    # ordered pre-insertion fibre, both endpoints and the split destination.
    rows=[r for r in rows if r['t']>=BASE]
    groups=[];j=0
    while j<len(rows):
        base=rows[j];k=j+1
        while k<len(rows):
            s=rows[k]['t']-base['t'];nxt=rows[k]
            if (nxt['left']!=base['left']+s or nxt['right']!=base['right']+s
                or nxt['delta']!=base['delta']
                or nxt['labels']!=tuple(x+s for x in base['labels'])
                or nxt['split']!=tuple(x+s for x in base['split'])
                or nxt['gap']!=base['gap'] or nxt['new_parts']!=base['new_parts']):break
            k+=1
        g={'t_start':base['t'],'t_end':rows[k-1]['t'],'count':k-j,
           'historical_arc':[base['left'],base['right']],
           'pre_insertion_labels':list(base['labels']),
           'split_labels':list(base['split']),
           'split_gap':list(base['gap']),
           'split_parts':[list(g) for g in base['new_parts']],
           'risk_increment':list(base['delta'])}
        # Each template translation has a valid historical adjacent arc.
        assert base['left']+g['count']-1<M and base['right']+g['count']-1<M
        groups.append(g);j=k
    assert sum(g['count'] for g in groups)==N-BASE
    return groups

def grouped_epochs(rows):
    rows=[x for x in rows if x['t']>=BASE]
    epochs=[];i=0
    while i<len(rows):
        j=i+1
        while j<len(rows) and rows[j]['delta']==rows[i]['delta']:j+=1
        epochs.append((rows[i]['t']+1,rows[j-1]['t']+1,rows[i]['delta']))
        i=j
    return epochs

def independent_checks(risk_by_n):
    checks=sorted(set(DIRECT_CHECKS)|set(Random(242024).sample(range(BASE,N+1),96)))
    for n in checks:
        assert direct_partition(n)==risk_by_n[n],('independent direct mismatch',n)
    return checks

def main():
    here=Path(__file__).resolve().parent
    R,rows,orderchecks,maxchecks=build()
    assert R[1270]==(-18559,70784)
    epochs=grouped_epochs(rows)
    assert epochs==EXPECTED_EPOCHS,(epochs,EXPECTED_EPOCHS)
    assert R[7620]==R[4527]
    assert R[1823]==R[1270] and R[3093]==R[1987] and R[4363]==R[3257]
    checks=independent_checks(R)
    groups=group_translated_fibres(rows)
    # exact interval statements for nonzero increments and strict breakpoints
    for a,b,delta in epochs:
        if delta!=(0,0):certify_positive(delta)
    with (here/'EPOCHS.tsv').open('w') as f:
        f.write('first_added_n\tlast_added_n\tcount\tdelta_A\tdelta_B\tR_before_A\tR_before_B\tR_after_A\tR_after_B\n')
        for first,last,delta in epochs:
            before=R[first-1];after=R[last]
            f.write(f'{first}\t{last}\t{last-first+1}\t{delta[0]}\t{delta[1]}\t{before[0]}\t{before[1]}\t{after[0]}\t{after[1]}\n')
    (here/'FIBRE_TEMPLATES.json').write_text(json.dumps({'schema':'R24_TRANSLATED_COMPLETE_FIBRE_CERT_V1',
         'theta_lower_num':THETA_LOW.numerator,'theta_upper_num':THETA_HIGH.numerator,
         'theta_den':D,'historical_cuts':M,'from_cut_count':BASE,'to_cut_count':N,
         'groups':groups},ensure_ascii=False,indent=2)+'\n')
    print('SCIENTIFIC_PIN enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34')
    print('OPEN_THETA_INTERVAL',THETA_LOW,THETA_HIGH)
    print('HISTORY_CUTS',M,'VERIFIED_CUT_COUNTS',BASE,'THROUGH',N)
    print('EXACT_UPDATE_COUNT',N-BASE,'ORDER_SIGN_TESTS',orderchecks,'MAX_SIGN_TESTS',maxchecks)
    print('INDEPENDENT_DIRECT_RECONSTRUCTIONS',len(checks),'FIRST_LAST',checks[0],checks[-1])
    print('SOURCE_LABELLED_TRANSLATION_FAMILIES',len(groups),'GROUP_MEMBER_COUNT',sum(g['count'] for g in groups))
    for first,last,d in epochs:
        print('EPOCH',first,last,'steps',last-first+1,'increment',d,'risk_after',R[last])
    for filename in ['EPOCHS.tsv','FIBRE_TEMPLATES.json']:
        p=here/filename;print('ARTIFACT',filename,'BYTES',p.stat().st_size,'SHA256',sha256(p.read_bytes()).hexdigest())
    print('PASS_R24_S23_AV_EXACT_EPOCHS_THROUGH_7621')

if __name__=='__main__':main()
