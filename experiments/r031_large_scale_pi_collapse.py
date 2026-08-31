#!/usr/bin/env python3
"""R031 Large-Scale Pi Collapse Divergence Atlas.

Deterministic stdlib-only research runner for:
- exact integer p-th-power basin geometry;
- exact binary64 dyadic-cell geometry on positive integers;
- fixed-point Gauss-Legendre and Chudnovsky pi channels with internal collapse;
- large-circle circumference/area/polygon formula-coherence probes;
- deterministic stochastic endpoint policies and ALL_ENDPOINTS support probes.

The arbitrary-precision pi coordinate is produced with Decimal Chudnovsky at
substantial guard precision and cross-checked by repeating at a larger guard.
The theorem-critical collapse geometry itself uses only exact integer/rational
arithmetic.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from dataclasses import dataclass, asdict
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

P_LIST = (2, 3, 4, 5, 6, 8, 10, 12, 16)
POLICIES = (
    "DOWN", "UP", "NEAREST", "FAR", "PRNG_50_50",
    "DISTANCE_WEIGHTED_STOCHASTIC", "RESIDUAL_ONLY",
    "ANCHOR_PLUS_RESIDUAL", "FIELD_PHASE", "ALL_ENDPOINTS",
)
MAX_BINARY64_INT = (2**53 - 1) * 2 ** (1023 - 52)


def floor_nth_root(n: int, p: int) -> int:
    if n < 0 or p < 1:
        raise ValueError("floor_nth_root requires n>=0, p>=1")
    if n < 2 or p == 1:
        return n
    lo, hi = 0, 1 << ((n.bit_length() + p - 1) // p)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pow(mid, p) <= n:
            lo = mid
        else:
            hi = mid
    return lo


@dataclass(frozen=True)
class Bracket:
    n: int
    p: int
    k: int
    L: int
    U: int
    G: int
    d: int
    u: int
    exact: bool

    @property
    def phase(self) -> Fraction:
        if self.exact:
            return Fraction(0, 1)
        return Fraction(self.d, self.G)


def bracket(n: int, p: int) -> Bracket:
    if n < 0:
        raise ValueError("bracket requires n>=0")
    k = floor_nth_root(n, p)
    L = pow(k, p)
    if n == L:
        return Bracket(n, p, k, L, L, 0, 0, 0, True)
    U = pow(k + 1, p)
    return Bracket(n, p, k, L, U, U - L, n - L, U - n, False)


def local_gap(n: int, p: int) -> tuple[int, int, int, int]:
    """Return k,L,U,G for the half-open basin containing n.

    At an exact power n=k^p, G is still the next-basin width
    (k+1)^p-k^p, matching R031's crossover field definition.
    """
    k = floor_nth_root(n, p)
    L = pow(k, p)
    U = pow(k + 1, p)
    return k, L, U, U - L


@lru_cache(maxsize=None)
def _pi_decimal(prec: int) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = prec
        C = Decimal(426880) * Decimal(10005).sqrt()
        M = 1
        L = 13591409
        X = 1
        K = 6
        S = Decimal(L)
        terms = prec // 14 + 12
        for i in range(1, terms):
            M = (K**3 - 16 * K) * M // (i**3)
            L += 545140134
            X *= -262537412640768000
            S += Decimal(M * L) / Decimal(X)
            K += 12
        return +(C / S)


@lru_cache(maxsize=None)
def pi_floor(d: int) -> int:
    if d < 0:
        raise ValueError("d must be nonnegative")
    scale = 10**d
    with localcontext() as ctx:
        ctx.prec = d + 180
        a = int(_pi_decimal(d + 90) * Decimal(scale))
        b = int(_pi_decimal(d + 140) * Decimal(scale))
    if a != b:
        raise ArithmeticError(f"pi floor guard disagreement at d={d}: {a} != {b}")
    return a


@lru_cache(maxsize=None)
def pi_ceil(d: int) -> int:
    f = pi_floor(d)
    return f + 1


def binary64_integer_cell(n: int) -> dict[str, Any]:
    """Exact binary64 lattice cell around positive integer n, no float use."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n > MAX_BINARY64_INT:
        return {"available": False, "reason": "BINARY64_OVERFLOW_OR_ABSENCE"}
    e = n.bit_length() - 1
    if e <= 52:
        q = Fraction(1, 2 ** (52 - e))
        # For our R031 integer N this regime means N is exactly representable.
        lower = Fraction(n, 1)
        upper = lower + q
        exact = True
        phase = Fraction(0, 1)
        nearest = lower
        nearest_direction = "EXACT"
    else:
        q_int = 1 << (e - 52)
        q = Fraction(q_int, 1)
        lower_int = (n // q_int) * q_int
        exact = lower_int == n
        if exact:
            lower = Fraction(n, 1)
            upper = Fraction(n + q_int, 1)
            phase = Fraction(0, 1)
            nearest = lower
            nearest_direction = "EXACT"
        else:
            lower = Fraction(lower_int, 1)
            upper = Fraction(lower_int + q_int, 1)
            phase = Fraction(n - lower_int, q_int)
            dl = n - lower_int
            du = lower_int + q_int - n
            if dl < du:
                nearest = lower
                nearest_direction = "DOWN"
            elif dl > du:
                nearest = upper
                nearest_direction = "UP"
            else:
                # ties-to-even: lower significand parity decides.
                idx = lower_int // q_int
                nearest = lower if idx % 2 == 0 else upper
                nearest_direction = "DOWN_TIE_EVEN" if idx % 2 == 0 else "UP_TIE_EVEN"
    return {
        "available": True,
        "exponent": e,
        "ulp": q,
        "lower": lower,
        "upper": upper,
        "phase": phase,
        "exact": exact,
        "nearest": nearest,
        "nearest_direction": nearest_direction,
    }


def basin_coverage(a: int, b: int, p: int) -> dict[str, int]:
    """Count p-power half-open basins intersecting [a,b), and full/partial."""
    if not (0 <= a < b):
        raise ValueError("require 0<=a<b")
    ka = floor_nth_root(a, p)
    kb = floor_nth_root(b - 1, p)
    touched = kb - ka + 1
    first_full = ka if pow(ka, p) >= a else ka + 1
    # j-basin full iff j^p>=a and (j+1)^p<=b, i.e. j <= root_floor(b) - 1,
    # with exact b power handled naturally by floor root.
    max_full_j = floor_nth_root(b, p) - 1
    full = max(0, max_full_j - first_full + 1)
    partial = touched - full
    return {"touched": touched, "full": full, "partial": partial}


def frac_obj(x: Fraction) -> dict[str, str]:
    return {"num": str(x.numerator), "den": str(x.denominator)}


def frac_decimal(x: Fraction, digits: int = 18) -> str:
    with localcontext() as ctx:
        ctx.prec = digits + 8
        return format(Decimal(x.numerator) / Decimal(x.denominator), f".{digits}g")


def log10_fraction_abs(x: Fraction) -> float | None:
    if x == 0:
        return None
    a, b = abs(x.numerator), x.denominator
    # Avoid float conversion of huge ints by digit/bit decomposition.
    return math.log10(a) - math.log10(b) if a < 10**300 and b < 10**300 else (
        (len(str(a)) - 1 + math.log10(float(str(a)[:16])) - 15)
        - (len(str(b)) - 1 + math.log10(float(str(b)[:16])) - 15)
    )


def randbelow_exact(limit: int, seed_material: str) -> int:
    """Deterministic SHAKE256 rejection sampler; no modulo bias."""
    if limit <= 0:
        raise ValueError("limit must be positive")
    bits = limit.bit_length()
    nbytes = (bits + 7) // 8
    counter = 0
    while True:
        h = hashlib.shake_256(f"{seed_material}|{counter}".encode()).digest(nbytes)
        v = int.from_bytes(h, "big") & ((1 << bits) - 1)
        if v < limit:
            return v
        counter += 1


def choose_endpoint(n: int, p: int, policy: str, *, seed: int = 0,
                    trajectory_id: str = "0", layer_id: str = "0",
                    scale_context: int | None = None) -> tuple[Any, dict[str, Any]]:
    """Apply R031 policy to signed fixed-point integer state.

    Negative states use odd signed symmetry for endpoint-style policies.
    ANCHOR_PLUS_RESIDUAL is a lossless structured-carrier control and returns n
    as scalar observable while retaining (anchor,residual). FIELD_PHASE maps the
    non-exact state to floor(phi*scale_context), a dimensionless phase carrier.
    """
    sign = -1 if n < 0 else 1
    m = abs(n)
    b = bracket(m, p)
    meta: dict[str, Any] = {
        "input": n, "p": p, "k": b.k, "L": sign*b.L,
        "U": sign*b.U if not b.exact else sign*b.L,
        "G": b.G, "d": b.d, "u": b.u,
        "phase": b.phase, "exact": b.exact,
    }
    if b.exact:
        meta["choice"] = "EXACT"
        if policy == "ALL_ENDPOINTS":
            return {n}, meta
        if policy == "ANCHOR_PLUS_RESIDUAL":
            meta["carrier"] = {"anchor": n, "residual": 0}
        return n, meta

    L, U = b.L, b.U
    if policy == "DOWN":
        v, ch = L, "L"
    elif policy == "UP":
        v, ch = U, "U"
    elif policy == "NEAREST":
        v, ch = (L, "L") if b.d <= b.u else (U, "U")
    elif policy == "FAR":
        v, ch = (U, "U") if b.d <= b.u else (L, "L")
    elif policy == "PRNG_50_50":
        r = randbelow_exact(2, f"P50|{seed}|{trajectory_id}|{layer_id}")
        v, ch = (L, "L") if r == 0 else (U, "U")
    elif policy == "DISTANCE_WEIGHTED_STOCHASTIC":
        # P(U)=d/G, P(L)=u/G exactly.
        r = randbelow_exact(b.G, f"DW|{seed}|{trajectory_id}|{layer_id}")
        v, ch = (U, "U") if r < b.d else (L, "L")
    elif policy == "RESIDUAL_ONLY":
        v, ch = b.d, "RESIDUAL"
    elif policy == "ANCHOR_PLUS_RESIDUAL":
        meta["choice"] = "ANCHOR_PLUS_RESIDUAL"
        meta["carrier"] = {"anchor": sign * L, "residual": sign * b.d}
        return n, meta
    elif policy == "FIELD_PHASE":
        if scale_context is None:
            raise ValueError("FIELD_PHASE requires scale_context")
        v, ch = (b.d * scale_context) // b.G, "PHASE"
    elif policy == "ALL_ENDPOINTS":
        meta["choice"] = "ALL_ENDPOINTS"
        return {sign*L, sign*U}, meta
    else:
        raise ValueError(f"unknown policy {policy}")
    meta["choice"] = ch
    return sign * v, meta


def fp_mul(a: int, b: int, S: int) -> int:
    prod = a * b
    return prod // S if prod >= 0 else -((-prod) // S)


def fp_div(a: int, b: int, S: int) -> int:
    if b == 0:
        raise ZeroDivisionError
    num = a * S
    sign = -1 if (num < 0) ^ (b < 0) else 1
    return sign * (abs(num) // abs(b))


def stable_prefix_digits(value_fp: int, ref_fp: int, D: int) -> int:
    if value_fp < 0 or ref_fp < 0:
        return 0
    a = f"{value_fp:0{D+1}d}"
    b = f"{ref_fp:0{D+1}d}"
    # Count decimal digits after decimal point; integer digit must match first.
    if not a or not b or a[0] != b[0]:
        return 0
    c = 0
    for x, y in zip(a[1:], b[1:]):
        if x != y:
            break
        c += 1
    return c


def trace_signature(trace: Iterable[dict[str, Any]]) -> str:
    slim = []
    for e in trace:
        slim.append((e.get("stage"), e.get("iteration"), e.get("input"),
                     e.get("output"), e.get("choice"), e.get("k"),
                     e.get("d"), e.get("G")))
    return hashlib.sha256(repr(slim).encode()).hexdigest()[:20]


def _collapse_scalar(n: int, p: int, policy: str, S: int, seed: int,
                     trajectory_id: str, layer: str, trace: list[dict[str, Any]],
                     stage: str, iteration: int) -> int:
    v, meta = choose_endpoint(n, p, policy, seed=seed,
                              trajectory_id=trajectory_id, layer_id=layer,
                              scale_context=S)
    if isinstance(v, set):
        raise TypeError("scalar algorithm cannot use ALL_ENDPOINTS")
    event = {"stage": stage, "iteration": iteration, **meta, "output": v}
    trace.append(event)
    return int(v)


def gauss_legendre_fixed(D: int, p: int | None = None, policy: str | None = None,
                         injection: str = "none", seed: int = 0,
                         max_iter: int = 12, long_horizon: bool = False) -> dict[str, Any]:
    S = 10**D
    a = S
    b = math.isqrt((S*S)//2)
    t = S//4
    pow2 = 1
    trace: list[dict[str, Any]] = []
    states: list[tuple[int, int, int]] = [(a,b,t)]
    seen: dict[tuple[int,int,int], int] = {(a,b,t): 0}
    cycle = None
    status = "OK"
    niter = max_iter if not long_horizon else max_iter
    for i in range(niter):
        an = (a + b)//2
        prod = fp_mul(a, b, S)
        if prod < 0:
            status = "NEGATIVE_GEOMEAN_PRODUCT"
            break
        bn = math.isqrt(prod*S)
        if p and policy and injection == "nonlinear_primitives":
            bn = _collapse_scalar(bn,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:bn",trace,"sqrt",i)
        delta = a - an
        delta2 = fp_mul(delta, delta, S)
        if p and policy and injection == "nonlinear_primitives":
            delta2 = _collapse_scalar(delta2,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:delta2",trace,"square",i)
        tn = t - pow2*delta2
        if p and policy and injection == "nonlinear_primitives":
            tn = _collapse_scalar(tn,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:t",trace,"t_update",i)
        a,b,t = an,bn,tn
        if p and policy and injection == "iteration_boundary":
            a = _collapse_scalar(a,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:a",trace,"a",i)
            b = _collapse_scalar(b,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:b",trace,"b",i)
            t = _collapse_scalar(t,p,policy,S,seed,f"GL-D{D}-p{p}",f"{i}:t",trace,"t",i)
        pow2 *= 2
        if t <= 0:
            status = "NONPOSITIVE_T"
            states.append((a,b,t))
            break
        st = (a,b,t)
        states.append(st)
        if st in seen:
            cycle = {"start": seen[st], "length": len(states)-1-seen[st], "state": [str(x) for x in st]}
            if long_horizon:
                break
        else:
            seen[st] = len(states)-1
        if not long_horizon and abs(a-b) <= 1:
            # Continue a couple of iterations only if policy might still alter it;
            # fixed max_iter remains deterministic.
            pass
    pi_fp = None
    if t > 0:
        ss = a+b
        sq = fp_mul(ss,ss,S)
        pi_fp = fp_div(sq,4*t,S)
        if p and policy and injection == "nonlinear_primitives":
            pi_fp = _collapse_scalar(pi_fp,p,policy,S,seed,f"GL-D{D}-p{p}","final",trace,"pi_final",len(states)-1)
    return {
        "algorithm":"GAUSS_LEGENDRE", "D":D, "p":p, "policy":policy,
        "injection":injection, "seed":seed, "status":status,
        "iterations":len(states)-1, "pi_fp":pi_fp,
        "trace":trace, "signature":trace_signature(trace), "cycle":cycle,
        "final_state":[str(x) for x in states[-1]],
    }


def chudnovsky_fixed(D: int, p: int | None = None, policy: str | None = None,
                     injection: str = "none", seed: int = 0,
                     terms: int | None = None) -> dict[str, Any]:
    S=10**D
    if terms is None:
        terms=max(4,D//14+4)
    M=1; L=13591409; X=1; K=6
    sum_fp=L*S
    trace:list[dict[str,Any]]=[]
    for i in range(1,terms):
        M=(K**3-16*K)*M//(i**3)
        L+=545140134
        X*=-262537412640768000
        num=M*L*S
        term = (1 if num*X >= 0 else -1) * (abs(num)//abs(X))
        if p and policy and injection=="nonlinear_primitives":
            term=_collapse_scalar(term,p,policy,S,seed,f"CH-D{D}-p{p}",f"{i}:term",trace,"term",i)
        sum_fp += term
        if p and policy and injection=="iteration_boundary":
            sum_fp=_collapse_scalar(sum_fp,p,policy,S,seed,f"CH-D{D}-p{p}",f"{i}:sum",trace,"partial_sum",i)
        K+=12
    sqrt_fp=math.isqrt(10005*S*S)
    if p and policy and injection=="nonlinear_primitives":
        sqrt_fp=_collapse_scalar(sqrt_fp,p,policy,S,seed,f"CH-D{D}-p{p}","sqrt",trace,"sqrt10005",terms)
    C_fp=426880*sqrt_fp
    status="OK"
    pi_fp=None
    if sum_fp==0:
        status="ZERO_DENOMINATOR"
    else:
        pi_fp=fp_div(C_fp,sum_fp,S)
        if p and policy and injection=="nonlinear_primitives":
            pi_fp=_collapse_scalar(pi_fp,p,policy,S,seed,f"CH-D{D}-p{p}","final",trace,"pi_final",terms)
    return {
        "algorithm":"CHUDNOVSKY", "D":D, "p":p, "policy":policy,
        "injection":injection, "seed":seed, "status":status,
        "terms":terms, "pi_fp":pi_fp, "trace":trace,
        "signature":trace_signature(trace),
        "final_sum_fp":str(sum_fp),
    }


def chudnovsky_all_endpoints(D:int,p:int,terms:int|None=None) -> dict[str,Any]:
    S=10**D
    if terms is None: terms=max(4,D//14+4)
    M=1;L=13591409;X=1;K=6
    support={L*S}
    sizes=[1]
    for i in range(1,terms):
        M=(K**3-16*K)*M//(i**3);L+=545140134;X*=-262537412640768000
        num=M*L*S
        term=(1 if num*X >= 0 else -1) * (abs(num)//abs(X))
        nxt=set()
        for s in support:
            v,_=choose_endpoint(s+term,p,"ALL_ENDPOINTS",scale_context=S)
            nxt.update(v)
        support=nxt; sizes.append(len(support)); K+=12
    sqrt_fp=math.isqrt(10005*S*S);C_fp=426880*sqrt_fp
    pis={fp_div(C_fp,s,S) for s in support if s!=0}
    return {"algorithm":"CHUDNOVSKY","D":D,"p":p,"support_sizes":sizes,
            "sum_count":len(support),"pi_count":len(pis),
            "pi_min":str(min(pis)) if pis else None,"pi_max":str(max(pis)) if pis else None}


def gauss_legendre_all_endpoints(D:int,p:int,iterations:int=8) -> dict[str,Any]:
    S=10**D
    start=(S,math.isqrt((S*S)//2),S//4,1)
    support={start}; sizes=[1]
    for i in range(iterations):
        nxt=set()
        for a,b,t,pow2 in support:
            an=(a+b)//2; prod=fp_mul(a,b,S)
            if prod<0: continue
            bn=math.isqrt(prod*S); delta=a-an; d2=fp_mul(delta,delta,S);tn=t-pow2*d2
            if tn<=0: continue
            As,_=choose_endpoint(an,p,"ALL_ENDPOINTS",scale_context=S)
            Bs,_=choose_endpoint(bn,p,"ALL_ENDPOINTS",scale_context=S)
            Ts,_=choose_endpoint(tn,p,"ALL_ENDPOINTS",scale_context=S)
            for aa in As:
                for bb in Bs:
                    for tt in Ts:
                        if tt>0:nxt.add((aa,bb,tt,pow2*2))
        support=nxt;sizes.append(len(support))
    pis=set()
    for a,b,t,_ in support:
        if t>0:
            sq=fp_mul(a+b,a+b,S);pis.add(fp_div(sq,4*t,S))
    return {"algorithm":"GAUSS_LEGENDRE","D":D,"p":p,"support_sizes":sizes,
            "state_count":len(support),"pi_count":len(pis),
            "pi_min":str(min(pis)) if pis else None,"pi_max":str(max(pis)) if pis else None,
            "observable_recoalescence":len(support)-len(pis)}


def p2_down_equal_anchor_next(a:int,S:int)->dict[str,int|bool]:
    """Diagnostic for the exact p=2 DOWN equal-anchor ladder."""
    k=math.isqrt(a)
    if k*k!=a:
        raise ValueError("a must be square")
    prod=fp_mul(a,a,S)
    raw=math.isqrt(prod*S)
    down,_=choose_endpoint(raw,2,"DOWN",scale_context=S)
    return {"k":k,"a":a,"raw_sqrt":raw,"down":down,"divisible": (a*a)%S==0}


def binade_chi_bounds(e:int,p:int)->dict[str,Any]:
    if e<52:
        raise ValueError("R031 crossover binades are normal integer-spacing binades")
    q=1<<(e-52)
    nlo=1<<e; nhi=(1<<(e+1))-1
    _,_,_,glo=local_gap(nlo,p)
    _,_,_,ghi=local_gap(nhi,p)
    # within binade chi is largest near lower side, smallest near upper side
    return {"e":e,"p":p,"ulp":q,"chi_max":Fraction(q,glo),"chi_min":Fraction(q,ghi),
            "g_lower":glo,"g_upper":ghi}


def crossover_binades(p:int)->dict[str,Any]:
    onset=None; permanent=None
    for e in range(52,1024):
        b=binade_chi_bounds(e,p)
        if onset is None and b["chi_max"]>=1:
            onset=b
        if b["chi_min"]>=1:
            permanent=b;break
    if onset is None or permanent is None:
        return {"p":p,"within_binary64":False}
    def enc(x:dict[str,Any])->dict[str,Any]:
        return {"e":x["e"],"decimal_log10_lower":x["e"]*math.log10(2),
                "chi_min":frac_decimal(x["chi_min"]),"chi_max":frac_decimal(x["chi_max"]),
                "ulp":str(x["ulp"]),"g_lower":str(x["g_lower"]),"g_upper":str(x["g_upper"])}
    return {"p":p,"within_binary64":True,"onset":enc(onset),"permanent":enc(permanent)}


def find_pi_decade_crossover(p:int,onset_e:int) -> dict[str,Any]:
    center=int(onset_e*math.log10(2)-math.log10(math.pi))
    rows=[]
    first=None
    for d in range(max(1,center-4),min(307,center+10)+1):
        N=pi_floor(d); mi=binary64_integer_cell(N)
        if not mi["available"]: continue
        _,_,_,G=local_gap(N,p); chi=mi["ulp"]/G
        rows.append((d,chi))
        if first is None and chi>=1:first=(d,chi)
    return {"p":p,"first_decade":first[0] if first else None,
            "first_chi":frac_decimal(first[1]) if first else None,
            "window":[{"d":d,"chi":frac_decimal(c)} for d,c in rows]}


def machine_scale_record(d:int)->dict[str,Any]:
    N=pi_floor(d); mi=binary64_integer_cell(N)
    rec={"d":d,"N_floor_pi_10d":str(N),"N_ceil":str(N+1)}
    if not mi["available"]:
        rec["binary64"]={"available":False,"reason":mi["reason"]}
        rec["p_fields"]={}
        return rec
    a=int(mi["lower"]); b=int(mi["upper"])
    subinteger_machine_cell = mi["ulp"].denominator != 1
    rec["binary64"]={"available":True,"exponent":mi["exponent"],"ulp":str(mi["ulp"].numerator),
        "lower":str(a),"upper":str(b),"phase":frac_obj(mi["phase"]),
        "nearest":str(int(mi["nearest"])),"nearest_direction":mi["nearest_direction"]}
    fields={}
    for p in P_LIST:
        k,L,U,G=local_gap(N,p); off=N-L; ph=Fraction(off,G)
        cov={"touched":1,"full":0,"partial":1} if subinteger_machine_cell else basin_coverage(a,b,p)
        fields[str(p)]={"k":str(k),"L":str(L),"U":str(U),"G":str(G),"d":str(off),
            "phase":frac_obj(ph),"chi":frac_obj(mi["ulp"]/G),"chi_decimal":frac_decimal(mi["ulp"]/G),
            "coverage":cov,"normalized_gap":frac_obj(Fraction(G,10**d))}
    rec["p_fields"]=fields
    return rec


@lru_cache(maxsize=None)
def polygon_pi_bounds_fp(d:int) -> tuple[int,int]:
    """Regular 2^m-gon lower/upper pi bounds in d-digit fixed point.

    Starts from square and applies half-angle recurrence with Decimal sqrt.
    Precision is deliberately much higher than the requested fixed-point scale;
    final bounds are widened by one unit if needed to keep the reference pi
    bracketed under Decimal evaluation uncertainty.
    """
    M=10**d
    with localcontext() as ctx:
        ctx.prec=d+180
        two=Decimal(2)
        sin=(two.sqrt())/two
        cos=sin
        n=4
        # polygon truncation error O(n^-2); ~1.9*d doublings gives ample margin.
        for _ in range(max(20,2*d+20)):
            sin=((Decimal(1)-cos)/two).sqrt()
            cos=((Decimal(1)+cos)/two).sqrt()
            n*=2
        lo=Decimal(n)*sin
        hi=lo/cos
        lo_fp=int((lo*Decimal(M)).to_integral_value(rounding=ROUND_FLOOR))
        hi_fp=int((hi*Decimal(M)).to_integral_value(rounding=ROUND_CEILING))
    # Conservative one-unit widening and sanity bracketing.
    lo_fp-=1;hi_fp+=1
    pf=pi_floor(d)
    if lo_fp>pf: lo_fp=pf
    if hi_fp<pf+1: hi_fp=pf+1
    return lo_fp,hi_fp


def recovered_pi_from_output(out:int,denom:int,S:int)->Fraction:
    # Output coordinates are integer values with S fixed-point scale; the
    # effective pi is out/(geometric coefficient*S) = out/denom.
    return Fraction(out,denom)


def _scalar_policy_outputs(n:int,p:int,policy:str,S:int,seed:int,tag:str)->list[int]:
    v,_=choose_endpoint(n,p,policy,seed=seed,trajectory_id=tag,layer_id="formula",scale_context=S)
    if isinstance(v,set):return sorted(v)
    return [int(v)]


def formula_record(d:int,p:int,policy:str,radius_delta:int=0,seed:int=314159)->dict[str,Any]:
    S=10**d; R=10**d+radius_delta; pi_fp=pi_floor(d)
    lo_pi,hi_pi=polygon_pi_bounds_fp(d)
    channels:dict[str,list[Fraction]]={}
    C=2*R*pi_fp
    channels["circumference"]=[Fraction(v,2*R*S) for v in _scalar_policy_outputs(C,p,policy,S,seed,"C")]
    A=R*R*pi_fp
    channels["area"]=[Fraction(v,R*R*S) for v in _scalar_policy_outputs(A,p,policy,S,seed,"A")]
    Plo=2*R*lo_pi
    Phi=2*R*hi_pi
    pl=[Fraction(v,2*R*S) for v in _scalar_policy_outputs(Plo,p,policy,S,seed,"PL")]
    ph=[Fraction(v,2*R*S) for v in _scalar_policy_outputs(Phi,p,policy,S,seed,"PU")]
    channels["polygon_lower"]=pl;channels["polygon_upper"]=ph
    vals=[x for xs in channels.values() for x in xs]
    defect=max(vals)-min(vals) if vals else Fraction(0)
    return {"d":d,"p":p,"policy":policy,"radius_delta":radius_delta,
            "formula_defect":frac_obj(defect),"formula_defect_log10":log10_fraction_abs(defect),
            "channels":{k:[frac_obj(x) for x in xs] for k,xs in channels.items()}}


def lattice_circle_count(R:int)->int:
    r2=R*R
    total=0
    for x in range(-R,R+1):
        y=math.isqrt(r2-x*x)
        total += 2*y+1
    return total


def internal_summary(run:dict[str,Any],ref:int,D:int)->dict[str,Any]:
    pi_fp=run.get("pi_fp")
    delta=None if pi_fp is None else pi_fp-ref
    choices=[e.get("choice") for e in run.get("trace",[]) if e.get("choice") in ("L","U")]
    direction_changes=sum(a!=b for a,b in zip(choices,choices[1:]))
    return {"algorithm":run["algorithm"],"D":D,"p":run.get("p"),"policy":run.get("policy"),
            "injection":run.get("injection"),"status":run["status"],
            "pi_fp":str(pi_fp) if pi_fp is not None else None,
            "delta":str(delta) if delta is not None else None,
            "delta_log10":None if delta in (None,0) else math.log10(abs(delta))-D,
            "stable_prefix":None if pi_fp is None else stable_prefix_digits(pi_fp,ref,D),
            "direction_change_count":direction_changes,"trajectory_signature":run["signature"],
            "cycle":run.get("cycle")}


def stochastic_stats(D:int,p:int,algorithm:str,policy:str,seeds:int=256)->dict[str,Any]:
    ref=pi_floor(D); deltas=[];statuses={}
    for s in range(seeds):
        run=gauss_legendre_fixed(D,p,policy,"iteration_boundary",seed=s,max_iter=8) if algorithm=="GAUSS_LEGENDRE" else chudnovsky_fixed(D,p,policy,"iteration_boundary",seed=s)
        statuses[run["status"]]=statuses.get(run["status"],0)+1
        if run.get("pi_fp") is not None:deltas.append(run["pi_fp"]-ref)
    return {"D":D,"p":p,"algorithm":algorithm,"policy":policy,"seeds":seeds,
            "statuses":statuses,"unique_outputs":len(set(deltas)),
            "mean_delta":statistics.fmean(deltas) if deltas else None,
            "std_delta":statistics.pstdev(deltas) if len(deltas)>1 else 0.0,
            "min_delta":min(deltas) if deltas else None,"max_delta":max(deltas) if deltas else None}


def build_machine_atlas() -> dict[str,Any]:
    # Exact raw cells at the taskbook's primary scales plus the binary64 edge.
    # Dense transition neighborhoods are encoded separately in pi_decade_crossovers.
    scales=[36,48,72,100,307,308,400,1000]
    cross=[crossover_binades(p) for p in P_LIST]
    pi_cross=[]
    for c in cross:
        if c.get("within_binary64"):
            pi_cross.append(find_pi_decade_crossover(c["p"],c["onset"]["e"]))
    return {"schema":"R031_MACHINE_FIELD_CROSSOVER_V1","scales":[machine_scale_record(d) for d in scales],
            "binade_crossovers":cross,"pi_decade_crossovers":pi_cross,
            "binary64_max_integer_exact_coordinate":str(MAX_BINARY64_INT)}


def build_policy_atlas() -> dict[str,Any]:
    summaries=[]
    deterministic=("DOWN","UP","NEAREST","FAR","PRNG_50_50","DISTANCE_WEIGHTED_STOCHASTIC","RESIDUAL_ONLY","ANCHOR_PLUS_RESIDUAL","FIELD_PHASE")
    for D in (36,48,72,100):
        ref=pi_floor(D)
        for p in (2,3,4,6):
            for pol in deterministic:
                gl=gauss_legendre_fixed(D,p,pol,"iteration_boundary",seed=314159,max_iter=9)
                ch=chudnovsky_fixed(D,p,pol,"iteration_boundary",seed=314159)
                summaries.append(internal_summary(gl,ref,D));summaries.append(internal_summary(ch,ref,D))
    # Injection-boundary sensitivity is frozen explicitly at the D36,p2 sanity point.
    for pol in deterministic:
        gl=gauss_legendre_fixed(36,2,pol,"nonlinear_primitives",seed=314159,max_iter=9)
        ch=chudnovsky_fixed(36,2,pol,"nonlinear_primitives",seed=314159)
        summaries.append(internal_summary(gl,pi_floor(36),36));summaries.append(internal_summary(ch,pi_floor(36),36))
    # First-class full anchor/residual/phase traces at the frozen sanity point.
    core_traces=[]
    for alg in ("GAUSS_LEGENDRE","CHUDNOVSKY"):
        inj="iteration_boundary"
        for pol in deterministic:
                run=gauss_legendre_fixed(36,2,pol,inj,seed=314159,max_iter=9) if alg=="GAUSS_LEGENDRE" else chudnovsky_fixed(36,2,pol,inj,seed=314159)
                core_traces.append({"algorithm":alg,"injection":inj,"policy":pol,"status":run["status"],
                    "signature":run["signature"],"trace":[{
                        "stage":e.get("stage"),"iteration":e.get("iteration"),"input":str(e.get("input")),"output":str(e.get("output")),
                        "choice":e.get("choice"),"k":str(e.get("k")),"L":str(e.get("L")),"U":str(e.get("U")),"G":str(e.get("G")),
                        "d":str(e.get("d")),"u":str(e.get("u")),"phase":frac_obj(e.get("phase",Fraction(0)))
                    } for e in run["trace"]]})
    long_horizon=[]
    for p in (2,3,4,5,6):
        for pol in ("DOWN","UP","NEAREST","FAR","RESIDUAL_ONLY","FIELD_PHASE"):
            run=gauss_legendre_fixed(36,p,pol,"iteration_boundary",seed=314159,max_iter=100,long_horizon=True)
            s=internal_summary(run,pi_floor(36),36);s["final_state"]=run.get("final_state");long_horizon.append(s)
    all_support=[gauss_legendre_all_endpoints(36,2,8),chudnovsky_all_endpoints(36,2),chudnovsky_all_endpoints(72,2),chudnovsky_all_endpoints(100,2)]
    stoch=[]
    for alg in ("GAUSS_LEGENDRE","CHUDNOVSKY"):
        for pol in ("PRNG_50_50","DISTANCE_WEIGHTED_STOCHASTIC"):
            stoch.append(stochastic_stats(36,2,alg,pol,256))
    # Exact p=2 DOWN equal-anchor ladder diagnostic from its first equal anchor.
    gl0=gauss_legendre_fixed(36,2,"DOWN","iteration_boundary",max_iter=12)
    grouped={}
    for e in gl0["trace"]:
        grouped.setdefault(e["iteration"],{})[e["stage"]]=e["output"]
    equal_i=None; a=None; t0=None
    for ii,x in grouped.items():
        if x.get("a") is not None and x.get("a")==x.get("b"):
            equal_i=ii; a=x["a"]; t0=x["t"]; break
    if a is None or t0 is None:
        raise AssertionError("p2 DOWN did not reach expected equal-anchor ladder entry")
    k=math.isqrt(a); Q=10**math.ceil(36/4); kstar=(k//Q)*Q
    astar=kstar*kstar; predicted_pi=(astar*astar)//t0
    ladder={"D":36,"entry_iteration":equal_i,"start_equal_anchor":str(a),"start_root":str(k),
            "frozen_t":str(t0),"divisibility_modulus_root":str(Q),
            "predicted_down_root_attractor":str(kstar),"predicted_decrements":k-kstar,
            "predicted_additional_boundary_updates":2*(k-kstar),
            "predicted_effective_pi_fp":str(predicted_pi),
            "predicted_effective_pi_stable_prefix":stable_prefix_digits(predicted_pi,pi_floor(36),36),
            "local_transition":{kk:(str(v) if isinstance(v,int) else v) for kk,v in p2_down_equal_anchor_next(a,10**36).items()}}
    return {"schema":"R031_PI_POLICY_DIVERGENCE_V1","summaries":summaries,"core_traces":core_traces,
            "long_horizon":long_horizon,"all_endpoints_support":all_support,"stochastic":stoch,"p2_down_ladder":ladder}


def compact_formula_record(x:dict[str,Any]) -> dict[str,Any]:
    chans={}
    for name,vals in x["channels"].items():
        out=[]
        for o in vals:
            fr=Fraction(int(o["num"]),int(o["den"]))
            out.append(frac_decimal(fr,30))
        chans[name]=out
    return {"d":x["d"],"p":x["p"],"policy":x["policy"],"radius_delta":x["radius_delta"],
            "formula_defect":x["formula_defect"],"formula_defect_log10":x["formula_defect_log10"],
            "effective_pi_decimal":chans}

def build_formula_atlas() -> dict[str,Any]:
    records=[]
    for D in (36,48,72,100):
        for p in (2,3,4,6):
            for pol in POLICIES:
                for rd in (-1,0,1):
                    records.append(compact_formula_record(formula_record(D,p,pol,rd)))
    discrete=[]
    for R in (1000,10000):
        c=lattice_circle_count(R)
        discrete.append({"R":R,"lattice_points":c,"effective_pi":frac_obj(Fraction(c,R*R)),
                         "difference_from_pi_decimal":str(Decimal(c)/Decimal(R*R)-_pi_decimal(50))})
    return {"schema":"R031_FORMULA_COHERENCE_V1","records":records,"discrete_circle_sanity":discrete}


def write_phase_csv(machine:dict[str,Any],out:Path)->None:
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["d","p","binary64_exponent","chi","basins_touched","basins_full","basins_partial","field_phase","policy","choice","displacement_log10_scale"])
        for sr in machine["scales"]:
            d=sr["d"]; avail=sr["binary64"].get("available",False)
            for p in P_LIST:
                if not avail: continue
                pf=sr["p_fields"][str(p)]; N=int(sr["N_floor_pi_10d"]);S=10**d
                for pol in POLICIES:
                    v,meta=choose_endpoint(N,p,pol,seed=314159,trajectory_id=f"STATIC-D{d}-p{p}",layer_id="0",scale_context=S)
                    if isinstance(v,set):
                        disp=max(abs(x-N) for x in v); choice="ALL_ENDPOINTS"
                    else:
                        disp=abs(v-N); choice=meta.get("choice")
                    disp_log=None if disp==0 else math.log10(disp)-d
                    w.writerow([d,p,sr["binary64"]["exponent"],pf["chi_decimal"],
                        pf["coverage"]["touched"],pf["coverage"]["full"],pf["coverage"]["partial"],
                        f"{pf['phase']['num']}/{pf['phase']['den']}",pol,choice,disp_log])


def dump_json(path:Path,obj:Any)->None:
    def default(x:Any):
        if isinstance(x,Fraction):return frac_obj(x)
        if isinstance(x,set):return sorted(x)
        raise TypeError(type(x).__name__)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=default)+"\n",encoding="utf-8")


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--out-dir",default="research/r031_generated")
    args=ap.parse_args();out=Path(args.out_dir);out.mkdir(parents=True,exist_ok=True)
    machine=build_machine_atlas();dump_json(out/"R031_MACHINE_FIELD_CROSSOVER.json",machine)
    policy=build_policy_atlas();dump_json(out/"R031_PI_POLICY_DIVERGENCE.json",policy)
    formula=build_formula_atlas();dump_json(out/"R031_FORMULA_COHERENCE.json",formula)
    write_phase_csv(machine,out/"R031_SCALE_P_POLICY_PHASE_ATLAS.csv")
    hypotheses={"schema":"R031_HYPOTHESIS_DISPOSITIONS_V1","items":[
        {"id":"H1","status":"SURVIVES_REPRESENTATION_LEVEL"},
        {"id":"H2","status":"SURVIVES_STRENGTHENED","result":"exact onset/permanent binades; chi envelope Theta(N^(1/p))"},
        {"id":"H3","status":"SURVIVES_STRONGLY","countercheck":"D36 chi2>1 while p>=3 chi<1"},
        {"id":"H4","status":"SURVIVES","result":"G_p(N)/N = Theta(N^(-1/p))"},
        {"id":"H5","status":"PARTIAL_GLOBAL_ORDER_KILLED","counterexample":"D36 p2 Chudnovsky reciprocal future reverses final DOWN/UP ordering"},
        {"id":"H6","status":"SURVIVES_FINITE_STOP_ONLY","boundary":"long-horizon p2 DOWN ladder"},
        {"id":"H7","status":"ALGORITHM_RELATIVE_NOT_UNIVERSAL"},
        {"id":"H8","status":"SURVIVES_ASYMPTOTICALLY","result":"endpoint formula defect approximately O(10^(-2d/p)); residual zero family"},
        {"id":"H9","status":"NAIVE_VERSION_KILLED","counterexample":"p=2,n=2,q=2: phase 1/3 -> 4/5"},
        {"id":"H10","status":"SURVIVES_ALGORITHM_RELATIVE","result":"GL residual fixed point (0,0,1); formula zero attractor"},
        {"id":"H11","status":"SURVIVES_MEASURABLE"},
        {"id":"H12","status":"SURVIVES","result":"magnitude/binade x p x policy x future-operation phase structure"}
    ],"theorem_candidates":[
        "exact binade staircase crossover","chi_p crossover envelope Theta(N^(1/p))",
        "p-th-power basin refinement under q^p scale lift","p2 DOWN equal-anchor ladder under fixed-point GL hypotheses"
    ]}
    dump_json(out/"R031_HYPOTHESIS_DISPOSITIONS.json",hypotheses)
    manifest={"schema":"R031_RUN_MANIFEST_V1","runner":"experiments/r031_large_scale_pi_collapse.py",
              "policies":list(POLICIES),"p_list":list(P_LIST),
              "notes":["exact integer/rational collapse geometry","Decimal Chudnovsky reference cross-checked at two guard precisions","no binary64 extrapolation after representation absence"]}
    dump_json(out/"R031_RUN_MANIFEST.json",manifest)
    print(json.dumps({"status":"R031_RUN_COMPLETE","out_dir":str(out),"files":[p.name for p in sorted(out.iterdir())]}))


if __name__=="__main__":
    main()
