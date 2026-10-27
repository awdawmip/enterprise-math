# D25 / SECOND-DIGIT-LIFT — original weighted-216 fourth-digit sharpness and bounded all-branch falsifier

2026-10-27, Research lane `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR-SIDE / EXACT ALGEBRAIC TAIL LEMMA / EXECUTED FINITE INTEGER CERTIFICATES / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_CHECKPOINT**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Frozen task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific source pin **`c47e13e4aba0e006366f989d6334d443f6333ae3`** (unchanged). Consume accepted D24 UR/JT0 and existing original-model source-port equivalence `Delta_p-R_p = (W_p-p)/p² (mod p)` only on p mod24=13,19. The prior original p³ middle/high-band decompositions are reused, not reasserted as newly proven. Maintenance conversation `chatgpt-hourly-enterprise-math-20260921` has no role here.

## Exact original coefficients and a separate fourth-digit lemma

In the p-local rationals for p>3, write

```
q_n = ((2n)! (3n)!)/((n!)^5 216^n)
w_n = (6n+1) q_n
W_p = sum(n=0,...,p-1) w_n .
```

For **every prime p=6m+1**, define the *previously invisible at precision p³* last band
`T4_p = sum(n=4m+1,...,p-1) w_n`.
Then the following is an exact theorem:

```
T4_p / p³  =
  -2 * sum(n=4m+1,...,p-1)
       (6n+1) (2n-p)! (3n-2p)! / ((n!)^5 216^n)
       (mod p).
```

The left division is in Z_(p) **before** reduction; all displayed factorial and power denominators on the right are units mod p. Thus the formula is meaningful for every such prime, not an inference from the finite checks.

**Proof.** For 4m+1<=n<=p-1, p<=2n<2p and 2p<=3n<3p. Legendre's formula gives `v_p(q_n)=floor(2n/p)+floor(3n/p)=1+2=3`. After removing their literal factors of p, Wilson's theorem yields

```
(2n)!/p = (p-1)! prod(k=1,...,2n-p)(p+k)
           = -(2n-p)! (mod p),
(3n)!/p² = (p-1)! prod(k=1,...,p-1)(p+k)
            * 2 * prod(k=1,...,3n-2p)(2p+k)
             = 2(3n-2p)! (mod p).
