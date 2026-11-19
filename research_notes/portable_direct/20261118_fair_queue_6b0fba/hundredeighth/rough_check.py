"""Cyclotomic maintenance of the first-cosine squarefree rough-prime readout."""
import argparse
import json
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import factorial, gcd
from pathlib import Path


def prime_factors(n):
    out = []
    k = 2
    while k*k <= n:
        while n % k == 0:
            out.append(k)
            n //= k
        k += 1
    if n > 1:
        out.append(n)
    return out


@cache
def primes_until(T):
    sieve = bytearray([1]) * (T+1)
    sieve[:2] = bytes(2)
    for p in range(2, T+1):
        if sieve[p]:
            for k in range(p*p,T+1,p):
                sieve[k] = 0
    return [p for p in range(2,T+1) if sieve[p]]


def standard_remainder(f, divisor):
    """Independent exact polynomial long division, ascending degree arrays."""
    work = f[:]
    nz = [(j, a) for j, a in enumerate(divisor) if a]
    for i in range(len(work)-1, len(divisor)-2, -1):
        c = work[i]
        if c:
            for j, a in nz:
                work[i-len(divisor)+1+j] -= c*a
    return work[:len(divisor)-1]


def exact_quotient(f, divisor):
    quotient = [0] * (len(f)-len(divisor)+1)
    work = f[:]
    nz = [(j, a) for j, a in enumerate(divisor) if a]
    for i in range(len(quotient)-1, -1, -1):
        q = work[i+len(divisor)-1]
        quotient[i] = q
        for j, a in nz:
            work[i+j] -= q*a
    assert not any(work)
    return quotient


@cache
def cyclotomic(n):
    f = [-1] + [0]*(n-1) + [1]
    for d in range(1, n):
        if n % d == 0:
            f = exact_quotient(f, cyclotomic(d))
    return f


class Fibers:
    def __init__(self, T):
        odd = set(prime_factors(T)) - {2}
        assert len(odd) <= 1 and T >= 2
        self.T = T
        self.p = next(iter(odd), None)
        self.L = 2*T // self.p if self.p else None
        self.delta = [0] * (2*T-self.L if self.p else 2*T)
        self.nonzero = 0
        self.updates = 0

    def edit(self, i, value):
        old = self.delta[i]
        self.delta[i] = old + value
        self.nonzero += (self.delta[i] != 0) - (old != 0)
        self.updates += 1

    def insert(self, n, value):
        assert 0 < n < self.T
        for i, c in ((n, value), (2*self.T-n, -value)):
            if self.p is None:
                self.edit(i, c)
                continue
            j, r = divmod(i, self.L)
            signed = c * (-1)**j
            if j < self.p-1:
                self.edit(r+j*self.L, signed)
            if j:
                self.edit(r+(j-1)*self.L, -signed)

    def power_basis(self):
        out = self.delta[:]
        if self.p:
            for r in range(self.L):
                total = 0
                for j in range(self.p-2, -1, -1):
                    i = r+j*self.L
                    total += self.delta[i]
                    out[i] = (-1)**j * total
        return out


