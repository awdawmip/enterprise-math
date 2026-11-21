"""Target-directed vacancy evidence on a maintained observation-prefix tree.

The production controller uses only inherited complete Boolean reads and the
actual identity output of inherited business words.  Full request tables appear
only below the verification boundary.  The parent programs are unmodified.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'incremental'))
import check_incremental_vacancy as old

prior, base, p, m, e, r = old.prior, old.base, old.p, old.m, old.e, old.r
ONE, ZERO = old.ONE, old.ZERO
CHECKS = 0


def ck(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


@dataclass(eq=False)
class Label:
    depth: int
    value: int
    representative: int
    refs: int = 1
    initial_slot: int | None = None
    previous: Label | None = None
    following: Label | None = None


class PrefixTree:
    """Finite arrays plus intrusive lists: no scan to find a live representative.

    A label is in the bucket of its deepest observed prefix.  count[node] is
    the number of distinct live labels in this node's entire subtree.  Copies
    share a label; initially equal but unobserved identities may remain distinct.
    """

    def __init__(self, slots, width):
        self.slots, self.width = slots, width
        self.modulus = 1 << width
        self.offsets = tuple((1 << level)-1 for level in range(width+1))
        size = 2*self.modulus-1
        self.count = [0]*size
        self.head = [None]*size
        self.tail = [None]*size
        self.labels = [None]*slots
        self.slot_next = list(range(slots))
        self.slot_previous = list(range(slots))
        self.live_labels = 0
        self.known_bits = 0
        self.max_live_labels = 0
        self.max_known_bits = 0
        self.events = dict(initial_labels=0, initial_node_cells=size,
                           query_label_moves=0, query_count_updates=0,
                           business_path_touches=0, business_label_completions=0,
                           bucket_removals=0, bucket_insertions=0,
                           slot_detaches=0, slot_attaches=0,
                           retired_labels=0, known_labels_introduced=0)
        for slot in range(slots):
            label = Label(0, 0, slot, initial_slot=slot)
            self.labels[slot] = label
            self._append(label)
            self.count[0] += 1
            self.live_labels += 1
            self.events['initial_labels'] += 1
        self._peaks()

    def index(self, level, prefix):
        return self.offsets[level]+prefix

    def _peaks(self):
        self.max_live_labels = max(self.max_live_labels, self.live_labels)
        self.max_known_bits = max(self.max_known_bits, self.known_bits)

    def _append(self, label):
        index = self.index(label.depth, label.value)
        previous = self.tail[index]
        label.previous, label.following = previous, None
        if previous is None:
            self.head[index] = label
        else:
            previous.following = label
        self.tail[index] = label
        self.events['bucket_insertions'] += 1

    def _unlink(self, label):
        index = self.index(label.depth, label.value)
        previous, following = label.previous, label.following
        if previous is None:
            self.head[index] = following
        else:
            previous.following = following
        if following is None:
            self.tail[index] = previous
        else:
            following.previous = previous
        label.previous = label.following = None
        self.events['bucket_removals'] += 1

    def observe_next(self, label, value):
        """One actual new bit: old ancestor counts remain unchanged."""
        if label.depth >= self.width or value not in (0, 1):
            raise ValueError('Expected one unobserved low-prefix bit')
        self._unlink(label)
        label.value |= value << label.depth
        label.depth += 1
        self._append(label)
        self.count[self.index(label.depth, label.value)] += 1
        self.known_bits += 1
        self.events['query_label_moves'] += 1
        self.events['query_count_updates'] += 1
        self._peaks()

    def complete(self, label, code):
        """Consume a full key actually returned by a business program."""
        value = code % self.modulus
        if value % (1 << label.depth) != label.value:
            raise ValueError('Actual business read disagrees with cached prefix')
        depth = label.depth
        if depth == self.width:
            return
        self._unlink(label)
        for level in range(depth+1, self.width+1):
            self.count[self.index(level, value % (1 << level))] += 1
            self.events['business_path_touches'] += 1
        label.depth, label.value = self.width, value
        self._append(label)
        self.known_bits += self.width-depth
        self.events['business_label_completions'] += 1
        self._peaks()

    def _detach(self, slot):
        label = self.labels[slot]
        if label.refs == 1:
            self._unlink(label)
            for level in range(label.depth+1):
                self.count[self.index(level, label.value % (1 << level))] -= 1
                self.events['business_path_touches'] += 1
            self.live_labels -= 1
            self.known_bits -= label.depth
            self.events['retired_labels'] += 1
            label.refs = 0
            label.representative = -1
        else:
            previous, following = self.slot_previous[slot], self.slot_next[slot]
            self.slot_next[previous] = following
            self.slot_previous[following] = previous
            label.refs -= 1
            if label.representative == slot:
                label.representative = following
        self.labels[slot] = None
        self.slot_previous[slot] = self.slot_next[slot] = slot
        self.events['slot_detaches'] += 1

    def known_write(self, slot, code):
        self._detach(slot)
        value = code % self.modulus
        label = Label(self.width, value, slot)
        self.labels[slot] = label
        self._append(label)
        for level in range(self.width+1):
            self.count[self.index(level, value % (1 << level))] += 1
            self.events['business_path_touches'] += 1
        self.live_labels += 1
        self.known_bits += self.width
        self.events['known_labels_introduced'] += 1
        self.events['slot_attaches'] += 1
        self._peaks()

    def copy(self, destination, source, code):
        if destination == source:
            return
        label = self.labels[source]
        self.complete(label, code)
        self._detach(destination)
        head = label.representative
        tail = self.slot_previous[head]
        self.slot_next[tail] = destination
        self.slot_previous[destination] = tail
        self.slot_next[destination] = head
        self.slot_previous[head] = destination
        label.refs += 1
        self.labels[destination] = label
        self.events['slot_attaches'] += 1
        self._peaks()

    def metrics(self):
        return dict(live_labels=self.live_labels, known_low_bits=self.known_bits,
                    allocated_prefix_nodes=len(self.count), label_pointers=self.slots)


class Controller:
    """One safe witness plus a persistent, actual-observation prefix tree."""

    def __init__(self, compiler):
        self.C = compiler
        self.tree = PrefixTree(compiler.slots, compiler.color_bits)
        self.witness = None
        self.vacancy_bit_reads = self.business_key_bit_reads = 0
        self.commands = self.api_calls = 0
        self.events = dict(witness_checks=0, witness_hits=0, target_searches=0,
                           query_node_visits=0, candidate_count_queries=0,
                           selected_branches=0)

    @staticmethod
    def capacity(start, colors, level, prefix):
        first = (prefix-start) % (1 << level)
        count = 0 if first >= colors else 1+(colors-1-first)//(1 << level)
        return count, first

    def all_events(self):
        return dict(**self.events, **self.tree.events)

    def step(self, J, op, *, trace=False, repeats=1, omitted=()):
        C = self.C
        words, logs, observations, branches, old_query_pairs = [], [], [], [], []
        mass = e.prep(J)
        omitted = set(omitted)
        before = self.all_events()
        vacancy_before = self.vacancy_bit_reads
        business_before = self.business_key_bit_reads

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

        def select(target):
            """Return one legal color and the last PHYSICAL Boolean output."""
            start = C.key(target, 0) % C.modulus
            self.events['witness_checks'] += 1
            if self.witness is not None:
                color = (self.witness-start) % C.modulus
                if color < C.colors:
                    self.events['witness_hits'] += 1
                    return color, 1
            self.events['target_searches'] += 1
            level = prefix = 0
            capacity = C.colors
            first = 0
            actual_last = int(C.observe_result(J))
            while True:
                index = self.tree.index(level, prefix)
                blockers = self.tree.count[index]
                self.events['query_node_visits'] += 1
                if capacity <= blockers:
                    raise ValueError('Target-directed vacancy deficit was lost')
                if blockers == 0:
                    return first, actual_last
                if level == C.color_bits:
                    raise ValueError('Occupied singleton cannot have a deficit')
                # Only this bucket is unclassified at this level.  Descendant
                # buckets already have observed bits and never replay them.
                while self.tree.head[index] is not None:
                    label = self.tree.head[index]
                    slot = label.representative
                    do(C.reads[slot, level])
                    value = actual_last = int(C.observe_result(J))
                    observations.append(('request_key_bit', slot, level, value))
                    if label.initial_slot is None:
                        raise ValueError('Controlled new identities are already fully known')
                    old_query_pairs.append((label.initial_slot, level))
                    self.vacancy_bit_reads += 1
                    self.tree.observe_next(label, value)
                eligible, counts, capacities = [], [], []
                for bit in (0, 1):
                    child_prefix = prefix | (bit << level)
                    n = self.tree.count[self.tree.index(level+1, child_prefix)]
                    cap, child_first = self.capacity(start, C.colors, level+1, child_prefix)
                    self.events['candidate_count_queries'] += 1
                    counts.append(n)
                    capacities.append(cap)
                    if n < cap:
                        eligible.append((n, bit, cap, child_first))
                if not eligible:
                    raise ValueError('No deficient child after actual classification')
                n, bit, capacity, first = min(eligible)
                branches.append(dict(level=level, prefix=prefix,
                                     label_counts=tuple(counts),
                                     candidate_counts=tuple(capacities),
                                     selected_bit=bit))
                self.events['selected_branches'] += 1
                prefix |= bit << level
                level += 1

        entry = dict(op=tuple(op))
        if op[0] == 'reserve':
            target = op[1]
            do(C.free_reads[target])
            available = bool(C.observe_result(J))
            observations.append(('target_available', target, int(available)))
            entry.update(color=None, key=None)
            if available:
                color, last = select(target)
                do(C.create_words[target, color, last])
                key = C.key(target, color)
                self.witness = key % C.modulus
                entry.update(color=color, key=key, physical_last_before_create=last)
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
                if code % C.modulus == self.witness:
                    self.witness = None
                self.tree.known_write(op[1], code)
                entry['observed_business_code'] = code
            elif op[1] != op[2]:
                self.tree.copy(op[1], op[2], data['code'])
                entry['observed_business_code'] = data['code']
        elif op[0] in ('valid', 'execute'):
            J, weight, data = C.dispatch(J, op[1], trace, delete=op[0] == 'execute',
                                         repeats=repeats, omitted=omitted)
            mass = r.serial(mass, weight)
            words.extend(data['word'])
            logs.extend(data['trace'])
            observations.extend(data['observations'])
            self.business_key_bit_reads += C.bits
            self.tree.complete(self.tree.labels[op[1]], data['code'])
            entry['observed_business_code'] = data['code']
        else:
            do(C.programs[tuple(op)])
            if op[0] == 'drop':
                self.tree.known_write(op[1], 0)

        self.commands += len(words)
        self.api_calls += 1
        after = self.all_events()
        entry.update(answer=bool(C.observe_result(J)), commands=len(words),
                     vacancy_bit_reads=self.vacancy_bit_reads-vacancy_before,
                     business_key_bit_reads=self.business_key_bit_reads-business_before,
                     witness=self.witness, memory=self.tree.metrics(),
                     control_events={key: after[key]-before[key] for key in after},
                     old_query_pairs=tuple(old_query_pairs), observations=tuple(observations),
                     branches=tuple(branches), word=tuple(words), trace=logs)
        return J, mass, entry

    def summary(self):
        return dict(strategy='directed', api_calls=self.api_calls, commands=self.commands,
                    vacancy_bit_reads=self.vacancy_bit_reads,
                    business_key_bit_reads=self.business_key_bit_reads,
                    control_events=self.all_events(), final_witness=self.witness,
                    max_live_labels=self.tree.max_live_labels,
                    max_known_low_bits=self.tree.max_known_bits,
                    allocated_prefix_nodes=len(self.tree.count))


# Verification boundary: only the functions below inspect the exact request table.
def verify_memory(C, controller, table):
    tree = controller.tree
    keys = tuple(0 if row is None else C.key(*row) for row in table[1])
    if controller.witness is not None:
        ck(controller.witness not in {key % C.modulus for key in keys if key},
           'safe witness excludes every nonempty request')
    refs, expected_counts, bucket_seen = {}, [0]*len(tree.count), set()
    for slot, (key, label) in enumerate(zip(keys, tree.labels)):
        refs.setdefault(label, []).append(slot)
        ck(label.value == key % (1 << label.depth), 'cached prefix matches actual request')
    ck(len(refs) == tree.live_labels <= C.slots, 'live label count')
    ck(sum(label.depth for label in refs) == tree.known_bits, 'known bit count')
    for label, slots in refs.items():
        ck(len(slots) == label.refs, 'label reference count')
        ck(len({keys[slot] for slot in slots}) == 1, 'shared label has one exact identity')
        ck(label.representative in slots, 'live representative slot')
        cycle, current = [], label.representative
        while current not in cycle:
            cycle.append(current)
            nxt = tree.slot_next[current]
            ck(tree.slot_previous[nxt] == current, 'intrusive slot links are inverse')
            current = nxt
        ck(current == label.representative and set(cycle) == set(slots), 'exact slot alias cycle')
        for level in range(label.depth+1):
            expected_counts[tree.index(level, label.value % (1 << level))] += 1
    ck(tree.count == expected_counts, 'every maintained subtree count matches live labels')
    for index in range(len(tree.count)):
        label, previous = tree.head[index], None
        while label is not None:
            ck(label not in bucket_seen, 'one observed-prefix bucket per label')
            bucket_seen.add(label)
            ck(tree.index(label.depth, label.value) == index, 'correct prefix bucket')
            ck(label.previous is previous, 'intrusive bucket previous pointer')
            previous, label = label, label.following
        ck(tree.tail[index] is previous, 'intrusive bucket tail')
    ck(bucket_seen == set(refs), 'all and only live labels are bucketed')
    ck(controller.vacancy_bit_reads <= C.slots*C.color_bits, 'cumulative extra reads <= rb')


def run_case(C, table, operations, *, cache=None, trace=False, repeats=1, omitted=(), check=True):
    controller = Controller(C)
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
            verify_memory(C, controller, table)
            for pair in entry['old_query_pairs']:
                ck(pair not in old_pairs, 'no repeated extra read of one initial label bit')
                old_pairs.add(pair)
            ck(entry['vacancy_bit_reads'] <= 2*C.slots-C.slots.bit_count(),
               'single search extra reads within inherited exact worst bound')
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
            row = {key: entry[key] for key in (
                'op', 'answer', 'key', 'commands', 'vacancy_bit_reads',
                'business_key_bit_reads', 'witness', 'old_query_pairs',
                'physical_last_before_create') if key in entry}
            row['control_events'] = {key: value for key, value in entry['control_events'].items() if value}
            result['first_steps'].append(row)
    return result


def compare(C, table, operations, *, keep_entries=0):
    rows, forms = [], None
    for strategy in old.STRATEGIES:
        _, weight, result = old.run_case(C, table, operations, strategy)
        if forms is None:
            forms = result['semantic_prefixes']
        else:
            ck(result['semantic_prefixes'] == forms, 'old strategy semantic equivalence')
        ck(weight.count == 1, 'one positive-CWM baseline path')
        row = old.compact(result)
        for key in ('initial_table', 'final_table', 'extra_old_bit_pairs'):
            row.pop(key, None)
        row['request_bit_inputs_to_search'] = row['vacancy_bit_reads']+row['cached_bit_uses']
        rows.append(row)
    _, weight, result = run_case(C, table, operations)
    ck(result['semantic_prefixes'] == forms, 'directed and prior future-relevant semantics agree')
    ck(weight.count == 1, 'one positive-CWM directed path')
    rows.append(compact(result, keep_entries))
    return rows


def costs():
    rows, inventories = [], []
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
                counting='All core primitive attempts; added vacancy reads, business identity reads and typed control events are separate')


def pure_creates():
    rows = []
    for slots in (6, 7):
        for target_count in (3, 8):
            H = base.H_DEFAULT if target_count == 3 else tuple(
                (3*i+1, 3*i+2, 3*i+3) for i in range(target_count))
            C = prior.Compiler(slots=slots, H=H)
            targets = (0, 2) if target_count == 3 else tuple(range(target_count))
            operations = tuple(('reserve', target) for target in targets)
            for preparation in ('empty', 'first_r_keys'):
                references = ((None,)*slots if preparation == 'empty' else
                              tuple((0, color) for color in range(slots)))
                table = ((None,)*target_count, references)
                _, old_weight, previous = old.run_case(C, table, operations, 'prefixes')
                _, new_weight, current = run_case(C, table, operations)
                ck(old_weight.count == new_weight.count == 1, 'one pure-create path per strategy')
                ck(previous['semantic_prefixes'] == current['semantic_prefixes'],
                   'pure-create strategies have the same future-relevant semantics')
                old_summary = old.compact(previous)
                for key in ('initial_table', 'final_table', 'extra_old_bit_pairs'):
                    old_summary.pop(key, None)
                old_summary['request_bit_inputs_to_search'] = (
                    previous['vacancy_bit_reads']+previous['cached_bit_uses'])
                rows.append(dict(slots=slots, target_count=target_count, preparation=preparation,
                                 target_sequence=targets, previous=old_summary,
                                 directed=compact(current, len(operations)),
                                 command_delta=current['commands']-previous['commands'],
                                 members=C.members, candidates=len(C.H),
                                 additional_members=0, additional_candidates=0))
    return dict(mode='pure_creates', rows=rows, assertions=CHECKS,
                scope='A,C or eight disjoint targets; slots 6/7; empty or first-r-key references')


def regressions():
    C = prior.Compiler(slots=6)
    empty = ((None,)*C.d, (None,)*C.slots)
    saturated = ((None,)*C.d, tuple((0, color) for color in range(C.slots)))
    cases = {
        'old_request_stays_stale': (empty, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', 0))),
        'copy_then_overwrite_representative': (saturated, (
            ('reserve', 0), ('copy', 1, 0), ('copy', 2, 0), ('bind', 0, 0),
            ('release', 1), ('reserve', 0), ('valid', 1), ('drop', 1),
            ('valid', 2), ('drop', 2), ('release', 1), ('reserve', 0))),
        'copy_within_same_alias_cycle': (saturated, (
            ('copy', 1, 0), ('copy', 2, 1), ('copy', 0, 2), ('copy', 1, 1),
            ('drop', 0), ('drop', 2), ('reserve', 0), ('valid', 1))),
        'empty_bind_ignores_stale_shared_key': (saturated, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1), ('bind', 0, 0),
            ('reserve', 0), ('copy', 0, 0), ('same', 0, 0))),
        'source_conflicts': (((None, None, 0), tuple((0, color) for color in range(6))), (
            ('reserve', 0), ('reserve', 1), ('reserve', 2), ('bind', 0, 0),
            ('copy', 1, 0), ('release', 1), ('reserve', 0), ('valid', 1))),
        'business_feedback_completes_label': (saturated, (
            ('valid', 4), ('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0))),
        'all_cached_no_read_search': (saturated, (
            ('reserve', 0), ('bind', 0, 0), ('release', 1))*4 + (('reserve', 0),)),
        'prior_physical_register_preparation': (((None,)*3, tuple(
            None if code == 0 else divmod(code-1, C.colors)
            for code in (0, 18, 9, 20, 10, 8))),
            (('reserve', 0), ('bind', 0, 0), ('release', 1))*2 + (('reserve', 0),)),
    }
    rows = [dict(name=name, strategies=compare(C, table, ops, keep_entries=20))
            for name, (table, ops) in cases.items()]
    _, _, cached = run_case(C, saturated, cases['all_cached_no_read_search'][1])
    zero_read_searches = [entry for entry in cached['entries']
                         if entry['op'][0] == 'reserve' and entry['answer']
                         and entry['control_events']['target_searches'] and not entry['vacancy_bit_reads']]
    ck(bool(zero_read_searches), 'reached maintained-tree search with zero new reads')
    ck(all(entry['physical_last_before_create'] == 1 for entry in zero_read_searches),
       'zero-read search preserves the actual successful availability output')
    table, ops = cases['source_conflicts']
    J, _, result = run_case(C, table, ops, trace=True)
    state = base.ref.old.seed(C.encode(table, False))
    protected = state.names()[C.targets[2]]
    for row in result['trace']:
        state, _, _ = base.ref.old.raw_step(state, row['command'], C.H)
        ck(state.names().get(C.targets[2]) == protected, 'original C creation survives every primitive prefix')
    ck(state.matching == J, 'birth-labelled replay matches actual endpoint')
    return dict(mode='regressions', rows=rows, protected_source_raw_prefixes=len(result['word']),
                zero_read_searches=len(zero_read_searches), assertions=CHECKS)


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
    mass, runs, api_calls = ZERO, 0, 0
    for index in range(start, stop):
        table = domain[index]
        cache = tuple(C.key(t, c) if c is not None else (5*index+3*t+1) % (1 << C.bits)
                      for t, c in enumerate(table[0]))
        for operations in sequences:
            _, weight, result = run_case(C, table, operations, cache=cache)
            mass = r.merge(mass, weight)
            runs += 1
            api_calls += len(operations)
    ck(mass.count == runs, 'positive CWM retains every preparation-sequence run')
    return dict(mode='audit', slots=slots, domain=len(domain), slice=[start, stop],
                sequences=sequences, sequences_run=runs, api_calls=api_calls,
                CWM=e.cw(mass), assertions=CHECKS, members=C.members, candidates=len(C.H),
                kernel_cache_misses=C.calls, primitive_uses=C.uses)


def omissions():
    C = prior.Compiler(slots=1)
    table = ((None,)*3, (None,))
    operations = (('reserve', 0), ('bind', 0, 0), ('release', 1), ('reserve', 0), ('valid', 0))
    want, _, baseline = run_case(C, table, operations, repeats=2)
    mass = ZERO
    for position in range(len(baseline['word'])):
        got, weight, result = run_case(C, table, operations, repeats=2, omitted=(position,))
        ck(got == want, 'one omitted attempt has exact endpoint with adjacent double repetition')
        ck(result['word'] == baseline['word'], 'omission preserves adaptive control branches')
        mass = r.merge(mass, weight)
    ck(mass.count == len(baseline['word']), 'all single omission positions counted')
    return dict(mode='omissions', repeats=2, omission_budget=1,
                raw_attempts=len(baseline['word']), omission_positions=len(baseline['word']),
                CWM=e.cw(mass), assertions=CHECKS,
                scope='Every one omitted primitive attempt on this specified sequential mixed invocation')


def protected():
    import check_batch_integration as integration
    gate = integration.gate

    class DirectedRing(integration.BatchRing):
        def begin(self, jobs, k, route):
            if k < len(jobs) and jobs[k][0] == 'mixed':
                return gate.PC('mixed', k, route=route)
            return super().begin(jobs, k, route)

        def body(self, node, actor, jobs, trace=False):
            pc = node.pcs[actor]
            controller = Controller(self.C)
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
        G = DirectedRing(slots=6)
        table = ((None,)*3, tuple((0, color) for color in range(6)))
        operations = (('reserve', 0), ('bind', 0, 0), ('release', 1))*4 + (('reserve', 0),)
        jobs = ((('mixed', operations),), (('bind', 5, 0),))
        node = G.initial_node(table, phase=phase)
        entry_commands = 0
        while node.pcs[0].phase != 'mixed':
            node, _, _, _ = G.next(node, 0, jobs)
            entry_commands += 1
        held = node
        ck(G.lock(0) in held.J, 'inherited real entry owns lock')
        node, controller, entries, words, logs = G.body(node, 0, jobs, trace=True)
        cache = G.C.initial_cache(table)
        for op, entry in zip(operations, entries):
            table, answer, cache = old.expected_selected(G.C, table, cache, op, entry)
        verify_memory(G.C, controller, table)
        extras = tuple(h for h in held.J if h not in G.C.H)
        ck(node.J == m.canon(G.C.encode(table, answer, cache)+extras), 'whole mixed body and gate state')
        boundaries = [held.J]+[row['after'] for row in logs]
        refused_commands = 0
        for state in boundaries:
            ck(G.lock(0) in state, 'holder lock survives each primitive boundary')
            blocked, count, admitted = gate.complete(G, replace(held, J=state), 1, jobs)
            ck(admitted == () and blocked.pcs[1].phase == 'busy', 'contender blocked before actual handoff')
            ck(tuple(h for h in blocked.J if h in G.C.H) == tuple(h for h in state if h in G.C.H),
               'refused contender preserves all core relations')
            refused_commands += count
        node, exit_commands, more = gate.complete(G, node, 0, jobs)
        ck(more == (), 'publish and handoff do not regrant holder')
        ck(gate.old.bit(node.J, G.lanes[0].reply) == answer, 'private final reply')
        node, next_commands, admitted = gate.complete(G, node, 1, jobs)
        ck(admitted == (1,), 'contender succeeds after actual handoff')
        table, next_answer, cache = prior.parent.expected(G.C, table, cache, jobs[1][0])
        want = G.C.encode(table, next_answer, cache)
        for actor, lane in enumerate(G.lanes):
            want = m.canon(want+p.reg(lane.admitted, 1)+p.reg(lane.reply, int((answer, next_answer)[actor])))
            if actor != node.turn:
                want = m.canon(want+(G.gate_pair[actor][phase ^ 1],))
        ck(node.J == want, 'whole final source, requests, keys, gates, private replies and cleanup')
        ck(entry_commands+exit_commands == 31, 'same inherited protection wrapper')
        rows.append(dict(phase=phase, body_operations=operations, body_commands=len(words),
                         wrapper_commands=entry_commands+exit_commands,
                         protected_invocation_commands=entry_commands+len(words)+exit_commands,
                         vacancy_bit_reads=controller.vacancy_bit_reads,
                         business_key_bit_reads=controller.business_key_bit_reads,
                         control_events=controller.all_events(),
                         contender_boundary_attempts=len(boundaries),
                         refused_contender_commands=refused_commands,
                         next_admitted_bind_commands=next_commands,
                         members=G.members, candidates=len(G.H),
                         additional_members=0, additional_candidates=0))
    return dict(mode='protected', rows=rows, assertions=CHECKS,
                coverage='Two gate phases, a separate complete contender bind attempt at every body boundary, then actual handoff')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('costs', 'pure_creates', 'regressions', 'audit', 'omissions', 'protected'))
    parser.add_argument('--slots', type=int, default=1)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--stop', type=int)
    parser.add_argument('--out')
    args = parser.parse_args()
    result = audit(args.slots, args.start, args.stop) if args.mode == 'audit' else globals()[args.mode]()
    text = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.out:
        Path(args.out).write_text(text)
    else:
        print(text)


if __name__ == '__main__':
    main()
