#!/usr/bin/env python3
"""Stage391-B: exact, typed X6 observer-fiber/BRC certificate.

No floating point, trig, matrix exponential, or physical time propagation.
H and J_m are declared model-test operators, not asserted heartbeat dynamics.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import reduce
from hashlib import sha256
from itertools import product
from math import factorial
import json
from pathlib import Path
import sys

EM_FROZEN_MAIN = '2af3fc484eb11060b69e0afc1b562bcaf5ad1419'
P000_PIN_BLOB = 'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'
GLOBAL_FROZEN_MAIN = 'bf84bd7c61a2444b59b1da96be57df0e9ae47e53'
W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
PARAMS = {'P': (F(1,4), F(3,4)), 'Q': (F(1,3), F(2,3))}
OPS = tuple(f'{sign}{i}' for i in range(1,7) for sign in ('+', '-')) + ('H', 'S')

@dataclass(frozen=True)
class State:
    a: tuple[int, int, int, int, int, int]
    step: int
    source: str

    def __post_init__(self):
        assert len(self.a) == 6 and all(type(v) is int for v in self.a)
        assert self.step >= 0 and self.source in PARAMS


def B(k:int,z:F)->F:
    assert k in range(4) and 0 <= z <= 1
    return z**k * (1-z)**(3-k)


def audit_and_residuals(source:str):
    x,y=PARAMS[source]
    audits = tuple(B(k,z) - B(k,anchor) for z,anchor in (
        (x,F(1,4)), (x,F(3,4)), (y,F(1,4)), (y,F(3,4))) for k in range(4))
    residuals = tuple((4*B(k,x)+B(k,y))/5 - F(M[k],160) for k in range(4))
    assert len(audits)==16 and len(residuals)==4
    return audits,residuals


def O(s:State):
    audits,r=audit_and_residuals(s.source)
    return (s.a[0:3],s.step,s.source,tuple(audits),tuple(r))


def C(s:State):
    return O(s)+(s.a[3]%2,)


def apply(s:State,op:str):
    a=list(s.a)
    src=s.source
    if op in OPS[:12]:
        index=int(op[1:])-1
        a[index] += 1 if op[0]=='+' else -1
    elif op=='H':
        if a[3]%2:
            a[0] += 1
    elif op=='S':
        src = 'Q' if src=='P' else 'P'
    elif op.startswith('J'):
        target=int(op[1:])
        if a[3]==target:
            a[0] += 1
    else:
        raise ValueError(op)
    return State(tuple(a),s.step+1,src)


def execute_word(s:State,word:tuple[str,...])->State:
    for op in word:
        s=apply(s,op)
    return s


def brc_from_anchor(a:tuple[int,...]):
    """Typed Boolean primitive-axis shortest-word multiplicity (not amplitude)."""
    counts = [abs(i) for i in a]
    n=sum(counts)
    den=1
    for c in counts:
        den *= factorial(c)
    return n,factorial(n)//den


def fr(q:F):
    return [q.numerator,q.denominator]


def produce_certificate():
    s0=State((0,0,0,0,0,0),0,'P')
    s1=State((0,0,0,1,0,0),0,'P')
    assert O(s0)==O(s1) and C(s0)!=C(s1)
    h0,h1=apply(s0,'H'),apply(s1,'H')
    assert h0.a[0]==0 and h1.a[0]==1 and O(h0)!=O(h1)
    assert brc_from_anchor(h0.a[:3])==(0,1)
    assert brc_from_anchor(h1.a[:3])==(1,1)
    assert brc_from_anchor(s0.a)==(0,1) and brc_from_anchor(s1.a)==(1,1)

    e0=State((0,0,0,0,0,0),0,'Q')
    e2=State((0,0,0,2,0,0),0,'Q')
    assert C(e0)==C(e2)
    assert O(apply(e0,'J0'))!=O(apply(e2,'J0'))
    assert brc_from_anchor(e0.a)==(0,1) and brc_from_anchor(e2.a)==(2,1)

    # Exhaustive table for model ops on representatives with same compressed C-state.
    table_checks=0
    for k in range(-3,4):
        for src in PARAMS:
            for step in (0,2):
                left=State((1,-2,3,k,5,-6),step,src)
                right=State((1,-2,3,k+2,17,-19),step,src)
                assert C(left)==C(right)
                for op in OPS:
                    assert C(apply(left,op))==C(apply(right,op)), (left,right,op)
                    table_checks+=1
    assert table_checks==7*2*2*14

    # Finite sampled word replay supplements, rather than replaces, the all-word proof.
    word_checks=0
    pairs=[
        (State((0,0,0,0,0,0),0,'P'),State((0,0,0,2,9,-7),0,'P')),
        (State((3,-2,1,-3,0,0),4,'Q'),State((3,-2,1,5,8,13),4,'Q')),
        (State((-1,2,-3,4,1,2),1,'P'),State((-1,2,-3,-2,-8,4),1,'P')),
    ]
    for left,right in pairs:
        assert C(left)==C(right)
        for length in range(4):
            for word in product(OPS,repeat=length):
                assert C(execute_word(left,word))==C(execute_word(right,word)),(left,right,word)
                word_checks+=1
    assert word_checks==3*(1+14+14**2+14**3)

    aP,rP=audit_and_residuals('P')
    aQ,rQ=audit_and_residuals('Q')
    assert aP!=aQ and rP!=rQ
    cert={
        'schema':'EM_STAGE391B_X6_FIBER_CERT_V1',
        'scientific_input_pins':{'global':GLOBAL_FROZEN_MAIN,'enterprise_math':EM_FROZEN_MAIN,'p000_blob':P000_PIN_BLOB},
        'coordinate_and_method':'selected E1,E2,E3 raw signed chart projection within native X6; separate abstract operation index; exact BRC primitive-axis paths',
        'audit_channels_per_source':16,
        'residual_channels_per_source':4,
        'params_example_not_optimizer_candidate':{src:{'x':fr(PARAMS[src][0]),'y':fr(PARAMS[src][1])} for src in PARAMS},
        'audits':{src:[fr(q) for q in ar] for src,ar in [('P',aP),('Q',aQ)]},
        'residuals':{src:[fr(q) for q in rr] for src,rr in [('P',rP),('Q',rQ)]},
        'operation_alphabet':list(OPS),
        'unrepaired_witness':{'a0':list(s0.a),'a1':list(s1.a),'same_current_observer':O(s0)==O(s1),'different_after_H':O(h0)!=O(h1),'after_H_selected_triples':[list(h0.a[:3]),list(h1.a[:3])], 'selected_BRC_length_and_multiplicity':[list(brc_from_anchor(h0.a[:3])),list(brc_from_anchor(h1.a[:3]))]},
        'parity_repair':{'coordinate':'a4 mod 2','distinguished_classes_per_O_fiber':2,'descent_table_checks':table_checks,'sampled_word_checks':word_checks,'max_sampled_word_length':3},
        'larger_alphabet_counterexample':{'pair_a4':[0,2],'same_parity_observer':C(e0)==C(e2),'operator':'J0','different_next_readout':O(apply(e0,'J0'))!=O(apply(e2,'J0')),'full_native_BRC_length_and_multiplicity':[list(brc_from_anchor(e0.a)),list(brc_from_anchor(e2.a))]},
        'proof_scope':'all native signed X6 chart displacements, two source labels, all words in declared finite alphabet; model-internal symbolic future actions; not an asserted physical heartbeat law or approved native dynamics',
        'verification_scope':'exact Fraction Bernoulli/BRC audit and residual evaluation; exact integer BRC path counts; exhaustive listed operation table and declared finite word replay; all-word result by separate induction in proof note'
    }
    return cert

if __name__=='__main__':
    cert=produce_certificate()
    output=json.dumps(cert,sort_keys=True,ensure_ascii=False,separators=(',',':'))+'\n'
    certpath=Path(__file__).with_name('CERTIFICATE_STAGE391B_X6_FIBER.json')
    certpath.write_bytes(output.encode('utf8'))
    print('STAGE391B_X6_FIBER_EXACT_PASS')
    print('table_checks',cert['parity_repair']['descent_table_checks'])
    print('sampled_word_checks',cert['parity_repair']['sampled_word_checks'])
    print('audit_labels_per_source',cert['audit_channels_per_source'])
    print('residual_channels_per_source',cert['residual_channels_per_source'])
    print('certificate_bytes',len(output.encode('utf8')))
    print('certificate_sha256',sha256(output.encode('utf8')).hexdigest())
