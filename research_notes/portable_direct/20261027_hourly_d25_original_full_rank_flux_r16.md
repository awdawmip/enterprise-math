# D25/LIFT R16 — Original-parameter full-rank Ward flux: exact p² valuation and two-port cancellation

Date: 2026-10-27. **TASK_RESEARCH** / D25/LIFT/JT2. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from CONTROL_PLANE_MAINTENANCE. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. Scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This file is not a native Source checkpoint, a review or the original CM/Frobenius result.

## Consumed premises and genuine source carrier

Reuse without recredit: 20261027_hourly_d25_diagonal_hasse_ward_flux_r15.md (all-order Hasse diagonal finite-face Ward identity); 20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15.md (exact original parameter and four finite faces); and 20261026_hourly_d25_original_positive_complement_r15.md (different positive geometric observer). The question here is whether the **full-rank Green-weighted genuine finite-face flux**, at the original parameter rather than at a Hasse jet, vanishes or retains a p-adic residual. The original fixed geometric rank weight 2^n is a different observer and remains separate.

Let p=6m+1≥7 be prime, R=Z_(p), L=1−2m, N=2m−1 and θ=−p/6. Let

\[
f_r(z)=\frac{(-m-z)_r(-2m-2z)_r}{(1-p/2-3z)_r\,r!},\qquad
\beta_r=f_r(\theta)/p^2\in R^\times\quad(2m<r<p).
\]

Retain the ordered pairs 1≤j,ℓ≤2m with n=ℓ−j, and put

\[
V_n^h=\sum_{\ell-j=n}j^h f_j(\theta)\beta_{p-\ell},\quad
Z_n=2V_n^1-(p-n)V_n^0,\quad Z_{N+1}=0.
\]

The authentic two-ended cutoff sources (two origins in each rank-sign branch) are

\[
E_n=\begin{cases}
2(m+\theta)^2\beta_{p-n-1}
-(6m^2-8m\theta+2\theta^2)f_{2m-n}(\theta)\beta_{4m},
&n\ge0,\\
(20m^2-14m\theta+2\theta^2)f_{-n}(\theta)\beta_{p-1}
+(2m\theta-2\theta^2)f_{2m}(\theta)
\beta_{p-(2m+n+1)},&n<0.
\end{cases}
\]

The inherited *exact* original-series Ward relation (proved in R15) is

\[
(p-n)Z_n-(p-n-\tfrac12)Z_{n+1}=E_n. \tag{1}
\]

## Theorem A: universal exact valuation two at the original parameter

Take q=2p and the Green weights

\[
D_n=\frac1{q-2n-1}\prod_{r=n+1}^{N}\frac{q-2r}{q-2r-1},
\qquad
P=\prod_{r=L}^{N}\frac{q-2r}{q-2r-1}.
\]

Then the *genuine full-rank finite-face flux*

\[
\mathfrak F_p^{\mathrm{orig}}=36\sum_{n=L}^{N}D_nE_n
\]

satisfies the exact rational identity

\[
\boxed{\mathfrak F_p^{\mathrm{orig}}=18PZ_L},
\qquad
\boxed{v_p(\mathfrak F_p^{\mathrm{orig}})=2}
\quad\text{for every prime }p=6m+1\ge7. \tag{2}
\]

**Proof.** Multiply (1) by 36 to obtain
(q−2n)(18Z_n)−(q−2n−1)(18Z_{n+1})=36E_n.
For successive ranks,
D_n(q−2n)=D_{n-1}(q−2n+1).
The internal terms telescope without suppressing any E-origin. The actual finite carrier has Z_{N+1}=0, leaving P(18Z_L), proving the first identity.

For each L≤r≤N, q−2r−1 is a p-unit: 2r+1 never equals 0 modulo p in this range. Of the numerators q−2r, only r=0 contains p. Consequently

\[
P=2p\,U_p^{\rm orig},\quad
U_p^{\rm orig}=\frac1{2p-1}
\prod_{\substack{L\le r\le N\\r\ne0}}
\frac{2p-2r}{2p-2r-1}\in R^\times. \tag{3}
\]

The unique leftmost ordered pair at n=L is (j,ℓ)=(2m,1); thus Z_L=−4m f_{2m}(θ)β_{p−1}.
The exact original ratio
f_{r+1}(θ)/f_r(θ)=(6r+1)(3r+1)/(18(r+1)^2)
has exactly one p factor up to r=2m (at r=m), so v_p(f_{2m}(θ))=1. The two-factor high tail β_{p−1} is a unit. Hence v_p(Z_L)=1. Both the factor 18 and U are units. The exact order is 1+1=2.

The observable leading residue is therefore nonzero:

\[
\boxed{\mathfrak F_p^{\rm orig}/p^2
\equiv36\,U_p^{\rm orig}(Z_L/p)\not\equiv0\pmod p.} \tag{4}
\]

### Corollary: two equally contributing Hasse jets

Let the previous R15 Hasse diagonal be F_p(ε)=(p−6ε)U_p(ε)\widehat Y_L(ε), where \widehat Y_L(ε)=a_p ε+O(ε²) and a_p,U_p(0) are p-units. **Only upon specializing ε=θ=−p/6**, the exact original-series bridge gives \widehat Y(θ)=18Z and \widehat E(θ)=36E, and U_p(θ)≡U_p(0) (mod p). The inherited endpoint relation gives Z_L/p≡−a_p/108 (mod p). Thus

