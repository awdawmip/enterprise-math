"""Run unmodified native profiles while explicitly reserving selected shards."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
from queue import Empty, Queue
import subprocess
from threading import Event, Lock
import time

HERE = Path(__file__).resolve().parent
LOWER = HERE.parent


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--cost', type=int, required=True)
    p.add_argument('--jobs', type=int, default=2)
    p.add_argument('--exclude-tag', action='append', default=[])
    p.add_argument('--profiles', type=Path)
    args = p.parse_args()
    args.work = args.work.resolve()
    source = args.profiles or LOWER/'audit'/f'cost_{args.cost}_profiles.txt'
    tags = source.read_text().splitlines()
    assert len(tags) == len(set(tags)) and set(args.exclude_tag).issubset(tags)
    types = list(map(tuple, json.loads((args.work/'manifest.json').read_text())['types']))
    provenance = {'engine': 'orbit-min',
                  'source_sha256': sha256((LOWER/'front_orbit_min_witness.cpp').read_bytes()).hexdigest(),
                  'bank_sha256': sha256((args.work/'bank').read_bytes()).hexdigest(),
                  'driver_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    done = {}
    log = args.work/'completed.jsonl'
    if log.exists():
        for line in log.read_text().splitlines():
            row = json.loads(line)
            assert row['cost'] == args.cost and row['tag'] in tags and row['found'] == 0
            assert row['tag'] not in done
            done[row['tag']] = row
    queue = Queue()
    for tag in tags:
        if tag not in done and tag not in args.exclude_tag:
            counts = {(s, c): n for s, c, n in (tuple(map(int, item.split('-'))) for item in tag.split('_'))}
            assert sum(counts.values()) == 12 and sum(s*n for (s, c), n in counts.items()) == 125
            assert sum(c*n for (s, c), n in counts.items()) == args.cost
            queue.put((tag, [counts.get(kind, 0) for kind in types]))
    lock = Lock()
    stop = Event()
    found = []

    def worker(worker_id):
        with subprocess.Popen([args.work/'front_orbit_min_witness', args.work/'bank', args.work, args.work],
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
            status = args.work/f'running{worker_id}.json'
            while not stop.is_set():
                try:
                    tag, vector = queue.get_nowait()
                except Empty:
                    break
                status.write_text(json.dumps({'tag': tag, 'cost': args.cost, 'started': time.time()})+'\n')
                start = time.monotonic()
                process.stdin.write(' '.join(map(str, [args.cost, *vector]))+'\n')
                process.stdin.flush()
                words = list(map(int, process.stdout.readline().split()))
                assert len(words) == 5 and words[0] == args.cost, words
                row = dict(zip(('cost', 'geometric_nodes', 'leaf_nodes', 'search_nodes', 'found'), words))
                row.update(tag=tag, seconds=time.monotonic()-start, **provenance)
                if row['found']:
                    assert (args.work/f'found_{args.cost}.json').exists()
                    found.append(row)
                    stop.set()
                    print(json.dumps(row, sort_keys=True), flush=True)
                    break
                with lock:
                    with log.open('a') as out:
                        out.write(json.dumps(row, sort_keys=True)+'\n')
                    done[tag] = row
                    if len(done) % 20 == 0:
                        print(json.dumps({'completed': len(done), 'pending_unassigned': queue.qsize(),
                                          'reserved_tags': args.exclude_tag, 'last': row}, sort_keys=True), flush=True)
                status.unlink(missing_ok=True)
            process.stdin.close()
            assert process.wait() == 0
            status.unlink(missing_ok=True)

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        list(pool.map(worker, range(min(args.jobs, queue.qsize()))))
    result = {'cost': args.cost, 'expected_whole_layer_profiles': len(tags),
              'completed_monolithic_profiles': len(done), 'reserved_tags': args.exclude_tag,
              'whole_layer_complete': len(done) == len(tags), 'found': found,
              'search_nodes': sum(row['search_nodes'] for row in done.values()),
              'geometric_nodes': sum(row['geometric_nodes'] for row in done.values())}
    (args.work/'result.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
