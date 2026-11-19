"""Exact terminal-law adapter for the frozen T,F,E Euler B01 controller."""
from __future__ import annotations

from collections import Counter, deque
from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha1, sha256
from importlib import util
from itertools import product
from pathlib import Path
import sys
from typing import NamedTuple

import numpy as np


B01_SHA256 = "868595349d4ed76eee8c8cd7376afa43e20e409d99e4c7c648b70fd966884621"
ALPHABET = "TFE"
SIZES = (3,2,8,4,2,3,3)
World = tuple[int,int,int,int,int,int,int]
Positive = int | Fraction


class Registers(NamedTuple):
    source: int
    reference: int
    receiver: int


class Phase(NamedTuple):
    one: Fraction
    omega: Fraction


def _labels(values, sizes):
    if len(values)!=len(sizes) or any(type(v) is not int or not 0<=v<m
                                     for v,m in zip(values,sizes)):
        raise ValueError("coordinates must be integer labels in the specified carrier")


def record(labels: Registers) -> Registers:
    _labels(labels,(3,3,3))
    j,a,r=labels
    return Registers(j,a,(r+j-a)%3)


def inverse_record(labels: Registers) -> Registers:
    _labels(labels,(3,3,3))
    j,a,r=labels
    return Registers(j,a,(r-j+a)%3)


def _positive(weight):
    if isinstance(weight,bool) or not isinstance(weight,(int,Fraction)):
        raise TypeError("use exact integer or Fraction masses")
    if weight<=0:
        raise ValueError("each listed branch needs positive mass")
    return Fraction(weight)


def calibration_correlation(preparation: Iterable[tuple[Registers, Positive]]) -> Phase:
    """Return C_RA before writing, equivalently C_RS after writing, in Q[omega]."""
    bins=[Fraction(0) for _ in range(3)]
    for labels,weight in preparation:
        _labels(labels,(3,3,3))
        bins[(labels.receiver-labels.reference)%3]+=_positive(weight)
    if sum(bins)!=1:
        raise ValueError("preparation must have total mass one")
    return Phase(bins[0]-bins[2],bins[1]-bins[2])


def _load(repo, b01_path):
    if b01_path is None:
        b01_path=Path(__file__).resolve().parent.parent/"hundredninth"/"feedback_check.py"
    path=Path(b01_path)
    if sha256(path.read_bytes()).hexdigest()!=B01_SHA256:
        raise ValueError("B01 adapter hash mismatch")
    spec=util.spec_from_file_location("euler_c04_pinned_b01",path)
    source=util.module_from_spec(spec)
    spec.loader.exec_module(source)
    repo=Path(repo).resolve()
    for name,wanted in source.PINS.items():
        data=(repo/name).read_bytes()
        digest=sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        if digest!=wanted:
            raise ValueError(f"frozen public source mismatch: {name}")
    sys.path.insert(0,str(repo/"src"))
    try:
        from enterprise_math import brc_weighted
    finally:
        sys.path.pop(0)
    if Path(brc_weighted.__file__).resolve()!=(repo/"src/enterprise_math/brc_weighted.py"):
        raise ValueError("conflicting enterprise_math import; use the pinned checkout")
    return source,brc_weighted


