"""Reuse the entire empty-prefix class observed by the inherited BRC query.

The decision controller consumes only the inherited Boolean query observations
and business identity outputs.  Exact request tables occur below the stated
verification boundary.  Existing programs and their physical output handling
remain unchanged.
"""
from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'directed'))
import check_directed_vacancy as directed

old, prior, base, e, r = directed.old, directed.prior, directed.base, directed.e, directed.r
CHECKS = 0


def ck(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


class PrefixCertificateController(directed.Controller):
    """One safe low-prefix class, plus the inherited maintained prefix tree.

certificate=(depth,prefix) denotes every residue congruent to prefix modulo
2**depth.  A nonempty new binding inside it removes the child's half containing
that new residue; a hit at a singleton consumes the certificate.
"""

    def __init__(self, compiler):
        super().__init__(compiler)
        self.certificate = None
        self.certificate_events = dict(certificate_checks=0, certificate_hits=0,
                                      certificate_misses=0, certificate_acquisitions=0,
                                      internal_class_acquisitions=0,
                                      certificate_refinements=0, certificate_exhaustions=0,
                                      residue_changes_inside_certificate=0)

    def all_events(self):
        return dict(**super().all_events(), **self.certificate_events)

    def step(self, J, op, *, trace=False, repeats=1, omitted=()):
        before = self.all_events()
        before_certificate = self.certificate
        if op[0] == 'reserve' and self.certificate is not None:
            depth, prefix = self.certificate
            start = self.C.key(op[1], 0) % self.C.modulus
            color = (prefix-start) % (1 << depth)
            if (self.witness is not None and
                    self.witness % (1 << depth) == prefix and
                    (self.witness-start) % self.C.modulus < self.C.colors):
                color = (self.witness-start) % self.C.modulus
            self.certificate_events['certificate_checks'] += 1
            if color < self.C.colors:
                value = (start+color) % self.C.modulus
                self.certificate_events['certificate_hits'] += 1
                if self.witness is not None and self.witness != value:
                    self.certificate_events['residue_changes_inside_certificate'] += 1
                self.witness = value
            else:
                self.certificate_events['certificate_misses'] += 1

        J, mass, entry = super().step(J, op, trace=trace, repeats=repeats, omitted=omitted)
        if op[0] == 'reserve' and entry['control_events']['target_searches']:
            # The last chosen child is the actual n=0 stopping node.  Cached
            # witness hits have target_searches=0 and never enter this branch.
            if entry['branches']:
                branch = entry['branches'][-1]
                depth = branch['level']+1
                prefix = branch['prefix'] | (branch['selected_bit'] << branch['level'])
            else:
                depth, prefix = 0, 0
            self.certificate = (depth, prefix)
            self.certificate_events['certificate_acquisitions'] += 1
            if depth < self.C.color_bits:
                self.certificate_events['internal_class_acquisitions'] += 1
        elif op[0] == 'bind' and self.certificate is not None:
            code = entry['observed_business_code']
            depth, prefix = self.certificate
            # Code zero denotes an empty request; it adds no retained identity.
            if code and code % (1 << depth) == prefix:
                self.witness = None
                if depth < self.C.color_bits:
                    next_bit = 1-((code >> depth) & 1)
                    self.certificate = (depth+1, prefix | (next_bit << depth))
                    self.certificate_events['certificate_refinements'] += 1
                else:
                    self.certificate = None
                    self.certificate_events['certificate_exhaustions'] += 1

        after = self.all_events()
        entry.update(certificate_before=before_certificate, certificate=self.certificate,
                     certificate_size=(0 if self.certificate is None else
                                       self.C.modulus >> self.certificate[0]),
                     witness=self.witness,
                     control_events={key: after[key]-before[key] for key in after})
        return J, mass, entry

    def summary(self):
        result = super().summary()
        result.update(strategy='prefix_class', final_certificate=self.certificate,
                      certificate_fields=2, additional_persistent_members=0,
                      additional_candidate_relations=0)
        return result


# Verification boundary: these functions may inspect exact request tables.
def verify_certificate(C, controller, table):
    directed.verify_memory(C, controller, table)
    if controller.certificate is not None:
        depth, prefix = controller.certificate
        ck(0 <= depth <= C.color_bits and 0 <= prefix < 1 << depth,
           'certificate is a well-formed low-prefix class')
        for row in table[1]:
            if row is not None:
                ck(C.key(*row) % (1 << depth) != prefix,
                   'every retained nonempty request avoids the entire class')
        if depth < C.color_bits or C.colors == C.modulus:
            for target in range(C.d):
                color = (prefix-C.key(target, 0)) % (1 << depth)
                ck(color < C.colors, 'internal empty prefix covers every target')


def run_case(C, table, operations, *, cache=None, trace=False, repeats=1, omitted=(), check=True,
             controller_factory=PrefixCertificateController, verifier=verify_certificate):
    controller = controller_factory(C)
    cache = C.initial_cache(table) if cache is None else tuple(cache)
    J = C.encode(table, False, cache)
    mass = e.prep(J)
    original_table = table
    entries, forms, words, logs, old_pairs = [], [], [], [], set()
    for op in operations:
        offset = len(words)
        J, weight, entry = controller.step(J, op, trace=trace, repeats=repeats,
                                            omitted={x-offset for x in omitted if x >= offset})
        mass = r.serial(mass, weight)
        if check:
            table, answer, cache = old.expected_selected(C, table, cache, op, entry)
            ck(J == C.encode(table, answer, cache), 'whole core matching and output')
            verifier(C, controller, table)
            for pair in entry['old_query_pairs']:
                ck(pair not in old_pairs, 'initial label bit is queried at most once')
                old_pairs.add(pair)
            ck(entry['vacancy_bit_reads'] <= 2*C.slots-C.slots.bit_count(),
               'inherited query retains its per-call worst bound')
            forms.append((base.canon(C, table), answer))
        entries.append({key: value for key, value in entry.items() if key not in ('word', 'trace')})
        words.extend(entry['word'])
        if trace:
            logs.extend(dict(row, position=row['position']+offset) for row in entry['trace'])
    return J, mass, dict(**controller.summary(), entries=entries, initial_table=original_table,
                         final_table=table if check else None, semantic_prefixes=forms,
                         word=tuple(words), trace=logs, extra_old_bit_pairs=sorted(old_pairs))


def compact(data, keep_entries=0):
    result = {key: value for key, value in data.items()
              if key not in ('word', 'trace', 'semantic_prefixes', 'entries',
                             'initial_table', 'final_table', 'extra_old_bit_pairs')}
    if keep_entries:
        result['first_steps'] = []
        for entry in data['entries'][:keep_entries]:
            fields = ('op', 'answer', 'key', 'commands', 'vacancy_bit_reads',
                      'business_key_bit_reads', 'witness', 'old_query_pairs',
                      'physical_last_before_create', 'certificate_before',
                      'certificate', 'certificate_size')
            row = {key: entry[key] for key in fields if key in entry}
            row['control_events'] = {key: value for key, value in entry['control_events'].items() if value}
            result['first_steps'].append(row)
    return result


def compare(C, table, operations, *, keep_entries=0):
    _, old_weight, before = directed.run_case(C, table, operations)
    _, new_weight, after = run_case(C, table, operations)
    ck(old_weight.count == new_weight.count == 1, 'one actual primitive path for each strategy')
    ck(before['semantic_prefixes'] == after['semantic_prefixes'],
       'future-relevant source/request semantics match after every operation')
    return dict(single_point=directed.compact(before, keep_entries),
                prefix_class=compact(after, keep_entries),
                primitive_command_delta=after['commands']-before['commands'],
                vacancy_read_delta=after['vacancy_bit_reads']-before['vacancy_bit_reads'])


def costs():
    rows, inventories = [], []
    for slots in (2, 6, 7):
        target_count = 4 if slots == 2 else 8
        H = tuple((3*i+1, 3*i+2, 3*i+3) for i in range(target_count))
        C = prior.Compiler(slots=slots, H=H)
        inventories.append(dict(slots=slots, targets=C.d, members=C.members,
                                candidates=len(C.H), additional_members=0, additional_candidates=0))
        for preparation in ('empty', 'first_r_keys'):
            references = ((None,)*slots if preparation == 'empty' else
                          tuple((0, color) for color in range(slots)))
            table = ((None,)*C.d, references)
            operations = tuple(('reserve', target) for target in range(C.d))
            rows.append(dict(scenario='all_disjoint_targets', slots=slots, preparation=preparation,
                             target_sequence=list(range(C.d)),
                             **compare(C, table, operations, keep_entries=C.d)))
    for slots in (6, 7):
        C = prior.Compiler(slots=slots)
        inventories.append(dict(slots=slots, targets=C.d, members=C.members,
                                candidates=len(C.H), additional_members=0, additional_candidates=0))
        for preparation in ('empty', 'first_r_keys'):
            references = ((None,)*slots if preparation == 'empty' else
                          tuple((0, color) for color in range(slots)))
            table = ((None,)*C.d, references)
            for rounds in (2, 8, 32):
                operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*rounds
                rows.append(dict(scenario='overwrite_one_slot', slots=slots,
                                 preparation=preparation, rounds=rounds,
                                 **compare(C, table, operations, keep_entries=12 if rounds==8 else 0)))
    C = prior.Compiler(slots=6, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(8)))
    references = tuple(divmod(code-1, C.colors) for code in (1, 2, 3, 5, 6, 7))
    table = ((None,)*C.d, references)
    operations = tuple(op for _ in range(16) for op in (
        ('reserve', 0), ('release', 1), ('reserve', 4), ('release', 13)))
    rows.append(dict(scenario='stable_opposite_targets', slots=6,
                     preparation='all_residues_except_0_and_4', rounds=32,
                     target_sequence=[0, 4]*16,
                     **compare(C, table, operations, keep_entries=8)))
    return dict(mode='costs', rows=rows, inventories=inventories, assertions=CHECKS,
                scope='Actual original BRC core commands; stable and controlled mixed cases')


