"""Exact word-boundary codec for a verified common invariant carrier.

This retains the actual complete native source and every reachable residual.
It is NOT a six-spatial-axis model and does not truncate intermediate gates.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PACKAGE / 'new_word_compiler'))
from compiled_streaming import CompleteNativeWord


def integer(x):
    return isinstance(x, int) and not isinstance(x, bool)


@dataclass(frozen=True)
class ExactCarrierCodec:
    full_dim: int
    indices: tuple[int, ...]

    def __post_init__(self):
        if not integer(self.full_dim) or self.full_dim < 1:
            raise ValueError('positive full carrier dimension required')
        if (not self.indices or len(set(self.indices)) != len(self.indices)
                or any(not integer(i) or not 0 <= i < self.full_dim
                       for i in self.indices)):
            raise ValueError('distinct full-carrier coordinates required')

    @property
    def dim(self):
        return len(self.indices)

    def encode(self, row):
        if len(row) != self.full_dim or any(not integer(v) for v in row):
            raise ValueError('complete integer row required')
        selected = set(self.indices)
        if any(v != 0 for j, v in enumerate(row) if j not in selected):
            raise ValueError('nonzero omitted residual is not encodable')
        return tuple(row[j] for j in self.indices)

    def decode(self, row):
        if len(row) != self.dim or any(not integer(v) for v in row):
            raise ValueError('complete encoded integer row required')
        full = [0] * self.full_dim
        for j, value in zip(self.indices, row):
            full[j] = value
        return tuple(full)

    def encode_state(self, state):
        return {key: self.encode(row) for key, row in state.items()}

    def decode_state(self, state):
        return {key: self.decode(row) for key, row in state.items()}


@dataclass(frozen=True)
class RestrictedNativeWord:
    """Immutable exact integer columns derived from full actual native replay."""
    dim: int
    den: int
    columns: tuple[tuple[int, ...], ...]
    inverse_columns: tuple[tuple[int, ...], ...]
    inverse_phase_word: tuple
    h4_count: int
    sign_count: int
    swap_count: int
    full_dim: int
    indices: tuple[int, ...]
    source_columns_sha256: str

    def apply_numer(self, values, inverse=False):
        if len(values) != self.dim or any(not integer(v) for v in values):
            raise ValueError('complete encoded integer row required')
        columns = self.inverse_columns if inverse else self.columns
        result = [0] * self.dim
        for j, value in enumerate(values):
            if value:
                for i, coefficient in enumerate(columns[j]):
                    if coefficient:
                        result[i] += coefficient * value
        return result

    def binding_record(self):
        return {
            'schema': 'BRC_EXACT_WORD_BOUNDARY_CARRIER_CODEC_V1',
            'full_dim': self.full_dim, 'encoded_dim': self.dim,
            'indices': self.indices, 'denominator': self.den,
            'actual_full_columns_sha256': self.source_columns_sha256,
            'word': self.inverse_phase_word,
            'scope': 'only full native-word boundaries; omitted input coordinates must be exactly zero',
        }


def restrict_word(word, codec):
    """Rebuild full actual columns; prove block structure before projection.

    The supplied object's potentially mutable cached matrix is never trusted.
    Provenance is the normalized native word replayed by CompleteNativeWord.
    Restriction covers forward and inverse maps and requires identity on the
    complement. A rotated complement could also be safe for zero tail, but is
    deliberately outside this narrower implementation contract.
    """
    if type(word) is not CompleteNativeWord or word.dim != codec.full_dim:
        raise ValueError('complete actual native word on the declared carrier required')
    full = CompleteNativeWord(word.inverse_phase_word, codec.full_dim)
    if (full.den, full.columns, full.inverse_columns, full.columns_sha256) != (
            word.den, word.columns, word.inverse_columns, word.columns_sha256):
        raise ValueError('source word cached fields do not match native replay')
    selected = set(codec.indices)
    for matrix in (full.columns, full.inverse_columns):
        for j, column in enumerate(matrix):
            for i, value in enumerate(column):
                if (i in selected) != (j in selected) and value:
                    raise ValueError('cross-block coupling prevents this exact codec')
                if i not in selected and j not in selected:
                    if value != (full.den if i == j else 0):
                        raise ValueError('full word is not identity on the complement')
    forward = tuple(tuple(full.columns[j][i] for i in codec.indices)
                    for j in codec.indices)
    backward = tuple(tuple(full.inverse_columns[j][i] for i in codec.indices)
                     for j in codec.indices)
    return RestrictedNativeWord(
        codec.dim, full.den, forward, backward, full.inverse_phase_word,
        full.h4_count, full.sign_count, full.swap_count,
        codec.full_dim, codec.indices, full.columns_sha256)


def restrict_bank(bank, *, indices=tuple(range(6)), full_dim=61):
    codec = ExactCarrierCodec(full_dim, tuple(indices))
    if codec.indices[0] != 0:
        raise ValueError('streaming initial internal basis e0 must be the first encoded coordinate')
    restricted = {m: restrict_word(word, codec) for m, word in bank.items()}
    bindings = {str(m): value.binding_record() for m, value in restricted.items()}
    canonical = json.dumps(bindings, sort_keys=True, separators=(',', ':')).encode()
    return codec, restricted, {
        'schema': 'BRC_COMMON_INVARIANT_CARRIER_CERTIFICATE_V1',
        'full_dim': full_dim, 'encoded_dim': codec.dim,
        'indices': codec.indices, 'all_forward_inverse_blocks_checked': True,
        'input_requirement': 'exact zero complement, verified by codec.encode',
        'full_state_scalar_slot_ratio': f'{full_dim}/{codec.dim}',
        'binding_sha256': hashlib.sha256(canonical).hexdigest(),
        'phases': bindings,
        'claim': 'lossless representation of the reachable subspace; no claim of polynomial work-label count',
    }
