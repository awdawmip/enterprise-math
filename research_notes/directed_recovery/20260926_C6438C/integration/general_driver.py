# Derived with explicit postprocessor injection; frozen driver is unmodified.
"""Exact streaming compiled-Shor readout and bounded factor attempts.

The caller supplies a StreamingProgram factory and a randrange interface. This
reuses Stage58's exact rational software draw, not a physical randomness model.
No order, factor, reference distribution, or reference QFT is supplied to a run.
"""
from general_streaming import ROOT
import sys
sys.path.insert(0, str(ROOT.parent / "sparse"))
from sparse_modular import sparse_classical_postprocess
from fractions import Fraction
from stage58.coupled_reader import choose
from stage80.fixed_phase import norm
from stage78.shor_benchmark import classical_postprocess, gcd_brc


def sample_once(program, rng, *, postprocess=sparse_classical_postprocess):
    """One history, keeping raw branch amplitudes and all residual modes.

    Program protocol: .N, .a, .t, initial()->(state,den), and
    branches(state,den,history)->((state0,den0),(state1,den1)).
    rng.randrange(n) must return a uniform integer in [0,n), conditional on
    the entire preceding history, for the exact-law
    theorem. A seeded PRNG is only a reproducible software demonstration.
    """
    state, den = program.initial()
    if norm(state, den) != 1:
        raise ValueError('Initial program must have unit total mass')
    history = ()
    events = []
    for i in range(program.t):
        before = norm(state, den)
        if before <= 0:
            raise ValueError('Cannot condition on a zero-mass history')
        children = program.branches(state, den, history)
        masses = [norm(s, d) for s, d in children]
        if len(masses) != 2 or sum(masses) != before:
            raise AssertionError('Instrument completeness failed')
        p0 = masses[0] / before
        try:
            bit = 1 if p0 == 0 else 0 if p0 == 1 else choose(p0, rng)
        except (StopIteration, EOFError):
            return {'status': 'INCOMPLETE_RANDOM_SOURCE', 'N': program.N,
                    'a': program.a, 't': program.t, 'history': history,
                    'events': events, 'next_round': i,
                    'resume_amplitude_denominator': str(den),
                    'resume_state': [{'key': list(k), 'row': list(map(str, v))}
                                     for k, v in sorted(state.items())],
                    'note': 'Raw state is before the unfinished round; preserve prefix, do not condition away this outcome.'}
        if masses[bit] <= 0:
            raise AssertionError('Random interface selected a zero-mass branch')
        state, den = children[bit]
        history += (bit,)
        events.append({'round': i, 'bit': bit, 'conditional_probability':
                       str(masses[bit] / before), 'history_mass': str(masses[bit]),
                       'endpoints': len(state), 'amplitude_denominator_bits': den.bit_length()})
    k = sum(bit << i for i, bit in enumerate(history))
    product = Fraction(1)
    for event in events:
        product *= Fraction(event['conditional_probability'])
    if product != norm(state, den):
        raise AssertionError('Conditional probabilities did not telescope')
    post = postprocess(program.N, program.a, program.t, k)
    return {'N': program.N, 'a': program.a, 't': program.t, 'k': k,
            'history': history, 'history_probability': str(product),
            'events': events, 'postprocessing': post}


def factor_attempts(N, t, max_attempts, rng, program_factory, bases=None, *, postprocess=sparse_classical_postprocess):
    """Return a verified nontrivial factor or an explicit bounded retry result.

    Random-base policy uses rng.randrange(2,N-1), conditionally uniform on
    {2,...,N-2}. Supplying bases makes that
    externally chosen policy explicit; exhaustion is returned, never hidden.
    This is a factor-finding procedure, not a primality certificate or recursive
    complete factorization. No trial-division fallback is used.
    """
    if not isinstance(N, int) or isinstance(N, bool) or N < 2:
        raise ValueError('N must be an integer >= 2')
    if not isinstance(max_attempts, int) or isinstance(max_attempts, bool) or max_attempts < 1:
        raise ValueError('max_attempts must be a positive integer')
    if not isinstance(t, int) or isinstance(t, bool) or t < 2 or t % 2:
        raise ValueError('Frozen Stage80 contract requires positive even t >= 2')
    if N <= 3:
        return {'status': 'NO_NONTRIVIAL_FACTOR_SMALL_INPUT', 'N': N, 'attempts': [], 'factors': []}
    if N % 2 == 0:
        return {'status': 'FACTOR_EVEN_PRECHECK', 'N': N, 'attempts': [], 'factors': [2]}
    base_iter = iter(bases) if bases is not None else None
    attempts = []
    for j in range(max_attempts):
        if base_iter is not None:
            try:
                a = next(base_iter)
            except StopIteration:
                return {'status': 'BASE_POLICY_EXHAUSTED', 'N': N, 'attempts': attempts, 'factors': []}
        else:
            try:
                a = rng.randrange(2, N - 1)
            except (StopIteration, EOFError):
                return {'status': 'INCOMPLETE_RANDOM_SOURCE', 'N': N,
                        'phase': 'BASE_SELECTION', 'attempts': attempts, 'factors': []}
        if not isinstance(a, int) or isinstance(a, bool) or not 2 <= a < N:
            raise ValueError('Each base must satisfy 2 <= a < N')
        d = gcd_brc(a, N)
        if 1 < d < N:
            attempts.append({'attempt': j + 1, 'a': a, 'status': 'FACTOR_GCD_PRECHECK', 'factor': d})
            return {'status': 'FACTOR_GCD_PRECHECK', 'N': N, 'attempts': attempts, 'factors': [d]}
        record = sample_once(program_factory(N, a, t), rng, postprocess=postprocess)
        record['attempt'] = j + 1
        attempts.append(record)
        if record.get('status') == 'INCOMPLETE_RANDOM_SOURCE':
            return {'status': 'INCOMPLETE_RANDOM_SOURCE', 'N': N,
                    'phase': 'CONTROL_READOUT', 'attempts': attempts, 'factors': []}
        factors = record['postprocessing']['factors']
        if factors:
            if not all(1 < f < N and N % f == 0 for f in factors):
                raise AssertionError('Invalid factor returned by postprocessor')
            return {'status': 'FACTORS', 'N': N, 'attempts': attempts, 'factors': factors}
    return {'status': 'RETRY_LIMIT', 'N': N, 'attempts': attempts, 'factors': []}
