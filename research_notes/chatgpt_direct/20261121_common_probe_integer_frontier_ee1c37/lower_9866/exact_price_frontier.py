"""Exact necessary cost spectra, retaining the full embedded/proper class type.

The dependencies provide the full single-class catalogue, centre-defect bounds,
mother-union bounds, and E=2 lower bound. This enumerates price combinations;
it does not infer existence from a surviving combination.
"""
import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cost', type=int, default=9866)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mother-proof', type=Path, default=HERE.parent/'integer_cuts/mother12')
    parser.add_argument('--defect-catalog', type=Path,
                        default=HERE.parent/'mother_sublevels_D/cost_defect_catalog.json')
    args = parser.parse_args()
    MOTHER = args.mother_proof.resolve()
    DEFECT = args.defect_catalog.resolve()
    spec = importlib.util.spec_from_file_location('mother_plan', MOTHER / 'plan.py')
    plan = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plan)
    data = plan.catalogue()
    minima = {key: min(value) for key, value in data.items()}
    size_rows = plan.make_rows(args.cost, minima)
    delta = {(row['size'], row['cost']): row['maximum_defect_upper_bound']
             for row in json.loads(DEFECT.read_text())['rows']}
    constants = {8: 419, 9: 557, 10: 744, 11: 993, 12: 1226}
    size_summary = []
    surviving = []
    eliminated = Counter()
    total_prices = 0
    for row in size_rows:
        e = row['embedded_count']
        key = (tuple(row['embedded_sizes']), tuple(row['proper_sizes']))
        if not row['unrestricted_union_bound_passes']:
            eliminated['size_mother_union'] += 1
            continue
        if e == 2 and args.cost < 9867:
            eliminated['size_E2_lower_bound_9867'] += 1
            continue
        slots = [(s, 1) for s in row['embedded_sizes']] + [(s, 0) for s in row['proper_sizes']]
        base = sum(minima[slot] for slot in slots)
        required = 3 * max(5 - e, 0)
        counts = Counter()
        kept = []

        def prices(at, left, defect, chosen):
            nonlocal total_prices
            if at == len(slots):
                if left:
                    return
                total_prices += 1
                counts['all'] += 1
                if defect < required:
                    counts['centre_defect'] += 1
                    return
                typed = Counter(chosen)
                cores = sum(n for (s, embed, c), n in typed.items()
                            if (s, c) in ((12, 1104), (13, 1296)))
                if cores >= 3 and args.cost < {3: 9881, 4: 9871}.get(cores, 9996):
                    counts['inherited_core_bound'] += 1
                    return
                combined = Counter()
                for (s, embed, c), n in typed.items():
                    combined[s, c] += n
                tag = '_'.join(f'{s}-{c}-{n}' for (s, c), n in sorted(combined.items()))
                rec = {'tag': tag, 'embedded_count': e, 'core_count': cores,
                       'maximum_proper_defect': defect, 'required_proper_defect': required,
                       'types': [{'size': s, 'embedded': embed, 'cost': c, 'count': n}
                                 for (s, embed, c), n in sorted(typed.items())]}
                kept.append(rec)
                surviving.append(rec)
                return
            s, embed = slot = slots[at]
            minimum_price = chosen[-1][2] if at and slots[at-1] == slot else -1
            for c in sorted(data[slot]):
                extra = c - minima[slot]
                if c < minimum_price or extra > left:
                    continue
                if embed:
                    extra_defect = 0
                elif (s, c) in delta:
                    extra_defect = delta[s, c]
                else:
                    extra_defect = min(3 * (s-2), (c-constants[s]) // 3)
                prices(at+1, left-extra, defect+extra_defect, chosen+[(s, embed, c)])

        prices(0, args.cost-base, 0, [])
        size_summary.append({'embedded_sizes': key[0], 'proper_sizes': key[1],
                             'embedded_count': e, 'minimum_cost': base, 'counts': dict(counts),
                             'surviving_typed_patterns': len(kept)})
    result = {'cost': args.cost, 'size_profiles': len(size_rows),
              'size_level_exclusions': dict(eliminated), 'total_exact_price_patterns': total_prices,
              'surviving_typed_patterns': len(surviving),
              'surviving_untyped_tags': len({row['tag'] for row in surviving}),
              'surviving_by_embedded_count': dict(Counter(row['embedded_count'] for row in surviving)),
              'size_summary': size_summary, 'survivors': surviving,
              'dependencies': [{'path': str(p), 'sha256': sha256(p.read_bytes()).hexdigest()}
                               for p in [MOTHER/'plan.py', MOTHER/'catalog.txt', DEFECT]],
              'status': 'NECESSARY_CONDITIONS_ONLY_NO_COVERAGE_SEARCH'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('size_summary', 'survivors', 'dependencies')}))


if __name__ == '__main__':
    main()
