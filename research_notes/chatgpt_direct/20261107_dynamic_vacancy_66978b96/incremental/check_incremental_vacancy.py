"""Invocation-local maintenance of vacancy evidence on the pinned triadic core.

Production control observes only complete Boolean outputs of inherited read
words, or the decoded code returned by the inherited addressed/dispatch program.
The full request table appears only in the verification functions below.

Strategies:
  fresh       reacquire the parent universal certificate at every free reserve;
  holes       retain H, remove newly bound residues, reacquire on a target miss;
  prefixes    as holes, with shared per-identity observed low-prefix memory.

All strategies use the same unmodified Compiler and triadic member inventory.
The memory lasts for one caller-owned stable interval; arbitrary outside writes
are excluded by that interval's existing ownership mechanism.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent / 'parent_bundle'
sys.path.insert(0, str(PARENT))
import check_batch_vacancy as prior

base, p, m, e, r = prior.base, prior.p, prior.m, prior.e, prior.r
ONE, ZERO = prior.ONE, prior.ZERO
STRATEGIES = ('fresh', 'holes', 'prefixes')
CHECKS = 0


def ck(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


@dataclass(eq=False)
class Prefix:
    """One live identity class; copies share this same record."""
    depth: int = 0
    value: int = 0
    initial_slot: int | None = None

    def accept(self, bit, value):
        if bit != self.depth:
            raise ValueError('A new observation must extend the known prefix')
        self.value |= int(value) << bit
        self.depth += 1

    def complete(self, code, width):
        if code % (1 << self.depth) != self.value:
            raise ValueError('Business read disagrees with the maintained prefix')
        self.depth = width
        self.value = code % (1 << width)


class Controller:
    """Explicit finite control memory; no matching/request-table decoder."""

    def __init__(self, compiler, strategy='prefixes'):
        if strategy not in STRATEGIES:
            raise ValueError(strategy)
        self.C = compiler
        self.strategy = strategy
        self.holes = None
        self.labels = ([Prefix(initial_slot=i) for i in range(compiler.slots)]
                       if strategy == 'prefixes' else None)
        self.vacancy_bit_reads = 0
        self.cached_bit_uses = 0
        self.business_key_bit_reads = 0
        self.certifications = 0
        self.commands = 0
        self.api_calls = 0
        self.max_live_labels = compiler.slots if self.labels is not None else 0
        self.max_known_low_bits = 0

    def memory_metrics(self):
        live = set(self.labels or ())
        self.max_live_labels = max(self.max_live_labels, len(live))
        self.max_known_low_bits = max(self.max_known_low_bits,
                                      sum(label.depth for label in live))
        return dict(live_labels=len(live),
                    known_low_bits=sum(label.depth for label in live),
                    label_pointers=0 if self.labels is None else len(self.labels),
                    certificate_residues=len(self.holes or ()))

    def step(self, J, op, *, trace=False, repeats=1, omitted=()):
        """Run one operation while retaining only this interval's observations."""
        C = self.C
        words, logs, observations = [], [], []
        mass = e.prep(J)
        omitted = set(omitted)
        vacancy_before = self.vacancy_bit_reads
        cached_before = self.cached_bit_uses
        business_before = self.business_key_bit_reads
        certificates_before = self.certifications
        old_query_pairs = []

        def do(block):
            nonlocal J, mass
            offset = len(words)
            expanded = tuple(raw for raw in block for _ in range(repeats))
            local = {x-offset for x in omitted if offset <= x < offset+len(expanded)}
            J, weight, records = C.runword(J, expanded, trace, local)
            mass = r.serial(mass, weight)
            if trace:
                logs.extend(dict(row, position=row['position']+offset) for row in records)
            words.extend(expanded)

        def acquire():
            nonlocal J, mass
            state = prior.start_search(C.slots)
            # Search-cache hits do not write the physical answer register.
            # Keep its last REAL value, beginning with successful free_reads.
            actual_last = int(C.observe_result(J))
            while state.task is not None:
                slot = state.task.active[state.at]
                bit = state.task.level
                label = None if self.labels is None else self.labels[slot]
                if label is not None and bit < label.depth:
                    value = (label.value >> bit) & 1
                    self.cached_bit_uses += 1
                    observations.append(('cached_request_bit', slot, bit, value))
                else:
                    do(C.reads[slot, bit])
                    value = int(C.observe_result(J))
                    actual_last = value
                    self.vacancy_bit_reads += 1
                    observations.append(('request_key_bit', slot, bit, value))
                    if label is not None:
                        if label.initial_slot is None:
                            raise ValueError('A controlled new identity must already be known')
                        old_query_pairs.append((label.initial_slot, bit))
                        label.accept(bit, value)
                state = prior.accept_bit(state, value, C.color_bits)
            self.holes = state.holes
            self.certifications += 1
            return actual_last

        entry = dict(op=tuple(op))
        if op[0] == 'reserve':
            target = op[1]
            do(C.free_reads[target])
            available = bool(C.observe_result(J))
            observations.append(('target_available', target, int(available)))
            entry.update(answer=available, color=None, key=None)
            if available:
                covered = (self.holes is not None and
                           any(C.key(target, color) % C.modulus in self.holes
                               for color in range(C.colors)))
                last = acquire() if self.strategy == 'fresh' or not covered else 1
                color = prior.select_color(C, target, self.holes)
                do(C.create_words[target, color, last])
                entry.update(color=color, key=C.key(target, color),
                             physical_last_before_create=last)
        elif op[0] in ('bind', 'copy'):
            J, weight, data = C.addressed(J, op, trace, repeats, omitted)
            mass = r.serial(mass, weight)
            words.extend(data['word'])
            logs.extend(data['trace'])
            observations.extend(data['observations'])
            self.business_key_bit_reads += sum(row[0] in ('shared_low_bit', 'reference_key_bit')
                                                for row in data['observations'])
            if op[0] == 'bind':
                code = data['code']
                entry['observed_business_code'] = code
                if self.holes is not None:
                    self.holes = tuple(h for h in self.holes if h != code % C.modulus)
                if self.labels is not None:
                    self.labels[op[1]] = Prefix(C.color_bits, code % C.modulus)
            elif op[1] != op[2] and self.labels is not None:
                # The existing full-key copy word supplies this observed code.
                source_label = self.labels[op[2]]
                source_label.complete(data['code'], C.color_bits)
                self.labels[op[1]] = source_label
                entry['observed_business_code'] = data['code']
        elif op[0] in ('valid', 'execute'):
            J, weight, data = C.dispatch(J, op[1], trace, delete=op[0] == 'execute',
                                         repeats=repeats, omitted=omitted)
            mass = r.serial(mass, weight)
            words.extend(data['word'])
            logs.extend(data['trace'])
            observations.extend(data['observations'])
            self.business_key_bit_reads += C.bits
            if self.labels is not None:
                self.labels[op[1]].complete(data['code'], C.color_bits)
            entry['observed_business_code'] = data['code']
        else:
            do(C.programs[tuple(op)])
            if op[0] == 'drop' and self.labels is not None:
                self.labels[op[1]] = Prefix(C.color_bits, 0)

        self.commands += len(words)
        self.api_calls += 1
        entry.update(answer=bool(C.observe_result(J)), commands=len(words),
                     vacancy_bit_reads=self.vacancy_bit_reads-vacancy_before,
                     cached_bit_uses=self.cached_bit_uses-cached_before,
                     business_key_bit_reads=self.business_key_bit_reads-business_before,
                     certificates=self.certifications-certificates_before,
                     holes=self.holes, memory=self.memory_metrics(),
                     old_query_pairs=tuple(old_query_pairs), observations=tuple(observations),
                     word=tuple(words), trace=logs)
        return J, mass, entry

    def summary(self):
        return dict(strategy=self.strategy, api_calls=self.api_calls,
                    commands=self.commands, vacancy_bit_reads=self.vacancy_bit_reads,
                    cached_bit_uses=self.cached_bit_uses,
                    business_key_bit_reads=self.business_key_bit_reads,
                    certifications=self.certifications,
                    max_live_labels=self.max_live_labels,
                    max_known_low_bits=self.max_known_low_bits,
                    final_holes=self.holes)


