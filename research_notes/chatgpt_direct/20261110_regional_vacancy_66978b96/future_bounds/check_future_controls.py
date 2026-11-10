"""Exact finite control experiment: a future intersection probe with cached prefixes.

The request table is held by the Oracle only.  Search consumes one next-bit
feedback at a time through the inherited production PrefixTree.  This module
counts Boolean observations and explicit controller events, not BRC commands.
"""
from __future__ import annotations

from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
from math import gcd
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'directed'))
from check_directed_vacancy import PrefixTree


class Oracle:
    def __init__(self, residues):
        self.residues = residues
        self.reads = []

    def read(self, slot, level):
        assert (slot, level) not in {(s, d) for s, d, _ in self.reads}
        value = (self.residues[slot] >> level) & 1
        self.reads.append((slot, level, value))
        return value


class CandidateTrie:
    """An explicit static candidate set, preprocessed with counted work."""
    def __init__(self, candidates, width):
        self.candidates = tuple(candidates)
        self.size = 2 * (1 << width) - 1
        self.count = [0] * self.size
        self.first = [None] * self.size
        self.writes = 0
        for value in candidates:
            for level in range(width + 1):
                index = (1 << level) - 1 + (value % (1 << level))
                self.count[index] += 1
                if self.first[index] is None:
                    self.first[index] = value
                self.writes += 1


class Search:
    def __init__(self, slots, width, read):
        self.tree = PrefixTree(slots, width)
        self.read = read
        self.width = width
        self.node_visits = self.candidate_build_writes = 0
        self.query_trace = []

    def query(self, candidates):
        """Return one proved absent candidate or None after complete exclusion.

        Strict ancestor buckets are drained before entering each node.  A node
        with more candidates than labels is guaranteed to contain a vacancy;
        otherwise both children may need examination.  This is the only change
        from the inherited one-deficit-branch controller.
        """
        candidate = CandidateTrie(candidates, self.width)
        self.candidate_build_writes += candidate.writes
        visits, reads = [], []

        def visit(level, prefix):
            index = self.tree.index(level, prefix)
            cap, labels = candidate.count[index], self.tree.count[index]
            if cap == 0:
                return None
            self.node_visits += 1
            visits.append((level, prefix, cap, labels))
            if labels == 0:
                return candidate.first[index]
            if level == self.width:
                return None
            while self.tree.head[index] is not None:
                label = self.tree.head[index]
                value = self.read(label.representative, level)
                reads.append((label.representative, level, value))
                self.tree.observe_next(label, value)
            children, deficient = [], []
            for bit in (0, 1):
                cp = prefix | (bit << level)
                ci = self.tree.index(level + 1, cp)
                nc, cc = self.tree.count[ci], candidate.count[ci]
                if cc:
                    children.append((nc, bit, cp))
                    if nc < cc:
                        deficient.append((nc, bit, cp))
            if deficient:
                _, _, cp = min(deficient)
                found = visit(level + 1, cp)
                assert found is not None
                return found
            for _, _, cp in sorted(children):
                found = visit(level + 1, cp)
                if found is not None:
                    return found
            return None

        found = visit(0, 0)
        self.query_trace.append(dict(candidates=list(candidates), result=found,
                                     observations=reads, visits=visits))
        return found


def target(r, phase):
    B = 1 << r.bit_length()
    start = (1 + phase * (r + 1)) % B
    return tuple((start + c) % B for c in range(r + 1))


def run(residues, phases, strategy):
    r = len(residues)
    oracle = Oracle(residues)
    search = Search(r, r.bit_length(), oracle.read)
    sets = [target(r, t) for t in phases]
    held, choices, probe = [], [], None
    if strategy == 'intersection':
        common = set.intersection(*(set(c) for c in sets))
        candidates = tuple(x for x in sets[0] if x in common)
        if candidates:
            probe = search.query(candidates)
            if probe is not None:
                held.append(probe)
    for legal in sets:
        hits = [x for x in held if x in legal]
        if hits:
            chosen = hits[0]
        else:
            chosen = search.query(legal)
            assert chosen is not None and chosen not in residues
            held = held + [chosen] if strategy == 'retained' else [chosen]
        assert chosen in legal
        choices.append(chosen)
    assert len(oracle.reads) <= r * r.bit_length()
    return dict(strategy=strategy, observations=len(oracle.reads),
                searches=len(search.query_trace), node_visits=search.node_visits,
                candidate_build_writes=search.candidate_build_writes,
                choices=choices, held=held, common_probe_result=probe,
                query_trace=search.query_trace)


def first_examples(max_r=6):
    found = {}
    examined = 0
    for r in range(2, max_r + 1):
        B, M = 1 << r.bit_length(), r + 1
        L = B // gcd(B, M)
        if L == 1:
            continue
        for residues in combinations_with_replacement(range(B), r):
            for phases in product(range(L), repeat=2):
                if phases[0] == phases[1]:
                    continue
                single = run(residues, phases, 'single')
                probe = run(residues, phases, 'intersection')
                examined += 1
                delta = probe['observations'] - single['observations']
                key = 'probe_reduces_reads' if delta < 0 else 'probe_increases_reads' if delta > 0 else None
                if key and key not in found:
                    found[key] = dict(r=r, residues=residues, phases=phases,
                                      target_residues=[target(r,t) for t in phases],
                                      single=single, intersection=probe)
                if len(found) == 2:
                    return dict(examined=examined, examples=found)
    return dict(examined=examined, examples=found)


def first_retention_example(max_r=6):
    examined = 0
    for r in range(2, max_r + 1):
        B, M = 1 << r.bit_length(), r + 1
        L = B // gcd(B, M)
        if L == 1:
            continue
        for residues in combinations_with_replacement(range(B), r):
            for a, b in product(range(L), repeat=2):
                if a == b:
                    continue
                phases = (a, b, a)
                single = run(residues, phases, 'single')
                retained = run(residues, phases, 'retained')
                examined += 1
                if retained['observations'] < single['observations']:
                    return dict(examined=examined, r=r, residues=residues,
                                phases=phases, single=single, retained=retained)
    return dict(examined=examined, example=None)


def prescribed_examples():
    return [dict(r=6, residues=tuple(range(1,7)), phases=phases,
                 rows=[run(tuple(range(1,7)), phases, s)
                       for s in ('single','retained','intersection')])
            for phases in ((0,2),(0,1,2,3,4,5,6,7),(0,1,0,1,0,1))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default=str(ROOT/'future_controls_checks.json'))
    args = parser.parse_args()
    result = dict(status='PASS', arithmetic='exact integers',
                  scope='Control callbacks on inherited production PrefixTree; no BRC command claim',
                  intersection_examples=first_examples(),
                  retention_example=first_retention_example(),
                  prescribed=prescribed_examples())
    Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('prescribed',)},ensure_ascii=False))


if __name__ == '__main__':
    main()
