"""Versioned SO-trace uniform policy with optional frozen outer guard.

No old bank impersonation. Adaptive transactions and actual observer formulas
are retained; the new immutable bank supplies a valid squared-norm upper bound.
"""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
ADAPTIVE=BASE/'sep27-qft-adaptive/adaptive_execution'
UNIFORM=BASE/'sep27-qft-uniform/uniform_execution'
BOUNDARY=BASE/'sep27-qft-boundary/boundary_execution'
TRACE=ROOT.parent/'trace_bank'
ADAPTIVE_SHA='86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45'
UNIFORM_SHA='755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28'
BOUNDARY_SHA='875133020ba713af755d19b121f416938193835c3e2c9b7e6ab228c19b814c83'
TRACE_SHA='e2f7f839a8b6826ee3edff7b06070dd91f3e90e7f29278d56e1682d608c6b18d'
PINS={ADAPTIVE/'adaptive_feedback.py':ADAPTIVE_SHA,
      UNIFORM/'uniform_feedback.py':UNIFORM_SHA,
      BOUNDARY/'boundary_uniform.py':BOUNDARY_SHA,
      TRACE/'so_trace_certificates.py':TRACE_SHA}


def verify_dependencies():
    for path,expected in PINS.items():
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise ValueError('frozen policy dependency changed: '+str(path))


verify_dependencies()
for directory in (ADAPTIVE,UNIFORM,BOUNDARY,TRACE):sys.path.insert(0,str(directory))
from adaptive_feedback import AdaptiveFeedbackGram,packed,strict_bytes,CursorReplayError
from uniform_feedback import UniformFeedbackGram
from boundary_uniform import BoundaryCheckedUniform as FrozenBoundary,public_entry
from so_trace_certificates import SOTraceBank


class SOTraceUniformFeedbackGram(AdaptiveFeedbackGram):
    policy='DROP_OLDEST_WORD_IF_SO_TRACE_BOUND_CERTIFIES_V1'

    def __init__(self,program,epsilon,*,query_budget=1000,certificate_bank=None):
        verify_dependencies()
        if certificate_bank is not None and type(certificate_bank) is not SOTraceBank:
            raise ValueError('actual exact-type SOTraceBank required')
        super().__init__(program,epsilon,query_budget=query_budget)
        self.word_certificates=SOTraceBank(program) if certificate_bank is None else certificate_bank
        self.word_certificates.check(program)
        self.certificate_admission_mode=('COLD_BUILD' if certificate_bank is None
                                        else 'REUSE_TRUSTED_IN_PROCESS_SO_TRACE_BANK_AFTER_BINDING_CHECK')
        self._own_source=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        self.policy_stats.update({'uniform_certificate_lookups':0,
            'prefix_covariance_defect_calls':0,'prefix_mass_observations_for_policy':0,
            'certificate_binding_checks':1})

    def _check(self):
        AdaptiveFeedbackGram._check(self)
        if hasattr(self,'word_certificates'):
            if type(self.word_certificates) is not SOTraceBank:
                raise ValueError('actual exact-type SOTraceBank required')
            self.word_certificates.check(self.program)
            self.policy_stats['certificate_binding_checks']+=1

    def defect(self,covariance,reference_ids,selected_ids):
        raise ValueError('SO trace policy does not execute a prefix-specific defect')

    def prepare_next(self):
        # Same actual scalar expressions and temporal omission as frozen
        # Uniform.prepare_next; only typed certificate semantics are new.
        self._check()
        if len(self.history)>=self.program.t:
            raise ValueError('terminal prefix has no next decision')
        if self.pending is not None:
            self.policy_stats['prepared_cache_hits']+=1
            return json.loads(packed(self.pending))
        depth=len(self.history)
        reference=tuple(depth-c+1 for c in range(depth) if self.history[c])
        candidate=reference[1:] if reference else reference
        spent=self._sum('committed_charge',(step.charge for step in self.steps))
        remaining=self._observe('remaining_charge',((self.epsilon,),(-F(1),spent)))
        if not 0<=remaining<=self.epsilon:raise AssertionError('budget ledger inconsistent')
        selected,charge,margin,witness,certificate_id=reference,F(0),None,None,None
        method,exact=None,None
        decision='REFERENCE_ZERO_BUDGET'
        if not reference:
            decision='IDENTITY';self.policy_stats['identity_steps']+=1
        elif remaining:
            self.policy_stats['candidate_tests']+=1
            cert=self.word_certificates.get(reference[0])
            self.policy_stats['uniform_certificate_lookups']+=1
            certificate_id=cert.certificate_sha256
            method,exact=cert.bound_method,cert.bound_is_exact
            if cert.bound_valid:
                witness=cert.s
                if not 0<=witness<=4:raise AssertionError('admitted trace bound outside [0,4]')
                margin=self._observe('uniform_rational_trace_distance_test',
                    ((F(8),witness),(-F(1),witness,witness),(-F(16),remaining,remaining)))
                if margin<=0:
                    selected,charge,decision=candidate,remaining,'OMIT_OLDEST_UNIFORM_CERTIFIED'
                    self.policy_stats['accepted_omissions']+=1
                else:
                    decision='REFERENCE_UNIFORM_BOUND_TOO_LARGE'
                    self.policy_stats['reference_fallbacks']+=1
            else:
                decision='REFERENCE_TRACE_BOUND_UNAVAILABLE'
                self.policy_stats['reference_fallbacks']+=1
        else:self.policy_stats['reference_fallbacks']+=1
        self.pending={'history':self.history,'reference_ids':reference,
            'candidate_ids':candidate,'selected_ids':selected,'remaining_before':remaining,
            'charge':charge,'decision':decision,'uniform_s':witness,
            'rational_test_margin':margin,'word_certificate_sha256':certificate_id,
            'certificate_bank_sha256':self.word_certificates.binding_sha256,
            'bound_method':method,'bound_is_exact':exact,
            'certificate_interface':'BRC_SO_TRACE_BANK_V1',
            'prefix_mass_observed_for_policy':False,'prefix_covariance_defect_observed':False,
            'zero_mass_extension':'same universal bound; probabilities refuses zero-mass conditioning'}
        return json.loads(packed(self.pending))

    def cursor(self):
        result=super().cursor()
        result.update({'schema':'BRC_SO_TRACE_UNIFORM_CURSOR_V1',
            'certificate_bank_sha256':self.word_certificates.binding_sha256,
            'trace_bank_source_sha256':TRACE_SHA,'parent_source_sha256':ADAPTIVE_SHA,
            'uniform_template_source_sha256':UNIFORM_SHA})
        return result

    # This frozen routine constructs cls, replays its public transactions and
    # compares the complete new cursor bytes. It never insists on the old bank
    # type itself; the new constructor above enforces the actual new bank type.
    restore=classmethod(UniformFeedbackGram.restore.__func__)

    def evidence(self):
        result=super().evidence()
        result.update({'certificate_bank_sha256':self.word_certificates.binding_sha256,
            'certificate_admission_mode':self.certificate_admission_mode,
            'trace_bank_source_sha256':TRACE_SHA,'parent_source_sha256':ADAPTIVE_SHA,
            'uniform_template_source_sha256':UNIFORM_SHA,
            'status':'AUTHOR_EXECUTED_IF_CALLED; VERSIONED_SO_TRACE_POLICY'})
        if self.certificate_admission_mode=='COLD_BUILD':
            result['cold_certificate_evidence']=self.word_certificates.evidence()
        return result


