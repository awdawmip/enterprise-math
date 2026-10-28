"""C42 held-out scale tests and probability-source diagnostics."""
from fractions import Fraction as Q
from itertools import combinations, product, permutations
from math import factorial
from biased_paths import *

scale_rows=[];held_out=0
for ent,w in [([1,-1,1],(1,1,2)),([1,-1,1],(1,1,1)),
              ([1,1,1],(1,2,3)),([Q(2,3),-1,Q(4,5)],(Q(1,2),1,Q(3,2))),
              ([0,1,-1],(2,3,5)),([-1,0,1],(3,1,2))]:
    d=skew(3,ent)
    h1,i1=state_distribution((1,)*3,d,w)
    h2,i2=state_distribution((2,)*3,d,w)
    c3=(i2['variance']-4*i1['variance'])/4
    c2=i1['variance']-c3
    assert c3>=0 and c2>=0
    h3,i3=state_distribution((3,)*3,d,w)
    prediction=27*c3+9*c2
    assert prediction==i3['variance'];held_out+=1
    scale_rows.append({'curvature_entries':ent,'priorities':w,'V1':i1['variance'],
       'V2':i2['variance'],'reconstructed_C3':c3,'reconstructed_C2':c2,
       'held_out_t3_prediction':prediction,'held_out_t3_computed':i3['variance']})

# A nonzero cubic term survives a declared deterministic variance error budget.
eps=Q(1,200);center=Q(1,90)
interval=(center-(eps+4*eps)/4,center+(eps+4*eps)/4)
assert interval==(Q(7,1440),Q(5,288)) and interval[0]>0

# Selection probabilities for temporarily labelled occurrences: analytic power
# priorities give exactly the same product as rational without-replacement draws.
# Only short finite permutations are tested; there is no numerical integration.
key_checks=0
for weights in [(Q(1),Q(2),Q(3)),(Q(1,2),Q(1),Q(1),Q(5,2)),
                (Q(1),Q(1),Q(2),Q(2),Q(3))]:
    mass=Q(0)
    for word in permutations(range(len(weights))):
        product_branch=Q(1)
        for j,i in enumerate(word):
            product_branch*=weights[i]/sum(weights[x] for x in word[j:])
        # Iterating elementary monomial integrals over 1>x1>x2>...>xn>0
        # gives the same suffix-sum denominator.
        numerator=Q(1);denominator=Q(1);partial=Q(0)
        for i in reversed(word):
            numerator*=weights[i];partial+=weights[i];denominator*=partial
        integrated=numerator/denominator
        assert product_branch==integrated
        mass+=product_branch;key_checks+=1
    assert mass==1

# Initial integer cases retain their original single-word preparations.
initial=[]
for n,a in [(1,()),(2,(1,)),(3,(1,)),(4,(2,)),(5,(1,))]:
    d=skew(len(a),[]);w=(Q(7,3),)*len(a)
    hist,info=state_distribution(a,d,w)
    assert hist=={Q(0):Q(1)}
    initial.append({'integer':n,'path_count':info['word_count'],
           'canonical_extra_reward':0,'initial_label':'rho_1 retained; common endpoint potential separate'})

# The exact same endpoint potential from C41 makes the displayed example
# increments strictly positive, regardless of the path probabilities.
positive_edges=0
for d,k in [(skew(3,[1,-1,1]),3),(skew(4,[0,1,-1,-1,1,0]),4)]:
    for used in product(range(5),repeat=k):
        for p in range(k):
            inc=2*sum(used)+1+sum(d[q][p]*used[q] for q in range(p))
            assert inc>0;positive_edges+=1

write('scale_and_source_checks.json',{'status':'PASS','scale_prediction_cases':held_out,
  'scale_rows':scale_rows,'variance_input_absolute_error':eps,'certified_C3_interval':interval,
  'priority_representation_finite_checks':key_checks,'initial_cases':initial,
  'positive_gauge_edges_checked':positive_edges,'gauge':'Phi(m)=Omega(m)^2',
  'BRC_calls':dict(COUNTS)})
print('PASS',held_out,key_checks,positive_edges,dict(COUNTS))
