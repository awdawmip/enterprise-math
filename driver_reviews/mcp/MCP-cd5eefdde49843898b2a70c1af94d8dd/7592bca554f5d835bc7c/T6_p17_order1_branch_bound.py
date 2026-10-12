"""Paper-only weighted farther-choice bound; not an affine search or census.

Reads the previously independently verified p17 GS norms and performs only
small rational budget/subset comparisons. No affine representative, lattice
point, author checker, LLL proposal, or native identity is constructed.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import itertools
import json

HERE = Path(__file__).resolve().parent
CERT = HERE / 'source-inputs/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json'
EXPECTED = 'fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6'


def main():
    raw = CERT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    certificate = json.loads(raw)
    norms = [Fraction(*pair) for pair in certificate['gram_schmidt_squared']]
    assert len(norms) == 16
    minimum = min(norms)
    maximum_R2 = 2026**2 + 2331**2
    assert minimum > maximum_R2
    assert 3 * minimum > 4 * maximum_R2
    classes = []
    for r in range(1, 17):
        atom_cost = 289 + 17*r - 1
        positive_budget = 2331 - atom_cost
        negative_budget = 2331
        R2 = positive_budget**2 + negative_budget**2
        singletons = [i for i, norm in enumerate(norms) if norm <= 4 * R2]
        pairs = [list(pair) for pair in itertools.combinations(range(16), 2)
                 if sum((norms[i] for i in pair), Fraction()) <= 4 * R2]
        assert all(norm > R2 for norm in norms)
        assert sum(sorted(norms)[:3]) > 4 * R2
        prefix_counts = []
        for depth in range(17):
            visited_indices = set(range(16-depth, 16))
            count = 1 + sum(i in visited_indices for i in singletons)
            count += sum(set(pair) <= visited_indices for pair in pairs)
            prefix_counts.append(count)
        leaf_bound = 1 + len(singletons) + len(pairs)
        assert prefix_counts[-1] == leaf_bound
        cofactor = 17 + r
        prime_factors = [p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
                         if cofactor % p == 0]
        admissible = all(p <= 17 for p in prime_factors)
        classes.append({'r': r, 'atom_cost': atom_cost,
                        'cofactor': cofactor, 'cofactor_prime_divisors': prime_factors,
                        'maximal_prime17_membership': admissible,
                        'outside_domain_is_not_relaxed_class_emptiness': not admissible,
                        'positive_q0_budget': positive_budget,
                        'negative_q0_budget': negative_budget, 'R2': R2,
                        'uniform_137_leaf_bound': 137,
                        'weighted_farther_choice_singletons': singletons,
                        'weighted_farther_choice_pairs': pairs,
                        'weighted_leaf_bound': leaf_bound,
                        'weighted_prefix_node_bounds': prefix_counts,
                        'weighted_total_node_bound': sum(prefix_counts)})
    result = {
        'schema': 'T6_P17_ORDER1_PAPER_FARTHER_CHOICE_BOUND_V1',
        'status': 'EXACT_SMALL_COMPARISONS_PASS_NOT_A_CENSUS',
        'certificate_sha256': EXPECTED,
        'minimum_D': [minimum.numerator, minimum.denominator],
        'minimum_D_floor': minimum.numerator // minimum.denominator,
        'max_R2': maximum_R2,
        'all_D_strictly_above_max_R2': True,
        'three_minimum_D_strictly_above_four_max_R2': True,
        'maximum_farther_choices_per_feasible_path': 2,
        'uniform_total_leaf_bound': 16 * 137,
        'weighted_total_leaf_bound': sum(row['weighted_leaf_bound'] for row in classes),
        'weighted_total_node_bound': sum(row['weighted_total_node_bound'] for row in classes),
        'actual_maximal_prime17_admissible_residues': [row['r'] for row in classes if row['maximal_prime17_membership']],
        'outside_maximal_prime17_residues': [row['r'] for row in classes if not row['maximal_prime17_membership']],
        'actual_maximal_prime17_weighted_total_leaf_bound': sum(row['weighted_leaf_bound'] for row in classes if row['maximal_prime17_membership']),
        'actual_maximal_prime17_weighted_total_node_bound': sum(row['weighted_total_node_bound'] for row in classes if row['maximal_prime17_membership']),
        'zero_based_descending_gs_indices': True,
        'norms': [[norm.numerator, norm.denominator] for norm in norms],
        'norm_floors': [norm.numerator // norm.denominator for norm in norms],
        'classes': classes,
        'proof_dependency': 'At each descending GS coordinate choose a deterministic nearest integer, smaller integer at exact ties. The other floor/ceiling integer is at distance >=1/2. Its squared contribution is >=D_i/4. Each farther-choice index set determines at most one complete path.',
        'not_proved': ['any class is empty', 'any modular kernel exists',
                       'a full p17 collision', 'p17 higher orders', 'global T6=2332'],
        'affine_representatives_or_lattice_points_constructed': False,
        'author_checkers_read_imported_or_executed': False,
        'native_claim_result_or_source_write': False,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE / 'P17_ORDER1_BRANCH_BOUND_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'],
                      'uniform_leaves': result['uniform_total_leaf_bound'],
                      'weighted_leaves': result['weighted_total_leaf_bound'],
                      'weighted_nodes': result['weighted_total_node_bound'],
                      'actual_p17_leaves': result['actual_maximal_prime17_weighted_total_leaf_bound'],
                      'actual_p17_nodes': result['actual_maximal_prime17_weighted_total_node_bound'],
                      'per_class_leaves': [row['weighted_leaf_bound'] for row in classes]}))


if __name__ == '__main__':
    main()
