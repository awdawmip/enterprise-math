"""Original CF/gcd decisions with lazy modular columns and typed gcd execution.

The plain result has exactly the frozen sparse postprocessor's fields.
The optional trace retains power steps, requested column evidence and resource
receipts separately. No all-N modular table is constructed by either route.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
from lazy_modular import LazyModularFactory, source_binding
from stage78.shor_benchmark import denominators
from lazy_gcd import typed_gcd_trace
from stage45.brc_loop_recheck import CALLS


def _power(factory, N, a, exponent, capture):
    table = factory(N, a)
    rest, value, bit = exponent, 1, 0
    steps = []
    while rest:
        selected = rest & 1
        output = table[value] if selected else value
        rest >>= 1
        next_b = table[table.b] if rest else None
        if capture:
            steps.append({'bit': bit, 'selected': selected, 'input': value, 'output': output,
                'b': table.b, 'next_b': next_b,
                'permutation_certificate_sha256': table.certificate_sha256,
                'multiply_column': value if selected else None,
                'square_column': table.b if rest else None})
        value = output
        if rest:
            table = factory(N, next_b)
        bit += 1
    return value, {'exponent': exponent, 'value': value, 'steps': steps,
                   'host_exponent_bit_wiring_operations': 2*bit}


def _run(N, a, t, k, capture):
    start = len(CALLS)
    factory = LazyModularFactory()
    powers, gcds = [], []
    if k == 0:
        result = {'status': 'ZERO_PHASE_RETRY', 'factors': []}
    else:
        rejected = []
        result = None
        for q in denominators(k, 1 << t, N-1):
            value, power = _power(factory, N, a, q, capture)
            if capture:
                powers.append(power)
            if value != 1:
                rejected.append((q, 'NOT_RETURNING_EXPONENT'))
                continue
            if q % 2:  # inherited parity policy, not a modular-value propagator
                rejected.append((q, 'ODD_RETURNING_EXPONENT'))
                continue
            h, power = _power(factory, N, a, q//2, capture)
            if capture:
                powers.append(power)
            gcd_start = len(CALLS)
            minus_trace, plus_trace = typed_gcd_trace(h-1, N), typed_gcd_trace(h+1, N)
            minus, plus = minus_trace['value'], plus_trace['value']
            if capture:
                gcds.append({'returning_exponent':q,'half_power':h,
                             'inputs':[[h-1,N],[h+1,N]],'outputs':[minus,plus],
                             'native_kernel_calls_delta':len(CALLS)-gcd_start,
                             'typed_traces':[minus_trace,plus_trace],
                             'adder_digit_replays':sum(x['cost']['adder_digit_replays']
                                                       for x in (minus_trace,plus_trace)),
                             'executor':'lazy_gcd.typed_gcd_trace'})
            factors = sorted({minus, plus}-{1,N})
            if factors:
                result = {'status':'FACTORS','verified_returning_exponent':q,
                          'minimal_order_claimed':False,'factors':factors}
                break
            rejected.append((q, 'TRIVIAL_GCD_RETRY'))
        if result is None:
            result = {'status':'NO_FACTOR_THIS_READOUT','factors':[],'rejected':rejected}
    if not capture:
        return result
    return {'result':result,'N':N,'a':a,'t':t,'k':k,
            'modular_powers':powers,'gcd_calls':gcds,
            'lazy_tables':factory.export_certificate(),
            'source':source_binding(),
            'postprocess_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'native_kernel_calls_delta':len(CALLS)-start,
            'native_core_calls':CALLS[start:],
            'whole_domain_enumerated':False,
            'policy':'frozen CF candidate order/cap, returning-exponent and gcd rules unchanged',
            'scope':'modular-power and gcd execution use typed lazy arithmetic; no minimum-order claim'}


def lazy_classical_postprocess(N, a, t, k):
    return _run(N, a, t, k, False)


def lazy_classical_postprocess_trace(N, a, t, k):
    return _run(N, a, t, k, True)
