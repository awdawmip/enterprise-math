# C314 — Exact source-derived reconstruction of the 79-branch positive-rational auxiliary

2026-10-26 | AUTHOR-EXACT; **unclaimed / not Source-admitted / not a native GF(2)-BRC theorem**.

## Frozen scope and provenance

GLOBAL_KNOWLEDGE_V1: main@f5baac141aa65cc4c755d83b19b1008b4e5599c6. Enterprise Math source: main@28000bfcd28be1b4d3f1b8ae94e662e78a2c437d. Read the canonical 00_BOOTSTRAP, OPERATING_MANUAL, P000 and ACTIVE worldview, project TASK researcher route, portable research protocol, and BRC/math policy. The source math is the frozen C275 original_F/fixed_multiplier/moving_mass definitions from the C301 replay pack preserved in C311/C313; frozen C284/C293 route selection has record SHA256 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

The test checks the **actual independently rederived termwise polynomial identities**, not just 125 approximate sample agreements. It bypasses C305.prepare and treats C298.make_terms as the candidate to be cross-examined; both sides necessarily share the upstream frozen C275 source definition and frozen paths.

## Theorem A — formula-by-formula equality on each frozen path

Let there be 79 fixed nodes u_j, with moving-index tuple I=(5,50,55,56), J its 75-index complement, x_k(t)=w_k+d_k t, and C275 exact constants Q=2^128, A, H, Z and fixed integer masses W_j. Define:

\[
T_j(t)=\frac{W_j}{Q}\prod_{k=0}^{3}
 \frac{Z-x_k(t)}{Z-u_{I_k}}
 \frac{|u_j-u_{I_k}|}{|u_j-x_k(t)|}
 \quad(j\in J),
\]

\[
T_{75+k}(t)=\frac{A/H}{[(2-x_k(t)^2)(3-x_k(t)^2)]^3}
 \prod_{j\in J}\frac{Z-u_j}{|x_k(t)-u_j|}
 \prod_{m\ne k}\frac{Z-x_m(t)}{|x_k(t)-x_m(t)|}
 \quad(k=0,1,2,3).
\]

On every frozen C293 strip the linear gaps retain a fixed nonzero sign, certified at both endpoints by exact Fraction arithmetic. Hence absolute values are fixed signed rational-affine factors, and all T_j have an extension in Q(t). By direct substitution into the C275 functions,

\[
F(v(t))/Q=\sum_{j=0}^{78}T_j(t)
\]

identically on the chosen strip and as the corresponding rational function in Q(t). The source-derived rational-factor representation of every T_j agrees with C298.make_terms in Q(t) for all 125 paths and all 79 labels.

**Proof.** The C275 fixed contribution is W_j times fixed_multiplier(j,v); dividing by Q gives the four displayed replacement ratios. Moving_mass(k,v)/Q gives the base factor and 75+3 gap factors shown above, with no extra scale. On each closed strip the sign of every affine gap is constant. Independently orient each source denominator positive, and write each direct branch as a rational scalar times ordered numerator/denominator pairs. For every corresponding source pair (n,d) and candidate C298 integer pair (N,D), exact coefficient convolution checks nD=Nd in Q[t]; the two rational scalars also agree exactly. Since each branch has 4 factors if fixed and 79 if moving, the number of exact cross-product checks is

\[
125(75\cdot4+4\cdot79)=77\,000.
\]

All 77,000 equalities and all 9,875 scalar/label alignments passed. This is an identity of rational functions rather than an interpolation inference. As a separate check, on each of the 125 strips the independent C275 original_F(v(mid))/Q, the source-derived sum and the candidate-factor sum agree as complete exact fractions. QED.

## Theorem B — two independent exact vanishing principal parts per path

For the moving pairs (5,55) and (50,56), let q(t)=q_0+q_1 t be the primitive integer linear factor of the corresponding positive-on-strip moving gap, with rational zero r=-q_0/q_1. The direct C275 reconstruction shows that, at r, **only** the two corresponding moving branch terms have this simple pole, with supports respectively (75,77) and (76,78). Their principal-part coefficients

\[
\rho_j=\lim_{t\to r}q(t)T_j(t)
\]

