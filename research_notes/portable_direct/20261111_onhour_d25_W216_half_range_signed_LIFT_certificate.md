# D25/JT2 — original W216 LIFT reduced to an exact signed half-range certificate

Date: 2026-11-11 (Asia/Hong_Kong). Scope: Enterprise Math TASK_RESEARCH, author-side mathematics, **UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN**. Logical Research lane declaration: `chatgpt-research-onhour-enterprise-math-20260923`; this file does not attest platform identity, recover any previous session capability, or exercise a native CLAIM. Maintenance conversation `chatgpt-hourly-enterprise-math-20260921` was not used.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **Frozen science:** `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Consume the accepted first-digit UR/JT0 and already-derived exact original source-port relation
[
\Delta_p-R_p\equiv (W_p-p)/p^2\pmod p.
]
The real fixed H0/B0 `[X]U mod 139129` experiment remains unexecuted and tracked in Issue #1559, with no confirmed owner at this research read.

## 1. Exact half-range theorem (all primes p=6m+1>3)

Put, in the p-local rationals,
[
a_k=\binom{2k}{k}^{2}\binom{3k}{k}\,216^{-k}
   =\frac{(2k)!(3k)!}{216^k(k!)^5},\qquad
W_p=\sum_{k=0}^{p-1}(6k+1)a_k.
]
Define **the first-half original signed observer**
[
S_p=\sum_{k=0}^{3m}(6k+1)a_k,
]
and, only for `2m+1 <= k <= 3m`, define the original valuation-one unit
[
u_k=\frac{a_k}{p}\bmod p\in\mathbf F_p^\times,qquad
J_p=\sum_{k=2m+1}^{3m}\frac{1-6k}{36k^3u_k}\in\mathbf F_p.
]
All denominators in `J_p` are p-units. Then **unconditionally for every prime p=6m+1>3**,
[
\boxed{ W_p\equiv S_p+p^2J_p\pmod{p^3}. }\tag{H}
]
The unit can be obtained without forming a high-band coefficient:
[
\boxed{u_k\equiv -\frac{(2k)!(3k-p)!}{216^k(k!)^5}\pmod p,
\quad 2m<k\le3m.}\tag{U}
]

For the frozen target residue classes `p mod 24 in {13,19}`, the accepted first-digit theorem `W_p=p mod p^2` implies `S_p=p mod p^2`. Therefore
[
L_p=\frac{S_p-p}{p^2}\bmod p
]
is p-integral, and the **original frozen LIFT is exactly equivalent** to the signed half-range equation
[
\boxed{\Delta_p-R_p\equiv L_p+J_p\pmod p;
\qquad \mathrm{LIFT}\iff L_p+J_p=0\text{ in }\mathbf F_p.}\tag{HL}
]
This replaces the length-`p` weighted hypergeometric truncation by the first `3m+1=(p+1)/2` original coefficients and one explicit inverse-unit correction over only `m=(p-1)/6` indices. It is a **shorter exact finite certificate in source-index coverage**, with no claim of asymptotic bit-complexity improvement. Both separately nonzero signed ports `L_p` and `J_p` remain observable.

## 2. Full proof: factorial complements, valuations, and original signs

For `0 <= k < p`, by Legendre's formula and the fact that `k!` and `216` are p-units,
[
v_p(a_k)=\lfloor 2k/p\rfloor+\lfloor 3k/p\rfloor.
]
When `p=6m+1`, this is 0 on `0..2m`, 1 on `2m+1..3m`, 2 on `3m+1..4m`, and 3 on `4m+1..6m` (including every endpoint). Pair each `k=1..3m` with the distinct `p-k=3m+1..6m`. The pair for `k<=2m` has high-band valuation 3 and contributes zero mod `p^3`.

For `2m<k<=3m`, the two paired coefficients have valuations 1 and 2 respectively. Let `r=3k-p` (`1<=r<p`). Wilson's congruence and the factorial complement identity
[
t!(p-t)!\equiv(-1)^t t\pmod p \quad(1\le t<p)
]
give
[
\frac{(2k)!(2p-2k)!}{p}\equiv-2k,\quad
\frac{(3k)!(3p-3k)!}{p^2}\equiv(-1)^r r,\quad
k!(p-k)!\equiv(-1)^k k\pmod p.
]
Because `r-k=2k-p` is odd and `216^p=216 mod p`, these imply the **source-labeled reflected product**
[
\boxed{\frac{a_ka_{p-k}}{p^3}
\equiv\frac{1}{36k^3}\pmod p.}\tag{P}
]
This derivation uses the actual signed factorial coefficients; no external unreviewed second-digit reflection theorem is needed. Since `u_k=a_k/p` is a unit, (P) yields
[
a_{p-k}\equiv\frac{p^2}{36k^3u_k}\pmod{p^3}.
]
The reflected original weight `6(p-k)+1` becomes `1-6k` modulo `p` because the coefficient starts at valuation two. Summing all disjoint pairs proves (H). For (U), `(3k)!/p\equiv-(3k-p)! mod p`, proving the stripped-unit formula. Combining (H) with the frozen original source-port identity and the accepted first-digit `W_p=p mod p^2` proves (HL), including legality of both divisions by `p^2`.

**BRC/observer audit.** Population: `k=0,...,p-1`, original signed weights and factorial coefficients. Pair operation: involution `k -> p-k` retaining both labels. Valuation carrier: `v=0,1,2,3`; retained low `a_k mod p^3` and inverse unit `u_k` on the reflection-sensitive middle band. Horizon: only the frozen `(W_p-p)/p^2 mod p` observer. The discarded high valuation-three band vanishes at that precision; the valuation-two band is **reconstructed with signs**, not declared redundant. This exact quotient does not change the native H0/B0 class, CM source, Frobenius operator, or `\kappa` port.

## 3. Reproducible deterministic test, two coefficient constructions

The following Python 3 standard-library checker computes the **full** sum by the independent hypergeometric recurrence, and the half-range by original integer binomials plus the independent Wilson-stripped unit formula. It checks each coefficient by both paths and then checks (H) and (HL). The latter equality is tested numerically only, not treated as a universal proof of vanishing.

```python
from math import comb, factorial, isqrt