class BoundaryCheckedSOTrace(SOTraceUniformFeedbackGram):
    policy='DROP_OLDEST_SO_TRACE_BOUND_WITH_OUTER_PUBLIC_GUARD_V1'
    guard_contract=FrozenBoundary.guard_contract
    # Exact pinned implementation includes owner/depth checks, BaseException
    # diagnostic capture and finally restoration. No new concurrency promise.
    _public_boundary=FrozenBoundary._public_boundary

    def __init__(self,program,epsilon,*,query_budget=1000,certificate_bank=None):
        self._guard_depth=0;self._guard_owner=None
        self._guard_stats={'outer_entries':0,'nested_entries':0,'max_reentrant_depth':0,
            'bank_check_attempts':0,'bank_check_successes':0,
            'inherited_constructor_bank_checks':0,'adaptive_snapshot_ledger_checks':0,
            'outer_by_method':{},'nested_by_method':{},'exception_events':[]}
        super().__init__(program,epsilon,query_budget=query_budget,certificate_bank=certificate_bank)
        self._guard_stats['bank_check_attempts']=1
        self._guard_stats['bank_check_successes']=1
        self._guard_stats['inherited_constructor_bank_checks']=1
        self._certificate_binding=self.word_certificates.binding_sha256

    def _check(self):
        self._guard_stats['adaptive_snapshot_ledger_checks']+=1
        AdaptiveFeedbackGram._check(self)

    def _full_boundary_check(self):
        self._check()
        if type(self.word_certificates) is not SOTraceBank:
            raise ValueError('actual exact-type SOTraceBank required')
        if self.word_certificates.binding_sha256!=self._certificate_binding:
            raise ValueError('admitted SO trace certificate identity changed')
        self._guard_stats['bank_check_attempts']+=1
        self.word_certificates.check(self.program)
        self._guard_stats['bank_check_successes']+=1
        self.policy_stats['certificate_binding_checks']+=1

    def _guard_diagnostics(self):
        return {'contract':self.guard_contract,'active_depth':self._guard_depth,
            'owner_active':self._guard_owner is not None,'stats':deepcopy(self._guard_stats),
            'uniform_template_source_sha256':UNIFORM_SHA,'trace_bank_source_sha256':TRACE_SHA,
            'boundary_guard_source_sha256':BOUNDARY_SHA,
            'ordinary_trusted_python_objects':True,
            'external_mutation_during_outer_call_supported':False,
            'counters_are_host_metadata_not_native_arithmetic':True}

    @public_entry
    def gamma(self,depth,residue):return super().gamma(depth,residue)

    @public_entry
    def mass(self):return super().mass()

    @public_entry
    def probabilities(self):return super().probabilities()

    @public_entry
    def advance(self,bit):return super().advance(bit)

    @public_entry
    def prepare_next(self):return super().prepare_next()

    @public_entry
    def cursor(self):
        result=super().cursor()
        result.update({'schema':'BRC_BOUNDARY_SO_TRACE_CURSOR_V1',
            'guard_contract':self.guard_contract,'boundary_guard_source_sha256':BOUNDARY_SHA})
        return result

    @public_entry
    def evidence(self):
        result=super().evidence()
        result.update({'guard_contract':self.guard_contract,'boundary_guard_source_sha256':BOUNDARY_SHA,
            'status':'AUTHOR_EXECUTED_IF_CALLED; OUTER_GUARDED_SO_TRACE_POLICY'})
        return result

    @public_entry
    def report(self):return super().report()