def regressions():
    C = prior.Compiler(slots=6)
    empty = ((None,)*C.d, (None,)*C.slots)
    saturated = ((None,)*C.d, tuple((0, color) for color in range(C.slots)))
    cases = {
        'bound_reference_stays_stale': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', 0))),
        'refine_then_exhaust': (empty, (('reserve', 0), ('bind', 0, 0), ('release', 1))*4),
        'empty_bind_preserves_certificate': (empty, (
            ('reserve', 0), ('release', 1), ('bind', 0, 0), ('reserve', 2))),
        'copy_drop_preserve_class': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('copy', 1, 0), ('drop', 0),
            ('release', 1), ('reserve', 2), ('valid', 1), ('drop', 1), ('reserve', 0))),
        'representative_and_selfcopy': (saturated, (
            ('reserve', 0), ('copy', 1, 0), ('copy', 2, 0), ('bind', 0, 0),
            ('release', 1), ('reserve', 0), ('valid', 1), ('drop', 1),
            ('copy', 2, 2), ('valid', 2), ('drop', 2), ('release', 1), ('reserve', 0))),
        'protected_existing_source': (((None, None, 0), tuple((0, color) for color in range(6))), (
            ('reserve', 0), ('reserve', 1), ('reserve', 2), ('bind', 0, 0),
            ('copy', 1, 0), ('release', 1), ('reserve', 0), ('valid', 1))),
        'business_feedback': (saturated, (
            ('valid', 4), ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0))),
        'physical_register': (((None,)*3, tuple(
            None if code == 0 else divmod(code-1, C.colors)
            for code in (0, 18, 9, 20, 10, 8))),
            (('reserve', 0), ('bind', 0, 0), ('release', 1))*2 + (('reserve', 0),)),
        'empty_binding_and_drop_inside_even_class': (((None,)*3, tuple(
            divmod(code-1, C.colors) for code in (1, 1, 3, 3, 5, 7))), (
            ('reserve', 0), ('bind', 0, 2), ('drop', 1), ('release', 1), ('reserve', 2))),
    }
    rows = [dict(name=name, **compare(C, table, ops, keep_entries=16))
            for name, (table, ops) in cases.items()]
    _, _, shrink = run_case(C, *cases['refine_then_exhaust'])
    ck([shrink['entries'][i]['certificate'] for i in (0, 1, 4, 7)] ==
       [(1, 1), (2, 3), (3, 7), None],
       'the first class follows its exact two refinements and singleton exhaustion')
    ck(shrink['control_events']['certificate_exhaustions'] >= 1,
       'matching singleton binding consumes the class')
    _, _, emptybind = run_case(C, *cases['empty_bind_preserves_certificate'])
    ck(emptybind['entries'][2]['observed_business_code'] == 0, 'actual empty binding has code zero')
    ck(emptybind['entries'][2]['certificate'] == emptybind['entries'][1]['certificate'],
       'empty binding preserves certificate')
    _, _, evenclass = run_case(C, *cases['empty_binding_and_drop_inside_even_class'])
    ck([entry['certificate'] for entry in evenclass['entries'][:3]] == [(1, 0)]*3,
       'empty code zero may lie inside a preserved even certificate')
    table, ops = cases['protected_existing_source']
    J, _, result = run_case(C, table, ops, trace=True)
    state = base.ref.old.seed(C.encode(table, False))
    protected = state.names()[C.targets[2]]
    for row in result['trace']:
        state, _, _ = base.ref.old.raw_step(state, row['command'], C.H)
        ck(state.names().get(C.targets[2]) == protected,
           'existing C keeps its original creation at every primitive prefix')
    ck(state.matching == J, 'birth-labelled endpoint agrees')
    return dict(mode='regressions', rows=rows, assertions=CHECKS,
                protected_source_raw_prefixes=len(result['word']))


