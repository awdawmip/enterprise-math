"""Q4 construction-only operator extension of frozen Source-covered q3 math.

No import-time input, native operation or feasibility execution. Self checks are
construction evidence, not genuine independent review. New static descriptor
validation and canonical first-six particular; exact input ordering is fixed.
"""
from fractions import Fraction
from pathlib import Path
from itertools import combinations_with_replacement, product
from collections import Counter
import hashlib,json
P,N,LIMIT,LOWER=17,16,2331,16901460
COMMON_SHA="7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce"
INPUT_SHA="62dc2e5b6a3fceb129c25a0c19fc27dbe6ac195c6cdedecde7cfb1639789e16a"
INPUT_BYTES=13084243
class InvariantError(RuntimeError): pass
def require(condition, message):
    if not condition:
        raise InvariantError(message)

def nofloat(_value):
    raise InvariantError("Floating or nonfinite JSON is forbidden")

def integer(value):
    require(type(value) is str and bool(value)
            and (value.isdecimal() or (value[0] == "-" and value[1:].isdecimal())),
            "Expected decimal-string scientific integer")
    return int(value)

def rat(value):
    require(type(value) is list and len(value) == 2, "Malformed rational pair")
    numerator, denominator = map(integer, value)
    require(denominator > 0, "Nonpositive rational denominator")
    return Fraction(numerator, denominator)

def pair(value):
    value = Fraction(value)
    return [str(value.numerator), str(value.denominator)]

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result

def read(path, sha=None):
    raw = Path(path).read_bytes()
    require(sha is None or digest(raw) == sha, "Input or evidence SHA256 mismatch: " + str(path))
    return json.loads(raw, parse_float=nofloat, parse_constant=nofloat,
                      object_pairs_hook=unique_object)

def dot(left, right):
    require(len(left) == len(right), "Vector dimension mismatch")
    return sum((x * y for x, y in zip(left, right)), Fraction(0))

