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
PLACEMENT_BINDING_SHA256 = '722628192d82a4ec5d277c3a07d4f6aea84276edada30e692c88a2853746d3d1'
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
    A = add(multiply(scale(add(s, constant(-1)), 3), t),
            multiply(imaginary, alpha, uN, add(R, s), difference(R, LN)))
    r = scale(add(constant(3), scale(beta, 3), scale(s, 2), h), -1)
    return {'alpha': alpha, 'beta': beta, 'i': imaginary, 'sqrt3': s, 'R': R, 't': t,
            'N': N, 'D0': D0, 'k': k, 'lambda': lam, 'C4': C4,
            'uN': uN, 'uD': uD, 'LN': LN, 'MD': MD, 'QD': QD, 'A': A, 'r': r}


def ode_residual(data):
    N, D0, R, t, k, lam, C4 = (data[key] for key in ('N', 'D0', 'R', 't', 'k', 'lambda', 'C4'))
    W = difference(multiply(twice_delta(N), D0), multiply(N, twice_delta(D0)))
    lhs = multiply(add(R, constant(2)), t, W, W)
    rhs = multiply(C4, add(t, k), add(t, k), N, difference(N, D0), difference(N, multiply(lam, D0)), D0)
    return difference(lhs, rhs), W


def rows(poly):
    return [{'exponents': list(m), 'coefficient': c} for m, c in sorted(poly.items())]


def power(poly, exponent):
    if type(exponent) is not int or exponent < 0:
        raise TypeError('Polynomial powers are nonnegative integers')
    result = constant(1)
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def evaluate(poly, R_value, t_value=None):
    result = {}
    for monomial, coefficient in poly.items():
        powers = list(monomial)
        nR, nt = powers[6], powers[7]
        powers[6] = 0
        if t_value is not None:
            powers[7] = 0
        term = multiply({tuple(powers): coefficient}, power(R_value, nR))
        if t_value is not None:
            term = multiply(term, power(t_value, nt))
        result = add(result, term)
    return result


def norm_t(poly):
    conjugate = {m: -c if m[7] else c for m, c in poly.items()}
    result = multiply(poly, conjugate)
    if any(m[7] for m in result):
        raise AssertionError('Conjugate norm retained a t coefficient')
    return result


def R_coefficient(poly, exponent):
    """Extract a coefficient in L[R]; this is not a field quotient."""
    if any(m[7] for m in poly):
        raise ValueError('The selected fiber polynomial must be in L[R]')
    answer = {}
    for monomial, coefficient in poly.items():
        if monomial[6] == exponent:
            key = list(monomial)
            key[6] = 0
            answer[tuple(key)] = coefficient
    return normalize(answer)


def R_degree(poly):
    if any(m[7] for m in poly):
        raise ValueError('The selected fiber polynomial must be in L[R]')
    return max((m[6] for m in poly), default=-1)


def deflate_monic_R(poly, root):
    """Exact rewrite p=(R-root)q+r, with no scalar division or content removal."""
    R = base.variable(6)
    current, quotient = dict(poly), {}
    while R_degree(current) > 0:
        degree = R_degree(current)
        leading = R_coefficient(current, degree)
        term = multiply(leading, power(R, degree - 1))
        quotient = add(quotient, term)
        current = difference(current, multiply(term, difference(R, root)))
        if R_degree(current) >= degree:
            raise AssertionError('Monic polynomial rewrite failed to lower degree')
    if difference(poly, add(multiply(difference(R, root), quotient), current)):
        raise AssertionError('Polynomial deflation reconstruction failed')
    return quotient, current


def R_derivative(poly):
    result = {}
    for monomial, coefficient in poly.items():
        if monomial[6]:
            key = list(monomial)
            exponent = key[6]
            key[6] -= 1
            result[tuple(key)] = coefficient * exponent
    return normalize(result)


def t_coefficient(poly, exponent):
    result = {}
    for monomial, coefficient in poly.items():
        if monomial[7] == exponent:
            key = list(monomial)
            key[7] = 0
            result[tuple(key)] = coefficient
    return normalize(result)


def pseudo_quotient_R(dividend, divisor):
    """Return M, q, r with M*dividend=q*divisor+r, without inverting scalars."""
    R = base.variable(6)
    remainder, quotient, multiplier = dict(dividend), {}, constant(1)
    degree_b = R_degree(divisor)
    if degree_b < 0:
        raise ValueError('Zero formal polynomial divisor')
    leading_b = R_coefficient(divisor, degree_b)
    while remainder and R_degree(remainder) >= degree_b:
        degree_a = R_degree(remainder)
        term = multiply(R_coefficient(remainder, degree_a), power(R, degree_a - degree_b))
        remainder = difference(multiply(leading_b, remainder), multiply(term, divisor))
        quotient = add(multiply(leading_b, quotient), term)
        multiplier = multiply(multiplier, leading_b)
        if R_degree(remainder) >= degree_a:
            raise AssertionError('Formal pseudo-quotient did not lower degree')
    if difference(multiply(multiplier, dividend), add(multiply(quotient, divisor), remainder)):
        raise AssertionError('Formal pseudo-quotient reconstruction failed')
    return multiplier, quotient, remainder


