#!/usr/bin/env python3
"""R284GC exact unbounded-parameter QF_LIA/QF_LRA residual cut checker.

The SMT-LIB formula is the negation of the proposed all-q two-heavy theorem.
All 255 graph vertex cuts are reduced to their exact minimal-size masks.
Uses libz3 via ctypes (Python standard library); no floating-point solver.

Usage:
  python3 R284GC_uniform_twoheavy_unsat_checker.py
  python3 R284GC_uniform_twoheavy_unsat_checker.py --emit DIR
The second command emits fully standalone SMT-LIB formulas.
"""
import argparse
import ctypes
import ctypes.util
from itertools import combinations
from pathlib import Path

PAIRS = tuple(combinations(range(4), 2))
ADJACENT = {(0, 1), (0, 3), (1, 2), (2, 3)}
HEAVY_TYPES = (3, 5, 6)
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
        for p in range(1, 8)}
LAST = {(p, i): next(edge for edge in ((i - 1 - t) % 4 for t in range(4))
                      if BITS[p][edge] != BITS[p][(edge + 1) % 4])
        for p in range(1, 8) for i in range(4)}


def cut_data(pair):
    """D_ij, and (pattern-mask, least vertex count) for every induced nonempty mask."""
    i, j = pair
    edges = [(p, LAST[p, i], 4 + LAST[p, j])
             for p in range(1, 8) if BITS[p][i] != BITS[p][j]]
    masks = {}
    for vertices in range(1, 1 << 8):
        mask = tuple(p for p, left, right in edges
                     if vertices & (1 << left) and vertices & (1 << right))
        if mask:
            masks[mask] = min(masks.get(mask, 9), vertices.bit_count())
    return tuple(p for p, _, _ in edges), tuple(masks.items())


PAIR_DATA = {pair: cut_data(pair) for pair in PAIRS}


def sum_vars(types):
    return '(+ ' + ' '.join(f'x{p}' for p in types) + ')'


def assertion(value):
    return f'(assert {value})'


def formula(k, sort='Real', reduced=False, nonheavy=True, fixed_q=None):
    """Exact SMT-LIB with 8 unbounded variables, never a finite q scan.

    reduced=True retains ONLY nominal 12,13,23 and flow cuts 01,02,03.
    Full mode uses all six nominal and all six stable residual-flow constraints.
    """
    assert k in (8, 9) and sort in ('Real', 'Int')
    lines = ['(set-logic QF_LRA)' if sort == 'Real' else '(set-logic QF_LIA)',
             f'(declare-const q {sort})']
    lines += [f'(declare-const x{p} {sort})' for p in range(1, 8)]
    lines += [assertion('(>= q 5)'),
              assertion(f'(= {sum_vars(range(1, 8))} (+ (* 4 q) {k}))')]
    lines += [assertion(f'(>= x{p} 0)') for p in range(1, 8)]
    if fixed_q is not None:
        lines += [assertion(f'(= q {fixed_q})')]
    for pair in PAIRS:
        distances, cuts = PAIR_DATA[pair]
        bound = 5 if pair in ADJACENT else 3
        if not reduced or pair in {(1, 2), (1, 3), (2, 3)}:
            lines.append(assertion(f'(>= {sum_vars(distances)} (+ (* 2 q) {bound}))'))
        if not reduced or pair in {(0, 1), (0, 2), (0, 3)}:
            alternatives = [f'(>= {sum_vars(mask)} (+ (* {size} q) 3))'
                            for mask, size in cuts]
            lines.append(assertion('(or ' + ' '.join(alternatives) + ')'))
    if nonheavy:
        light = {p: f'(<= x{p} (+ (* 2 q) 1))' for p in HEAVY_TYPES}
        lines.append(assertion('(or ' + ' '.join(
            '(and ' + light[a] + ' ' + light[b] + ')'
            for a, b in combinations(HEAVY_TYPES, 2)) + ')'))
    lines += ['(check-sat)']
    return '\n'.join(lines) + '\n'


class Z3:
    def __init__(self):
        library = ctypes.util.find_library('z3') or 'libz3.so.4'
        self.lib = ctypes.CDLL(library)
        self.lib.Z3_mk_config.restype = ctypes.c_void_p
        self.lib.Z3_del_config.argtypes = [ctypes.c_void_p]
        self.lib.Z3_mk_context.argtypes = [ctypes.c_void_p]
        self.lib.Z3_mk_context.restype = ctypes.c_void_p
        self.lib.Z3_del_context.argtypes = [ctypes.c_void_p]
        self.lib.Z3_eval_smtlib2_string.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lib.Z3_eval_smtlib2_string.restype = ctypes.c_char_p
        self.lib.Z3_get_version.argtypes = [ctypes.POINTER(ctypes.c_uint)] * 4

    def version(self):
        v = [ctypes.c_uint() for _ in range(4)]
        self.lib.Z3_get_version(*(ctypes.byref(x) for x in v))
        return '.'.join(str(x.value) for x in v)

    def check(self, text):
        config = self.lib.Z3_mk_config()
        ctx = self.lib.Z3_mk_context(config)
        self.lib.Z3_del_config(config)
        try:
            return self.lib.Z3_eval_smtlib2_string(ctx, text.encode('utf-8')).decode('utf-8').strip()
        finally:
            self.lib.Z3_del_context(ctx)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--emit', type=Path, default=None, help='emit standalone SMT-LIB2 files')
    args = ap.parse_args()
    if args.emit:
        args.emit.mkdir(parents=True, exist_ok=True)
    z3 = Z3()
    print('Z3 exact QF linear arithmetic version:', z3.version())
    for k in (8, 9):
        for mode, sort, reduced, nonheavy in (
            ('full-LIA', 'Int', False, True),
            ('full-LRA', 'Real', False, True),
            ('six-constraint-LIA', 'Int', True, True),
            ('six-constraint-LRA', 'Real', True, True),
            ('positive-control', 'Int', False, False),
        ):
            script = formula(k, sort, reduced, nonheavy)
            if args.emit:
                (args.emit / f'R284GC_k{k}_{mode}.smt2').write_text(script)
            actual = z3.check(script)
            expected = 'sat' if mode == 'positive-control' else 'unsat'
            print(f'k={k} {mode}: {actual} (expected {expected})')
            assert actual == expected, (k, mode, expected, actual)
    print('PASS: all q>=5, both k=8,9; strong real relaxation; positive controls SAT')


if __name__ == '__main__':
    main()
