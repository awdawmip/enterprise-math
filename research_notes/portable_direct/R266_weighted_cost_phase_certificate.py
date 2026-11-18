"""R266: exact heterogeneous class-cost and phase-biased sequential observers.
Frozen 63-source positive-rational auxiliary science @ 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
No third-party libraries. Run: python R266_weighted_cost_phase_certificate.py
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

S=F(67,169); J=1184397599; T=989553240; K=3805974000
P=2184; PRIME=13
REPS=(9,10,12,13,24,26)
W=(144,576,1440,4320,17280,86400,518400)

def mul(poly,root):
    nxt=[F(0)]*(len(poly)+1)
    for i,v in enumerate(poly):nxt[i]-=root*v;nxt[i+1]+=v
    return nxt

def charpoly(ids,a,b):
    pol=[F(1)]
    for i in ids:pol=mul(pol,a[i])
    for i in ids:
        q=[F(1)]
        for j in ids:
            if i!=j:q=mul(q,a[j])
        for j,v in enumerate(q):pol[j]-=b[i]*v
    return pol

def labelled_supports():
    t=(1691*S-2615)/(2615*S-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),S,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    taps=0;covers={}
    for m in range(63):
        ids=[0]+[i+1 for i in range(6) if (m>>i)&1]
        d=len(ids)
        poly=[v*T**(d-i) for i,v in enumerate(charpoly(ids,a,b))]
        assert all(v.denominator==1 for v in poly)
        coeff=[int(v)%PRIME for v in poly]
        state=[F(1)]*d;seq=[]
        for k in range(3+d):
            if k>=3:
                q=F(J*T**k,K)*W[m.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ids))
                assert q.denominator==1
                seq.append(int(q)%PRIME)
            total=sum(pi[i]*state[j] for j,i in enumerate(ids))
            state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ids)]
        for n in range(d,P+d):
            seq.append(-sum(coeff[j]*seq[n-d+j] for j in range(d))%PRIME)
        assert seq[:d]==seq[P:P+d],m
        taps+=d
        covers[m]=sum(1<<i for i in range(P) if seq[i]!=0)
    assert taps==249
    groups=defaultdict(list)
    for m,v in covers.items():groups[v].append(m)
    assert len(groups)==7 and len(groups[0])==39
    assert sorted(min(v) for k,v in groups.items() if k)==list(REPS)
    return covers,groups,taps

def permutation_lines(covers,kind):
    full=(1<<P)-1
    union=0
    for v in covers.values():union|=v
    phase_mask=sum(1<<i for i in range(0,P,6))
    assert union.bit_count()==2182
    lines={}
    for perm in permutations(REPS):
        remainder=full;a=b=0;order=[]
        for m in perm:
            order.append(m)
            if kind=='class9':
                if m==9:b+=remainder.bit_count()
                else:a+=remainder.bit_count()
            elif kind=='phase0':
                b+=(remainder&phase_mask).bit_count()
                a+=(remainder&~phase_mask).bit_count()
            else:raise ValueError(kind)
            remainder &= ~covers[m]
            if (remainder&union)==0:break
        key=(a,b)
        if key not in lines or tuple(order)<lines[key]:lines[key]=tuple(order)
    return lines

def hull(lines):
    # Find exact lower envelope of a+b*x over x>=1.
    # Sorted slopes descending; successive switching points increase.
    best_by_slope={}
    for (a,b),order in lines.items():
        if b not in best_by_slope or (a,order)<(best_by_slope[b][0],best_by_slope[b][1]):
            best_by_slope[b]=(a,order)
    stack=[]
    for b in sorted(best_by_slope,reverse=True):
        a,order=best_by_slope[b]
        start=None
        while stack:
            aa,bb,oo,prev=stack[-1]
            x=F(a-aa,bb-b)
            if prev is not None and x<=prev:stack.pop()
            else:start=x;break
        stack.append((a,b,order,start))
    current=[]
    for i,(a,b,order,start) in enumerate(stack):
        end=stack[i+1][3] if i+1<len(stack) else None
        if end is not None and end<=1:continue
        current.append((max(F(1),start) if start is not None else F(1),a,b,order))
    assert current[0][0]==1
    for i,(begin,a,b,order) in enumerate(current):
        end=current[i+1][0] if i+1<len(current) else begin+1
        test=(begin+end)/2
        assert a+b*test==min(aa+bb*test for aa,bb in lines)
    return current

def run():
    covers,groups,taps=labelled_supports()
    expected_classes=[[9,14,27,29,41,46,59,61],[10,25,30,42,57,62],
        [12,15,44,47],[13,45],[24,56],[26,58]]
    classes=sorted((sorted(v) for k,v in groups.items() if k),key=lambda g:g[0])
    assert classes==expected_classes
    class_lines=permutation_lines(covers,'class9')
    phase_lines=permutation_lines(covers,'phase0')
    class_segments=hull(class_lines)
    phase_segments=hull(phase_lines)
    assert class_segments==[(F(1),172,2184,(9,26,10,13)),
         (F(169,168),2200,168,(26,9,10,13)),
         (F(15,14),2380,0,(26,12,10,13))],class_segments
    assert phase_segments==[(F(1),1936,420,(9,26,10,13)),
         (F(3,2),1972,396,(26,9,10,13)),
         (F(5),1992,392,(26,10,9,13)),
         (F(8),2216,364,(10,26,9,13))],phase_segments
    def exhaustive(lines,x):return min(a+b*x for a,b in lines)
    for x in (F(1),F(1001,1000),F(169,168),F(21,20),F(15,14),F(2)):
        assert exhaustive(class_lines,x)==min(a+b*x for start,a,b,order in class_segments)
    for x in (F(1),F(5,4),F(3,2),F(2),F(5),F(8),F(9)):
        assert exhaustive(phase_lines,x)==min(a+b*x for start,a,b,order in phase_segments)
    cert={
      'schema':'EM_R266_WEIGHTED_SEQUENTIAL_OBSERVER_EXACT_ENVELOPES_V1',
      'frozen_scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      'auxiliary_parameter':'67/169','prime':13,'k_start':3,'event_period':2184,
      'shifted_recurrence_taps_verified':taps,
      'source_classes':classes,
      'model':'Boolean nonzero original-label queries; 63 labels; 39 identically zero; 6 active profile classes; query cost positive; no event phase directly visible; all 2184 events must be correctly classified',
      'all_zero_events_per_period':2,
      'permutations_checked_per_family':720,
      'distinct_cost_affine_lines':{'class9':len(class_lines),'phase0':len(phase_lines)},
      'class9_cost_parameter':'theta>=1 multiplies probe cost for every one of the eight equivalent class-9 labels; all other active label classes cost 1',
      'class9_pieces':[{'from_theta':str(x),'objective':f'{a}+{b}*theta','order':list(o)} for x,a,b,o in class_segments],
      'phase0_weight_parameter':'alpha>=1 multiplies weight of phase n=(k-3)%2184 with n%6=0; all other 1820 phases weight 1; each probe costs 1',
      'phase0_total_population_weight':'1820+364*alpha',
      'phase0_pieces':[{'from_alpha':str(x),'objective':f'{a}+{b}*alpha','order':list(o)} for x,a,b,o in phase_segments],
      'verification':'PASS exact Fraction enumeration, recurrence periodicity, support grouping, 720 permutations per family, exact rational lower-envelope computation with independent sample/breakpoint checks',
      'scope':'Auxiliary positive-rational scalar model and Boolean support oracle only. Does not reconstruct all labelled values or native typed BRC ports.'
    }
    path=Path(__file__).with_name('R266_verification.json')
    path.write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print('R266 PASS: class9 breakpoints 169/168,15/14; phase0 breakpoints 3/2,5,8; 249 recurrence taps')
    print('lines',len(class_lines),len(phase_lines))
    return cert
if __name__=='__main__':run()
