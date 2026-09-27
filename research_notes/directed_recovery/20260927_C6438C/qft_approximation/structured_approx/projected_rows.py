"""Certified-envelope prototype, with full native rows and totalized kernels.

No gate is replaced by an ideal reference. Pruning is an explicit approximate
work-label projection, governed by the separate global error certificate.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import asdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep27-qft-research'
sys.path.insert(0, str(OLD/'gram_research'))
from single_walker import (PointRowOracle, RawRow, SingleWalker, QueryBudgetExhausted,
                           normalize_row)
from certified_word_compiler import PositivePathObserver, packed
from stage45.brc_loop_recheck import CALLS


def observed(observer, name, terms):
    terms = tuple(tuple(F(x) for x in term) for term in terms if all(term))
    return observer.evaluate(name, terms) if terms else F(0)


def descriptor(program):
    return {'N': program.N, 'a': program.a, 't': program.t, 'dim': program.dim,
            'full_dim': program.full_dim, 'phase_bindings': program.phase_bindings,
            'codec_binding': program.codec_binding, 'h4_binding': program.h4_binding,
            'multipliers': [table.b for table in program.tables]}


def digest(value):
    return hashlib.sha256(packed(value)).hexdigest()


def preparation_walk(program, depth, rng):
    if type(depth) is not int or not 0 <= depth < program.t:
        raise ValueError('preparation depth must precede final readout')
    label = 1
    path = [label]
    coins = []
    for i in range(depth):
        bit = rng.randrange(2)
        if type(bit) is not int or bit not in (0, 1):
            raise ValueError('fresh uniform binary draw required')
        coins.append(bit)
        if bit:
            label = program.tables[i][label]
        path.append(label)
    return {'coins': coins, 'labels': path}


def train_envelope(program, *, samples, caps, exact_initial_depth, rng):
    if (type(samples) is not int or samples < 1 or len(caps) != program.t
            or any(type(k) is not int or k < 1 for k in caps)
            or type(exact_initial_depth) is not int or not 0 <= exact_initial_depth < program.t):
        raise ValueError('positive fixed training budget/caps and initial exact depth required')
    counts = [Counter() for _ in range(program.t)]
    paths = []
    for _ in range(samples):
        path = preparation_walk(program, program.t-1, rng)
        paths.append(path)
        for depth, label in enumerate(path['labels']):
            counts[depth][label] += 1
    sets = [{label for label, _ in sorted(c.items(), key=lambda p: (-p[1], p[0]))[:caps[i]]}
            for i, c in enumerate(counts)]
    exact = [{1}]
    traces = []
    for i in range(exact_initial_depth):
        following = set(exact[-1])
        transitions = []
        for label in sorted(exact[-1]):
            target = program.tables[i][label]
            following.add(target)
            transitions.append([label, target])
        exact.append(following)
        traces.append({'depth': i+1, 'transitions': transitions})
        # Declared exact layers may override the training cap; this is charged
        # and recorded, never silently counted as a cap-sized approximation.
        sets[i+1] = following
    sets[0] = {1}
    body = {'schema': 'FROZEN_TRAINING_WORK_ENVELOPE_V1',
            'program_descriptor_sha256': digest(descriptor(program)),
            'sets': [sorted(s) for s in sets], 'caps_requested': list(caps),
            'training_samples': samples, 'training_paths': paths,
            'training_frequency_counts': [sorted(c.items()) for c in counts],
            'exact_initial_depth': exact_initial_depth,
            'exact_initial_coverage': traces,
            'exact_initial_column_queries': sum(len(x['transitions']) for x in traces),
            'training_random_draws': samples*(program.t-1),
            'frozen_before_holdout': True}
    body['envelope_sha256'] = digest(body)
    return body


def verify_envelope(program, envelope):
    body = {k: v for k, v in envelope.items() if k != 'envelope_sha256'}
    if digest(body) != envelope.get('envelope_sha256'):
        raise ValueError('training envelope hash mismatch')
    if body['program_descriptor_sha256'] != digest(descriptor(program)):
        raise ValueError('envelope/program binding mismatch')
    sets = body['sets']
    if (len(sets) != program.t or sets[0] != [1]
            or any(s != sorted(set(s)) or any(type(w) is not int or not 0<=w<program.tables[0].carrier_size for w in s) for s in sets)):
        raise ValueError('invalid work sets')
    # Reconstruct every training path using actual columns, then the exact
    # initial coverage. A forged hash alone cannot bypass either proof.
    counts = [Counter() for _ in range(program.t)]
    if len(body['training_paths']) != body['training_samples']:
        raise ValueError('training sample count mismatch')
    for path in body['training_paths']:
        if len(path['coins']) != program.t-1 or path['labels'][0] != 1:
            raise ValueError('invalid training path')
        label, labels = 1, [1]
        for i, bit in enumerate(path['coins']):
            if type(bit) is not int or bit not in (0, 1):
                raise ValueError('invalid training bit')
            if bit:
                label = program.tables[i][label]
            labels.append(label)
        if labels != path['labels']:
            raise ValueError('training typed-column replay mismatch')
        for i, label in enumerate(labels):
            counts[i][label] += 1
    if [sorted(c.items()) for c in counts] != [list(map(tuple, x)) for x in body['training_frequency_counts']]:
        raise ValueError('training frequencies mismatch')
    current = {1}
    for i in range(body['exact_initial_depth']):
        transitions = [[w, program.tables[i][w]] for w in sorted(current)]
        current |= {p[1] for p in transitions}
        if body['exact_initial_coverage'][i] != {'depth': i+1, 'transitions': transitions} or sorted(current) != sets[i+1]:
            raise ValueError('exact initial coverage mismatch')
    for i in range(body['exact_initial_depth']+1, program.t):
        trained = sorted(w for w, _ in sorted(counts[i].items(), key=lambda p: (-p[1],p[0]))[:body['caps_requested'][i]])
        if trained != sets[i]:
            raise ValueError('envelope not the declared training selection')
    return tuple(frozenset(s) for s in sets)


def binomial_lower_tail(observer, samples, misses, threshold):
    """P_{threshold}(Bin(samples, threshold)<=misses), actual observer DP."""
    threshold = F(threshold)
    if not 0 < threshold < 1 or not 0 <= misses <= samples:
        raise ValueError('interior threshold and actual miss count required')
    probabilities = [F(1)] + [F(0)]*misses
    for trial in range(samples):
        future = []
        for j in range(misses+1):
            terms = [(probabilities[j], 1-threshold)]
            if j:
                terms.append((probabilities[j-1], threshold))
            future.append(observed(observer, 'binomial_lower_tail_step', terms))
        probabilities = future
    return observed(observer, 'binomial_lower_tail_sum', ((x,) for x in probabilities))


def validate_envelope(program, envelope, *, samples, thresholds, confidences, rng):
    sets = verify_envelope(program, envelope)
    if (type(samples) is not int or samples < 1 or len(thresholds) != program.t
            or len(confidences) != program.t):
        raise ValueError('fixed positive independent validation budget required')
    thresholds, confidences = tuple(map(F, thresholds)), tuple(map(F, confidences))
    exact = envelope['exact_initial_depth']
    if any(thresholds[i] != 0 or confidences[i] != 0 for i in range(exact+1)):
        raise ValueError('exact layers use deterministic zero missing mass')
    if any(not 0<thresholds[i]<1 or not 0<confidences[i]<1 for i in range(exact+1, program.t)):
        raise ValueError('statistical layers need interior declared thresholds/confidences')
    paths = [preparation_walk(program, program.t-1, rng) for _ in range(samples)]
    misses = [sum(path['labels'][i] not in sets[i] for path in paths) for i in range(program.t)]
    observer = PositivePathObserver()
    tests = []
    for i in range(exact+1, program.t):
        tail = binomial_lower_tail(observer, samples, misses[i], thresholds[i])
        tests.append({'depth': i, 'misses': misses[i], 'samples': samples,
                      'threshold': str(thresholds[i]), 'confidence_budget': str(confidences[i]),
                      'binomial_lower_tail_at_threshold': str(tail),
                      'accepted': tail <= confidences[i]})
    if any(misses[i] for i in range(exact+1)):
        raise AssertionError('deterministic coverage contradicted by actual holdout')
    accepted = all(x['accepted'] for x in tests)
    certificate = {'schema': 'INDEPENDENT_HOLDOUT_WORK_ENVELOPE_V1',
            'envelope_sha256': envelope['envelope_sha256'],
            'status': 'ACCEPTED_STATISTICAL_CERTIFICATE' if accepted else 'NOT_CERTIFIED',
            'thresholds': list(map(str, thresholds)), 'confidences': list(map(str, confidences)),
            'validation_paths': paths, 'validation_random_draws': samples*(program.t-1),
            'tests': tests, 'actual_probability_observer': observer.operations,
            'joint_false_accept_probability_bound': str(sum(confidences, F(0))),
            'conditional_on_acceptance_probability_bound_claimed': False,
            'independent_seed_contract_required': True, 'retries_performed': 0}
    certificate['certificate_sha256'] = digest(certificate)
    return certificate


def verify_validation(program, envelope, certificate):
    body = {k:v for k,v in certificate.items() if k!='certificate_sha256'}
    if digest(body) != certificate.get('certificate_sha256'):
        raise ValueError('validation certificate digest mismatch')
    if (body.get('conditional_on_acceptance_probability_bound_claimed') is not False
            or body.get('independent_seed_contract_required') is not True
            or body.get('retries_performed') != 0):
        raise ValueError('holdout statistical contract fields changed')
    sets = verify_envelope(program, envelope)
    if body['envelope_sha256'] != envelope['envelope_sha256']:
        raise ValueError('wrong holdout envelope')
    paths = body['validation_paths']
    if not paths or body['validation_random_draws'] != len(paths)*(program.t-1):
        raise ValueError('holdout sample/draw count mismatch')
    for path in paths:
        if len(path['coins']) != program.t-1:
            raise ValueError('bad holdout path depth')
        label, labels = 1, [1]
        for i,bit in enumerate(path['coins']):
            if type(bit) is not int or bit not in (0,1):
                raise ValueError('bad holdout binary draw')
            if bit:
                label = program.tables[i][label]
            labels.append(label)
        if labels != path['labels']:
            raise ValueError('holdout actual column replay mismatch')
    misses = [sum(path['labels'][i] not in sets[i] for path in paths) for i in range(program.t)]
    exact = envelope['exact_initial_depth']
    thresholds = tuple(map(F,body['thresholds']))
    confidences = tuple(map(F,body['confidences']))
    if len(thresholds)!=program.t or len(confidences)!=program.t:
        raise ValueError('holdout budget dimensions mismatch')
    if any(thresholds[i] or confidences[i] or misses[i] for i in range(exact+1)):
        raise ValueError('false zero-error coverage claim')
    observer = PositivePathObserver()
    expected = []
    for i in range(exact+1,program.t):
        if not 0<thresholds[i]<1 or not 0<confidences[i]<1:
            raise ValueError('invalid certificate allocation')
        tail = binomial_lower_tail(observer,len(paths),misses[i],thresholds[i])
        expected.append({'depth':i,'misses':misses[i],'samples':len(paths),
            'threshold':str(thresholds[i]),'confidence_budget':str(confidences[i]),
            'binomial_lower_tail_at_threshold':str(tail),'accepted':tail<=confidences[i]})
    status = 'ACCEPTED_STATISTICAL_CERTIFICATE' if all(x['accepted'] for x in expected) else 'NOT_CERTIFIED'
    if (expected != body['tests'] or status != body['status']
            or observer.operations != body['actual_probability_observer']
            or str(sum(confidences,F(0))) != body['joint_false_accept_probability_bound']):
        raise ValueError('full holdout probability replay mismatch')
    return {'verified':True,'status':status,'probability_observer_replay_count':len(observer.operations)}


class ProjectedRowOracle(PointRowOracle):
    def __init__(self, program, envelope, history=(), *, query_budget=100000):
        super().__init__(program, (), query_budget=query_budget)
        self.envelope = envelope
        self.sets = verify_envelope(program, envelope)
        self.rows = {1: RawRow(tuple(int(j==0) for j in range(self.dim)), 1)}
        self.state_depth = 0
        self.stats.update({'row_lookup_queries': 0, 'projected_row_inputs': 0,
            'discarded_nonzero_candidate_rows': 0, 'peak_retained_rows': 1,
            'peak_candidate_rows': 1, 'operation_units_used': 0})
        for bit in history:
            self.append(bit)

    def charge(self, name):
        if self.stats['operation_units_used'] >= self.query_budget:
            raise QueryBudgetExhausted('projected row operation budget reached; parent retained')
        self.stats['operation_units_used'] += 1
        self.stats[name] += 1

    def query(self, depth, label):
        if (type(depth) is not int or depth != self.state_depth or depth != len(self.history)
                or type(label) is not int or not 0<=label<self.program.tables[0].carrier_size):
            raise ValueError('projected current-prefix row required')
        self.charge('row_lookup_queries')
        return self.rows.get(label, RawRow((0,)*self.dim, 1))

    def append(self, bit):
        if type(bit) is not int or bit not in (0, 1) or len(self.history)>=self.program.t:
            raise ValueError('one exact classical bit required')
        depth = len(self.history)
        if depth+1 == self.program.t:
            # No approximate terminal row is needed by the readout sampler.
            self.history += (bit,)
            return
        future = {}
        for label, row in self.rows.items():
            self.charge('projected_row_inputs')
            moved = self.apply_feedback(depth, row)
            for destination, contribution, sign in (
                    (label, row, 1),
                    (self.program.tables[depth][label], moved, 1 if bit==0 else -1)):
                contribution = normalize_row(tuple(sign*x for x in contribution.values), contribution.den<<1)
                if destination in future:
                    contribution = self.combine(future[destination], contribution, halve=False)
                if any(contribution.values):
                    future[destination] = contribution
                else:
                    future.pop(destination, None)
        self.stats['peak_candidate_rows'] = max(self.stats['peak_candidate_rows'], len(future))
        self.stats['discarded_nonzero_candidate_rows'] += sum(w not in self.sets[depth+1] for w in future)
        retained = {w:r for w,r in future.items() if w in self.sets[depth+1]}
        # Commit field and history only after the whole bounded update succeeds.
        self.rows, self.state_depth = retained, depth+1
        self.history += (bit,)
        self.stats['peak_retained_rows'] = max(self.stats['peak_retained_rows'], len(retained))
        for row in retained.values():
            self.stats['max_numerator_bits'] = max(self.stats['max_numerator_bits'],max(map(lambda x:abs(x).bit_length(),row.values),default=0))
            self.stats['max_denominator_bits'] = max(self.stats['max_denominator_bits'],row.den.bit_length())

    def report(self):
        result = super().report()
        result.update({'oracle_type': 'ACTUAL_FULL_ROW_WITH_FROZEN_WORK_PROJECTION',
            'state_depth': self.state_depth, 'retained_rows': len(self.rows),
            'retained_scalar_slots': len(self.rows)*self.dim,
            'envelope_sha256': self.envelope['envelope_sha256'],
            'approximate_latent_norm_invariant_claimed': False})
        return result

    def evidence(self):
        result = super().evidence()
        result.update({'projected_rows': [{'label': w, **asdict(row)} for w,row in sorted(self.rows.items())],
            'projected_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
        return result


def approximate_plan(oracle, latent, auxiliary):
    if (type(auxiliary) is not int or auxiliary not in (0,1) or type(latent) is not int
            or not 0<=latent<oracle.program.tables[0].carrier_size):
        raise ValueError('valid latent and binary proposal required')
    depth = len(oracle.history)
    candidate = latent if auxiliary==0 else oracle.program.tables[depth][latent]
    predecessor = oracle.inverse_table(depth)[candidate]
    x = oracle.query(depth, candidate)
    y = oracle.apply_feedback(depth, oracle.query(depth, predecessor))
    total = oracle.observe('approximate_pair_norm', ((oracle.norm_observation(x),), (oracle.norm_observation(y),)))
    if total:
        plus = oracle.combine(x,y,halve=False)
        p0 = oracle.norm_observation(plus)/(2*total)
    else:
        p0 = F(1,2)
    if not 0<=p0<=1:
        raise AssertionError('invalid approximate sign probability')
    return {'history': oracle.history, 'latent_before': latent, 'auxiliary_bit': auxiliary,
            'candidate': candidate, 'predecessor': predecessor, 'row_x': x, 'row_y': y,
            'bit_probability_given_proposed_label': p0, 'zero_pair_fair_fallback': total==0}


class ProjectedWalker(SingleWalker):
    def __init__(self, program, envelope, certificate, *, query_budget=100000):
        self.certificate_replay = verify_validation(program,envelope,certificate)
        if certificate['status'] != 'ACCEPTED_STATISTICAL_CERTIFICATE' or certificate['envelope_sha256'] != envelope['envelope_sha256']:
            raise ValueError('accepted matching holdout certificate required')
        super().__init__(program, oracle=ProjectedRowOracle(program, envelope, query_budget=query_budget))
        self.pending_selected_bit = None

    def step(self, rng):
        if len(self.history)>=self.program.t:
            raise ValueError('terminal projected walker')
        if self.pending_auxiliary_bit is None:
            self.pending_auxiliary_bit = self._draw(F(1,2),rng)
        if self.pending_plan is None:
            self.pending_plan = approximate_plan(self.oracle,self.latent,self.pending_auxiliary_bit)
        plan = self.pending_plan
        if tuple(plan['history']) != self.history or plan['latent_before'] != self.latent:
            raise AssertionError('unfinished approximate transition changed parent')
        if self.pending_selected_bit is None:
            self.pending_selected_bit = self._draw(plan['bit_probability_given_proposed_label'],rng)
        bit = self.pending_selected_bit
        self.oracle.append(bit)
        self.latent = plan['candidate']
        event = {**plan, 'selected_bit': bit}
        self.events.append(event)
        self.pending_auxiliary_bit = self.pending_plan = self.pending_selected_bit = None
        return event

    def run(self, rng, *, postprocess=None):
        result = super().run(rng, postprocess=postprocess)
        result['pending_selected_bit'] = self.pending_selected_bit
        result['approximate_reference_contract'] = 'FROZEN_WORK_ENVELOPE_GLOBAL_RAW_L2'
        return result


def run_one_shot(program, *, training_samples, holdout_samples, caps,
                 exact_initial_depth, thresholds, confidences,
                 training_rng, holdout_rng, walker_rng, query_budget=100000):
    """One frozen training/holdout attempt, then automatic totalized route.

    Independence/uniformity of the three random sources is a caller contract,
    not a claim that different Python objects prove statistical independence.
    Any incomplete random/query run is exposed as such; never retried secretly.
    """
    if len({id(training_rng),id(holdout_rng),id(walker_rng)}) != 3:
        raise ValueError('separate training, holdout and walker random-source objects required')
    first=len(CALLS)
    stages=[]
    envelope = train_envelope(program,samples=training_samples,caps=caps,
        exact_initial_depth=exact_initial_depth,rng=training_rng)
    stages.append({'stage':'after_training','core_calls_since_outer_start':len(CALLS)-first,
        'program_metrics':program.report_metrics()})
    certificate = validate_envelope(program,envelope,samples=holdout_samples,
        thresholds=thresholds,confidences=confidences,rng=holdout_rng)
    stages.append({'stage':'after_holdout','core_calls_since_outer_start':len(CALLS)-first,
        'program_metrics':program.report_metrics()})
    if certificate['status']=='ACCEPTED_STATISTICAL_CERTIFICATE':
        walker=ProjectedWalker(program,envelope,certificate,query_budget=query_budget)
        route='ACCEPTED_PROJECTED_ROWS'
        replay=walker.certificate_replay
    else:
        replay=verify_validation(program,envelope,certificate)
        walker=SingleWalker(program,query_budget=query_budget)
        route='AUTOMATIC_EXACT_FALLBACK'
    result=walker.run(walker_rng)
    stages.append({'stage':'after_replay_and_sample','core_calls_since_outer_start':len(CALLS)-first,
        'program_metrics':program.report_metrics(),'oracle_report':walker.oracle.report()})
    return {'route':route,'training':envelope,'holdout':certificate,
        'certificate_replay':replay,'sample':result,'oracle_evidence':walker.oracle.evidence(),
        'holdout_attempts':1,'resampling_until_acceptance':False,
        'resource_stages':stages,
        'combined_error_budget':{'thresholds':list(map(str,thresholds)),
            'false_accept_addition':str(sum(map(F,confidences),F(0))),
            'norm_bound_formula':'sum_{i=1}^{t-1} sqrt(sum_{j=1}^{i} delta_j)',
            'requires_complete_sample_status':True},
        'live_walker':walker}
