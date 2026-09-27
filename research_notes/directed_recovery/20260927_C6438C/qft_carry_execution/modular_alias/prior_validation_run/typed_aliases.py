"""Complete bounded modular aliases through the actual typed lazy arithmetic.

Scientific residue products, inverses and displacement sums retain typed
certificates. Python dictionary lookup, exponent-bit/index routing, sign tags
and sorting are declared host wiring, never replacement modular arithmetic.
"""
from __future__ import annotations

from pathlib import Path
from copy import deepcopy
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep26-shor-general'
sys.path.insert(0, str(OLD / 'optimization/lazy_modular'))
from lazy_modular import Arithmetic, LazyModularFactory, verify_lazy_permutation, source_binding
from stage45.brc_loop_recheck import CALLS


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value):
    return type(value) is int


class AliasDiscoveryError(ValueError):
    def __init__(self, message, evidence, metrics):
        super().__init__(message)
        self.evidence = evidence
        self.metrics = metrics


def source_hashes():
    import lazy_modular
    return {
        'typed_aliases.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'lazy_modular.py': hashlib.sha256(Path(lazy_modular.__file__).read_bytes()).hexdigest(),
    }


def discover_aliases(program, depth, targets, baby_width):
    """Return every d with |d| < 2**depth and b**d == target (mod N).

    b is the program's last applied multiplier at depth>=1. Its original
    permutation certificate is replayed, not assumed from an arbitrary list.
    The result keeps all repeated baby exponents and does not hide a large J
    behind a short-period fallback. Short period is reported only if actually
    found in the consecutive powers through baby_width.

    At depth zero no b is needed: only displacement zero at target one exists.
    Targets must be canonical unit residues; duplicate target requests coalesce.
    A failure raises AliasDiscoveryError carrying available complete evidence.
    """
    calls_before = len(CALLS)
    arithmetic = Arithmetic()
    factory = LazyModularFactory()
    verifications = []
    verified = {}
    evidence = {'schema': 'BRC_COMPLETE_BOUNDED_ALIASES_V1',
        'inputs': {'N': getattr(program, 'N', None), 'a': getattr(program, 'a', None),
                   't': getattr(program, 't', None), 'depth': depth,
                   'baby_width': baby_width},
        'source_sha256': source_hashes(), 'program_binding': None,
        'target_unit_checks': [], 'baby_powers': [], 'baby_buckets': [],
        'giant_queries': [], 'short_period': None,
        'scope': 'complete signed displacement aliases only; no phase propagation or known order input',
        'host_wiring': 'loop indices, exponent sign tagging, exact label dictionary equality, list selection and sorting'}
    stats = {'baby_steps': 0, 'giant_steps': 0, 'giant_queries': 0,
             'matched_baby_exponents_inspected': 0, 'discarded_final_block_candidates': 0,
             'negative_zero_excluded': 0, 'output_aliases': 0,
             'peak_baby_exponent_pairs': 0, 'peak_baby_distinct_labels': 0}

    def finish():
        tables = factory.export_certificate()
        evidence['arithmetic_operations'] = deepcopy(arithmetic.operations)
        evidence['arithmetic_cost'] = dict(arithmetic.stats)
        evidence['table_instances'] = tables
        evidence['permutation_verifications'] = deepcopy(verifications)
        evidence['native_source'] = source_binding() if tables else None
        metrics = dict(stats)
        metrics['arithmetic_cost'] = dict(arithmetic.stats)
        metrics['table_instance_count'] = len(tables)
        metrics['table_stats'] = [dict(x['stats']) for x in tables]
        metrics['setup_adder_digit_replays'] = sum(x['stats']['setup_adder_digit_replays'] for x in tables)
        metrics['column_adder_digit_replays'] = sum(x['stats']['column_adder_digit_replays'] for x in tables)
        metrics['verification_adder_digit_replays'] = sum(x['result']['replayed_adder_digits'] for x in verifications)
        metrics['auxiliary_adder_digit_replays'] = arithmetic.stats['adder_digit_replays']
        metrics['total_adder_digit_replays'] = (metrics['setup_adder_digit_replays'] +
            metrics['column_adder_digit_replays'] + metrics['verification_adder_digit_replays'] +
            metrics['auxiliary_adder_digit_replays'])
        metrics['column_requests'] = sum(x['stats']['column_requests'] for x in tables)
        metrics['computed_columns'] = sum(x['stats']['computed_columns'] for x in tables)
        metrics['actual_native_core_calls_delta'] = len(CALLS)-calls_before
        metrics['evidence_json_bytes'] = len(json.dumps(evidence, sort_keys=True, separators=(',', ':')).encode())
        return deepcopy(evidence), metrics

    def table(multiplier):
        item = factory(N, multiplier)
        if multiplier not in verified:
            record = verify_lazy_permutation(item)
            verified[multiplier] = record
            verifications.append({'scope': 'new_alias_table', 'result': record})
        return item

    try:
        N, t = getattr(program, 'N', None), getattr(program, 't', None)
        require(integer(N) and N >= 3, 'integer modulus N>=3 required')
        require(integer(t) and t >= 1, 'program integer width required')
        require(integer(depth) and 0 <= depth <= t, 'depth outside program width')
        L = 1 << depth
        require(integer(baby_width) and 1 <= baby_width <= L, 'baby_width outside [1,2^depth]')
        require(isinstance(targets, (tuple, list)), 'explicit tuple/list of targets required')
        require(all(integer(z) and 1 <= z < N for z in targets), 'canonical integer residues 1<=z<N required')
        canonical_targets = tuple(sorted(set(targets)))
        evidence['inputs']['targets'] = canonical_targets
        evidence['inputs']['interval_length'] = L
        # A typed gcd precheck exposes the full failed arithmetic trace as well
        # as successful unit checks; no constructor exception hides that work.
        for z in canonical_targets:
            left, right, steps = N, z, []
            while right:
                quotient, remainder, op = arithmetic.divide(left, right)
                steps.append({'left': left, 'right': right, 'quotient': quotient,
                              'remainder': remainder, 'division_operation': op})
                left, right = right, remainder
            evidence['target_unit_checks'].append({'target': z, 'gcd': left, 'steps': steps})
            require(left == 1, 'target is not a unit modulo N')
        if depth == 0:
            aliases = {z: ((0,) if z == 1 else ()) for z in canonical_targets}
            stats['output_aliases'] = sum(len(x) for x in aliases.values())
            evidence.update(status='COMPLETE', aliases=aliases,
                completeness='Only displacement 0 exists at depth zero; b is not read.')
            record, metrics = finish()
            return {'status': 'COMPLETE', 'aliases': aliases, 'short_period': None,
                    'evidence': record, 'metrics': metrics}
        require(hasattr(program, 'modular_powers') and hasattr(program, 'tables'), 'certified program schedule required')
        require(len(program.modular_powers) == t and len(program.tables) == t, 'incomplete program schedule')
        b = program.modular_powers[depth-1]
        inherited = program.tables[depth-1]
        require(integer(b) and inherited.N == N and inherited.b == b, 'program multiplier/table mismatch')
        binding = verify_lazy_permutation(inherited)
        verifications.append({'scope': 'inherited_program_multiplier', 'result': binding})
        evidence['program_binding'] = {'N': N, 'b': b, 'depth': depth,
            'permutation': deepcopy(inherited.permutation_certificate), 'verification': binding}
        base = table(b)
        buckets = {}
        value, short_period = 1, None
        for exponent in range(baby_width):
            buckets.setdefault(value, []).append(exponent)
            evidence['baby_powers'].append({'exponent': exponent, 'residue': value})
            value = base[value]
            stats['baby_steps'] += 1
            if value == 1 and short_period is None:
                short_period = exponent+1  # index of the observed consecutive return
        evidence['baby_width_power'] = {'exponent': baby_width, 'residue': value}
        evidence['baby_buckets'] = [{'residue': z, 'exponents': tuple(es)} for z, es in sorted(buckets.items())]
        stats['peak_baby_exponent_pairs'] = baby_width
        stats['peak_baby_distinct_labels'] = len(buckets)
        width_table = table(value)
        inverse_width = width_table.inverse_multiplier
        giant_table = table(inverse_width)
        evidence['inverse_baby_width_power'] = inverse_width
        evidence['short_period'] = short_period
        aliases = {}
        for z in canonical_targets:
            target_table = table(z)
            inverse_z = target_table.inverse_multiplier
            found = []
            for sign, seed in ((1, z), (-1, inverse_z)):
                offset, query, block = 0, seed, 0
                while offset < L:
                    matches = buckets.get(query, ())
                    rows = []
                    for u in matches:
                        d, add_id = arithmetic.add(offset, u)
                        relation, _, compare_id = arithmetic.compare(d, L)
                        keep = relation < 0 and (sign == 1 or d != 0)
                        stats['matched_baby_exponents_inspected'] += 1
                        if relation >= 0:
                            stats['discarded_final_block_candidates'] += 1
                        elif sign == -1 and d == 0:
                            stats['negative_zero_excluded'] += 1
                        if keep:
                            found.append(d if sign == 1 else -d)
                        rows.append({'baby_exponent': u, 'magnitude': d, 'signed_displacement': d if sign == 1 else -d,
                                     'sum_operation': add_id, 'range_comparison': compare_id, 'retained': keep})
                    next_offset, offset_id = arithmetic.add(offset, baby_width)
                    next_query = giant_table[query] if next_offset < L else None
                    if next_query is not None:
                        stats['giant_steps'] += 1
                    evidence['giant_queries'].append({'target': z, 'sign': sign, 'block': block,
                        'offset': offset, 'query': query, 'matched': rows, 'next_offset': next_offset,
                        'offset_add_operation': offset_id, 'next_query': next_query})
                    stats['giant_queries'] += 1
                    offset, query, block = next_offset, next_query, block+1
            require(len(found) == len(set(found)), 'duplicate signed displacement after unique block decomposition')
            aliases[z] = tuple(sorted(found))
        stats['output_aliases'] = sum(len(x) for x in aliases.values())
        evidence.update(status='COMPLETE', aliases=aliases,
            completeness='All (v,u) with 0<=u<B, vB+u<L are tested through exact residue lookup; repeated baby exponents retained; positive z and negative z^-1 searches; zero excluded only in negative search.',
            short_period_is_discovered_not_input=True,
            complexity_scope='B + ceil(L/B) modular preparation/query terms plus all J outputs, target count, full certificates and exact arithmetic bit cost; no polynomial input-bit claim.')
        record, metrics = finish()
        return {'status': 'COMPLETE', 'aliases': aliases, 'short_period': short_period,
                'evidence': record, 'metrics': metrics}
    except ValueError as error:
        evidence.update(status='REJECTED', error=str(error))
        record, metrics = finish()
        raise AliasDiscoveryError(str(error), record, metrics) from error


