"""Explicit column-compiler injection into the proven terminal instrument.

The inherited branch map is unchanged. Only its complete modular permutation
compiler and its supplied full-dimensional native phase bank are replaceable.
"""
import os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PREVIOUS = Path(os.environ.get('BRC_STREAMING_PREVIOUS', str(ROOT.parents[1] / 'sep26-shor-alternative')))
sys.path.insert(0, str(PREVIOUS / 'algorithm_intake'))
from terminal_instrument import StreamingProgram as FrozenStreamingProgram


class GeneralStreamingProgram(FrozenStreamingProgram):
    def __init__(self, N, a, t, bank, dim, *, column_factory):
        integer = lambda x: isinstance(x, int) and not isinstance(x, bool)
        if not integer(N) or N < 3: raise ValueError('N >= 3 required')
        if not integer(a) or not 1 <= a < N: raise ValueError('1 <= a < N required')
        if not integer(t) or t < 2 or t % 2: raise ValueError('even t >= 2 required')
        if not integer(dim) or dim < 2: raise ValueError('complete internal dimension required')
        if any(m not in bank or bank[m].dim != dim for m in range(2, t + 1)):
            raise ValueError('all complete phase maps must use one common carrier')
        self.N, self.a, self.t, self.bank, self.dim = N, a, t, bank, dim
        b = a; powers = []; tables = []
        for _ in range(t):
            table = column_factory(N, b)
            powers.append(b); tables.append(table); b = table[b]
        self.modular_powers = tuple(reversed(powers))
        # Each square is read from the same certified BRC column, retaining
        # the dependency on the actual modular compiler even for input labels.
        self.tables = tuple(reversed(tables))
        W = 1 << (N - 1).bit_length()
        for table in self.tables:
            if len(table) != W or set(table) != set(range(W)):
                raise ValueError('column compiler must return a full permutation')
        self.metrics = {'branch_calls': 0, 'empty_branch_calls': 0,
            'phase_calls': 0, 'H4_calls': 0, 'modular_column_applications': 0,
            'peak_endpoints': 0, 'peak_scalar_slots': 0,
            'peak_nonzero_scalars': 0, 'peak_denominator_bits': 0,
            'boundary_spectator_nonzero_seen': False}
        self.depth_metrics = {}


class NativeWordPower:
    """Literal composition of an already fully certified native phase word.

    Exponent is a word repeat count, never a target angle or a period reduction.
    Forward and inverse operations retain the entire common carrier.
    """
    def __init__(self, root, exponent):
        if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent < 1:
            raise ValueError('positive literal repeat count required')
        self.root, self.exponent, self.dim = root, exponent, root.dim
        self.den = root.den ** exponent
        self.h4_count = root.h4_count * exponent
        self.sign_count = root.sign_count * exponent
        self.swap_count = root.swap_count * exponent
        self.inverse_phase_word = root.inverse_phase_word * exponent

    def apply_numer(self, v, inverse=False):
        for _ in range(self.exponent):
            v = self.root.apply_numer(v, inverse=inverse)
        return v


def common_phase3_bank(bank):
    if 3 not in bank or 4 not in bank: raise ValueError('phase 3 and 4 required')
    result = dict(bank)
    result[3] = NativeWordPower(bank[4], 2)
    return result
