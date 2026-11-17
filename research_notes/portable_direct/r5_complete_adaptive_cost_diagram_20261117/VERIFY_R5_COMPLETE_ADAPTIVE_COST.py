#!/usr/bin/env python3
"""Reproduce the complete R5 adaptive absolute-noise cost phase diagram."""
import collections
import hashlib
import itertools
import json
import pathlib
import sys

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
COHORT_SHA = 'a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'
TABLE_SHA = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
D3 = 1744659037213380157479321600000
D4 = 1882951873548292168718745600000
E, M, L = range(214, 222), range(223, 292), range(293, 315)

def load_checked(path, digest):
    contents = pathlib.Path(path).read_bytes()
    assert hashlib.sha256(contents).hexdigest() == digest, (path, 'SHA256 mismatch')
    return json.loads(contents)

def maximal_ambiguous(states, k, gap, n):
    """Maximal subsets admitting a common real observation for 2eta=gap."""
    a = sorted((n[k][b], b) for b in states)
    candidate = set()
    j = 0
    for i, (low, _b) in enumerate(a):
        j = max(j, i)
        while j < len(a) and a[j][0] - low <= gap:
            j += 1
        s = frozenset(b for _, b in a[i:j])
        if len(s) > 1:
            candidate.add(s)
    return sorted((s for s in candidate if not any(s < t for t in candidate)),
                  key=lambda x: (-len(x), tuple(sorted(x))))

def separated(states, budgets, n, gap):
    return all(any(abs(n[k][a] - n[k][b]) > gap for k in budgets)
               for a, b in itertools.combinations(states, 2))

def separation_margin(n, budgets):
    minimum, witnesses = None, []
    for a in range(256):
        for b in range(a + 1, 256):
            distance = max(abs(n[k][a] - n[k][b]) for k in budgets)
            if minimum is None or distance < minimum:
                minimum, witnesses = distance, [(a, b)]
            elif distance == minimum:
                witnesses.append((a, b))
    return minimum, witnesses

def early_two_queries(n, gap):
    rows = []
    for first in E:
        cliques = maximal_ambiguous(list(range(16)), first, gap, n)
        seconds = [next((j for j in E if separated(s, [j], n, gap)), None)
                   for s in cliques]
        feasible = all(j is not None for j in seconds)
        rows.append({'first': first, 'ambiguous_cliques': len(cliques),
                     'second_latest': max(seconds) if feasible and seconds else None,
                     'min_worst_cost': first + max(seconds) if feasible and seconds
                         else (first if not seconds else None)})
    return rows

