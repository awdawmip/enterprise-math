# EC49DU — Joint neutral futures reveal an eighth native BRC residual

**2026-11-02 | Author analytic theorem and executed exact checks | PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**

## Exact scientific scope and immutable inputs

Continues EC49DT at commit `a63bee1c8c2e912e546ab7bf695305b8d1399f26`. Scientific frozen references: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Separately, current normative reads: GK `main@6fe5152374ea27cc2a7247434dfcbd5495c25d8a`; EM `main@9a1ea3ab71469ff6a4f645852d1be9f33b09fdc9`. P000 and ACTIVE worldview unchanged.

An old history w is an ordered, signed **six-native-axis** path (primitive steps ±E_j), length n and full displacement D=−2E1. Flags A/B detect adjacent (+E1,+E2)/(+E2,+E1) *including the history/future seam*; old last-step port L is 1 for +E1, 2 for +E2 and 0 otherwise. If the positive primitive count is p, the old BRC instruments are X_p=∏x_j^{p_j}, Y_p=∏y_j^{p_j}, plus unweighted count, with all x,y strictly positive and negative primitive steps of unit weight. Separate returning future operation words and final (A,B) buckets form distinct columns. No positive weights are treated as signed amplitudes.

Original future operations are a=(−1,−1), b=(−2,−2), c=(+1,+2,−1,−2), d=(+2,+1,−2,−1), e=(+3,+1,+1,−3). EC49DT diagnostically added f=(+1,−1). **This study additionally tests g=(+2,−2)**. Here each signed integer is a native primitive axis index, *not* a spatial dimension reduction. A future operation word is accepted if its full six-axis displacement is +2E1, equivalently #b=0 and #e=#a+1. Both f and g have zero displacement and neither has an internal A/B pair.

## Theorem A — exact eight-feature factorization for every future horizon

On formal old states (A,B,L)∈{0,1}²×{0,1,2}, let

`z=(z00,z01,z10,z11,pA,pB,q,r)`,

where `zij=1[(A,B)=(i,j)]`, `pA=1[A=0,L=1]`, `pB=1[B=0,L=2]`, `q=1[A=B=0,L=2]`, and `r=1[A=B=0,L=1]`.

For **any finite history population**, **every x,y∈(0,∞)^6**, and **every finite h≥2**, the actual three-instrument returning-future observer O_h has exactly the same rank as the historical 24-column matrix `H8=[X_p z | Y_p z | z]`. For cumulative horizons 1..h (h≥2) the same equality holds. At h=1 only operation e returns and `rank O_1=rank H4`, where H4 uses the four old joint flags.

*Upper bound.* Each operation ends in a negative primitive, so internal A appears only in c, internal B only in d, and no A/B can start across operation boundaries. Writing C=1[c occurs], T=1[d occurs], s=first primitive of the whole future, the exact flags after concatenation obey
`A'=A ∨ C ∨ (L=1 ∧ s=+E2)`, `B'=B ∨ T ∨ (L=2 ∧ s=+E1)`.
For C=T=1 output is 11. For C=1,T=0 the dependence is on B and at most pB; for C=0,T=1 on A and at most pA. For C=T=0, future beginning e/a/b preserves the four z-buckets; beginning f changes (00,01,10,11) by `(−q,+q,−(pB−q),+(pB−q))`; beginning g by `(−r,−(pA−r),+r,+(pA−r))`. Thus all columns factor linearly through z.

*Matching lower bound.* At h=2 the returning words `ef,ce,ec,de,ed,fe,ge,eg` recover all four joint bucket features (from ef), pB (ce−ec, 11 bucket), pA (de−ed, 11 bucket), q (fe−ef, 00 bucket) and r (ge−eg, 00 bucket). At h=3, the returning word aee recovers the four joint buckets, and respective contrasts `cce−ecc`, `dde−edd`, `ffe−eff`, `gge−egg` recover pB,pA,q,r. Here subtraction refers to normalized **columns** in a real-linear rank argument, not negative BRC path masses. Append (ae)^k to any returning future to raise its length by 2 without changing final flags or net displacement. Its extra positive BRC multipliers are `(x3*x1²)^k` and `(y3*y1²)^k`, which are nonzero. Hence both parity base constructions persist for every h≥2. Distinct future-word BRC multipliers are nonzero column scalars separately in each instrument, so the rank identity holds for arbitrary x,y. The eight formal features are independent: feature rows on old states 000,001,002,010,011,100,102,110 have determinant +1.

