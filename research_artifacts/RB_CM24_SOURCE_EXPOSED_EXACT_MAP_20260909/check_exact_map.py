"""Source-exposed RB CM24, using the existing task-local integer polynomial API.

The coefficient generators are formal: a=alpha, b=beta, c=i.  No root or
integer quotient is evaluated.  Function fractions retain their denominators.
The first checkpoint checks full function-field identities, not the whole task.
"""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from research_artifacts.RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908 import check_squareclass_rr as base

REL = 'research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909'
FREEZE_SHA256 = '85946a8cb4e736021cef6cd311c8cfffbde1cce34fe728255db4b6703f5887f2'
BASE_SHA256 = '32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269'
_deadline_ns = None
_job = None
_max_terms = 0
_max_bits = 0
_calls = {'add': 0, 'multiply': 0, 'scale': 0, 'twice_delta': 0, 'rr_fiber_difference': 0}


class ResourceBoundary(RuntimeError):
    pass


def enforce_limits(policy):
    """Apply the declared process memory and wall-clock limits before a run."""
    global _deadline_ns, _job
    limits = policy['limits_per_mathematical_command']
    _deadline_ns = time.monotonic_ns() + limits['wall_time_seconds'] * 1000000000
    memory_bytes = limits['memory_limit_mib'] * 1024 * 1024
    if os.name == 'nt':
        from ctypes import wintypes

        class Basic(ctypes.Structure):
            _fields_ = [('process_time', ctypes.c_int64), ('job_time', ctypes.c_int64),
                        ('flags', wintypes.DWORD), ('min_ws', ctypes.c_size_t),
                        ('max_ws', ctypes.c_size_t), ('processes', wintypes.DWORD),
                        ('affinity', ctypes.c_size_t), ('priority', wintypes.DWORD),
                        ('scheduling', wintypes.DWORD)]

        class Counters(ctypes.Structure):
            _fields_ = [(name, ctypes.c_uint64) for name in ('read_ops', 'write_ops', 'other_ops', 'read_bytes', 'write_bytes', 'other_bytes')]

        class Extended(ctypes.Structure):
            _fields_ = [('basic', Basic), ('io', Counters), ('process_memory', ctypes.c_size_t),
                        ('job_memory', ctypes.c_size_t), ('peak_process', ctypes.c_size_t),
                        ('peak_job', ctypes.c_size_t)]

        kernel = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
        kernel.CreateJobObjectW.restype = wintypes.HANDLE
        kernel.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
        kernel.SetInformationJobObject.restype = wintypes.BOOL
        kernel.GetCurrentProcess.restype = wintypes.HANDLE
        kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
        kernel.AssignProcessToJobObject.restype = wintypes.BOOL
        _job = kernel.CreateJobObjectW(None, None)
        info = Extended()
        info.basic.flags = 256  # JOB_OBJECT_LIMIT_PROCESS_MEMORY
        info.process_memory = memory_bytes
        if not _job or not kernel.SetInformationJobObject(_job, 9, ctypes.byref(info), ctypes.sizeof(info)):
            raise ResourceBoundary('Cannot establish the declared Windows process memory limit: ' + str(ctypes.get_last_error()))
        if not kernel.AssignProcessToJobObject(_job, kernel.GetCurrentProcess()):
            raise ResourceBoundary('Cannot attach the declared Windows process memory limit: ' + str(ctypes.get_last_error()))
    else:
        import resource
        resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))