def det(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    require(n > 0 and all(len(row) == n for row in a), "Determinant dimensions")
    previous, sign = 1, 1
    for k in range(n - 1):
        pivot = next((j for j in range(k, n) if a[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                q, r = divmod(value * a[i][j] - a[i][k] * a[k][j], previous)
                require(r == 0, "Nonexact Bareiss division")
                a[i][j] = q
            a[i][k] = 0
        previous = value
    return sign * a[-1][-1]

def modular_solve(matrix, rhs, modulus):
    n = len(matrix)
    require(len(rhs) == n and all(len(row) == n for row in matrix), "Modular dimensions")
    a = [[x % modulus for x in row] + [rhs[i] % modulus]
         for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k] % P != 0), None)
        require(pivot is not None, "Missing unit modular pivot")
        a[k], a[pivot] = a[pivot], a[k]
        inverse = pow(a[k][k], -1, modulus)
        a[k] = [(x * inverse) % modulus for x in a[k]]
        for i in range(n):
            if i != k:
                multiplier = a[i][k]
                a[i] = [(x - multiplier * y) % modulus for x, y in zip(a[i], a[k])]
    result = [a[i][-1] for i in range(n)]
    require(all((sum(x * y for x, y in zip(row, result)) - target) % modulus == 0
                for row, target in zip(matrix, rhs)), "Modular solve invariant")
    return result

def factors(value):
    answer, trial = [], 2
    while trial * trial <= value:
        if value % trial == 0:
            while value % trial == 0:
                answer.append(trial)
                value //= trial
        trial += 1
    if value > 1:
        answer.append(value)
    return answer


def partitions(total, minimum=1):
    if total == 0:
        yield ()
    for q in range(minimum, total + 1):
        for tail in partitions(total - q, q):
            yield (q,) + tail


def ordered_descriptors():
    """Compose the published fixed ordering, retaining all exact multiplicities."""
    for partition in partitions(4):
        groups = [list(combinations_with_replacement([(q, r) for r in range(1, 17)], count))
                  for q, count in sorted(Counter(partition).items())]
        for selected in product(*groups):
            counts = Counter(atom for group in selected for atom in group)
            support = sorted(counts)
            for tail in product((1, -1), repeat=len(support)-1):
                plus, minus = [], []
                for atom, sign in zip(support, (1,) + tail):
                    (plus if sign == 1 else minus).extend([atom] * counts[atom])
                yield partition, plus, minus


def load_inputs(common_path, ordered_path):
    require(digest(Path(common_path).read_bytes()) == COMMON_SHA, 'Common whole-byte SHA mismatch')
    raw = Path(ordered_path).read_bytes()
    require(len(raw) == INPUT_BYTES and digest(raw) == INPUT_SHA, 'Ordered whole input mismatch')
    return read(common_path, COMMON_SHA), read(ordered_path, INPUT_SHA)


def validate_static_input(problem):
    """No affine representative or feasibility search; exact descriptor arithmetic only."""
    require(problem['schema'] == 'T6_P17_TOTAL_ORDER4_LITERAL_FULL30992_FIXED_INPUT_V1'
            and problem['scientific_feasibility_executed'] is False
            and problem['classifier_result_asserted'] is False, 'Not the frozen q4 descriptor input')
    require(problem['scope']['total_vertical_order'] == 4
            and problem['scope']['all_literal_outside_systems_require_classification'] is True,
            'Literal outsiders are mandatory')
    coefficients = [[pow(j, -k, 17**k) for j in range(1,17)] for k in range(1,7)]
    atom_map = {}
    require(len(problem['atom_data']) == 64, 'Atom table length')
    for row, (q,r) in zip(problem['atom_data'], product(range(1,5), range(1,17))):
        cofactor = 17*q+r
        expected = {'q':q,'r':r,'cofactor':cofactor,'denominator':17*cofactor,
                    'exponent_mass':17*cofactor-1,'prime_factors':factors(cofactor),
                    'reciprocal_moments':[str(pow(cofactor,-k,17**k)) for k in range(1,7)]}
        require(row == expected, 'Exact atom data mismatch')
        atom_map[(q,r)] = expected
    cases, domains, masks, partition_counts = [], Counter(), Counter(), Counter()
    descriptors = iter(ordered_descriptors())
    require(len(problem['cases']) == 30992, 'Complete30992 ordered cases required')
    for i, raw in enumerate(problem['cases']):
        expected = next(descriptors, None)
        require(expected is not None, 'Unexpected extra descriptor')
        partition, plus, minus = expected
        costs = [sum(atom_map[a]['exponent_mass'] for a in side) for side in (plus,minus)]
        budgets = [LIMIT-x for x in costs]
        require(min(budgets) >= 0, 'Negative signed budget')
        targets = [(-sum(int(atom_map[a]['reciprocal_moments'][k-1]) for a in plus)
                    +sum(int(atom_map[a]['reciprocal_moments'][k-1]) for a in minus)) % 17**k
                   for k in range(1,7)]
        radius = sum(x*x for x in budgets)
        domain = 'ADMISSIBLE' if all(max(atom_map[a]['prime_factors']) <= 17 for a in plus+minus) else 'OUTSIDE_DOMAIN'
        quarter = 4*radius < LOWER
        expected_row = {'case_index':i,'case_id':f'q4-literal-{i+1:05}',
                        'positive_atoms':[list(a) for a in plus], 'negative_atoms':[list(a) for a in minus],
                        'order_partition':list(partition),'maximal_p17_domain':domain,
                        'fixed_vertical_side_costs':list(map(str,costs)), 'q0_side_budgets':list(map(str,budgets)),
                        'mixed_rhs':list(map(str,targets)), 'radius_squared':str(radius),
                        'strict_conservative_quarter_mask':quarter,
                        'conditional_coordinate_choice_ceiling':32 if quarter else 272}
        require(raw == expected_row, 'Frozen descriptor/target/budget/domain/order mismatch')
        require(quarter or 2*radius < LOWER, 'Ordinary strict radius bound unavailable')
        cases.append({'index':i,'id':expected_row['case_id'],'positive_atoms':plus,'negative_atoms':minus,
                      'budgets':budgets,'targets':targets,'radius':radius,'domain':domain,
                      'quarter':quarter,'action_bound':32 if quarter else 272})
        domains[domain]+=1; masks[quarter]+=1; partition_counts[partition]+=1
    require(next(descriptors,None) is None, 'Missing ordered descriptor')
    require(domains == {'ADMISSIBLE':10212,'OUTSIDE_DOMAIN':20780}
            and masks == {True:4724,False:26268}, 'Population or conservative mask count mismatch')
    require(partition_counts == {(1,1,1,1):22016,(1,1,2):8192,(1,3):512,(2,2):256,(4,):16},
            'Complete signed-multiplicity coverage mismatch')
    require(sum(c['action_bound'] for c in cases)==7296064, 'Full conditional action ceiling mismatch')
    require((min(c['radius'] for c in cases),max(c['radius'] for c in cases))==(3016546,6776842),
            'Radius extrema mismatch')
    return cases


def establish_operator(portable):
    """Exact common kernel/Gram/inverse construction, without any particular case."""
    weights=[17*j-1 for j in range(1,17)]
    require(list(map(integer,portable['weights']))==weights, 'Exact weight/coordinate order')
    U=[[integer(x) for x in row] for row in portable['unweighted_basis']]
    B=[[integer(x) for x in row] for row in portable['weighted_basis']]
    require(len(U)==len(B)==16 and all(len(row)==16 for row in U+B), 'Basis dimensions')
    require(B==[[w*x for w,x in zip(weights,row)] for row in U], 'Weighted kernel scaling')
    coeff=[[pow(j,-k,17**k) for j in range(1,17)] for k in range(1,7)]
    require(abs(det(U))==17**21, 'Full mixed-kernel determinant/index')
    require(det([row[:6] for row in coeff])%17 !=0, 'Surjective mixed map unit minor')
    require(all(sum(x*a for x,a in zip(row,coeff[k]))%17**(k+1)==0 for row in U for k in range(6)),
            'Every basis row must satisfy all six mixed congruences')
    D=list(map(rat,portable['gram_schmidt_squared']))
    mu=[[rat(x) for x in row] for row in portable['mu']]
    require(len(D)==len(mu)==16 and all(len(row)==16 for row in mu), 'GS dimensions')
    require(all(D[i]>LOWER and mu[i][i]==1 and all(mu[i][j]==0 for j in range(i+1,16))
                for i in range(16)), 'Exact GS positivity/lower/triangular rules')
    require(all(dot(B[i],B[j])==sum((mu[i][k]*mu[j][k]*D[k] for k in range(16)),Fraction(0))
                for i in range(16) for j in range(16)), 'Exact weighted Gram identity')
    star=[]
    for i,row in enumerate(B):
        star.append([Fraction(row[c])-sum(mu[i][j]*star[j][c] for j in range(i)) for c in range(16)])
        require(dot(star[i],star[i])==D[i], 'GS orthogonal norm identity')
    A=[row[:6] for row in coeff];M=17**6
    inverse_columns=[modular_solve(A,[int(i==j) for i in range(6)],M) for j in range(6)]
    inverse=[[inverse_columns[j][i] for j in range(6)] for i in range(6)]
    require(all(sum(A[i][k]*inverse[k][j] for k in range(6))%M==int(i==j)
                for i in range(6) for j in range(6)), 'Canonical exact A inverse identity')
    # Only first six particular entries vary; all centers are reconstructed exactly.
    linear=[[Fraction(weights[j])*star[i][j]/D[i] for j in range(6)] for i in range(16)]
    return {'weights':weights,'U':U,'B':B,'coeff':coeff,'D':D,'mu':mu,'star':star,
            'A':A,'inverse':inverse,'center_linear':linear}


def canonical_particular(operator, case):
    M=17**6;half=M//2
    y=[sum(x*t for x,t in zip(row,case['targets']))%M for row in operator['inverse']]
    a=[(x+half)%M-half for x in y]+[0]*10
    require(all(sum(x*c for x,c in zip(a,row))%17**k==target
                for k,(row,target) in enumerate(zip(operator['coeff'],case['targets']),1)),
            'Canonical particular six original congruences')
    return a
