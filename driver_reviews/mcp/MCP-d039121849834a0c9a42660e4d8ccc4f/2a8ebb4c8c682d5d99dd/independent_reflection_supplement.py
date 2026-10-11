"""New bounded reflection/derivative checks over F_p only.

No primary campaign, Gauss composition, lifted harmonic calculation, provider
query, or author implementation is imported or executed.  H is built by the
explicit Legendre coefficient formula; reflection uses binomial expansion.
"""
from pathlib import Path
from math import comb
import hashlib
import json

ROOT = Path(__file__).resolve().parent
TASK = 'RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT'
AUTHOR_MEMO = ROOT.parent / 'cm24-next-p3-20261011/GLOBAL_REFLECTION_FIXES_CARRIER_BOUNDARY_PREPARATION.md'


def reflect(a, p):
    return [sum((-1)**j * comb(n, j) * a[n]
                for n in range(j, len(a))) % p for j in range(len(a))]


def diff(a, p):
    return [n*a[n] % p for n in range(1, len(a))]


def d_h(a, p):
    return [((j+1)**2 * (a[j+1] if j+1 < len(a) else 0)
             -(3*j+1)*(3*j+2)*pow(9, -1, p)*a[j]) % p
            for j in range(len(a))]


def rank(matrix, p):
    a = [row[:] for row in matrix]
    row = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(row, len(a)) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = pow(a[row][col], -1, p)
        a[row] = [v*scale % p for v in a[row]]
        for r in range(len(a)):
            if r != row and a[r][col] % p:
                scale = a[r][col]
                a[r] = [(u-scale*v) % p for u, v in zip(a[r], a[row])]
        row += 1
    return row


def mul(a, b, p):
    return ((a[0]*b[0]+2*a[1]*b[1]) % p,
            (a[0]*b[1]+a[1]*b[0]) % p)


def evaluate(a, x, p):
    y = (0, 0)
    for c in reversed(a):
        y = mul(y, x, p)
        y = ((y[0]+c) % p, y[1])
    return y


def one_prime(p, historical):
    m = (p-1)//6
    size = p-1
    h = [(-1)**n*comb(2*m, n)*comb(2*m+n, n) % p
         if n <= 2*m else 0 for n in range(size)]
    i = [0]
    for j in range(p-2):
        i.append(((3*j+1)*(3*j+2)*i[-1]-2)
                 *pow(9*(j+1)**2, -1, p) % p)
    ir = reflect(i, p)
    h_ref = reflect(h, p)
    assert h_ref == h and h[2*m] != 0
    assert not any(d_h(h, p))
    assert d_h(i, p) == [(-2*pow(9, -1, p)) % p]*size
    assert reflect([1]*size, p) == [p-1]*size
    i1 = sum(i) % p
    assert [(u+v) % p for u, v in zip(i, ir)] == [i1*c % p for c in h]
    b = -i1*pow(2, -1, p) % p
    odd = [(u-v)*pow(2, -1, p) % p for u, v in zip(i, ir)]
    carrier = [(u+b*v) % p for u, v in zip(i, h)]
    assert odd == carrier
    assert reflect(carrier, p) == [-v % p for v in carrier]
    assert d_h(carrier, p) == d_h(i, p)
    assert b == historical['boundary']  # comparison only; not a definition
    d_i = diff(i, p)
    d_ir_evaluated = reflect(d_i, p)
    d_carrier = diff(carrier, p)
    derivative_plus = [(u+v)*pow(2, -1, p) % p
                       for u, v in zip(d_i, d_ir_evaluated)]
    derivative_wrong_minus = [(u-v)*pow(2, -1, p) % p
                              for u, v in zip(d_i, d_ir_evaluated)]
    assert d_carrier == derivative_plus
    assert reflect(d_carrier, p) == d_carrier
    wrong_indices = [n for n, (u, v) in enumerate(zip(d_carrier, derivative_wrong_minus))
                     if u != v]
    assert wrong_indices
    matrix = []
    for j in range(size):
        row = [0]*size
        row[j] = -(3*j+1)*(3*j+2)*pow(9, -1, p) % p
        if j+1 < size:
            row[j+1] = (j+1)**2 % p
        matrix.append(row)
    dh_rank = rank(matrix, p)
    assert dh_rank == size-1
    inv4 = pow(4, -1, p)
    xplus = (2*inv4 % p, inv4)
    xminus = (2*inv4 % p, -inv4 % p)
    branches = []
    for sign, x in (('+', xplus), ('-', xminus)):
        value = evaluate(carrier, x, p)
        slope = evaluate(d_carrier, x, p)
        i_value = evaluate(i, x, p)
        i_slope = evaluate(d_i, x, p)
        h_value = evaluate(h, x, p)
        h_slope = evaluate(diff(h, p), x, p)
        assert value[0] == 0 and slope[1] == 0
        if p in (13, 19):
            assert h_value == (0, 0)
            assert value == i_value
            assert slope != i_slope
            assert h_slope != (0, 0)
        branches.append({'branch': sign, 'A': value, 'A_prime': slope,
                         'I': i_value, 'I_prime': i_slope,
                         'H': h_value, 'H_prime': h_slope})
    assert branches[0]['A'][1] == -branches[1]['A'][1] % p
    assert branches[0]['A_prime'] == branches[1]['A_prime']
    return {'prime': p, 'I': i, 'H': h, 'A': carrier, 'I_at_1': i1,
            'reflection_boundary': b, 'historical_boundary_comparison': 'PASS',
            'forcing_including_last_equation': 'PASS', 'reflection_all_coefficients': 'PASS',
            'homogeneous_matrix_dimension': size, 'homogeneous_matrix_rank': dh_rank,
            'homogeneous_kernel_dimension': 1,
            'degree_of_nonzero_C_xpH': p+2*m, 'upper_degree_of_E_minus_Eref': p-1,
            'odd_projection_derivative_plus': 'PASS',
            'wrong_minus_derivative_negative_indices': wrong_indices,
            'marked_branches': branches,
            'CM0_root_claim': p in (13, 19)}


if __name__ == '__main__':
    historical_path = ROOT / 'INDEPENDENT_FINITE_RESULTS.json'
    historical_bytes = historical_path.read_bytes()
    historical = {row['prime']: row for row in json.loads(historical_bytes)['primes']}
    memo_bytes = AUTHOR_MEMO.read_bytes()
    result = {
        'scope': 'SEPARATE_BOUNDED_FP_REFLECTION_SUPPLEMENT_ONLY',
        'task_id': TASK, 'researcher_id': 'EM-ENTERPRISE-3F2857',
        'activity_id': 'RA-C05628958AD19A1F120F685E',
        'author_code_read_imported_or_executed': False,
        'primary_six_prime_campaign_rerun': False,
        'lifted_harmonic_or_Gauss_composition_recomputed': False,
        'memo_sha256': hashlib.sha256(memo_bytes).hexdigest(),
        'historical_results_sha256': hashlib.sha256(historical_bytes).hexdigest(),
        'primes': [one_prime(p, historical[p]) for p in (7, 13, 19)],
        'all_checks': 'PASS'
    }
    output = ROOT / 'REFLECTION_SUPPLEMENT_FP_RESULTS.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'all_checks': 'PASS', 'primes': [7, 13, 19],
                      'output': str(output), 'bytes': output.stat().st_size}))