def path_tradeoffs():
    rows = []
    C = prior.Compiler(slots=2, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(4)))
    table = ((None,)*4, (None,)*2)
    operations = (('reserve', 0), ('bind', 0, 0), ('reserve', 3))
    row = compare(C, table, operations, keep_entries=len(operations))
    ck(row['single_point']['vacancy_bit_reads'] == 3 and
       row['prefix_class']['vacancy_bit_reads'] == 2, 'actual strict extra-reading improvement')
    rows.append(dict(name='strict_read_saving', slots=2, initial_codes=[0, 0],
                     operations=operations, members=C.members, candidates=len(C.H), **row))
    C = prior.Compiler(slots=10, H=tuple((3*i+1, 3*i+2, 3*i+3) for i in range(15)))
    codes = (7, 7, 0, 0, 5, 0, 1, 0, 1, 2)
    references = tuple(None if code == 0 else divmod(code-1, C.colors) for code in codes)
    table = ((None,)*C.d, references)
    operations = (('reserve', 9), ('bind', 8, 9), ('reserve', 1), ('bind', 7, 1),
                  ('reserve', 14), ('bind', 8, 14), ('reserve', 13), ('bind', 1, 13),
                  ('reserve', 0), ('bind', 9, 0), ('reserve', 10))
    row = compare(C, table, operations, keep_entries=len(operations))
    ck(row['single_point']['vacancy_bit_reads'] == 25 and
       row['prefix_class']['vacancy_bit_reads'] == 26, 'actual mixed-path reverse comparison')
    rows.append(dict(name='mixed_path_reverse', slots=10, initial_codes=codes,
                     operations=operations, members=C.members, candidates=len(C.H), **row))
    return dict(mode='path_tradeoffs', rows=rows, assertions=CHECKS,
                scope='Original BRC execution of the exact control witnesses from future_bounds')


