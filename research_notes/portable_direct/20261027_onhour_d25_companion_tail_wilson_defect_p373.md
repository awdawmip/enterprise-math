# D25 / SECOND-DIGIT-LIFT — exact p³ companion-tail defect and Wilson finite-field certificate

**Status:** AUTHOR-SIDE / PROVED EXACT TAIL REDUCTION / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.  
**Date:** 2026-10-27. **Logical Research lane:** `chatgpt-research-onhour-enterprise-math-20260923`.  
**Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.  
**Publication:** `TP2-B6F4FC938FF94941C1B7`.  
**Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

## Scope and consumed inputs

For primes `p ≡ 13 or 19 (mod 24)` write `p=6m+1` and take the full original weighted coefficients

```
w_n = (6n+1) (2n)! (3n)! / ((n!)^5 216^n),
W_p = sum(n=0..p-1) w_n.
s_n = (8n+1) (4n)! / ((n!)^4 2304^n),
S_p = sum(n=0..p-1) s_n.
```

All coefficients lie in `Z_(p)`. The previously consumed **exact original interface** is `Delta_p-R_p ≡ (W_p-p)/p² (mod p)`; accepted UR/JT0 already proves `W_p ≡ p (mod p²)` for the target classes. Guo–Zudilin, *A q-microscope for supercongruences*, arXiv:1803.01830, proves `S_p ≡ p (-3/p) = p (mod p³)` in these classes. The existing author note `20261027_onhour_d25_guo_zudilin_companion_bridge_precision_gate.md`, commit `e23883a9c09f92480d3fa52b635e6793497a9dbc`, already established the equivalence `LIFT iff W_p-S_p ≡ 0 (mod p³)`. This note DOES NOT take credit for that prior result, its 15-prime regression, or the existing four-band valuation of `w_n`.

## New theorem: the unmatched companion tail has a nonzero, exactly computable p² digit

Define `q = floor((3p-1)/4) = 4m + floor((m+1)/2)`. For every prime in the specified target classes,

```
(A)  W_p - S_p ≡ sum(n=0..4m) (w_n-s_n) - p² E_p  (mod p³),

(B)  E_p ≡ 2 sum(n=4m+1..q)
                (8n+1)(4n-2p)! / ((n!)^4 2304^n)     (mod p).
```

The gap contains exactly `floor((m+1)/2)` terms, each of exact p-adic valuation **2** in `s_n`, and `w_n ≡ 0 (mod p³)` for all `n>4m`. Thus the gap must NOT be discarded when transferring the proven companion theorem to the original weighted sum. The expression (B) involves only the finite field `F_p`, ordinary factorials with argument <p, and unit inverses. In particular, *no native H0/B0 computation is implied*.

**Proof.** Since `n<p` and `p≥13`, Legendre's factorial valuation gives exactly

```
v_p(w_n)=floor(2n/p)+floor(3n/p)+1_{n=m},
v_p(s_n)=floor(4n/p)+1_{n=n_star}.
```

The first indicator follows from the unique solution of `p | 6n+1`, namely `n=m`; `6n+1<p²`. The second follows from `8n+1<p²`: for `p≡13 (mod24)`, `n_star=(5p-1)/8`, and for `p≡19 (mod24)`, `n_star=(3p-1)/8`. They contribute an extra valuation **in different bands**: the former changes `v_p(s_n):2→3`, the latter `1→2`. Neither special index lies in `(4m,q]`. This retains the signed-weight observer and its residue-class provenance, rather than quotienting to the unweighted factorial ratio.

For `n≥4m+1`, one has `floor(2n/p)≥1` and `floor(3n/p)≥2`, hence `w_n=0 (mod p³)`; for `n≥q+1`, one has `floor(4n/p)≥3`, hence `s_n=0 (mod p³)`. For `4m<n≤q`, `2p<4n<3p`, so `floor(4n/p)=2` and the weight is a unit: `v_p(s_n)=2`.

To evaluate the exact divided digit, set `a=4n-2p`, so `0≤a<p`. Removing the two p-divisible factors in `(4n)!` gives

```
(4n)!/p² = 2 * product(j=1..4n, j ≠ p,2p) j
         ≡ 2*((p-1)!)² * a!
         ≡ 2*a!                             (mod p)
```

by Wilson's theorem. Dividing only by the p-units `(n!)^4 2304^n` proves (B). Splitting both original full sums into retained, unmatched-gap and vanished ranges proves (A). There is no numerical premise in this proof.

Since accepted first-digit UR and the published companion theorem imply `W_p-S_p ≡ 0 (mod p²)`, the shared-prefix sum is also divisible by `p²`. Therefore an **exact observer-preserving remaining bridge condition** is

```
  [ p^(-2) sum(n=0..4m) (w_n-s_n) ] mod p = E_p in F_p.
```

This locates an explicit p² correction that a common-cutoff or term-by-term matching proof would otherwise lose. It reduces the tail to prime-field arithmetic, **not the whole p³ shared-prefix challenge**. The all-target bridge is NOT proved and this is not claimed to meet the task's terminal strict-smaller-certificate criterion.

## Exact native-target p=373 discriminator

For `p=373`, `m=62`, `4m=248`, `q=279`, and the 31 unmatched terms are `n=249,...,279`. The Wilson finite-field sum yields

```
E_373 = 281 in F_373,
p² E_373 = 281*139129 = 39095249 (mod 373³=51895117).
```

Independently computing the full exact binomial coefficients modulo `373³` gives

```
sum(n=249..279) s_n ≡ 39095249 (mod 51895117),
sum(n=0..248) (w_n-s_n) ≡ 39095249 (mod 51895117).
```