def _semantic(value):
    """Drop only process-dependent native cache-call deltas for full replay."""
    if isinstance(value, dict):
        return {str(k): _semantic(v) for k, v in value.items()
                if k != 'native_kernel_calls_delta'}
    if isinstance(value, (tuple, list)):
        return [_semantic(v) for v in value]
    return value


def verify_alias_result(program, result):
    """Actual typed replay; reject changed aliases, words or completeness data.

    The full replay evidence and cost are returned, so verification is not
    claimed to be a free hash check. The caller retains both records if needed.
    """
    require(result.get('status') == 'COMPLETE', 'only COMPLETE alias records can be consumed')
    inputs = result['evidence']['inputs']
    require(inputs['N'] == program.N and inputs['a'] == program.a and inputs['t'] == program.t,
            'alias record belongs to another program')
    replay = discover_aliases(program, inputs['depth'], list(inputs['targets']), inputs['baby_width'])
    require(_semantic(result['aliases']) == _semantic(replay['aliases']), 'alias outputs do not replay')
    require(result['short_period'] == replay['short_period'], 'short period does not replay')
    require(_semantic(result['evidence']) == _semantic(replay['evidence']),
            'complete typed alias evidence does not replay')
    return {'verified': True, 'replay': replay,
            'scope': 'complete scientific evidence replay; native cache-call deltas are process dependent'}
