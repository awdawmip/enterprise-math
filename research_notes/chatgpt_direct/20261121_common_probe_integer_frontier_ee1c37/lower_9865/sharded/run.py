"""Run one exact cost profile in disjoint persisted top-level prefix batches."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import time

HERE = Path(__file__).resolve().parent


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work', type=Path, required=True, help='Already prepared complete native input bank and anchor files')
    p.add_argument('--tag', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--batch-size', type=int, default=32)
    p.add_argument('--begin', type=int, default=0, help='Optional begin batch index, for disjoint worker ranges')
    p.add_argument('--end', type=int, help='Optional end batch index, exclusive')
    args = p.parse_args()
    assert args.batch_size >= 1 and args.begin >= 0
    args.work = args.work.resolve()
    args.output.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((args.work/'manifest.json').read_text())
    types = list(map(tuple, manifest['types']))
    counts = {(s, c): n for s, c, n in (tuple(map(int, item.split('-'))) for item in args.tag.split('_'))}
    assert sum(counts.values()) == 12 and sum(s*n for (s, c), n in counts.items()) == 125
    cost = sum(c*n for (s, c), n in counts.items())
    vector = [counts.get(kind, 0) for kind in types]
    assert sum(vector) == 12 and all(kind in types for kind in counts)
    provenance = {'source_sha256': sha256((HERE/'front_sharded.cpp').read_bytes()).hexdigest(),
                  'bank_sha256': sha256((args.work/'bank').read_bytes()).hexdigest(),
                  'profile_manifest_sha256': sha256((args.work/'manifest.json').read_bytes()).hexdigest()}
    with subprocess.Popen([HERE/'front_sharded', args.work/'bank', args.work, args.work],
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
        def request(begin, end):
            start = time.monotonic()
            process.stdin.write(' '.join(map(str, [cost, begin, end, *vector]))+'\n')
            process.stdin.flush()
            words = list(map(int, process.stdout.readline().split()))
            assert len(words) == 6 and words[0] == cost, words
            row = dict(zip(('cost', 'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found', 'total_frames'), words))
            row.update(tag=args.tag, begin_frame=begin, end_frame=end, seconds=time.monotonic()-start,
                       engine='orbit-min-sharded', **provenance)
            return row

        probe = request(0, 0)
        assert probe['found'] == probe['search_nodes'] == probe['geometric_nodes'] == probe['leaf_nodes'] == 0
        total = probe['total_frames']
        assert total >= 0
        plan = {'cost': cost, 'tag': args.tag, 'total_frames': total, 'batch_size': args.batch_size,
                'ranges': [[start, min(total, start+args.batch_size)] for start in range(0, total, args.batch_size)],
                **provenance}
        plan_file = args.output/'plan.json'
        if plan_file.exists():
            assert json.loads(plan_file.read_text()) == plan
        else:
            plan_file.write_text(json.dumps(plan, indent=2, sort_keys=True)+'\n')
        completed = args.output/'completed'
        completed.mkdir(exist_ok=True)
        found = False
        for index, (begin, end) in enumerate(plan['ranges']):
            if index < args.begin or args.end is not None and index >= args.end:
                continue
            target = completed/f'{index:06d}.json'
            if target.exists():
                row = json.loads(target.read_text())
                assert all(row[k] == v for k, v in provenance.items())
                assert row['tag'] == args.tag and row['found'] == 0
                assert (row['begin_frame'], row['end_frame'], row['total_frames']) == (begin, end, total)
                continue
            status = args.output/f'running_{args.begin}.json'
            status.write_text(json.dumps({'tag': args.tag, 'cost': cost, 'batch': index,
                                         'begin_frame': begin, 'end_frame': end, 'started': time.time()})+'\n')
            row = request(begin, end)
            assert row['total_frames'] == total
            temporary = target.with_suffix('.tmp')
            temporary.write_text(json.dumps(row, indent=2, sort_keys=True)+'\n')
            temporary.replace(target)
            print(json.dumps(row, sort_keys=True), flush=True)
            if row['found']:
                assert (args.work/f'found_{cost}.json').exists()
                found = True
                break
            status.unlink(missing_ok=True)
        process.stdin.close()
        assert process.wait() == 0
    if found:
        print(json.dumps({'found': True, 'cost': cost, 'tag': args.tag,
                          'witness': str(args.work/f'found_{cost}.json')}, sort_keys=True), flush=True)
        return
    audit(args.output)


def audit(directory):
    plan = json.loads((directory/'plan.json').read_text())
    rows = []
    missing = []
    for index, (begin, end) in enumerate(plan['ranges']):
        target = directory/'completed'/f'{index:06d}.json'
        if not target.exists():
            missing.append(index)
            continue
        row = json.loads(target.read_text())
        for key in ('cost', 'tag', 'total_frames', 'source_sha256', 'bank_sha256', 'profile_manifest_sha256'):
            assert row[key] == plan[key]
        assert (row['begin_frame'], row['end_frame']) == (begin, end)
        assert row['found'] == 0
        rows.append(row)
    if plan['ranges']:
        assert plan['ranges'][0][0] == 0 and plan['ranges'][-1][1] == plan['total_frames']
    else:
        assert plan['total_frames'] == 0
    assert all(a[1] == b[0] for a, b in zip(plan['ranges'], plan['ranges'][1:]))
    summary = {key: plan[key] for key in ('cost', 'tag', 'total_frames', 'source_sha256', 'bank_sha256', 'profile_manifest_sha256')}
    summary.update(engine='orbit-min-sharded', complete=not missing, missing_batches=missing,
                   completed_batches=len(rows), expected_batches=len(plan['ranges']), found=0,
                   search_nodes=sum(row['search_nodes'] for row in rows),
                   geometric_nodes=sum(row['geometric_nodes'] for row in rows),
                   leaf_nodes=sum(row['leaf_nodes'] for row in rows))
    (directory/'coverage.json').write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n')
    print(json.dumps(summary, sort_keys=True), flush=True)
    return summary


if __name__ == '__main__':
    main()
