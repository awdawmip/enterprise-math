"""One-shot typed BRC unit-conic transport; compare already saved evidence."""
from pathlib import Path
import gzip
import hashlib
import json
import sys
import traceback

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'RELATIVE_PORT_RESULTS.json.gz': '5a9c055dc879a9a8b33620055183b41131d739d03c735ff37a1ed67704aeca26',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, data):
    with path.open('xb') as stream:
        stream.write(data)


def run():
    guard = json.loads((BASE/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard['activity_allowed'] and guard['persistence_allowed']
    assert not guard['sync_debt_events']
    assert guard['record_sha256'] == 'aad2a53ba51160513368bd8a966fce8c6d20c2d37a21c7348f59a280d3fe8db6'
    for name, digest in EXPECTED.items():
        assert sha(BASE/name) == digest, name
    binding = {'source_sha256': sha(Path(__file__)),
               'plan_sha256': sha(OUT/'EXPERIMENT_PLAN.md'),
               'guard_sha256': sha(BASE/'STARTUP_GUARD.json'),
               'saved_baseline': EXPECTED}
    # Refuse replay before native module imports or arithmetic execution.
    write_new(OUT/'STARTED.json', (json.dumps(binding, indent=2)+'\n').encode())
    try:
        execute(binding)
    except BaseException:
        write_new(OUT/'FAILED.txt', traceback.format_exc().encode())
        raise


def execute(binding):
    sys.path.insert(0, str(BASE))
    import native_relative_port as old
    from fractions import Fraction

    binding['reused_interfaces'] = old.source_check()
    saved_raw = gzip.decompress((BASE/'RELATIVE_PORT_RESULTS.json.gz').read_bytes())
    assert hashlib.sha256(saved_raw).hexdigest() == '6a111ca626f3330d16d513a15bfc31923a8c990723108e99c65b61fa5d229d28'
    saved = json.loads(saved_raw)

    def decode(rows):
        return {tuple(row['port']): old.hist.WeightHistogram.from_counts(
            {Fraction(n, d): count for n, d, count in row['histogram']}) for row in rows}

    def fold(u, v, route):
        comparison, _, _ = route.arithmetic.compare(u, v)
        return (u, v) if comparison <= 0 else (v, u)

    def collapse(states):
        out = {}
        for key, packet in states.items():
            old.merge(out, key if key[0] == 'FACTOR' else ('LIVE', key[1]), packet)
        return out

    def verify_conic(states, validator):
        products = []
        for key in sorted(states):
            if key[0] == 'LIVE':
                value, operation = validator.arithmetic.modmul(key[1], key[2], validator.N)
                assert value == 1, key
                products.append({'point': list(key[1:]), 'product': value, 'operation': operation})
        return products

    cases = []
    for baseline in saved['cases']:
        inputs = baseline['inputs']
        N, a, t = inputs['N'], inputs['a'], inputs['layers']
        production = old.Route(N, 'correlated_conic')
        schedule = old.Route(N, 'public_schedule')
        validation = old.Route(N, 'conic_validation')
        states = {('LIVE', 1, 1): old.ONE}
        layers = []
        c = a
        for depth in range(1, t+1):
            ci = production.table(c).inverse_multiplier
            out = {}
            for key, packet in sorted(states.items()):
                if key[0] == 'FACTOR':
                    production.deposit(out, key, packet, old.ONE)
                    continue
                u, v = key[1:]
                candidates = [(u, v, old.DOUBLE),
                    (production.mul(c, u), production.mul(ci, v), old.ATOM),
                    (production.mul(ci, u), production.mul(c, v), old.ATOM)]
                for x, y, atom in candidates:
                    g = production.observe(x, 1)
                    destination = ('FACTOR', g, depth) if 1 < g < N else ('LIVE', *fold(x, y, production))
                    production.deposit(out, destination, packet, atom)
            states = out
            invariant_receipts = verify_conic(states, validation)
            reference = baseline['layers'][depth-1]
            assert c == reference['multiplier']
            assert collapse(states) == decode(reference['folded'])
            assert old.total_packet(states).total_mass == 1
            layers.append({'depth': depth, 'multiplier': c, 'states': old.encode_states(states),
                           'invariant_receipts': invariant_receipts,
                           'saved_folded_histogram_equal': True})
            if depth < t:
                c, _ = schedule.arithmetic.modmul(c, c, N)
        assert old.final_observation(states) == decode(baseline['output'])
        assert not production.inverses and not production.folds
        cases.append({'inputs': inputs, 'layers': layers,
                      'output': old.encode_states(old.final_observation(states)),
                      'routes': [r.export() for r in (production, schedule, validation)]})

    negative = old.Route(15, 'reject_nonconic_point')
    value, operation = negative.arithmetic.modmul(2, 2, 15)
    assert value != 1
    payload = {'status': 'PASS_FINITE_CONIC_AUTHOR_EXECUTION_NOT_ADMITTED',
               'binding': binding, 'cases': cases,
               'negative': {'point': [2, 2], 'N': 15, 'product': value,
                            'rejected': True, 'operation': operation, 'route': negative.export()},
               'native_catalog_calls': len(old.CALLS), 'all_native_records': old.CALLS}
    raw = (json.dumps(payload, sort_keys=True, default=old.plain, separators=(',', ':'))+'\n').encode()
    compressed = gzip.compress(raw, mtime=0)
    write_new(OUT/'CONIC_RESULTS.json.gz', compressed)

    def digits(route):
        return (route['arithmetic_stats']['adder_digit_replays']
                + sum(t['stats']['setup_adder_digit_replays']+t['stats']['column_adder_digit_replays'] for t in route['tables'].values())
                + sum(v['cost']['adder_digit_replays'] for v in route['inverses'].values())
                + sum(v['cost']['adder_digit_replays'] for v in route['gcds'].values()))

    summary = {'status': payload['status'], 'raw_bytes': len(raw),
               'raw_sha256': hashlib.sha256(raw).hexdigest(),
               'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
               'native_catalog_calls': len(old.CALLS),
               'cases': [{'inputs': now['inputs'],
                    'new_costs': {r['name']: digits(r) for r in now['routes']},
                    'saved_baseline_costs': {r['name']: digits(r) for r in then['routes']},
                    'layer_histogram_equal': [row['saved_folded_histogram_equal'] for row in now['layers']],
                    'standalone_state_inverse_certificates': len(now['routes'][0]['inverses']),
                    'output': now['output']} for now, then in zip(cases, saved['cases'])],
               'negative_digits': digits(payload['negative']['route']),
               'cost_scope': 'Typed digit replay ledger; setup and column work included; auxiliary histogram merges and general allocation/rational-library costs excluded. No timing/scaling claim.'}
    write_new(OUT/'CONIC_SUMMARY.json', (json.dumps(summary, indent=2)+'\n').encode())
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    run()
