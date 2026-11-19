"""Exact small-state checks for clipped reflection, guarded mixing and word costs."""
import argparse
import json
from fractions import Fraction
from itertools import product
from math import comb, gcd, lcm
from pathlib import Path


def primitive(row):
    row = tuple(row)
    common = gcd(*row)
    if not common:
        return row
    if next(x for x in row if x) < 0:
        common = -common
    return tuple(x // common for x in row)


def integers(row):
    row = tuple(map(Fraction, row))
    den = lcm(*(x.denominator for x in row))
    return primitive(int(x * den) for x in row)


def insert(basis, row):
    row = primitive(row)
    for i in range(len(row)):
        value = row[i]
        if value:
            if i not in basis:
                basis[i] = row
                return True
            old = basis[i]
            row = primitive(old[i] * u - value * v for u, v in zip(row, old))
    return False


def echelon(rows):
    basis = {}
    for row in rows:
        insert(basis, row)
    return basis


def kernel(basis, size):
    """Integer null-space vectors of a dictionary whose keys are pivot columns."""
    vectors = []
    for free in sorted(set(range(size)) - basis.keys()):
        v = [Fraction(int(j == free)) for j in range(size)]
        for i in sorted(basis, reverse=True):
            old = basis[i]
            v[i] = -sum((old[j] * v[j] for j in range(i+1, size)), Fraction()) / old[i]
        vectors.append(integers(v))
    return vectors


def pairing(f, v):
    return sum(x * y for x, y in zip(f, v))


def powers(M, d):
    return tuple(x ** d for x in range(M+1))


def setting_rows(M, word):
    states = list(range(M+1))
    for letter in word:
        states = [min(x+1, M) if letter == "A" else M-x for x in states]
    return [tuple(1 for x in states), tuple(states), tuple(x*x for x in states)]


def settings(M, T):
    if T == 0:
        return [""]
    count = min(M-2, 2*T-1)
    for right in range(min(count,T), -1, -1):
        left = count-right
        if left <= T-1 and (right+1)//2 + (left+1)//2 == (count+1)//2:
            break
    else:
        raise AssertionError("two endpoint budgets failed to pack")
    words = [""]
    for count, prefix in [(right, ""), (left, "R")]:
        indices = list(range(2, count+1, 2))
        if count % 2:
            indices.append(count)
        words.extend(prefix + "A"*j for j in indices)
    return words


def lifted(row, op, guard):
    a = row[1:] + row[-1:]
    r = row[::-1]
    if op == "A":
        return a
    if op == "R":
        return r
    den, numer = guard
    return tuple(k*u + (den-k)*v for k, u, v in zip(numer, a, r))


def lift_actual(row, op, guard):
    # lifted multiplies a random read by the common denominator; undo it here.
    f = lifted(row, op, guard)
    return tuple(Fraction(x, guard[0]) for x in f) if op == "B" else f


def pack(probabilities):
    den = lcm(*(x.denominator for x in probabilities))
    numer = tuple(int(x*den) for x in probabilities)
    assert all(0 <= k <= den for k in numer)
    return den, numer


def advance(basis, alphabet, guard):
    nxt = dict(basis)
    for row in basis.values():
        for op in alphabet:
            insert(nxt, lifted(row, op, guard))
    return nxt


def endpoint_set(M, T):
    if not T:
        return []
    return sorted(set(range(min(T-1, M+1))) | set(range(max(0, M-T+1), M+1)))


def proposed_rows(M, T, coeff):
    a, b, c = coeff
    if T == 0:
        return [(str(j), powers(M,j)) for j in range(3)]
    if T == 1:
        labeled = [(str(j), powers(M,j)) for j in range(4)]
    else:
        labeled = [(str(j), powers(M,j)) for j in range(2*T)]
        beta = -Fraction((2*T-1)*(M-1), 2) + b/a
        top = integers(x**(2*T+1) + beta*x**(2*T) for x in range(M+1))
        labeled.append(("top", top))
    labeled.extend((f"e{x}", tuple(int(j == x) for j in range(M+1)))
                   for x in endpoint_set(M,T))
    return labeled


def quadratic_rank(M, T, coeff):
    if T == 0:
        return 3
    if T == 1:
        return min(M+1,5)
    a, b, c = coeff
    return min(M+1, 4*T) - int(M == 4*T-1 and b/a == -(M-1))


def samples(M):
    k = M-1
    candidates = {
        "square": (Fraction(1,M*M), Fraction(0), Fraction(0)),
        "reversed": (Fraction(1,k*k), Fraction(-2,k), Fraction(1)),
        "balanced": (Fraction(1,k*k), Fraction(-1,k), Fraction(1,2)),
        "balanced_concave": (-Fraction(1,k*k), Fraction(1,k), Fraction(1,2)),
        "affine_tilt": (Fraction(1,4*M*M), Fraction(1,4*M), Fraction(1,5)),
    }
    for name, coeff in candidates.items():
        a, b, c = coeff
        for endpoint in [Fraction(0), Fraction(2,5), Fraction(1)]:
            yield name, coeff, endpoint, pack([a*x*x+b*x+c for x in range(M)]+[endpoint])


def word_layers(M, T, guard):
    current = {"": (powers(M,1), powers(M,2))}
    yield current
    for k in range(T):
        nxt = {}
        for word, reads in current.items():
            for op in "ARB":
                nxt[op+word] = tuple(lift_actual(f, op, guard) for f in reads)
        current = nxt
        yield current


def first_separation(v, layers):
    for layer in layers:
        for word in sorted(layer):
            for degree, read in enumerate(layer[word], 1):
                d = pairing(read, v)
                if d:
                    return word, degree, d
    return None


def law_pair(v):
    """Two positive probability distributions with difference v / denominator."""
    n = len(v)
    assert sum(v) == 0 and max(map(abs,v)) > 0
    uniform_num = max(map(abs,v))+1
    den = n*uniform_num
    altered = [uniform_num+x for x in v]
    assert min(altered) > 0 and sum(altered) == den
    return {"base_numerator_per_state": uniform_num, "shifted_numerators": altered,
            "shared_denominator": den}


def certificate(M, T, name):
    name, coeff, endpoint, guard = next(item for item in samples(M)
                                        if item[0] == name and item[2] == Fraction(2,5))
    marked = []
    basis = {}
    for label, row in proposed_rows(M, T, coeff):
        if insert(basis,row):
            marked.append((label,row))
    layers = list(word_layers(M, T+1, guard))
    records = []
    for i, (label, row) in enumerate(marked):
        other = echelon(r for j, (k,r) in enumerate(marked) if j != i)
        v = next(v for v in kernel(other,M+1) if pairing(row,v))
        assert all((pairing(f,v) != 0) == (j == i) for j, (k,f) in enumerate(marked))
        hit = first_separation(v, layers[:T+1]) if sum(v) == 0 else None
        datum = {"deleted": label, "deleted_row": row, "integer_contrast": v}
        if not sum(v):
            word, degree, difference = hit
            laws = law_pair(v)
            datum.update({"strictly_positive_laws": laws, "shortest_word": word,
                          "moment_degree": degree,
                          "exact_probability_gap": str(Fraction(difference)/laws["shared_denominator"])})
        else:
            # At deletion of mass the current total itself separates. Positivity
            # can be made strict, but equal totals would erase this witness.
            offset = max(map(abs,v)) + 1
            datum.update({"shortest_word":"", "moment_degree":0, "total_gap":sum(v),
                          "positive_unnormalized_base":[offset]*(M+1),
                          "positive_unnormalized_shift":[offset+x for x in v]})
        records.append(datum)
    exhausted = kernel(basis,M+1)
    later = []
    for v in exhausted:
        assert first_separation(v, layers[:T+1]) is None
        hit = first_separation(v, layers)
        if hit is not None:
            word, moment, gap = hit
            laws = law_pair(v)
            later.append({"integer_contrast":v, "strictly_positive_laws":laws,
                          "first_separating_word":word,"moment_degree":moment,
                          "exact_probability_gap":str(Fraction(gap)/laws["shared_denominator"])})
    return {"M":M, "T":T, "guard":name, "coefficients":list(map(str,coeff)),
            "p_at_M":str(endpoint), "basis_size":len(marked),
            "basis_deletions":records,"horizon_ambiguities_then_separated":later}


def original_setting_deletions(M, T, words):
    measurements = {w:setting_rows(M,w)[1:] for w in words}
    all_deterministic = []
    for length in range(T+1):
        layer = {}
        for letters in product("AR", repeat=length):
            w = "".join(letters)
            layer[w] = setting_rows(M,w)[1:]
        all_deterministic.append(layer)
    cases = []
    for omit in words:
        others = [powers(M,0)]
        for w in words:
            if w != omit:
                others.extend(measurements[w])
        v = next(v for v in kernel(echelon(others),M+1)
                 if any(pairing(v,f) for f in measurements[omit]))
        assert all(pairing(f,v)==0 for f in others)
        laws = law_pair(v)
        word,degree,gap = first_separation(v,all_deterministic)
        cases.append({"omitted_setting":omit,"strictly_positive_laws":laws,
                      "integer_contrast":v,"shortest_separating_word":word,
                      "moment_degree":degree,
                      "probability_gap":str(Fraction(gap)/laws["shared_denominator"])})
    return cases


def bit_budget_witness():
    M, word, guard_name = 11, "BBRABBAB", "affine_tilt"
    _, _, _, guard = next(item for item in samples(M)
                            if item[0]==guard_name and item[2]==Fraction(2,5))
    counts = tuple((x+1)**2 for x in range(M+1))
    start_den = sum(counts)
    steps = word.count("B")
    den = start_den * guard[0]**steps
    probability = [Fraction(w,start_den) for w in counts]
    peak = max(w.numerator.bit_length() for w in probability)
    for op in word:
        nx = [Fraction(0) for x in range(M+1)]
        for x, w in enumerate(probability):
            p = Fraction(guard[1][x],guard[0]) if op=="B" else Fraction(int(op=="A"))
            nx[min(M,x+1)] += p*w
            nx[M-x] += (1-p)*w
        probability = nx
        peak = max(peak,*(w.numerator.bit_length() for w in probability))
    moments = [sum(w*x**j for x,w in enumerate(probability)) for j in range(3)]
    for j, w in enumerate(moments):
        read = powers(M,j)
        for op in reversed(word):
            read = lift_actual(read,op,guard)
        assert w == Fraction(pairing(read,counts),start_den)
        assert den % w.denominator == 0 and w.numerator <= M**j*den
    return {"M":M,"physical_word":word,"random_steps":steps,"guard":guard_name,
            "one_step_common_denominator":guard[0],"initial_denominator":start_den,
            "full_path_common_denominator":den,"exact_moments":list(map(str,moments)),
            "largest_forward_mass_numerator_bits":peak,
            "output_numerator_bit_bound":(M*M*den).bit_length()}


def run():
    settings_cases = 0
    blind_examples = []
    # Original deterministic and genuinely random pullback have the same rank.
    for M in range(2,25):
        guard = pack([Fraction(x,M) for x in range(M+1)])
        base = echelon([powers(M,d) for d in range(3)])
        for T in range(9):
            words = settings(M,T)
            r = 3 if T == 0 else min(M+1,2*T+2)
            assert len(words) == r//2 and max(map(len, words)) <= T
            transported = [row for w in words for row in setting_rows(M,w)]
            obs = echelon(transported)
            assert len(obs) == len(base) == r
            assert all(not insert(dict(obs),v) for v in base.values())
            if (M,T) in [(4,2),(8,3),(11,5),(14,7)]:
                blind_examples.append({"M":M,"T":T,"settings":words,"rank":r,
                                       "setting_deletions":original_setting_deletions(M,T,words)})
            settings_cases += 1
            base = advance(base,"ARB",guard)
    ranks = 0
    quadratic_one_step_covers = 0
    boundary = {}
    census = 0
    for M in range(2,22):
        for name, coeff, endpoint, guard in samples(M):
            computed = echelon(powers(M,d) for d in range(3))
            if M >= 4:
                first = [powers(M,d) for d in (1,2)]
                jointly = [powers(M,0)]
                jointly.extend(first if endpoint else [lifted(f,"A",guard) for f in first])
                jointly.extend(lifted(f,"B",guard) for f in first)
                assert len(echelon(jointly)) == 5
                quadratic_one_step_covers += 1
            for T in range(7):
                formula_rows = [f for _,f in proposed_rows(M,T,coeff)]
                expected = quadratic_rank(M,T,coeff)
                assert len(computed) == len(echelon(formula_rows)) == expected
                assert all(not insert(dict(computed),f) for f in formula_rows)
                if T >= 2 and M == 4*T-1 and endpoint == Fraction(2,5):
                    boundary.setdefault(str(M), {})[name] = len(computed)
                ranks += 1
                computed = advance(computed,"ARB",guard)
            if M in [4,7,11,15] and endpoint==Fraction(2,5):
                rows = {0:powers(M,0)}
                for T, layer in enumerate(word_layers(M,4,guard)):
                    for pair in layer.values():
                        for row in pair:
                            insert(rows,integers(row))
                        census += 1
                    assert len(rows) == quadratic_rank(M,T,coeff)
    examples = [certificate(7,2,"square"),certificate(7,2,"balanced"),
                certificate(11,3,"balanced")]
    for group in examples[1:]:
        m,t = group["M"],group["T"]
        late = group["horizon_ambiguities_then_separated"]
        assert len(late)==1 and len(late[0]["first_separating_word"])==t+1
        assert late[0]["integer_contrast"]==tuple(
            (-1)**(j-(t-1))*comb(2*t,j-t+1) if t-1<=j<=3*t-1 else 0
            for j in range(m+1))
    return {
        "protocol":"Exact expectation readout on repeated preparations of one finite input law. Each chronological word returns the total and the first two moments.",
        "original":{"M_inclusive":[2,24],"T_inclusive":[0,8],
                    "matched_lower_bound_cases":settings_cases,
                    "small_covers":blind_examples,
                    "two_new_clipped_columns":[[-1,-2],["-(2M+1)","-(4M+4)"]],
                    "two_by_two_determinant":2},
        "quadratic":{"M_inclusive":[2,21],"T_inclusive":[0,6],
                     "laws":["square","reversed","balanced","balanced_concave","affine_tilt"],
                     "p_M":["0","2/5","1"],"exact_span_comparisons":ranks,
                     "M_at_least_four_sharp_two_setting_one_step_checks":quadratic_one_step_covers,
                     "fully_enumerated_words_cumulative_across_fixtures":census,
                     "enumerated_M":[4,7,11,15],"full_word_max_length":4,
                     "rank_at_M_equals_4T_minus_1":boundary},
        "deletion_certificates":examples, "forward_and_bit_check":bit_budget_witness()
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    encoded = json.dumps(run(), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
