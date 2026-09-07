"""Independent bounded adapter checks; does not run legacy m3 or author ensembles."""

from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'experiments/owner_pp_finite_brc_20260907'))
import finite_hcm_brc as adapter


def expected_histogram(weights):
    counts = Counter(weight for weight in weights if weight > 0)
    return tuple(sorted(counts.items()))


def main():
    # Repeated weights in different j-layers and omitted zero-weight words matter.
    betas = [(F(0),), (F(7, 3),), (F(1, 2), F(0), F(1, 2), F(2, 3))]
    cylinders = coefficients = 0
    records = []
    for beta in betas:
        d = len(beta) - 1
        words = [(word, beta[sum(word)]) for word in product((0, 1), repeat=d)]
        h = tuple(sum((mass for word, mass in words if all(word[i] for i in range(a))), F(0))
                  for a in range(d + 1))
        certificate = adapter.build_certificate(h)
        assert adapter.verify_certificate(h, certificate)['valid']
        assert tuple(F(x) for x in certificate['beta']) == beta
        full = adapter.prefix_observation_histogram(h, 0, 0)
        assert full.entries == expected_histogram(mass for _, mass in words)
        # Every disjoint pair of labelled fixed-position sets, not only a prefix.
        for constraints in product((-1, 0, 1), repeat=d):
            kept = [mass for word, mass in words
                    if all(fixed == -1 or word[i] == fixed for i, fixed in enumerate(constraints))]
            r, k = constraints.count(1), constraints.count(0)
            actual = adapter.prefix_observation_histogram(h, r, k)
            assert actual.entries == expected_histogram(kept)
            assert actual.total_mass == sum(kept, F(0))
            cylinders += 1
        for k in range(d + 1):
            pairs = [(word, marks, mass) for word, mass in words
                     for marks in combinations([i for i, value in enumerate(word) if value == 0], k)]
            actual = adapter.coefficient_histogram(h, k)
            assert actual.entries == expected_histogram(mass for _, _, mass in pairs)
            assert actual.total_mass == sum((mass for _, _, mass in pairs), F(0))
            coefficients += 1
        records.append({'d':d, 'beta':[str(v) for v in beta], 'h':[str(v) for v in h],
                        'full_histogram':adapter.histogram_record(full)})

    h = (F(1), F(1, 2), F(1, 5))
    good = adapter.build_certificate(h)
    mutations = []
    def changed(label, fn, sequence=h, baseline=good):
        certificate = deepcopy(baseline)
        fn(certificate)
        result = adapter.verify_certificate(sequence, certificate)
        assert result['status'] == 'INVALID_CERTIFICATE' and not result['valid'], (label, result)
        mutations.append(label)

    changed('bool_layer_index', lambda c: c['layers'][0].update(j=False))
    changed('float_word_count', lambda c: c['layers'][0].update(word_count=1.0))
    changed('fraction_word_count', lambda c: c['layers'][0].update(word_count=F(1)))
    changed('float_histogram_count', lambda c: c['histogram'].update(branch_count=4.0))
    changed('bool_histogram_entry_count', lambda c: c['histogram']['entries'][0].update(count=True))
    changed('zero_denominator', lambda c: c['beta'].__setitem__(0, '1/0'))
    changed('noncanonical_fraction', lambda c: c['beta'].__setitem__(0, '2/10'))
    changed('wrong_beta', lambda c: c['beta'].__setitem__(0, '0/1'))
    changed('group_mass_in_place_of_per_word', lambda c: c['layers'][1].update(per_word_mass='3/5'))
    changed('erase_histogram_multiplicity', lambda c: c['histogram']['entries'][0].update(count=1))
    changed('wrong_original_h', lambda c: None, sequence=(F(2), F(1, 2), F(1, 5)))
    changed('forged_power_measure_realized', lambda c: c.update(power_moment_measure='EXISTS'))
    obstructed_h = (1, 1, 0)
    obstructed = adapter.build_certificate(obstructed_h)
    changed('forged_power_measure_obstructed', lambda c: c.update(power_moment_measure='EXISTS'),
            sequence=obstructed_h, baseline=obstructed)
    changed('bool_obstruction_index', lambda c: c['obstruction'].update(r=False),
            sequence=obstructed_h, baseline=obstructed)
    changed('extra_nested_field', lambda c: c['layers'][0].update(measure='EXISTS'))
    changed('overlong_beta', lambda c: c.update(beta=['0/1'] * 4))

    yielded = []
    def vector():
        for value in good['beta']:
            yielded.append(value)
            yield value
    changed('generator_beta_rejected_before_iteration', lambda c: c.update(beta=vector()))
    assert yielded == []

    budget_cases = []
    for label, certificate, degree in [('degree_budget', good, 1),
        ('scalar_budget', dict(good, scope='x' * 100001), 256),
        ('node_budget', dict(good, layers=[list(range(20001))]), 256)]:
        result = adapter.verify_certificate(h, certificate, max_degree=degree)
        assert result['status'] == 'UNVERIFIED' and not result['valid'], (label, result)
        budget_cases.append(label)
    # This was a mathematically valid d=0 certificate misclassified as INVALID
    # when Python's decimal conversion ceiling preceded any declared bit budget.
    huge_h = (10 ** 4500,)
    huge_text = '1' + '0' * 4500 + '/1'
    huge_certificate = {'schema':adapter.SCHEMA, 'scope':adapter.SCOPE,
        'status':'REALIZED', 'degree':0, 'input_h':[huge_text], 'beta':[huge_text],
        'layers':[{'j':0, 'word_count':1, 'per_word_mass':huge_text, 'total_layer_mass':huge_text}],
        'histogram':{'entries':[{'weight':huge_text, 'count':1}], 'branch_count':1,
                     'total_mass':huge_text}, 'power_moment_measure':'UNCLASSIFIED'}
    assert adapter.verify_certificate(huge_h, huge_certificate)['status'] == 'UNVERIFIED'
    try:
        adapter.build_certificate(huge_h)
    except adapter.ResourceLimit:
        pass
    else:
        raise AssertionError('large exact input did not report its resource limit')
    beta_limit = deepcopy(good)
    beta_limit['beta'][0] = huge_text
    assert adapter.verify_certificate(h, beta_limit)['status'] == 'UNVERIFIED'
    budget_cases += ['valid_large_rational_unverified', 'large_input_build_resource_limit',
                     'large_certificate_rational_unverified']
    exact_type_rejections = 0
    for data in [(1, True, 0), (1, 0.5, 0), ['1/1'], [], iter([1])]:
        try:
            adapter.build_certificate(data)
        except (TypeError, ValueError):
            exact_type_rejections += 1
        else:
            raise AssertionError('nonexact or invalid input accepted')
    assert adapter.verify_square_obstruction(h, (F(-1, 2), F(1)))['square_readout'] == '-1/20'
    assert adapter.verify_square_obstruction((1, 0, 0), (0, 1))['status'] == 'UNDETERMINED'
    # A nonsymmetric prefix observer has a different contract: word 10 gives
    # h=(1,1,0), while no exchangeable word law has these symmetric observations.
    word = (1, 0)
    assert tuple(int(all(word[:a])) for a in range(3)) == obstructed_h
    assert adapter.verify_certificate(obstructed_h, obstructed)['status'] == 'OBSTRUCTED'
    assert 'EXCHANGEABLE' in adapter.SCOPE and 'SYMMETRIC_FACTORIAL' in adapter.SCOPE

    author = json.loads((ROOT / 'experiments/owner_pp_finite_brc_20260907/finite_brc_certificate_20260907.json').read_text())
    historical = json.loads((ROOT / 'experiments/owner_pp_finite_moment_audit_20260907.json').read_text())
    # Bind the already audited m3 data; never rerun either legacy source route.
    assert author['actual_m3']['normalized_h'] == author['actual_m3']['brc_certificate']['input_h']
    supplied_h = tuple(F(v) for v in author['actual_m3']['normalized_h'])
    assert supplied_h == tuple(F(v) for v in historical['model_binding']['h_normalized'])
    assert tuple(F(v) for v in author['actual_m3']['q']) == tuple(
        F(v) for v in historical['model_binding']['q_coefficients'])
    assert F(author['actual_m3']['square_obstruction']['square_readout']) == F(
        historical['positive_power_moment_obstruction']['normalized_L_h_p_squared'])
    assert adapter.verify_certificate(supplied_h, author['actual_m3']['brc_certificate'])['valid']

    source = Path(adapter.__file__)
    output = {'status':'PASS', 'local_ensembles':len(betas), 'all_labelled_cylinder_checks':cylinders,
              'marked_word_coefficient_checks':coefficients, 'invalid_certificates_rejected':mutations,
              'resource_semantics_checked':budget_cases, 'exact_input_rejections':exact_type_rejections,
              'generator_items_consumed':len(yielded), 'local_ensembles_data':records,
              'source_sha256':{str(source.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(source.read_bytes()).hexdigest(),
                   str(Path(__file__).relative_to(ROOT)).replace('\\','/'):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'existing_m3_certificate_verified_against_supplied_h':True,
              'historical_m3_h_q_negative_square_agree_without_recomputation':True,
              'scope':'adapter and local finite identities; no legacy m3 source runs or author 63-ensemble rerun'}
    destination = ROOT / 'experiments/owner_pp_brc_consumer_audit_20260907.json'
    destination.write_text(json.dumps(output, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k:output[k] for k in ('status','local_ensembles','all_labelled_cylinder_checks',
                                          'marked_word_coefficient_checks','generator_items_consumed')}))


if __name__ == '__main__':
    main()
