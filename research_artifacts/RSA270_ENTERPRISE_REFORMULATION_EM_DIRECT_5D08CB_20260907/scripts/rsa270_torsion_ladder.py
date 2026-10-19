"""
RSA-270 research (EM-DIRECT-5D08CB / DIRECT-RSA270):
Torsion-ladder classification of the bivariate Enterprise-layer factor profile.

Setup (from journal 20260906T105500+0800-rsa270-bivariate-factor-profile-qr-barrier-91ad72.md):

  F(Q,u) = sum_{m,n>=1} W_{m+n}(u) Q^(2mn-m-n),   W_s(u) = sum_{j=0}^{s-2} u^(2-s+2j)

For odd N, M=(N-1)/2:
  [Q^M]F(Q,u) = sum_{d|N} W_{(d+N/d+2)/2}(u)
For N=pq (S=p+q):
  P(u) := [Q^M]F(Q,u) = 2 W_{(N+3)/2}(u) + 2 W_{(S+2)/2}(u)      (two-plateau profile)

This script:
  V1: product-side identity check for small N (Ramanujan product vs divisor profile)
  V2: torsion evaluation formula  P(w_m) = 2 g_m(r0) + 2 g_m(r1),
      g_m(r) = (w^(2-r) - w^r)/(1-w^2) = sin(2*pi*(r-1)/m)/sin(2*pi/m) = U_{r-2}(cos(2*pi/m))
      r0 = ((N+3)/2) mod m (N-only),  r1 = ((S+2)/2) mod m (factor-bearing)
  V3: fiber classification of r -> g_m(r) for m=3..48
  V4: u=1 moment ladder (W_s(1)=s-1, W'_s(1)=0, W''_s(1)=(s-2)(s-1)s/3) and u=-1 case
"""
import math, cmath

def W(s):
    return {2 - s + 2*j: 1 for j in range(s - 1)}

def W_eval(s, u):
    return sum(u ** (2 - s + 2*j) for j in range(s - 1))