def cleared_square_R(poly):
    """For the degree <=6 fiber factors, certify S^2=K*poly with scalar K."""
    R = base.variable(6)
    degree = R_degree(poly)
    c = R_coefficient(poly, degree)
    if degree == 0:
        square, multiplier = c, c
    elif degree == 2:
        square = add(scale(multiply(c, R), 2), R_coefficient(poly, 1))
        multiplier = scale(c, 4)
    elif degree == 4:
        a = R_coefficient(poly, 3)
        b = difference(scale(multiply(c, R_coefficient(poly, 2)), 4), power(a, 2))
        square = add(scale(multiply(power(c, 2), power(R, 2)), 8), scale(multiply(c, a, R), 4), b)
        multiplier = scale(power(c, 3), 64)
    elif degree == 6:
        a = R_coefficient(poly, 5)
        b = difference(scale(multiply(c, R_coefficient(poly, 4)), 4), power(a, 2))
        e = difference(scale(multiply(power(c, 2), R_coefficient(poly, 3)), 8), multiply(a, b))
        square = add(scale(multiply(power(c, 3), power(R, 3)), 16),
                     scale(multiply(power(c, 2), a, power(R, 2)), 8),
                     scale(multiply(c, b, R), 2), e)
        multiplier = scale(power(c, 5), 256)
    else:
        raise AssertionError('Unexpected bounded square degree: ' + str(degree))
    residual = difference(power(square, 2), multiply(multiplier, poly))
    if residual:
        raise AssertionError('The remaining fiber polynomial is not the claimed scalar square: ' + json.dumps(rows(residual)))
    return square, multiplier


def conjugate_t(poly):
    return {m: -coefficient if m[7] else coefficient for m, coefficient in poly.items()}


def unramified_class_checkpoint(data, label, numerator, denominator, H_num, H_den,
                                cancel_roots, Q3, denominator_scalar):
    """A task-specific Hilbert-90 witness, with every scalar denominator retained.

    Norm(numerator/denominator)=(H_num/H_den)^2.  Its trace plus 2H is
    reduced to a degree<=6 R-polynomial divided by a square.  No square root
    of a coefficient is evaluated or silently adjoined.
    """
    norm_n, norm_d = norm_t(numerator), norm_t(denominator)
    if difference(multiply(norm_n, power(H_den, 2)), multiply(norm_d, power(H_num, 2))):
        raise AssertionError('The proposed norm root is wrong for ' + label)
    trace_n = add(multiply(numerator, conjugate_t(denominator)),
                  multiply(conjugate_t(numerator), denominator))
    U = add(multiply(H_den, trace_n), scale(multiply(H_num, norm_d), 2))
    V = multiply(H_den, norm_d)
    # The non-square factors known in V are canceled by actual polynomial
    # identities first.  Q3 is scaled rather than divided by its leading 16.
    reduced = U
    removed = constant(1)
    for root in cancel_roots:
        reduced, residue = deflate_monic_R(reduced, root)
        if residue:
            raise AssertionError('Known Hilbert-90 common factor failed for ' + label)
        removed = multiply(removed, difference(data['R'], root))
    M, reduced, residue = pseudo_quotient_R(reduced, Q3)
    if residue:
        raise AssertionError('Known Hilbert-90 cubic common factor failed for ' + label)
    # This binds r=U/V to an exact rational expression
    # r=reduced/(denominator_scalar*M*Q3^2); its sign/256 is in that scalar pair.
    scalar_num, scalar_den = denominator_scalar
    identity = difference(multiply(V, scalar_den),
                          multiply(scalar_num, removed, power(Q3, 3)))
    if identity:
        raise AssertionError('The reduced Hilbert-90 denominator was not bound for ' + label)
    if difference(multiply(M, U), multiply(removed, Q3, reduced)):
        raise AssertionError('The reduced Hilbert-90 numerator was not bound for ' + label)
    branch_multiplicities = {}
    square_branch, odd_branch = constant(1), constant(1)
    remaining = reduced
    for branch_label, root in [('T0', constant(0)), ('Tplus', data['sqrt3']),
                               ('Tminus', scale(data['sqrt3'], -1))]:
        count = 0
        while remaining and not evaluate(remaining, root):
            remaining, residue = deflate_monic_R(remaining, root)
            if residue:
                raise AssertionError('Branch deflation lost an exact zero')
            count += 1
        branch_multiplicities[branch_label] = count
        pairs, parity = 0, count
        while parity >= 2:
            pairs += 1
            parity -= 2
        factor = difference(data['R'], root)
        square_branch = multiply(square_branch, power(factor, pairs))
        if parity:
            odd_branch = multiply(odd_branch, factor)
    S, K = cleared_square_R(remaining)
    total_S = multiply(S, square_branch)
    if difference(multiply(K, reduced), multiply(odd_branch, power(total_S, 2))):
        raise AssertionError('The retained odd branch factor reconstruction failed')
    odd = [name for name, count in branch_multiplicities.items() if count & 1]
    if len(odd) == 0 or len(odd) == 3:
        twist = 'O'
    elif len(odd) == 1:
        twist = odd[0]
    else:
        twist = next(name for name in ('T0', 'Tplus', 'Tminus') if name not in odd)
    receipt = {'label': label, 'geometric_unramified_twist': twist,
            'branch_multiplicities_of_reduced_R_polynomial': branch_multiplicities,
            'norm_root_pair': {'numerator': rows(H_num), 'denominator': rows(H_den)},
            'trace_plus_2H_pair': {'numerator': rows(U), 'denominator': rows(V)},
            'pseudo_multiplier': rows(M), 'reduced_R_polynomial': rows(reduced),
            'denominator_scalar_pair': {'numerator': rows(scalar_num), 'denominator': rows(scalar_den)},
            'square_witness': rows(total_S), 'square_scalar_K': rows(K), 'odd_branch_factor': rows(odd_branch),
            'identities': ['Norm(h)=H^2', 'M*U=removed*Q3*reduced',
                           'V*scalar_den=scalar_num*removed*Q3^3',
                           'K*reduced=odd_branch_factor*square_witness^2'],
            'constants_and_descent': 'All scalar factors are retained in L; the geometric label does not claim any retained scalar is a square in L.'}
    return receipt, {'M': M, 'K': K, 'S': total_S, 'odd': odd_branch,
                     'scalar_num': scalar_num, 'scalar_den': scalar_den}


