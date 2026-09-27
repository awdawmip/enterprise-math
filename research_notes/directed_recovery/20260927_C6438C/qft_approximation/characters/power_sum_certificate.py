"""A public arithmetic witness for a multi-bit actual uniform suffix.

No factor, order or discrete-log input is accepted. This certifies a lower
bound on the two-part of the order, not a general bare-label color oracle.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1] / 'sep26-shor-general'
JACOBI = ROOT.parents[1] / 'sep27-qft-research/character_certificates'
for path in (PREVIOUS / 'optimization/lazy_modular', JACOBI):
    sys.path.insert(0, str(path))
from lazy_modular import Arithmetic, digest, require, sparse, source_binding
from lazy_gcd import typed_gcd_trace
from typed_jacobi import typed_jacobi_trace, certify_program_final_bit

STRUCTURE = 'ACTUAL_TYPED_POWER_SUM_TWO_PART_WITNESS_V1'
PROGRAM = 'ACTUAL_NATIVE_POWER_SUM_UNIFORM_SUFFIX_V1'


def source():
    return {'power_sum_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic_source': source_binding(),
        'jacobi_source_sha256': hashlib.sha256((JACOBI/'typed_jacobi.py').read_bytes()).hexdigest(),
        'gcd_source_sha256': hashlib.sha256((PREVIOUS/'optimization/lazy_modular/lazy_gcd.py').read_bytes()).hexdigest(),
        'project_snapshot': '671530e485921a9eeed91c1635decd60cc195dc3',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC',
        'uniform_suffix_theorem': {'source_commit':'d8447e4dc9c6500720c671649798e4ae08df2ae2',
            'path':'research_notes/HEARTBEAT94_UNIFORM_SUFFIX_PROOF_20260926.md',
            'git_blob':'6d6552cdcfaa58a609d88b9582ef79bfa3ff0d82'},
        'scope':'shared author domain-operator composition; no new arithmetic primitive or propagator'}


def certify_power_sum_structure(N, a, ell, u, v):
    """Check N=u^(2^(ell-1))+v^(2^(ell-1)), gcd(u,v)=1, J(a,N)=-1.

    For every prime p dividing this primitive odd power sum, 2^ell divides
    p-1. A negative Jacobi symbol then forces 2^ell to divide ord_N(a).
    Only the displayed integer witness is evaluated; no factor or order is.
    """
    require(sparse.integer(N) and N >= 3 and (N & 1), 'odd integer N >= 3 required')
    require(sparse.integer(a) and 1 <= a < N, 'canonical positive base required')
    require(sparse.integer(ell) and ell >= 1, 'positive integer suffix length required')
    require(sparse.integer(u) and sparse.integer(v) and u >= 1 and v >= 1,
            'positive integer power-sum witnesses required')
    require((u & 1) != (v & 1), 'power-sum witnesses must have opposite parity')
    # Since one witness is >=2, any true witness has 2^(ell-1)<bit_length(N).
    # This structural rejection prevents enormous shifts for malformed inputs;
    # it is not a fixed-width or fixed-precision restriction.
    require(ell <= (N.bit_length()-1).bit_length(), 'claimed power-sum degree cannot fit N')
    gcd = typed_gcd_trace(u, v)
    require(gcd['value'] == 1, 'primitive power-sum witness required')
    arithmetic, powers = Arithmetic(), []
    for label, value in (('u',u),('v',v)):
        initial, steps = value, []
        for level in range(ell-1):
            following, operation = arithmetic.multiply(value, value)
            relation, _, comparison = arithmetic.compare(following, N)
            require(relation < 0, 'individual witness power is already at least N')
            steps.append({'level':level+1,'input':value,'output':following,
                          'square_operation':operation,'below_N_comparison':comparison})
            value = following
        powers.append({'label':label,'initial':initial,'steps':steps,'value':value})
    total, addition = arithmetic.add(powers[0]['value'],powers[1]['value'])
    relation, _, comparison = arithmetic.compare(total,N)
    require(relation == 0, 'typed power sum does not equal N')
    jacobi = typed_jacobi_trace(a,N)
    available = jacobi['value'] == -1
    return {'schema':STRUCTURE,
        'status':'CERTIFIED_TWO_PART_LOWER_BOUND' if available else 'UNAVAILABLE',
        'N':N,'a':a,'ell':ell,'u':u,'v':v,'degree':1 << (ell-1),
        'requested_power_of_two':1 << ell,
        'certified_suffix_bits':ell if available else 0,
        'primitive_witness_gcd':gcd,'powers':powers,'sum':total,
        'addition_operation':addition,'sum_comparison_operation':comparison,
        'arithmetic_operations':arithmetic.operations,
        'arithmetic_cost':{k:x for k,x in arithmetic.stats.items() if k != 'native_kernel_calls_delta'},
        'jacobi':jacobi,'source':source(),
        'reason':'public primitive power sum and negative Jacobi' if available else 'Jacobi is not minus one',
        'order_value_computed':False,'factor_or_order_input':False,
        'bare_work_label_coloring_implemented':False,
        'theorem_conclusion':'2^ell divides ord_N(a)' if available else None,
        'claim_of_nonuniformity_if_unavailable':False,
        'admission':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED'}


def verify_power_sum_structure(certificate):
    require(isinstance(certificate,dict) and certificate.get('schema') == STRUCTURE,
            'wrong power-sum structure certificate')
    rebuilt = certify_power_sum_structure(*(certificate[k] for k in ('N','a','ell','u','v')))
    require(digest(rebuilt) == digest(certificate), 'power-sum certificate does not replay')
    return {'verified':True,'status':rebuilt['status'],'certificate_sha256':digest(rebuilt)}


def certify_program_suffix(program, ell, u, v):
    """Bind the new lower-bound witness to the original actual square program.

    The existing actual source/schedule/initial-state contract is retained.
    No arbitrary intermediate field or private latent label is certified.
    """
    require(sparse.integer(ell) and 1 <= ell <= program.t, 'suffix length outside program')
    canonical = certify_program_final_bit(program)
    structure = certify_power_sum_structure(program.N,program.a,ell,u,v)
    available = (canonical['status'] == 'CERTIFIED_FINAL_BIT_FAIR'
                 and structure['status'] == 'CERTIFIED_TWO_PART_LOWER_BOUND')
    return {'schema':PROGRAM,
        'status':'CERTIFIED_UNIFORM_TERMINAL_SUFFIX' if available else 'UNAVAILABLE',
        'ell':ell,'suffix_start_depth':program.t-ell,
        'certified_suffix_bits':ell if available else 0,
        'program_witness':canonical,'structure_witness':structure,
        'source':source(),
        'scope':'all reachable positive-mass histories from canonical work 1; last ell reported bits independent and fair',
        'arbitrary_midrun_state_authorized':False,
        'postmeasurement_field_omission_authorized':False,
        'bare_work_label_coloring_implemented':False,
        'complete_row_oracle_and_recipe_must_be_retained':True}


def verify_program_suffix(certificate, program):
    require(isinstance(certificate,dict) and certificate.get('schema') == PROGRAM,
            'wrong power-sum program certificate')
    structure = certificate['structure_witness']
    rebuilt = certify_program_suffix(program,certificate['ell'],structure['u'],structure['v'])
    require(digest(rebuilt) == digest(certificate), 'power-sum program certificate does not replay')
    return {'verified':True,'status':rebuilt['status'],'certificate_sha256':digest(rebuilt)}
