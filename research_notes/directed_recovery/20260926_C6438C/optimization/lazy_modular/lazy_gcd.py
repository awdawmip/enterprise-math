"""Exact gcd using actual full-adder binary long division at each step."""
from pathlib import Path
import hashlib
from lazy_modular import Arithmetic, digest, require, source_binding, sparse


def typed_gcd_trace(left, right):
    require(sparse.integer(left) and sparse.integer(right), 'integer gcd inputs required')
    # Input sign is a label convention; the arithmetic transducer uses magnitudes.
    a, b = abs(left), abs(right)
    arithmetic = Arithmetic()
    steps = []
    while b:
        quotient, remainder, division = arithmetic.divide(a, b)
        require(0 <= remainder < b, 'typed gcd remainder invariant')
        steps.append({'left':a,'right':b,'quotient':quotient,'remainder':remainder,
                      'division_operation':division})
        a, b = b, remainder
    return {'schema':'BRC_TYPED_LAZY_GCD_V1','left':left,'right':right,'value':a,
            'steps':steps,'arithmetic_operations':arithmetic.operations,
            'cost':{k:v for k,v in arithmetic.stats.items() if k != 'native_kernel_calls_delta'},
            'source':source_binding(),
            'gcd_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'integer_sign_convention':'gcd of absolute input magnitudes; gcd(0,0)=0',
            'dense_euclidean_graph_used':False,'host_remainder_used':False}


def typed_gcd(left, right):
    return typed_gcd_trace(left, right)['value']


def verify_typed_gcd(certificate):
    require(certificate.get('schema') == 'BRC_TYPED_LAZY_GCD_V1', 'wrong typed gcd certificate')
    rebuilt = typed_gcd_trace(certificate['left'], certificate['right'])
    require(digest(rebuilt) == digest(certificate), 'typed gcd trace does not replay')
    return {'verified':True,'value':rebuilt['value'],'certificate_sha256':digest(rebuilt),
            'replayed_adder_digits':rebuilt['cost']['adder_digit_replays']}