def coprime_R_witness(left, right):
    """Small fiber-specific pseudo-remainder chain; every multiplier is retained."""
    R = base.variable(6)
    a, b = dict(left), dict(right)
    chain = []
    if R_degree(a) < R_degree(b):
        a, b = b, a
    for _ in range(8):
        if not b:
            raise AssertionError('The selected fiber factors have a common root')
        if R_degree(b) == 0:
            return {'terminal_nonzero_constant': rows(b), 'steps': chain}
        before = a
        degree_b = R_degree(b)
        leading_b = R_coefficient(b, degree_b)
        multiplier = constant(1)
        q = {}
        while a and R_degree(a) >= degree_b:
            degree_a = R_degree(a)
            leading_a = R_coefficient(a, degree_a)
            term = multiply(leading_a, power(R, degree_a - degree_b))
            a = difference(multiply(leading_b, a), multiply(term, b))
            q = add(multiply(leading_b, q), term)
            multiplier = multiply(multiplier, leading_b)
            if R_degree(a) >= degree_a:
                raise AssertionError('Pseudo-remainder degree did not drop')
        if difference(multiply(multiplier, before), add(multiply(q, b), a)):
            raise AssertionError('Pseudo-remainder exact reconstruction failed')
        chain.append({'input_degrees': [R_degree(before), degree_b],
                      'multiplier': rows(multiplier), 'quotient': rows(q),
                      'remainder': rows(a)})
        a, b = b, a
    raise ResourceBoundary('The bounded special-fiber chain exceeded eight steps')


def unsquared_input_residual(data, W, y_numerator=None, y_denominator=None):
    """Clear the three actual coefficient pairs; never infer a Y sign by squaring."""
    dX_num = W
    dX_den = scale(multiply(data['t'], data['D0'], data['D0']), 2)
    Y_num = W if y_numerator is None else y_numerator
    Y_den = (scale(multiply(add(data['t'], data['k']), data['D0'], data['D0']), 2)
             if y_denominator is None else y_denominator)
    phi_num, phi_den = add(data['t'], data['k']), data['t']
    return difference(multiply(dX_num, Y_den, phi_den),
                      multiply(phi_num, dX_den, Y_num))


