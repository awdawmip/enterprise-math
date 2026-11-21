"""Cost-aware selection and bounded probing through original BRC words.

The controller reads original Boolean outputs and maintained prefix labels.
The exact request table belongs only to the verification functions below.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'future'))
import check_region_certificate as regional
from selector import MaskedRegionEvidence, TargetWindow, choose_observed_prefix

directed, prior, old, base, e, r = (regional.directed, regional.prior,
    regional.old, regional.base, regional.e, regional.r)
CHECKS = 0


def ck(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(message)


def key_weight(key, width):
    return 2*key.bit_count()+4*(1-((key >> (width-1)) & 1))


def reference_choice(tree, start, colors, extra_bits=None):
    """Simple control reference: test candidates against observed labels only.

    This O(colors*slots) decision reference counts its own comparisons. It
    never examines an original request identity or a physical relation table.
    """
    labels = set(tree.labels)
    extra_bits = {} if extra_bits is None else extra_bits
    available, comparisons = [], 0
    for key in range(start, start+colors):
        for label in labels:
            comparisons += 1
            mask, value = extra_bits.get(label, (0, 0))
            if key % (1 << label.depth) == label.value and key & mask == value:
                break
        else:
            available.append(key)
    return (min(available, key=lambda k: (key_weight(k, tree.width), k))
            if available else None), comparisons


class CostAwareController(directed.Controller):
    """Original non-reserve API with cost-aware reserve and optional probes."""

    def __init__(self, compiler, *, initial='deficit', probe_at=None, planner=None):
        super().__init__(compiler)
        self.initial = initial
        self.probe_at = probe_at
        self.planner = planner
        self.successful_reserves = 0
        self.extra_bits = {}
        self.initial_probe_done = False
        self.region = MaskedRegionEvidence(compiler.slots, compiler.color_bits)
        self.target_windows = tuple(TargetWindow.make(compiler.color_bits,
            compiler.key(t, 0), compiler.colors) for t in range(compiler.d))
        self.selector_events = dict(weighted_query_visits=0, observed_prefix_visits=0)
        self.optimization_events = dict(cost_selections=0, candidate_prefix_checks=0,
            candidate_probe_attempts=0, candidate_probe_successes=0,
            explicit_probe_bit_reads=0, initial_even_probes=0,
            initial_probe_fallbacks=0, initial_high_probes=0,
            cached_bits_promoted_to_prefix=0)

    def knowledge(self):
        result=[]
        for label in self.tree.labels:
            mask,value=self.extra_bits.get(label,(0,0))
            result.append((mask | ((1 << label.depth)-1),value | label.value))
        return tuple(result)

    def all_events(self):
        return dict(**super().all_events(), **self.optimization_events,
            **self.selector_events,
            **{'region_'+k:v for k,v in self.region.events.items()})

    def choose(self, target):
        self.optimization_events['cost_selections'] += 1
        start = self.C.key(target, 0)
        if self.region.tree is not None:
            key = self.region.select_key(start, self.C.colors,
                                         window=self.target_windows[target])
            if key is not None:
                return key
        unpromoted = any(mask >> label.depth for label, (mask, value)
                         in self.extra_bits.items() if label.refs)
        if not unpromoted:
            return choose_observed_prefix(self.tree, start, self.C.colors,
                window=self.target_windows[target], metrics=self.selector_events)
        key, checks = reference_choice(self.tree, self.C.key(target, 0), self.C.colors,
                                      self.extra_bits)
        self.optimization_events['candidate_prefix_checks'] += checks
        return key

    def step(self, J, op, *, trace=False, repeats=1, omitted=()):
        if op[0] != 'reserve':
            before = self.all_events()
            J, mass, entry = super().step(J, op, trace=trace, repeats=repeats, omitted=omitted)
            if op[0] == 'bind':
                self.region.bind(op[1], entry['observed_business_code'])
            elif op[0] == 'copy':
                self.region.copy(op[1], op[2])
            elif op[0] == 'drop':
                self.region.drop(op[1])
            after = self.all_events()
            entry['control_events'] = {k:after[k]-before[k] for k in after}
            entry['region'] = self.region.metrics()
            return J, mass, entry
        C, target = self.C, op[1]
        words, logs, observations, branches, old_pairs = [], [], [], [], []
        mass = e.prep(J)
        omitted = set(omitted)
        before = self.all_events()
        vacancy_before = self.vacancy_bit_reads

        def do(block):
            nonlocal J, mass
            offset = len(words)
            expanded = tuple(raw for raw in block for _ in range(repeats))
            local = {x-offset for x in omitted if offset <= x < offset+len(expanded)}
            J, weight, records = C.runword(J, expanded, trace, local)
            mass = r.serial(mass, weight)
            words.extend(expanded)
            if trace:
                logs.extend(dict(row, position=row['position']+offset) for row in records)

        def read_bit(label, bit, reason):
            if bit < label.depth:
                return (label.value >> bit) & 1
            mask, saved = self.extra_bits.get(label, (0, 0))
            if mask & (1 << bit):
                return (saved >> bit) & 1
            slot = label.representative
            do(C.reads[slot, bit])
            value = int(C.observe_result(J))
            observations.append(('request_key_bit', slot, bit, value, reason))
            if label.initial_slot is None:
                raise ValueError('Controlled identities are fully known')
            old_pairs.append((label.initial_slot, bit))
            self.vacancy_bit_reads += 1
            if reason != 'deficit':
                self.optimization_events['explicit_probe_bit_reads'] += 1
            self.extra_bits[label] = mask | (1 << bit), saved | (value << bit)
            return value

        def read_next(label, reason):
            bit = label.depth
            if self.extra_bits.get(label, (0, 0))[0] & (1 << bit):
                self.optimization_events['cached_bits_promoted_to_prefix'] += 1
            value = read_bit(label, bit, reason)
            self.tree.observe_next(label, value)

        def drain(level, prefix, reason):
            index = self.tree.index(level, prefix)
            while self.tree.head[index] is not None:
                read_next(self.tree.head[index], reason)

        def certify(residue):
            self.optimization_events['candidate_probe_attempts'] += 1
            while True:
                compatible = [label for label in set(self.tree.labels)
                    if residue % (1 << label.depth) == label.value and
                    residue & self.extra_bits.get(label, (0, 0))[0]
                    == self.extra_bits.get(label, (0, 0))[1]]
                if not compatible:
                    self.optimization_events['candidate_probe_successes'] += 1
                    return True
                if any(label.depth == C.color_bits for label in compatible):
                    return False
                label = min(compatible, key=lambda x: (x.depth, x.representative))
                read_next(label, 'candidate_probe')

        def guaranteed_query():
            start = C.key(target, 0) % C.modulus
            level = prefix = 0
            capacity = C.colors
            self.events['target_searches'] += 1
            while True:
                index = self.tree.index(level, prefix)
                blockers = self.tree.count[index]
                self.events['query_node_visits'] += 1
                if capacity <= blockers:
                    raise ValueError('Target-directed deficit was lost')
                if blockers == 0:
                    return level, prefix
                if level == C.color_bits:
                    raise ValueError('Occupied singleton cannot have a deficit')
                drain(level, prefix, 'deficit')
                eligible, counts, capacities = [], [], []
                for bit in (0, 1):
                    child_prefix = prefix | (bit << level)
                    n = self.tree.count[self.tree.index(level+1, child_prefix)]
                    cap, first = self.capacity(start, C.colors, level+1, child_prefix)
                    self.events['candidate_count_queries'] += 1
                    counts.append(n); capacities.append(cap)
                    if n < cap:
                        eligible.append((n, bit, cap, first))
                _, bit, capacity, _ = min(eligible)
                branches.append(dict(level=level, prefix=prefix,
                    label_counts=counts, candidate_counts=capacities, selected_bit=bit))
                self.events['selected_branches'] += 1
                prefix |= bit << level
                level += 1

        high_probe = (not self.initial_probe_done and
                      self.initial in ('high_half', 'high_half_late'))
        prechecked = high_probe and self.initial == 'high_half_late'
        if prechecked:
            do(C.free_reads[target])
            available = bool(C.observe_result(J))
            observations.append(('target_available', target, int(available)))
        if high_probe and (not prechecked or available):
            self.optimization_events['initial_high_probes'] += 1
            # A physically read high bit is kept as a masked observation until
            # any later low-prefix traversal reaches its position.
            for label in sorted(set(self.tree.labels), key=lambda x:x.representative):
                read_bit(label, C.color_bits-1, 'initial_high_probe')
            values = {(read_bit(label, C.color_bits-1, 'cached_high'))
                      for label in set(self.tree.labels)}
            if len(values) == 1:
                high = 1 << (C.color_bits-1)
                self.region.acquire_mask(high, (1-next(iter(values)))*high)
            self.initial_probe_done = True
        planned_key = None
        if self.planner is not None:
            if self.planner.targets[self.successful_reserves] != target:
                raise ValueError('Planned target sequence differs from actual call')
            while True:
                action = self.planner.action(self.knowledge(), self.successful_reserves)
                if action[0] == 'create':
                    planned_key = action[1]
                    break
                _,slot,bit=action
                read_bit(self.tree.labels[slot],bit,'bellman_query')
        # This required conflict check runs after an initial high-bit probe.
        # Its real successful result is the physical Boolean consumed below.
        if not prechecked:
            do(C.free_reads[target])
            available = bool(C.observe_result(J))
            observations.append(('target_available', target, int(available)))
        entry = dict(op=tuple(op), color=None, key=None)
        if available:
            number = self.successful_reserves+1
            initial_probe = number == 1 and self.initial == 'even_first'
            if initial_probe:
                self.optimization_events['initial_even_probes'] += 1
                drain(0, 0, 'initial_probe')
                if C.color_bits > 1:
                    drain(1, 0, 'initial_probe')
            if self.probe_at == number:
                start = C.key(target, 0)
                desired = min(range(start, start+C.colors),
                              key=lambda k: (key_weight(k, C.color_bits), k))
                entry['probed_key'] = desired
                entry['candidate_probe_succeeded'] = certify(desired % C.modulus)
            key = planned_key if planned_key is not None else self.choose(target)
            if key is None:
                if initial_probe or high_probe:
                    self.optimization_events['initial_probe_fallbacks'] += 1
                level, prefix = guaranteed_query()
                if self.initial in ('high_half', 'high_half_late'):
                    self.region.acquire(level, prefix)
                key = self.choose(target)
            if key is None:
                raise ValueError('Guaranteed empty class must contain a legal key')
            color = key-C.key(target, 0)
            last = int(C.observe_result(J))
            do(C.create_words[target, color, last])
            self.witness = key % C.modulus
            self.successful_reserves += 1
            entry.update(color=color, key=key, physical_last_before_create=last,
                         selected_key_weight=key_weight(key, C.color_bits))
        self.commands += len(words)
        self.api_calls += 1
        after = self.all_events()
        entry.update(answer=bool(C.observe_result(J)), commands=len(words),
            vacancy_bit_reads=self.vacancy_bit_reads-vacancy_before,
            business_key_bit_reads=0, witness=self.witness, memory=self.tree.metrics(),
            control_events={key: after[key]-before[key] for key in after},
            old_query_pairs=tuple(old_pairs), observations=tuple(observations),
            branches=tuple(branches), word=tuple(words), trace=logs)
        entry['region'] = self.region.metrics()
        return J, mass, entry

    def summary(self):
        result = super().summary()
        result.update(strategy='cost_aware_observed', initial_policy=self.initial,
            probe_at=self.probe_at, successful_reserves=self.successful_reserves,
            future_planner=self.planner is not None,
            final_region=self.region.metrics(),
            compiled_target_windows=len(self.target_windows),
            arbitrary_observation_mask_records=len(self.extra_bits),
            arbitrary_observed_bits=sum(mask.bit_count() for mask,value in self.extra_bits.values()),
            additional_persistent_members=0, additional_candidate_relations=0)
        return result


# Verification boundary: exact request tables are used only below this line.
def verify_controller(C, controller, table):
    directed.verify_memory(C, controller, table)
    keys = [0 if row is None else C.key(*row) for row in table[1]]
    for label, key in zip(controller.tree.labels, keys):
        mask, value = controller.extra_bits.get(label, (0, 0))
        ck(key & mask == value, 'cached arbitrary bits match actual identity')
    region = controller.region
    if region.tree is None:
        return
    expected = [key % C.modulus if key and region.spec.contains(key % C.modulus)
                else None for key in keys]
    ck(region.members == expected, 'masked regional slot memberships')
    counts = Counter(x for x in expected if x is not None)
    ck(region.refs == counts, 'masked region multiplicities')
    ck(region.tree.free_count == region.spec.size-len(counts), 'masked free cardinality')
    for index in range(region.spec.size):
        residue = region.spec.unpack(index)
        ck(region.tree.minimum(index,index) == (None if residue in counts else index),
           'weighted masked index has exactly the unretained residues')


def run_case(C, table, operations, *, initial='deficit', probe_at=None, cache=None,
             trace=False, repeats=1, omitted=(), controller_factory=None):
    controller = (CostAwareController(C, initial=initial, probe_at=probe_at)
                  if controller_factory is None else controller_factory(C))
    cache = C.initial_cache(table) if cache is None else tuple(cache)
    J = C.encode(table, False, cache)
    mass = e.prep(J)
    original = table
    entries, forms, words, logs, pairs = [], [], [], [], set()
    for op in operations:
        offset = len(words)
        J, weight, entry = controller.step(J, op, trace=trace, repeats=repeats,
            omitted={x-offset for x in omitted if x >= offset})
        mass = r.serial(mass, weight)
        table, answer, cache = old.expected_selected(C, table, cache, op, entry)
        ck(J == C.encode(table, answer, cache), 'whole original core and output')
        verify_controller(C, controller, table)
        for pair in entry['old_query_pairs']:
            ck(pair not in pairs, 'initial label bit observed only once')
            pairs.add(pair)
        forms.append((base.canon(C, table), answer))
        entries.append({k:v for k,v in entry.items() if k not in ('word','trace')})
        words.extend(entry['word'])
        if trace:
            logs.extend(dict(row, position=row['position']+offset) for row in entry['trace'])
    return J, mass, dict(**controller.summary(), entries=entries,
        initial_table=original, final_table=table, semantic_prefixes=forms,
        word=tuple(words), trace=logs, extra_old_bit_pairs=sorted(pairs))


def compact(result, keep_entries=0):
    value = directed.compact(result, keep_entries)
    if keep_entries:
        for row, full in zip(value['first_steps'], result['entries']):
            for key in ('selected_key_weight','probed_key','candidate_probe_succeeded'):
                if key in full:
                    row[key] = full[key]
    return value


def compare(C, table, operations, *, keep_entries=0):
    strategies = {
        'single_point': directed.run_case,
        'tracked_region': regional.run_case,
        'weighted_observed': lambda c,t,o: run_case(c,t,o),
        'weighted_probe_second': lambda c,t,o: run_case(c,t,o,probe_at=2),
        'weighted_even_first': lambda c,t,o: run_case(c,t,o,initial='even_first'),
        'weighted_high_half': lambda c,t,o: run_case(c,t,o,initial='high_half'),
        'weighted_high_half_late': lambda c,t,o: run_case(c,t,o,initial='high_half_late'),
    }
    rows, semantics = {}, None
    for name, runner in strategies.items():
        _, mass, result = runner(C,table,operations)
        ck(mass.count == 1, 'one actual original-kernel path')
        if semantics is None:
            semantics=result['semantic_prefixes']
        else:
            ck(result['semantic_prefixes']==semantics, 'API semantics preserved')
        row=compact(result, keep_entries)
        row['by_round'] = []
        total=0
        for index in range(len(operations)//3):
            block=result['entries'][3*index:3*index+3]
            total+=sum(x['commands'] for x in block)
            row['by_round'].append(dict(round=index+1,key=block[0].get('key'),
                commands=[x['commands'] for x in block],cumulative=total,
                reads=block[0]['vacancy_bit_reads'],
                physical_last=block[0].get('physical_last_before_create')))
        rows[name]=row
    return rows


def family():
    rows=[]
    formula_prefixes=0
    for slots in (6,14):
        C=prior.Compiler(slots=slots)
        codes=(2,)*(slots//2)+(3,)*(slots//2)
        table=((None,)*C.d,tuple(divmod(k-1,C.colors) for k in codes))
        for rounds in (1,2,8,32):
            ops=(('reserve',0),('bind',0,0),('release',1))*rounds
            strategies=compare(C,table,ops,keep_entries=6)
            constant=8*C.color_bits+2*C.bits+38
            for index in range(rounds):
                T=index+1
                high=strategies['weighted_high_half']['by_round'][index]
                late=strategies['weighted_high_half_late']['by_round'][index]
                ck(high['cumulative']==8*slots+(constant+3)*T-(T%2),
                   'exact high-half total at each actual horizon prefix')
                ck(late['cumulative']==high['cumulative']+4,
                   'required free check replaces separate physical-result cleanup')
                ck(high['key']==(C.modulus//2+(index%2)), 'minimum-weight alternating high keys')
                a=strategies['weighted_observed']['by_round'][index]
                b=strategies['weighted_probe_second']['by_round'][index]
                expected=0 if T==1 else 8*(slots//2-1)-4*(T//2)
                ck(b['cumulative']-a['cumulative']==expected,
                   'exact optional-expansion crossover under the common odd-class entry')
                formula_prefixes+=1
            rows.append(dict(slots=slots,rounds=rounds,initial_codes=codes,
                members=C.members,candidates=len(C.H),
                strategies=strategies))
    return dict(status='PASS',mode='family',rows=rows,assertions=CHECKS,
        original_kernel_runs=56,formula_prefixes_checked=formula_prefixes,
        decision_implementation='Weighted sparse region on the main half-region family; bounded observed-prefix scan or explicit masked-candidate reference on fallback',
        exact_high_half_formula='8*r+(8*b+2*q+41)*T-(T mod 2)',
        common_odd_entry_expansion_difference='T=1: 0; T>=2: 8*(r/2-1)-4*floor(T/2)')


def word_lengths():
    rows=[]
    for slots in (1,2,6,14):
        C=prior.Compiler(slots=slots)
        for target in range(C.d):
            for color in range(C.colors):
                key=C.key(target,color)
                lengths=[]
                for last in (0,1):
                    actual=len(C.create_words[target,color,last])
                    expected=C.bits+2+key.bit_count()+4*(1-last)
                    ck(actual==expected,'exact creation suffix length')
                    lengths.append(actual)
                sources=tuple(color if t==target else None for t in range(C.d))
                table=(sources,(None,)*C.slots)
                J=C.encode(table,False)
                got,weight,data=C.addressed(J,('bind',0,target))
                expected=8*C.color_bits+C.bits+10+key.bit_count()+4*(1-((key>>(C.color_bits-1))&1))
                ck(len(data['word'])==expected,'actual addressed binding length')
                ck(data['code']==key and weight.count==1,'actual business key read')
                rows.append(dict(slots=slots,target=target,key=key,create_by_last=lengths,
                    bind_commands=len(data['word']),weight=key_weight(key,C.color_bits)))
    return dict(status='PASS',mode='word_lengths',rows=rows,assertions=CHECKS,
        key_dependent_cost='2 popcount(K)+4(1-bit_(b-1)(K))',
        separate_creation_last_surcharge='4(1-physical_last)')


def regressions():
    C=prior.Compiler(slots=6)
    empty=((None,)*C.d,(None,)*C.slots)
    def table(codes,sources=None):
        return ((None,)*C.d if sources is None else sources,
                tuple(None if code==0 else divmod(code-1,C.colors) for code in codes))
    operations=(('reserve',0),('bind',0,0),('release',1))*4
    cases={
        'empty_requests':(empty,operations),
        'mixed_high_failure_and_cached_fallback':(table((1,2,3,4,5,6)),operations),
        'opposite_empty_half':(table((4,5,6,7,4,5)),operations),
        'aliases_and_last_reference':(table((1,1,1,1,1,1)),(
            ('reserve',0),('bind',0,0),('copy',1,0),('copy',2,1),('drop',0),
            ('release',1),('reserve',0),('valid',1),('drop',1),('drop',2),
            ('bind',0,0),('copy',0,0),('release',1),('reserve',2))),
        'source_execute_keeps_request':(empty,(
            ('reserve',0),('bind',0,0),('execute',0),('reserve',0),('valid',0))),
        'nonempty_zero_residue_and_empty_bind':(table((4,5,6,7,4,5)),(
            ('reserve',1),('bind',0,1),('copy',1,0),('release',4),
            ('reserve',2),('valid',0),('bind',0,1),('drop',1),('release',4),('reserve',1))),
        'blocked_source_probe':(table((2,2,2,3,3,3),(0,None,None)),(
            ('reserve',0),('reserve',1),('release',1),('reserve',0))),
        'protected_existing_source':(table((1,2,3,4,5,6),(None,None,0)),(
            ('reserve',0),('reserve',1),('reserve',2),('bind',0,0),
            ('copy',1,0),('release',1),('reserve',0),('valid',1))),
    }
    rows=[]
    for name,(initial,ops) in cases.items():
        _,base_mass,baseline=directed.run_case(C,initial,ops)
        J,mass,result=run_case(C,initial,ops,initial='high_half',trace=name=='protected_existing_source')
        ck(base_mass.count==mass.count==1,'one kernel realization')
        ck(result['semantic_prefixes']==baseline['semantic_prefixes'],'original API semantics')
        if name=='mixed_high_failure_and_cached_fallback':
            ck(result['control_events']['initial_probe_fallbacks']==1,'mixed high bits trigger real fallback')
            ck(result['control_events']['cached_bits_promoted_to_prefix']>0,
               'fallback reuses high observations without another physical read')
        if name=='blocked_source_probe':
            ck(result['entries'][0]['key'] is None and result['entries'][0]['vacancy_bit_reads']==6,
               'failed source check retains fully charged earlier probe cost')
        if name=='protected_existing_source':
            state=base.ref.old.seed(C.encode(initial,False))
            birth=state.names()[C.targets[2]]
            for command in result['word']:
                state,_,_=base.ref.old.raw_step(state,command,C.H)
                ck(state.names().get(C.targets[2])==birth,'existing source birth preserved through every primitive')
            ck(state.matching==J,'birth replay endpoint')
            protected_prefixes=len(result['word'])
        rows.append(dict(name=name,initial=initial,operations=ops,
            old=compact(baseline),new=compact(result,len(ops))))
    return dict(status='PASS',mode='regressions',rows=rows,assertions=CHECKS,
        protected_source_primitive_prefixes=protected_prefixes)


def protected():
    result=regional.prefix.protected(
        controller_factory=lambda C:CostAwareController(C,initial='high_half'),
        verifier=verify_controller)
    result['status']='PASS'
    result['new_controller_assertions']=CHECKS
    return result


def omissions():
    C=prior.Compiler(slots=2)
    table=((None,)*C.d,((0,0),(0,1)))
    ops=(('reserve',0),('bind',0,0),('copy',1,0),('drop',0),
         ('release',1),('reserve',0),('valid',1),('drop',1))
    want,_,baseline=run_case(C,table,ops,initial='high_half',repeats=2)
    mass=directed.ZERO
    for position in range(len(baseline['word'])):
        got,weight,result=run_case(C,table,ops,initial='high_half',repeats=2,omitted=(position,))
        ck(got==want and result['word']==baseline['word'],
           'one omitted repeated primitive preserves endpoint and adaptive decisions')
        ck(result['final_region']==baseline['final_region'],'masked region agrees after omission')
        ck(result['extra_old_bit_pairs']==baseline['extra_old_bit_pairs'],'same actually read bit set')
        mass=r.merge(mass,weight)
    ck(mass.count==len(baseline['word']),'every omission position executed')
    return dict(status='PASS',mode='omissions',slots=2,repeats=2,omission_budget=1,
        omission_positions=len(baseline['word']),CWM=e.cw(mass),assertions=CHECKS,
        initial_table=table,operations=ops)


def future_plan():
    C=prior.Compiler(slots=2)
    table=((None,)*C.d,((0,0),(0,0)))
    ops=(('reserve',0),('bind',0,0),('release',1),
         ('reserve',1),('bind',0,1),('release',4))

    class KnownFuture(CostAwareController):
        def __init__(self,C):
            super().__init__(C,initial='high_half')

        def choose(self,target):
            # Public desired target order 0,1; the action is admitted only if
            # the actual acquired evidence proves key 3 currently safe.
            if self.successful_reserves==0 and target==0 and self.region.contains(3):
                self.optimization_events['cost_selections']+=1
                return 3
            return super().choose(target)

    _,_,greedy=run_case(C,table,ops,initial='high_half')
    _,_,planned=run_case(C,table,ops,controller_factory=KnownFuture)
    ck(greedy['semantic_prefixes']==planned['semantic_prefixes'],'same future-relevant API semantics')
    ck([row['key'] for row in greedy['entries'] if row['op'][0]=='reserve']==[2,4],
       'myopic weighted choices')
    ck([row['key'] for row in planned['entries'] if row['op'][0]=='reserve']==[3,6],
       'known-future weighted choices')
    ck(greedy['commands']-planned['commands']==8,'one real old-bit reader saved')
    return dict(status='PASS',mode='future_plan',initial_table=table,operations=ops,
        greedy=compact(greedy,len(ops)),planned=compact(planned,len(ops)),assertions=CHECKS,
        scope='Two specified targets; desired first key is checked against actual acquired evidence')


def minimax():
    from itertools import product
    from bellman_planner import Planner, control_replay
    rows=[]
    total_runs=0
    cases=((2,(0,)),(2,(0,1)),(3,(0,1,2,0)))
    for slots,targets in cases:
        C=prior.Compiler(slots=slots)
        planner=Planner(slots,targets)
        blank=((0,0),)*slots
        value=planner.value(blank,0)
        constant=sum(len(C.free_reads[t])+(C.bits+2)+(8*C.color_bits+C.bits+10)
                     +len(C.programs[('release',C.targets[t][0])]) for t in targets)
        operations=tuple(op for t in targets for op in (
            ('reserve',t),('bind',0,t),('release',C.targets[t][0])))
        samples=[]
        maxima=[]
        observed_max=-1
        for residues in product(range(C.modulus),repeat=slots):
            # Residue zero is represented by a nonempty full code B.
            codes=tuple(x or C.modulus for x in residues)
            table=((None,)*C.d,tuple(divmod(code-1,C.colors) for code in codes))
            _,mass,result=run_case(C,table,operations,
                controller_factory=lambda compiler:CostAwareController(compiler,planner=planner))
            oracle=control_replay(planner,residues)
            actual_score=result['commands']-constant
            ck(actual_score==oracle['cost'],'original-word variable cost equals planner replay')
            ck(actual_score<=value,'each actual residue preparation is below minimax value')
            ck(all(row['physical_last_before_create']==1 for row in result['entries']
                   if row['op'][0]=='reserve'),'planned observation precedes required conflict check')
            ck(mass.count==1,'one original path for each complete residue preparation')
            total_runs+=1
            sample=dict(initial_residues=residues,initial_codes=codes,
                commands=result['commands'],variable_cost=actual_score,
                vacancy_bit_reads=result['vacancy_bit_reads'],
                keys=[row['key'] for row in result['entries'] if row['op'][0]=='reserve'])
            samples.append(sample)
            if actual_score>observed_max:
                observed_max=actual_score;maxima=[sample]
            elif actual_score==observed_max:
                maxima.append(sample)
        ck(observed_max==value,'complete B^r preparation attains claimed minimax')
        rows.append(dict(slots=slots,targets=targets,domain=C.modulus**slots,
            business_constant=constant,planner_value=value,
            actual_worst_commands=constant+observed_max,
            planner_metrics=planner.metrics(),samples=samples,worst_witnesses=maxima[:4]))
    C=prior.Compiler(slots=2)
    planner=Planner(2,(0,1))
    table=((None,)*C.d,((0,0),(0,0)))
    operations=(('reserve',0),('bind',0,0),('release',1),
                ('reserve',1),('bind',0,1),('release',1))
    _,_,seeded=run_case(C,table,operations,
        controller_factory=lambda compiler:CostAwareController(compiler,initial='high_half',planner=planner))
    ck([row['key'] for row in seeded['entries'] if row['op'][0]=='reserve']==[3,6],
       'planner consumes actually acquired high-half evidence')
    ck(seeded['vacancy_bit_reads']==2 and seeded['commands']==151,
       'actual high-half acquisition plus future planning needs no further old read')
    return dict(status='PASS',mode='minimax',rows=rows,original_kernel_runs=total_runs+1,
        exhaustive_preparation_runs=total_runs,assertions=CHECKS,
        high_half_seeded=compact(seeded,len(operations)),
        objective='8*old-request-bit-reads + sum key_weight; fixed business constants added')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=('family','word_lengths','regressions','protected','omissions','future_plan','minimax'))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=globals()[args.mode]()
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')


if __name__=='__main__':main()
