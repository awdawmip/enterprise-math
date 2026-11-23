# EC49FXX — Exact genuine Farey fixed-probe height staircase for distances 5–10

Date: 2026-11-23 (Asia/Shanghai). **Frozen scientific input: BRC16943.** Continuation of EC49FXW (frozen scientific source `b35d9862cb4e52fac9899fb3e4260177d70e4e7f`), itself continuing EC49FXV (`d1bf9b7b827b919d4c14da968e5a9f792c550ef8`). Parent product/spectrum census: EC49FXU (`5e33d4576bb0c1ef09e9169f8e17df469b8b7692`). This is an auxiliary scalar model result; no P000 or ACTIVE-worldview edits, no native-X6 transfer. Status **AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED**.

## Exact question and observer

Retain the original Boolean predicate
```text
C11(h,n) = P10(h mod 10,n mod 10) * 1[9h+10n != 0 mod 11].
```
For each reduced rational Farey anchor 0<a<b with b≤H, use the previously frozen determinant-one left-branch rephasing and normalized 10×11 trace U⊗V. The observer receives its **full indexed reflection-defect spectrum** and the externally known height bound H. Anchor and affine origin remain hidden; a single fixed set of physical Boolean sites S⊂(Z/10)×(Z/11) is chosen **before** observing that spectrum. For each equal-spectrum pair of *different normalized traces* with b≤H, require at least r differing bits on S. Write N_H(r) for the minimal cardinality of S.

This continuation proves the previously open high-distance low-height cases: all **integer 22≤H<64 and 5≤r≤10**, and derives the all-height result for each such r. H≥64 was known from EC49FXV; r≤4 and H≥22 were completed in EC49FXW.

## Theorem: exact staircase

For every integer H≥22 and 5≤r≤10:

| r | first plateau | second plateau | third plateau | final plateau |
|---|---|---|---|---|
| 5 | N=15, 22≤H≤46 | N=16, 47≤H≤51 | N=17, 52≤H≤53 | N=18, H≥54 |
| 6 | N=18, 22≤H≤46 | N=19, 47≤H≤51 | N=20, 52≤H≤53 | N=21, H≥54 |
| 7 | N=21, 22≤H≤41 | N=22, 42≤H≤45 | N=23, H=46 | N=24, H≥47 |
| 8 | N=24, 22≤H≤41 | N=25, 42≤H≤45 | N=26, H=46 | N=27, H≥47 |
| 9 | N=27, 22≤H≤35 | N=28, 36≤H≤37 | N=29, 38≤H≤43 | N=30, H≥44 |
| 10 | N=30, 22≤H≤35 | N=31, 36≤H≤37 | N=32, 38≤H≤43 | N=33, H≥44 |

Combining this with EC49FXW yields one uniform formula for **all integer H≥22 and 1≤r≤10**. Let A={1,4,6,9}, B={2,7}, C={3,8} be row supports. Let Z_G(H)⊆Z/11 comprise precisely the non-null deleted columns z occurring in an *actual* equal-spectrum normalized genuine-anchor pair of support G at maximum first-attainment denominator ≤H. For each of the three minimal supports, put m_A=4, m_B=m_C=2. Then

```text
N_H(r) = 3r + sum_{G in {A,B,C}} 1[ r > m_G * (11-|Z_G(H)|) ].
```

This formula counts **deleted-column occurrences by distinct z**, not pair multiplicity; full non-deleted 11-factor states are included separately in the census. All Z_G(H) become complete by H=64, yielding N_H(r)=3(r+1) at all larger heights.

In particular the previous r≤4 formula would wrongly predict 16 sites at H=52,r=5; the exact value is **17**. The full unrestricted optimal cost is reached already at H=54 for r=5,6, at H=47 for r=7,8, and at H=44 for r=9,10 — all earlier than H=64 for r≤4.

## Proof

**1. Genuine-state and difference-support reduction.** By direct enumeration from the immutable C11 definition, each first-occurrence reduced anchor of b≤139 yields one of exactly 600 normalized product traces, and the 600 are exhausted by height 139. Their indexed reflection-defect spectra have 478 fibers, including 122 two-element fibers. Each two-element fiber shares the same 11-factor V, either complete or deleting exactly one column z. Its Hamming-difference support is G×(Z/11 minus {z}), where G is the XOR of the two 10-bit row words. Exactly seven G values occur; each contains at least one of the three *pairwise disjoint* A,B,C, and each A,B,C occurs as an exact difference support by height 22. For a full factor write z=null. These finite facts are rederived, rather than assumed from prior output, in the verifier.

