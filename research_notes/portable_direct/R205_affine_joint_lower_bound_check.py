"""R205: exact F_2 affine observer witness, independent portable checker.
Uses the explicit R201 reset/shift construction, not the installed BRC package.
"""
import json
from math import comb, ceil, log2
from pathlib import Path

M,K,L=12,6,2
A=M*(K+1)
BITS=A.bit_length()  # exactly ceil(log2(A+1)) for positive integer A
S=K+comb(K,2)
D=S+BITS*L
pairs=[(i,j) for i in range(K) for j in range(i+1,K)]

def initial():
    return sum(1<<i for i in range(S))

def update(v,event):
    src=event%(K+1)-1
    if src>=0:
        v &= ~(1<<src)
        for p,(i,j) in enumerate(pairs):
            bit=1<<(K+p)
            if src==i: v &= ~bit
            elif src==j: v |= bit
    tail=(v>>S)&((1<<(BITS*L))-1)
    tail=(tail>>BITS) | ((event+1)<<(BITS*(L-1)))
    return (v&((1<<S)-1)) | (tail<<S)

def apply_word(word):
    v=initial()
    for e in word:v=update(v,e)
    return v

def rank_f2(vectors):
    pivots={}
    for v in vectors:
        while v:
            b=v.bit_length()-1
            if b not in pivots:
                pivots[b]=v
                break
            v^=pivots[b]
    return len(pivots)

# A source-full word with last source label K-1
prefix=tuple(i+1 for i in range(K))
neutral=0
last_src=K
preservers=[d*(K+1)+label for d in range(M) for label in (0,last_src)]
inputs=[apply_word(prefix+(e,)) for e in preservers]
outputs=[update(v,neutral) for v in inputs]
assert len(set(inputs))==2*M
assert len(set(outputs))==2*M
# all same source state, all different latest-2 event prefixes
source_base={v&((1<<S)-1) for v in inputs+outputs}
assert len(source_base)==1
assert rank_f2([v^inputs[0] for v in inputs])>=ceil(log2(2*M))
assert rank_f2([v^outputs[0] for v in outputs])>=ceil(log2(2*M))
# Projector E= two neutral appends fixes source block, erases tail, on differences.
assert all((update(update(v,neutral),neutral)&((1<<S)-1))==(v&((1<<S)-1)) for v in inputs)
# All individual tail basis bits are killed after L neutral shifts.
tail_basis=[1<<(S+i) for i in range(BITS*L)]
def neutral_linear(v):
    return update(v,neutral)^update(0,neutral)
assert all(neutral_linear(neutral_linear(v))==0 for v in tail_basis)
tail_rank=rank_f2([neutral_linear(v) for v in tail_basis])
assert tail_rank==BITS
result={
    'status':'PASS','backend':'PORTABLE_F2_EXACT_REFERENCE','native_package_executed':False,
    'parameters':{'directions':M,'selected_sources':K,'tail_depth':L,'event_alphabet':A,'field':2},
    'source_feature_dim':S,'tail_feature_dim':BITS*L,'r201_upper_dim':D,
    'r205_lower_bound':S+L*ceil(log2(2*M)),
    'source_preserving_distinct_events':len(preservers),
    'fixed_source_fiber_inputs':len(set(inputs)),
    'fixed_source_fiber_after_neutral_append':len(set(outputs)),
    'fiber_output_affine_difference_rank':rank_f2([v^outputs[0] for v in outputs]),
    'neutral_linear_tail_rank_after_one':tail_rank,
    'nilpotence_index_at_most':L,
    'source_base_value_count':len(source_base),
    'claims_scope':'Explicit R201 construction and fixed-fiber witness; universal lower bound from separate proof'
}
print(json.dumps(result,indent=2,ensure_ascii=False))
with Path(__file__).with_name('R205_verification.json').open('w',encoding='utf-8') as f:
    json.dump(result,f,indent=2)
    f.write('\n')