def run(c, t):
    assert c['scientific_input'] == PIN and PIN in t['scope']
    n = {}
    for k in range(214, 315):
        coeff = [(int(z), int(v)) for z, v in c['all_budget_coefficients'][str(k)].items()]
        n[k] = [sum(v for z, v in coeff if z & b == z) for b in range(256)]
        assert n[k] == [int(x) for x in t['counts_and_cohorts'][str(k)]['counts']], k

    margins = []
    for expected_cost, Q in enumerate([(214,223,294),(214,223,295),(214,223,296)], start=731):
        assert sum(Q) == expected_cost
        d, witnesses = separation_margin(n, Q)
        assert witnesses
        assert not separated(range(256), Q, n, d)
        assert separated(range(256), Q, n, d - 1)
        margins.append({'cost': expected_cost, 'budgets': list(Q),
                        'min_pair_gap': str(d), 'min_pair_witnesses_count': len(witnesses),
                        'first_witness': list(witnesses[0])})
    a, b, z = (int(x['min_pair_gap']) for x in margins)
    assert (a, b, z) == (76289178155959966960189440,
                         3133722521542003559403356160,
                         13883516118328421520506880000)
    assert 0 < a < b < z < D3 < D4

    assert all(n[k][16] == n[k][32] for k in itertools.chain(E, M))
    assert all(n[k][2] == n[k][8] for k in itertools.chain(M, L))
    assert all(n[k][0] == n[k][64] for k in itertools.chain(E, L))
    late_gaps = {str(k): str(abs(n[k][16] - n[k][32])) for k in range(293, 297)}
    assert int(late_gaps['293']) == 0
    assert int(late_gaps['294']) == a
    assert int(late_gaps['295']) == b
    assert int(late_gaps['296']) > z

    fibre = [lo|m|l for lo in range(16) for m in (0,64) for l in (16,32)]
    assert len(fibre) == len(set(fibre)) == 64
    for k in range(214, 315):
        if k in E:
            for lo in range(16):
                assert len({n[k][lo|m|l] for m in (0,64) for l in (16,32)}) == 1
        elif k in M:
            for m in (0,64):
                assert len({n[k][lo|m|l] for lo in range(16) for l in (16,32)}) == 1
        elif k in L:
            for l in (16,32):
                assert len({n[k][lo|m|l] for lo in range(16) for m in (0,64)}) == 1
        else:
            assert len({n[k][s] for s in fibre}) == 1

    at_d3 = early_two_queries(n, D3)
    at_d4minus1 = early_two_queries(n, D4 - 1)
    assert min(x['min_worst_cost'] for x in at_d3 if x['min_worst_cost'] is not None) == 433
    assert min(x['min_worst_cost'] for x in at_d4minus1 if x['min_worst_cost'] is not None) == 433
    for k in E:
        assert min(abs(n[k][i] - n[k][j]) for i,j in itertools.combinations(range(16),2)) <= D3
    assert all(abs(n[k][16] - n[k][80]) <= D3 for k in range(223,224))
    assert all(abs(n[k][16] - n[k][32]) <= D3 for k in range(293,298))
    assert abs(n[224][16] - n[224][80]) >= D4
    assert abs(n[298][16] - n[298][32]) >= D4

    cliques = maximal_ambiguous(list(range(256)), 215, D4 - 1, n)
    seconds = []
    for s in cliques:
        second = next((k for k in E if separated(s, [k,224,298], n, D4 - 1)), None)
        assert second is not None and second <= 218
        seconds.append(second)
    hist = dict(sorted(collections.Counter(seconds).items()))
    assert len(cliques) == 19 and hist == {214:5,216:7,217:5,218:2}
    assert 215 + max(seconds) + 224 + 298 == 955
    assert min(abs(n[217][i]-n[217][j]) for i,j in itertools.combinations(range(16),2)) == D3
    assert 5 * 214 > 955


    # Full minimax noise/cost staircase for all finite adaptive policies.
    triples = [(214,223,294),(214,223,295),(214,223,296),
               (215,223,296),(216,223,296),(216,223,297),
               (217,223,297),(217,224,297),(217,224,298)]
    thresholds = [
        76289178155959966960189440,
        3133722521542003559403356160,
        13883516118328421520506880000,
        25845652773852463277015040000,
        58182461585441404127941754880,
        92195224223274674159616000000,
        267753525139190986466918400000,
        651779164849779092423599718400,
        D3]
    e_gaps={k:min(abs(n[k][a]-n[k][b]) for a,b in
                   itertools.combinations(range(16),2)) for k in E}
    m_gaps={k:abs(n[k][0]-n[k][64]) for k in M}
    l_gaps={k:abs(n[k][16]-n[k][32]) for k in L}
    assert len(thresholds)==len(set(thresholds))==9
    assert thresholds==sorted(thresholds)
    assert max(e_gaps.values())==D3
    assert 4*214>739
    chart=[]
    for i,q in enumerate(triples):
        tau=0 if i==0 else thresholds[i-1]
        first_e=next((k for k in E if e_gaps[k]>tau),None)
        first_m=next((k for k in M if m_gaps[k]>tau),None)
        first_l=next((k for k in L if l_gaps[k]>tau),None)
        assert (first_e,first_m,first_l)==q
        assert sum(q)==731+i
        margin,witnesses=separation_margin(n,q)
        assert margin==thresholds[i] and witnesses
        chart.append({'minimum_cost':sum(q),'budgets':list(q),
                      'left_gap_inclusive':str(tau),
                      'right_gap_exclusive':str(margin),
                      'minimizing_pair_count':len(witnesses),
                      'first_witness_pair':list(witnesses[0])})
    assert all(g<=D3 for g in e_gaps.values())
    assert min(row['min_worst_cost'] for row in early_two_queries(n,D3)
               if row['min_worst_cost'] is not None)==433
    assert next(k for k in M if m_gaps[k]>D3)==224
    assert next(k for k in L if l_gaps[k]>D3)==298
    assert 433+224+298==955
    # Universal impossibility at/above D4: intervals for states 11,14
    # overlap at all 101 budgets. No adaptive query can split them.
    no_go={k:abs(n[k][11]-n[k][14]) for k in range(214,315)}
    assert max(no_go.values())==D4
    no_go_max_budgets=[k for k,v in no_go.items() if v==D4]
    assert no_go_max_budgets==[217]

    return {'status':'PASS_R5_COMPLETE_ADAPTIVE_ABSOLUTE_NOISE_COST_PHASE_DIAGRAM',
            'input_pin':PIN,'cohort_sha256':COHORT_SHA,'complete_table_sha256':TABLE_SHA,
            'complete_three_query_staircase':chart,
            'no_go_threshold':str(D4),
            'no_go_pair':[11,14],
            'no_go_max_budgets':no_go_max_budgets,
            'exact_count_crosschecks':101*256,'budgets_checked':101,'masks_checked':256,
            'low_noise_minimax_cost_steps':[
                {'eta':'0 <= eta < '+str(a)+'/2','min_worst_cost':731,'certificate':margins[0]},
                {'eta':str(a)+'/2 <= eta < '+str(b)+'/2','min_worst_cost':732,'certificate':margins[1]},
                {'eta':str(b)+'/2 <= eta < '+str(z)+'/2','min_worst_cost':733,'certificate':margins[2]}],
            'late_pair_gaps':late_gaps,
            'four_query_plateau':{'eta':str(D3)+'/2 <= eta < '+str(D4)+'/2',
                'min_worst_cost':955,'hard_fibre_size':64,'early_factor_minimax_lower_bound':433,
                'middle_factor_earliest':224,'late_factor_earliest':298,
                'upper_strategy_first':215,'upper_strategy_last_two':[224,298],
                'maximal_observation_cliques':len(cliques),'second_budget_histogram':hist,
                'early_first_budget_lower_at_D3':at_d3,
                'early_first_budget_lower_at_D4_minus_one':at_d4minus1},
            'scope':'fixed derived integer count observer, adversarial real absolute noise, arbitrary finite adaptive policies; full cost/noise phase diagram verified for all eta >= 0'}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: python VERIFY_R5_COMPLETE_ADAPTIVE_COST.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json')
    print(json.dumps(run(load_checked(sys.argv[1], COHORT_SHA),
                         load_checked(sys.argv[2], TABLE_SHA)),
                     ensure_ascii=False, sort_keys=True, indent=2))