def placement_checkpoint(data, Q2, Q3, Ql):
    R, t, s, lam = (data[x] for x in ('R', 't', 'sqrt3', 'lambda'))
    N, D0 = data['N'], data['D0']
    A1, Al = difference(N, D0), difference(N, multiply(lam, D0))
    beta_minus_one = add(data['beta'], constant(-1))
    xQ = multiply(s, beta_minus_one)
    tQ = multiply(data['i'], data['beta'], power(data['alpha'], 3), beta_minus_one)
    slope_numerator = add(scale(power(xQ, 2), 3), constant(-3))
    ell = add(scale(multiply(tQ, t), 2), scale(multiply(slope_numerator, R), -1),
              multiply(slope_numerator, xQ), scale(power(tQ, 2), -2))
    identities = {
        'half-point is on C': add(power(tQ, 2), scale(power(xQ, 3), -1), scale(xQ, 3)),
        'tangent contains Q': evaluate(ell, xQ, tQ),
        'Norm(tangent)=-4*tQ^2*(R-xQ)^2*(R+sqrt3)':
            add(norm_t(ell), scale(multiply(power(tQ, 2), power(difference(R, xQ), 2), add(R, s)), 4)),
        'V4 Xnew-1=(1-lambda)*D0/(N-D0)':
            difference(difference(Al, A1), multiply(difference(constant(1), lam), D0)),
        'V4 Xnew-lambda=(1-lambda)*N/(N-D0)':
            difference(difference(Al, multiply(lam, A1)), multiply(difference(constant(1), lam), N)),
    }
    for name, value in identities.items():
        if value:
            raise AssertionError(name + ': ' + json.dumps(rows(value)))
    if not tQ or not add(xQ, s):
        raise AssertionError('The chosen half-point is degenerate')
    empty, empty_raw = unramified_class_checkpoint(data, 'Xnew with G0=1', Al, A1,
        Ql, multiply(power(lam, 5), Q3), [scale(s, -3)], Q3,
        (scale(power(lam, 5), -1), constant(256)))
    pair_num = multiply(difference(constant(1), lam), D0, ell)
    pair_den = multiply(A1, t)
    Hpair = scale(multiply(tQ, difference(constant(1), lam), difference(R, xQ), Q2), 4)
    pair, pair_raw = unramified_class_checkpoint(data, '(Xnew-1)/(t/tangent)', pair_num, pair_den,
        Hpair, Q3, [scale(s, -3), constant(0), s, scale(s, -1)], Q3,
        (constant(1), constant(256)))
    if (empty['geometric_unramified_twist'], pair['geometric_unramified_twist']) != ('Tplus', 'T0'):
        raise AssertionError('Unexpected actual unramified classes of this pinned map')
    # These are explicit L-rational representatives, with constants retained
    # as numerator/denominator data. No square root of a constant is chosen.
    alpha0_num = multiply(empty_raw['M'], empty_raw['scalar_num'], empty_raw['K'])
    alpha0_den = empty_raw['scalar_den']
    alpha1_num = multiply(pair_raw['M'], pair_raw['scalar_num'], pair_raw['K'])
    alpha1_den = pair_raw['scalar_den']
    u0_num = add(multiply(power(lam, 5), Q3, Al), multiply(Ql, A1))
    u0_den = multiply(power(lam, 5), A1, t, empty_raw['S'])
    u1_num = add(multiply(Q3, pair_num), multiply(Hpair, pair_den))
    u1_den = multiply(pair_den, R, pair_raw['S'])
    Hproduct_num = multiply(difference(lam, constant(1)),
                            difference(multiply(twice_delta(N), D0), multiply(N, twice_delta(D0))))
    Hproduct_den = multiply(add(t, data['k']), A1, A1)
    alphal_num = multiply(alpha0_den, alpha1_den)
    alphal_den = multiply(data['C4'], alpha0_num, alpha1_num)
    ul_num = multiply(Hproduct_num, u0_den, u1_den)
    ul_den = multiply(Hproduct_den, t, u0_num, u1_num)
    hl_num = multiply(difference(constant(1), lam), N)
    hl_den = multiply(A1, add(R, constant(2)), ell)
    square_pairs = {
        'zero': (Al, A1, difference(R, s), alpha0_num, alpha0_den, u0_num, u0_den),
        'one': (pair_num, pair_den, R, alpha1_num, alpha1_den, u1_num, u1_den),
        'lambda': (hl_num, hl_den, add(R, s), alphal_num, alphal_den, ul_num, ul_den),
    }
    square_receipts = {}
    for label, (h_num, h_den, gamma, a_num, a_den, u_num, u_den) in square_pairs.items():
        if not all((h_num, h_den, gamma, a_num, a_den, u_num, u_den)):
            raise AssertionError('Zero symbolic square-class factor for ' + label)
        residual = difference(multiply(a_den, h_num, power(u_den, 2)),
                              multiply(a_num, gamma, h_den, power(u_num, 2)))
        if residual:
            raise AssertionError('L-rational square-class reconstruction failed for ' + label)
        square_receipts[label] = {
            'gamma': rows(gamma), 'alpha_numerator': rows(a_num), 'alpha_denominator': rows(a_den),
            'u_numerator': rows(u_num), 'u_denominator': rows(u_den),
            'cleared_reconstruction_remainder': [], 'all_factors_nonzero_in_proved_field_basis': True}
    normalized = dict(data, N=multiply(lam, A1), D0=Al)
    normalized_ode, normalized_W = ode_residual(normalized)
    original_W = difference(multiply(twice_delta(N), D0), multiply(N, twice_delta(D0)))
    normalization_derivative = difference(normalized_W,
        multiply(lam, difference(constant(1), lam), original_W))
    if normalized_ode or normalization_derivative:
        raise AssertionError('The actual fixed-lambda normalization failed its ODE or derivative')
    return {'V4_transform': 'Xnew=(X-lambda)/(X-1)',
            'V4_old_to_new_labels': {'0': 'lambda', '1': 'infinity', 'lambda': '0', 'infinity': '1'},
            'normalized_branch_blocks': {'0': [], '1': ['T0', 'Tplus'],
                                         'lambda': ['O', 'Tminus', 'Pplus', 'Pminus'], 'infinity': []},
            'base_pair_half_point': {'R': rows(xQ), 't': rows(tQ), 'twice_Q': 'Tminus'},
            'base_pair_g': 't/tangent', 'tangent': rows(ell),
            'G_product': 'G0=1; G1=t/tangent; Glambda=(R+2)*tangent; product=(R+2)*t',
            'cleared_identity_remainders': {name: [] for name in identities},
            'unramified_classes': {'zero': empty, 'one': pair},
            'L_rational_square_class_representatives_for_Xnew': square_receipts,
            'geometric_twist_triple_for_Xnew': ['Tplus', 'T0', 'Tminus'],
            'canonical_empty_infinity_coordinate': 'z=lambda/Xnew=lambda*(X-1)/(X-lambda)',
            'canonical_old_to_new_V4_labels': [1, 0, 3, 2],
            'canonical_assignment': [1, 2, 2, 1, 1, 1],
            'canonical_twist_triple': ['Tplus', 'T0', 'Tminus'],
            'canonical_Y': 'Yz=lambda*(1-lambda)*Y/(X-lambda)^2; same C4/4 and d(z)/Yz=phi',
            'canonical_full_ode_remainder': [], 'canonical_derivative_remainder': [],
            'canonical_pole_half_divisor': 'E_lambda, the three distinct L-defined points cut out by Qlambda(R)=0 and N-lambda*D0=0; poles of z are 2*E_lambda.',
            'pole_class_constraint': 'S=sum(E_lambda), 2*S=-B0, so S is not O; no unproved replacement by 3O.',
            'placement_boundary': 'The explicit scalar/function pairs reconstruct all three classes over L. The old 16 classes are geometric labels, not a claim that these retained constants are squares in a smaller field.'}


