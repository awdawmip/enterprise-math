"""Public modular-root witnesses for actual uniform terminal suffixes.

The witness b is an independent public input, not an uncharged root-search
or power-of-a oracle. No factor/order or general label-color query is used.
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
from typed_jacobi import typed_jacobi_trace, certify_program_final_bit

STRUCTURE = 'ACTUAL_TYPED_PUBLIC_ROOT_TWO_PART_WITNESS_V1'
PROGRAM = 'ACTUAL_NATIVE_PUBLIC_ROOT_UNIFORM_SUFFIX_V1'


def source():
    return {'root_unity_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic_source':source_binding(),
        'jacobi_source_sha256':hashlib.sha256((JACOBI/'typed_jacobi.py').read_bytes()).hexdigest(),
        'project_snapshot':'671530e485921a9eeed91c1635decd60cc195dc3',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC',
        'uniform_suffix_theorem':{'source_commit':'d8447e4dc9c6500720c671649798e4ae08df2ae2',
            'path':'research_notes/HEARTBEAT94_UNIFORM_SUFFIX_PROOF_20260926.md',
            'git_blob':'6d6552cdcfaa58a609d88b9582ef79bfa3ff0d82'},
        'scope':'shared author domain-operator composition; no new arithmetic primitive or propagator'}


def certify_root_structure(N, a, ell, b):
    """Check public b^(2^(ell-1)) == -1 (mod N) and J(a,N) == -1.

    Each p|N then has 2^ell|p-1. Negative Jacobi forces at least this
    two-part in the order of a, without factoring N or computing that order.
    Distinct b and a are allowed; equality is not mathematically forbidden.
    """
    require(sparse.integer(N) and N >= 3 and (N & 1), 'odd integer N >= 3 required')
    require(sparse.integer(a) and 1 <= a < N, 'canonical positive Shor base required')
    require(sparse.integer(b) and 1 <= b < N, 'canonical positive public root required')
    require(sparse.integer(ell) and ell >= 1, 'positive integer suffix length required')
    # Any true witness forces some p|N to satisfy p >= 2^ell+1.
    # This follows from the theorem and is not a fixed precision restriction.
    require(ell < N.bit_length(), 'root order cannot fit the modulus')
    arithmetic = Arithmetic()
    relation, minus_one, subtraction = arithmetic.compare(N,1)
    require(relation > 0, 'positive modulus-minus-one invariant')
    value, steps = b, []
    for level in range(ell-1):
        following, operations = arithmetic.modmul(value,value,N)
        steps.append({'level':level+1,'input':value,'output':following,
                      'modular_square_operations':operations})
        value = following
    relation, _, comparison = arithmetic.compare(value,minus_one)
    require(relation == 0, 'public modular root does not reach minus one')
    jacobi = typed_jacobi_trace(a,N)
    available = jacobi['value'] == -1
    return {'schema':STRUCTURE,
        'status':'CERTIFIED_TWO_PART_LOWER_BOUND' if available else 'UNAVAILABLE',
        'N':N,'a':a,'ell':ell,'b':b,'public_root_exponent':1 << (ell-1),
        'requested_power_of_two':1 << ell,
        'certified_suffix_bits':ell if available else 0,
        'minus_one':minus_one,'minus_one_subtraction_operation':subtraction,
        'modular_square_steps':steps,'final_residue':value,
        'final_minus_one_comparison_operation':comparison,
        'arithmetic_operations':arithmetic.operations,
        'arithmetic_cost':{k:x for k,x in arithmetic.stats.items() if k != 'native_kernel_calls_delta'},
        'jacobi':jacobi,'source':source(),
        'root_unit_status':'implied by the verified power being minus one modulo odd N',
        'reason':'public modular root and negative Jacobi' if available else 'Jacobi is not minus one',
        'independent_public_witness_parameter':True,
        'root_finding_algorithm_supplied':False,
        'generic_shor_base_order_search_performed':False,'factor_or_shor_base_order_input':False,
        'witness_root_order_certified':1 << ell,
        'a_equals_public_root':a == b,
        'shor_base_order_certified_if_same_root':(1 << ell) if a == b else None,
        'order_scope':'no generic order search; if a equals b this same verified witness also certifies its exact order',
        'bare_work_label_coloring_implemented':False,
        'theorem_conclusion':'2^ell divides ord_N(a)' if available else None,
        'every_prime_factor_congruence':{'modulus':1 << ell,'residue':1},
        'claim_of_nonuniformity_if_unavailable':False,
        'admission':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED'}


def verify_root_structure(certificate):
    require(isinstance(certificate,dict) and certificate.get('schema') == STRUCTURE,
            'wrong public-root structure certificate')
    rebuilt = certify_root_structure(*(certificate[k] for k in ('N','a','ell','b')))
    require(digest(rebuilt) == digest(certificate), 'public-root certificate does not replay')
    return {'verified':True,'status':rebuilt['status'],'certificate_sha256':digest(rebuilt)}


def certify_program_root_suffix(program, ell, b):
    require(sparse.integer(ell) and 1 <= ell <= program.t, 'suffix length outside program')
    canonical = certify_program_final_bit(program)
    structure = certify_root_structure(program.N,program.a,ell,b)
    available = (canonical['status'] == 'CERTIFIED_FINAL_BIT_FAIR'
                 and structure['status'] == 'CERTIFIED_TWO_PART_LOWER_BOUND')
    return {'schema':PROGRAM,
        'status':'CERTIFIED_UNIFORM_TERMINAL_SUFFIX' if available else 'UNAVAILABLE',
        'ell':ell,'suffix_start_depth':program.t-ell,
        'certified_suffix_bits':ell if available else 0,
        'program_witness':canonical,'structure_witness':structure,'source':source(),
        'scope':'all reachable positive-mass histories from canonical work 1; last ell reported bits independent and fair',
        'arbitrary_midrun_state_authorized':False,
        'postmeasurement_field_omission_authorized':False,
        'bare_work_label_coloring_implemented':False,
        'complete_row_oracle_and_recipe_must_be_retained':True}


def verify_program_root_suffix(certificate, program):
    require(isinstance(certificate,dict) and certificate.get('schema') == PROGRAM,
            'wrong public-root program certificate')
    rebuilt = certify_program_root_suffix(program,certificate['ell'],certificate['structure_witness']['b'])
    require(digest(rebuilt) == digest(certificate), 'public-root program certificate does not replay')
    return {'verified':True,'status':rebuilt['status'],'certificate_sha256':digest(rebuilt)}
