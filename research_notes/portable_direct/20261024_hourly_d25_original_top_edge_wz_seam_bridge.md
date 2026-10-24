# D25/LIFT — original top-edge WZ boundary, exact source seam bridge and a universal valuation-one theorem

2026-10-24 | TASK_RESEARCH | **NEW ALL-TARGET-PRIME RATIONAL/P-ADIC PROOF, 13 AUTHOR EXACT CHECKS; UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT.** This is a portable proof and reproducibility artifact, not a native benchmark, Source-authorized CLAIM/run, Result or independent review.

**Provenance.** Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen *scientific* Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. Author lane chatgpt-research-hourly-enterprise-math-20260923 is distinct from maintenance chatgpt-hourly-enterprise-math-20260921 and the independent onhour Researcher. The cited onhour exact WZ/FIVE theorem and exact original two-seam Gosper deformation are **inputs, not new units claimed here**. Previous onhour third-digit five-tail work covers the fixed-prime window ceil(m/2)<=k<=m−1. This proof treats the **previously uncovered top transition k=m** for p=6m+1, retaining the true original moving terminal.

Input references:
- Original full summand and WZ/FIVE: research_notes/portable_direct/20261024_onhour_d25_original_endpoint_all_m_wz_five_tail.md, commit c7fb90fd7ec451a954b553b963dd85d4ec99fc96.
- Original exact two-seam Gosper identity and source normalization: research_notes/portable_direct/20261024_onhour_d25_original_endpoint_gosper_two_seam_p2.md.
- Predecessor all-prime top-seam valuation v_p(R_(4m))=1 and the distinct source/carrier defect: the latter is at research_notes/portable_direct/20261024_hourly_d25_third_digit_odd_product_source_transfer.md, commit 28e35a1fd123e2cb3bdb29165928844c6792fd59. Neither is rerun or claimed as newly proved.

## 1. Exact original objects and new edge question

Fix a prime p=6m+1>=13 (m>=2). Put

\[
\mathcal A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad R_{r,0}=1,\quad
\frac{R_{r,n+1}}{R_{r,n}}=
\frac{(4r+2n+1)(3n+1)(3n+2)}
{36(n+1)(2r+n+1)(4r+n+1)},
\]
\[
W_{r,n}=\mathcal A_r(6n+12r+1)R_{r,n},
\qquad S_r=\sum_{n=0}^{4r}W_{r,n}.
\]

These are the **unchanged original source-defined summands**, including their authentic n=2m and n=4m seams. Reuse the independent onhour theorem, valid as an identity in Q:

\[
S_{m+1}-S_m=E_0+\sum_{j=1}^4E_j,\quad
E_0=W_{m,4m+1}g(m,4m+1),\
E_j=W_{m+1,4m+j}.
\tag{FIVE}
\]

The already-proved g has the boundary simplification, with Q_m=360m^2+274m+49,

\[
(6(4m+1)+12m+1)\,g(m,4m+1)
=\frac{2(3m+1)Q_m}{3(2m+1)(8m+3)}.
\tag{G}
\]

The exact original Gosper reduction at p=6m+1 defines \(\mathcal K_p\) and proves
\[
\frac{S_m}{p}=\mathcal A_m\mathcal K_p\quad\text{in }\mathbb Q.
\tag{S/K}
\]
Here \(\mathcal K_p\) includes BOTH normalized n=2m, n=4m/terminal seams; it is not an auxiliary HIGH carrier. Set \(T_4=R_{m,4m}/p\in\mathbb Z_{(p)}^\times\), as in that original two-seam theorem.

## 2. New theorem A — the complete old-rank boundary is the original terminal seam

**Theorem A.** Define the exact p-integral rational coefficient

\[
C_m=\frac{(2p-1)^2(3m+1)(360m^2+274m+49)}
{9(4m+1)(4p-1)(2m+1)(8m+3)}.
\tag{C}
\]

Then, for every stated prime,

\[
\boxed{\frac{E_0}{p}=\mathcal A_m T_4 C_m \quad\text{in }\mathbb Q,\qquad C_m\equiv-2\pmod p.}
\tag{EDGE-OLD}
\]

Consequently v_p(E_0)=1 exactly.

**Proof.** The original R recursion gives the exact endpoint step
\[
R_{m,4m+1}/R_{m,4m}
=\frac{(2p-1)^2}{6(4m+1)(4p-1)}.
\]
Substitute this and (G) into the unaltered WZ old-boundary E_0. The coefficient is exactly (C), proving the rational identity. All denominators in C are p-units for p>=13. In the finite field set \(m=-1/6\). Then \(Q_m=40/3\), \(g(m,4m+1)=4\), and \(R_{m,4m+1}/R_{m,4m}=-1/2\) modulo p; thus \(C_m=-2\) modulo p. Both \(\mathcal A_m\) and \(T_4\) are p-units, proving the sharp valuation. QED.

