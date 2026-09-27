"""History-consistent omission using a paid reusable actual-word norm bound.

Uniform certificates remove prefix-specific defect calculations, not the Gram
queries used by the underlying sampler. No random driver is implemented here.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
PARENT = BASE/'sep27-qft-adaptive/adaptive_execution'
PARENT_SHA = '86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45'
sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(ROOT.parent/'word_certificates'))
from adaptive_feedback import AdaptiveFeedbackGram, CursorReplayError, packed, digest, strict_bytes
from word_certificates import WordCertificateBank


class UniformFeedbackGram(AdaptiveFeedbackGram):
    policy = 'DROP_OLDEST_WORD_IF_REUSABLE_UNIFORM_BOUND_CERTIFIES_V1'

    def __init__(self, program, epsilon, *, query_budget=1000, certificate_bank=None):
        if hashlib.sha256((PARENT/'adaptive_feedback.py').read_bytes()).hexdigest() != PARENT_SHA:
            raise ValueError('frozen adaptive transaction source changed')
        super().__init__(program, epsilon, query_budget=query_budget)
        if certificate_bank is not None and type(certificate_bank) is not WordCertificateBank:
            raise ValueError('actual trusted WordCertificateBank required')
        self.word_certificates = (WordCertificateBank(program) if certificate_bank is None
                                  else certificate_bank)
        self.word_certificates.check(program)
        self.certificate_admission_mode = ('COLD_BUILD' if certificate_bank is None
                                           else 'REUSE_TRUSTED_IN_PROCESS_BANK_AFTER_BINDING_CHECK')
        self._own_source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        self.policy_stats.update({'uniform_certificate_lookups':0,
                                  'prefix_covariance_defect_calls':0,
                                  'prefix_mass_observations_for_policy':0,
                                  'certificate_binding_checks':1})

    def _check(self):
        super()._check()
        if hasattr(self, 'word_certificates'):
            self.word_certificates.check(self.program)
            self.policy_stats['certificate_binding_checks'] += 1

    def defect(self, covariance, reference_ids, selected_ids):
        raise ValueError('uniform policy does not execute a prefix-specific defect')

    def prepare_next(self):
        self._check()
        if len(self.history) >= self.program.t:
            raise ValueError('terminal prefix has no next decision')
        if self.pending is not None:
            self.policy_stats['prepared_cache_hits'] += 1
            return json.loads(packed(self.pending))
        depth = len(self.history)
        reference = tuple(depth-c+1 for c in range(depth) if self.history[c])
        candidate = reference[1:] if reference else reference
        spent = self._sum('committed_charge', (step.charge for step in self.steps))
        remaining = self._observe('remaining_charge', ((self.epsilon,),(-F(1),spent)))
        if not 0 <= remaining <= self.epsilon:
            raise AssertionError('budget ledger inconsistent')
        selected, charge, margin, witness, certificate_id = reference, F(0), None, None, None
        decision = 'REFERENCE_ZERO_BUDGET'
        if not reference:
            decision = 'IDENTITY'
            self.policy_stats['identity_steps'] += 1
        elif remaining:
            self.policy_stats['candidate_tests'] += 1
            cert = self.word_certificates.get(reference[0])
            self.policy_stats['uniform_certificate_lookups'] += 1
            certificate_id = cert.certificate_sha256
            if cert.accepted:
                witness = cert.s
                if not 0 <= witness <= 4:
                    raise AssertionError('admitted uniform bound outside [0,4]')
                margin = self._observe('uniform_rational_trace_distance_test',
                    ((F(8),witness),(-F(1),witness,witness),
                     (-F(16),remaining,remaining)))
                if margin <= 0:
                    selected, charge, decision = candidate, remaining, 'OMIT_OLDEST_UNIFORM_CERTIFIED'
                    self.policy_stats['accepted_omissions'] += 1
                else:
                    decision = 'REFERENCE_UNIFORM_BOUND_TOO_LARGE'
                    self.policy_stats['reference_fallbacks'] += 1
            else:
                decision = 'REFERENCE_WORD_CERTIFICATE_FAILED'
                self.policy_stats['reference_fallbacks'] += 1
        else:
            self.policy_stats['reference_fallbacks'] += 1
        self.pending = {'history':self.history, 'reference_ids':reference,
            'candidate_ids':candidate, 'selected_ids':selected,
            'remaining_before':remaining, 'charge':charge, 'decision':decision,
            'uniform_s':witness, 'rational_test_margin':margin,
            'word_certificate_sha256':certificate_id,
            'certificate_bank_sha256':self.word_certificates.binding_sha256,
            'prefix_mass_observed_for_policy':False,
            'prefix_covariance_defect_observed':False,
            'zero_mass_extension':'same universal bound; probabilities refuses zero-mass conditioning'}
        return json.loads(packed(self.pending))

    def cursor(self):
        cursor = super().cursor()
        cursor['schema'] = 'BRC_UNIFORM_FEEDBACK_CURSOR_V1'
        cursor['certificate_bank_sha256'] = self.word_certificates.binding_sha256
        cursor['parent_source_sha256'] = PARENT_SHA
        return cursor

    @classmethod
    def restore(cls, program, cursor, *, query_budget=1000, certificate_bank=None):
        if type(cursor) is not dict or type(cursor.get('history')) is not list:
            raise ValueError('strict cursor object and history required')
        if any(type(bit) is not int or bit not in (0,1) for bit in cursor['history']):
            raise ValueError('cursor bits must be integers, not booleans')
        new = cls(program, cursor.get('epsilon'), query_budget=query_budget,
                  certificate_bank=certificate_bank)
        try:
            for bit in cursor['history']:
                new.advance(bit)
            if cursor.get('pending_certificate_sha256') is not None:
                new.prepare_next()
            if strict_bytes(new.cursor()) != strict_bytes(cursor):
                raise ValueError('cursor differs from exact deterministic replay')
        except Exception as error:
            raise CursorReplayError('uniform cursor replay failed: '+str(error),new.evidence()) from error
        return new

    def evidence(self):
        result = super().evidence()
        result.update({'certificate_bank_sha256':self.word_certificates.binding_sha256,
                       'certificate_admission_mode':self.certificate_admission_mode,
                       'parent_source_sha256':PARENT_SHA,
                       'status':'AUTHOR_EXECUTED_IF_CALLED; NO_EFFICIENT_GRAM_ORACLE_CLAIM'})
        if self.certificate_admission_mode == 'COLD_BUILD':
            result['cold_certificate_evidence'] = self.word_certificates.evidence()
        return result