are exact, individually nonzero rationals and satisfy \(\rho_a+\rho_b=0\). This is checked independently of C305.prepare for **250/250** zero-residue pairs across 125 paths. Each path's two primitive factors are also distinct (125/125).

Let D_sh be C298's integer common denominator containing each such primitive factor with multiplicity one, and let A_sh=D_sh F/Q be its integer numerator (the integrality construction is C298's earlier result). Vanishing principal part implies A_sh(r)=0, so q divides A_sh in Q[t]; q primitive and A_sh integral imply by Gauss's lemma that q divides A_sh in Z[t]. The two distinct primitive factors can thus be canceled in an integral polynomial representation.

This proves *those two* legitimate cancellations; the separate C300 result that all **other** linear and quadratic factors survive is not reproved here. QED.

## Exact execution and checkable inputs

An executable same-content compact replayer is published as C314_COMPACT_SOURCE_RECONSTRUCTION_REPLAYER.py. Run it from a directory containing a subfolder EM_C301_EXACT_PORTABLE populated by exactly these frozen files: C275_STANDALONE_EXACT_REPLAY.py, C284_187_EXACT_DYADIC_BRACKETS.json, C288_ISOLATING_BOXES_EXACT.py, C293_125_REFINED_BRACKETS.json, C296_DYADIC_INTERVAL_SIGNS.py, C297_UNIFORM_WIDTH_AND_HEIGHT_EXACT.py, C298_SHARED_DENOMINATOR_EXACT.py. It uses Python stdlib Fraction and no floating-point predicates.

Verified execution results:

| Exact check | Passed |
| --- | ---: |
| Frozen paths with 79 labelled branches | 125 / 125 |
| Rational scalar/label alignments | 9875 / 9875 |
| Rational polynomial-factor cross-products | 77000 / 77000 |
| Midpoint equality with C275 original_F | 125 / 125 |
| Exact pairs of nonzero opposite residues | 250 / 250 |
| Distinct primitive pole factors | 125 / 125 |

The independently built full checker additionally emits C314_125_INDEPENDENT_SOURCE_AUDIT.json with all 125 indexed factor pairs, branch labels and exact residue numerator/denominator bitlengths. Its observed SHA256 is **dab2b9348acf85fdf1f9582642c5386447a862706ecd903bb930311846429591** (129,841 bytes). The exact compact executable Git blob is fe223f3eacfcdb78965381a6d9832e2ec7a38a16; its SHA256 is 3f75b797ec9828879a5d3c47eb17d52ecbe0630709005418a730c2830f7ea1b0. The full author proof and frozen inputs reside in the user-facing portable ZIP of this run. The compact script regenerates the decisive test independently from those frozen inputs.

## Observer/BRC scope and unresolved science

The scalar function is a **positive-rational auxiliary** with 79 labels, not the signed/phase/port-aware native GF(2)-BRC carrier. Both opposite principal-part residues are nonzero and have distinct branch identities even though their scalar sum vanishes. Preserve provenance and future-operation residuals; no safe native quotient has been proved. This research neither modifies locked P000 nor transforms any auxiliary result into an X6 Cell theorem. The global six spatial dimensions plus separately typed time remain unchanged.

The proof assumes that C275's executable original_F is the intended C195/H168 model. It does **not** independently validate the earliest textual source's masses, floor operation, constants, or branch indexing. It does not rerun C300's 37,925 other noncancellation witnesses. Consequently the high-degree results C300–C313 receive a materially stronger **source-to-C298 algebraic audit**, but not a complete independent review of the entire dependency chain.

Native em_control_tasks returned CONTROL_QUOTA. Native em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Live Owner, Source CLAIM, activity session, frozen Result and independent Driver admission were not verified or obtained. GitHub branch persistence proves only that these author evidence bytes are stored.

**Next exact research unit:** Read the earliest standalone textual definition of C195/H168 (rather than copying C275) and audit all 79 terms, including W_j floor, Q, A/H, absolute-gap signs and the four moving indices. Independently audit noncancellation of the remaining 37,925 linear factors without sharing C300's residue implementation. Preserve the original labelled branch carrier while comparing scalar consequences.
