"""Constructive alternatives and state sufficiency checks, all rational."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json, math
import history_memory as h

ROOT=Path(__file__).resolve().parent
stats=defaultdict(int)
r1=tuple(map(F,(1,2,3,1)))
r2=tuple(map(F,(3,1,1,2)))

def mixture(w,rates1=r1,rates2=r2,prior=F(1,2)):
    return prior*h.old.pl_probability(w,rates1)+(1-prior)*h.old.pl_probability(w,rates2)


def four_cross(base,v,u):
    return base[v+(2,3)]*base[u+(3,2)]/(base[v+(3,2)]*base[u+(2,3)])


def mixture_prefix_likelihood(prefix,rates,counts):
    left=list(counts);p=F(1)
    for a in prefix:
        p*=rates[a]*left[a]/sum(rates[j]*left[j] for j in range(4))
        left[a]-=1
    return p


def mixture_state_next(prefix,counts,rates1=r1,rates2=r2,prior=F(1,2)):
    l1=mixture_prefix_likelihood(prefix,rates1,counts)
    l2=mixture_prefix_likelihood(prefix,rates2,counts)
    pi=prior*l1/(prior*l1+(1-prior)*l2)
    rem=[counts[i]-prefix.count(i) for i in range(4)]
    den1=sum(rates1[i]*rem[i] for i in range(4))
    den2=sum(rates2[i]*rem[i] for i in range(4))
    nxt={i:pi*rates1[i]*n/den1+(1-pi)*rates2[i]*n/den2 for i,n in enumerate(rem) if n}
    return pi,nxt

# Static source mixture exhibits non-unit history contrast on 1260.
base={w:mixture(w) for w in h.ALL_WORDS};assert sum(base.values())==1
Q,_=h.terminal_selected(base,F(1,2),F(1,2))
v=h.word('2332');u=h.word('3223')
c1260=h.cross_ratio(Q)
assert c1260==F(13529,12374)

# A second experiment preserves counts, score and last-visible factor as well.
counts=(3,2,1,1)
all2520=tuple(h.words(counts));assert len(all2520)==420
v2=h.word('23322');u2=h.word('32232')
assert h.prefix_state(v2)==h.prefix_state(u2)
base2520={w:mixture(w) for w in all2520}
Q2520,_=h.terminal_selected(base2520,F(1,2),F(1,2))
c2520=four_cross(Q2520,v2,u2)
assert c2520==F(5617,5358)
for rates,theta in [(r1,F(2)),(r2,F(1,2)),(tuple(map(F,(2,2,1,1))),F(3))]:
    bm=h.reference(rates,theta,counts)
    qm,_=h.terminal_selected(bm,F(1,2),F(1,2))
    assert four_cross(qm,v2,u2)==1
    stats['last_visible_rejections_by_extended_witness']+=1

# A single posterior source probability is sufficient for the mixture's
# reference continuation, with exact Bayes updates. Verify all prefixes.
for cc in ((2,2,1,1),(3,2,1,1)):
    ww=tuple(h.words(cc));bb={w:mixture(w) for w in ww}
    prefixes={w[:i] for w in ww for i in range(len(w))}
    for prefix in prefixes:
        pi,prob=mixture_state_next(prefix,cc)
        assert prob==h.old.conditional_next(bb,prefix)
        stats['mixture_posterior_reference_checks']+=1
        for a,p in prob.items():
            rem=[cc[i]-prefix.count(i) for i in range(4)]
            p1=r1[a]*rem[a]/sum(r1[i]*rem[i] for i in range(4))
            p2=r2[a]*rem[a]/sum(r2[i]*rem[i] for i in range(4))
            pi2=pi*p1/(pi*p1+(1-pi)*p2)
            actual,_=mixture_state_next(prefix+(a,),cc) if len(prefix)+1<sum(cc) else (None,None)
            if actual is not None:
                assert pi2==actual
                stats['mixture_posterior_update_checks']+=1

# Positive terminal weighting preserves response-row distinctions and all
# rectangular cross ratios when the column's final observer is shared.
for numerator in range(1,10):
    for denominator in range(1,8):
        # Independently chosen positive row scales and column scales.
        a,b,c,d=F(numerator,11),F(denominator,9),F(3,13),F(5,17)
        row1,row2=F(numerator+2,7),F(denominator+1,5)
        col1,col2=F(2,19),F(7,23)
        original=a*d/(b*c)
        changed=(row1*a*col1)*(row2*d*col2)/((row1*b*col2)*(row2*c*col1))
        assert original==changed
        # Three positive entries admit a rank-one completion at any values.
        completed=b*c/a
        assert a*completed==b*c
        stats['general_rectangle_identities']+=1

# Under unknown even terminal weights the memory contrast is still recovered.
rates=tuple(map(F,(1,2,3,1)));theta=F(2)
mem=h.reference(rates,theta)
for weight in (lambda A,B:F(1,1+(F(A)+F(1,2)*B)**2),
               lambda A,B:F(1,1+(F(A)+F(1,2)*B)**4),
               lambda A,B:1+(F(A)+F(1,2)*B)**2):
    qq=h.old.selected_general(mem,weight)
    assert h.recover_preparation(qq)['theta']==2
    stats['nonquadratic_memory_recoveries']+=1

# A quartic weighting keeps the preparation diagnostics but has different
# out-of-calibration score odds than the quadratic law.
quartic=h.old.selected_general(mem,lambda A,B:F(2)**(-A**4))
info=h.infer(quartic)
assert info['theta']==theta and info['rates']==rates
assert info['u']==info['v']==F(2)**-16
pred=h.predict_all(rates,theta,info['u'],info['v'])
w4=next(w for w in h.ALL_WORDS if h.raw_scores(w)==(4,1))
obs=(quartic[w4]/mem[w4])/(quartic[h.W0]/mem[h.W0])
fitted=(pred[w4]/mem[w4])/(pred[h.W0]/mem[h.W0])
assert obs==F(2)**-256 and fitted==F(2)**-64
stats['quartic_holdout_witnesses']+=1

# Same (A,B) aggregates can hide opposite memory contrasts. Modify only the
# four neutral word probabilities, preserving each of the two fibers.
memQ,_=h.terminal_selected(mem,F(1,2),F(1,2))
modified=dict(memQ)
# Equalize row odds by choosing half of each column mass for each prefix.
cplus=memQ[h.W0]+memQ[h.W30];cminus=memQ[h.W7]+memQ[h.W37]
modified[h.W0]=modified[h.W30]=cplus/2
modified[h.W7]=modified[h.W37]=cminus/2
assert all(v>0 for v in modified.values()) and sum(modified.values())==1
assert h.old.score_mass(modified)==h.old.score_mass(memQ)
assert h.cross_ratio(memQ)==4 and h.cross_ratio(modified)==1
stats['equal_fiber_mass_different_history_witnesses']+=1

# Input sensitivity of contrast; this separates the robust history finding
# from the more demanding complete six-parameter fit.
eps=F(1,100);fac=(1-eps)/(1+eps)
cb=(4*fac*fac,4/(fac*fac))
assert cb[0]>1
mb1=(c1260*fac*fac,c1260/(fac*fac));mb2=(c2520*fac*fac,c2520/(fac*fac))
assert mb1[0]>1 and mb2[0]>1

# Minimal integer in the declared four-prime two-visible-history design.
# For fewer than four visible occurrences one type occurs <=1; the inversion
# count is injective. With counts (2,2), the only repeated-score pair is below.
assert h.raw_scores(h.word('2332'))==h.raw_scores(h.word('3223'))
primes=(2,3,5,7,11,13)
candidates=[]
for p,q in combinations(primes,2):
    for r,s in combinations([x for x in primes if x not in (p,q)],2):
        candidates.append((p*p*q*q*r*s,(p,q,r,s)))
assert min(candidates)[0]==1260
stats['minimal_design_finite_checks']=len(candidates)

out={'status':'ALL_ASSERTIONS_PASSED','counts':dict(stats),
     'mixture1260':{'rates1':r1,'rates2':r2,'prior':F(1,2),'cross':c1260,'input_1pct_range':mb1},
     'mixture2520':{'histories':('23322','32232'),'cross':c2520,'input_1pct_range':mb2,
                    'posterior_regime1':{h.text(p):mixture_state_next(p,counts)[0] for p in (v2,u2)}},
     'memory4_range':cb,'same_fiber_contrast_change':(h.cross_ratio(memQ),h.cross_ratio(modified)),
     'quartic_test':{'word':h.text(w4),'actual_corrected_odds':obs,'quadratic_prediction':fitted}}
(ROOT/'results'/'diagnostics.json').write_text(json.dumps(h.serialise(out),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(stats),indent=2))
print('STATIC MIXTURE',c1260,float(c1260),'EXTENDED',c2520,float(c2520))
print('CONTRAST 1PCT',[float(x) for x in cb])
print('MIXTURE extended posterior',[(h.text(p),mixture_state_next(p,counts)[0]) for p in (v2,u2)])
