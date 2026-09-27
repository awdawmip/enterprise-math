"""Outer-public-entry certificate checks for the frozen uniform policy.

Native arithmetic and policy choices are inherited unchanged. The synchronous
call contract excludes external program mutation during one outer call and
arbitrary Python monkeypatching; it does not offer a concurrent-object API.
"""
from contextlib import contextmanager
from copy import deepcopy
from functools import wraps
from pathlib import Path
from threading import get_ident
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
UNIFORM = BASE/'sep27-qft-uniform/uniform_execution'
WORDS = BASE/'sep27-qft-uniform/word_certificates'
UNIFORM_SHA = '755d398a19881508112c9e360c94bf10133681af8d3cbdbb103accdecc306e28'
WORDS_SHA = 'c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3'
sys.path.insert(0,str(UNIFORM))
from uniform_feedback import (UniformFeedbackGram, AdaptiveFeedbackGram,
                              WordCertificateBank, packed, strict_bytes,
                              CursorReplayError)


def public_entry(method):
    @wraps(method)
    def guarded(self,*args,**kwargs):
        with self._public_boundary(method.__name__):
            value=method(self,*args,**kwargs)
        # Metadata-only capture after this entry's finally has restored depth.
        # A nested report can legitimately record its still-active parent depth.
        if method.__name__ in ('report','evidence'):
            value['boundary_guard']=self._guard_diagnostics()
        return value
    return guarded


class BoundaryCheckedUniform(UniformFeedbackGram):
    policy='DROP_OLDEST_UNIFORM_BOUND_WITH_OUTER_PUBLIC_GUARD_V1'
    guard_contract='SYNCHRONOUS_OUTER_ENTRY_FULL_BANK_INNER_SNAPSHOT_LEDGER_V1'

    def __init__(self,program,epsilon,*,query_budget=1000,certificate_bank=None):
        for path,expected in ((UNIFORM/'uniform_feedback.py',UNIFORM_SHA),
                              (WORDS/'word_certificates.py',WORDS_SHA)):
            if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
                raise ValueError('frozen uniform/certificate dependency changed')
        self._guard_depth=0
        self._guard_owner=None
        self._guard_stats={
            'outer_entries':0,'nested_entries':0,'max_reentrant_depth':0,
            'bank_check_attempts':0,'bank_check_successes':0,
            'inherited_constructor_bank_checks':0,
            'adaptive_snapshot_ledger_checks':0,
            'outer_by_method':{},'nested_by_method':{},'exception_events':[]}
        super().__init__(program,epsilon,query_budget=query_budget,
                         certificate_bank=certificate_bank)
        self._guard_stats['bank_check_attempts']=1
        self._guard_stats['bank_check_successes']=1
        self._guard_stats['inherited_constructor_bank_checks']=1
        self._certificate_binding=self.word_certificates.binding_sha256
        self._own_source=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    def _check(self):
        """Private computational/ledger guard, retained inside every recurrence."""
        self._guard_stats['adaptive_snapshot_ledger_checks']+=1
        AdaptiveFeedbackGram._check(self)

    def _full_boundary_check(self):
        self._check()
        if type(self.word_certificates) is not WordCertificateBank:
            raise ValueError('actual frozen WordCertificateBank required')
        if self.word_certificates.binding_sha256!=self._certificate_binding:
            raise ValueError('admitted word certificate identity changed')
        self._guard_stats['bank_check_attempts']+=1
        self.word_certificates.check(self.program)
        self._guard_stats['bank_check_successes']+=1
        self.policy_stats['certificate_binding_checks']+=1

    @contextmanager
    def _public_boundary(self,name):
        owner=get_ident()
        outer=self._guard_depth==0
        if not outer and self._guard_owner!=owner:
            raise ValueError('concurrent use of one boundary-checked object is unsupported')
        if outer:
            self._guard_owner=owner
        self._guard_depth+=1
        group='outer' if outer else 'nested'
        self._guard_stats[group+'_entries']+=1
        by_method=self._guard_stats[group+'_by_method']
        by_method[name]=by_method.get(name,0)+1
        self._guard_stats['max_reentrant_depth']=max(
            self._guard_stats['max_reentrant_depth'],self._guard_depth)
        try:
            if outer:
                self._full_boundary_check()
            yield
        except BaseException as error:
            self._guard_stats['exception_events'].append({
                'method':name,'outer':outer,'depth':self._guard_depth,
                'exception_type':type(error).__name__,'message':str(error)})
            raise
        finally:
            self._guard_depth-=1
            if outer:
                self._guard_owner=None
                if self._guard_depth!=0:
                    raise AssertionError('public guard depth did not restore to zero')

    def _guard_diagnostics(self):
        return {'contract':self.guard_contract,'active_depth':self._guard_depth,
            'owner_active':self._guard_owner is not None,
            'stats':deepcopy(self._guard_stats),
            'uniform_source_sha256':UNIFORM_SHA,'word_source_sha256':WORDS_SHA,
            'ordinary_trusted_python_objects':True,
            'external_mutation_during_outer_call_supported':False,
            'counters_are_host_metadata_not_native_arithmetic':True}

    @public_entry
    def gamma(self,depth,residue):
        return super().gamma(depth,residue)

    @public_entry
    def mass(self):
        return super().mass()

    @public_entry
    def probabilities(self):
        return super().probabilities()

    @public_entry
    def advance(self,bit):
        return super().advance(bit)

    @public_entry
    def prepare_next(self):
        return super().prepare_next()

    @public_entry
    def cursor(self):
        result=super().cursor()
        result.update({'schema':'BRC_BOUNDARY_UNIFORM_CURSOR_V1',
            'uniform_source_sha256':UNIFORM_SHA,'guard_contract':self.guard_contract})
        return result

    @public_entry
    def evidence(self):
        result=super().evidence()
        result.update({'uniform_source_sha256':UNIFORM_SHA,
            'guard_contract':self.guard_contract,
            'status':'AUTHOR_EXECUTED_IF_CALLED; OUTER_GUARD_OPTIMIZATION_ONLY'})
        return result

    @public_entry
    def report(self):
        return super().report()

    # The inherited strict classmethod restore constructs cls, replays committed
    # public advance/prepare calls, and compares the complete new cursor bytes.
    # Its exception evidence is captured after the failed public guard unwinds.
    # Old-stage cursors intentionally fail: schema/policy/source are different.
