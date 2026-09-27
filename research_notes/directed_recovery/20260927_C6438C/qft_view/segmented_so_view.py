"""Versioned outer guard with complete segmented bytes and frozen fallback.

No scientific arithmetic is changed. The immutable token is derived only from
the actual admitted SOTraceBank, never accepted as caller-supplied authority.
"""
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
POLICY = BASE/'sep27-qft-trace/policy_execution'
TRACE = BASE/'sep27-qft-trace/trace_bank'
LEGACY = BASE/'sep27-qft-uniform/word_certificates'
POLICY_SHA = '62121d7c1e1a7eafff452990b991ddfe027e65ada5e980881aa4d716de92bd20'
TRACE_SHA = 'e2f7f839a8b6826ee3edff7b06070dd91f3e90e7f29278d56e1682d608c6b18d'
LEGACY_SHA = 'c3e8156b5c7573778cd1e781f23e82394c83842a9f4655b59c9659035dc62ce3'
PINS = {POLICY/'so_trace_feedback.py': POLICY_SHA,
        TRACE/'so_trace_certificates.py': TRACE_SHA,
        LEGACY/'word_certificates.py': LEGACY_SHA}
PROFILE = 'SEGMENTED_STRICT_SO_VIEW_WITH_FROZEN_FALLBACK_V1'


def verify_dependencies():
    for path, expected in PINS.items():
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('segmented-view dependency changed: '+str(path))


verify_dependencies()
sys.path.insert(0, str(POLICY))
from so_trace_feedback import (BoundaryCheckedSOTrace, SOTraceUniformFeedbackGram,
    SOTraceBank, public_entry, packed, strict_bytes, CursorReplayError, BOUNDARY_SHA)
from word_certificates import _program_view, strict_bytes as metadata_bytes


def segment_raw_view(raw):
    """Pure encoding helper; it performs no program or certificate admission."""
    if type(raw) is not tuple or len(raw) != 6:
        raise ValueError('frozen six-field native view required')
    if type(raw[-2]) is not bytes or type(raw[-1]) is not bytes:
        raise ValueError('frozen metadata JSON byte fields required')
    return (metadata_bytes(raw[:-2]), raw[-2], raw[-1])


def compare_raw_or_frozen(raw, expected, frozen_check):
    """Representation lemma helper; a fallback callable is not an admission API."""
    if (type(expected) is not tuple or len(expected) != 3
            or any(type(part) is not bytes for part in expected)):
        raise ValueError('three immutable expected JSON byte strings required')
    if segment_raw_view(raw) == expected:
        return 'SEGMENTED_FAST_ACCEPT'
    frozen_check()
    return 'FROZEN_COMPATIBILITY_ACCEPT'


@dataclass(frozen=True)
class _AdmittedViewToken:
    bank: SOTraceBank
    bank_binding_sha256: str
    admitted_view_bytes: bytes
    segments: tuple
    profile: str
    adapter_source_sha256: str
    token_sha256: str


def _derive_token(bank, adapter_source):
    if type(bank) is not SOTraceBank or type(bank._view_bytes) is not bytes:
        raise ValueError('actual immutable SO bank view required')
    decoded = json.loads(bank._view_bytes)
    if type(decoded) is not dict or set(decoded) != {'native_fields','phase_bindings','codec_binding'}:
        raise ValueError('frozen admitted wrapper schema mismatch')
    if metadata_bytes(decoded) != bank._view_bytes:
        raise ValueError('admitted wrapper is not in canonical frozen encoding')
    segments = tuple(metadata_bytes(decoded[key]) for key in
                     ('native_fields','phase_bindings','codec_binding'))
    token_payload = {'profile': PROFILE, 'bank_binding_sha256': bank.binding_sha256,
        'adapter_source_sha256': adapter_source,
        'source_pins': {path.name: expected for path, expected in PINS.items()},
        'segments': [part.decode('utf-8') for part in segments]}
    digest = hashlib.sha256(metadata_bytes(token_payload)).hexdigest()
    return _AdmittedViewToken(bank, bank.binding_sha256, bank._view_bytes,
                              segments, PROFILE, adapter_source, digest)