# Verification below may decode full preparations; production control above
# receives only J, static API arguments, and observations of inherited programs.
def expected_selected(C, table, cache, op, entry):
    if op[0] != 'reserve':
        return prior.parent.expected(C, table, cache, op)
    current, refs = table
    target = op[1]
    allowed = not any(current[s] is not None for s in C.conflicts[target])
    ck(entry['answer'] == allowed, 'source conflict answer')
    if not allowed:
        return table, False, cache
    color = entry['color']
    ck((target, color) not in refs, 'selected identity avoids every retained request')
    current = list(current)
    current[target] = color
    cache = list(cache)
    cache[target] = C.key(target, color)
    return (tuple(current), refs), True, tuple(cache)


def verify_memory(C, controller, table):
    keys = tuple(0 if row is None else C.key(*row) for row in table[1])
    if controller.holes is not None:
        ck(not set(controller.holes) & {key % C.modulus for key in keys if key},
           'certificate remains absent from every nonempty request')
    if controller.labels is not None:
        exact_by_label = {}
        for key, label in zip(keys, controller.labels):
            ck(0 <= label.depth <= C.color_bits, 'prefix depth within low width')
            ck(label.value == key % (1 << label.depth), 'retained prefix agrees with actual request')
            exact_by_label.setdefault(label, set()).add(key)
        ck(all(len(codes) == 1 for codes in exact_by_label.values()),
           'shared labels refer to the same exact request identity')
        ck(len(exact_by_label) <= C.slots, 'live label storage bounded by slot count')
        ck(controller.vacancy_bit_reads <= C.slots*C.color_bits,
           'cumulative additional vacancy reads bounded by r times b')


