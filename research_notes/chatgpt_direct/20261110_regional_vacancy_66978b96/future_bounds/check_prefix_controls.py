"""Exact control comparisons for a single empty-prefix certificate.

Imports the inherited maintained tree through check_future_controls.  All exact
request table access remains in the feedback oracle and assertions.  No physical
BRC command count is inferred from these finite control experiments.
"""
from __future__ import annotations

from itertools import combinations_with_replacement, product
from math import gcd
from pathlib import Path
import argparse
import json

from check_future_controls import Search, target

ROOT = Path(__file__).resolve().parent


class PrefixControl:
    def __init__(self, residues, strategy):
        self.residues = list(residues)
        self.r = len(residues)
        self.width = self.r.bit_length()
        self.B = 1 << self.width
        self.strategy = strategy
        self.reads = []
        self.search = Search(self.r, self.width, self.read)
        self.cert = None
        self.selected = None
        self.trace = []
        self.hits = self.misses = self.refinements = self.discards = 0

    def read(self, slot, level):
        value = (self.residues[slot] >> level) & 1
        self.reads.append((slot, level, value))
        return value

    def reserve(self, phase):
        legal = target(self.r, phase)
        chosen = None
        if self.cert is not None:
            level, prefix = self.cert
            chosen = next((x for x in legal if x % (1 << level) == prefix), None)
        if chosen is None:
            self.misses += 1
            chosen = self.search.query(legal)
            last = self.search.query_trace[-1]['visits'][-1]
            level, prefix, _, labels = last
            assert labels == 0
            self.cert = ((self.width, chosen) if self.strategy == 'point'
                         else (level, prefix))
        else:
            self.hits += 1
        assert chosen not in self.residues and chosen in legal
        self.selected = chosen
        return chosen

    def bind(self, slot):
        assert self.selected is not None
        value = self.selected
        self.residues[slot] = value
        self.search.tree.known_write(slot, value)
        if self.cert is not None:
            level, prefix = self.cert
            if value % (1 << level) == prefix:
                if self.strategy == 'prefix' and level < self.width:
                    other = 1 - ((value >> level) & 1)
                    self.cert = level + 1, prefix | (other << level)
                    self.refinements += 1
                else:
                    self.cert = None
                    self.discards += 1

    def step(self, op):
        before = len(self.reads)
        if op[0] == 'reserve':
            result = self.reserve(op[1])
        elif op[0] == 'bind':
            self.bind(op[1]); result = None
        else:
            raise ValueError(op)
        if self.cert is not None:
            level, prefix = self.cert
            assert all(x % (1 << level) != prefix for x in self.residues)
        self.trace.append(dict(op=op, choice=result, cert=self.cert,
                               additional_reads=len(self.reads)-before))

    def result(self):
        return dict(strategy=self.strategy, reads=len(self.reads),
                    searches=self.misses, certificate_hits=self.hits,
                    nodes=self.search.node_visits, refinements=self.refinements,
                    discards=self.discards, trace=self.trace)


def compare(residues, operations):
    rows = []
    for strategy in ('point','prefix'):
        control = PrefixControl(residues, strategy)
        for op in operations:
            control.step(op)
        assert len(control.reads) <= len(residues) * len(residues).bit_length()
        rows.append(control.result())
    return dict(residues=residues, operations=operations, point=rows[0], prefix=rows[1])


def finite_mixed():
    examples = {}
    examined = 0
    # Two rounds already distinguish repeated probes from prefix refinement.
    for r in range(2, 7):
        B, M = 1 << r.bit_length(), r + 1
        L = B // gcd(B,M)
        for residues in combinations_with_replacement(range(B),r):
            for phases in product(range(L), repeat=3):
                operations = [('reserve',phases[0]),('bind',0),
                              ('reserve',phases[1]),('bind',1),
                              ('reserve',phases[2])]
                row = compare(residues, operations)
                examined += 1
                delta = row['prefix']['reads'] - row['point']['reads']
                key = 'prefix_reads_less' if delta < 0 else 'prefix_reads_more' if delta > 0 else None
                if key and key not in examples:
                    examples[key] = row
                if len(examples) == 2:
                    return dict(examined=examined, examples=examples)
    return dict(examined=examined, examples=examples)


def stable_family():
    rows = []
    for b in (3,5,7,9):
        r = (1 << b) - 2
        B = 1 << b
        # The only free residues, 0 and B/2, form one depth-(b-1) class.
        # Every target contains one of them.  Alternating omissions makes
        # a point cache miss each time, while the class cache always hits.
        phases = [0,B//2] * 16
        residues = tuple(x for x in range(B) if x not in (0,B//2))
        row = compare(residues, [('reserve',t) for t in phases])
        assert row['point']['reads'] == row['prefix']['reads'] == 2*B-2*b-2
        assert row['point']['nodes'] == b*len(phases)
        assert row['prefix']['nodes'] == b
        assert row['point']['searches'] == len(phases)
        assert row['prefix']['searches'] == 1
        rows.append(dict(b=b,r=r,targets=len(phases),phases=phases,
                         point={k:v for k,v in row['point'].items() if k!='trace'},
                         prefix={k:v for k,v in row['prefix'].items() if k!='trace'}))
    return rows


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--out',default=str(ROOT/'prefix_controls_replay.json'))
    p.add_argument('--exhaustive',action='store_true')
    a=p.parse_args()
    examples = {
        'strict_read_gain': compare((0,0), [('reserve',0),('bind',0),('reserve',3)]),
        'mixed_read_tradeoff': compare((7,7,0,0,5,0,1,0,1,2),
            [('reserve',9),('bind',8),('reserve',1),('bind',7),
             ('reserve',14),('bind',8),('reserve',13),('bind',1),
             ('reserve',0),('bind',9),('reserve',10)])}
    assert (examples['strict_read_gain']['point']['reads'],
            examples['strict_read_gain']['prefix']['reads']) == (3,2)
    assert (examples['mixed_read_tradeoff']['point']['reads'],
            examples['mixed_read_tradeoff']['prefix']['reads']) == (25,26)
    result=dict(status='PASS',scope='Exact integer controller callbacks; no BRC command claim',
                regressions=examples, stable_family=stable_family())
    if a.exhaustive:
        result['mixed'] = finite_mixed()
    Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__ == '__main__':main()
