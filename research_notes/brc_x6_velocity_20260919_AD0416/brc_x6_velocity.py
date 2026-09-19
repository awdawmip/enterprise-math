"""Exact heartbeat/cadence transport. Research specialization, not a physical law.

A local step in a coarse chart is costed in fine native steps; the clock is not
an extra spatial axis. No occupancy, state-dependent interaction, beam, or
semantic-memory claim is made. Existing X6/BRC modules remain the source core.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd, lcm, isqrt
from pathlib import Path
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
CANDIDATES = (HERE.parent/'verify_heartbeat.py',
              HERE.parent/'brc_x6_heartbeat_20260919_AD0416'/'verify_heartbeat.py')
SOURCE = next((p for p in CANDIDATES if p.is_file()), None)
if SOURCE is None:
    raise ImportError('The pinned original verify_heartbeat.py is required')
spec = importlib.util.spec_from_file_location('x6_heartbeat_source', SOURCE)
hb = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = hb
spec.loader.exec_module(hb)
bt, pq = hb.bt, hb.pq
D, PERIOD, ZERO = 6, 12, (0,)*6
E1 = (1,0,0,0,0,0)


def natural(v, name):
    if type(v) is not int or v < 0:
        raise ValueError(name+' must be a nonnegative integer')
    return v


def add(x, y):
    return tuple(a+b for a,b in zip(hb.point(x),hb.point(y)))


def mul(n, x):
    if type(n) is not int:
        raise TypeError('integer multiplier required')
    return tuple(n*a for a in hb.point(x))


def height(phase):
    phase = natural(phase,'phase') % PERIOD
    return min(phase, PERIOD-phase)


def step_vector(phase, b=2, reverse=True):
    """After exact analysis to depth j, move +/-e1 and synthesize unchanged digits."""
    phase = natural(phase,'phase') % PERIOD
    hb.radix(b)
    g = E1
    for _ in range(height(phase)):
        g = hb.expand(g,b)
    return mul(-1 if reverse and phase >= 6 else 1, g)


def lifted_step(x, phase, moves, b=2, reverse=True):
    natural(moves,'moves')
    q, digits = hb.analyze(hb.point(x), height(phase), b)
    sign = -1 if reverse and phase % PERIOD >= 6 else 1
    q = add(q,mul(sign*moves,E1))
    return hb.synthesize(q,digits,b)


@dataclass(frozen=True)
class Cadence:
    """p/q chart-local steps per tick; rho is a clock carry, not a spatial residue."""
    p: int
    q: int
    rho: int = 0

    def __post_init__(self):
        natural(self.p,'p')
        if type(self.q) is not int or self.q < 1 or gcd(self.p,self.q)!=1:
            raise ValueError('reduced p/q with q>=1 required')
        if type(self.rho) is not int or not 0 <= self.rho < self.q:
            raise ValueError('clock carry outside [0,q)')

    def at(self,t):
        natural(t,'t')
        return ((t+1)*self.p+self.rho)//self.q-(t*self.p+self.rho)//self.q

    def tick(self,rho):
        if type(rho) is not int or not 0 <= rho < self.q:
            raise ValueError('invalid clock carry')
        moves,new_rho = divmod(rho+self.p,self.q)
        return moves,new_rho


def signature(cadence, b=2):
    L = lcm(PERIOD,cadence.q)
    phase_counts = tuple(sum(cadence.at(t) for t in range(j,L,PERIOD))
                         for j in range(PERIOD))
    vectors = tuple(step_vector(j,b) for j in range(PERIOD))
    delta = tuple(sum(n*g[i] for n,g in zip(phase_counts,vectors)) for i in range(D))
    return {'ticks':L,'delta':delta,'chart_steps':sum(phase_counts),
            'fine_step_cost':sum(n*sum(map(abs,g)) for n,g in zip(phase_counts,vectors)),
            'phase_counts':phase_counts,'phase_class_count':gcd(PERIOD,cadence.q)}


def walk(cadence,ticks,b=2,start=ZERO,modulus=None):
    natural(ticks,'ticks')
    if modulus is not None and (type(modulus) is not int or modulus<1):
        raise ValueError('positive integer modulus required')
    x=hb.point(start); positions=[]
    for t in range(ticks):
        positions.append(x)
        x=add(x,mul(cadence.at(t),step_vector(t,b)))
        if modulus is not None: x=tuple(a%modulus for a in x)
    return positions,x


def augmented_torus_period(cadence,modulus,b=2):
    if type(modulus) is not int or modulus<1:
        raise ValueError('positive modulus required')
    sig=signature(cadence,b)
    return sig['ticks']*modulus//gcd(modulus,*sig['delta'])


def irrational_moves(t):
    """Slope sqrt(2)-1, phase zero: exact integers, no floating approximation."""
    natural(t,'t')
    return isqrt(2*(t+1)**2)-isqrt(2*t*t)-1


def bernoulli_moments(cycles,probability=F(1,2),b=2):
    """Independent move/stay branches, NOT deterministic rational cadence."""
    natural(cycles,'cycles')
    if not isinstance(probability,F) or not 0 < probability < 1:
        raise ValueError('strictly intermediate exact Fraction probability required')
    state=bt.MomentState.from_point(ZERO)
    packets=[]
    for j in range(PERIOD):
        packets.append(bt.EffectHistogram.from_terms(D,[
            (1-probability,bt.Affine.identity(D),1),
            (probability,bt.Affine(bt.eye(D),step_vector(j,b)),1)]))
    for _ in range(cycles):
        for packet in packets: state=state.then(packet)
    return state,tuple(packets)


def outward_block(x,steps,b=2):
    """Different model: actual repeated A_b transport, not closed breathing."""
    if len(steps)!=D: raise ValueError('six step vectors required')
    y=hb.point(x)
    for u in steps: y=add(hb.expand(y,b),hb.point(u))
    return y


def additive_residue_period(velocity,modulus):
    """Period of x -> x+v modulo a declared precision modulus."""
    if type(modulus) is not int or modulus<1:
        raise ValueError('positive modulus required')
    return modulus//gcd(modulus,*hb.point(velocity))
