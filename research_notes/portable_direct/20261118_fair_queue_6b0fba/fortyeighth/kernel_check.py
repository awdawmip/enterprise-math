"""Enumerate signed six-axis paths and the five stationary router laws. Standard library."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, prod
import json

MODELS = [('iid', 0, 1), ('half+', 1, 1), ('half-', 1, -1),
          ('pure+', 2, 1), ('pure-', 2, -1)]
ZERO = (0,) * 6


def transition_numer(step, twice_eta, sign):
    return 2 - twice_eta + 6 * twice_eta * (step == sign % 6)


def endpoint_raw(n, eta2, direction):
    counts = Counter()
    marked = 0
    denom = 12 * 24**(n-1)
    for axes in product(range(6), repeat=n):
        w = prod(transition_numer((j-i) % 6, eta2, direction) for i,j in zip(axes,axes[1:]))
        if not w:
            continue
        for signs in product((-1,1), repeat=n):
            point = [0]*6
            for axis,s in zip(axes,signs):
                point[axis] += s
            counts[tuple(point)] += w
            marked += w * signs[-1] * sum((6*v-sum(signs))**3 for v in point)
    assert sum(counts.values()) == denom
    return counts, denom, F(marked,216*denom)


def orbit(x):
    # Coordinate sign flips, rotations and reflections. Only endpoint probabilities are compressed.
    u = tuple(abs(t) for t in x)
    return min(v[j:]+v[:j] for v in (u, u[::-1]) for j in range(6))


def moments(counts, denom, n, eta, marked):
    moment = [0]*5
    for x,w in counts.items():
        s = sum(x)
        h6 = [6*t-s for t in x]
        q36 = sum(z*z for z in h6)
        a216 = sum(z**3 for z in h6)
        obs = [q36,q36*q36,q36**3,s*a216,s*s*q36]
        moment = [v+w*y for v,y in zip(moment,obs)]
    m2,m4,m6,sa3,s2q = [F(v,denom*d) for v,d in zip(moment,(36,36**2,36**3,216,36))]
    cov = s2q - n*m2
    q4 = m4 - 35*F(n*n,36)
    q6 = m6 - F(9*n,2)*q4 - F(35*n**3,24)
    returns = [(1-eta**l)/6 + eta**l*(l%6==0) for l in range(1,n)]
    delta = 4*sum((n-l)*(r-F(1,6)) for l,r in enumerate(returns,1))
    assert m2 == F(5*n,6)
    assert m4 == m2*m2+4*sum((n-l)*(F(1,36)+F(2,3)*r) for l,r in enumerate(returns,1))
    assert sa3 == F(5*n,9) + delta and cov == delta
    assert marked == F(5,9) + 2*sum((r-F(1,6)) for r in returns)
    return {k:str(v) for k,v in [('m2',m2), ('m4',m4), ('m6',m6), ('k4',q4), ('k6',q6),
                                 ('Gamma4',q4/m2**2), ('E_S_sum_H3',sa3),
                                 ('E_S_Hi3',sa3/6), ('cov_S2_Hnorm2',cov),
                                 ('E_last_sign_sum_H3',marked)]}


def endpoint_table():
    rows, all_moments = {}, {}
    for n in range(1,5):
        tables = {}
        per_model = {}
        for name,e,d in MODELS:
            counts, den, marked = endpoint_raw(n,e,d)
            tables[name] = counts
            per_model[name] = moments(counts,den,n,F(e,2),marked)
        for intensity in ('half','pure'):
            assert tables[intensity+'+'] == tables[intensity+'-']
            assert per_model[intensity+'+'] == per_model[intensity+'-']
        if n==2:
            assert [F(tables[m][ZERO],den) for m,e,d in MODELS]==[F(2-e,24) for m,e,d in MODELS]
        reps = defaultdict(list)
        for x in tables['iid']:
            reps[orbit(x)].append(x)
        out = []
        for rep, keys in sorted(reps.items()):
            w = [tables[name][rep] for name in ('iid','half+','pure+')]
            for x in keys:
                assert [tables[name][x] for name in ('iid','half+','pure+')] == w
            out.append([''.join(map(str,rep)),len(keys),*w])
        rows[n] = dict(common_denominator=den, orbits=out, admissible_point_count=len(tables['iid']))
        all_moments[n] = {k:per_model[k] for k in ('iid','half+','pure+')}
    return rows,all_moments


def ordered_table():
    features = {}
    for name,e,s in MODELS:
        rows = {}
        for lag in (1,2):
            counts = Counter()
            for path in product(range(6),repeat=lag+1):
                w = prod(transition_numer((j-i)%6,e,s) for i,j in zip(path,path[1:]))
                counts[path[0],path[-1]] += w
            eta=F(e,2)
            for (i,j),num in counts.items():
                assert F(num,6*12**lag)==(1-eta**lag)/36+eta**lag*((j-i-s*lag)%6==0)/6
            rows[lag] = [str(F(counts[0,j],6*12**lag)) for j in range(6)]
        features[name]=rows
    good = [[i,j] for i,j in product(range(6),repeat=2)
            if len({features[name][1][(j-i)%6] for name,e,s in MODELS})==5]
    assert len(good)==12
    return features,good


def finite_observation(T):
    # Each axis-difference path has denominator 12^T for each of the five simple hypotheses.
    best = 0
    direction_loss_twice = 0
    total = [0]*5
    vectors = set()
    for plus in range(T+1):
        for minus in range(T-plus+1):
            other = T-plus-minus
            mult = comb(T,plus)*comb(T-plus,minus)*4**other
            weights = [2**T,7**plus,7**minus,12**T*int(plus==T),12**T*int(minus==T)]
            assert tuple(weights) not in vectors
            vectors.add(tuple(weights))
            best += mult*max(weights)
            direction_loss_twice += mult*min(weights[1],weights[2])
            for j,w in enumerate(weights):
                total[j] += mult*w
    assert total==[12**T]*5 and len(vectors)==comb(T+2,2)
    if T<=6:
        raw = same = 0
        for seq in product(range(6),repeat=T):
            weights=[prod(transition_numer(j,e,s) for j in seq) for _,e,s in MODELS]
            raw += max(weights)
            same += min(weights[1:3])
        assert (raw,same)==(best,direction_loss_twice)
    return dict(transitions=T, minimal_sufficient_classes=len(vectors),
                five_equal_prior_error=str(1-F(best,5*12**T)),
                half_direction_equal_prior_error=str(F(direction_loss_twice,2*12**T)))


def color_law(colors, length, eta2, direction):
    counts=Counter()
    for path in product(range(6),repeat=length):
        w = prod(transition_numer((j-i)%6,eta2,direction) for i,j in zip(path,path[1:]))
        counts[tuple(colors[i] for i in path)]+=w
    return counts


def color_checks():
    lengths=Counter()
    witness=(0,0,1,0,1,1)
    for bits in product(range(2), repeat=6):
        reflected=bits[::-1]
        symmetric=any(bits==reflected[j:]+reflected[:j] for j in range(6))
        first=None
        for k in range(1,7):
            counts=Counter(tuple(bits[(i+j)%6] for j in range(k)) for i in range(6))
            if any(v!=counts[w[::-1]] for w,v in counts.items()):
                first=k
                break
        assert (first is None)==symmetric
        lengths[first or 'never']+=1
        # Direct noisy forward and reverse axis-word enumeration at both boundary lengths.
        for k in (3,4):
            law=color_law(bits,k,1,1)
            assert all(law[w]==law[w[::-1]] for w in law)==(first is None or k<first)
    results=[]
    for name,e,s in MODELS:
        k=4
        law=color_law(witness,k,e,s)
        results.append(str(F(law[(0,0,1,0)],6*12**3)))
    assert F(results[1])-F(results[2])==F(1,48)
    return dict(binary_colorings=64, always_symmetric=lengths['never'],
                first_separation_length_four=lengths[4],
                word='0010', coloring='001011', probabilities_in_model_order=results)


def main():
    rows,raw_moments=endpoint_table()
    ordered,minimum=ordered_table()
    data=dict(model_order=[m for m,_,_ in MODELS],
              endpoint_orbit_columns=['canonical_absolute_D6_tuple','orbit_size',
                                      'iid_numerator','half_either_numerator','pure_either_numerator'],
              endpoint_orbits=rows, endpoint_moments=raw_moments,
              lag_rows_by_j_minus_i=ordered, minimal_fixed_singleton_axis_pairs_zero_based=minimum,
              exact_sample_tests=[finite_observation(T) for T in (0,1,2,3,4,6,8,16,32)],
              binary_colors=color_checks())
    print(json.dumps(data,indent=2))
if __name__=='__main__':
    main()
