"""R265 exact optimal sequential zero-only labelled observer, frozen science@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Standard-library only. Mod-13 calculations and period check are exact.
Run: python R265_optimal_sequential_observer.py
"""
import json
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path

S, J, T, K, p, P = F(67,169), 1184397599, 989553240, 3805974000, 13, 2184
W=(144,576,1440,4320,17280,86400,518400)

def multiply(c, a):
    z=[F(0)]*(len(c)+1)
    for j,v in enumerate(c):
        z[j]-=a*v; z[j+1]+=v
    return z

def charpoly(ids,a,b):
    c=[F(1)]
    for i in ids:c=multiply(c,a[i])
    for i in ids:
        v=[F(1)]
        for j in ids:
            if j!=i:v=multiply(v,a[j])
        for j,x in enumerate(v):c[j]-=b[i]*x
    return c

def compute_covers():
    t=(1691*S-2615)/(2615*S-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),S,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    covers={}; taps=0
    for m in range(63):
        ids=[0]+[i+1 for i in range(6) if m>>i&1]
        d=len(ids)
        cc=[v*T**(d-j) for j,v in enumerate(charpoly(ids,a,b))]
        assert all(v.denominator==1 for v in cc)
        c=[int(v)%p for v in cc]
        state=[F(1)]*d
        seq=[]
        for k in range(3+d):
            if k>=3:
                v=F(J*T**k,K)*W[m.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ids))
                assert v.denominator==1
                seq.append(int(v)%p)
            total=sum(pi[i]*state[j] for j,i in enumerate(ids))
            state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ids)]
        for n in range(d,P+d):
            seq.append(-sum(c[j]*seq[n-d+j] for j in range(d))%p)
        # Monic induction proves infinite 2184-periodicity for this label.
        assert seq[:d]==seq[P:P+d]
        taps+=d
        covers[m]=sum(1<<i for i in range(P) if seq[i]!=0)
    assert taps==249
    return covers

def cost_and_remaining(order,covers):
    remaining=(1<<P)-1; cost=0; steps=[]
    for m in order:
        steps.append(remaining.bit_count())
        cost+=steps[-1]
        remaining &= ~covers[m]
    return cost,steps,remaining

def run():
    covers=compute_covers()
    groups=defaultdict(list)
    for m in range(63):groups[covers[m]].append(m)
    inactive=groups.pop(0)
    assert len(inactive)==39
    assert len(groups)==6
    reps=sorted(min(v) for v in groups.values())
    assert reps==[9,10,12,13,24,26]
    group_labels=sorted((sorted(v) for v in groups.values()),key=lambda g:g[0])
    assert group_labels==[[9,14,27,29,41,46,59,61],[10,25,30,42,57,62],
                          [12,15,44,47],[13,45],[24,56],[26,58]]
    U=0
    for m in covers:U|=covers[m]
    assert U.bit_count()==2182
    active=sorted(m for m in covers if covers[m])
    assert len(active)==24
    assert all((covers[a]|covers[b]|covers[c])!=U for a,b,c in combinations(active,3))
    full=(1<<P)-1
    @lru_cache(None)
    def opt(S):
        union=0
        for j,m in enumerate(reps):
            if S>>j&1:union|=covers[m]
        if union==U:return 0,()
        wait=(full&~union).bit_count()
        return min((wait+opt(S|(1<<j))[0],(m,)+opt(S|(1<<j))[1])
                   for j,m in enumerate(reps) if not (S>>j&1))
    min_cost,order=opt(0)
    assert opt.cache_info().currsize==64
    assert min_cost==2356 and order==(9,26,10,13)
    expected=(2184,156,12,4)
    cost,steps,remaining=cost_and_remaining(order,covers)
    assert cost==sum(expected) and tuple(steps)==expected and remaining.bit_count()==2
    # Independent 6! enumeration, without DP recurrence.
    brute=10**10
    for perm in permutations(reps):
        subset=0; prefix=[]
        for m in perm:
            prefix.append(m);subset |= covers[m]
            if subset==U:break
        c,_,_=cost_and_remaining(prefix,covers)
        brute=min(brute,c)
    assert brute==min_cost
    valid4=0;best4=10**10
    for q in combinations(active,4):
        if (covers[q[0]]|covers[q[1]]|covers[q[2]]|covers[q[3]])!=U:continue
        valid4+=1
        for perm in permutations(q):best4=min(best4,cost_and_remaining(perm,covers)[0])
    assert valid4==384 and best4==2356
    old_cost,old_steps,_=cost_and_remaining((9,10,13,26),covers)
    assert (old_cost,old_steps)==(2418,[2184,156,52,26])
    cert={
      'schema':'EM_R265_OPTIMAL_SEQUENTIAL_ZERO_OBSERVER_V1',
      'frozen_science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
      'input':{'parameter':'67/169','prime':p,'k_start':3,'period':P,'labels':63},
      'exact_period_shifted_taps_verified':249,
      'active_label_count':24,'identically_zero_label_count':39,
      'distinct_nonzero_coverage_profiles':6,
      'equivalent_source_classes':group_labels,
      'representatives':reps,
      'representative_nonzero_counts':{str(m):covers[m].bit_count() for m in reps},
      'all_nonzero_event_count':2182,'all_zero_event_count':2,
      'minimal_fixed_cover_size':4,'valid_four_label_covers':valid4,
      'globally_optimal_sequential_order':list(order),
      'optimal_total_reads_over_one_period':min_cost,
      'optimal_step_event_counts':steps,
      'optimal_mean_reads_numerator':min_cost,
      'optimal_mean_reads_denominator':P,
      'original_R262_order':[9,10,13,26],
      'original_order_total_reads':old_cost,
      'original_order_step_counts':old_steps,
      'DP_states_checked':64,'all_six_class_permutations_checked':720,
      'verification':'PASS: exact Fraction model, 249 taps, 2184 events, six cover classes, exhaustive small cover and 64-state DP with independent permutations',
      'model_scope':'Boolean zero/nonzero label probes; no phase-index readout; uniform 2184-event workload; auxiliary scalar model only',
      'mathematical_status':'AUTHOR_PROVED / EXACT_FINITE_VERIFICATION / NOT_REVIEWED'
    }
    Path(__file__).with_name('R265_verification.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('R265 PASS: 6 coverage profiles, 64-state DP, optimal 2356/2184 reads, labels 9,26,10,13')
if __name__=='__main__':run()