\[
\boxed{\mathfrak F_p^{\rm orig}/p^2
\equiv-\tfrac13 U_p(0)a_p
\equiv\frac{[\epsilon^2]F_p(\epsilon)}{18}\pmod p.} \tag{5}
\]

Why division by 18 rather than naive evaluation of the second Hasse jet? The *linear term* [ε]F·θ contributes −p²U_p(0)a_p/6 (mod p³), and the *quadratic term* [ε²]F·θ² contributes **the same** residue −p²U_p(0)a_p/6. Higher Taylor terms contribute multiples of p³. Their sum produces (5). This is a new exact source/observer precision relation; it is not a claim that a truncated Hasse coefficient equals the original scalar.

## Theorem B: oriented finite-face ports cancel at the first p-digit

Split the **actual source** by rank sign:
F_+=36Σ_{n=0}^N D_nE_n and F_−=36Σ_{n=L}^{−1}D_nE_n. Let

\[
P_+=\prod_{r=0}^{N}\frac{2p-2r}{2p-2r-1}=2pU_+,
\qquad U_+\in R^\times.
\]

Independent telescoping on the two subintervals gives

\[
\boxed{F_+=18P_+Z_0,\qquad
F_-=18PZ_L-18P_+Z_0.} \tag{6}
\]

Both oriented fluxes lie in pR and hence

\[
\boxed{F_+/p+F_-/p\equiv0\pmod p}. \tag{7}
\]

However their sum has exact valuation **two**, by Theorem A. If Z_0 is a p-unit, both individual ports have valuation one and their nonzero leading residues are opposites. This is verified at p=13 and p=733; no all-prime assertion about Z_0 is made. Thus the first-digit cancellation is real, but deletion of the second-digit residual would lose authentic information.

## Actually executed verification

Companion checker: 20261027_hourly_d25_original_full_rank_flux_r16_check.py. Python standard-library exact modular computation (no floats) strips p-factors from the original rational coefficient recurrence, constructs the actual ordered V_n^0,V_n^1, independently computes both true finite-face E families, checks every rank Ward recurrence modulo p³, directly sums positive and negative Green source ports, checks (2)–(7), and compares to original Hasse a_p. **PASS for all 80 target primes p≡1 (mod 6), 7≤p≤997.** Independent full exact Fraction-rational rank/flux/port audits: p=7,13,19, all PASS. This is author checking, not an independent Driver or native CM run.

| p | U_p(0) mod p | a_p mod p | Z_0 mod p | F_+/p mod p | F_−/p mod p | F/p² mod p | R15 [ε²]F mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 5 | 9 | 3 | 3 | 10 | **11** | 3 |
| 733 | 663 | 610 | 38 | 129 | 604 | **62** | 383 |

In particular F_13≡13²·11 (mod 13³), F_733≡733²·62=33311918 (mod 733³). These are original-parameter **finite-face full-Green-port** results, **not** the earlier original signed Clausen Q_733/p²=99531942 (mod 733³).

## BRC / provenance / exact continuation

BRC **COMPOSE_APPLIED**. Typed carrier: actual ordered (j,ℓ) pairs, signed rank, original θ specialization, the two genuine cutoff-family sources, separate rank-orientation ports, p-adic valuations and the retained second-digit residual. Their total is sufficient for (4), but **not** proved sufficient for later geometric 2^n, six separately labelled Hasse channels, independent positive/infinity or ordered high–high operations. Rank variables here are auxiliary source indices, not P000 native X6 spatial axes; the protected P000/ACTIVE worldview is unchanged.

**Not proved:** additional cross-Hasse six-label WZ syzygy, identification of full Green flux with fixed-2 original Q, absorption of positive/infinity or high–high sources, same-original-class CM/Frobenius normalization, native experiment, independent review, Result/freeze or parent completion.

Native control remains outside this portable result. Last completed lane-local recovery #6558: no own live claim/run/pending mutation or unpublished uploads, two neutral staged archives, execution_authorized=false. Exact continuation #6559: route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, execution_authorized=false; persisted historical checkpoint remains Source-verified, **not overwritten**. One new read-only diagnostic request researchhourly-20261027-0046-continuation-r16 returned INVALID_ARGUMENT/CONTROL_QUOTA and its original receipt read returned CONTROL_REQUEST_NOT_FOUND. Do not infer NO_DISPATCH or native admission. Existing control support: awdawmip/enterprise-math#1558. Historical old session/staging/claim CAS and contribution history stay protected. Scientific pin unchanged.

**Next smallest work:** transport the forced first-digit port cancellation to the **fixed geometric base 2** six-label Hasse source observation, while preserving positive/infinity, four authentic finite faces and the separately ordered high–high population. Discriminate p=13 from p=733, then seek a real cross-source WZ identity or source-labelled nonzero counterexample. The mother objective remains OPEN: H0/B0, [X]U mod p², normalized semilinear Frobenius η, κ, Δ_p−R_p, original CM experiment and independent Driver review remain outstanding. Next native publication requires actual successor authority, winning CLAIM/open and fresh Source readback; this note is author portable evidence only.