Their difference is zero modulo `373³`; this checks the known finite `W_373-S_373` example, **not a universal bridge proof**. The first displayed nonzero residue proves that simply truncating *both* models at `n=248` is a mathematically invalid strategy. The special `s_n` weighted zero lies at `n_star=233` (valuation 3), and the original `w_n` weighted special term lies at `n=m=62` (valuation 1); neither can be silently dropped from the shared-prefix observer.

Second residue-class check: `p=19,m=3,4m=12,q=14,n_star=7` has `E_19=16`, `sum(n=13..14)s_n ≡ 16*19²=5776 (mod 6859)`. Here `n_star` raises `s_7` from valuation 1 to 2. Both modulo-24 branches are explicitly preserved.

## Reproducible precise integer checker (executed in this turn)

The first path evaluates the exact binomial coefficients modulo p³; the second uses Wilson's finite-field expression for the unmatched tail. No floats, approximations or remote computation. It tests only the listed eight primes; the theorem above is symbolic.

```python
from math import comb

def check(p):
    assert p>=13 and p%24 in (13,19)
    m=(p-1)//6
    q=(3*p-1)//4
    mod=p**3
    F=[1]*p
    for n in range(1,p):
        F[n]=F[n-1]*n%p
    direct_gap=shared=0
    for k in range(p):
        w=((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod))%mod
        s=((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,mod))%mod
        if k<=4*m:
            shared=(shared+w-s)%mod
        if 4*m<k<=q:
            assert w==0
            assert s%p**2==0
            direct_gap=(direct_gap+s)%mod
        if k>q:
            assert s==0
        if k>4*m:
            assert w==0
    wilson_gap=0
    for k in range(4*m+1,q+1):
        a=4*k-2*p
        t=2*(8*k+1)*F[a]*pow(F[k],-4,p)*pow(2304,-k,p)%p
        wilson_gap=(wilson_gap+t)%p
    assert direct_gap==p**2*wilson_gap
    # Only an empirical check of the unresolved entire bridge:
    assert shared==direct_gap
    return p,m,4*m,q,q-4*m,wilson_gap,shared

primes=[13,19,37,43,61,67,211,373]
rows=[check(p) for p in primes]
assert rows[0]==(13,2,8,9,1,6,1014)
assert rows[1]==(19,3,12,14,2,16,5776)
assert rows[-1]==(373,62,248,279,31,281,39095249)
print(rows)
```

Observed tuple sequence (p,m,4m,q,gap_count,E_p,shared_mod_p3):

```
(13,2,8,9,1,6,1014)
(19,3,12,14,2,16,5776)
(37,6,24,27,3,17,23273)
(43,7,28,32,4,28,51772)
(61,10,40,45,5,13,48373)
(67,11,44,50,6,49,219961)
(211,35,140,158,18,83,3695243)
(373,62,248,279,31,281,39095249)
```

## Scientific / authority continuation

**Mother:** D25 LIFT/JT2 after accepted D24 UR/JT0. **New author-only frontier:** proved exact (A)–(B), isolated the nonvanishing p² companion gap (31 terms at 373), and executed two algorithmically different exact finite arithmetic checks. **Do not repeat:** accepted UR, the preexisting W four-band valuation, the 815-prime W regression, the Guo–Zudilin companion evaluation, the earlier 15-prime bridge and p⁴ neg-control, previous E3 author-side CM/isogeny notes.

**Highest missing required evidence:** truly same-original-class fixed **H0/B0 divided-power** representative, `[X]U mod 139129`, native module rank, semilinear Frobenius direction and normalization `eta`, signed Green/Hesse original observer and same-definition `kappa`; native run `NOT_EXECUTED / PENDING_OWNER`, authoritative support intake [#1559](https://github.com/awdawmip/enterprise-math/issues/1559). Do not promote this modular-tail certificate into a native experiment or a Source Result.

**Next exact action:** authorized owner locates/runs the genuine native evaluator and publishes raw implementation/inputs/operator data for independent validation. If a canonical research authorization becomes available, consume the exact current Source continuation before any claim/run, then use this Wilson correction only for any specifically authorized *portable* proof of the entire bridge. Native experiment cannot be replaced by a finite scan, unrelated auxiliary claim or this lemma.

**Control request provenance:** same Research logical conversation; fresh read-only recovery request `research-onhour-20261027-0501-recovery-r13`, [bridge issue #6575](https://github.com/awdawmip/kimi-query-bridge/issues/6575), shows local ACTIVE session `MCP-de3e5bafb24f43f4a5e6285e7601676a` with `source_authority_verified=false`, prior_contribution_ids not inherited and no local claim/open. Own recovery-directed canonical dispatch `research-onhour-20261027-0507-dispatch-r13`, [#6576](https://github.com/awdawmip/kimi-query-bridge/issues/6576), ended `FAILED / TimeoutExpired` (no new task ownership). Original failed registration repair [#1539](https://github.com/awdawmip/enterprise-math/issues/1539) remains an actual control-maintenance support boundary. Old neutral staging `SD-d7c23e7984c2ddaac60a` remains independent and not accepted Result evidence. Source-native session/claim/run for this lane: **no currently verified authorized writer / winning claim / open run**.

**Submission classification:** AUTHOR-SIDE, UNREVIEWED, NOT_ADMITTED, REGISTER_PENDING, SYNC_DEBT. No Source-native checkpoint, freeze, review, Result, native mathematical experiment, or activity-registration success is asserted. No scheduler, notification, head-control authority, P000 or frozen scientific source pin was changed.
