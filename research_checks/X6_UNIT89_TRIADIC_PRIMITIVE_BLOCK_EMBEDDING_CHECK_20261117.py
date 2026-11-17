#!/usr/bin/env python3
"""Independent exact integer test of typed X6 signed triad-event -> 3-primitive-block embedding.

Frozen premise: six named signed integer axes, 12 primitive +/-e_i operations,
160 simultaneous triad event types choosing 3 distinct axes and 8 signs.
This checker makes no claim about time-labeled native physical realization.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path
import hashlib
import json

N=6
ZERO=(0,)*N
D=(1,)*N

def add(u,v):
    return tuple(a+b for a,b in zip(u,v))

def neg(u):
    return tuple(-a for a in u)

def sub(u,v):
    return tuple(a-b for a,b in zip(u,v))

def point(steps):
    z=[0]*N
    for i,s in steps:
        z[i]+=s
    return tuple(z)

def minzero(z):
    mn=min(z)
    return tuple(v-mn for v in z)

def cover0(z,m):
    return len(set(z))==1 and z[0]%m==0

TRIADS=tuple(tuple(zip(axes,sgns))
             for axes in combinations(range(N),3)
             for sgns in product((-1,1),repeat=3))
assert len(TRIADS)==160
triad_endpoints=tuple(point(t) for t in TRIADS)
assert len(set(triad_endpoints))==160

# Independent integer triadic two-event census.
triad_two=Counter(add(u,v) for u in triad_endpoints for v in triad_endpoints)
assert sum(triad_two.values())==160**2
triad_two_cell=triad_two[ZERO]
triad_two_cover1=sum(v for z,v in triad_two.items() if cover0(z,1))
assert triad_two_cell==160 and triad_two_cover1==200

# Distinct-axis primitive blocks are the six permutations of each signed triad.
BLOCKS=tuple(tuple(q) for t in TRIADS for q in permutations(t))
assert len(BLOCKS)==960 and len(set(BLOCKS))==960
assert len(set(point(w) for w in BLOCKS))==160
block_counts=Counter(point(w) for w in BLOCKS)
assert set(block_counts.values())=={6}

# Exact direct 960^2 count of 6-primitive-step words constrained blockwise.
block_six=Counter()
block_endpoints=tuple(point(w) for w in BLOCKS)
for p in block_endpoints:
    for q in block_endpoints:
        block_six[add(p,q)]+=1
assert sum(block_six.values())==960**2
assert all(block_six[z]==36*count for z,count in triad_two.items())
assert len(block_six)==len(triad_two)

# Independent unrestricted 12-direction primitive BRC dynamic program through 6 steps.
primitive=tuple(point(((i,s),)) for i in range(N) for s in (-1,1))
states=Counter({ZERO:1})
for _ in range(6):
    nxt=Counter()
    for u,cnt in states.items():
        for d in primitive:
            nxt[add(u,d)]+=cnt
    states=nxt
# Direct sparse integer transition, independently of native closed-form kernel.
assert sum(states.values())==12**6
native_six_cell=states[ZERO]
native_six_cover1=sum(v for z,v in states.items() if cover0(z,1))
assert native_six_cell==19920 and native_six_cover1==21360

# Four-event return via independent two-event midpoint convolution, avoiding 160^4.
triad_four_cell=sum(cnt*triad_two[neg(z)] for z,cnt in triad_two.items())
triad_four_plus2=sum(cnt*triad_two[sub(tuple(2 for _ in range(N)),z)] for z,cnt in triad_two.items())
triad_four_minus2=sum(cnt*triad_two[sub(tuple(-2 for _ in range(N)),z)] for z,cnt in triad_two.items())
assert triad_four_cell==460320
assert triad_four_plus2==triad_four_minus2==1860
assert triad_four_cell+triad_four_plus2+triad_four_minus2==464040

# Independent closed primitive length-12 count via exact multinomial coefficients.
# Each axis has k_i plus and k_i minus uses, sum k_i=6.
def comps(total,k,prefix=()):
    if k==1:
        yield prefix+(total,)
    else:
        for a in range(total+1):
            yield from comps(total-a,k-1,prefix+(a,))
primitive_twelve_cell=sum(factorial(12)//__import__('math').prod(factorial(k)**2 for k in ks)
                         for ks in comps(6,6))
assert primitive_twelve_cell==8175770064

# Endpoint-level witness already at one block: +e_0+e_0+e_0 is allowed natively,
# but impossible with three-distinct-axis block support.
repeated_axis_witness=(3,0,0,0,0,0)
assert repeated_axis_witness not in block_counts

summary={
 'schema':'EM_X6_UNIT89_EXACT_BLOCK_EMBEDDING_CHECK_V1',
 'date':'2026-11-17',
 'axes':6,
 'primitive_signed_alphabet':12,
 'simultaneous_signed_triad_alphabet':160,
 'distinct_axis_primitive_blocks':len(BLOCKS),
 'two_triad_event_words':160**2,
 'six_primitive_blockwise_distinct_words':len(BLOCKS)**2,
 'six_primitive_unrestricted_words':12**6,
 'triad_two_cell_return':triad_two_cell,
 'triad_two_cover_mod1_return':triad_two_cover1,
 'block_six_cell_return':block_six[ZERO],
 'block_six_cover_mod1_return':sum(v for z,v in block_six.items() if cover0(z,1)),
 'native_six_cell_return':native_six_cell,
 'native_six_cover_mod1_return':native_six_cover1,
 'unrestricted_minus_block_cell_L2':native_six_cell-block_six[ZERO],
 'unrestricted_minus_block_cover1_L2':native_six_cover1-sum(v for z,v in block_six.items() if cover0(z,1)),
 'four_triad_event_cell_return':triad_four_cell,
 'four_triad_event_cover_mod2_return':triad_four_cell+triad_four_plus2+triad_four_minus2,
 'four_triad_event_nonzero_mod2_diagonal_per_sign':triad_four_plus2,
 'twelve_primitive_blockwise_distinct_cell_return':6**4*triad_four_cell,
 'twelve_primitive_unrestricted_cell_return':primitive_twelve_cell,
 'first_endpoint_witness_primitive_not_triad_block':repeated_axis_witness,
 'six_step_endpoint_multiplicity_classes':len(states),
 'six_step_blockwise_endpoint_multiplicity_classes':len(block_six),
 'two_event_endpoint_multiplicity_classes':len(triad_two),
 'verified_block_projection_identity_L2':True,
 'verified_zero_failures':True,
 'native_R063_Helly_benchmarks_executed':False
}
encoded=(json.dumps(summary,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
result_path=Path(__file__).with_name('X6_UNIT89_TRIADIC_PRIMITIVE_BLOCK_EMBEDDING_RESULTS_20261117.json')
with result_path.open('wb') as f:f.write(encoded)
print(json.dumps({'result_sha256':hashlib.sha256(encoded).hexdigest(),**summary},sort_keys=True))
