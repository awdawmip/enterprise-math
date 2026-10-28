# D25 / SECOND-DIGIT-LIFT — exact CM(-24) Gauss pullback and eight-class p² precision

2026-10-29 Asia/Hong_Kong. **AUTHOR-SIDE / EXACT ALGEBRA + PROVED FINITE CUTOFF + EXECUTED INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED**. No native Source session, claim, run, checkpoint or Result is asserted.

Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923`; no maintenance-lane identity borrowed. Previous exact frontier: `research_notes/portable_direct/20261029_onhour_d25_b2304_two_branch_jet_and_carry.md`.

## Problem and exact natural cutoff theorem

Original B2304 companion: `β_n=(1/8)_n (3/8)_n/(n!)²`, `K_b(z)=Σ_{n=0}^b β_n z^n`. The unresolved conditional **Root2** claim is `K_b(1/9)≡0 (mod p²)` for all `p≡13 (mod24)`, with `b=(7p−3)/8`. Previous author-side work checked 83 target primes, but did not prove Root2.

For **every prime p>3** define two distinct numerator-hit indices `r_1=min{0≤r<p : p|8r+1}`, `r_3=min{0≤r<p : p|8r+3}`, `b=max(r_1,r_3)`. Direct modular arithmetic gives:

| p mod 8 | r1 | r3 | b |
|---|---|---|---|
| 1 | (p−1)/8 | (3p−3)/8 | (3p−3)/8 |
| 3 | (3p−1)/8 | (p−3)/8 | (3p−1)/8 |
| 5 | (5p−1)/8 | (7p−3)/8 | (7p−3)/8 |
| 7 | (7p−1)/8 | (5p−3)/8 | (7p−1)/8 |

Since n! is a p-unit for n<p and each numerator-hit belongs to the product precisely when n>r, the exact valuation satisfies `v_p(β_n)≥1_{n>r_1}+1_{n>r_3}`, with equality for all primes p≥7 and all 0≤n<p. At p=5, n=4, the factor 8·3+1=25=p² gives the **exception** v_p(β_4)=2 rather than 1. For n>b, both hits have occurred, so **v_p(β_n)≥2** for all 0≤n<p. This proves the **coefficientwise polynomial congruence**, for all primes p>3:

```text
Σ_{n=0}^{p−1} β_n z^n  ≡  K_b(z)   (mod p²)   in Z_(p)[z].
```

This all-four-mod8-class natural cutoff is new as a combined scoped derivation; the b values for classes 3,5 were used in prior D25. It **cannot** delete n>b terms modulo p³ or extend the identity to the entire infinite series.

## Analytic modular CM(-24) identification (exact, NOT finite p-adic transport)

Classical DLMF 15.8.18 quadratic transformation, with the branch analytic at t=0:

```text
₂F₁(1/8,3/8;1;4t(1−t)) = ₂F₁(1/4,3/4;1;t).
```

At original z=1/9, `36t²−36t+1=0`, `t_±=(3±2√2)/6`. The standard signature-four modular parameter is

```text
J(t)=64(1+3t)³ / (t(1−t)²).
```

**Exact integer polynomial identity**, checked symbolically using only integer-array arithmetic:

```text
64(1+3t)³ − (5121792 t−143424)t(1−t)²
  = −64(36t²−36t+1)(2223t²−2286t−1).