```

Multiplication and the original factor `6n+1` prove the displayed formula. The original p³ compression dropping this band remains exact **for the declared second-digit observer**, but is not a fourth-digit compression. No cancellation claim about the full sum follows merely from a tail term.

## Independently computed exact fourth-digit negative witnesses

Direct integer-binomial summation modulo p⁴ and independent factorial-Wilson evaluation of the displayed tail agree:

| prime p | T4_p / p³ mod p | W_p mod p⁴ | (W_p-p)/p³ mod p |
|---:|---:|---:|---:|
| 13 | 5 | 19786 = 13+9*13³ | 9 |
| 19 | 4 | 82327 = 19+12*19³ | 12 |
| 373 | 278 | 11832087049 = 373+228*373³ | 228 |

In particular **W_13 is NOT 13 modulo 13⁴**. The literal p³ LIFT precision is sharp already at the first target prime, and the discarded high tail has nonzero fourth-digit contribution at both target branches, including p=373. This negative witness rules out upgrading the original congruence to p⁴ as an unqualified assertion; it does **not** refute the p³ LIFT and supplies no native H0/B0 output.

## Actually executed, wider third-digit falsification (not a theorem)

An integer-only C++17 checker evaluated the original W_p mod p³ for **every prime 5<=p<=100000** (9590 primes) via

```
q_0=1;
q_(n+1)/q_n = (2n+1)(3n+1)(3n+2)/(36(n+1)^3),
W_p = sum(n=0,...,p-1) (6n+1) q_n.
```

All inverses are of p-adic units n+1<p and 36; modular multiplication uses unsigned 128-bit integers. The separately tested full integer binomial form uses `binom(2n,n)^2 binom(3n,n) 216^(-n)`; finite validation uses neither floating point nor unproven oracle. Checked candidate on all eight odd residue classes:

`W_p ≡ p * (-3/p) (mod p³)`, with Legendre `(-3/p)=+1` when p mod3=1 and `-1` when p mod3=2.

| p mod24 | primes through 100000 | counterexamples | largest tested prime |
|---:|---:|---:|---:|
| 1 | 1181 | 0 | 99961 |
| 5 | 1206 | 0 | 99989 |
| 7 | 1205 | 0 | 99991 |
| 11 | 1203 | 0 | 99971 |
| **13** | **1193** | **0** | **99901** |
| 17 | 1203 | 0 | 99929 |
| **19** | **1205** | **0** | **99907** |
| 23 | 1194 | 0 | 99839 |

The two **frozen D25 target** residue classes comprise **2398 primes, no falsifier**. The additional six classes are **bounded exploratory evidence**, not a modification of the Source Task, accepted theorem, or a claimed all-prime extension. The combined 9590 finite checks cannot prove the congruence beyond 100000.

Executable independent modular-recurrence checker (the same arithmetic and interval as actually run):
`research_notes/portable_direct/d25_weighted216_modp3_all_classes_100k_20261027.cpp`; immutable initial checker commit `a0c7dabc5174e4ff7ef7c2c849c4c551fd94ba14`, blob `8ed72d1ff0bc8a79da39220588dfc45559b8c19f`. Original local run returned 9590 checks and zero failures (execution 13.756 s); the published checker omits only nonessential rolling checksums. The following independent exact-integer spot check was actually executed for p=5,7,11,13,17,19,23,37,43,73,211,373:

```python
from math import comb
for p in (5,7,11,13,17,19,23,37,43,73,211,373):
    modulus=p**4
    i216=pow(216,-1,modulus)
    w=sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(i216,n,modulus)
          for n in range(p)) % modulus
    chi=1 if p%3==1 else -1
    assert (w-chi*p) % (p**3)==0
    if p in (13,19,373):
        assert ((w-p) % modulus)//(p**3)=={13:9,19:12,373:228}[p]
```

## Scope, BRC carrier and next real action

This is a **new precision-boundary certificate for the original sum**, not a recycled p³ middle/high-band identity. BRC observer is the exact signed weighted original sum; retained carrier consists of prime residue branch, integer factorial valuation, actual cutoffs, p³ normalized high-tail residue, character `(-3/p)`, and frozen Source-to-LIFT mapping. Dropping n>4m is lawful at p³, **not** at p⁴; p⁴ negative controls do not migrate to a native H0/B0 Frobenius observer without a proven bridge. No auxiliary two-dimensional model is promoted to the P000 X6 native world.

The actual unresolved benchmark remains **same-original-class native H0/B0** for p=373 with `[X]U mod139129`, native rank, Frobenius direction and eta normalization, signed odd Hesse/Green, original kappa and Delta-R, source/version and independent review. Existing capability support `awdawmip/enterprise-math#1559` was OPEN / PENDING_OWNER / NATIVE_NOT_EXECUTED at this run's GitHub read; no authorized executor identified. No alternative recurrence or finite W certificate counts as that benchmark.

Gateway 0.6.11 reported Site-only, `research_authority_granted=false`, `executor_binding_configured=false`, and exact canonical continuation returned `CONTROL_QUOTA`; own Source CLAIM/open/run is **NOT VERIFIED**. Old research-lane recovery/dispatch Issues `awdawmip/kimi-query-bridge#6575/#6576` remain provenance with no current Source authority; no fresh dispatch/claim was sent. Prior unrelated staging remains independent. **AUTHOR-SIDE / NOT_ADMITTED**, source Researcher registration `REGISTER_PENDING`.

**Exact next action:** find an actually authorized native H0/B0 executor through existing #1559, run the fixed p=373 test, store raw reproducible original-class rank/operator/normalization/observations and validate via an authorized independent path; mathematically pursue a genuine all-target p³ proof or counterexample using the already-proven p³ three-band + original reflected R observer. The p⁴ tail negative witness is complete and need not be repeated. Frozen source pin, ownership, scheduler and notification settings unchanged.