def primes_upto(n):
    return [p for p in range(13, n + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]

def check(p):
    assert p > 3 and p % 6 == 1
    m, mod = (p - 1) // 6, p**3
    inv216 = pow(216, -1, mod)
    # Full recurrence: a_(k+1)/a_k = (2k+1)(3k+1)(3k+2)/[36(k+1)^3].
    a, W = 1, 0
    for k in range(p):
        exact = comb(2*k,k)**2 * comb(3*k,k) * pow(inv216,k,mod) % mod
        assert a == exact, (p,k)
        W = (W + (6*k+1)*a) % mod
        if k < p-1:
            a = (a*(2*k+1)*(3*k+1)*(3*k+2) *
                 pow(36*(k+1)**3, -1, mod)) % mod
    S, J = 1, 0
    for k in range(1,3*m+1):
        ak = comb(2*k,k)**2 * comb(3*k,k) * pow(inv216,k,mod) % mod
        S = (S + (6*k+1)*ak) % mod
        if k>2*m:
            u = (-factorial(2*k)*factorial(3*k-p) *
                 pow(216,-k,p)*pow(factorial(k),-5,p)) % p
            assert u != 0 and u == (ak // p) % p, (p,k)
            J = (J + (1-6*k)*pow(36*k**3*u,-1,p)) % p
    assert W == (S+p*p*J)%mod, (p,W,S,J)
    if p%24 in (13,19):
        assert (S-p)%(p*p)==0, (p,S)
        L = ((S-p)%mod)//(p*p)
        assert (W-p)//(p*p) == (L+J)%p if W>=p else ((W-p)%mod)//(p*p) == (L+J)%p
        return p,L,J,((W-p)%mod)//(p*p)
    return p

results=[check(p) for p in primes_upto(499) if p%24 in (13,19)]
assert len(results)==23
assert all((L+J)%p==0 and defect==0 for p,L,J,defect in results)
for p,L,J,_ in results:
    if p in (13,19,109,139,373,499):
        print(p,L,J)
```

Exact run: **23 target primes** `p<=499`, independent factorial and recurrence checks passed for every `k<p`; 23 half-range identities and original LIFT residual checks passed. Representative `(p,L_p,J_p)`:
```
(13,3,10)
(19,10,9)
(109,93,16)
(139,126,13)
(373,107,266)
(499,190,309)
```
For `p=373`, the low source sum is `S=14887176 mod 373^3`, the corrected high-band contribution is `373^2*266=37008314 mod 373^3`, and their sum is `373 mod 373^3`. Both `L_373=107` and `J_373=266` are nonzero.

## 4. Status, native evidence, and next exact action

**Author proof status:** (H), (U) and the conditional (HL) follow algebraically for their stated domains; the 23-prime run is exact finite supporting evidence. They constitute a source-index-shorter strict equivalent certificate of original LIFT, not an all-prime proof that `L_p+J_p=0`. A separate independent research/Driver review and Source admission have not occurred.

**Highest-priority native evidence:** Issue #1559 remains `NATIVE_H0_B0_NOT_RUN / PENDING_OWNER`. The required original-class `[X]U mod 139129` at `p=373`, true module rank, actual Frobenius semilinear direction, eta normalization, nonzero signed odd Hesse/Green observer, `\kappa`, original `\Delta_p-R_p`, and independent validation are all still missing. The nonnative Hesse norm candidate `122102 mod 139129` stays conditional on native rank-one and correct coefficient identification.

**Next mathematics:** search an exact terminating finite-field/adjoint identity directly for the now short, **signed** scalar `L_p+J_p`, preserving both target classes; classify it as proved/false/unresolved, not by additional undirected prime scanning. **Next native action:** authorized exact original H0/B0 evaluator executes the frozen experiment under #1559 and publishes reproducible raw operator/certificate through its own legitimate Researcher lane. Do not substitute (H) for the native benchmark.

**Control provenance:** Former read request `onhour11-20261110-2355-exact-read` had Source SUCCEEDED, snapshot `4dc28da53c6036c80a4098a3b6cd12d92e1d8a69`. A fresh exact read `onhour11-20261111-0102-source-cont` initially returned QUEUED and requires **receipt/reconcile on the same request_id**; neither receipt grants execution authority. Local `recovery_status` with historical `MCP-5378d3819d8947bda9049c9428493e2d` returned `SESSION_CAPABILITY_REQUIRED`. No owned active CLAIM/open run has been authenticated in this turn. This artifact is **AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED**, not a native checkpoint/Result, and its immutable Git commit must be established by publication/readback before Source inclusion.