```

Consequently `J(t_±)=2417472±1707264√2`, with minimal polynomial

```text
H_{−24}(X)=X²−4834944X+14670139392.
```

This matches the classical Hilbert class polynomial of discriminant −24, corresponding to Q(√−6). Independent mathematical references: DLMF https://dlmf.nist.gov/15.8.E18 ; signature-four J-invariant formula https://en.wikipedia.org/wiki/J-invariant#Inverse_function ; standard Hilbert class polynomial definitions https://magma.maths.usyd.edu.au/magma/handbook/text/1660 ; D=−24 polynomial table https://numberdb.org/Hilbert_class_polynomials . The modular formula itself is **prior mathematics**; only this explicitly checked arithmetic specialization and its relationship to the present finite Root2 frontier are being recorded. No CM Frobenius, p-adic period-normalization, native H0/B0 class or finite Root2 statement follows merely from this complex-analytic identity.

Quadratic reciprocity: `(−6/p)=+1` for p≡1,5,7,11 (mod24), `(−6/p)=−1` for p≡13,17,19,23. Field inertness alone is **not** the observed Root2 threshold.

## Executed 667-prime exact-integer classification

Reproducible executed checker: `research_notes/portable_direct/d25_cm24_gauss_fourclass_guard_20261029.py`. It uses `x_0=1`, `x_{n+1}=x_n(8n+1)(8n+3)/(576(n+1)²)` in Z/p², accumulates K_b(1/9), independently cross-checks a factorial-product computation on selected primes, verifies the exact CM polynomial identity, tests n-level valuations for every prime p<100, and probes p³ precision on selected roots. No floating-point math; no native H0/B0 evaluator.

**All 667 primes 5≤p<5000 pass these finite observations**:

| p mod24 | number | observed v_p(K_b) | (-6/p) |
|---:|---:|---|---|
| 1 | 76 | 0 (unit) | +1 |
| 5 | 85 | 0 (unit) | +1 |
| 7 | 88 | 0 (unit) | +1 |
| 11 | 84 | 0 (unit) | +1 |
| **13** | **83** | **≥2** | −1 |
| 17 | 85 | 1 | −1 |
| **19** | **83** | **1** | −1 |
| **23** | **83** | **≥2** | −1 |

`≥2` is only a lower bound modulo p². Sharp third-digit examples are `K_37 ≡ 42439 = 31·37² (mod37³)`, `K_23 ≡6877=13·23² (mod23³)`; `K_13≡0 (mod13³)` is an exceptional extra-valuation sample. The checker identified the only extra numerator-factor valuation for small primes as `(p,n,baseline,actual)=(5,4,1,2)`. Terminal result: `PASS_D25_CM24_PULLBACK_EIGHT_CLASS_P2 667 primes`. Both Root2 for all p≡13 and a possible p≡23 extension remain **CONJECTURAL**, not proved.

**Falsified shortcut:** `(−6/p)=−1 ⇒ v_p(K_b)≥2` is false, e.g. p=17 and p=19 have valuation **exactly 1**, consistent with the earlier p≡19 companion-jet condition. Retain the mod8 branch/period twist rather than collapsing all four inert classes to one Boolean character. This is a concrete BRC observer-information-loss witness.

## Provenance, BRC type and exact successor

BRC resolution **COMPOSE_APPLIED**, scoped to valuation/source-carry discipline: carrier `(p,n,β_n,r1,r3,degree,ordered_numerator_hits,v_p,original_truncation)`; readout `K_b(1/9) modp²` **only after** explicit cutoff and evaluation. The table is an observer projection, not a source-equivalent rewrite for p³ derivatives/Green/Hesse/other operations. P000 / ACTIVE discrete six-axis worldview / three-dimensional slice and older frozen science pin are untouched. Analytic modular Q(√−6) is external typed mathematical auxiliary, not automatic native geometric transfer.

**Next minimal mathematical proof obligation:** construct a **finite p-adic quadratic pullback with explicit modulo-p² truncation and period normalization defect** at z=1/9, and use discriminant−24 CM to explain why the p≡13 branch gets a second p factor **without** predicting that same factor for p≡17,19. The p≡23 pattern is a distinct conjectural extension. Then return to the original A216/B2304 full mod-p³ cross-kernel cancellation with all signed high-degree source contributions, and to the frozen Δ_p−R_p witness; do not rerun completed Clausen/373 scalar theory as new results.

**Native outstanding benchmark (independent):** GitHub Issue #1559 https://github.com/awdawmip/enterprise-math/issues/1559 remains OPEN/PENDING_OWNER/NATIVE_NOT_EXECUTED, fresh read on 2026-10-29. A lawful actual native executor must compute original fixed p=373 H0/B0 divided-power `[X]U mod139129`, original module rank, actual semilinear Frobenius direction and η, full signed odd Hesse/Green, κ and Δ_p−R_p with independent reproducible receipt. No scalar CM/supercongruence work substitutes for this.

**Control recovery:** present Site subject has `research_authority_granted=false`, `executor_binding_configured=false`, active jobs 5/5. Read-only gateway `em_checkpoint_get` for research ID returned `ACCESS_DENIED`; exact old request IDs `research-onhour-20261027-0501-recovery-r13` and `research-onhour-20261027-0507-dispatch-r13` both returned `CONTROL_REQUEST_NOT_FOUND` to this Site. No own service recovery_status action exposed. Do not reissue, do not infer no task, and do not borrow another session/claim. Next authorized operator needs Site-bound Researcher permission/real-own original receipt/continuation read and original winning claim verification before native writes. These GitHub materials are **only author-side durable evidence, NOT a canonical Source checkpoint, formal Result or independent acceptance**. Existing research automation stays enabled and unchanged.