def special_fiber_checkpoint(data, W):
    """Three complete conjugate norm identities, retaining all special points."""
    R, s, lam, N, D0 = (data[x] for x in ('R', 'sqrt3', 'lambda', 'N', 'D0'))
    zero, one = constant(0), constant(1)
    A1, Al = difference(N, D0), difference(N, multiply(lam, D0))
    selected = {'infinity': (D0, [zero, s, scale(s, -3)]),
                'one': (A1, [scale(s, -3)]),
                'lambda': (Al, [scale(s, -3)])}
    reduced = {}
    for name, (value, roots) in selected.items():
        remaining = scale(norm_t(value), -1)
        for root in roots:
            remaining, remainder = deflate_monic_R(remaining, root)
            if remainder:
                raise AssertionError('Known fiber norm factor failed: ' + name)
        reduced[name] = remaining
    F2, F3, Fl = (reduced[x] for x in ('infinity', 'one', 'lambda'))
    if (R_degree(F2), R_degree(F3), R_degree(Fl)) != (4, 6, 6):
        raise AssertionError('Unexpected residual fiber norm degrees')
    if (R_coefficient(F2, 4), R_coefficient(F3, 6), R_coefficient(Fl, 6)) != (one, one, power(lam, 2)):
        raise AssertionError('Unexpected residual fiber leading coefficients')
    # Cleared square roots are recovered by integer triangular coefficient
    # identities. The denominators 8, 16 and 16*lambda^5 stay symbolic.
    a2 = R_coefficient(F2, 3)
    b8 = difference(scale(R_coefficient(F2, 2), 4), power(a2, 2))
    Q2 = add(scale(power(R, 2), 8), scale(multiply(a2, R), 4), b8)
    a3 = R_coefficient(F3, 5)
    b3 = difference(scale(R_coefficient(F3, 4), 4), power(a3, 2))
    c3 = difference(scale(R_coefficient(F3, 3), 8), multiply(a3, b3))
    Q3 = add(scale(power(R, 3), 16), scale(multiply(a3, power(R, 2)), 8), scale(multiply(b3, R), 2), c3)
    al = R_coefficient(Fl, 5)
    bl = difference(scale(multiply(power(lam, 2), R_coefficient(Fl, 4)), 4), power(al, 2))
    cl = difference(scale(multiply(power(lam, 4), R_coefficient(Fl, 3)), 8), multiply(al, bl))
    Ql = add(scale(multiply(power(lam, 6), power(R, 3)), 16),
             scale(multiply(power(lam, 4), al, power(R, 2)), 8),
             scale(multiply(power(lam, 2), bl, R), 2), cl)
    identities = {
        'Q2^2=64*F2': difference(power(Q2, 2), scale(F2, 64)),
        'Q3^2=256*F3': difference(power(Q3, 2), scale(F3, 256)),
        'Qlambda^2=256*lambda^10*Flambda': difference(power(Ql, 2), scale(multiply(power(lam, 10), Fl), 256)),
        'unsquared_actual_input_cross_product': unsquared_input_residual(data, W),
    }
    for name, value in identities.items():
        if value:
            raise AssertionError(name + ': ' + json.dumps(rows(value)))
    factors = {'infinity': Q2, 'one': Q3, 'lambda': Ql}
    nonzero = {}
    chains = {}
    for name, q in factors.items():
        chains[name + ': squarefree'] = coprime_R_witness(q, R_derivative(q))
        chains[name + ': not both t sheets'] = coprime_R_witness(q, t_coefficient(selected[name][0], 1))
        for label, value in [('T0', zero), ('Tplus', s), ('Tminus', scale(s, -1)),
                             ('Pplus/Pminus', constant(-2)), ('B0', scale(s, -3))]:
            nonzero[name + ': Q at ' + label] = evaluate(q, value)
    nonzero['QD(T0)'] = evaluate(data['QD'], zero)
    nonzero['QD(Tplus)'] = evaluate(data['QD'], s)
    nonzero['2delta_D0(B0)'] = evaluate(twice_delta(D0), scale(s, -3),
                                      scale(multiply(data['i'], data['beta'], data['alpha']), 6))
    for name, value in nonzero.items():
        if not value:
            raise AssertionError('Special fiber nonzero witness vanished: ' + name)
    negative_y = unsquared_input_residual(data, W, y_numerator=scale(W, -1))
    missing_two = unsquared_input_residual(data, W,
        y_denominator=multiply(add(data['t'], data['k']), D0, D0))
    if not negative_y or not missing_two:
        raise AssertionError('An actual Y normalization countercheck did not reject')
    placement = placement_checkpoint(data, Q2, Q3, Ql)
    return {'factor_roots': {name: rows(q) for name, q in factors.items()},
            'factor_root_denominators': {'infinity': '8', 'one': '16', 'lambda': '16*lambda^5'},
            'norm_identities': {
                'infinity': 'Norm(D0)=-R*(R-sqrt3)*(R+3sqrt3)*(Q2/8)^2',
                'one': 'Norm(N-D0)=-(R+3sqrt3)*(Q3/16)^2',
                'lambda': 'Norm(N-lambda*D0)=-(R+3sqrt3)*(Qlambda/(16*lambda^5))^2'},
            'cleared_identity_remainders': {name: [] for name in identities},
            'coprimality_chains': chains,
            'nonzero_witnesses': {name: rows(value) for name, value in nonzero.items()},
            'actual_Y_input_negative_residuals': {'negate_Y_numerator': rows(negative_y),
                                                'omit_2_in_Y_denominator': rows(missing_two)},
            'placement_checkpoint': placement,
            'paper_interpretation_required': 'Normal forms and pseudo-remainder identities are exact; valuations on C and geometric square-class placement are separate proof statements.'}