## 3. New theorem B — exact four-tail valuations and second normalized digit

Define for t<3p the **labeled p-free factorial**:
\[
U_p(t)=\prod_{\substack{1\le a\le t\\p\nmid a}}a\quad\bmod p.
\]
For j=1,2,3,4 set r=m+1 and n=4m+j, and define the explicit scalar

\[
\boxed{\tau_{p,j}=
4(6n+12r+1)
\frac{U_p(6r)\,U_p(4r+2n)\,U_p(3n)}
{3^{6r}\,216^n\,U_p(2r)\,U_p(n)^2\,U_p(2r+n)^2\,U_p(4r+n)}
\quad\in\mathbb F_p.}
\tag{TAU}
\]

**Theorem B.** Every genuine new-rank tail satisfies
\[
\boxed{v_p(E_j)\ge2,\qquad E_j/p^2\equiv\tau_{p,j}\pmod p.}
\tag{EDGE-NEW}
\]
A zero \(\tau_{p,j}\) is allowed: at p=13,19,31 respectively a genuine extra p factor occurs in the relevant linear term. No unjustified claim of exact valuation two is made.

**Proof.** From the original unchanged hypergeometric product, one has the exact rational factorial identity
\[
\mathcal A_rR_{r,n}=
\frac{(6r)!(4r+2n)!(3n)!}
{3^{6r}(2r)!\,216^n(n!)^2((2r+n)!)^2(4r+n)!}.
\tag{FACT}
\]
For r=m+1 and n=4m+j the seven factorial p-adic orders in the displayed numerator/denominator are respectively
\[
\begin{array}{c|ccc|cccc}
 & (6r)! &(4r+2n)!&(3n)!&(2r)!&(n!)^2&((2r+n)!)^2&(4r+n)!\\
v_p&1&2&2&0&0&2&1
\end{array}
\]
because 6r=p+5, 4r+2n=2p+2j+2, 3n=2p+3j-2, 2r+n=p+1+j, and 4r+n=p+2m+3+j. All arguments remain <3p for p>=13. Thus FACT has valuation exactly 2. The removed multiples of p contribute the factorial multipliers \((1!)(2!)(2!)/((1!)^2(1!))=4\). Stripping those p factors gives exactly the p-free unit quotient in (TAU); the remaining linear coefficient \(6n+12r+1\) can add valuation but never remove it. This proves both assertions. QED.

## 4. New theorem C — first genuine source-seam to full-WZ top-edge bridge at p³

**Theorem C.** For every prime p=6m+1>=13,
\[
\boxed{\frac{S_{m+1}-S_m}{p}\equiv
\mathcal A_mT_4C_m+p\sum_{j=1}^4\tau_{p,j}\pmod{p^2}.}
\tag{BRIDGE-1}
\]
Equivalently, consuming the exact original two-seam Gosper reduction,
\[
\boxed{\frac{S_{m+1}}p\equiv
\mathcal A_m\bigl(\mathcal K_p+T_4C_m\bigr)
+p\sum_{j=1}^4\tau_{p,j}\pmod{p^2}.}
\tag{BRIDGE-2}
\]
All displayed reductions are defined in \(\mathbb Z_{(p)}\). In particular the complete original moving-rank difference has the **universal sharp valuation**:
\[
\boxed{v_p(S_{m+1}-S_m)=1,\qquad
(S_{m+1}-S_m)/p\equiv-2\mathcal A_mT_4\not\equiv0\pmod p.}
\tag{SHARP}
\]

**Proof.** Divide the exact inherited (FIVE) by p. Apply Theorem A *exactly* to the old-rank WZ seam and Theorem B to the four separately retained new-rank tails; reduction modulo p² yields BRIDGE-1. Insert (S/K) to get BRIDGE-2. The first-digit coefficient of BRIDGE-1 is the nonzero unit \(-2\mathcal A_mT_4\), and the other four contributions lie in p times a p-integral scalar after dividing by p. Therefore there can be no first-digit cancellation, proving SHARP. QED.

