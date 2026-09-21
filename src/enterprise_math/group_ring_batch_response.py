"""Candidate terminal-only batch extensions of the existing BRC moment matcher.

Same-base varying windows share accumulated hit count and exponent sum. Aligned
binary suffix cuts share one giant trajectory and split baby offsets by their
2-adic divisibility. No order/log is supplied: if a complete short orbit is
actually traversed during table construction, its witnessed period is reused.

This is classical BSGS/prefix-moment reuse, not faster generic order finding,
not arbitrary-future lumpability. Scan budgets count baby iterations and giant
lookups, NOT integer bit work, input validation, inversions, output or RAM.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterable
from types import MappingProxyType
from collections.abc import Mapping

from .group_ring_terminal_response import cyclic_terminal_value


def _nat(name: str, value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f'{name} must be an integer >= {minimum}')
    return value


def _inputs(n, b, max_baby_steps, max_scan_steps):
    _nat('n', n, 3); _nat('b', b, 1)
    _nat('max_baby_steps', max_baby_steps, 1)
    _nat('max_scan_steps', max_scan_steps)
    if b >= n or gcd(b, n) != 1:
        raise ValueError('base must be a canonical unit modulo n')


def _states(n, states):
    states = tuple(states)
    if any(type(u) is not int or not 0 <= u < n for u in states):
        raise ValueError('states must be canonical integer residues')
    return states


def _baby(n, b, width):
    """One first offset per residue ONLY until an actual full orbit closes."""
    table = {}; v = 1
    for j in range(width):
        table[v] = j
        v = v*b % n
        if v == 1:
            # Powers 0..j are distinct; first return witnesses exact order j+1.
            return table, j+1, v
    return table, None, v


@dataclass(frozen=True)
class BatchResponse:
    status: str
    values: tuple | None
    baby_width: int
    table_entries: int
    required_scans: int
    executed_scans: int
    giant_lookups: int
    learned_order: int | None


def window_responses(n: int, b: int, requests: Iterable[tuple[int, int]], *,
                     baby_width: int | None = None,
                     max_baby_steps: int = 100_000,
                     max_scan_steps: int = 1_000_000) -> BatchResponse:
    """Return h_L(u) for explicit (length,state) requests in their original order.

    Repeated requests are permitted. Each signed target scans giant blocks only
    up to its largest requested length. A no-hit proves zero only in that window.
    Required scans is a preflight upper bound; short complete orbits can use less.
    All-or-nothing preflight refusal returns values=None and executes no scans.
    """
    _inputs(n, b, max_baby_steps, max_scan_steps)
    req = tuple(tuple(x) for x in requests)
    for x in req:
        if len(x) != 2:
            raise ValueError('request must be (length,state)')
        _nat('length', x[0], 1)
    states = _states(n, (x[1] for x in req))
    if not req:
        return BatchResponse('COMPLETE', (), 0, 0, 0, 0, 0, None)
    largest = max(L for L, _ in req)
    if baby_width is not None:
        _nat('baby_width', baby_width, 1)
        if baby_width > largest:
            raise ValueError('baby_width exceeds every requested window')
    if b == 1 or largest == 1:
        return BatchResponse('COMPLETE', tuple(L*L*int(u == 1) for L, u in req),
                             0, 0, 0, 0, 0, 1 if b == 1 else None)
    inv = {u: pow(u, -1, n) for u in set(states) if gcd(u, n) == 1}
    tasks: dict[int, set[int]] = {}
    for L, u in req:
        if u in inv:
            tasks.setdefault(u, set()).add(L)
            tasks.setdefault(inv[u], set()).add(L)
    if not tasks:
        return BatchResponse('COMPLETE', (0,)*len(req), 0, 0, 0, 0, 0, None)
    span_sum = sum(max(lens) for lens in tasks.values())
    width = min(largest, isqrt(span_sum-1)+1, max_baby_steps)
    if baby_width is not None:
        width = baby_width
    required = width + sum((max(lens)-1)//width+1 for lens in tasks.values())
    if width > max_baby_steps or required > max_scan_steps:
        return BatchResponse('BUDGET_EXHAUSTED', None, width, 0, required, 0, 0, None)
    table, order, power = _baby(n, b, width)
    if order is not None:
        vals = tuple(cyclic_terminal_value(order, L, table[u]) if u in table else 0
                     for L, u in req)
        return BatchResponse('COMPLETE', vals, width, len(table), required, order, 0, order)
    step = pow(power, -1, n)
    sums = {}; lookups = 0
    for target, lengths in tasks.items():
        maximum = max(lengths)
        block = 0; v = target; count = 0; exponent_sum = 0
        offset = table.get(v); lookups += 1
        for L in sorted(lengths):
            full, tail = divmod(L, width)
            # C,D contain all hits strictly before this query's partial block.
            while block < full:
                if offset is not None:
                    count += 1; exponent_sum += block*width+offset
                block += 1
                if block*width < maximum:
                    v = v*step % n; offset = table.get(v); lookups += 1
                else:
                    offset = None
            val = L*count-exponent_sum
            if tail and offset is not None and offset < tail:
                val += tail-offset
            sums[(target, L)] = val
    values = tuple(sums[(u, L)]+sums[(inv[u], L)]-L*int(u == 1)
                   if u in inv else 0 for L, u in req)
    return BatchResponse('COMPLETE', values, width, len(table), required,
                         width+lookups, lookups, None)


def dyadic_cut_responses(n: int, a: int, total_bits: int, cuts: Iterable[int],
                         states: Iterable[int] = (1,), *,
                         width_bits: int | None = None,
                         max_baby_steps: int = 100_000,
                         max_scan_steps: int = 1_000_000) -> BatchResponse:
    """Return a matrix (cuts x states) for ALIGNED fixed dyadic suffixes.

    Master exponent window N=2**total_bits, B=2**width_bits. Every selected cut
    must be <=width_bits<=total_bits. This explicit alignment is essential:
    a^(2^cut) raised to B/2^cut is the SAME a^B at all selected cuts. Very deep
    cuts that require an over-budget master table are refused, not silently
    approximated. Call the inherited suffix_responses separately for those cuts.

    Table construction learns an order only on an actual first return to 1.
    No arbitrary caller-supplied order or exponent is trusted by this API.
    """
    _inputs(n, a, max_baby_steps, max_scan_steps)
    _nat('total_bits', total_bits)
    if total_bits > 1_000_000:
        raise ValueError('bit allocation cap exceeded')
    cuts = tuple(cuts); states = _states(n, states)
    for cut in cuts:
        _nat('cut', cut)
        if cut > total_bits:
            raise ValueError('cut exceeds total_bits')
    if width_bits is not None:
        _nat('width_bits', width_bits)
        if width_bits > total_bits or (cuts and width_bits < max(cuts)):
            raise ValueError('alignment requires max(cuts)<=width_bits<=total_bits')
    if not cuts or not states:
        return BatchResponse('COMPLETE', tuple(() for _ in cuts), 0, 0, 0, 0, 0, None)
    if a == 1 or total_bits == 0:
        vals = tuple(tuple((1 << (2*(total_bits-j)))*int(u == 1) for u in states)
                     for j in cuts)
        return BatchResponse('COMPLETE', vals, 0, 0, 0, 0, 0, 1 if a == 1 else None)
    inv = {u: pow(u, -1, n) for u in set(states) if gcd(u, n) == 1}
    targets = tuple(sorted(set(inv) | set(inv.values())))
    if not targets:
        return BatchResponse('COMPLETE', tuple((0,)*len(states) for _ in cuts),
                             0, 0, 0, 0, 0, None)
    N = 1 << total_bits; J = max(cuts)
    optimal = min(N, isqrt(len(targets)*N-1)+1, max_baby_steps)
    k = max(J, optimal.bit_length()-1) if width_bits is None else width_bits
    width = 1 << k; blocks = N//width
    required = width+len(targets)*blocks
    if width > max_baby_steps or required > max_scan_steps:
        return BatchResponse('BUDGET_EXHAUSTED', None, width, 0, required, 0, 0, None)
    table, order, power = _baby(n, a, width)
    if order is not None:
        vals = []
        for cut in cuts:
            step = 1 << cut; g = gcd(order, step); s = order//g
            inverse = pow(step//g, -1, s) if s > 1 else 0
            row = []
            for u in states:
                e = table.get(u)
                if e is None or e % g:
                    row.append(0)
                else:
                    log = (e//g*inverse) % s
                    row.append(cyclic_terminal_value(s, 1 << (total_bits-cut), log))
            vals.append(tuple(row))
        return BatchResponse('COMPLETE', tuple(vals), width, len(table), required,
                             order, 0, order)
    # Table is injective: otherwise the orbit would have closed during _baby.
    # A hit d=i*B+j affects exactly cuts <=v2(j), since every cut <=k.
    decorated = {v: (j, J if j == 0 else min(J, (j & -j).bit_length()-1))
                 for v, j in table.items()}
    # Release duplicate map; peak allocations still include this temporary copy.
    del table
    giant_inverse = pow(power, -1, n)
    positive = {}
    for target in targets:
        bins = [0]*(J+1); v = target
        for i in range(blocks):
            item = decorated.get(v)
            if item is not None:
                offset, depth = item
                bins[depth] += N-i*width-offset
            v = v*giant_inverse % n
        running = 0; row = [0]*(J+1)
        for j in range(J, -1, -1):
            running += bins[j]
            if running % (1 << j):
                raise ArithmeticError('aligned mass must divide exactly')
            row[j] = running >> j
        positive[target] = row
    vals = tuple(tuple(positive[u][j]+positive[inv[u]][j]
                       -(1 << (total_bits-j))*int(u == 1) if u in inv else 0
                       for u in states) for j in cuts)
    return BatchResponse('COMPLETE', vals, width, len(decorated), required,
                         required, blocks*len(targets), None)


@dataclass(frozen=True)
class BoundedTerminalIndex:
    """Locally compiled finite-query index, NOT authenticated external evidence.

    When at least one unit state is registered and span>1, order=None means
    compilation proved order>span. Empty/nonunit-only domains do not test order.
    Missing logs prove no match inside [0,span), not arbitrary subgroup absence.
    Querying an unregistered state or larger master span raises, never yields 0.
    """
    n: int
    base: int
    span: int
    order: int | None
    _logs: Mapping[int, int]
    _inverses: Mapping[int, int]
    _domain: frozenset[int]

    def windows(self, requests: Iterable[tuple[int, int]]) -> tuple[int, ...]:
        req = tuple(tuple(x) for x in requests)
        for x in req:
            if len(x) != 2:
                raise ValueError('request must be (length,state)')
            L, u = x; _nat('length', L, 1)
            if L > self.span or type(u) is not int or u not in self._domain:
                raise ValueError('query outside compiled horizon/state domain')
        def positive(L, u):
            e = self._logs.get(u)
            if e is None or e >= L:
                return 0
            count = 1 if self.order is None else (L-1-e)//self.order+1
            correction = 0 if self.order is None else self.order*count*(count-1)//2
            return count*(L-e)-correction
        return tuple(positive(L,u)+positive(L,self._inverses[u])-L*int(u == 1)
                     if u in self._inverses else 0 for L,u in req)

    def cuts(self, total_bits: int, cuts: Iterable[int], states: Iterable[int]) -> tuple:
        _nat('total_bits', total_bits)
        if total_bits >= self.span.bit_length():
            raise ValueError('master span exceeds compiled horizon')
        cuts = tuple(cuts); states = _states(self.n, states)
        for j in cuts:
            _nat('cut', j)
            if j > total_bits:
                raise ValueError('cut exceeds total_bits')
        if any(u not in self._domain for u in states):
            raise ValueError('state not registered in this index')
        result = []
        for j in cuts:
            step = 1 << j; L = 1 << (total_bits-j)
            if self.order is None:
                def positive(u):
                    e = self._logs.get(u)
                    return max(0,L-e//step) if e is not None and e % step == 0 else 0
                row = tuple(positive(u)+positive(self._inverses[u])-L*int(u == 1)
                            if u in self._inverses else 0 for u in states)
            else:
                g = gcd(self.order,step); s = self.order//g
                reciprocal = pow(step//g,-1,s) if s > 1 else 0
                row = tuple(cyclic_terminal_value(s,L,self._logs[u]//g*reciprocal)
                            if u in self._logs and self._logs[u] % g == 0 else 0 for u in states)
            result.append(row)
        return tuple(result)


@dataclass(frozen=True)
class TerminalIndexCompilation:
    status: str
    index: BoundedTerminalIndex | None
    baby_width: int
    table_entries: int
    required_scans: int
    executed_scans: int


def compile_terminal_index(n: int, a: int, span: int, states: Iterable[int], *,
                           baby_width: int | None = None,
                           max_baby_steps: int = 100_000,
                           max_scan_steps: int = 1_000_000) -> TerminalIndexCompilation:
    """Classical shared bounded BSGS with finite-period/first-hit compilation.

    No period or log is an input. Cost includes looking for the smallest
    positive identity exponent <=span, then the smallest exponent in [0,span)
    for each signed target. The baby table is discarded after compiling logs.
    Downstream arbitrary windows and dyadic cuts are exact ONLY in this domain.
    Preflight is conservative and includes unsuccessful whole-interval scans.
    """
    _inputs(n,a,max_baby_steps,max_scan_steps); _nat('span',span,1)
    states = _states(n,states)
    if baby_width is not None:
        _nat('baby_width',baby_width,1)
        if baby_width > span:
            raise ValueError('baby_width exceeds span')
    domain = frozenset(states)
    inverses = {u:pow(u,-1,n) for u in domain if gcd(u,n) == 1}
    targets = tuple(sorted(set(inverses) | set(inverses.values())))
    def finish(logs,order,width,entries,required,scans):
        idx = BoundedTerminalIndex(n,a,span,order,MappingProxyType(logs),
                                   MappingProxyType(inverses),domain)
        return TerminalIndexCompilation('COMPLETE',idx,width,entries,required,scans)
    if not states or not targets or a == 1 or span == 1:
        return finish({1:0} if 1 in targets else {},1 if a == 1 else None,0,0,0,0)
    width = min(span,isqrt((len(targets)+1)*span)+1,max_baby_steps)
    if baby_width is not None:
        width = baby_width
    order_blocks = span//width+1
    log_blocks = (span-1)//width+1
    required = width+order_blocks+len(targets)*log_blocks
    if width > max_baby_steps or required > max_scan_steps:
        return TerminalIndexCompilation('BUDGET_EXHAUSTED',None,width,0,required,0)
    baby,order,z = _baby(n,a,width)
    if order is not None:
        return finish({u:baby[u] for u in targets if u in baby},order,width,len(baby),required,order)
    giant_inverse = pow(z,-1,n); scans = width; v = 1
    for i in range(order_blocks):
        j = baby.get(v); scans += 1
        if j is not None and 0 < i*width+j <= span:
            order = i*width+j; break
        v = v*giant_inverse % n
    logs = {}
    for target in targets:
        v = target
        for i in range(log_blocks):
            j = baby.get(v); scans += 1
            if j is not None and i*width+j < span:
                logs[target] = i*width+j; break
            v = v*giant_inverse % n
    return finish(logs,order,width,len(baby),required,scans)