def source_events(T, y, window):
    """Each allowed squarefree n<T occurs exactly once as d*s; bucket by largest rough prime."""
    primes = set(primes_until(T))
    if window != sorted(set(window)) or any(p not in primes or p <= y for p in window):
        raise ValueError("an insertion must be a new prime above the cutoff")
    buckets = {p: [] for p in [1]+window}
    # SPF and squarefree tests for the smooth part s are tabulated once.
    spf = list(range(T))
    for p in range(2, T):
        if spf[p] == p:
            for k in range(p*p, T, p):
                if spf[k] == k:
                    spf[k] = p
    smooth = [False, True] + [False]*(T-2)
    for n in range(2, T):
        p = spf[n]
        smooth[n] = smooth[n//p] and n//p % p != 0 and p <= y
    terms = [s for s in range(1,T) if smooth[s]]
    states = []

    def visit(d, depth, start, last):
        states.append(d)
        for s in terms:
            if s*d >= T:
                break
            buckets[last].append((s*d, (-1)**depth))
        for j in range(start,len(window)):
            p = window[j]
            if d*p >= T:
                break
            visit(d*p, depth+1, j+1, p)

    visit(1, 0, 0, 1)
    return buckets, states


@cache
def angle_and_degree(bits):
    def atan_interval(v):
        term = Fraction(1, v)
        total = Fraction(0)
        j = 0
        while True:
            total += term
            term = -term * Fraction(2*j+1, (2*j+3)*v*v)
            if abs(term) < Fraction(1, 2**(bits+12)):
                return min(total, total+term), max(total, total+term)
            j += 1
    l5, h5 = atan_interval(5)
    l239, h239 = atan_interval(239)
    lo, hi = 8*l5-2*h239, 8*h5-2*l239
    scale = 2**(bits+4)
    angle = Fraction(int(lo * scale), scale)
    assert 0 < angle < 2 and hi-angle < Fraction(1, 2**(bits+3))
    j = 0
    while Fraction(2**(2*j+2), factorial(2*j+2)) >= Fraction(1, 2**(bits+3)):
        j += 1
    return angle, j


@cache
def interval(n, T, bits):
    angle, degree = angle_and_degree(bits)
    x = angle * Fraction(n, T)
    term = value = Fraction(1)
    for j in range(1, degree+1):
        term *= -x*x / ((2*j-1)*(2*j))
        value += term
    scaled = value * 2**bits
    k = scaled.numerator // scaled.denominator
    return k-1, k+2


def add_bound(lo, hi, n, sign, T, bits):
    a,b = interval(n,T,bits)
    return (lo+a,hi+b) if sign == 1 else (lo-b,hi-a)


def independent_signs(T,y,M):
    """Independent population via naive trial factoring, retaining the actual chosen window."""
    e = [0]*(2*T)
    for n in range(1,T):
        factors = prime_factors(n)
        if len(set(factors)) != len(factors):
            continue
        rough = {p for p in factors if p>y}
        if rough <= M:
            e[n] = (-1)**len(rough)
            e[2*T-n] = -e[n]
    return e


def digest(x):
    return sha256(json.dumps(x,separators=(",",":")).encode()).hexdigest()


def audit_case(T,y,skip):
    window = [p for p in primes_until(T) if p>y and p not in skip]
    buckets, ds = source_events(T,y,window)
    state = Fibers(T)
    modulo = cyclotomic(4*T)
    bits = 4
    lo = hi = 0
    signed_terms = []
    M = set()
    data = []
    for p in [1]+window:
        if p != 1:
            M.add(p)
        for n,sign in buckets[p]:
            state.insert(n,sign)
            signed_terms.append((n,sign))
            lo,hi = add_bound(lo,hi,n,sign,T,bits)
        while lo <= 0 <= hi:
            bits *= 2
            lo = hi = 0
            for n,sign in signed_terms:
                lo,hi = add_bound(lo,hi,n,sign,T,bits)
        f = independent_signs(T,y,M)
        assert state.power_basis() == standard_remainder(f,modulo)
        assert state.nonzero == sum(x!=0 for x in state.delta) > 0
        assert max(map(abs,state.delta)) <= (2 if state.p else 1)
        data.append([p,1 if lo>0 else -1,lo,hi,bits,state.nonzero])
    changes = [data[i] for i in range(1,len(data)) if data[i][1]!=data[i-1][1]]
    return dict(T=T,y=y,skipped=skip,steps_with_empty_prefix=len(data),subscales_without_vanishing_endpoint=len(ds),
                different_weight_terms=len(signed_terms),coordinate_updates=state.updates,
                coordinate_count=len(state.delta),peak_certifying_fraction_bits=bits,
                all_prefix_signs="".join("+" if row[1]>0 else "-" for row in data),
                sign_change_rows=changes,first_two_insertions=data[1:3],first_and_final=[data[0],data[-1]],
                rows_format="last admitted prime (1 for empty), sign, lower, upper, denominator exponent, nonzero fiber coordinates",
                full_rows_sha256=digest(data))


def finite_mixed_support():
    """Independent former support-only control for all primes up to a cutoff, without signs."""
    scales = set()
    two = 4
    while two<=30031:
        L = two
        while L<=30031:
            scales.add(L)
            L*=3
        two*=2
    limit = 3*max(scales)//2
    allowed = [limit+1,1]
    for n in range(2,limit+1):
        ps = prime_factors(n)
        allowed.append(ps[-1] if len(ps)==len(set(ps)) else limit+1)
    largest = cases = 0
    for L in sorted(scales):
        T=3*L//2
        masks = (2,3,5,7,11,13) if L>=68 else range(2,T+1)
        for bound in masks:
            def usable(x):
                x = min(x % (2*T), -x % (2*T))
                return 0<x<T and allowed[x]<=bound
            r = next(r for r in range(1,L) if len({usable(r+j*L) for j in range(3)})>1)
            largest=max(largest,r)
            cases+=1
    return dict(scales=len(scales),cases=cases,maximum_first_witness_r=largest,largest_L=max(scales))


def exhaustive_menus():
    rows = []
    for T in (6,12,18,24,27,32,36,48):
        window = primes_until(T)[1:]
        nz = 0
        for mask in range(1<<len(window)):
            M={p for j,p in enumerate(window) if mask>>j & 1}
            f=independent_signs(T,2,M)
            v=standard_remainder(f,cyclotomic(4*T))
            assert any(v)
            nz+=1
        rows.append([T,nz])
    return rows


def galois_test():
    # Verify equal-floor sharing by a genuine automorphism on a multi-term base.
    T,y = 125,3
    d,e = 29,31
    assert T//d == T//e == 4 and gcd(d,4*T) == gcd(e,4*T) == 1
    mult = e*pow(d,-1,4*T) % (4*T)
    assert gcd(mult,4*T) == 1
    base = [1,2,3]
    def embed(t):
        entries = [0] * (4*T)
        for n in base:
            entries[n*t % (4*T)] += 1
            entries[-n*t % (4*T)] += 1
        return standard_remainder(entries,cyclotomic(4*T))
    left,right = embed(d),embed(e)
    assert left != right and embed(d*mult) == right
    return dict(T=T,y=y,denominators=[d,e], floor_subscale=T//d,
                automorphism_exponent=mult, smooth_squarefree_terms=base,
                distinct_power_basis_hashes=[digest(left),digest(right)])


def trace_energy_test():
    """Exact online real cyclotomic trace versus independent polynomial division."""
    def eval_case(T, edits):
        q = 4*T
        primes = sorted(set(prime_factors(q)))
        divisors = [(q, 1)]
        for p in primes:
            divisors += [(d//p, -mu) for d,mu in divisors]
        bins = {d:{} for d,mu in divisors}
        double_energy = 0
        full = [0]*(q+1)
        hist = []
        for n,weight in edits:
            assert 0 < n < T
            full[n] += weight
            full[q-n] += weight
            for d,mu in divisors:
                counts = bins[d]
                for r in (n%d, (-n)%d):
                    old = counts.get(r,0)
                    counts[r] = old+weight
                    double_energy += d*mu*weight*(2*old+weight)
            assert double_energy % 2 == 0 and double_energy >= 0
            energy = double_energy//2
            remainder = standard_remainder(full,cyclotomic(q))
            assert (energy == 0) == (not any(remainder))
            hist.append(energy)
        return hist
    cases = [(36,3,[5,7]),(108,3,[7,11,17]),(125,2,[5,11]),
             (30,2,[3,7]),(105,3,[5,11,19])]
    records = []
    for T,y,menu in cases:
        eps = independent_signs(T,y,set(menu))[:T]
        history = eval_case(T,[(n,w) for n,w in enumerate(eps) if w])
        population = sum(w*w for w in eps)
        # All exponents +n and -n are distinct modulo 2T.
        assert 0 < history[-1] <= 2*T*population
        records.append(dict(T=T,y=y,menu=menu,terms=population,trace=history[-1],
                            odd_character_upper_bound=2*T*population))
    # This three-term relation is a signed test vector, independent of original menus.
    zero_control = eval_case(15,[(3,1),(7,-1),(13,-1)])
    assert zero_control[-1] == 0 and zero_control[0] > 0
    return dict(original_menus=records,algebraic_zero_control_T15=zero_control)


def main():
    # Origin fixture first two scales, plus a mixed family and genuinely gapped input.
    cases = [(36,3,[]),(386,3,[]),(108,3,[5,13]),(125,2,[3,7]),(128,5,[])]
    duplicate_rejected = False
    try:
        source_events(36,3,[5,5,7])
    except ValueError:
        duplicate_rejected = True
    assert duplicate_rejected
    mixed = standard_remainder(independent_signs(18, 2, {5,7,11,13,17}), cyclotomic(72))
    mixed_terms = [[i,w] for i,w in enumerate(mixed) if w]
    assert mixed_terms == [[5,-2],[7,-2],[19,2]]
    return dict(mixed_content_two_terms=mixed_terms, trace_energy=trace_energy_test(), cases=[audit_case(T,y,s) for T,y,s in cases],
                exhaustive_arbitrary_prime_subsets_T_and_count=exhaustive_menus(),
                complete_prefix_support_only_crosscheck=finite_mixed_support(),
                duplicate_prime_rejected=duplicate_rejected, exact_subscale_conjugacy=galois_test())


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    raw=json.dumps(main(),indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.write_text(raw,encoding="utf-8")
    else:
        print(raw,end="")
