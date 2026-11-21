"""Original BRC integration of the reference-counted safe-prefix region.

The controller inherits the unchanged original physical command execution and
uses actual business identity outputs to maintain RegionEvidence.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'regional'))
from region import RegionEvidence
import check_prefix_certificate as prefix

directed, prior, old, base, e, r = (prefix.directed, prefix.prior, prefix.old,
                                  prefix.base, prefix.e, prefix.r)
CHECKS = 0


def ck(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


class RegionController(directed.Controller):
    def __init__(self, compiler):
        super().__init__(compiler)
        self.region = RegionEvidence(compiler.slots, compiler.color_bits)

    def all_events(self):
        return dict(**super().all_events(),
                    **{'region_'+key: value for key, value in self.region.events.items()})

    def step(self, J, op, *, trace=False, repeats=1, omitted=()):
        before = self.all_events()
        before_region = self.region.metrics()
        if op[0] == 'reserve':
            start = self.C.key(op[1], 0) % self.C.modulus
            color = self.region.select(start, self.C.colors, preferred=self.witness)
            if color is not None:
                self.witness = (start+color) % self.C.modulus
        J, mass, entry = super().step(J, op, trace=trace, repeats=repeats, omitted=omitted)
        if op[0] == 'reserve' and entry['control_events']['target_searches']:
            if entry['branches']:
                branch = entry['branches'][-1]
                depth = branch['level']+1
                value = branch['prefix'] | (branch['selected_bit'] << branch['level'])
            else:
                depth, value = 0, 0
            self.region.acquire(depth, value)
        elif op[0] == 'bind':
            self.region.bind(op[1], entry['observed_business_code'])
        elif op[0] == 'copy':
            self.region.copy(op[1], op[2])
        elif op[0] == 'drop':
            self.region.drop(op[1])
        after = self.all_events()
        entry.update(region_before=before_region, region=self.region.metrics(),
                     control_events={key: after[key]-before[key] for key in after})
        return J, mass, entry

    def summary(self):
        result = super().summary()
        result.update(strategy='tracked_region', final_region=self.region.metrics(),
                      additional_persistent_members=0, additional_candidate_relations=0)
        return result


# Verification boundary: exact table and full sparse-index enumeration occur here.
def verify_region(C, controller, table):
    directed.verify_memory(C, controller, table)
    region = controller.region
    if region.tree is None:
        return
    expected_members = []
    for row in table[1]:
        code = 0 if row is None else C.key(*row)
        residue = code % C.modulus
        expected_members.append(residue if code != 0 and residue % region.delta == region.prefix else None)
    ck(region.members == expected_members, 'regional slot marks equal exact current memberships')
    counts = Counter(value for value in expected_members if value is not None)
    ck(region.refs == counts, 'regional multiplicities match actual request slots')
    ck(region.tree.free_count == region.tree.size-len(counts), 'exact available region cardinality')
    for index in range(region.tree.size):
        residue = region.prefix+index*region.delta
        ck(region.tree.first(index, index) == (None if residue in counts else index),
           'sparse successor represents each available regional point exactly')
        ck(region.contains(residue) == (residue not in counts), 'regional membership is exact')
    ck(len(region.touched) == len(set(region.touched)), 'each touched slot is tracked once per region')
    ck({slot for slot, marked in enumerate(region.marked) if marked} == set(region.touched),
       'touched slot list and flags agree')


def run_case(C, table, operations, **kwargs):
    return prefix.run_case(C, table, operations, controller_factory=RegionController,
                           verifier=verify_region, **kwargs)


def compact(data, keep_entries=0):
    result = directed.compact(data, 0)
    if keep_entries:
        result['first_steps'] = []
        for entry in data['entries'][:keep_entries]:
            fields = ('op', 'answer', 'key', 'commands', 'vacancy_bit_reads',
                      'business_key_bit_reads', 'witness', 'old_query_pairs',
                      'physical_last_before_create', 'region_before', 'region')
            row = {key: entry[key] for key in fields if key in entry}
            row['control_events'] = {key: value for key, value in entry['control_events'].items() if value}
            result['first_steps'].append(row)
    return result


def compare(C, table, operations, *, keep_entries=0):
    rows, semantics = {}, None
    for name, runner, summarizer in (
            ('single_point', directed.run_case, directed.compact),
            ('prefix_class', prefix.run_case, prefix.compact),
            ('tracked_region', run_case, compact)):
        _, mass, result = runner(C, table, operations)
        ck(mass.count == 1, 'one actual original-kernel path')
        if semantics is None:
            semantics = result['semantic_prefixes']
        else:
            ck(result['semantic_prefixes'] == semantics, 'future-relevant semantics agree at each API boundary')
        rows[name] = summarizer(result, keep_entries)
    return rows


def costs():
    rows, inventories = [], []
    for slots in (6, 7):
        C = prior.Compiler(slots=slots)
        inventories.append(dict(slots=slots, targets=C.d, members=C.members,
                                candidates=len(C.H), additional_members=0, additional_candidates=0))
        for preparation in ('empty', 'first_r_keys'):
            references = ((None,)*slots if preparation == 'empty' else
                          tuple((0, color) for color in range(slots)))
            table = ((None,)*C.d, references)
            for rounds in (8, 32):
                operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*rounds
                rows.append(dict(scenario='overwrite_one_slot', slots=slots,
                                 preparation=preparation, rounds=rounds,
                                 **compare(C, table, operations, keep_entries=12 if rounds==8 else 0)))
    C = prior.Compiler(slots=6, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(8)))
    table = ((None,)*C.d, tuple(divmod(code-1, C.colors) for code in (1, 2, 3, 5, 6, 7)))
    operations = tuple(op for _ in range(16) for op in (
        ('reserve', 0), ('release', 1), ('reserve', 4), ('release', 13)))
    rows.append(dict(scenario='stable_opposite_targets', slots=6, rounds=32,
                     **compare(C, table, operations, keep_entries=8)))
    C = prior.Compiler(slots=2, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(4)))
    table = ((None,)*C.d, (None,)*C.slots)
    operations = (('reserve', 0), ('bind', 0, 0), ('reserve', 3))
    rows.append(dict(scenario='strict_read_saving', slots=2,
                     **compare(C, table, operations, keep_entries=len(operations))))
    return dict(mode='costs', rows=rows, inventories=inventories, assertions=CHECKS)


def regressions():
    C = prior.Compiler(slots=6)
    empty = ((None,)*C.d, (None,)*C.slots)
    saturated = ((None,)*C.d, tuple((0, color) for color in range(C.slots)))
    cases = {
        'restore_after_last_alias': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('copy', 1, 0), ('copy', 2, 1),
            ('drop', 0), ('drop', 1), ('release', 1), ('reserve', 0),
            ('valid', 2), ('drop', 2), ('release', 1), ('reserve', 0))),
        'overwrite_alias_and_selfcopy': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('copy', 1, 0), ('copy', 2, 0),
            ('copy', 1, 1), ('release', 1), ('reserve', 0), ('bind', 0, 0),
            ('valid', 1), ('drop', 1), ('drop', 2), ('release', 1), ('reserve', 0))),
        'empty_bind_and_drop_inside_even_region': (((None,)*3, tuple(
            divmod(code-1, C.colors) for code in (1, 1, 3, 3, 5, 7))), (
            ('reserve', 0), ('bind', 0, 2), ('drop', 1), ('release', 1), ('reserve', 2))),
        'nonempty_full_key_with_zero_residue': (((None,)*3, tuple(
            divmod(code-1, C.colors) for code in (1, 1, 3, 3, 5, 7))), (
            ('reserve', 1), ('bind', 0, 1), ('copy', 1, 0), ('release', 4),
            ('reserve', 2), ('valid', 0), ('drop', 0), ('drop', 1),
            ('release', 4), ('reserve', 1))),
        'reacquire_and_clear_marks': (saturated, (
            ('reserve', 0), ('bind', 0, 0), ('copy', 1, 0), ('release', 1),
            ('reserve', 0), ('bind', 1, 0), ('drop', 0), ('release', 1), ('reserve', 0))),
        'execute_removes_source_preserves_request': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('execute', 0), ('reserve', 0), ('valid', 0))),
        'protected_existing_source': (((None, None, 0), tuple((0, color) for color in range(6))), (
            ('reserve', 0), ('reserve', 1), ('reserve', 2), ('bind', 0, 0),
            ('copy', 1, 0), ('release', 1), ('reserve', 0), ('valid', 1))),
        'physical_register': (((None,)*3, tuple(
            None if code == 0 else divmod(code-1, C.colors)
            for code in (0, 18, 9, 20, 10, 8))),
            (('reserve', 0), ('bind', 0, 0), ('release', 1))*2 + (('reserve', 0),)),
    }
    rows = [dict(name=name, **compare(C, table, ops, keep_entries=len(ops)))
            for name, (table, ops) in cases.items()]
    _, _, restored = run_case(C, *cases['restore_after_last_alias'])
    counts = [entry['region']['occupied_residues'] for entry in restored['entries']]
    ck(counts[1:6] == [1]*5 and counts[9] == 0,
       'copy aliases hold a residue until its last reference is removed')
    _, _, executed = run_case(C, *cases['execute_removes_source_preserves_request'])
    ck(executed['entries'][2]['region']['occupied_residues'] == 1,
       'executing a request removes its source but retains its identity')
    _, _, zeroresidue = run_case(C, *cases['nonempty_full_key_with_zero_residue'])
    ck(zeroresidue['entries'][1]['observed_business_code'] == 8,
       'actual nonempty full key eight has residue zero')
    ck(zeroresidue['entries'][6]['region']['occupied_residues'] == 1 and
       zeroresidue['entries'][7]['region']['occupied_residues'] == 0,
       'zero residue remains occupied until the last nonempty-key alias is dropped')
    table, ops = cases['protected_existing_source']
    J, _, result = run_case(C, table, ops, trace=True)
    state = base.ref.old.seed(C.encode(table, False))
    protected = state.names()[C.targets[2]]
    for row in result['trace']:
        state, _, _ = base.ref.old.raw_step(state, row['command'], C.H)
        ck(state.names().get(C.targets[2]) == protected, 'existing C birth survives each original primitive')
    ck(state.matching == J, 'birth-labelled replay endpoint agrees')
    return dict(mode='regressions', rows=rows, assertions=CHECKS,
                protected_source_raw_prefixes=len(result['word']))


def regional_gain():
    rows = []
    for slots in (6, 14):
        C = prior.Compiler(slots=slots)
        codes = (2,)*(slots//2)+(3,)*(slots//2)
        references = tuple(divmod(code-1, C.colors) for code in codes)
        table = ((None,)*C.d, references)
        for rounds in (8, 32):
            operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*rounds
            result = compare(C, table, operations, keep_entries=12 if rounds==8 else 0)
            first_reads = 3*slots//2
            ck(result['tracked_region']['vacancy_bit_reads'] == first_reads,
               'one first query funds all later regional selections')
            ck(result['single_point']['vacancy_bit_reads'] == first_reads+slots//2-1 and
               result['prefix_class']['vacancy_bit_reads'] == first_reads+slots//2-1,
               'point and shrinking class eventually read the untouched opposite branch')
            rows.append(dict(slots=slots, rounds=rounds, initial_codes=codes,
                             operations_per_round=[['reserve', 0], ['bind', 0, 0], ['release', 1]],
                             members=C.members, candidates=len(C.H),
                             additional_members=0, additional_candidates=0, **result))
    return dict(mode='regional_gain', rows=rows, assertions=CHECKS,
                scope='Exact original BRC execution of the half-key-2/half-key-3 preparation')


def path_tradeoff():
    C = prior.Compiler(slots=10, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(15)))
    codes = (7, 7, 0, 0, 5, 0, 1, 0, 1, 2)
    references = tuple(None if code == 0 else divmod(code-1, C.colors) for code in codes)
    table = ((None,)*C.d, references)
    operations = (('reserve', 9), ('bind', 8, 9), ('reserve', 1), ('bind', 7, 1),
                  ('reserve', 14), ('bind', 8, 14), ('reserve', 13), ('bind', 1, 13),
                  ('reserve', 0), ('bind', 9, 0), ('reserve', 10))
    result = compare(C, table, operations, keep_entries=len(operations))
    ck([result[key]['vacancy_bit_reads'] for key in ('single_point', 'prefix_class', 'tracked_region')]
       == [25, 26, 26], 'actual regional mixed-path reverse comparison')
    return dict(mode='path_tradeoff', slots=10, initial_codes=codes,
                operations=operations, members=C.members, candidates=len(C.H),
                assertions=CHECKS, **result)


def audit(slots):
    C = prior.Compiler(slots=slots)
    domain = base.domain(C)
    j = min(1, slots-1)
    sequences = (
        (('reserve', 0), ('bind', 0, 0), ('copy', j, 0), ('drop', 0), ('release', 1),
         ('reserve', 2), ('valid', j), ('drop', j), ('reserve', 0)),
        (('reserve', 2), ('bind', j, 2), ('copy', 0, j), ('execute', 0), ('reserve', 2),
         ('bind', j, 2), ('drop', 0), ('release', 4), ('reserve', 2)),
    )
    mass, runs, calls = directed.ZERO, 0, 0
    for index, table in enumerate(domain):
        cache = tuple(C.key(t, c) if c is not None else (5*index+3*t+1) % (1 << C.bits)
                      for t, c in enumerate(table[0]))
        for operations in sequences:
            _, weight, _ = run_case(C, table, operations, cache=cache)
            mass = r.merge(mass, weight)
            runs += 1
            calls += len(operations)
    ck(mass.count == runs, 'each finite preparation and alias sequence executes once')
    return dict(mode='audit', slots=slots, domain=len(domain), sequences=sequences,
                sequences_run=runs, api_calls=calls, CWM=e.cw(mass), assertions=CHECKS,
                inherited_assertions=directed.CHECKS, members=C.members, candidates=len(C.H))


def protected():
    result = prefix.protected(controller_factory=RegionController, verifier=verify_region)
    result['region_assertions'] = CHECKS
    return result


def omissions():
    C = prior.Compiler(slots=2)
    table = ((None,)*3, (None,)*2)
    ops = (('reserve', 0), ('bind', 0, 0), ('copy', 1, 0), ('drop', 0),
           ('release', 1), ('reserve', 0), ('valid', 1), ('drop', 1))
    want, _, baseline = run_case(C, table, ops, repeats=2)
    mass = directed.ZERO
    for position in range(len(baseline['word'])):
        got, weight, result = run_case(C, table, ops, repeats=2, omitted=(position,))
        ck(got == want and result['word'] == baseline['word'],
           'one omitted repeated primitive preserves endpoint and adaptive branches')
        ck(result['final_region'] == baseline['final_region'], 'final regional evidence agrees')
        mass = r.merge(mass, weight)
    ck(mass.count == len(baseline['word']), 'all individual omission positions counted')
    return dict(mode='omissions', slots=2, repeats=2, omission_budget=1,
                omission_positions=len(baseline['word']), CWM=e.cw(mass), assertions=CHECKS,
                operations=ops)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('costs', 'regressions', 'regional_gain', 'path_tradeoff', 'audit1', 'audit2', 'protected', 'omissions'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = audit(int(args.mode[-1])) if args.mode.startswith('audit') else globals()[args.mode]()
    text = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