def run_case(C, table, operations, strategy, *, cache=None, trace=False,
             repeats=1, omitted=(), check=True):
    controller = Controller(C, strategy)
    cache = C.initial_cache(table) if cache is None else tuple(cache)
    J = C.encode(table, False, cache)
    mass = e.prep(J)
    original_table = table
    entries, forms, word, logs = [], [], [], []
    old_pairs = set()
    for op in operations:
        offset = len(word)
        J, weight, entry = controller.step(J, op, trace=trace, repeats=repeats,
                                            omitted={x-offset for x in omitted if x >= offset})
        mass = r.serial(mass, weight)
        if check:
            table, answer, cache = expected_selected(C, table, cache, op, entry)
            ck(J == C.encode(table, answer, cache),
               'whole matching: source, current records, both identity indexes, answer, clean scratch')
            verify_memory(C, controller, table)
            for pair in entry['old_query_pairs']:
                ck(pair not in old_pairs, 'no repeated additional read of an initial identity bit')
                old_pairs.add(pair)
            forms.append((base.canon(C, table), answer))
        entries.append({k: v for k, v in entry.items() if k not in ('word', 'trace')})
        word.extend(entry['word'])
        if trace:
            logs.extend(dict(row, position=row['position']+offset) for row in entry['trace'])
    return J, mass, dict(**controller.summary(), entries=entries, initial_table=original_table,
                         final_table=table if check else None, semantic_prefixes=forms,
                         word=tuple(word), trace=logs, extra_old_bit_pairs=sorted(old_pairs))


def compact(data, keep_entries=0):
    result = {k: v for k, v in data.items() if k not in ('word', 'trace', 'semantic_prefixes', 'entries')}
    if keep_entries:
        result['entries'] = data['entries'][:keep_entries]
    return result


def compare(C, table, operations, *, keep_entries=0):
    rows = []
    forms = None
    for strategy in STRATEGIES:
        _, weight, result = run_case(C, table, operations, strategy)
        if forms is None:
            forms = result['semantic_prefixes']
        else:
            ck(result['semantic_prefixes'] == forms, 'same business semantics after each operation')
        ck(weight.count == 1, 'one retained positive-CWM execution path')
        rows.append(compact(result, keep_entries))
    return rows