## Theorem B — all-parameter sharp full-24 criterion at n=10

Fix n=10,D=−2E1: exactly four of ten primitive steps are positive. Define 11 count patterns

`C11={(p1,p2)=(1,3),(2,2),(3,1)} ∪ {(1,2,one E_j),(2,1,one E_j):j=3,4,5,6}`.

For each p let G_C have one row `(X_p,Y_p,1)`, giving a real 11×3 matrix. Then for **every x,y>0**, `rank H8=24` **if and only if** `rank G_C=3`. Thus all future observers O_h, h≥2, have full 24 rank exactly under the same condition.

*Sufficiency.* There are eight genuine n=10, D=−2E1 histories at **each** of the eleven count patterns whose old states span z with determinant +1. This is a finite integer certificate: `EC49DU_EXECUTED.json` lists all 88 signed native paths; `VERIFY_EC49DU.js` reconstructs all positions, positive counts, flags and ports using finite remaining-multiplicity dynamic programming. Given three linearly independent G_C rows, choose the corresponding three groups of eight histories. Their 24×24 matrix is, up to ordering, `G3 ⊗ F8` with det F8=1, so `|det M24|=|det G3|^8>0`.

*Necessity.* A history exhibiting both A and B has, among its four positive primitives, either subsequence 121 or 212. Therefore its p lies in C11. When `rank G_C<3`, a nonzero coefficient triple annihilates the three instrument values (X_p,Y_p,1) for all those p. Applying that triple solely to the z11 coordinates annihilates every historical row, so H8 cannot have rank 24.

*Sharp length bound.* The history positive-step count at D=−2E1 is (n−2)/2. At lengths n≤6 there are fewer than three positive steps and both flags cannot occur. At n=8 exactly three positive steps permit at most the two relevant patterns (1,2),(2,1), so the z11 instrument submatrix has rank ≤2, preventing rank 24. The construction above shows n=10 suffices whenever `rank G_C=3`.

## Exact model witness and observable eighth residual

For x=(2,3,1,2,3,4), y=(5,7,3,5,7,9), the three core C11 rows have `det G3=420`, and the 24×24 integer determinant is `420^8=968265199641600000000`.

The new r coordinate cannot be omitted from the EC49DT seven-feature sufficient history. Within p=(1,3), construct two *positive* two-path populations: P+ uses states (0,0,1),(0,1,0); P− uses states (0,0,0),(0,1,1), with actual ordered ten-step paths stored in the execution report. Their aggregate prior seven features (z00,z01,z10,z11,pA,pB,q) coincide, and all paths have the same X_p,Y_p. Therefore the old f-only future observer cannot distinguish them. Under the new returning word ge, final 00-bucket count difference P+−P− is −1 and both positive BRC channels have proportional nonzero differences. This is a minimal **observer-language-dependent structural residual**, not a physical-law assertion.

## Verification, reproducibility and permissions

Run `node VERIFY_EC49DU.js > EC49DU_EXECUTED.json` (Node with BigInt). The source was **actually executed** using its verify() body in a V8 environment; all assertions returned PASS. It enumerated **all returning operation words h=1..5** (1,8,51,304,1770) and obtained exact modular transfer ranks 4,8,8,8,8; the determinant is computed using integer BigInt Bareiss (no floats). All 88 native signed histories are constructed and rechecked. A separate independent Python standard-library checker also executed locally; its full archival evidence is available in the same-turn author handoff. For unrestricted h, the conclusion comes from the analytic operator proof, not from extrapolation of five finite windows. The historical witness enumeration is finite with exact declared counts. The executable records its sample, tested transfer ranks, collision populations, and all witnesses in the JSON file.

Native Enterprise Math gateway 0.6.11 returned `research_authority_granted=false`; owner lookup `CONTROL_QUOTA`; own `session_start` refused `STATIC_READONLY_SCOPE_DENIED`, `operation_sent=false`. A GitHub draft commit is author evidence, **not** native Research Activity, Task CLAIM, frozen Result, independent Driver review or Foundation admission.

**Next EC49DV:** classify the *defective* cases `rank G_C<3`, determining actual historical/future ranks and minimal sufficient residuals (full-24 criterion alone does not determine those lower ranks), with an exact smallest counterexample or a refined sufficient statistic.