def audit(slots=1):
    C = prior.Compiler(slots=slots)
    domain = base.domain(C)
    j = min(1, slots-1)
    sequences = (
        (('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 2), ('valid', 0)),
        (('reserve', 0), ('copy', j, 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', j)),
        (('reserve', 2), ('bind', j, 2), ('copy', 0, j), ('drop', j), ('release', 4), ('reserve', 2)),
    )
    mass, runs, api_calls = directed.ZERO, 0, 0
    for index, table in enumerate(domain):
        cache = tuple(C.key(t, c) if c is not None else (5*index+3*t+1) % (1 << C.bits)
                      for t, c in enumerate(table[0]))
        for operations in sequences:
            _, weight, result = run_case(C, table, operations, cache=cache)
            mass = r.merge(mass, weight)
            runs += 1
            api_calls += len(operations)
    ck(mass.count == runs, 'positive CWM includes every finite preparation and sequence')
    return dict(mode='audit', slots=slots, domain=len(domain), sequences=sequences,
                sequences_run=runs, api_calls=api_calls, CWM=e.cw(mass),
                assertions=CHECKS, inherited_assertions=directed.CHECKS,
                members=C.members, candidates=len(C.H))


def omissions():
    C = prior.Compiler(slots=2)
    table = ((None,)*3, (None,)*2)
    ops = (('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 2), ('valid', 0))
    want, _, baseline = run_case(C, table, ops, repeats=2)
    mass = directed.ZERO
    for position in range(len(baseline['word'])):
        got, weight, result = run_case(C, table, ops, repeats=2, omitted=(position,))
        ck(got == want and result['word'] == baseline['word'],
           'one omitted repeated primitive preserves endpoint and adaptive branches')
        ck(result['final_certificate'] == baseline['final_certificate'],
           'certificate state agrees after each single omission')
        mass = r.merge(mass, weight)
    ck(mass.count == len(baseline['word']), 'each omission position counted once')
    return dict(mode='omissions', slots=2, repeats=2, omission_budget=1,
                omission_positions=len(baseline['word']), CWM=e.cw(mass), assertions=CHECKS)


def protected(*, controller_factory=PrefixCertificateController, verifier=verify_certificate):
    import check_batch_integration as integration
    gate, m, p = integration.gate, directed.m, directed.p

    class PrefixRing(integration.BatchRing):
        def begin(self, jobs, k, route):
            if k < len(jobs) and jobs[k][0] == 'mixed':
                return gate.PC('mixed', k, route=route)
            return super().begin(jobs, k, route)

        def body(self, node, actor, jobs, trace=False):
            pc = node.pcs[actor]
            controller = controller_factory(self.C)
            words, logs, entries = [], [], []
            J = node.J
            for op in jobs[actor][pc.job][1]:
                J, _, entry = controller.step(J, op, trace=trace)
                offset = len(words)
                words.extend(entry['word'])
                logs.extend(dict(row, position=row['position']+offset) for row in entry['trace'])
                entries.append(entry)
            pcs = list(node.pcs)
            pcs[actor] = self.begin(jobs[actor], pc.job+1, pc.route)
            return replace(node, J=J, pcs=tuple(pcs)), controller, entries, words, logs

    rows = []
    for phase in (0, 1):
        G = PrefixRing(slots=6)
        table = ((None,)*3, (None,)*6)
        operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*4 + (('reserve', 0),)
        jobs = ((('mixed', operations),), (('bind', 5, 0),))
        node = G.initial_node(table, phase=phase)
        entry_commands = 0
        while node.pcs[0].phase != 'mixed':
            node, _, _, _ = G.next(node, 0, jobs)
            entry_commands += 1
        held = node
        ck(G.lock(0) in held.J, 'inherited real entry owns the lock')
        node, controller, entries, words, logs = G.body(node, 0, jobs, trace=True)
        cache = G.C.initial_cache(table)
        for op, entry in zip(operations, entries):
            table, answer, cache = old.expected_selected(G.C, table, cache, op, entry)
        verifier(G.C, controller, table)
        extras = tuple(h for h in held.J if h not in G.C.H)
        ck(node.J == m.canon(G.C.encode(table, answer, cache)+extras),
           'whole mixed body and protection state')
        boundaries = [held.J]+[row['after'] for row in logs]
        refused_commands = 0
        for state in boundaries:
            ck(G.lock(0) in state, 'holder lock survives every primitive boundary')
            blocked, count, admitted = gate.complete(G, replace(held, J=state), 1, jobs)
            ck(admitted == () and blocked.pcs[1].phase == 'busy',
               'contender remains blocked before handoff')
            ck(tuple(h for h in blocked.J if h in G.C.H) == tuple(h for h in state if h in G.C.H),
               'refused contender preserves all core relations')
            refused_commands += count
        node, exit_commands, more = gate.complete(G, node, 0, jobs)
        ck(more == (), 'publish and handoff do not grant a second holder admission')
        ck(gate.old.bit(node.J, G.lanes[0].reply) == answer, 'private final reply')
        node, next_commands, admitted = gate.complete(G, node, 1, jobs)
        ck(admitted == (1,), 'contender enters after actual handoff')
        table, next_answer, cache = prior.parent.expected(G.C, table, cache, jobs[1][0])
        want = G.C.encode(table, next_answer, cache)
        for actor, lane in enumerate(G.lanes):
            want = m.canon(want+p.reg(lane.admitted, 1)+p.reg(lane.reply, int((answer, next_answer)[actor])))
            if actor != node.turn:
                want = m.canon(want+(G.gate_pair[actor][phase ^ 1],))
        ck(node.J == want, 'full final source, requests, keys, gate, replies and cleanup')
        ck(entry_commands+exit_commands == 31, 'unchanged real protection wrapper')
        rows.append(dict(phase=phase, body_operations=operations, body_commands=len(words),
                         wrapper_commands=entry_commands+exit_commands,
                         protected_invocation_commands=entry_commands+len(words)+exit_commands,
                         vacancy_bit_reads=controller.vacancy_bit_reads,
                         business_key_bit_reads=controller.business_key_bit_reads,
                         final_certificate=getattr(controller, 'certificate', None),
                         control_events=controller.all_events(),
                         contender_boundary_attempts=len(boundaries),
                         refused_contender_commands=refused_commands,
                         next_admitted_bind_commands=next_commands,
                         members=G.members, candidates=len(G.H),
                         additional_members=0, additional_candidates=0))
        if hasattr(controller, 'region'):
            rows[-1]['final_region'] = controller.region.metrics()
    return dict(mode='protected', rows=rows, assertions=CHECKS,
                coverage='Two gate phases; a separate complete contender bind at every body boundary; actual handoff')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('costs', 'regressions', 'path_tradeoffs', 'audit1', 'audit2', 'omissions', 'protected'))
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