def costs():
    rows = []
    inventories = []
    for slots in (6, 7):
        C = prior.Compiler(slots=slots)
        inventories.append(dict(slots=slots, targets=C.d, members=C.members,
                                candidates=len(C.H), additional_members=0, additional_candidates=0))
        table = ((None,)*C.d, tuple((0, color) for color in range(slots)))
        for rounds in (1, 2, 8, 32):
            operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*rounds
            rows.append(dict(scenario='overwrite_one_slot', slots=slots, rounds=rounds,
                             strategies=compare(C, table, operations, keep_entries=6 if rounds==8 else 0)))
    C = prior.Compiler(slots=6)
    table = ((None,)*C.d, tuple((0, color) for color in range(6)))
    operations = tuple(op for k in range(12) for op in (
        ('reserve', 0), ('reserve', 2), ('reserve', 1),
        ('bind', k % 6, 0), ('copy', (k+1) % 6, k % 6),
        ('bind', (k+2) % 6, 2), ('release', 1), ('release', 4)))
    rows.append(dict(scenario='two_coexisting_targets_with_copy', slots=6, rounds=12,
                     strategies=compare(C, table, operations, keep_entries=16)))
    H = tuple((3*i+1, 3*i+2, 3*i+3) for i in range(8))
    C = prior.Compiler(slots=6, H=H)
    table = ((None,)*8, tuple((0, color) for color in range(6)))
    operations = tuple(op for k in range(3) for target in range(8) for op in (
        ('reserve', target), ('bind', target % 6, target), ('release', 3*target+1)))
    rows.append(dict(scenario='eight_disjoint_targets', slots=6, rounds=3,
                     strategies=compare(C, table, operations, keep_entries=8)))
    inventories.append(dict(slots=6, targets=8, members=C.members, candidates=len(C.H),
                            additional_members=0, additional_candidates=0))
    return dict(mode='costs', rows=rows, inventories=inventories, assertions=CHECKS,
                counting='All primitive command attempts; extra vacancy reads and inherited business key reads reported separately')


def regressions():
    C = prior.Compiler(slots=6)
    empty = ((None,)*C.d, (None,)*C.slots)
    saturation = ((None,)*C.d, tuple((0, color) for color in range(C.slots)))
    cases = {
        'old_request_stays_stale': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', 0))),
        'copy_then_overwrite_source_slot': (saturation, (
            ('reserve', 0), ('copy', 1, 0), ('bind', 0, 0), ('release', 1),
            ('reserve', 0), ('valid', 1), ('drop', 0), ('drop', 1),
            ('release', 1), ('reserve', 0))),
        'empty_bind_ignores_stale_shared_key': (saturation, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1), ('bind', 0, 0),
            ('reserve', 0), ('copy', 0, 0), ('same', 0, 0))),
        'source_conflicts': (((None, None, 0), tuple((0, c) for c in range(6))), (
            ('reserve', 0), ('reserve', 1), ('reserve', 2), ('bind', 0, 0),
            ('copy', 1, 0), ('release', 1), ('reserve', 0), ('valid', 1))),
        'read_only_business_feedback_teaches_prefix': (saturation, (
            ('valid', 4), ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0))),
    }
    rows = []
    for name, (table, operations) in cases.items():
        rows.append(dict(name=name, strategies=compare(C, table, operations, keep_entries=20)))
    # The public successful answer must track the physical output, even when
    # the last bit consumed by the search comes entirely from cached control.
    table = saturation
    operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*3 + (('reserve', 0),)
    _, _, result = run_case(C, table, operations, 'prefixes')
    cached_creations = [entry for entry in result['entries']
                        if entry['op'][0]=='reserve' and entry['cached_bit_uses'] and not entry['vacancy_bit_reads']]
    ck(bool(cached_creations), 'regression reaches an all-cache acquisition')
    ck(all(entry['answer'] and entry['physical_last_before_create']==1 for entry in cached_creations),
       'all-cache acquisition preserves free-read true before creation')
    rows.append(dict(name='physical_answer_after_all_cache_search',
                     creations=cached_creations, totals=compact(result)))
    # Exact reached failure of treating the last cached bit as the live output.
    codes = (0, 18, 9, 20, 10, 8)
    table = ((None,)*3, tuple(None if code == 0 else divmod(code-1, C.colors) for code in codes))
    controller = Controller(C, 'prefixes')
    J = C.encode(table, False)
    prefix_ops = (('reserve', 0), ('bind', 0, 0), ('release', 1))*2
    for op in prefix_ops:
        J, _, _ = controller.step(J, op)
    before = J
    good, _, entry = controller.step(before, ('reserve', 0))
    ck(entry['physical_last_before_create'] == 0 and entry['observations'][-1] ==
       ('cached_request_bit', 0, 2, 1), 'reached physical-zero versus cached-one mismatch')
    ck(entry['word'][-4:] == tuple(C.clearout()+[p.add(h) for h in p.reg(C.out, 1)]),
       'successful creation needs the actual false-to-true correction')
    wrong, _, _ = C.runword(before, entry['word'][:-4])
    good_table, good_answer = C.decode(good)
    wrong_table, wrong_answer = C.decode(wrong)
    ck(good_table == wrong_table and good_answer and not wrong_answer,
       'using final cached-one would create the right identity but falsely return failure')
    rows.append(dict(name='last_cached_bit_is_not_physical_answer', initial_request_keys=codes,
                     prefix_operations=prefix_ops, operation=('reserve', 0),
                     selected_key=entry['key'], physical_last=0, last_cached_bit=1,
                     corrected_answer=good_answer, uncorrected_answer=wrong_answer,
                     correct_commands=len(entry['word']), uncorrected_commands=len(entry['word'])-4))
    # Existing C event must keep its original creation identity at every prefix.
    table, operations = cases['source_conflicts']
    J, _, result = run_case(C, table, operations, 'prefixes', trace=True)
    state = base.ref.old.seed(C.encode(table, False))
    protected = state.names()[C.targets[2]]
    for row in result['trace']:
        state, _, _ = base.ref.old.raw_step(state, row['command'], C.H)
        ck(state.names().get(C.targets[2]) == protected, 'unrelated source creation survives every raw prefix')
    ck(state.matching == J, 'birth-labelled replay matches the full actual endpoint')
    return dict(mode='regressions', rows=rows, protected_source_raw_prefixes=len(result['word']),
                assertions=CHECKS)


