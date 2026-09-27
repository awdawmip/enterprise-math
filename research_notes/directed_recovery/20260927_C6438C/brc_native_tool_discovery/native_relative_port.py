"""Finite first-factor instrument composed from existing actual BRC interfaces.

This is a positive histogram quotient, not a signed Shor simulator or a cheap
unknown-order oracle. All scientific modular/gcd labels use the frozen typed
adder implementation. Python wires ports and retains exact source records.
"""
from pathlib import Path
from fractions import Fraction
import gzip
import hashlib
import json
import sys

OUT = Path(__file__).resolve().parent
NATIVE = Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src')
ARITH = Path('D:/em/TEMP/sep26-shor-general/optimization/lazy_modular')
sys.path.insert(0, str(NATIVE))
sys.path.insert(0, str(ARITH))
from enterprise_math import brc_histogram as hist
import lazy_modular as lm
import lazy_gcd as lg
from stage45.brc_loop_recheck import CALLS

GRID = ((15, 2, 3), (21, 2, 3), (35, 2, 3), (15, 14, 3))
ONE = hist.WeightHistogram.from_weights([1])
ATOM = hist.WeightHistogram.from_weights([Fraction(1, 4)])
DOUBLE = hist.WeightHistogram.from_counts({Fraction(1, 4): 2})
ZERO = hist.WeightHistogram(())


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def source_check():
    expected = {Path(lm.__file__): '08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4',
                Path(lg.__file__): 'b704590f055da0785d03b6026d9fa749e75218acd2764d25e90288f32db0965e'}
    for path, sha in expected.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == sha, str(path)
    assert blob(Path(hist.__file__).read_bytes()) == '9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'
    return {'em_source_ref': '2e81851d62c869a20b47ae083a24dde1a4c0420c',
            'histogram_blob': blob(Path(hist.__file__).read_bytes()),
            'files': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in expected},
            'native_arithmetic': lm.source_binding(),
            'new_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'plan_sha256': hashlib.sha256((OUT/'EXPERIMENT_PLAN.md').read_bytes()).hexdigest()}


def merge(out, key, packet):
    out[key] = hist.histogram_recoalesce(out.get(key, ZERO), packet)


def total_packet(states):
    out = ZERO
    for packet in states.values():
        out = hist.histogram_recoalesce(out, packet)
    return out


def encode_states(states):
    return [{'port': list(key), 'histogram': [[w.numerator, w.denominator, c] for w, c in packet.entries]}
            for key, packet in sorted(states.items())]


def plain(value):
    if isinstance(value, Fraction):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    raise TypeError(type(value).__name__)


class Route:
    def __init__(self, N, name):
        self.N, self.name = N, name
        self.arithmetic = lm.Arithmetic()
        self.tables = {}
        self.inverses = {}
        self.folds = {}
        self.gcds = {}
        self.factor_checks = {}
        self.calls = {'multiply_column': 0, 'inverse_requests': 0, 'gcd_requests': 0,
                      'histogram_serial': 0, 'histogram_recoalesce': 0}

    def table(self, c):
        if c not in self.tables:
            self.tables[c] = lm.LazyModularColumns(self.N, c)
        return self.tables[c]

    def mul(self, c, x):
        self.calls['multiply_column'] += 1
        return self.table(c)[x]

    def inv(self, x):
        self.calls['inverse_requests'] += 1
        if x not in self.inverses:
            self.inverses[x] = lm.inverse_certificate(self.N, x)
        return self.inverses[x]['inverse_multiplier']

    def ratio(self, x, y):
        return self.mul(self.inv(y), x)

    def fold(self, u):
        if u not in self.folds:
            v = self.inv(u)
            relation, _, _ = self.arithmetic.compare(u, v)
            self.folds[u] = u if relation <= 0 else v
        return self.folds[u]

    def observe(self, x, y):
        d, _ = self.arithmetic.modsubtract(x, y, self.N)
        self.calls['gcd_requests'] += 1
        if d not in self.gcds:
            self.gcds[d] = lg.typed_gcd_trace(d, self.N)
        g = self.gcds[d]['value']
        if 1 < g < self.N and g not in self.factor_checks:
            quotient, remainder, operation = self.arithmetic.divide(self.N, g)
            assert remainder == 0 and 1 < quotient < self.N
            self.factor_checks[g] = {'factor': g, 'cofactor': quotient, 'remainder': remainder,
                                     'typed_division_operation': operation}
        return g

    def deposit(self, out, key, parent, atom):
        self.calls['histogram_serial'] += 1
        self.calls['histogram_recoalesce'] += 1
        merge(out, key, hist.histogram_serial(parent, atom))

    def export(self):
        return {'name': self.name, 'N': self.N, 'calls': self.calls,
                'arithmetic_operations': self.arithmetic.operations, 'arithmetic_stats': self.arithmetic.stats,
                'tables': {str(c): table.export_certificate() for c, table in self.tables.items()},
                'inverses': self.inverses, 'folds': self.folds, 'gcds': self.gcds,
                'factor_checks': self.factor_checks}


