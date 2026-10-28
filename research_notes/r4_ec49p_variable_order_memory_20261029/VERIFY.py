"""EC49P: exact positive rational two-source observation-model checks.
Pure standard-library Python, no external I/O except the report beside this script.
Theorems for all real policies are analytic; this checks finite cases and witnesses.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json

U = range(3)
ORDERS = ('X', 'Y')

def s(w, x, y):
    return int(y == (x + w) % 3) - int(y == (x + w + 1) % 3)

def mass(source, w, x, y):
    return F(1, 27) if source == 'Q' else F(2 + s(w, x, y), 54)

def fs(x):
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

def fmt(v):
    return list(map(fs, v))

for src in ('P', 'Q'):
    atom = [mass(src, w, x, y) for w, x, y in product(U, repeat=3)]
    assert len(atom) == 27 and min(atom) > 0 and sum(atom, F(0)) == 1
    for w, z in product(U, repeat=2):
        assert sum((mass(src, w, z, y) for y in U), F(0)) == F(1, 9)
        assert sum((mass(src, w, x, z) for x in U), F(0)) == F(1, 9)

# Deterministic zero-external-memory controllers: stage zero chooses
# STOP, X-first or Y-first by visible W; after the first sensor, the
# source-independent controller chooses BUY-OTHER or STOP for each (order,z).
# All terminal accept/reject rules are optimized exactly by taking the
# positive part of the signed P-Q terminal atom, not sampled.
best = F(-1)
best_plan = None
nplans = 0
for start in product((-1, 0, 1), repeat=3):
    for after in product((0, 1), repeat=6):
        nplans += 1
        signed_positive = 0
        for order_index, order in enumerate(ORDERS):
            for x, y in product(U, repeat=2):
                z = x if order == 'X' else y
                if not after[3 * order_index + z]:
                    continue
                coeff = sum(s(w, x, y) for w in U if start[w] == order_index)
                signed_positive += max(0, coeff)
        score = F(signed_positive, 54)
        if score > best:
            best, best_plan = score, (start, after)
assert nplans == 1728
assert best == F(1, 9), (best, best_plan)

# A direct controller evaluator for buy-both/stop-at-zero policies.
# routes[w] has (probability, initial_order, memory_label) triples.
# initial_order='N' means stop/reject. The decision at the terminal
# must be a function only of retained (order,label,x,y).
def routes_eval(routes, accept):
    out = []
    for src in ('P', 'Q'):
        a, c = F(0), F(0)
        for w, x, y in product(U, repeat=3):
            atom = mass(src, w, x, y)
            for p, order, label in routes[w]:
                if order == 'N':
                    continue
                c += atom * p * 3
                a += atom * p * accept(order, label, x, y)
        out.append((a, c))
    return out[0][0], out[1][0], out[0][1], out[1][1]

zero_route = {0: [(F(1), 'X', 0)],
              1: [(F(1), 'X', 0)],
              2: [(F(1), 'Y', 0)]}
def zero_accept(o, d, x, y):
    return int((y == x) if o == 'X' else (y == (x + 2) % 3))
zero_witness = routes_eval(zero_route, zero_accept)
assert zero_witness == (F(4, 9), F(1, 3), F(3), F(3)), zero_witness

code = {0: ('X', 0), 1: ('X', 1), 2: ('Y', 0)}
decode = {v: k for k, v in code.items()}
full_route = {w: [(F(1), *code[w])] for w in U}
def full_accept(o, d, x, y):
    return int(s(decode[(o, d)], x, y) == 1)
full_witness = routes_eval(full_route, full_accept)
assert full_witness == (F(1, 2), F(1, 3), F(3), F(3)), full_witness

# Exact sharp (alpha-beta) versus cost = c frontiers at seven rational c.
frontiers = []
for c in (F(0), F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(3)):
    b = c / 3
    one_routes = {w: [(b, *code[w]), (1 - b, 'N', 0)] for w in U}
    one = routes_eval(one_routes, full_accept)
    assert one[2:] == (c, c) and one[0]-one[1] == c / 18
    if c <= 2:
        a0 = min(F(1), c)
        a1 = max(F(0), c - 1)
        no_routes = {
            0: [(a0, 'X', 0), (1 - a0, 'N', 0)],
            1: [(a1, 'Y', 0), (1 - a1, 'N', 0)],
            2: [(F(1), 'N', 0)],
        }
        def no_accept(o, d, x, y):
            return int((y == x) if o == 'X' else y == (x + 1) % 3)
    else:
        extra = c - 2
        no_routes = {
            0: [(F(1), 'X', 0)],
            1: [(F(1), 'Y', 0)],
            2: [(extra, 'X', 0), (1 - extra, 'N', 0)],
        }
        def no_accept(o, d, x, y):
            return int((y == x or y == (x + 2) % 3) if o == 'X'
                       else (y == (x + 1) % 3))
    no = routes_eval(no_routes, no_accept)
    assert no[2:] == (c, c) and no[0] - no[1] == min(c / 18, F(1, 9)), (c, no)
    frontiers.append({'cost':fs(c),'zero_bit':fmt(no),'one_bit':fmt(one),
                      'zero_bit_support':fs(no[0]-no[1]),
                      'one_bit_support':fs(one[0]-one[1])})

# Test the universal full-to-one-bit formula on nontrivial rational
# fresh-behavioral policies. This is a finite reproduction check only.
rng = Random(490016)
def probs(k):
    vals = [rng.randrange(1, 7) for _ in range(k)]
    return [F(v, sum(vals)) for v in vals]

def full_stats():
    # initial actions A,R,X,Y; after first action A,R,B;
    # terminal acceptance is arbitrary rational with denominator 11.
    init = {w: probs(4) for w in U}
    after = {(w, o, z): probs(3) for w, o, z in product(U, ORDERS, U)}
    terminal = {(w, o, x, y): F(rng.randrange(12), 11)
                for w, o, x, y in product(U, ORDERS, U, U)}
    b = n = c0 = F(0)
    a = {-1:F(0), 0:F(0), 1:F(0)}
    for w in U:
        n += init[w][0] / 3
        for oi, o in enumerate(ORDERS):
            qstart = init[w][2+oi]
            first_cost = 1 if o=='X' else 2
            for z in U:
                qprefix = qstart / 9  # Q(W=w, first=z)=P(...)=1/9
                pa, pr, pb = after[(w, o, z)]
                n += qprefix * pa
                c0 += qprefix * (pa+pr) * first_cost
                b += qprefix * pb
                for other in U:
                    x,y = (z,other) if o=='X' else (other,z)
                    a[s(w,x,y)] += qprefix * pb * F(1,3) * terminal[(w,o,x,y)]
    alpha = n + sum(F(2+k,2)*a[k] for k in (-1,0,1))
    beta = n + sum(a.values())
    C = 3*b+c0
    assert F(0)<=b<=F(1) and F(0)<=n<=1-b
    assert F(0)<=c0<=2*(1-b)
    assert all(F(0)<=a[k]<=b/3 for k in (-1,0,1))
    # Independent direct 27-atom evaluation of the original full-history
    # behavioral policy, without using the likelihood-class decomposition.
    direct = []
    for src in ('P','Q'):
        acc = cost = F(0)
        for w,x,y in product(U, repeat=3):
            atom = mass(src,w,x,y)
            accepted = init[w][0]
            spent = F(0)
            for oi,o in enumerate(ORDERS):
                qstart = init[w][2+oi]
                z = x if o == 'X' else y
                pa,pr,pb = after[(w,o,z)]
                accepted += qstart * (pa + pb*terminal[(w,o,x,y)])
                spent += qstart * ((1 if o=='X' else 2) + pb*(2 if o=='X' else 1))
            acc += atom*accepted
            cost += atom*spent
        direct.append((acc,cost))
    direct_vec = (direct[0][0],direct[1][0],direct[0][1],direct[1][1])
    assert direct_vec == (alpha,beta,C,C), (fmt(direct_vec),fmt((alpha,beta,C,C)))
    return (alpha,beta,C,C),b,n,c0,a

def compiled_stats(b,n,c0,a):
    # Explicit one-bit controller, memory (order,D):
    # COMPLETE W0=(X,0), W1=(X,1), W2=(Y,0).
    # INCOMPLETE padded first-Y = (Y,1), then STOP.
    # All other incomplete paths STOP at stage zero.
    pad = c0/2
    qstop = 1-b-pad
    assert pad>=0 and qstop>=0
    t = n/(1-b) if b < 1 else F(0)
    r = {k: (3*a[k]/b if b else F(0)) for k in (-1,0,1)}
    assert all(F(0)<=v<=1 for v in r.values())
    Pacc=Qacc=PCost=QCost=F(0)
    for src in ('P','Q'):
        acc = cost = F(0)
        for w,x,y in product(U,repeat=3):
            atom = mass(src,w,x,y)
            o,d=code[w]
            acc += atom*(b*r[s(w,x,y)]+pad*t+qstop*t)
            cost += atom*(3*b+2*pad)
        if src=='P': Pacc,PCost=acc,cost
        else: Qacc,QCost=acc,cost
    return Pacc,Qacc,PCost,QCost

samples = []
for i in range(128):
    vec,b,n,c0,a = full_stats()
    compressed = compiled_stats(b,n,c0,a)
    assert vec == compressed, (i,fmt(vec),fmt(compressed))
    if i < 3:
        samples.append({'full_and_compiled':fmt(vec),'buy_both_Q_mass':fs(b),
                        'noncompleted_accept_mass':fs(n),'noncompleted_cost':fs(c0),
                        'accepted_Q_by_likelihood_type':{str(k):fs(v) for k,v in a.items()}})

report = {
 'research':'EC49P reversible sensor order = one-bit exact raw four-region compilation',
 'model':'W,X,Y in {0,1,2}; Q=1/27; P=(2+s_w(x,y))/54; cost X=1, Y=2',
 'source_atoms_per_source':27,'strictly_positive':True,
 'source_neutral_one_sensor_marginals':True,
 'raw_regions':'S_one_bit = S_full; S_zero_bit proper subset',
 'zero_bit_support_L':'1/9','one_bit_and_full_support_L':'1/6',
 'zero_bit_full_separator_gap':'1/18',
 'zero_bit_support_deterministic_plans':nplans,
 'terminal_rules_optimized_exactly':'positive signed terminal coefficients',
 'zero_bit_optimal_plan':{'initial':list(best_plan[0]),'buy_other_by_order_first':list(best_plan[1])},
 'zero_bit_full_cost_witness':fmt(zero_witness),
 'one_bit_full_cost_witness':fmt(full_witness),
 'cost_budget_support':{'zero_bit':'min(C/18,1/9)','one_bit_and_full':'C/18','cost_domain':'0<=C<=3'},
 'budget_witness_samples':frontiers,
 'random_rational_full_policies_compiled':128,
 'random_seed':490016,
 'three_sample_compilations':samples,
 'analytic_scope':'All real source-independent fresh behavioral policies; variable first sensor order; first-sensor/order/action recall; one bit external W memory; no uncounted shared seed.',
 'formal_admission':'UNREVIEWED_NOT_ADMITTED',
 'not_claimed':'No native signed BRC/X6/heartbeat dynamics, no native task claim, no independent review.'
}
Path(__file__).with_name('EXACT_REPORT.json').write_text(
    json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('raw_regions','zero_bit_support_L','one_bit_and_full_support_L','zero_bit_support_deterministic_plans','random_rational_full_policies_compiled','zero_bit_full_cost_witness','one_bit_full_cost_witness','cost_budget_support')},indent=2))