def normalize(poly):
    global _max_terms, _max_bits
    if _deadline_ns is not None and time.monotonic_ns() > _deadline_ns:
        raise ResourceBoundary('Declared mathematical wall-clock limit exceeded')
    if not isinstance(poly, dict):
        raise TypeError('Polynomial must use the existing exponent-tuple dictionary carrier')
    result = {}
    for monomial, coeff in poly.items():
        if (not isinstance(monomial, tuple) or len(monomial) != 10
                or any(type(x) is not int or x < 0 for x in monomial)
                or type(coeff) is not int
                or any(monomial[x] for x in (3, 4, 5, 8, 9))):
            raise TypeError('Invalid exponent, coefficient, or unused legacy symbol')
        powers = list(monomial)
        while powers[0] >= 4:
            powers[0] -= 4
            coeff *= 3
        while powers[1] >= 2:
            powers[1] -= 2
            coeff *= 2
        while powers[2] >= 2:
            powers[2] -= 2
            coeff = -coeff
        key = tuple(powers)
        result[key] = result.get(key, 0) + coeff
    result = base.reduce_curve(result)
    _max_terms = max(_max_terms, len(result))
    _max_bits = max(_max_bits, max((abs(c).bit_length() for c in result.values()), default=0))
    if _max_bits > 65536 or len(result) > 250000:
        raise ResourceBoundary('Declared integer or exact-record budget exceeded')
    return result


def constant(integer):
    if type(integer) is not int:
        raise TypeError('Only exact integer coefficients are allowed')
    return base.constant(integer)


def add(*polys):
    _calls['add'] += 1
    return normalize(base.add(*polys))


def scale(poly, integer):
    if type(integer) is not int:
        raise TypeError('Scaling is integer-only')
    _calls['scale'] += 1
    return normalize(base.scale(poly, integer))


def multiply(*polys):
    result = constant(1)
    for poly in polys:
        _calls['multiply'] += 1
        result = normalize(base.multiply(result, poly))
    return result


def difference(left, right):
    _calls['rr_fiber_difference'] += 1
    return normalize(base.rr_fiber_difference(left, right))


def twice_delta(poly):
    _calls['twice_delta'] += 1
    return normalize(base.twice_delta(poly))


def formula():
    alpha, beta, imaginary, R, t = (base.variable(i) for i in (0, 1, 2, 6, 7))
    s = multiply(alpha, alpha)
    h = multiply(s, beta)
    uN = add(scale(h, -2), constant(-3), scale(s, 2), scale(beta, 3))
    LN = scale(add(constant(2), beta, s, h), 3)
    uD = add(constant(-3), scale(h, -1), beta, s)
    MD = add(h, scale(s, -2), scale(beta, -3))
    QD = add(multiply(R, R), multiply(add(constant(6), scale(beta, -3), scale(s, -1), h), R),
             constant(18), scale(beta, -18), scale(s, -12), scale(h, 6))
    N = multiply(add(R, constant(2)), add(multiply(scale(add(s, constant(-1)), 3), t),
                  multiply(imaginary, alpha, uN, add(R, s), difference(R, LN))))
    D0 = add(multiply(t, QD), multiply(imaginary, alpha, uD, R, difference(R, s), difference(R, MD)))
    k = scale(multiply(imaginary, alpha, add(h, constant(-2))), -1)
    lam = add(constant(35), scale(beta, 24), scale(s, -20), scale(h, -14))
    C4 = scale(multiply(imaginary, alpha, add(constant(9), scale(beta, 3), scale(s, 2), scale(h, 4))), -1)
    return {'alpha': alpha, 'beta': beta, 'i': imaginary, 'sqrt3': s, 'R': R, 't': t,
            'N': N, 'D0': D0, 'k': k, 'lambda': lam, 'C4': C4}


def ode_residual(data):
    N, D0, R, t, k, lam, C4 = (data[key] for key in ('N', 'D0', 'R', 't', 'k', 'lambda', 'C4'))
    W = difference(multiply(twice_delta(N), D0), multiply(N, twice_delta(D0)))
    lhs = multiply(add(R, constant(2)), t, W, W)
    rhs = multiply(C4, add(t, k), add(t, k), N, difference(N, D0), difference(N, multiply(lam, D0)), D0)
    return difference(lhs, rhs), W


def rows(poly):
    return [{'exponents': list(m), 'coefficient': c} for m, c in sorted(poly.items())]


def check_sources(root):
    frozen = root.joinpath(REL, 'source_freeze.json').read_bytes()
    if hashlib.sha256(frozen).hexdigest() != FREEZE_SHA256:
        raise ValueError('Pinned source-freeze bytes changed')
    source = json.loads(frozen)
    for pin in source['source_pins']:
        if hashlib.sha256(root.joinpath(pin['path']).read_bytes()).hexdigest() != pin['sha256']:
            raise ValueError('Pinned source changed: ' + pin['path'])
    if hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest() != BASE_SHA256:
        raise ValueError('Canonical reused integer-polynomial implementation changed')
    return source