def audit(slots=1, start=0, stop=None):
    C = prior.Compiler(slots=slots)
    domain = base.domain(C)
    stop = len(domain) if stop is None else min(stop, len(domain))
    j = min(1, slots-1)
    sequences = (
        (('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', 0)),
        (('reserve', 0), ('copy', j, 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', j)),
        (('reserve', 2), ('bind', j, 2), ('copy', 0, j), ('drop', j), ('release', 4), ('reserve', 2)),
        (('reserve', 0), ('reserve', 1), ('reserve', 2), ('bind', 0, 0), ('execute', 0), ('reserve', 0)),
    )
    mass = ZERO
    sequences_run = api_calls = 0
    for index in range(start, stop):
        table = domain[index]
        cache = tuple(C.key(t,c) if c is not None else (5*index+3*t+1) % (1<<C.bits)
                      for t,c in enumerate(table[0]))
        for operations in sequences:
            _, weight, result = run_case(C, table, operations, 'prefixes', cache=cache)
            mass = r.merge(mass, weight)
            sequences_run += 1
            api_calls += len(operations)
    ck(mass.count == sequences_run, 'CWM retains each exact preparation-sequence path')
    return dict(mode='audit', slots=slots, domain=len(domain), slice=[start, stop],
                sequences=sequences, sequences_run=sequences_run, api_calls=api_calls,
                CWM=e.cw(mass), assertions=CHECKS, members=C.members, candidates=len(C.H),
                kernel_cache_misses=C.calls, primitive_uses=C.uses)


def omissions():
    C = prior.Compiler(slots=1)
    table = ((None,)*3, (None,))
    operations = (('reserve', 0), ('bind', 0, 0), ('release', 1),
                  ('reserve', 0), ('valid', 0))
    want, _, baseline = run_case(C, table, operations, 'prefixes', repeats=2)
    mass = ZERO
    for position in range(len(baseline['word'])):
        got, weight, result = run_case(C, table, operations, 'prefixes', repeats=2, omitted=(position,))
        ck(got == want, 'one omitted attempt with two adjacent copies has exact endpoint')
        ck(result['word'] == baseline['word'], 'omission preserves all adaptive branch decisions')
        mass = r.merge(mass, weight)
    ck(mass.count == len(baseline['word']), 'every single-omission position retained')
    return dict(mode='omissions', repeats=2, omission_budget=1,
                raw_attempts=len(baseline['word']), omission_positions=len(baseline['word']),
                CWM=e.cw(mass), assertions=CHECKS,
                scope='Every single omitted original-command attempt on this one mixed invocation; sequential body')


def protected():
    """Actual inherited entry/body/publication, with bounded contender probes."""
    import check_batch_integration as integration
    gate = integration.gate

    class MixedRing(integration.BatchRing):
        def begin(self, jobs, k, route):
            if k < len(jobs) and jobs[k][0] == 'mixed':
                return gate.PC('mixed', k, route=route)
            return super().begin(jobs, k, route)

        def body(self, node, actor, jobs, *, strategy='prefixes', trace=False):
            pc = node.pcs[actor]
            if pc.phase != 'mixed':
                raise ValueError('Mixed body begins after the inherited entry and phase read')
            controller = Controller(self.C, strategy)
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
        G = MixedRing(slots=6)
        table = ((None,)*3, tuple((0, color) for color in range(6)))
        operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*4 + (('reserve', 0),)
        jobs = ((('mixed', operations),), (('bind', 5, 0),))
        node = G.initial_node(table, phase=phase)
        entry_commands = 0
        grants = []
        while node.pcs[0].phase != 'mixed':
            node, _, _, grant = G.next(node, 0, jobs)
            if grant:
                grants.append(0)
            entry_commands += 1
        held = node
        ck(G.lock(0) in held.J, 'actual inherited entry acquired the persistent token')
        node, controller, entries, words, logs = G.body(node, 0, jobs, trace=True)
        cache = G.C.initial_cache(table)
        for op, entry in zip(operations, entries):
            table, answer, cache = expected_selected(G.C, table, cache, op, entry)
        extras = tuple(h for h in held.J if h not in G.C.H)
        ck(node.J == m.canon(G.C.encode(table, answer, cache)+extras),
           'mixed body preserves the complete gate and private-register state')
        boundaries = [held.J]+[row['after'] for row in logs]
        refused_attempts = refused_commands = 0
        for state in boundaries:
            ck(G.lock(0) in state, 'holder token survives each original-command prefix')
            # A separate complete contender entry at each boundary; this is
            # finite coverage of these attempts, not an all-interleavings graph.
            probe = replace(held, J=state)
            blocked, count, admitted = gate.complete(G, probe, 1, jobs)
            ck(admitted == () and blocked.pcs[1].phase == 'busy',
               'contender bind cannot enter the mixed stable interval')
            ck(tuple(h for h in blocked.J if h in G.C.H) ==
               tuple(h for h in state if h in G.C.H),
               'refused contender preserves every core relation')
            refused_attempts += 1
            refused_commands += count
        node, exit_commands, more = gate.complete(G, node, 0, jobs)
        ck(more == (), 'publication and handoff do not regrant the holder')
        ck(gate.old.bit(node.J, G.lanes[0].reply) == answer,
           'last mixed answer is delivered to the private reply register')
        node, next_commands, admitted = gate.complete(G, node, 1, jobs)
        ck(admitted == (1,), 'contender binds after actual handoff')
        table, next_answer, cache = prior.parent.expected(G.C, table, cache, jobs[1][0])
        want = G.C.encode(table, next_answer, cache)
        answers = (answer, next_answer)
        for actor, lane in enumerate(G.lanes):
            want = m.canon(want+p.reg(lane.admitted, 1)+p.reg(lane.reply, int(answers[actor])))
            if actor != node.turn:
                want = m.canon(want+(G.gate_pair[actor][phase^1],))
        ck(node.J == want, 'whole final source, requests, keys, cyclic gates, replies and cleanup')
        ck(entry_commands+exit_commands == 31, 'one inherited protection wrapper per mixed interval')
        rows.append(dict(phase=phase, body_operations=operations, body_commands=len(words),
                         wrapper_commands=entry_commands+exit_commands,
                         protected_invocation_commands=entry_commands+len(words)+exit_commands,
                         vacancy_bit_reads=controller.vacancy_bit_reads,
                         business_key_bit_reads=controller.business_key_bit_reads,
                         contender_boundary_attempts=refused_attempts,
                         refused_contender_commands=refused_commands,
                         next_admitted_bind_commands=next_commands,
                         members=G.members, candidates=len(G.H),
                         additional_members=0, additional_candidates=0))
    return dict(mode='protected', rows=rows, assertions=CHECKS,
                coverage='Two inherited gate phases; each body boundary receives one separate complete competing bind attempt; one actual subsequent handoff and bind')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('costs', 'regressions', 'audit', 'omissions', 'protected'))
    parser.add_argument('--slots', type=int, default=1)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--stop', type=int)
    parser.add_argument('--out')
    args = parser.parse_args()
    answer = (audit(args.slots, args.start, args.stop) if args.mode=='audit'
              else globals()[args.mode]())
    text = json.dumps(answer, ensure_ascii=False, indent=2) + '\n'
    if args.out:
        Path(args.out).write_text(text)
    else:
        print(text)


if __name__ == '__main__':
    main()