def _exact_certificate(labels, ops):
    n=len(labels)
    queue=deque((np.array([int(i==key) for i in labels],dtype=np.int64),"",key)
                for key in range(9))
    basis={}; rows=[]; words=[]; sizes=Counter()
    prime=101
    while queue:
        raw,word,key=queue.popleft()
        row=raw.copy()
        for i in sorted(basis):
            if row[i]:
                row=(row-row[i]*basis[i])%prime
        piv=np.flatnonzero(row)
        if not len(piv):
            continue
        i=int(piv[0])
        basis[i]=row*pow(int(row[i]),-1,prime)%prime
        rows.append(raw)
        words.append((word,divmod(key,3)))
        sizes[len(word)]+=1
        for letter,perm in ops.items():
            queue.append((raw[perm],letter+word,key))
    pivots=tuple(sorted(basis))
    free=tuple(sorted(set(range(n))-basis.keys()))
    # Free-coordinate identity gives an integral certificate of independence.
    null=np.eye(n,dtype=np.int64)[list(free)]
    for i in reversed(pivots):
        null[:,i]=-(null@basis[i])%prime
    null=(null+50)%prime-50
    actual=np.stack(rows)
    if len(pivots)!=409 or np.any(actual@null.T):
        raise ArithmeticError("rank or lifted kernel does not match B01")
    if any(np.any(actual[:,perm]@null.T) for perm in ops.values()):
        raise ArithmeticError("integer row space is not closed under a generator")
    return pivots,free,null,tuple(words),tuple(sizes[i] for i in range(max(sizes)+1))


@dataclass(frozen=True)
class TerminalLaw:
    model: B01Observer
    coordinates: tuple[Fraction,...]

    def read(self, word: str) -> tuple[Fraction,...]:
        """Nine exact terminal bin masses in row-major order (j, r-j)."""
        if not isinstance(word,str) or any(a not in ALPHABET for a in word):
            raise ValueError("only complete T,F,E commands form an admissible word")
        labels=self.model.labels
        for a in reversed(word):
            labels=labels[self.model.ops[a]]
        bins=[Fraction(0) for _ in range(9)]
        for i,mass in zip(self.model.pivots,self.coordinates,strict=True):
            bins[int(labels[i])]+=mass
        return tuple(bins)


class B01Observer:
    """Build once and reuse the fixed B01 representation and integer certificate."""
    def __init__(self, repo: Path, b01_path: Path|None=None):
        self.source,self.brc=_load(repo,b01_path)
        states=product(*(range(m) for m in SIZES))
        traces={}
        table={}
        representatives=[]
        ids={}
        for z in states:
            x=z[:5]
            if x not in traces:
                traces[x]=self.source.passive(x)
            key=(traces[x],z[-1],z[-2])
            if key not in ids:
                ids[key]=len(ids)
                representatives.append(z)
            table[z]=ids[key]
        self.table=table
        self.reps=tuple(representatives)
        self.ops={a:np.array([table[self.source.fused(z,a)] for z in self.reps],dtype=np.int64)
                  for a in ALPHABET}
        self.labels=np.array([3*j+d for j,d in map(self.source.read,self.reps)],dtype=np.int64)
        for z,i in table.items():
            for a in ALPHABET:
                if table[self.source.fused(z,a)]!=self.ops[a][i]:
                    raise ArithmeticError("transition did not descend to class")
        self.pivots,self.free,self.kernel,self.words,self.increments=_exact_certificate(
            self.labels,self.ops)
        self._signed_updates=[[(int(i),int(row[i])) for i in np.flatnonzero(row)]
                              for row in self.kernel]
        for ar in (self.labels,self.kernel,*self.ops.values()):
            ar.flags.writeable=False

    def future_observer(self, preparation: Iterable[tuple[World,Positive]]) -> TerminalLaw:
        """Encode a normalized positive joint preparation for single endpoint queries."""
        masses=[self.brc.CWM_ZERO for _ in self.reps]
        for z,weight in preparation:
            _labels(z,SIZES)
            k=self.table[tuple(z)]
            masses[k]=self.brc.cwm_recoalesce(masses[k],self.brc.cwm_edge(_positive(weight)))
        if sum(x.total for x in masses)!=1:
            raise ValueError("preparation must have total mass one")
        raw=[x.total for x in masses]
        for i,updates in zip(self.free,self._signed_updates,strict=True):
            weight=masses[i].total
            if weight:
                for j,sign in updates:
                    raw[j]-=sign*weight
        return TerminalLaw(self,tuple(raw[i] for i in self.pivots))
