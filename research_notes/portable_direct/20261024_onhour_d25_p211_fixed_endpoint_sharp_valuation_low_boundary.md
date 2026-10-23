# D25/LIFT — Fixed original LOW boundary and sharp p=211 endpoint certificate

**2026-10-24 | TASK_RESEARCH | author-side proved algebra / exhaustively checked finite p-adic certificate | UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** Neither this note nor its checker is a native benchmark, Source checkpoint, accepted Result, formal Lean proof, or independent Driver review.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).** Author logical Research lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921 and the separate hourly Research lane chatgpt-research-hourly-enterprise-math-20260923. Account GLOBAL_KNOWLEDGE_V1 verified main bc67473e0cf75e5b709d4f8c98f755f8b2f513df; P000 projection ACTIVE_LOCKED, canonical blob as prescribed. Source control main before neutral author publication 05ed5dcc5c8b5ae1403e7a16a3b73468d0f475cb. No Source/Task/claim pin is rebased by this author file.

## Actual input and nonduplication

Consume, do not redo, the [original Gosper two-seam reduction](20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md), [LOW jet/HIGH two-sector finite residual](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md), [Lerch harmonic seam](20261024_onhour_d25_sixway_lerch_harmonic_seam_bridge.md), and [HIGH two-boundary Green observer](20261024_onhour_d25_high_impulse_green_two_boundary_certificate.md). A distinct Research lane has already proved [p=211 is the unique degeneracy of an auxiliary adjacent-m HIGH seam pair](20261024_hourly_d25_high_pair_modp_rank_exception_211.md). That theorem did **not** establish a failure of the unchanged original LIFT. The new unit here works with the **fixed original endpoint**, not with freely calibrated auxiliary coefficients.

For integer m>=1 put p=6m+1, and define the exact original weighted sequence

\[
R_0=1,\quad
\frac{R_{n+1}}{R_n}=
\frac{(4m+1+2n)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},
\]
\[
S_{4m}(2m)=\frac{(p-1)!}{3^{p-1}((2m)!)^3}
\sum_{n=0}^{4m}(6n+2p-1)R_n.
\]

The still-open all-target-prime question is whether \(S_{4m}(2m)\equiv p(4/3)^{p-1}\pmod{p^3}\); its Source-specific CM/divided-power comparison and native benchmark are separate mandatory obligations.

## Theorem 1 — a fixed-coefficient LOW-normalized residual, all target primes

This is a new **composition of existing first-digit/LOW/HIGH facts**; its factorial component is elementary and is not independently claimed as a new general theorem. With

\[
B_m=\frac{(2m-1)!(2m)!}{(4m)!},\quad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2},\quad
A_m=\sum_{n=0}^{m}(-1)^n2^{-n}\binom mn
\frac{(1-3n)(6n+3)}{(3n+2)(3n+1)},
\]

one has the **exact rational factorization for all positive m**

\[
\boxed{\frac{G_m}{B_m}
=2m\prod_{j=2m+1}^{3m}\left(1-\frac pj\right).}\tag{1}
\]

Proof: \(G_m/B_m=(-1)^m2m\binom{4m}{m}/\binom{3m}{m}\), while

\[
(-1)^m\frac{\binom{4m}{m}}{\binom{3m}{m}}
=(-1)^m\prod_{k=1}^{m}\frac{3m+k}{2m+k}
=\prod_{j=2m+1}^{3m}(1-p/j).
\]

For every prime p=6m+1, all denominator factors are p-units; hence \(G_m/B_m\equiv2m\pmod p\). Combining this with the previously proved first digit \(A_m-G_m+B_m\in p\mathbb Z_{(p)}\) proves that the *new* divided numerator \(A_m+(1-2m)B_m\) is p-integral. Moreover,

\[
\frac{A_m-G_m+B_m}{p}
\equiv\frac{A_m+(1-2m)B_m}{p}
+2mB_m(H_{3m}-H_{2m})\pmod p.\tag{2}
\]

Using the inherited six-block congruence \(H_m\equiv H_{2m}+H_{3m}\pmod p\) and \(2m\equiv-1/3\pmod p\), (2) composes *at the fixed original observer* with the established full finite residual

