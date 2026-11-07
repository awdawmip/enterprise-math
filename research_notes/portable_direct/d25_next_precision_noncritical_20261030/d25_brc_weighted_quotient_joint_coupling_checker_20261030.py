#!/usr/bin/env python3
"""Exact finite checks for weighted observer-quotient transport and joint-coupling obstruction.

Auxiliary finite ring. This is NOT a native Heartbeat World execution.
"""
from collections import Counter
from itertools import product
import json
from pathlib import Path

p,L,e=3,2,1
M=p**L; n=L-e; A=p**n
alphabet=('T','Ux','Uy')

def f(x,y):
    return x*y*(y-1)

def signature(x,y):
    return tuple(f(x % A,(y+j)%A)%A for j in range(A))

def quotient(state):
    q,x,y=state
    return q,signature(x,y)

def source_step(state,op):
    q,x,y=state
    if op=='T': return (q+p**e*f(x,y))%M,x,y
    if op=='Ux': return q,(x+p)%M,y
    if op=='Uy': return q,x,(y+1)%M
    raise ValueError(op)

def quotient_step(z,op):
    q,s=z
    if op=='T': return (q+p**e*s[0])%M,s
    if op=='Ux': return q,s # hidden shift p is zero mod p
    if op=='Uy': return q,s[1:]+s[:1]
    raise ValueError(op)

def word_step(state,word,op):
    for letter in word: state=op(state,letter)
    return state

states=list(product(range(M),repeat=3)) # q1 and two hidden labels
weights={x:1+(x[0]+2*x[1]+3*x[2])%7 for x in states}
assert len(states)==M**3
# Every generator commutes with the observer quotient at every labeled source state.
for z in states:
    for op in alphabet:
        assert quotient(source_step(z,op))==quotient_step(quotient(z),op)
# Arbitrary integer weighted measure pushforward commutes with 121 operation words.
mu=Counter()
for z,w in weights.items(): mu[quotient(z)]+=w
word_count=0
source_transitions=0
for k in range(5):
    for word in product(alphabet,repeat=k):
        direct=Counter()
        for z,w in weights.items():
            direct[quotient(word_step(z,word,source_step))]+=w
            source_transitions+=len(word)
        coarse=Counter()
        for sigma,w in mu.items():
            coarse[word_step(sigma,word,quotient_step)]+=w
        assert direct==coarse,(word,direct,coarse)
        word_count+=1

# Pairwise joint couplings: same exact marginal mass, incompatible equality-event count.
a=(0,0,0)
b=(0,1,0)
assert quotient(a)!=quotient(b)
W=('Uy','Uy','T')
ra=word_step(a,W,source_step)[0]
rb=word_step(b,W,source_step)[0]
assert (ra,rb)==(0,6)
nu_diag=[(a,a),(b,b)]
nu_cross=[(a,b),(b,a)]
def marginal(pairs,idx):return Counter(pair[idx] for pair in pairs)
assert marginal(nu_diag,0)==marginal(nu_cross,0)
assert marginal(nu_diag,1)==marginal(nu_cross,1)
def equality_mass(pairs):
    return sum(word_step(x,W,source_step)[0]==word_step(y,W,source_step)[0] for x,y in pairs)
assert equality_mass(nu_diag)==2 and equality_mass(nu_cross)==0

# Adding undeclared branch/height-sensitive operator splits an old future fiber.
c=(0,0,1)
assert quotient(a)==quotient(c)
def V(z):
    q,x,y=z
    return ((q+int(y%A==1))%M,x,y)
assert V(a)[0]!=V(c)[0]

cert={
 'schema':'D25_WEIGHTED_BRC_QUOTIENT_JOINT_COUNTEREXAMPLE_AUTHOR_CHECK_V1',
 'model':'FINITE_AUXILIARY_RING_NOT_NATIVE_X6',
 'parameters':{'p':p,'L':L,'e':e,'r':2,'strides':{'Ux':1,'Uy':0},'f':'XY(Y-1)'},
 'full_labeled_one_stream_states':len(states),
 'nonzero_weighted_sources':len(weights),
 'total_integer_input_mass':sum(weights.values()),
 'local_generator_commutation_checks':len(states)*len(alphabet),
 'all_operation_words_up_to_length_4':word_count,
 'full_source_generator_applications_in_weighted_checks':source_transitions,
 'joint_couplings':{
   'diagonal_pairs':[['a','a'],['b','b']],
   'cross_pairs':[['a','b'],['b','a']],
   'a_source':list(a),'b_source':list(b),
   'readout_word':list(W),
   'q1_after_word':{'a':ra,'b':rb},
   'both_legs_marginals_equal':True,
   'equality_event_count_diagonal':equality_mass(nu_diag),
   'equality_event_count_cross':equality_mass(nu_cross)
 },
 'additional_operation_obstruction':{'V':'q1 increments by 1 if y mod 3 == 1','sources_same_old_quotient':{'a':list(a),'c':list(c)},'V_readouts':[V(a)[0],V(c)[0]]},
 'status':'PASS','evidence_role':'AUTHOR_EXACT_CHECK_NOT_INDEPENDENT_NOT_NATIVE'
}
out=Path(__file__).with_name('d25_brc_weighted_quotient_joint_coupling_author_check_20261030.json')
out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(json.dumps({'PASS':True,'words':word_count,'states':len(states),'source_applications':source_transitions,'mass':cert['total_integer_input_mass']},ensure_ascii=False))
