"""Rebuild the marked residue sets via Legendre, without using divided truncations."""
from math import comb
import json

import sympy as sp


class Field:
    """Encode a+b sqrt(2) by a+p*b; the output serializes [a,b]."""

    def __init__(self, p):
        self.p = p
        self.elts = range(p * p)
        assert pow(2, (p - 1) // 2, p) == p - 1

    def coords(self, x):
        return [x % self.p, x // self.p]

    def elt(self, a, b):
        return a % self.p + self.p * (b % self.p)

    def add(self, x, y):
        a, b = self.coords(x)
        c, d = self.coords(y)
        return self.elt(a + c, b + d)

    def sub(self, x, y):
        a, b = self.coords(x)
        c, d = self.coords(y)
        return self.elt(a - c, b - d)

    def mul(self, x, y):
        a, b = self.coords(x)
        c, d = self.coords(y)
        return self.elt(a * c + 2 * b * d, a * d + b * c)

    def power(self, x, n):
        if n < 0:
            assert x
            n %= self.p**2 - 1
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            n >>= 1
        return out

    def div(self, x, y):
        return self.mul(x, self.power(y, -1))

    def conj(self, x):
        a, b = self.coords(x)
        return self.elt(a, -b)

    def norm(self, x):
        return self.mul(x, self.conj(x))

    def poly(self, x, coefs):
        value = 0
        for a in reversed(coefs):
            value = self.add(self.mul(value, x), a % self.p)
        return value


def jets():
    t, H = sp.symbols("t H")
    s = sp.sqrt(2)
    A = t * (t + 9)**2 / (t + 6)**3
    B = t**2 * (t + 9) / (t + 12)**3
    M = 2 * (t + 6) / (t + 12)
    at = lambda expr: sp.radsimp(expr.subs(t, 6*s)).expand()
    assert at(A) == (2+s)/4 and at(B) == (2-s)/4 and at(M) == s
    assert at(A.diff(t)) == at(B.diff(t)) == (3-2*s)/8
    assert at(M.diff(t)/A.diff(t)) == sp.Rational(4, 3)
    h = (H + 3) / 3
    j = lambda v: 27*v**3*(v**3+8)**3/(v**3-1)**3
    j_marked = (H+3)**3*(H+9)**3*(H**2+27)**3/(H**3*(H**2+9*H+27)**3)
    assert sp.cancel(j(1 + 9/H) - j(h)) == 0
    assert sp.cancel(j(h)-j_marked) == 0
    return {"A' = B'": "(3-2*sqrt(2))/8", "M'/A'": "4/3",
            "same_j_rational_identity": True}


def maier_mod_p(p):
    # After clearing the denominators each side has degree at most p-1.
    n = (p - 1) // 3
    bs = [comb(3*r, r)*comb(2*r, r)*pow(27,-r,p) % p for r in range(n+1)]
    for t in range(p):
        left = right = 0
        for r, b in enumerate(bs):
            scale = b * pow(t+9, r, p)
            left += scale * pow(t*(t+9),r,p) * pow(t+6,3*(n-r),p)
            right += scale * pow(t,2*r,p) * pow(t+12,3*(n-r),p)
        assert (left - right) % p == 0
    return {"degree_at_most": p - 1, "distinct_base_field_tests": p}


def finite(p):
    E = Field(p)
    plus, minus, times, invpow = E.add, E.sub, E.mul, E.power
    n = (p - 1) // 2
    ls = [comb(n, r)**2 % p for r in range(n+1)]
    legendre_roots = [x for x in E.elts if E.poly(x, ls) == 0]
    assert len(legendre_roots) == n
    js = set()
    for x in legendre_roots:
        one_minus = minus(1, x)
        num = times(256 % p, invpow(plus(one_minus, times(x,x)),3))
        js.add(E.div(num, invpow(times(x, one_minus),2)))

    roots = []
    for H in E.elts:
        den_base = times(H, E.poly(H,[27,9,1]))
        if den_base:
            num_base = times(times(plus(H,3),plus(H,9)), E.poly(H,[27,0,1]))
            if invpow(E.div(num_base,den_base),3) in js:
                roots.append(H)
    assert len(roots) == p - 1

    inv4 = pow(4,-1,p)
    xp = E.elt(2*inv4, inv4)
    xm = E.conj(xp)
    omega = next(w for w in range(2,p) if pow(w,3,p) == 1)
    h = next(u for u in E.elts if times(invpow(u,3),xp) == 1)
    mark = lambda v: minus(times(3,v),3)
    anchors = [mark(h),mark(times(omega,h)),mark(E.conj(h))]
    assert all(x in roots for x in anchors)
    A, B, C = anchors
    du, dv = E.coords(minus(B,A))
    eu, ev = E.coords(minus(C,A))
    # Tr((a+b*s)*conj(c+d*s)) = 2ac-4bd.
    r1, s1, r2, s2 = 2*du, -4*dv, 2*eu, -4*ev
    det = pow((r1*s2-r2*s1) % p,-1,p)
    recovered = []
    for H in roots:
        dA,dB,dC = [E.norm(minus(H,S)) for S in anchors]
        y1 = dA-dB-E.norm(A)+E.norm(B)
        y2 = dA-dC-E.norm(A)+E.norm(C)
        recovered.append(E.elt((s2*y1-s1*y2)*det, (r1*y2-r2*y1)*det))
    assert recovered == roots
    reflected_C = plus(A, times(E.div(minus(B,A),E.conj(minus(B,A))), E.conj(minus(C,A))))
    assert reflected_C != C
    assert all(E.norm(minus(S, C)) == E.norm(minus(S, reflected_C)) for S in (A,B))

    m = (p-1)//6
    inv2 = pow(2,-1,p)
    D = sum(r*comb(m,r)*comb(2*m,r)*pow(inv2,r-1,p) for r in range(1,m+1)) % p
    rho = pow(6*D,-1,p)
    rows = []
    for H in recovered:
        u = E.div(plus(H,3),3)
        if not u:
            continue
        x = invpow(u,-3)
        if x not in (xp,xm):
            continue
        deriv = 1
        for other in recovered:
            if H != other:
                deriv = times(deriv, minus(H,other))
        a = invpow(deriv,-1)
        qp = minus(4,times(8,x))
        value = E.div(times(minus(0,qp),times(invpow(u,p-5),a)),6)
        assert value == rho
        assert E.norm(a) == -E.norm(u)*pow(D,-2,p) % p
        rows.append({"H":E.coords(H),"inverse_root_derivative":E.coords(a),
                     "delta":E.norm(a),"norm_h":E.norm(u)})
    assert len(rows) == 6
    return {"p":p, "maier_cleared_polynomial":maier_mod_p(p), "coordinate_model":"a+b*sqrt(2)", "D":D, "rho":rho,
            "supersingular_j": [E.coords(j) for j in sorted(js)],
            "legendre_root_count":len(legendre_roots), "source_H_count":len(roots),
            "reconstructed_H_count":len(recovered), "anchors":[E.coords(x) for x in anchors],
            "two_anchor_reflected_C":E.coords(reflected_C), "six_lifts":rows}


if __name__ == "__main__":
    print(json.dumps({"rational_checks":jets(),"marked_residue_checks":[finite(p) for p in (43,61)]},
                     indent=2, ensure_ascii=False))
