"""EC49O exact rational model and finite-memory support verification.
No external dependencies. This auxiliary probability model is not native signed BRC/X6.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

W = X = Y = range(3)

def s(w, x, y):
    return int(y == (x + w) % 3) - int(y == (x + w + 1) % 3)

def atom(source, w, x, y):
    return F(1, 27) if source == 'Q' else F(2 + s(w, x, y), 54)

def valstr(q):
    return str(q.numerator) if q.denominator == 1 else f'{q.numerator}/{q.denominator}'

def eval_policy(continue_w, terminal_accept):
    # continue_w(w) returns True for both purchases, False for early REJECT;
    # terminal_accept(w,x,y) is the deterministic terminal decision on bought paths.
    result = []
    for source in ('P','Q'):
        acc = sum((atom(source,w,x,y) for w,x,y in product(W,X,Y)
                   if continue_w(w) and terminal_accept(w,x,y)), F(0))
        cost = sum((3*atom(source,w,x,y) for w,x,y in product(W,X,Y)
                    if continue_w(w)), F(0))
        result.append((acc,cost))
    return (result[0][0],result[1][0],result[0][1],result[1][1])

# Joint (W,X,Y) has strictly positive rational source masses and exact probabilities.
for source in ('P','Q'):
    mass = [atom(source,w,x,y) for w,x,y in product(W,X,Y)]
    assert len(mass) == 27 and min(mass) > 0 and sum(mass,F(0)) == 1
    for w,x in product(W,X):
        assert sum((atom(source,w,x,y) for y in Y),F(0)) == F(1,9)
    for w,y in product(W,Y):
        assert sum((atom(source,w,x,y) for x in X),F(0)) == F(1,9)

full = eval_policy(lambda w: True, lambda w,x,y: s(w,x,y)>0)
one_bit = eval_policy(lambda w: True,
                      lambda w,x,y: (y == x) if w==0 else (y == (x+1)%3))
zero_bit = eval_policy(lambda w: w==0, lambda w,x,y: y==x)
assert full == (F(1,2),F(1,3),F(3),F(3)), full
assert one_bit == (F(4,9),F(1,3),F(3),F(3)), one_bit
assert zero_bit == (F(1,6),F(1,9),F(1),F(1)), zero_bit

# Exactly optimize the support α−β for deterministic 0/1-memory causal policies.
# Initial visible W => STOP (-1) or BUY X with one memory label.
# After observing X, choose STOP or BUY Y with updated memory label;
# terminal accept is optimized exactly by taking positive signed mass.
# At STOP stages, acceptance has zero P−Q mass and cannot improve the support.
checks = {}
for m in (1,2):
    states = tuple(range(m))
    start_choices = tuple((-1,)+states)
    transition_choices = tuple((-1,)+states)
    best_integer = -1
    best_start = best_update = None
    n = 0
    for start in product(start_choices,repeat=3):
        for update in product(transition_choices,repeat=3*m):
            n += 1
            score = 0
            for x in X:
                for d2 in states:
                    for y in Y:
                        coefficient = sum(s(w,x,y) for w in W
                                          if start[w] >= 0 and
                                          update[x*m+start[w]] == d2)
                        score += max(0,coefficient)
            if score > best_integer:
                best_integer = score
                best_start,best_update = start,update
    expected = F(m,18)
    assert F(best_integer,54)==expected, (m,n,best_integer)
    checks[f'{m}_memory_states'] = {
        'enumerated_start_and_update_plans': n,
        'maximum_alpha_minus_beta': valstr(F(best_integer,54)),
        'integer_54_support': best_integer,
        'argmax_initial': list(best_start),
        'argmax_after_X': list(best_update),
    }
assert checks['1_memory_states']['enumerated_start_and_update_plans']==64
assert checks['2_memory_states']['enumerated_start_and_update_plans']==19683

# Independent per-X convex-extreme vertex certificate with up to two memory labels.
for x in X:
    all_scores=[]
    for assignment in product((-1,0,1),repeat=3):
        score=sum(max(0,sum(s(w,x,y) for w in W if assignment[w]==d))
                  for d,y in product((0,1),Y))
        all_scores.append(score)
    assert max(all_scores)==2 and len(all_scores)==27

report={
 'model':'EC49O three W histories, sequential adaptive priced ternary sensors',
 'probabilities':'Q=1/27; P=(2+s_w(x,y))/54; s=1_{y=x+w mod 3}-1_{y=x+w+1 mod 3}',
 'leaves_per_source':27,'strictly_positive':True,
 'sensor_cost_X':'1','sensor_cost_Y':'2',
 'full_four_vector':list(map(valstr,full)),
 'one_bit_four_vector':list(map(valstr,one_bit)),
 'zero_bit_four_vector':list(map(valstr,zero_bit)),
 'support_exact':{'0_bits':'1/18','1_bit':'1/9','2_bits':'1/6'},
 'sharp_support_gaps_vs_full':{'0_bits':'1/9','1_bit':'1/18'},
 'memory_lower_bound':'2 bits = 3 memory states; one bit insufficient',
 'enumeration':checks,
 'extreme_point_checks':81,
 'verification_scope':'Exact Fraction atoms, normalization, all W/source single-sensor marginals, 3 witness four-vectors; exact deterministic causal support enumeration; analytic convexity extends to all real fresh behavioral policies.',
 'not_claimed':'No native signed BRC, X6, 3D slice, source Result/CLAIM or independent review.'
}
with Path(__file__).with_name('EXACT_REPORT.json').open('w',encoding='utf-8') as f:
    json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
print(json.dumps(report,indent=2,ensure_ascii=False))