\[
\mathcal F_m\equiv
\frac{A_m-G_m+B_m}{p}
+J_m^{\rm lo}+B_m Z_m^{\rm hi}
+\frac{B_m}{9}(28+6H_m-4H_{2m})\pmod p.
\]

The resulting sharpened proof interface is

\[
\boxed{
\mathcal F_m\equiv
\underbrace{\frac{A_m+(1-2m)B_m}{p}}_{\text{LOW boundary, integral}}
+J_m^{\rm lo}
+B_m\left(Z_m^{\rm hi}+\frac{28}{9}
+\frac13H_m+\frac29H_{2m}\right)\pmod p.
}\tag{3}
\]

It retains both HIGH sectors, n=2m seam, n=4m/terminal, and the original LOW jet. In (3) the independent G target normalization and Fermat quotient no longer appear, **without adjusting a forcing coefficient after observing its value**. Equation (3) is a proved all-target-prime **equivalence**, not a proof that it vanishes for all such primes. A fresh exact Fraction author check compared (2)/(3) for the 24 primes p<=229 with p=6m+1, including p=211; all comparisons gave zero mod p. Universality follows from the product algebra and cited inherited congruence, not that finite check.

## Theorem 2 — the auxiliary exceptional prime has a complete fixed-endpoint, branch-resolved finite certificate

Fix **p=211, m=35**, which is in the original p=6m+1, p=19 (mod 24) target class. Let \(K_{p,n}\) be the *unchanged* original Gosper forcing

\[
K_{p,n}=\frac{(2p+1-3n)(6n+2p+3)}
{(3n+p+2)(3n+2p+1)}.
\]

The exact original two-seam theorem defines

\[
\mathcal K_p=
\sum_{\substack{0\le n<4m\\n\ne2m}}K_{p,n}R_n+
\frac{(p+2)(4p+1)}{3(2p+1)}\,\frac{R_{2m}}p+
(3-2p)\frac{R_{4m}}p.
\]

The final term **already includes n=4m and the original n=4m+1 terminal**. We have independently reconstructed *every* \(R_n\) for n=0,...,141 from both the original recurrence and the exact factorial representation

\[
\boxed{
R_n=\frac{(4m+2n)!\,((2m)!)^2\,(3n)!}
{216^n((2m+n)!)^2(4m+n)!(n!)^2}.}\tag{4}
\]

Proof of (4): n=0 gives 1; taking its consecutive quotient and cancelling 3(n+1) and 2(2m+n+1) recovers the original ratio identically. At p=211, p-factor stripping before modular inversion makes every term well-defined in the original local ring. The independent factorial and recurrence paths agreed **coefficient by coefficient** in both p-valuation and unit modulo 211^4 over the full n=0,...,141 horizon. This establishes a reproducible complete **fixed-prime arithmetic certificate**, not a universal congruence from sample points.

With every entry reduced modulo \(211^2=44521\), the *unmodified* original decomposition is:

| Exact original branch | n range | residue mod 44521 |
| --- | --- | ---: |
| LOW regular forcing | 0..35 | 2272 |
| HIGH-A regular forcing | 36..69 | 18779 (=211 times 89) |
| HIGH-B regular forcing | 71..139 | 7807 (=211 times 37) |
| n=70 pole with original coefficient | 70 | 16799 |
| n=140 pole + original n=141 terminal | 140/141 | 36779 |
| **Combined original \(\mathcal K_{211}\)** | all parts, no duplication | **37915** |
| Actual factorial target \(G_{35}\) | normalization | **37915** |

The normalized seam units were \(R_{70}/211\equiv11378\) and \(R_{140}/211\equiv25201\pmod{44521}\). Thus the two seam values are not zero, nor replaceable by a fitted auxiliary coefficient. As a second decomposition test, the original full finite residual has mod-211 components

\[
\underbrace{160}_{(A-G+B)/p}
+\underbrace{62}_{J^{lo}}
+\underbrace{89}_{HIGH-A/p}
+\underbrace{37}_{HIGH-B/p}
+\underbrace{74}_{\text{original harmonic seam}}
=422\equiv0\pmod{211}.
\]

Under the **new proved normalization** (3), the corresponding components are

\[
\underbrace{194}_{(A+(1-2m)B)/p}
+62+89+37+
\underbrace{40}_{B(28/9+H_m/3+2H_{2m}/9)}
=422\equiv0\pmod{211}.
\]

