"""Finite rational verification for C54. No stochastic simulation is used."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import factorial
from pathlib import Path
import json, time
import predictive_rank as p

ROOT = Path(__file__).resolve().parent
results = {}
checks = defaultdict(int)
started = time.monotonic()

# Independent pair scoring for all selected concatenations.
for history in p.HISTORIES:
    assert tuple(history.count(i) for i in range(4)) == (4, 2, 0, 0)
    assert sum(a == 0 and b == 1 for i, a in enumerate(history) for b in history[i+1:]) == 4
    assert [p.SCORES(history+tail) for tail in p.TAILS] == [(-2,2),(-2,0),(-2,-2)]
    checks['matched_history_score_rows'] += 1
assert [p.state_after(w) for w in p.HISTORIES] == [2,1,0]

# Explicit continuation law, determinant, and nuisance-free table.
T = [[p.suffix_probability(2,j,z) for j in (2,1,0)]
     for z in (F(4),F(1),F(1,4))]
expected = [[F(32,45),F(8,45),F(1,9)],
            [F(1,3),F(1,3),F(1,3)],
            [F(1,15),F(4,15),F(2,3)]]
assert T == expected
assert p.determinant(T) == F(1,15)
K = p.canonical_table(T)
assert K == [[F(1),F(1),F(1)],[F(1),F(4),F(32,5)],[F(1),F(16),F(64)]]
assert p.determinant(K) == 108
assert p.invariant_ratio(T) == F(116,71)
eps = F(1,100)
box = p.error_box(F(116,71),eps)
assert box[0] > 1
# Endpoint test for up to eight-percent entrywise input budget.
assert p.error_box(F(116,71),F(8,100))[0] > 1
results['canonical_witness'] = {'histories':[p.inherited.text(w) for w in p.HISTORIES],
    'tails':[p.inherited.text(w) for w in p.TAILS], 'reference_continuations':T,
    'canonical_table':K,'det_reference':F(1,15),'det_canonical':108,
    'invariant_ratio':F(116,71),'one_percent_interval':box,
    'eight_percent_interval':p.error_box(F(116,71),F(8,100)),
    'rank_two_prediction_for_canonical_last_entry':F(28),'actual_last_entry':F(64)}

# Row/column scale invariance, including non-even terminal weights.
for row_scale in product((F(1,3),F(1),F(5)),repeat=3):
    for col_scale in ((F(1),F(1),F(1)),(F(2),F(3),F(7)),(F(1,9),F(2,5),F(11))):
        scaled = [[T[i][j]*row_scale[i]*col_scale[j] for j in range(3)] for i in range(3)]
        assert p.canonical_table(scaled) == K
        assert p.invariant_ratio(scaled) == F(116,71)
        checks['positive_row_column_invariance'] += 1

# All 512 corners of the 1% nine-entry box preserve the determinant sign.
for signs in product((-1,1), repeat=9):
    a = [[T[i][j]*(1+eps*signs[3*i+j]) for j in range(3)] for i in range(3)]
    assert p.determinant(a) > 0
    assert box[0] <= p.invariant_ratio(a) <= box[1]
    checks['nine_entry_error_box_corners'] += 1

# Whole-word reference and DP agree on exact score mass for multiple counts.
configurations = [(1,1,1,1),(2,1,2,1),(2,2,1,1),(3,2,2,1),(4,2,2,1)]
rate_sets = [(F(1),F(1),(F(1,4),F(1),F(4))),
             (F(2),F(3),(F(3),F(1,2),F(2))),
             (F(3,2),F(2,3),(F(1),F(1),F(1)))]
base_example = None
for counts in configurations:
    ww = tuple(p.inherited.words(counts))
    assert len(ww) == factorial(sum(counts))//__import__('functools').reduce(lambda a,b:a*factorial(b),counts,1)
    for x,y,z in rate_sets:
        base = {w:p.reference_word(w,x,y,z) for w in ww}
        assert sum(base.values()) == 1
        hist = defaultdict(F)
        for w,mass in base.items():
            hist[p.SCORES(w)] += mass
        assert dict(hist) == p.reference_histogram(counts,x,y,z)
        checks['whole_word_DP_cases'] += 1
        checks['direct_word_probabilities'] += len(ww)
        if counts == p.COUNTS and (x,y,z) == rate_sets[0]:
            base_example = base

# Positive BRC reused unchanged for an entire 3780-word selected law.
assert base_example is not None
weight = lambda A,B: F(3,4)**int((F(A)+F(1,2)*B)**2)
selected,ops = p.selected_law(base_example,weight,use_brc=True)
checks['BRC_serial_recoalesce_calls'] += ops
assert sum(selected.values()) == 1
Qtable = p.table(selected)
assert p.canonical_table(Qtable) == K
assert p.invariant_ratio(Qtable) == F(116,71)
results['selected_witness'] = {'q':F(3,4),'gamma':F(1,2), 'probability_table':Qtable,
    'matched_nine_probability':sum(map(sum,Qtable)),
    'conditional_rows':[[v/sum(row) for v in row] for row in Qtable]}
for q,gamma in product((F(1,2),F(2,3),F(3,4)),(F(-1),F(0),F(1,2),F(1))):
    masses = [[base_example[h+c]*q**int((F(A)+gamma*B)**2)
               for c in p.TAILS for A,B in [p.SCORES(h+c)]] for h in p.HISTORIES]
    assert p.invariant_ratio(masses) == F(116,71)
    checks['quadratic_terminal_invariance'] += 1
for shift in range(-3,4):
    masses = [[base_example[h+c]/(3+(A+shift)**2+(B+2)**2)
               for c in p.TAILS for A,B in [p.SCORES(h+c)]] for h in p.HISTORIES]
    assert p.invariant_ratio(masses) == F(116,71)
    checks['non_even_terminal_invariance'] += 1

# Previous one-bit preparation has no more than two rows after this cut.
pl_sets = [tuple(map(F,r)) for r in [(1,1,1,1),(1,2,3,1),(3,1,1,2),(2,3,2,1),(1,4,1,3)]]
for rates,theta in product(pl_sets,(F(1,3),F(1),F(2),F(5))):
    for shift in range(3):
        a = [[p.inherited.memory_probability(h+c,rates,theta)/(3+(A+shift)**2+(B+2)**2)
               for c in p.TAILS for A,B in [p.SCORES(h+c)]] for h in p.HISTORIES]
        assert p.determinant(a) == 0
        checks['one_bit_null_tables'] += 1

# Any two fixed PL regimes produce a rank-at-most-two table.
for r1,r2 in combinations(pl_sets,2):
    for prior in (F(1,4),F(1,2),F(3,4)):
        for shift in range(3):
            a = [[(prior*p.inherited.old.pl_probability(h+c,r1)+(1-prior)*p.inherited.old.pl_probability(h+c,r2))
                  /(3+(A+shift)**2+(B+2)**2)
                  for c in p.TAILS for A,B in [p.SCORES(h+c)]] for h in p.HISTORIES]
            assert p.determinant(a) == 0
            checks['two_regime_null_tables'] += 1

# A separate explicit three-regime law proves exactly three required modes.
regimes = [pl_sets[1],pl_sets[2],pl_sets[0]]
mixture = [[sum(p.inherited.old.pl_probability(h+c,r) for r in regimes)/3
            for c in p.TAILS] for h in p.HISTORIES]
assert p.determinant(mixture) == F(19,70769988256968000)
assert p.invariant_ratio(mixture) != 1
results['three_fixed_regime_witness'] = {'rates':regimes,'priors':[F(1,3)]*3,
    'unselected_joint_table':mixture,'determinant':p.determinant(mixture),
    'invariant_ratio':p.invariant_ratio(mixture)}

# Direct mixture enumeration vs state-space DP, preserving regime labels.
mixture_full = {w:sum(p.inherited.old.pl_probability(w,r) for r in regimes)/3
                for w in base_example}
mixture_hist = defaultdict(F)
for w,mass in mixture_full.items():mixture_hist[p.SCORES(w)] += mass
combined = defaultdict(F)
for rate in regimes:
    for score,mass in p.inherited.old.pl_weighted_dp(p.COUNTS,rate).items():
        combined[score] += mass/3
assert dict(mixture_hist) == dict(combined)
assert sum(mixture_full.values()) == 1
checks['mixture_direct_word_probabilities'] += len(mixture_full)
checks['mixture_DP_cases'] += 1

# Vandermonde continuation determinant and direct product probabilities.
for r in range(1,8):
    for den in (1,2,5):
        rates = [F(i+1,den) for i in range(r+1)]
        a = [[p.suffix_probability(r,j,z) for j in range(r+1)] for z in rates]
        assert p.determinant(a) == p.suffix_determinant_formula(rates) > 0
        for z,row in zip(rates,a):
            assert sum(row) == 1
            for j,prob in enumerate(row):
                word = (2,)*j+(3,)+(2,)*(r-j)
                assert prob == p.inherited.old.pl_probability(word,(F(1),F(1),z,F(1)))
                checks['tail_direct_products'] += 1
        checks['Vandermonde_identities'] += 1
    rates = [F(1)]*(r+1)
    assert p.determinant([[p.suffix_probability(r,j,z) for j in range(r+1)] for z in rates]) == 0
    checks['equal_rate_degeneracies'] += 1

# Independent binary word counts validate the recurrence.
for a in range(1,8):
    for b in range(1,6):
        hist = [0]*(a*b+1)
        for w in p.inherited.words((a,b,0,0)):
            inv = sum(x==0 and y==1 for i,x in enumerate(w) for y in w[i+1:])
            hist[inv] += 1
            checks['binary_words'] += 1
        assert tuple(hist) == p.inversion_counts(a,b)
        checks['binary_histograms'] += 1
mins = [p.minimum_carrier(k,bound) for k,bound in [(2,1260),(3,25200),(4,302400)]]
assert [r['integer'] for r in mins] == [1260,25200,302400]
results['minimum_matching_carriers'] = mins
# Divisor counts are computed independently by divisor sieve.
N = 302400
tau=[0]*(N+1)
for divisor in range(1,N+1):
    for multiple in range(divisor,N+1,divisor):tau[multiple]+=1
assert tau[1260]==36 and max(tau[1:1260])==32
assert tau[25200]==90 and max(tau[1:25200])==84
assert tau[302400]==168 and tau[277200]==180
results['divisor_comparison']={'tau1260':36,'previous_max1260':32,
    'tau25200':90,'previous_max25200':84,
    'tau302400':168,'smaller_integer277200_tau':180}
checks['divisor_sieve_integers'] = N

# Initial 1..5 each has a unique complete word; positive terminal weighting
# preserves its probability and the initial rho_1 remains a symbolic label.
for counts in [(0,0,0,0),(1,0,0,0),(0,1,0,0),(2,0,0,0),(0,0,1,0)]:
    ww=list(p.inherited.words(counts));assert len(ww)==1
    assert p.reference_word(ww[0]) == 1
    checks['initial_1_to_5'] += 1

results['checks']=dict(checks)
results['elapsed_seconds']=time.monotonic()-started
results['status']='ALL_DECLARED_ASSERTIONS_PASSED'
(ROOT/'results'/'exact_checks.json').write_text(json.dumps(p.serialize(results),ensure_ascii=False,indent=2))
print(json.dumps({'status':results['status'],'checks':dict(checks),'elapsed_seconds':results['elapsed_seconds']},indent=2))
