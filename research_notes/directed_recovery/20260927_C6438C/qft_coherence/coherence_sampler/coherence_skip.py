"""Frozen preparation partition, independent union test, and totalized walker.

This is an approximate sampler of the admitted native instrument. It never
replaces a phase action, truncates an internal coordinate, or assumes that
its latent law equals the exact conditional row norm after a skipped score.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parents[1]/'sep27-qft-approx'
OLD = HERE.parents[1]/'sep27-qft-research'
sys.path.insert(0,str(PREVIOUS/'structured_approx'))
sys.path.insert(0,str(OLD/'gram_research'))
from projected_rows import (descriptor, digest, preparation_walk,
                            binomial_lower_tail, observed, PositivePathObserver)
from single_walker import SingleWalker, PointRowOracle


def train_partition(program, depth, *, samples, cap, rng):
    if type(depth) is not int or not 0 <= depth < program.t:
        raise ValueError('one nonterminal preparation depth required')
    if type(samples) is not int or samples < 1 or type(cap) is not int or cap < 1:
        raise ValueError('fixed positive training budget and cap required')
    paths=[preparation_walk(program,depth,rng) for _ in range(samples)]
    counts=Counter(p['labels'][-1] for p in paths)
    chosen=sorted(w for w,n in sorted(counts.items(),key=lambda x:(-x[1],x[0]))[:cap])
    body={'schema':'FROZEN_PREPARATION_PARTITION_V1','depth':depth,'cap':cap,
        'program_descriptor_sha256':digest(descriptor(program)),
        'training_samples':samples,'training_paths':paths,
        'training_random_draws':samples*depth,'counts':sorted(counts.items()),
        'set_A':chosen,'frozen_before_validation':True}
    return {**body,'partition_sha256':digest(body)}


def replay_paths(program, paths, depth):
    endpoints=[]
    for path in paths:
        if len(path['coins']) != depth or len(path['labels']) != depth+1:
            raise ValueError('path dimensions changed')
        w=1
        labels=[w]
        for i,bit in enumerate(path['coins']):
            if type(bit) is not int or bit not in (0,1):
                raise ValueError('binary preparation coin required')
            if bit:w=program.tables[i][w]
            labels.append(w)
        if labels != path['labels']:
            raise ValueError('actual typed preparation replay mismatch')
        endpoints.append(w)
    return endpoints


def verify_partition(program, partition):
    body={k:v for k,v in partition.items() if k!='partition_sha256'}
    if digest(body)!=partition.get('partition_sha256'):
        raise ValueError('partition hash changed')
    if (body['program_descriptor_sha256']!=digest(descriptor(program))
            or body['schema']!='FROZEN_PREPARATION_PARTITION_V1'
            or body['frozen_before_validation'] is not True):
        raise ValueError('partition program or contract changed')
    depth,samples,cap=body['depth'],body['training_samples'],body['cap']
    if (type(depth) is not int or not 0<=depth<program.t
            or type(samples) is not int or samples<1
            or type(cap) is not int or cap<1
            or len(body['training_paths'])!=samples
            or body['training_random_draws']!=samples*depth):
        raise ValueError('invalid frozen training dimensions')
    counts=Counter(replay_paths(program,body['training_paths'],depth))
    chosen=sorted(w for w,n in sorted(counts.items(),key=lambda x:(-x[1],x[0]))[:cap])
    if chosen!=body['set_A'] or sorted(counts.items())!=list(map(tuple,body['counts'])):
        raise ValueError('training selection replay mismatch')
    return frozenset(chosen)


def validation_body(program, partition, paths, threshold, confidence):
    A=verify_partition(program,partition)
    d,zeta=F(threshold),F(confidence)
    if not 0<d<=F(1,2) or not 0<zeta<1 or not paths:
        raise ValueError('interior one-shot error and confidence budgets required')
    depth=partition['depth']
    labels=replay_paths(program,paths,depth)
    records=[]
    for w in labels:
        target=program.tables[depth][w]
        records.append({'w':w,'P_w':target,'outside_A':w not in A,
            'shifted_inside_A':target in A,'union_bad':w not in A or target in A})
    misses=sum(x['union_bad'] for x in records)
    obs=PositivePathObserver()
    tail=binomial_lower_tail(obs,len(paths),misses,d)
    square=observed(obs,'coherence_error_bound_squared',((d,1-d),))
    return {'schema':'INDEPENDENT_UNION_COHERENCE_TEST_V1',
        'partition_sha256':partition['partition_sha256'],'depth':depth,
        'threshold':str(d),'confidence_budget':str(zeta),
        'validation_paths':paths,'validation_random_draws':len(paths)*depth,
        'union_records':records,'misses':misses,'samples':len(paths),
        'binomial_lower_tail_at_threshold':str(tail),
        'layer_joint_TV_bound_squared':str(square),
        'status':'ACCEPTED_STATISTICAL_CERTIFICATE' if tail<=zeta else 'NOT_CERTIFIED',
        'probability_observer':obs.operations,
        'independent_training_validation_and_sampling_required':True,
        'conditional_on_acceptance_bound_claimed':False,'attempts':1}


def validate_partition(program, partition, *, samples, threshold, confidence, rng):
    if type(samples) is not int or samples<1:
        raise ValueError('fixed positive held-out sample budget required')
    paths=[preparation_walk(program,partition['depth'],rng) for _ in range(samples)]
    body=validation_body(program,partition,paths,threshold,confidence)
    return {**body,'certificate_sha256':digest(body)}


def verify_validation(program, partition, certificate):
    body={k:v for k,v in certificate.items() if k!='certificate_sha256'}
    if digest(body)!=certificate.get('certificate_sha256'):
        raise ValueError('validation hash changed')
    expected=validation_body(program,partition,body['validation_paths'],
                             body['threshold'],body['confidence_budget'])
    if expected!=body:
        raise ValueError('full statistical/typed-column replay mismatch')
    return body['status']=='ACCEPTED_STATISTICAL_CERTIFICATE'


def total_transition_plan(oracle, latent, auxiliary_bit, *, fair=False):
    """Exact row score everywhere it exists, fair extension of zero pairs."""
    i=len(oracle.history)
    if type(auxiliary_bit) is not int or auxiliary_bit not in (0,1) or i>=oracle.program.t:
        raise ValueError('nonterminal binary proposal required')
    candidate=latent if auxiliary_bit==0 else oracle.program.tables[i][latent]
    common={'history':oracle.history,'latent_before':latent,
            'auxiliary_bit':auxiliary_bit,'candidate':candidate}
    if fair:
        return {**common,'mode':'CERTIFIED_COHERENCE_FAIR_REPLACEMENT',
                'bit_probability_given_proposed_label':F(1,2),
                'row_query_performed':False,'zero_pair_fair_extension':False}
    predecessor=oracle.inverse_table(i)[candidate]
    x=oracle.query(i,candidate)
    source=oracle.query(i,predecessor)
    y=oracle.apply_feedback(i,source)
    plus=oracle.combine(x,y,halve=False)
    minus=oracle.combine(x,y,sign=-1,halve=False)
    nx,ny=oracle.norm_observation(x),oracle.norm_observation(y)
    total=oracle.observe('complete_pair_norm',((nx,),(ny,)))
    numerator=oracle.norm_observation(plus)
    other=oracle.norm_observation(minus)
    if numerator+other!=2*total or total<0:
        raise AssertionError('actual full-native parallelogram law failed')
    p0=numerator/(2*total) if total else F(1,2)
    return {**common,'mode':'FULL_EXACT_ROWS_TOTALIZED_OFF_REFERENCE',
        'predecessor':predecessor,'row_x':x,'row_y':y,
        'proposal_norm_sum':total,'plus_norm':numerator,'minus_norm':other,
        'bit_probability_given_proposed_label':p0,'row_query_performed':True,
        'zero_pair_fair_extension':not total,
        'parent_latent_row_zero':not any((x if auxiliary_bit==0 else source).values)}


class CoherenceWalker(SingleWalker):
    def __init__(self,program,partition,certificate,*,query_budget=1000):
        super().__init__(program,query_budget=query_budget)
        self.partition,self.certificate=partition,certificate
        self.accepted=verify_validation(program,partition,certificate)
        self.skip_depth=partition['depth'] if self.accepted else None
        self._frozen_descriptor=digest(descriptor(program))
        self._partition_hash=digest(partition)
        self._certificate_hash=digest(certificate)
        self._owned_oracle=self.oracle

    def step(self,rng):
        if (digest(descriptor(self.program))!=self._frozen_descriptor
                or digest(self.partition)!=self._partition_hash
                or digest(self.certificate)!=self._certificate_hash
                or self.oracle is not self._owned_oracle):
            raise ValueError('live program/certificate/oracle binding changed')
        if self.history!=tuple(e['selected_bit'] for e in self.events):
            raise ValueError('externally replaced history')
        expected=self.events[-1]['candidate'] if self.events else 1
        if self.latent!=expected:
            raise ValueError('externally replaced latent label')
        if len(self.history)>=self.program.t:raise ValueError('terminal walker')
        if self.pending_auxiliary_bit is None:
            self.pending_auxiliary_bit=self._draw(F(1,2),rng)
        if self.pending_plan is None:
            self.pending_plan=total_transition_plan(self.oracle,self.latent,
                self.pending_auxiliary_bit,fair=len(self.history)==self.skip_depth)
        plan=self.pending_plan
        if tuple(plan['history'])!=self.history or plan['latent_before']!=self.latent:
            raise ValueError('unfinished proposal changed parent')
        bit=self._draw(plan['bit_probability_given_proposed_label'],rng)
        self.oracle.append(bit)
        self.latent=plan['candidate']
        self.events.append({**plan,'selected_bit':bit,
            'selected_local_probability':plan['bit_probability_given_proposed_label'] if bit==0 else 1-plan['bit_probability_given_proposed_label']})
        self.pending_auxiliary_bit=self.pending_plan=None
        return self.events[-1]

    def run(self,rng,**kwargs):
        result=super().run(rng,**kwargs)
        result['coherence_optimization']={'certificate_accepted':self.accepted,
            'skip_depth':self.skip_depth,'partition_sha256':self.partition['partition_sha256'],
            'certificate_sha256':self.certificate['certificate_sha256'],
            'all_other_scores_use_complete_exact_rows':True,
            'off_reference_kernel_totalized':True,'statistical_attempts':1,
            'same_admitted_unchanged_program_contract':True,
            'arbitrary_runtime_code_monkeypatch_detection_claimed':False,
            'incomplete_outputs_must_resume_or_charge_unresolved_probability':True}
        return result


def run_one_shot(program,depth,*,training_samples,cap,holdout_samples,
                 threshold,confidence,training_rng,holdout_rng,walker_rng,query_budget=1000):
    partition=train_partition(program,depth,samples=training_samples,cap=cap,rng=training_rng)
    certificate=validate_partition(program,partition,samples=holdout_samples,
        threshold=threshold,confidence=confidence,rng=holdout_rng)
    walker=CoherenceWalker(program,partition,certificate,query_budget=query_budget)
    return {'partition':partition,'certificate':certificate,
        'sample':walker.run(walker_rng),'live_walker':walker,
        'outer_branch':'APPROXIMATE_CERTIFIED' if walker.accepted else 'AUTOMATIC_EXACT_FALLBACK',
        'false_acceptance_unconditional_bound':str(F(confidence)),
        'fixed_attempt_budget':1}