class SegmentedBoundarySOTrace(BoundaryCheckedSOTrace):
    policy = 'DROP_OLDEST_SO_TRACE_BOUND_WITH_SEGMENTED_COMPATIBLE_GUARD_V1'

    def __init__(self, program, epsilon, *, query_budget=1000, certificate_bank=None):
        verify_dependencies()
        # The frozen constructor calls the actual bank check directly; it does
        # not dispatch an outer public entry before our token exists. Its own
        # dependency checks and cold admission, when requested, remain paid.
        super().__init__(program, epsilon, query_budget=query_budget,
                         certificate_bank=certificate_bank)
        self._own_source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        token = _derive_token(self.word_certificates, self._own_source)
        self._view_token = self._admitted_view_token = token
        self._view_stats = {'constructor_frozen_checks': 1, 'token_derivations': 1,
            'segmented_check_attempts': 0, 'raw_view_construction_failures': 0,
            'fast_accepts': 0, 'compatibility_checks': 0,
            'compatibility_accepts': 0, 'compatibility_rejections': 0,
            'bank_identity_rejections': 0, 'token_identity_rejections': 0}

    def _frozen_compatibility_check(self):
        self._view_stats['compatibility_checks'] += 1
        try:
            # Call the unmodified exact class method, without an instance
            # replacement or a weakened metadata representation.
            SOTraceBank.check(self.word_certificates, self.program)
        except BaseException:
            self._view_stats['compatibility_rejections'] += 1
            raise
        self._view_stats['compatibility_accepts'] += 1

    def _full_boundary_check(self):
        self._check()  # unchanged inner Adaptive snapshot and committed ledger
        token = self._view_token
        if (type(self.word_certificates) is not SOTraceBank
                or self.word_certificates is not self._admitted_view_token.bank
                or self.word_certificates.binding_sha256 != self._certificate_binding):
            self._view_stats['bank_identity_rejections'] += 1
            raise ValueError('exact admitted SO bank identity changed')
        if (type(token) is not _AdmittedViewToken or token is not self._admitted_view_token
                or token.profile != PROFILE or token.adapter_source_sha256 != self._own_source
                or token.bank_binding_sha256 != self._certificate_binding
                or token.admitted_view_bytes is not self.word_certificates._view_bytes):
            self._view_stats['token_identity_rejections'] += 1
            raise ValueError('immutable admitted segmented token changed')
        self._guard_stats['bank_check_attempts'] += 1
        self._view_stats['segmented_check_attempts'] += 1
        try:
            raw = _program_view(self.program)
        except BaseException:
            self._view_stats['raw_view_construction_failures'] += 1
            raise
        route = compare_raw_or_frozen(raw, token.segments, self._frozen_compatibility_check)
        if route == 'SEGMENTED_FAST_ACCEPT':
            self._view_stats['fast_accepts'] += 1
        self._guard_stats['bank_check_successes'] += 1
        self.policy_stats['certificate_binding_checks'] += 1

    def _guard_diagnostics(self):
        result = super()._guard_diagnostics()
        token = self._admitted_view_token
        result.update({'view_profile': PROFILE, 'segmented_adapter_source_sha256': self._own_source,
            'view_token_sha256': token.token_sha256, 'view_stats': deepcopy(self._view_stats),
            'segment_bytes': [len(part) for part in token.segments],
            'view_comparison_is_full_bytes_not_hash_only': True,
            'logical_bank_check_counters_include_segmented_checks': True,
            'frozen_bank_check_invocations': (self._view_stats['constructor_frozen_checks']+
                                             self._view_stats['compatibility_checks'])})
        return result

    # The other six methods inherit exactly one existing @public_entry layer.
    # These two overrides call the undecorated policy base, avoiding a second
    # wrapper and preserving the prior nested guard topology.
    @public_entry
    def cursor(self):
        result = SOTraceUniformFeedbackGram.cursor(self)
        result.update({'schema': 'BRC_SEGMENTED_SO_TRACE_CURSOR_V1',
            'guard_contract': self.guard_contract, 'view_profile': PROFILE,
            'so_policy_parent_source_sha256': POLICY_SHA,
            'boundary_guard_source_sha256': BOUNDARY_SHA,
            'view_token_sha256': self._admitted_view_token.token_sha256})
        return result

    @public_entry
    def evidence(self):
        result = SOTraceUniformFeedbackGram.evidence(self)
        result.update({'guard_contract': self.guard_contract, 'view_profile': PROFILE,
            'so_policy_parent_source_sha256': POLICY_SHA,
            'boundary_guard_source_sha256': BOUNDARY_SHA,
            'view_token_sha256': self._admitted_view_token.token_sha256,
            'status': 'AUTHOR_EXECUTED_IF_CALLED; SEGMENTED_STRICT_VIEW_WITH_FROZEN_FALLBACK'})
        return result

    # Frozen classmethod restore constructs cls, repeats actual bank admission,
    # derives a fresh token, then strictly compares the complete new cursor.
