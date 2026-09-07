"""#1162: chi_29 CM / non-LCM certificate, Python standard library only.

All certificate arithmetic uses rational numbers or outward-rounded dyadic
intervals implemented with integers. No floating-point arithmetic is used.
The analytic theta-duality argument is supplied in the accompanying note.
This is an experiment-local verifier, not a general BRC foundation module.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
import json

BITS = 768
SCALE = 1 << BITS

def ceildiv(a: int, b: int) -> int:
    if b < 0:
        a, b = -a, -b
    if b == 0:
        raise ZeroDivisionError
    return -((-a) // b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("Reversed interval")

    @classmethod
    def exact(cls, value: int | F) -> I:
        v = F(value)
        return cls(v.numerator*SCALE // v.denominator,
                   ceildiv(v.numerator*SCALE, v.denominator))

    def __add__(self, other: I | int | F) -> I:
        b = other if isinstance(other, I) else I.exact(other)
        return I(self.lo+b.lo, self.hi+b.hi)

    __radd__ = __add__

    def __neg__(self) -> I:
        return I(-self.hi, -self.lo)

    def __sub__(self, other: I | int | F) -> I:
        return self + -(other if isinstance(other, I) else I.exact(other))

    def __rsub__(self, other: I | int | F) -> I:
        return -self + other

    def __mul__(self, other: I | int | F) -> I:
        b = other if isinstance(other, I) else I.exact(other)
        endpoints = (self.lo*b.lo, self.lo*b.hi,
                     self.hi*b.lo, self.hi*b.hi)
        return I(min(endpoints)//SCALE, ceildiv(max(endpoints), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other: I | int | F) -> I:
        b = other if isinstance(other, I) else I.exact(other)
        if b.lo <= 0 <= b.hi:
            raise ZeroDivisionError("Denominator interval includes zero")
        endpoints = [F(a*SCALE, c)
                     for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        l, h = min(endpoints), max(endpoints)
        return I(l.numerator//l.denominator, ceildiv(h.numerator,h.denominator))

    def __pow__(self, exponent: int) -> I:
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Only nonnegative integer powers")
        acc, base, n = I.exact(1), self, exponent
        while n:
            if n & 1:
                acc = acc*base
            base = base*base
            n //= 2
        return acc

    def abs_upper(self) -> F:
        return F(max(abs(self.lo),abs(self.hi)), SCALE)

    def within(self, lower: F, upper: F) -> bool:
        return F(self.lo,SCALE) > lower and F(self.hi,SCALE) < upper

    def decimal_enclosure(self, digits: int = 18) -> list[str]:
        """Decimal endpoints rounded outwards, using only integer arithmetic."""
        ten = 10**digits
        def fmt(n: int) -> str:
            sign = "-" if n < 0 else ""
            n = abs(n)
            return f"{sign}{n//ten}.{n%ten:0{digits}d}"
        return [fmt(self.lo*ten//SCALE), fmt(ceildiv(self.hi*ten,SCALE))]

def exp_minus_positive(t: F, terms: int = 160) -> I:
    """Enclose exp(-t) by bounding the positive Taylor series for exp(t)."""
    if t < 0 or terms < 0 or t >= terms+2:
        raise ValueError("Invalid Taylor-tail parameters")
    term = F(1)
    partial = term
    for j in range(1, terms+1):
        term = term*t/j
        partial += term
    next_term = term*t/(terms+1)
    upper = partial + next_term/(1-t/(terms+2))
    low, high = 1/upper, 1/partial
    return I(low.numerator*SCALE//low.denominator,
             ceildiv(high.numerator*SCALE, high.denominator))

def character29(n: int) -> int:
    r = n % 29
    if r == 0:
        return 0
    value = pow(r,14,29)
    if value not in (1,28):
        raise AssertionError("Euler criterion failure")
    return 1 if value == 1 else -1

def log_jet(coeff: list[I]) -> list[I]:
    """Positive constant term, Taylor coefficients of log, constant omitted."""
    if coeff[0].lo <= 0:
        raise ValueError("Positive Taylor constant required")
    b = [I.exact(0) for _ in coeff]
    for n in range(1,len(coeff)):
        b[n] = (n*coeff[n] -
                sum(k*b[k]*coeff[n-k] for k in range(1,n)))/(n*coeff[0])
    return b

def character_log_jet(order: int = 39) -> list[I]:
    """Taylor jet of log g_29(z) at z0=9/4; g_29(z)=F_29(sqrt z)/sqrt z."""
    z0, t0 = F(9,4), F(3,2)
    choose = F(1)
    v = []
    for j in range(order+1):
        if j:
            choose = choose*(F(1,2)-(j-1))/j
        v.append(I.exact(-t0*choose/z0**j))
    e0 = exp_minus_positive(t0)
    exponentials = {}
    for a in range(1,30):
        out = [e0**a]+[I.exact(0) for _ in range(order)]
        for n in range(1,order+1):
            out[n] = sum(j*a*v[j]*out[n-j] for j in range(1,n+1))/n
        exponentials[a] = out
    numerator = [sum(character29(a)*exponentials[a][j] for a in range(1,29))
                 for j in range(order+1)]
    denominator = [I.exact(int(j==0))-exponentials[29][j]
                   for j in range(order+1)]
    ln, ld = log_jet(numerator), log_jet(denominator)
    result = [I.exact(0)]
    for j in range(1,order+1):
        log_sqrt = F((-1)**(j+1),2*j*z0**j)
        result.append(ln[j]-ld[j]-log_sqrt)
    return result

def normalized_power_jet(logjet: list[I], power: F) -> list[I]:
    """Jet of (h(z0+w)/h(z0))**power. Normalization leaves signs unchanged."""
    c = [I.exact(1)] + [I.exact(0) for _ in logjet[1:]]
    for n in range(1,len(c)):
        c[n] = power*sum(j*logjet[j]*c[n-j] for j in range(1,n+1))/n
    return c

def power_parameter_coefficients(logjet: list[I]) -> list[I]:
    """Coefficient in w^M of exp(r*sum_j logjet[j] w^j), as polynomial in r."""
    M = len(logjet)-1
    c = [[I.exact(0) for _ in range(M+1)] for _ in range(M+1)]
    c[0][0] = I.exact(1)
    for n in range(1,M+1):
        for k in range(1,n+1):
            c[n][k] = sum(j*logjet[j]*c[n-j][k-1]
                          for j in range(1,n-k+2))/n
    return c[M]

def run() -> dict:
    # Analytic positivity certificate for theta_29(u), u>=1:
    # rho=exp(-pi*u/29)<a. The first five character signs are +--++.
    # f(rho)=1-rho^3-rho^8+rho^15+rho^24 > 1/10.
    # |tail|/rho <= a^35/(1-a^13)<1/25.
    a = F(9,10)
    f_at_a = 1-a**3-a**8+a**15+a**24
    C = -8+15*a**7+24*a**16
    derivative_bound = -3+a**5*C
    tail = a**35/(1-a**13)
    assert [character29(j) for j in range(1,6)] == [1,-1,-1,1,1]
    assert sum(character29(j) for j in range(1,29)) == 0
    assert sum(j*character29(j) for j in range(1,29)) == 0
    assert sum(j*j*character29(j) for j in range(1,29)) == 348
    assert C > 0 and derivative_bound < 0
    assert f_at_a > F(1,10)
    assert tail < F(1,25)
    # pi>31/10 and exp(31/290)>10/9 imply exp(-pi/29)<9/10.
    t = F(31,290)
    assert 1+t+t*t/2 > F(10,9)

    j = 39
    z0 = F(9,4)
    l = character_log_jet(j)
    # (-1)^39 z0^39/(38!) * d^39 log h/dz^39 = (-1)^39*39*z0^39*l_39.
    lcm = (-1)**j*j*z0**j*l[j]
    assert lcm.within(F(-47736,10**6), F(-47735,10**6))

    c = normalized_power_jet(l,F(1,100))
    root = (-1)**j*j*z0**j*c[j]
    assert root.within(F(-196279,10**9),F(-196278,10**9))

    # Uniform obstruction for every real 0<r<=1/60.
    pc = power_parameter_coefficients(l)
    pc = [(-1)**j*j*z0**j*v for v in pc]
    assert all(v.lo > 0 for v in pc[2:])
    remainder_upper = sum(pc[k].abs_upper()*F(1,60)**(k-1)
                          for k in range(2,j+1))
    uniform_upper = F(pc[1].hi,SCALE)+remainder_upper
    assert uniform_upper < F(-106,10**6)
    def Q(r: F) -> I:
        acc = I.exact(0)
        for coefficient in pc[:0:-1]:
            acc = acc*r + coefficient
        return acc
    root_lo, root_hi = F(1670229478,10**11), F(1670229479,10**11)
    assert Q(root_lo).hi < 0 and Q(root_hi).lo > 0
    root64 = Q(F(1,64))*F(1,64)
    assert root64.within(F(-49974,10**9), F(-49973,10**9))

    return {
        "status": "PASS",
        "character": 29,
        "g_29_at_zero": "6",
        "arithmetic": "integer outward-rounded dyadic intervals; exact rational tail inequalities",
        "bits": BITS,
        "exp_Taylor_terms": 160,
        "order": j,
        "z0": "9/4",
        "theta_first5_signs": [1,-1,-1,1,1],
        "theta_f_at_9over10": str(f_at_a),
        "theta_derivative_upper": str(derivative_bound),
        "theta_tail_upper": str(tail),
        "theta_global_lower": "theta(u)>(3/50)*exp(-pi*u/29) for u>=1; use theta(u)=u^(-1/2)theta(1/u) for 0<u<1",
        "normalized_log_derivative_enclosure": lcm.decimal_enclosure(),
        "normalized_100th_root_derivative_enclosure": root.decimal_enclosure(),
        "all_powers_0_lt_r_le_1over60_excluded": True,
        "normalized_64th_root_derivative_enclosure": root64.decimal_enclosure(),
        "power_polynomial_coefficients_k2_to_k39_positive": True,
        "local_order39_obstruction_crossing": [str(root_lo), str(root_hi)],
        "crossing_is_not_claimed_as_global_CM_threshold": True,
        "uniform_scaled_derivative_over_r_upper": I.exact(uniform_upper).decimal_enclosure(),
        "limitations": [
            "Not a Lean proof or independent external review.",
            "Theta modular identity and Gaussian Laplace integral are analytic inputs proved in the note.",
            "No global classification of admissible exponents is claimed."
        ]
    }

if __name__ == "__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