def geometry_checkpoint(data, W):
    R, t, s, beta, imaginary, alpha = (data[x] for x in ('R', 't', 'sqrt3', 'beta', 'i', 'alpha'))
    A, r, uN, uD, N, D0 = (data[x] for x in ('A', 'r', 'uN', 'uD', 'N', 'D0'))
    a = scale(add(s, constant(-1)), 3)
    expected_norm = scale(multiply(s, uN, uN, add(R, s), add(R, scale(s, 3)), power(difference(R, r), 2)), -1)
    norm_residual = difference(norm_t(A), expected_norm)
    if norm_residual:
        raise AssertionError('Pinned A norm factorization failed: ' + json.dumps(rows(norm_residual)))
    identities = {
        'N=(R+2)A': difference(N, multiply(add(R, constant(2)), A)),
        'uN=(beta-1)(3-2sqrt3)': difference(uN, multiply(add(beta, constant(-1)), add(constant(3), scale(s, -2)))),
        'uD=-2-(sqrt3-1)(beta-1)': add(uD, constant(2), multiply(add(s, constant(-1)), add(beta, constant(-1)))),
        'r*sqrt3=-LN': add(multiply(r, s), data['LN']),
    }
    R_B = scale(s, -3)
    t_B = scale(multiply(imaginary, beta, alpha), 6)
    identities.update({
        'B0 lies on C': add(multiply(t_B, t_B), scale(power(R_B, 3), -1), scale(R_B, 3)),
        'N(B0)=0': evaluate(N, R_B, t_B),
        'D0(B0)=0': evaluate(D0, R_B, t_B),
    })
    tZ_numerator = scale(multiply(imaginary, alpha, uN, add(r, s), difference(r, data['LN'])), -1)
    identities['Z cleared carrier'] = difference(multiply(tZ_numerator, tZ_numerator), multiply(a, a, add(power(r, 3), scale(r, -3))))
    dz = add(multiply(tZ_numerator, evaluate(data['QD'], r)),
             multiply(a, imaginary, alpha, uD, r, difference(r, s), difference(r, data['MD'])))
    nonzero = {
        'D0(Tminus)': evaluate(D0, scale(s, -1), constant(0)),
        'D0(Pplus)': evaluate(D0, constant(-2), multiply(imaginary, beta)),
        'D0(Pminus)': evaluate(D0, constant(-2), scale(multiply(imaginary, beta), -1)),
        'a*D0(Z)': dz, '2delta_A(B0)': evaluate(twice_delta(A), R_B, t_B),
        'r+2': add(r, constant(2)), 'r+sqrt3': add(r, s),
        'r+3sqrt3': add(r, scale(s, 3)), 'r': r, 'r-sqrt3': difference(r, s),
        'uN': uN, 'uD': uD, '3(sqrt3-1)': a, 'C4': data['C4'],
        'lambda': data['lambda'], '1-lambda': difference(constant(1), data['lambda']),
        'k': data['k'], 'k^2': power(data['k'], 2),
        'k^2-2': add(power(data['k'], 2), constant(-2)),
        'k^2+2': add(power(data['k'], 2), constant(2)),
    }
    lam = data['lambda']
    j_num = scale(power(add(constant(1), scale(lam, -1), power(lam, 2)), 3), 256)
    j_den = multiply(lam, lam, power(difference(constant(1), lam), 2))
    j_value = add(constant(2417472), scale(beta, 1707264))
    identities['j exact cleared equality'] = difference(j_num, multiply(j_den, j_value))
    for name, residual in identities.items():
        if residual:
            raise AssertionError(name + ': ' + json.dumps(rows(residual)))
    for name, value in nonzero.items():
        if not value:
            raise AssertionError('Required field nonzero witness vanished: ' + name)
    pole_N = max(2*m[6] + 3*m[7] for m in N)
    pole_D = max(2*m[6] + 3*m[7] for m in D0)
    if (pole_N, pole_D) != (6, 7):
        raise AssertionError('Unexpected O-pole orders')
    # Clearing the unsquared dX/Y-phi comparison cancels only as a rational
    # identity. Replacing Y by -Y changes this to a nonzero doubled numerator.
    differential_common = multiply(W, add(t, data['k']), t, D0, D0)
    if not differential_common:
        raise AssertionError('Differential comparison degenerates')
    return {'norm_A_factorization': 'Norm(A)=-sqrt3*uN^2*(R+sqrt3)*(R+3sqrt3)*(R-r)^2',
            'r': rows(r), 'norm_A': rows(norm_t(A)), 'identities': {name: [] for name in identities},
            'field_nonzero_witnesses': {name: rows(value) for name, value in nonzero.items()},
            'N_zero_orders_on_C': {'Pplus': 1, 'Pminus': 1, 'Tminus': 1, 'B0': 1, 'Z': 2},
            'section_pole_orders_at_O': {'N': pole_N, 'D0': pole_D},
            'common_base_divisor': 'B0 with common order exactly 1; proof uses Norm(A) support, the displayed nonzero D0 witnesses, and N order 1 at B0.',
            'degree_X_on_C': 6, 'degree_map_D_to_target': 6,
            'j_value': rows(j_value),
            'unsquared_sign_counterexample_numerator': rows(scale(differential_common, 4)),
            'nonzero_basis_justification_required': 'All displayed nonzero dictionaries use the proved sixteen-element coefficient basis and the {1,t} function-field basis; see exact_map_proof.md.'}


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
    binding = root.joinpath(REL, 'checkpoints', 'placement_source_binding.json').read_bytes()
    if hashlib.sha256(binding).hexdigest() != PLACEMENT_BINDING_SHA256:
        raise ValueError('Pinned placement binding changed')
    for pin in json.loads(binding)['source_pins']:
        if hashlib.sha256(root.joinpath(pin['path']).read_bytes()).hexdigest() != pin['sha256']:
            raise ValueError('Pinned historical placement source changed: ' + pin['path'])
    return source


