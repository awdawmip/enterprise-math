"""Exact finite certificates for the classical 2**budget covering horizon.

No floating point, probable-prime tests, optimizer or unbounded-orbit scan.
The arbitrary-budget implication is the theorem proved/cited in proof.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import json
from math import gcd, isqrt, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
ROOT = next(p for p in HERE.parents if (p / BASE_REL).is_file())
SOURCE = next(p for p in (ROOT / 'src', ROOT / 'vendor_src')
              if (p / 'enterprise_math/brc_transport.py').is_file())
PRIMALITY = {}


def prime(p):
    if p not in PRIMALITY:
        assert p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))
        PRIMALITY[p] = {'trial_bound': isqrt(p), 'deterministic': True}


def factor(n):
    m, d, ans = n, 2, []
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d
            e += 1
        if e:
            ans.append([d, e])
        d = 3 if d == 2 else d + 2
    if m > 1:
        ans.append([m, 1])
    for p, e in ans:
        prime(p)
        assert e > 0
    assert prod(p**e for p, e in ans) == n
    return ans


def status(k, qs, proper=False):
    """One 2**len(qs) prefix; full-coverage conclusion uses the theorem."""
    assert k >= 3 and k % 2 and qs == tuple(sorted(set(qs)))
    for q in qs:
        prime(q)
    horizon = 1 << len(qs)
    rows = []
    missing = None
    for n in range(1, horizon+1):
        x = (k << n) - 1
        hits = [q for q in qs if x % q == 0 and (not proper or q < x)]
        rows.append({'n': n, 'hits': hits})
        if not hits and missing is None:
            missing = n
    return {'horizon': horizon, 'proper': proper, 'first_missing': missing,
            'full_cover_by_interval_theorem': missing is None, 'rows': rows}


def search(k, budget, qs=(), proper=False):
    obs = status(k, qs, proper)
    node = {'selected': list(qs), 'observation': obs}
    n = obs['first_missing']
    if n is None:
        return dict(node, answer=True, children=[])
    if len(qs) == budget:
        return dict(node, answer=False, children=[])
    x = (k << n) - 1
    fs = factor(x)
    candidates = [p for p, _ in fs if p not in qs and (not proper or p < x)]
    children = []
    for p in candidates:
        child = search(k, budget, tuple(sorted(qs+(p,))), proper)
        children.append({'added': p, 'node': child})
        if child['answer']:
            return dict(node, answer=True, missing_factorization=fs,
                        candidates=candidates, children=children)
    return dict(node, answer=False, missing_factorization=fs,
                candidates=candidates, children=children)


def check_tree(k, budget, node, qs=(), proper=False):
    assert node['selected'] == list(qs)
    obs = status(k, qs, proper)
    assert obs == node['observation']
    n = obs['first_missing']
    if n is None:
        assert node['answer'] and not node['children']
        return True, 1
    assert n <= 1 << len(qs)
    if len(qs) == budget:
        assert not node['answer'] and not node['children']
        return False, 1
    x = (k << n) - 1
    fs = factor(x)
    assert fs == node['missing_factorization']
    candidates = [p for p, _ in fs if p not in qs and (not proper or p < x)]
    assert candidates == node['candidates']
    count = 1
    answers = []
    for i, child in enumerate(node['children']):
        assert child['added'] == candidates[i]
        answer, nodes = check_tree(k, budget, child['node'],
                                  tuple(sorted(qs+(child['added'],))), proper)
        answers.append(answer)
        count += nodes
    if node['answer']:
        assert answers and answers[-1] and not any(answers[:-1])
    else:
        assert len(answers) == len(candidates) and not any(answers)
    return node['answer'], count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=HERE/'window_certificate.json')
    args = parser.parse_args()
    base_bytes = (ROOT/BASE_REL).read_bytes()
    base = json.loads(base_bytes)
    checks = {}
    for name, expected in base['project_source_blobs'].items():
        b = (SOURCE/'enterprise_math'/name).read_bytes()
        observed = sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        assert observed == expected
        checks[name] = {'expected': expected, 'observed': observed, 'match': True}
    sys.path.insert(0, str(SOURCE))
    from enterprise_math.brc_transport import Affine, EffectHistogram
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),),(1,)), 1)])
    assert step.entries == ((Fraction(1), Affine(((2,),),(1,)), 1),)
    k, Q = 509203, (3, 5, 7, 13, 17, 241)
    x = k-1
    values = {}
    for n in range(1, 65):
        (point, weights), = step.evaluate((x,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        x = int(point[0])
        assert x == (k << n)-1
        values[n] = x
    cover = status(k, Q, True)
    assert cover['full_cover_by_interval_theorem']
    private = [1,3,4,11,15,19]
    pairs = [{'i': i, 'j': j, 'gcd': gcd(values[i], values[j])}
             for i,j in combinations(private, 2)]
    assert all(row['gcd'] == 1 for row in pairs)
    assert max(private) <= 1 << 5
    minimal_witness = []
    for q in Q:
        n = next(n for n in range(1,33)
                 if values[n] % q == 0 and all(values[n] % p for p in Q if p != q))
        minimal_witness.append({'q': q, 'private_n': n,
                                'within_2_pow_s_minus_one': True})
    examples = []
    for kk, budget, proper in [(3,0,False),(3,1,False),(3,2,False),(3,3,False),
                                (3,3,True),(509203,6,True)]:
        tree = search(kk,budget,proper=proper)
        answer, nodes = check_tree(kk,budget,tree,proper=proper)
        assert answer == (kk == 509203)
        examples.append({'k': kk,'budget':budget,'proper':proper,
                         'answer':answer,'node_count':nodes,'tree':tree})
    binary = []
    for t in range(1,13):
        rows = [(1<<(i-1),1<<i) for i in range(1,t+1)]
        assert all(any(n%m == r for r,m in rows) for n in range(1,1<<t))
        assert all((1<<t)%m != r for r,m in rows)
        binary.append({'classes':rows,'covered_initial':(1<<t)-1,
                       'first_missing':1<<t})
    fc_path = ROOT/'research_notes/portable_direct/riesel_completion_20261120/finite_cover/exact_complexity_certificate.json'
    fc = json.loads(fc_path.read_text())
    a = int(fc['root_a'])
    H = [h if h else 105 for h in fc['H_u']]
    extra = tuple(sorted(row['q'] if 'q' in row else row['p'] for row in fc['Q0']))
    assert len(extra) == 5 and len(H) == 36
    fiber_records = []
    for h in sorted(H):
        coverage = []
        for v in range(32):
            n = 2*h+210*v
            hits = [q for q in extra if (a*a*pow(2,n,q)-1)%q == 0]
            assert hits
            coverage.append({'v':v,'n':n,'hits':hits})
        fiber_records.append({'h':h,'coverage':coverage})
    assert max(r['n'] for f in fiber_records for r in f['coverage']) == 6720
    assert 2*a*a-1 > max(extra)
    result = {
        'schema':'enterprise-math.riesel-budget-horizon.v1',
        'researcher_id':'EM-DIRECT-970E1C',
        'research_activity_id':'RA-D2EC212845B63844081F9A14',
        'status':'classical theorem application and exact finite checks; not independent project Review',
        'base_certificate_sha256':sha256(base_bytes).hexdigest(),
        'native_source_commit':base['project_source_commit'],
        'native_source_checks_before_import':checks,
        'native_update_count':64,
        'classical_theorem_doi':'10.1090/S0002-9939-1970-0258719-2',
        'horizon_formula':'2**t',
        'k509203':{'cover':cover,'exact_total_cost':6,
                   'six_coprime_exponents':private,'gcd_checks':pairs,
                   'each_prime_has_private_index_at_most_32':minimal_witness},
        'complete_search_examples':examples,
        'binary_sharpness_examples':binary,
        'old_hole_budget5':{'sample_count':1152,'max_exponent':6720,
                           'same_extra_primes':extra,'fibers':fiber_records,
                           'root_source_sha256':sha256(fc_path.read_bytes()).hexdigest()},
        'deterministic_prime_checks':PRIMALITY,
        'not_claimed':['optimal horizon for each fixed k','efficient factoring or cover search',
                       'decidability of unrestricted finite-cover existence',
                       'infinite covering cost of the fixed old root']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'native_updates':64,'k509203_tau':6,
                      'gcd_pairs':15,'search_cases':len(examples),
                      'search_nodes':[e['node_count'] for e in examples],
                      'old_hole_joint_sample':1152}))


if __name__ == '__main__':
    main()