def profile_poly(N, p, q):
    S = p + q
    P = {}
    for s, mult in [((N + 3)//2, 2), ((S + 2)//2, 2)]:
        for j in range(s - 1):
            e = 2 - s + 2*j
            P[e] = P.get(e, 0) + mult
    return P

def P_eval(P, u):
    return sum(c * (u ** e) for e, c in P.items())

def g_m(m, r):
    """g_m(r) = sin(2*pi*(r-1)/m)/sin(2*pi/m); r any int, reduced mod m internally."""
    th = 2.0 * math.pi / m
    return math.sin(((r - 1) % m) * th) / math.sin(th)

def g_m_direct(m, r):
    """direct ratio form with complex omega (verification only)."""
    w = cmath.exp(2j * math.pi / m)
    r %= m
    return (w ** (2 - r) - w ** r) / (1 - w ** 2)

def product_profile(N, M, umax):
    """Compute [Q^M]F(Q,u) from the Ramanujan product side,
    truncated to |u-exponent| <= umax. Returns dict u_exp -> coeff (float)."""
    cur = {(0, 0): 1.0}
    n = 1
    while 2*n - 1 <= M:
        for b, a, e in [(2*n, 0, 2), (2*n, 2, 1), (2*n, -2, 1),
                        (2*n - 1, 1, -2), (2*n - 1, -1, -2)]:
            # series coefficients of (1 - x)^e for x = u^a Q^b, truncated to Q<=M
            terms = []
            for k in range(0, M // b + 1):
                if e == 2:    ck = (1, -2, 1)[k] if k <= 2 else 0
                elif e == 1:  ck = (1, -1)[k] if k <= 1 else 0
                elif e == -1: ck = 1
                elif e == -2: ck = k + 1
                if ck:
                    terms.append((k*b, k*a, ck))
            nxt = {}
            for (qe, ue), c in cur.items():
                for db, da, ck in terms:
                    key = (qe + db, ue + da)
                    if key[1] > umax or key[1] < -umax:
                        continue
                    nxt[key] = nxt.get(key, 0.0) + c * ck
            cur = nxt
        n += 1
    return {ue: c for (qe, ue), c in cur.items() if qe == M}

def check(cond, msg):
    print(("PASS  " if cond else "FAIL  ") + msg)
    return cond

ok = True

# ---------------- V1: product-side identity, N=35=5*7 ----------------
print("== V1 product-side identity (N=35, p=5, q=7) ==")
N, p, q = 35, 5, 7
M = (N - 1)//2
S = p + q
prod = product_profile(N, M, M)
P = profile_poly(N, p, q)
mism = 0
for e in range(-M, M + 1):
    a = prod.get(e, 0.0)
    b = P.get(e, 0)
    if abs(a - b) > 1e-9:
        mism += 1
        if mism < 5:
            print(f"  mismatch at u^{e}: product={a} profile={b}")
ok &= check(mism == 0, f"product side equals 2W_{(N+3)//2}+2W_{(S+2)//2} coefficient-wise (mismatches={mism})")
# plateau structure
vals = set(P.values()); ok &= check(vals == {2, 4}, f"profile is {{0,2,4}}-valued on support, observed {vals}")
top = max(P.keys()); ok &= check(top == (N - 1)//2, f"outer top exponent = {(N-1)//2}")
inner_top = max(e for e, c in P.items() if c == 4); ok &= check(inner_top == (S - 2)//2, f"plateau boundary (S-2)/2 = {(S-2)//2}")

# ---------------- V2: torsion formula ----------------
print("\n== V2 torsion evaluation formula ==")
for (N, p, q) in [(35, 5, 7), (143, 11, 13), (391, 17, 23), (899, 29, 31), (3599, 59, 61)]:
    S = p + q
    P = profile_poly(N, p, q)
    r0 = ((N + 3)//2)
    r1 = ((S + 2)//2)
    bad = 0
    for m in range(3, 17):
        w = cmath.exp(2j * math.pi / m)
        lhs = P_eval(P, w)
        rhs = 2 * g_m(m, r0) + 2 * g_m(m, r1)
        # also verify direct complex ratio form vs sine form
        d0 = g_m_direct(m, r0); d1 = g_m_direct(m, r1)
        if abs(lhs - rhs) > 1e-9 or abs(d0 - g_m(m, r0)) > 1e-9 or abs(d1 - g_m(m, r1)) > 1e-9:
            bad += 1
    ok &= check(bad == 0, f"N={N}: P(w_m) = 2g_m(r0)+2g_m(r1) and ratio==sine form for m=3..16 (bad={bad})")

# ---------------- V3: fiber classification ----------------
print("\n== V3 fiber classification r -> g_m(r) = U_{r-2}(cos(2pi/m)) ==")
fibers_ok = True
for m in range(3, 49):
    vals = [g_m(m, r) for r in range(m)]
    def key(x): return round(x, 9)
    groups = {}
    for r, v in enumerate(vals):
        groups.setdefault(key(v), []).append(r)
    if m % 2 == 1:
        pred = "singletons" if all(len(g) == 1 for g in groups.values()) else "NON-singletons"
        if pred != "singletons":
            fibers_ok = False
            print(f"  m={m} ODD: unexpected fibers {[g for g in groups.values() if len(g)>1]}")
    else:
        pred_ok = all(sorted(g) == sorted([r % m for r in (r0_, m//2 + 2 - r0_)]) or len(g) == 1
                      for g in groups.values() for r0_ in [g[0]])
        if not pred_ok:
            fibers_ok = False
            print(f"  m={m} EVEN: unexpected fibers {groups}")
ok &= check(fibers_ok, "odd m: all fibers singletons; even m: fibers are {r, m/2+2-r} pairs/singletons (m=3..48)")

# ---------------- V4: moment ladder ----------------
print("\n== V4 moment ladder at u=1 and u=-1 ==")
mom_ok = True
for s in range(2, 31):
    w1 = W_eval(s, 1.0) if s >= 2 else 0
    if s == 1:
        w1 = 0  # W_1(u) = empty sum = 0; support empty; handle separately
    if abs(W_eval(s, 1.0) - (s - 1)) > 1e-9: mom_ok = False
    d1 = sum((2 - s + 2*j) for j in range(s - 1))
    if abs(d1) > 1e-9: mom_ok = False
    d2 = sum((2 - s + 2*j)**2 for j in range(s - 1))
    pred = (s - 2)*(s - 1)*s / 3.0
    if abs(d2 - pred) > 1e-9: mom_ok = False
    # u=-1 limit value (s-1)(-1)^s
    if abs(W_eval(s, -1.0) - (s - 1)*((-1)**s)) > 1e-9: mom_ok = False
ok &= check(mom_ok, "W_s(1)=s-1, W'_s(1)=0, W''_s(1)=(s-2)(s-1)s/3, W_s(-1)=(s-1)(-1)^s for s=2..30")

print("\n" + ("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED"))