def matching_classification_entry(root):
    old = 'research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908'
    assignment = json.loads(root.joinpath(old, 'branch_assignment_classification.json').read_bytes())
    if assignment['branch_labels'] != ['O', 'T0', 'Tplus', 'Tminus', 'Pplus', 'Pminus']:
        raise ValueError('Historical source point order changed')
    if assignment['target_labels'] != ['0', '1', 'lambda', 'infinity']:
        raise ValueError('Historical target label order changed')
    raw = (0, 3, 3, 0, 0, 0)
    representatives = [tuple(permutation[x] for x in raw) for permutation in base.V4]
    fixed = min(representatives)
    normalized = min(value for value in representatives if 3 not in value)
    old_certificate = json.loads(root.joinpath(old, 'squareclass_rr_certificate.json').read_bytes())
    matches = [(index, row) for index, row in enumerate(old_certificate['patterns']['4+2+0+0']['rows'], 1)
               if tuple(row['fixed_parameter_representative']) == fixed]
    if len(matches) != 1 or tuple(matches[0][1]['infinity_empty_representative']) != normalized:
        raise ValueError('The proved source assignment has no unique compatible frozen row')
    if normalized != (1, 2, 2, 1, 1, 1):
        raise ValueError('The actual canonical V4 representative changed')
    return {'historical_row_one_based': matches[0][0], 'historical_row': matches[0][1],
            'raw_source_assignment': list(raw),
            'point_and_fiber_input_basis': 'The complete special-fiber divisor proof, not assignment-only enumeration.',
            'V4_images_checked': [list(value) for value in representatives],
            'placement_source_binding_sha256': PLACEMENT_BINDING_SHA256,
            'retained_geometric_component': {'pattern': '4+2+0+0', 'canonical_assignment': list(normalized),
                                             'base_pair_half_point': 'Q=(sqrt3*(beta-1), i*beta*alpha^3*(beta-1))',
                                             'twists_0_1_lambda': ['Tplus', 'T0', 'Tminus'],
                                             'empty_fiber_twist_is_nontrivial': True},
            'not_claimed': 'No other one of the 1980 parameter families is solved or excluded by this matching operation.'}


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
    geometry = geometry_checkpoint(data, W)
    fibers = special_fiber_checkpoint(data, W)
    result = {'schema': 'RB_CM24_EXACT_MAP_IDENTITY_CHECKPOINT_V1', 'task_verdict': 'INCOMPLETE',
              'identity_status': 'FULL_FUNCTION_FIELD_ODE_CLEARED_IDENTITY_PASS',
              'source_freeze_sha256': FREEZE_SHA256, 'reused_integer_api_sha256': BASE_SHA256,
              'generator_order': list(base.NAMES), 'coefficient_embedding': {'a': 'positive alpha, alpha^4=3', 'b': 'positive beta, beta^2=2', 'c': 'i, i^2=-1'},
              'complete_ring_remainder': [], 'critical_divisor_substitution_used': False,
              'N': rows(data['N']), 'D0': rows(data['D0']), 'k': rows(data['k']),
              'lambda': rows(data['lambda']), 'C4': rows(data['C4']), 'W': rows(W),
              'target_equation': 'Y=w*W/(2*(t+k)*D0^2) gives Y^2=(C4/4)*X*(X-1)*(X-lambda) by the same full cleared identity and w^2=(R+2)*t.',
              'geometry_checkpoint': geometry,
              'special_fiber_checkpoint': fibers,
              'frozen_classification_match': matching_classification_entry(root),
              'remaining_gates': ['source-exposed independent review of the complete fiber/square-class proof', 'gate-by-gate durable return and formal Driver review'],
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