**2. Analytic lower bound.** Fix one of the minimal supports G with m_G rows. Let q_G be the number of selected sites in these rows. An actual pair of exact support G exists for every H≥22, so q_G≥r. Suppose q_G=r. For every z∈Z_G(H), that pair requires

```text
r <= (q_G - number of selected sites in column z within G).
```

Consequently no one of those r sites may occupy any forbidden column z. There are just m_G(11-|Z_G(H)|) distinct physical sites in the remaining columns, so q_G=r is impossible if r exceeds this capacity; then q_G≥r+1. Because A,B,C are disjoint, adding the three bounds yields precisely the formula's right-hand side as a **rigorous lower bound** for every H≥22 and r≥1. The argument is independent of MIP duality, approximate arithmetic, or the particular minimizing layout. For r=5, H=52, forbidden columns for pure B already occupy nine of eleven columns, so with only two B rows at most 2×2=4 safe sites exist: B must use at least 6 sites; pure A already needs 6 and pure C needs 5. This gives the rigorous 17-site lower bound.

**3. Explicit upper certificates for r=5–10.** The accompanying self-contained `EC49FXX_HEIGHT_R5_R10_VERIFY.js` contains **18 fixed witness layouts**, encoded as ten 11-bit integer masks (one per row, bit z selects column z). They are supplied at every **right endpoint below the last plateau**:

- r=5,6: endpoints H=46,51,53.
- r=7,8: endpoints H=41,45,46.
- r=9,10: endpoints H=35,37,43.

At the final plateau use S={(j,z): j∈{1,2,3}, 0≤z≤r}, totaling 3(r+1) sites. Every genuine difference G contains at least one of A,B,C, and therefore at least one of row 1,2,3; deleting at most one column leaves at least r selected sites on that row. For each earlier plateau, the program exhaustively checks the corresponding stored explicit integer masks against every actual same-spectrum pair present by the endpoint. Monotonicity in H (a layout valid at the right endpoint remains valid at smaller H) supplies all intermediate upper bounds; the matching analytic lower bound is constant on each plateau. Together these are equal upper and lower bounds. EC49FXW already supplies the same matching upper bounds for r=1–4; the present formula's lower bound agrees with its four previously established staircases.

**4. Exhaustiveness and check correctness.** For b=2,...,139 and 1≤a<b with gcd(a,b)=1, compute the determinant-one inverse a^(-1) mod b, the unique frozen ten-phase rephasing, the P10 support word, and the 11-factor hole from the integer linear form 9h+10n. Deduplicate normalized (word,hole) pairs at their *earliest* anchor height. Compute the 110-entry indexed reflection spectrum from exact cyclic autocorrelations; collect every fiber of size two and its actual support G, hole z and first-attainment height max(b1,b2). The checker verifies the 600/478/122 census, the inclusion of A,B,C in every difference, the lower capacity formula, and the explicit upper layouts at **every H=22,...,139 for every r=5,...,10**. It independently rechecks C11=U⊗V for each first-occurrence anchor and 110 trace positions. Once all 600 states appear by H=139, no larger H adds a new normalized state; all claims for H>139 follow.

## Reproduction and observed result

Command: `node research_notes/portable_direct/EC49FXX_HEIGHT_R5_R10_VERIFY.js`. Expected JSON file: `EC49FXX_HEIGHT_R5_R10_OUTPUT.json`.

Local exact run (2026-11-23) produced **ALL_PASS**, 600 states, 478 spectra, 122 genuine paired fibers, 66,000 direct original-C11 equality checks, **708 height-by-distance cases** (6×118), **69,588 physical layout-versus-pair distance comparisons**, and 18 explicit endpoint masks. No numerical optimizer, floating-point arithmetic, network service, Lean, CI or unverified random search is used by the proof checker. An independent exploratory HiGHS integer-programming comparison agreed with selected endpoints, but it is not needed for the theorem.

**Unresolved / next unit:** The externally given denominator bound H is an extra observer input. Quantify its acquisition cost (and possible correlations with the full indexed spectrum) before projecting these fixed-probe conclusions into a joint-observation protocol. Then address original-trajectory phase/branch/provenance and native X6 transfer with a declared map and corresponding proof. Formal Result/independent mathematical Review remain separate.