def build_certificate(root):
    check_sources(root)
    policy = json.loads(root.joinpath(REL, 'execution_policy.json').read_bytes())
    enforce_limits(policy)
    data = formula()
    residual, W = ode_residual(data)
    # A complete ring remainder, with no substitution t=-k or reduction at Q.
    if residual:
        return {'schema': 'RB_CM24_EXACT_MAP_IDENTITY_CHECKPOINT_V1', 'task_verdict': 'INCOMPLETE',
                'identity_status': 'NONZERO_FORMAL_REMAINDER_REQUIRES_EXACT_EMBEDDING_FAILURE_REVIEW',
                'source_freeze_sha256': FREEZE_SHA256, 'ode_residual': rows(residual),
                'W': rows(W), 'generator_order': list(base.NAMES)}
    if not W or not data['D0'] or not data['C4']:
        raise AssertionError('Degenerate numerator, denominator or target constant')
    result = {'schema': 'RB_CM24_EXACT_MAP_IDENTITY_CHECKPOINT_V1', 'task_verdict': 'INCOMPLETE',
              'identity_status': 'FULL_FUNCTION_FIELD_ODE_CLEARED_IDENTITY_PASS',
              'source_freeze_sha256': FREEZE_SHA256, 'reused_integer_api_sha256': BASE_SHA256,
              'generator_order': list(base.NAMES), 'coefficient_embedding': {'a': 'positive alpha, alpha^4=3', 'b': 'positive beta, beta^2=2', 'c': 'i, i^2=-1'},
              'complete_ring_remainder': [], 'critical_divisor_substitution_used': False,
              'N': rows(data['N']), 'D0': rows(data['D0']), 'k': rows(data['k']),
              'lambda': rows(data['lambda']), 'C4': rows(data['C4']), 'W': rows(W),
              'target_equation': 'Y=w*W/(2*(t+k)*D0^2) gives Y^2=(C4/4)*X*(X-1)*(X-lambda) by the same full cleared identity and w^2=(R+2)*t.',
              'remaining_gates': ['field/embedding nonzero certificates', 'all special-fiber valuations and square-class placement/descent', 'all common basepoint cancellation and exact map degree', 'exact target j/model relation', 'unsquared differential and exceptional-point regularity', 'independent counterchecks and full proof/return'],
              'parent_period_and_exhaustive_classification': 'OPEN_OUTSIDE_THIS_TASK',
              'arithmetic': {'actual_integer_divisions': 0, 'actual_root_evaluations': 0, 'brc_evaluations': 0,
                             'operations': 'Integer coefficient additions/multiplications and monic algebraic relation rewrites; function denominators and scalar denominator 4 unevaluated.',
                             'actual_reused_api_calls': dict(_calls), 'largest_normalized_support': _max_terms, 'largest_observed_coefficient_bits': _max_bits},
              'resource_policy_sha256': hashlib.sha256(root.joinpath(REL, 'execution_policy.json').read_bytes()).hexdigest(),
              'no_blind_or_formal_acceptance': True}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    result = build_certificate(args.root)
    encoded = (json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')
    if len(encoded) > 67108864:
        raise ResourceBoundary('Declared exact output budget exceeded')
    target = args.output or args.root.joinpath(REL, 'exact_map_certificate.json')
    if args.write:
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as stream:
            stream.write(encoded)
    elif target.read_bytes() != encoded:
        raise ValueError('Stored exact identity checkpoint differs from this deterministic replay')
    print(json.dumps({'identity_status': result['identity_status'], 'task_verdict': result['task_verdict'], 'sha256': hashlib.sha256(encoded).hexdigest(), 'bytes': len(encoded), 'remaining_gates': result.get('remaining_gates', [])}, sort_keys=True))
    return 0 if not result.get('ode_residual') else 2


if __name__ == '__main__':
    raise SystemExit(main())