**Observer and source-boundary warning.** The shifted S_(m+1) is the original hypergeometric *different-rank expression*, not a new assertion that p=6(m+1)+1 stays fixed or even prime. BRIDGE-2 uses the **original** same-prime normalization S_m/p from its exact Gosper identity; it does not identify the other lane's auxiliary rank-m Cauchy carrier with the original WZ endpoint. In particular the previously proved source-vs-carrier correction \(\Xi_m\) belongs to a *different auxiliary fixed-p rank observer*; it cannot replace any of the five source-labeled ports above without a separate map. This is a rigorous positive edge map, not a no-go for the full LIFT.

## 5. Author exact rational checks and discriminating target examples

A separate standard-library Python checker reconstructs R and W independently as Fraction values, verifies the complete original five-tail Q-identity, the **exact** old-seam equality, all four normalized tail units against independently p-stripped full fractions, and both bridge equations. It passed 13 target primes p=13,19,31,37,43,61,67,73,79,97,103,127,211. The all-prime assertions above rest on the factorial proof, not on finite extrapolation.

At both requested discriminating primes, the source seam and all four WZ ports survive faithfully (entries modulo p² except the four \(\tau\), modulo p):

| p | m | \(\mathcal A_mT_4C_m\bmod p^2\) | \((\tau_1,\tau_2,\tau_3,\tau_4)\bmod p\) | \((S_{m+1}-S_m)/p\bmod p^2\) | \(S_m/p\bmod p^2\) | \(S_{m+1}/p\bmod p^2\) |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 148 | (0,5,12,9) | 148 | 144 | 123 |
| 19 | 3 | 292 | (7,0,2,16) | 45 | 134 | 179 |
| **31** | **5** | **352** | **(13,5,7,0)** | **166** | **807** | **12** |
| **211** | **35** | **36152** | **(145,178,42,82)** | **41427** | **42201** | **39107** |

At p=31, 352+31(13+5+7+0)=1127≡166 (mod 961), and 12−807≡166. At p=211, 36152+211(145+178+42+82)=130469≡41427 (mod 44521), and 39107−42201≡41427. Every sample has nonzero first-digit edge, as the universal proof requires. These are author checks, not independent review or native experiments.

**Reproducibility:** same-commit companion research_notes/portable_direct/20261024_hourly_d25_original_top_edge_wz_seam_bridge_check.py. It uses standard-library exact integers/Fraction and independent factorial-unit reconstruction; no floating precision, external API or native runtime is assumed.

## 6. Highest frontier and next executable scientific unit

**New proved author units:** (A) source-fixed exact edge WZ/Gosper seam map and its nonzero p-residue; (B) complete top-rank four-tail p² divisibility with labeled p-free unit formula; (C) full p³ top-edge bridge and universal sharp v_p=1 theorem for p>=13. **Consumed, not re-credited:** onhour original all-m WZ, original two-seam p² Gosper, onhour k<=m−1 five-port transport, source-fixed LOW/HIGH first jet, existing third-digit source/carrier defect, accepted D24 frontier. This avoids duplicating the other Research lane's current LOW seed/CM work.

**BRC/Enterprise coordinates: COMPOSE_APPLIED / REUSE_APPLIED.** Retained state is a signed rational, five-port original WZ carrier with source index labels, valuation/unit jets, the old-rank n=4m seam, and the four true new-rank tails. Future operation is cross-rank summation then a p² normalized readout. A total-only or same-rank mod-p auxiliary carrier does not factor through that operation without the exhibited repair data. No claim is made about native X6 dynamics; P000 and the current ACTIVE residual-fidelity worldview are preserved.

**Next smallest unproved step:** combine this new source-seam top-edge map with the true original first/second-digit LOW/HIGH forcing and the already proved \(\Xi_m\) source/carrier correction, without identifying their distinct rank/fixed-prime observers. Seek the precise full observer equivalence or a counter-witness at p=31/211; the lower-half seed requires source-specific CM/divided-power class and normalization. The native original benchmark, actual current-session claim/open/publish_checkpoint, independent review, and result/freeze remain unperformed. D25/LIFT parent OPEN.

**Control recovery boundary:** The last verified Research recovery request rsch20-recovery-r11-20261024-d25 (#6255) showed the lawful service Researcher session ACTIVE, preserved contributor history and no own current winning CLAIM/run/unpublished uploads. The exact continuation request rsch20-continuation-r11-20261024-d25 (#6256) returned SUCCEEDED transport but execution_authorized=false, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, and a source-specific CM normalization/representative scientific blocker. Old neutral staging was not reclassified as progress. This document performs no native session transition, claim, open, checkpoint, freeze, review, or scheduler/notification change. Support responsibility remains enterprise-math issue #1558.

**Claim status: UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT / parent OPEN.**
