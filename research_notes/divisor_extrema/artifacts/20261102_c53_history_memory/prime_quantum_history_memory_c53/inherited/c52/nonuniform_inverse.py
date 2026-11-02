"""C52: separate PL preparation and terminal residual selection on 1260.

Finite full-word probabilities; exact positive rational branch weights.
The same-score terminal quotient is used only after preparation is retained.
No claim of native physical dynamics or mathematical admission is made.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import math
import sys
from typing import Mapping, Sequence

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'inherited'))
import c51_inverse as previous

native = previous.native
words = previous.words
raw_scores = previous.raw_scores
COUNTS = (2, 2, 1, 1)
PRIMES = (2, 3, 5, 7)

def word(text: str) -> tuple[int, ...]:
    return tuple(PRIMES.index(int(p)) for p in text)

def text(w: Sequence[int]) -> str:
    return ''.join(str(PRIMES[i]) for i in w)

# Five paths all have D^2=gamma^2, regardless of gamma.
W0 = word('233257')
W7 = word('233275')
W2 = word('233572')
W30 = word('322357')
W3 = word('322573')
PREP_WORDS = (W0, W7, W2, W30, W3)
ALL_WORDS = tuple(words(COUNTS))
WP = word('232357')
WM = word('323257')
CALIBRATION_WORDS = PREP_WORDS + (WP, WM)


def pl_probability(w: Sequence[int], rates: Sequence[F]) -> F:
    """Successive weighted choice of remaining unlabelled occurrences."""
    if len(rates) != 4 or any(r <= 0 for r in rates):
        raise ValueError('Four positive preparation rates are required')
    left = [w.count(i) for i in range(4)]
    ans = F(1)
    for p in w:
        total = sum(rates[i]*left[i] for i in range(4))
        ans *= rates[p]*left[p]/total
        left[p] -= 1
    return ans


def pl_weighted_dp(counts: tuple[int, ...], rates: Sequence[F]) -> dict[tuple[int, int], F]:
    """Mass observer on (used counts, A increment, B increment).

    With fixed rates, future transitions depend only on counts; terminal
    selection depends only on the accumulated score pair. This proves the
    declared quotient sufficient for the fixed-target terminal observer.
    """
    delta = {(0,1): 1, (0,2): -1, (0,3): 1, (1,2): 1, (1,3): -1}
    states = {((0,0,0,0), 0, 0): F(1)}
    for _ in range(sum(counts)):
        out = defaultdict(F)
        for (used, a, b), mass in states.items():
            rem = [counts[i]-used[i] for i in range(4)]
            total = sum(rates[i]*rem[i] for i in range(4))
            for p in range(4):
                if rem[p] == 0:
                    continue
                nxt = list(used); nxt[p] += 1
                da = 2*sum(used[j]*delta.get((j,p), 0) for j in range(p))
                db = 2*used[2] if p == 3 else 0
                out[tuple(nxt), a+da, b+db] += mass*rates[p]*rem[p]/total
        states = dict(out)
    h0 = sum(counts[i]*counts[j]*d for (i,j),d in delta.items())
    cd = counts[2]*counts[3]
    return {(a-h0,b-cd): mass for (used,a,b),mass in states.items()}


def reference(rates: Sequence[F]) -> dict[tuple[int, ...], F]:
    out = {w: pl_probability(w, rates) for w in ALL_WORDS}
    assert sum(out.values()) == 1
    return out


def selected(base: Mapping[tuple[int,...],F], q: F, gamma: F,
             use_brc: bool = False) -> tuple[dict[tuple[int,...],F], int]:
    """Common q^(gamma^2) is cancelled, with an additional common shift.

    For the validation grid gamma is half-integral, so all remaining weights
    are rational. For other inputs the caller must use certified powers.
    """
    if not 0 < q < 1:
        raise ValueError('Require 0<q<1')
    exps = {w: F(A*A)+2*gamma*A*B for w in base for A,B in [raw_scores(w)]}
    if any(e.denominator != 1 for e in exps.values()):
        raise ValueError('This exact routine requires integral relative exponents')
    shift = min(exps.values())
    masses = {}; calls = 0
    total = native.weight_histogram([]) if use_brc else None
    for w, p in base.items():
        wt = q**int(exps[w]-shift)
        if use_brc:
            h = native.histogram_serial(native.weight_histogram([p]),
                                        native.weight_histogram([wt]))
            total = native.histogram_recoalesce(total, h)
            masses[w] = h.total_mass
            calls += 2
        else:
            masses[w] = p*wt
    z = total.total_mass if use_brc else sum(masses.values())
    return {w: p/z for w,p in masses.items()}, calls


def selected_general(base: Mapping[tuple[int,...],F], weight) -> dict[tuple[int,...],F]:
    masses = {w: p*weight(*raw_scores(w)) for w,p in base.items()}
    if any(p <= 0 for p in masses.values()):
        raise ValueError('Terminal masses must be strictly positive')
    z = sum(masses.values())
    return {w:p/z for w,p in masses.items()}


def rational_sqrt(x: F) -> F:
    """Exact root for validation data that lie on the declared model."""
    a,b = math.isqrt(x.numerator), math.isqrt(x.denominator)
    if a*a != x.numerator or b*b != x.denominator:
        raise ValueError('Non-rational root: use interval inversion')
    return F(a,b)


def infer_preparation(p: Mapping[tuple[int,...],F]) -> tuple[F,F,F,F]:
    z = p[W0]/p[W7]
    r2 = p[W0]/p[W2]
    r3 = p[W30]/p[W3]
    x = (rational_sqrt(1+4*(1+z)*r2)-1)/2
    y = (rational_sqrt(1+4*(1+z)*r3)-1)/2
    return x,y,z,F(1)


def residual_odds(p: Mapping[tuple[int,...],F], rates: Sequence[F]) -> tuple[F,F]:
    anchor = p[W0]/pl_probability(W0,rates)
    u = (p[WP]/pl_probability(WP,rates))/anchor
    v = (p[WM]/pl_probability(WM,rates))/anchor
    if u*v >= 1:
        raise ValueError('Residual odds violate 0<q<1')
    return u,v


def predict_all(rates: Sequence[F], u: F, v: F) -> dict[tuple[int,...],F]:
    masses = {}
    for w in ALL_WORDS:
        A,B = raw_scores(w); k=A//2
        e1=k*(k+B)//2; e2=k*(k-B)//2
        assert e1 >= 0 and e2 >= 0
        masses[w] = pl_probability(w,rates)*u**e1*v**e2
    total=sum(masses.values())
    return {w:p/total for w,p in masses.items()}


def score_mass(p: Mapping[tuple[int,...],F]) -> dict[tuple[int,int],F]:
    out=defaultdict(F)
    for w,x in p.items():
        out[raw_scores(w)] += x
    return dict(out)


def infer_from_fibers(pmass, reference_mass):
    u=(pmass[2,1]/reference_mass[2,1])/(pmass[0,1]/reference_mass[0,1])
    v=(pmass[-2,1]/reference_mass[-2,1])/(pmass[0,1]/reference_mass[0,1])
    return u,v


# Interval inversion also covers nearby off-model input frequencies.
I=tuple[F,F]

def point(x) -> I:
    return F(x),F(x)

def outward(a:I,bits:int=100)->I:
    den=1<<bits
    return F((a[0].numerator*den)//a[0].denominator,den),F(-((-a[1].numerator*den)//a[1].denominator),den)

def iadd(a:I,b:I)->I: return outward(previous.add(a,b))
def isub(a:I,b:I)->I: return outward(previous.sub(a,b))
def imul(a:I,b:I)->I: return outward(previous.mul(a,b))
def idiv(a:I,b:I)->I: return outward(previous.div(a,b))
def iscale(a:I,k)->I:return imul(a,point(k))
def sqrt_box(a:I)->I:
    return previous.root_interval(a[0],2,100)[0],previous.root_interval(a[1],2,100)[1]

def preparation_box(p: Mapping[tuple[int,...],I])->tuple[I,I,I,I]:
    z=idiv(p[W0],p[W7]);r2=idiv(p[W0],p[W2]);r3=idiv(p[W30],p[W3])
    def inverse(r):
        return iscale(isub(sqrt_box(iadd(point(1),iscale(imul(iadd(point(1),z),r),4))),point(1)),F(1,2))
    return inverse(r2),inverse(r3),z,point(1)

def pl_box(w: Sequence[int],ratebox: Sequence[I])->I:
    """Use monotonicity of each categorical probability for tight bounds."""
    rem=[w.count(i) for i in range(4)];ans=point(1)
    for p in w:
        lo=ratebox[p][0]*rem[p];hi=ratebox[p][1]*rem[p]
        otherhi=sum(ratebox[j][1]*rem[j] for j in range(4) if j!=p)
        otherlo=sum(ratebox[j][0]*rem[j] for j in range(4) if j!=p)
        factor=(lo/(lo+otherhi),hi/(hi+otherlo))
        ans=imul(ans,factor);rem[p]-=1
    return ans

def inverse_box(p:Mapping[tuple[int,...],I]):
    rates=preparation_box(p)
    # Adjacent swaps cancel five-step shared factors before interval propagation.
    import itertools
    vertices=list(itertools.product(*(b for b in rates[:3])))
    fu=[(y+z+1)/(x+z+1) for x,y,z in vertices]
    fv=[(2*x+y+z+1)/(x+2*y+z+1) for x,y,z in vertices]
    u=imul(idiv(p[WP],p[W0]),(min(fu),max(fu)))
    v=imul(idiv(p[WM],p[W0]),(min(fv),max(fv)))
    lu=outward(previous.log_box(u));lv=outward(previous.log_box(v))
    logs=iadd(lu,lv)
    if logs[1]>=0: raise ValueError('Input box does not ensure q<1')
    product=imul(u,v)
    qbox=previous.root_interval(product[0],8,100)[0],previous.root_interval(product[1],8,100)[1]
    gbox=idiv(isub(lu,lv),logs)
    return {'rates':rates,'q':qbox,'gamma':gbox,'u':u,'v':v}


def conditional_next(p: Mapping[tuple[int,...],F], prefix: tuple[int,...]) -> dict[int,F]:
    """Full-word conditional readout, retaining the ordered prefix."""
    mass=defaultdict(F)
    for w,prob in p.items():
        if w[:len(prefix)]==prefix and len(w)>len(prefix):
            mass[w[len(prefix)]] += prob
    z=sum(mass.values())
    if z==0: raise ValueError('Prefix has no next-step mass')
    return {a:x/z for a,x in mass.items()}


def tilted_transitions(rates: Sequence[F],q:F,gamma:F):
    """Exact h-transform; rates describe reference, not selected transitions."""
    delta = {(0,1): 1, (0,2): -1, (0,3): 1, (1,2): 1, (1,3): -1}
    # Relative exponents remove common gamma^2; B is +-1 at the terminal.
    @lru_cache(None)
    def h(used:tuple[int,...],araw:int,braw:int)->F:
        if used==COUNTS:
            A=araw-4;B=braw-1
            ex=F(A*A)+2*gamma*A*B
            if ex.denominator!=1:raise ValueError('Non-rational terminal routine')
            return q**int(ex)
        rem=[COUNTS[i]-used[i] for i in range(4)]
        z=sum(rem[i]*rates[i] for i in range(4));out=F()
        for p in range(4):
            if not rem[p]:continue
            nxt=list(used);nxt[p]+=1
            da=2*sum(used[j]*delta.get((j,p),0) for j in range(p))
            db=2*used[2] if p==3 else 0
            out+=rates[p]*rem[p]/z*h(tuple(nxt),araw+da,braw+db)
        return out
    def next_at(prefix:tuple[int,...]):
        used=[0]*4;a=b=0
        for p in prefix:
            a+=2*sum(used[j]*delta.get((j,p),0) for j in range(p))
            b+=2*used[2] if p==3 else 0
            used[p]+=1
        rem=[COUNTS[i]-used[i] for i in range(4)]
        z=sum(rem[i]*rates[i] for i in range(4))
        state=(tuple(used),a,b);H=h(*state);out={}
        for p in range(4):
            if not rem[p]:continue
            nxt=used.copy();nxt[p]+=1
            da=2*sum(used[j]*delta.get((j,p),0) for j in range(p))
            db=2*used[2] if p==3 else 0
            out[p]=(rates[p]*rem[p]/z)*h(tuple(nxt),a+da,b+db)/H
        return out
    return next_at,h