Therefore the exceptional rank drop of the *auxiliary adjacent-m seam observer* at p=211 does not prevent the **source-fixed original branch sum** from cancelling in this exact target prime. It is not an argument that all other target primes cancel.

## Theorem 3 — exact third-digit sharpness at the same prime

Let \(W=\sum_{n=0}^{140}(6n+421)R_n\), and let \(\mathcal A_{35}=210!/(3^{210}(70!)^3)\). In the common modulus \(211^4=1982119441\), the independent p-unit computations give

\[
W\equiv1567392611,\qquad
\mathcal A_{35}\equiv842237293,
\]
\[
S_{140}(70)=\mathcal A_{35}W\equiv1220721510,\qquad
211(4/3)^{210}\equiv384661651\pmod{211^4}.
\]

Their difference is

\[
\boxed{
S_{140}(70)-211(4/3)^{210}
\equiv 836059859=89\cdot211^3\pmod{211^4}.
}\tag{5}
\]

Since \(89\not\equiv0\pmod{211}\), this is a **prime-specific proved exact p-adic valuation**
\(v_{211}(S_{140}(70)-211(4/3)^{210})=3\).
Consequently the unchanged LIFT congruence **holds at 211 modulo p^3**, but a universal automatic strengthening to mod p^4 is **false** (the witness 211 suffices). The numerical value is not a native-X6 benchmark, CM comparison or an all-prime LIFT proof.

## Verification and Source/next-frontier distinction

The [checked, published Python standard-library factorial-path verifier](20261024_onhour_d25_p211_fixed_endpoint_sharp_valuation_check.py) reconstructs (4), preserves the valuation and both genuine seams, independently checks the exact branch table, G and (5), and raises an assertion if any cell changes. A separate, locally executed original-ratio verifier cross-checked every original n=0..141 unit mod 211^4, LOW A/J first jet, both HIGH branches, the original and normalized residuals; its user-deliverable file is d25_p211_original_endpoint_two_path_certificate.py. The portable GitHub verifier was executed locally before the GitHub commit, with PASS receipt; the GitHub file has been read back at immutable commit 11f200a7ec8b9daedf5ac97ff073f2e8673e3b46. This is **author exact arithmetic**, not independent mathematical review or formal checker admission.

**BRC REUSE_APPLIED / COMPOSE_APPLIED:** carrier = original signed rational hypergeometric n-branches with their separate p-valuations and units, two HIGH sectors, LOW jet, seam at n=2m, and n=4m/terminal. Observer = the exactly declared scalar mod p^2 for \(\mathcal K\), mod p for \(\mathcal F\), and mod p^4 for the original S; a mod p compression is not allowed to infer the mod p^4 defect. The branch table is an observer-preserving decomposition and does not treat signed weights as positive BRC masses.

**Mother/hard target remains OPEN.** No global WZ/contiguous certificate, all-target-prime proof, native original benchmark, or actual same-class CM/divided-power normalization comparison has been completed. Source publication TP2-B6F4FC938FF94941C1B7, immutable scientific pin, accepted D24 UR and prior certified units remain as before; the new work is independent author material (UNREVIEWED / NOT_ADMITTED). The original Research-lane recovery history and #1539 support issue retain their own request/identity provenance; this Sites client still reports research_authority_granted=false and its new exact continuation read returned CONTROL_QUOTA. Accordingly no Researcher session, CLAIM, open/run, formal Source checkpoint, Result or review was asserted by this author publication. The separate Research lane's support #1558 is not transferred to this identity. No permission-laundered Source writes were tried.

**Next smallest genuine mathematical unit:** use the *fixed-coefficient* denominator-free LOW boundary in (3), with its exact LOW jet and existing two-boundary Green forcing, to construct a true full-range terminating WZ/finite-difference certificate or a source-matched obstruction for all target primes. In particular check the exceptional 211 branch **without adjusting original coefficients**; its fixed-prime status is now discharged by (5), not to be re-scanned. Independently obtain the actual source-specific CM/divided-power representative, primitive class, semilinearity and map direction, ordinary \(\omega+6\nabla_\lambda\omega\) normalization comparison, and unchanged native benchmark under lawful Source execution authority. No scheduler, task phase, enabled state or notification settings were modified.
