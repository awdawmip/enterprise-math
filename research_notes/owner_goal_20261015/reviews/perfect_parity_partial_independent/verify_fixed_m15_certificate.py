"""Independent verification of one Source-fixed m15/S0 certificate and identities.

No imports from the author's checker or reused primitives, no parameter sweep,
and no new trace input.  Only this fixed existing certificate is consumed.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).resolve().parent
EARLY = BASE / 'verified_source_members/PARITY_EARLY_EXACT_EVIDENCE_CAPSULE'
CERT = EARLY / 'ONE_ACTUAL_FULL_TRACE_EXACT_AUDIT.json'
M = 15
N = M - 1
START = time.perf_counter()
raw = CERT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == 'ae5d48f835da27c2cf1a44c81bc23a62febc15ac547d53237e93ce63b75ffd9c'
certificate = json.loads(raw)
assert certificate['domain'] == {'m': 15, 'S': '0', 'a': '1', 'c': '1', 'r0': '0', 'r': '15', 's': '30', 'M_gap': 15, 'N_gap': 30}

def product(xs):
    answer = F(1)
    for x in xs:
        answer *= x
    return answer

def rising(x, count):
    return product(x + j for j in range(count))

def transpose(a):
    return [list(x) for x in zip(*a)]

def multiply(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]

def eye(size):
    return [[F(i == j) for j in range(size)] for i in range(size)]

def diagonal(xs):
    return [[x if i == j else F(0) for j in range(len(xs))] for i, x in enumerate(xs)]

def gram(frame, weights):
    return [[sum((weights[k] * frame[k][i] * frame[k][j] for k in range(M)), F(0)) for j in range(N)] for i in range(N)]

def read_matrix(name):
    record = certificate['complete_matrices'][name]
    a = [[F(x) for x in row] for row in record['values']]
    assert len(a) == record['rows'] and all(len(row) == record['columns'] for row in a)
    return a

theta = [F(i + 1, M) for i in range(M)]
w = [(-1) ** i * comb(N, i) for i in range(M)]
computed = {}
for block in (1, 2):
    gap = M * block
    frame = [[(rising(x + gap, a) - rising(x, a)) / (gap * factorial(a)) for a in range(1, M)] for x in theta]
    weights = [F(w[i] * factorial(N), M) / rising(gap + theta[i], M) for i in range(M)]
    h = gram(frame, weights)
    # Separate falling-binomial original-node quotient, with the same Sigma.
    original = [[F(comb(j + gap, a) - comb(j, a), gap) for a in range(1, M)] for j in range(M)]
    original_weights = [F(w[j] * factorial(N)) / product(M * (gap + j) + k for k in range(1, M + 1)) for j in range(M)]
    q = gram(original, original_weights)
    sigma = [F((-1) ** (a + 1)) for a in range(1, M)]
    assert [[sigma[i] * q[i][j] * sigma[j] for j in range(N)] for i in range(N)] == h
    for name, matrix in [(f'F{block}', frame), (f'D{block}', diagonal(weights)), (f'H{block}', h)]:
        assert matrix == read_matrix(name), name
        computed[name] = matrix

inverse = read_matrix('H2_inverse')
assert multiply(computed['H2'], inverse) == eye(N)
assert multiply(inverse, computed['H2']) == eye(N)
mixed = multiply(inverse, computed['H1'])
assert mixed == read_matrix('H2_inverse_H1')
trace = sum((mixed[i][i] for i in range(N)), F(0))
gap = trace - N
assert trace == F(certificate['complete_actual_normalized_trace'])
assert gap == F(certificate['trace_minus_baseline']) > 0
assert certificate['trace_strictly_exceeds_baseline'] is True
assert certificate['actual_full_trace_counterexample'] is False

# An independent elimination verifies nonzero pivots and the determinant.
eliminated = [row[:] for row in computed['H2']]
determinant = F(1)
pivots = []
for col in range(N):
    pivot_row = next(i for i in range(col, N) if eliminated[i][col])
    if pivot_row != col:
        eliminated[col], eliminated[pivot_row] = eliminated[pivot_row], eliminated[col]
        determinant *= -1
    pivot = eliminated[col][col]
    determinant *= pivot
    pivots.append({'column': col, 'pivot_row': pivot_row, 'pivot': str(pivot)})
    for i in range(col + 1, N):
        multiplier = eliminated[i][col] / pivot
        for j in range(col + 1, N):
            eliminated[i][j] -= multiplier * eliminated[col][j]
        eliminated[i][col] = F(0)
assert determinant == F(certificate['det_H2'])
assert pivots == certificate['inverse_elimination_pivots']

# Check the already-claimed complete residue identity at this same fixed point.
# T = sum_{h=0}^{M-2} (-(E_M-I)/2)^h on degree <= M-2 polynomials.
degree = M - 2
translation_coefficients = [sum((F((-1) ** j * comb(h, j), 2 ** h) for h in range(j, degree + 1)), F(0)) for j in range(degree + 1)]

def value_and_derivative(roots, x):
    factors = [x - a for a in roots]
    value = product(factors)
    derivative = sum((product(factors[:i] + factors[i + 1:]) for i in range(len(factors))), F(0))
    return value, derivative

cache = {}
def polynomial_data(t, x):
    key = (t, x)
    if key not in cache:
        v, vp = value_and_derivative(theta, x)
        p, pp = value_and_derivative([-F(t) - j for j in range(M)], x)
        cache[key] = (v, vp, p - v, pp - vp)
    return cache[key]

def reduced_bezout(t, x, y):
    vx, vpx, rx, rpx = polynomial_data(t, x)
    vy, _, ry, _ = polynomial_data(t, y)
    quotient = (vx * ry - rx * vy) / (x - y) if x != y else vpx * rx - rpx * vx
    linear = F(M * t) + F(M * M + 1, 2)
    return quotient - rx * ry / linear

residue_terms = []
for k in range(M):
    x = -F(M) - k
    transformed = sum((translation_coefficients[i] * translation_coefficients[j] * reduced_bezout(2 * M, x + i * M, x + j * M) for i in range(degree + 1) for j in range(degree + 1)), F(0))
    z = transformed - reduced_bezout(M, x, x)
    b = F((-1) ** k, factorial(k) * factorial(N - k)) * z
    denominator = product(M + k + a for a in theta)
    term = F((-1) ** N) * b / denominator
    residue_terms.append({'k': k, 'Z_at_pole': str(z), 'b': str(b), 'positive_denominator': str(denominator), 'oriented_signed_term': str(term)})
residue_sum = sum((F(t['oriented_signed_term']) for t in residue_terms), F(0))
assert residue_sum == gap

report = {
    'schema': 'PARITY_PARTIAL_INDEPENDENT_FIXED_M15_CERTIFICATE_VERIFICATION_V1',
    'reviewer': 'EM-PARITYREV-12B648',
    'activity_id': 'RA-EB0794CB61621CB6E90B4730',
    'context': 'NONBLIND_SHARED_CONTROL_CONTEXT_DISCLOSED_NO_AUTHOR_SIDE_CONTRIBUTION',
    'source_commit': 'b46c77b64f5f42ed98a14f94dda29d4e2dc2cfac',
    'source_certificate_sha256': hashlib.sha256(raw).hexdigest(),
    'verification_input_count': 1,
    'new_trace_inputs': 0,
    'author_checker_or_primitives_imported': False,
    'scientific_parameter_grid': False,
    'exact_fraction_arithmetic_only': True,
    'both_full_FDH_and_original_Q_congruences_verified': True,
    'all_eight_stored_full_matrices_match_or_verify': True,
    'two_sided_inverse_verified': True,
    'determinant_and_all_pivots_verified': True,
    'complete_trace': str(trace),
    'baseline': N,
    'trace_gap': str(gap),
    'complete_m_term_residue_identity_at_same_point_verified': True,
    'complete_residue_sum': str(residue_sum),
    'residue_terms': residue_terms,
    'positive_evidence_scope': 'Exactly m15,S0,a=c1; no uniform sign, least-dimension, whole Task or mother conclusion',
    'elapsed_wall_seconds': time.perf_counter() - START,
}
target = BASE / 'FIXED_M15_CERTIFICATE_INDEPENDENT_VERIFICATION.json'
target.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'all_checks_passed': True, 'point': 'm15/S0/a=c1 existing certificate only', 'new_trace_inputs': 0, 'report': str(target), 'report_bytes': target.stat().st_size, 'report_sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'elapsed_wall_seconds': report['elapsed_wall_seconds']}))
