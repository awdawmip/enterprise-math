"""Portable replay of the mixed cost bound and four COMPLETED E=2 profiles.

Ten further E=2 size profiles remain pending in this snapshot. The replay
checks exact frame completeness, frozen native inputs, the original observer,
and every actual completed search receipt. It does not run the pending cases.
"""
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, required=True)
    parser.add_argument('--seeds', type=Path, required=True)
    parser.add_argument('--mother-proof', type=Path, default=HERE.parents[1])
    parser.add_argument('--work', type=Path, required=True)
    args = parser.parse_args()
    work = args.work.resolve(); work.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((HERE/'package_manifest.json').read_text())
    for entry in manifest['files']:
        b = (HERE/entry['path']).read_bytes()
        assert len(b) == entry['bytes'] and sha256(b).hexdigest() == entry['sha256']
    mother_manifest = json.loads((args.mother_proof/'package_manifest.json').read_text())
    for entry in mother_manifest['files']:
        b = (args.mother_proof/entry['path']).read_bytes()
        assert len(b) == entry['bytes'] and sha256(b).hexdigest() == entry['sha256']
    mother_plan = json.loads((args.mother_proof/'plan_9995.json').read_text())
    selected = json.loads((HERE/'selected_profiles.json').read_text())
    normalize = lambda x: json.dumps(x, sort_keys=True)
    assert {normalize(r) for r in selected['rows']} == {
        normalize(r) for r in mother_plan['profiles'] if r['embedded_count'] == 2}
    assert len(selected['rows']) == 14
    subprocess.run([sys.executable, '-B', HERE/'verify_mixed_bound.py',
                    '--previous', args.previous, '--seeds', args.seeds,
                    '--parents', HERE/'inputs/parent', '--proper11-bank', HERE/'inputs/B11',
                    '--proper12-bank', HERE/'inputs/B12', '--output', work/'mixed_bound.json'], check=True)
    assert json.loads((work/'mixed_bound.json').read_text()) == json.loads((HERE/'mixed_bound_verification.json').read_text())
    spec = importlib.util.spec_from_file_location('bundle_native_observer', args.previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    bad, pair = native.observation_tables()
    observation = (HERE/'inputs/obs').read_bytes()
    assert len(observation) == 641000
    expected_pairs = b''.join(pair[i][j].to_bytes(32, 'little') for i in range(125) for j in range(125))
    assert observation[:500000] == expected_pairs
    triples = {tuple(observation[i:i+3]) for i in range(500000, len(observation), 3)}
    expected_triples = {(i, j, k) for i in range(125) for j in range(i+1, 125)
                        for k in range(j+1, 125) if bad[i][j] >> k & 1}
    assert triples == expected_triples and len(triples) == 47000
    parents = [int(line.split()[0])+(int(line.split()[1]) << 64) for line in (HERE/'inputs/parent').read_text().splitlines()[:250]]
    assert len(set(parents)) == 250
    classes = []
    for line in (HERE/'positive_construct.txt').read_text().splitlines():
        s, c, *ids = map(int, line.split()); mask = sum(1 << i for i in ids)
        assert native.native_class(mask, bad, pair) == (s, c)
        classes.append((s, c, mask, any(mask & ~m == 0 for m in parents)))
    assert len(classes) == 12 and sum(c for s, c, m, e in classes) == 9996
    occupied = 0
    for s, c, m, e in classes:
        assert not occupied & m; occupied |= m
    assert occupied == (1 << 125)-1
    assert [(s, c) for s, c, m, e in classes if e] == [(13, 1296), (13, 1296)]
    proper = [(s, c, m) for s, c, m, e in classes if not e]
    coords = [(i//25, i//5 % 5, i % 5) for i in range(125)]
    fibers = [sum(1 << i for i, p in enumerate(coords) if p[j] == a) for j in range(3) for a in range(5)]
    for chosen in range(1 << 10):
        remaining = [(s, c, m) for i, (s, c, m) in enumerate(proper) if not (chosen >> i & 1)]
        free = 0
        for s, c, m in remaining: free |= m
        slack = sum(c-(557 if s == 9 else 744) for s, c, m in remaining)
        assert 3*sum(max((free & f).bit_count()-2*len(remaining), 0) for f in fibers) <= slack
    for stem in ('union', 'frame', 'native_marginal'):
        subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt', HERE/'sources'/(stem+'.cpp'), '-o', work/stem], check=True)
    profile_result = json.loads((HERE/'result.json').read_text())
    assert profile_result['complete_E2_exclusion'] is False
    frames = {}
    for count, total in sorted({(r['embedded_count'], sum(r['embedded_sizes'])) for r in selected['rows']}):
        assert count == 2 and total > 13*(count-1)
        run = subprocess.run([work/'union', str(count), str(total), '-1', 'all'],
                             input=(HERE/'inputs/parent').read_text(), text=True, capture_output=True, check=True)
        canonical = subprocess.run([work/'frame', HERE/'inputs/parent', HERE/'inputs/maps', str(count)],
                                   input=run.stdout, text=True, capture_output=True, check=True)
        file = f'frames_{count}_{total}.txt'; expected = (HERE/'frames'/file).read_text()
        assert canonical.stdout == expected
        frame_receipt = json.loads((HERE/'frames'/file.replace('.txt', '.json')).read_text())
        assert list(map(int, canonical.stderr.split())) == [frame_receipt['original_frames'], frame_receipt['canonical_frames']]
        (work/file).write_text(canonical.stdout)
        frames[count, total] = frame_receipt['canonical_frames']
    total_nodes = total_guards = total_frames = 0
    for file in profile_result['completed_receipt_files']:
        receipt = json.loads((HERE/'receipts'/file).read_text()); row = receipt['profile']
        assert receipt['engine'] == 'marginal' and receipt['complete_profile_exclusion']
        assert row['outside_condition_trivial_union'] and row['all_parents_for_embedded_classes_must_be_distinct']
        assert row['old_union_enumerator_cannot_stop_before_k'] and row['embedded_count'] == 2
        count, total = row['embedded_count'], sum(row['embedded_sizes'])
        cmd = [str(work/'native_marginal'), str(HERE/'inputs/obs'), str(HERE/'inputs/parent'), str(HERE/'inputs/B'),
               str(work/f'frames_{count}_{total}.txt'), ','.join(map(str, row['proper_sizes'])),
               ','.join(map(str, row['embedded_sizes'])), str(row['minimum_embedded_cost']), '9995',
               '0', str(frames[count, total]), '0', '0', ','.join(['0']*14)]
        completed = subprocess.run(cmd, text=True, capture_output=True, check=True)
        lines = completed.stderr.splitlines()
        assert not completed.stdout and len(lines) == 2
        values = list(map(int, lines[0].split()))
        assert values == receipt['counts'] and values[0] == frames[count, total] and values[-1] == 0
        assert lines[1].split()[0] == 'marginal'
        guards = list(map(int, lines[1].split()[1:]))
        assert guards == receipt['marginal_test_prune_counts']
        total_frames += values[0]; total_nodes += values[1]; total_guards += guards[1]
    assert total_nodes == profile_result['completed_search_nodes'] == 3161088
    assert total_frames == profile_result['completed_mother_profile_frames'] == 38
    assert total_guards == profile_result['completed_guard_prunes'] == 3145978
    result = {'schema': 'MIXED_BOUND_AND_FOUR_E2_LAYERS_REPLAY_V1', 'all_verified': True,
              'mixed_bound_native_rows': 50678, 'native_positive_classes': 12, 'positive_guard_substates': 1024,
              'completed_size_profiles_replayed': 4, 'mother_profile_frames': total_frames,
              'search_nodes': total_nodes, 'guard_prunes': total_guards,
              'pending_size_profiles': 10, 'complete_E2_exclusion': False,
              'scope': 'Full replay of the fixed completed sublayers only. Pending cases and broader optimum claims remain outside this certificate.'}
    (work/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