def layer(states, c, depth, route, relative, mutant=False, fold=False):
    out = {}
    inverse_c = route.table(c).inverse_multiplier if relative else None
    for key, packet in states.items():
        if key[0] == 'FACTOR':
            route.deposit(out, key, packet, ONE)
            continue
        if relative:
            u = key[1]
            destinations = [(u, ATOM if mutant else DOUBLE),
                            (route.mul(c, u), ATOM), (route.mul(inverse_c, u), ATOM)]
            for v, atom in destinations:
                g = route.observe(v, 1)
                port = ('FACTOR', g, depth) if 1 < g < route.N else ('LIVE', route.fold(v) if fold else v)
                route.deposit(out, port, packet, atom)
        else:
            x, y = key[1:]
            cx, cy = route.mul(c, x), route.mul(c, y)
            for xx, yy in ((x, y), (cx, y), (x, cy), (cx, cy)):
                g = route.observe(xx, yy)
                port = ('FACTOR', g, depth) if 1 < g < route.N else ('LIVE', xx, yy)
                route.deposit(out, port, packet, ATOM)
    return out


def projected(states, validator):
    out = {}
    for key, packet in states.items():
        port = key if key[0] == 'FACTOR' else ('LIVE', validator.ratio(key[1], key[2]))
        merge(out, port, packet)
    return out


def folded_projection(states, validator):
    out = {}
    for key, packet in states.items():
        port = key if key[0] == 'FACTOR' else ('LIVE', validator.fold(key[1]))
        merge(out, port, packet)
    return out


def final_observation(states):
    out = {}
    for key, packet in states.items():
        merge(out, key if key[0] == 'FACTOR' else ('FAIL',), packet)
    return out


def case(N, a, t):
    pair, quotient, folding, schedule, validation = (Route(N, name) for name in
        ('paired', 'quotient', 'inversion_folded', 'public_schedule', 'validation'))
    paired, relative = {('LIVE', 1, 1): ONE}, {('LIVE', 1): ONE}
    folded = {('LIVE', 1): ONE}
    multipliers, layers = [], []
    c = a
    for depth in range(1, t+1):
        multipliers.append(c)
        paired = layer(paired, c, depth, pair, False)
        relative = layer(relative, c, depth, quotient, True)
        folded = layer(folded, c, depth, folding, True, fold=True)
        projected_paired = projected(paired, validation)
        assert projected_paired == relative, ('histogram quotient mismatch', N, a, depth)
        assert folded_projection(relative, validation) == folded, ('inversion quotient mismatch', N, a, depth)
        assert total_packet(paired).total_mass == total_packet(relative).total_mass == 1
        layers.append({'depth': depth, 'multiplier': c, 'pair': encode_states(paired),
                       'relative': encode_states(relative), 'folded': encode_states(folded),
                       'exact_histogram_equal': True,
                       'pair_live': len([k for k in paired if k[0] == 'LIVE']),
                       'relative_live': len([k for k in relative if k[0] == 'LIVE']),
                       'folded_live': len([k for k in folded if k[0] == 'LIVE'])})
        if depth < t:
            c, _ = schedule.arithmetic.modmul(c, c, N)
    output = final_observation(relative)
    assert output == final_observation(paired)
    assert output == final_observation(folded)
    return {'inputs': {'N': N, 'a': a, 'layers': t}, 'multipliers': multipliers,
            'layers': layers, 'output': encode_states(output),
            'routes': [route.export() for route in (pair, quotient, folding, schedule, validation)]}


def run():
    binding = source_check()
    catalog_calls = len(CALLS)
    cases = [case(*inputs) for inputs in GRID]
    negative = Route(15, 'gcd_key_negative')
    rows = []
    for x, y in ((1, 2), (1, 8)):
        before = negative.observe(x, y)
        after = negative.observe(negative.mul(2, x), y)
        rows.append({'pair': [x, y], 'before_gcd': before, 'after_left_2_gcd': after})
    assert rows[0]['before_gcd'] == rows[1]['before_gcd']
    assert rows[0]['after_left_2_gcd'] != rows[1]['after_left_2_gcd']
    mutant = Route(15, 'missing_identity_multiplicity_mutant')
    mutated = layer({('LIVE', 1): ONE}, 2, 1, mutant, True, True)
    assert total_packet(mutated).total_mass != 1
    payload = {'status': 'PASS_FINITE_AUTHOR_EXECUTION_NOT_ADMITTED', 'binding': binding,
               'cases': cases, 'negative_gcd_key': rows,
               'mutant_mass': total_packet(mutated).total_mass,
               'negative_routes': [negative.export(), mutant.export()],
               'native_catalog_calls': catalog_calls, 'all_native_records': CALLS,
               'cost_scope': 'source-bound arithmetic traces and histogram invocation counts; no timing/scaling claim'}
    raw = (json.dumps(payload, sort_keys=True, default=plain, separators=(',', ':'))+'\n').encode()
    (OUT/'RELATIVE_PORT_RESULTS.json.gz').write_bytes(gzip.compress(raw, mtime=0))
    summary = {'status': payload['status'], 'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
               'gzip_sha256': hashlib.sha256((OUT/'RELATIVE_PORT_RESULTS.json.gz').read_bytes()).hexdigest(),
               'native_catalog_calls': catalog_calls, 'total_native_calls': len(CALLS),
               'cases': [{'inputs': c['inputs'], 'layer_live_counts': [[l['pair_live'], l['relative_live'], l['folded_live']] for l in c['layers']],
                          'output': c['output']} for c in cases], 'negative_gcd_key': rows,
               'missing_identity_mutant_mass': payload['mutant_mass']}
    (OUT/'RELATIVE_PORT_SUMMARY.json').write_text(json.dumps(summary,indent=2,default=plain)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2,default=plain))


if __name__ == '__main__':
    run()
