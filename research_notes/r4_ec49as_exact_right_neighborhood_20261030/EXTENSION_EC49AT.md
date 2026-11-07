# EC49AT — a purchase-aware BRC dual extends exact optimality through η=9/25

2026-10-30. Author-side mathematical proof; exact Python Fraction endpoint certificate executed. Status: AUTHOR_PROVED / EXACT_CERT_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. This extension strengthens EC49AS PROOF.md while preserving its earlier bound and its upper-envelope obstruction as originally stated.

## Exact all-real theorem

Keep precisely the positive auxiliary 18+18-leaf observer of EC49AQ–EC49AS, causal hidden-w erasure, actions c=(A0,A1,B0,B1,STOP), first cost C1=43/48, expected sensor cost C2=13/16, information t(w,u)=1/2+(2u−1)(1−w)η, and H=α−(177/172)β. Arbitrary real first-stage x[w,c], independent conditional purchase coins r(c,u) and lawful terminal accept probabilities are allowed.

For **every real η in [175/674,9/25]**, the exact full causal optimum is

    Hmax(η)=77/688+(674η−175)/16512.

Together with EC49AQ/AR, this supplies the exact optimum for every real 0≤η≤9/25:

    Hmax(η) = 77/688                            if 0≤η≤175/674,
              77/688+(674η−175)/16512          if 175/674≤η≤9/25.

At η=9/25, Hmax=47891/412800, with the same legal first-stage witness and observer acceptance: (α,β)=(103/240,2191/7200).

## New purchase-aware dual

For each purchased observer fiber (c,u), c<4, define

    q_z(c,u)=x[z,c]t(z,u)/3,
    T(c,u)=Σ_z q_z(c,u),
    Vη(c,u)=Σ_z[43q_z(c,u)−16T(c,u)]_+/172.

V is the optimal expected support for buying z on this fiber; unpurchased and STOP fibers optimally contribute zero because their P and Q observation masses agree. For any legal strategy, H≤Σ r(c,u)Vη(c,u), with exact resource C2=Σ r(c,u)T(c,u), and 0≤r(c,u)≤1. Therefore, for **every fixed λ≥0**,

    H≤λ C2+Σ_{c,u}[Vη(c,u)−λ T(c,u)]_+ =: Gλ,η(x).

The inequality is exact pointwise because r d≤[d]_+ for 0≤r≤1, even if d is negative. It explicitly enforces the purchase-resource price rather than pretending every high-mass vertex can buy on all paid fibers.

All legal first stages satisfy the same η-independent cut polytope Π from EC49AS: x≥0; 3 row sums; first cost Σ cost(c)x[w,c]=43/16; and paid mass c(x)≥13/16. It has exactly 168 vertices (24 original high and 144 paid-cut vertices) by the complete rational support enumeration in VERIFY.py.

For fixed λ and η, V is a sum of positive parts of affine functions of x and T is affine in x. Hence Gλ,η is convex in x. For fixed x, each purchased-leaf score is affine in η; V is convex in η, T affine in η, and [V−λ T]_+ convex in η. Thus Uλ(η)=max_{x∈Π}Gλ,η(x) is convex in η; the finite vertex maximum is exact for all real x.

Choose the **single rational dual multiplier λ=3/50** for the entire interval. The actual exhaustive Fraction endpoint certificate is:

| η | max G over 24 high vertices | max G over 144 paid-cut vertices | Uλ(η) |
|---|---|---|---|
| 175/674 | 6863/67400 (0 upper-bound ties) | 77/688 (24 ties) | 77/688 |
| 9/25 | 371/3200 (0 upper-bound ties) | 47891/412800 (8 ties) | 47891/412800 |

The affine lawful witness from EC49AR/AS matches the upper envelope at both endpoints. Since Uλ(η) is convex, its graph on the full real parameter interval is at most the chord joining these endpoint values. The witness yields that chord for every η, proving equality throughout. The complete finite certificate covers 1365+3003 support solves and two evaluations of each of the 168 truncated vertices, with exact rational arithmetic.

## What this changes

EC49AS identified that the **unpriced full-purchase** upper envelope F ceases to match the witness after η=32/103. The new priced dual, with λ=3/50 and exact purchase coins, proves the original witness remains globally optimal at least through η=9/25>32/103. Therefore 32/103 was a method boundary, **not** a true optimum transition. No assertion is made that η=9/25 is the sharp end of the witness's optimality.

## Reproduction and native-type limits

Run Python standard-library `VERIFY_DUAL.py` next to `VERIFY.py` and compare output with `DUAL_REPORT.json`; both scripts were actually executed in this run. They enumerate the cut polytope and calculate all purchased scores using exact P and Q source leaves. Neither finite grid search nor floating arithmetic supplies the real-parameter argument; the proof is the two-endpoint convexity of the cost-aware dual.

No Source-native CLAIM, Result or independent Driver review is inferred from the proof/PR. This is strictly an auxiliary positive probability BRC theorem; signed BRC, native X6 and heartbeat require a separate typed preservation map, and the protected P000/ACTIVE worldview are unmodified.
