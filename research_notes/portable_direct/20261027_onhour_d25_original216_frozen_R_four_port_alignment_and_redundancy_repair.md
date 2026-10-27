# D25 / SECOND-DIGIT-LIFT — original frozen R is exactly the new Clausen boundary; repair the redundant five-observer claim

Date: 2026-10-27 Asia/Hong_Kong. Requested TASK_RESEARCH research-onhour logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; never the separate \`chatgpt-hourly-enterprise-math-20260921\` maintenance lane. Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`. Publication: \`TP2-B6F4FC938FF94941C1B7\`. Frozen science pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (unchanged).

**Evidence class:** AUTHOR-SIDE / EXACT ALGEBRAIC ALIGNMENT (using previously proved and explicitly sourced high-coefficient reflection) / 11 EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED. This new unit *corrects an overstrong necessity statement in the immediately preceding five-observer author note* and consumes, rather than repeats, earlier frozen R and reflected-tail work. Neither this note nor its code is a Source-native TASK checkpoint, Result, review or CLAIM.

## 1. Exact original quantities

Let \`p=6m+1>3\` be prime. Work in the localization \`Z_(p)\`, with all congruences modulo their displayed powers. Use the **unchanged original** original-weighted-216 sum and the Gauss Clausen coefficients
\[
t_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2},\qquad
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}n^2\binom{3n}n}{216^n}.
\]

The preceding author note at \`research_notes/portable_direct/20261027_onhour_d25_original216_clausen_p3_boundary_five_observer_certificate.md\` defined
\[
D=\sum_{k=0}^{2m}t_k,\quad E=\sum_{k=0}^{2m}k t_k,\quad
J=\sum_{k=0}^{m}k t_k,\quad C=\sum_{k=2m+1}^{p-1}t_k,
\]
\[
H=\sum_{k=5m+1}^{p-1}t_k\sum_{j=p-k}^{m}(6(k+j)+1)t_j.
\]
It proved the exact local formula
\[
W_p\equiv D^2+12DE+12JC-2H\pmod{p^3}.
\tag{A}
\]
The original **frozen** reflected cutoff (not an observer invented here) is
\[
Q_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}(6(i+j)+1)t_it_j,\quad
R_p=2\sum_{i=1}^{m}t_i
       \sum_{a=1}^{i}(1+6(i-a))C_a\pmod p,
\]
where \[
C_a=\frac{2^{a-1}((a-1)!)^2}{18(5/6)_a(2/3)_a}.
\tag{B}
\]
**Precise historical source:** \`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md\` at the frozen scientific Source commit above, directly reread this run. Its original plus-class domain is \`p≡13,19 (mod24)\`. Extending the same finite expression for \`R_p\` to other \`p≡1 (mod6)\` is solely a diagnostic definition; it does not enlarge the original Task or accepted theorem.

The already author-proved reflected-coefficient lemma from \`research_notes/portable_direct/20261025_onhour_d25_clausen_three_band_local_jet_joint.md\` and source-port alignment at \`research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md\` states, for \`1≤a≤m\`,
\[
\frac{t_{p-a}}{p^2}\equiv C_a\pmod p.
\tag{C}
\]
The exact recurrence for both sides is \`v_1=1/10\`, \`v_{a+1}=36a²v_a/((6a+5)(3a+2))\`; its denominators in this range are p-units. This unit reuses that coefficient lemma with its existing provenance.

## 2. New correction: TWO safe observer compressions

**Theorem 1 (signed cutoff / frozen R alignment).** For all primes \`p≡1 (mod6)\`, the *unmodified full-degree cutoff* and the *new high/low Clausen boundary* obey
\[
\boxed{Q_p\equiv 2H\pmod{p^3}.}
\tag{1}
\]
For the frozen target classes, the original scalar \`R_p\` in (B) consequently satisfies
\[
\boxed{\frac{Q_p}{p^2}\equiv \frac{2H}{p^2}\equiv R_p\pmod p.}
\tag{2}
\]

**Proof.** The coefficient ratios give the exact valuation bands \`v_p(t_k)=0\` for \`k≤m\`, \`1\` for \`m<k≤2m\`, and \`2\` for \`2m<k<p\` (two exact numerator p-factors, denominators p-units). In the defining condition \`i+j≥p\` of \`Q_p\`, both \`i,j≤2m\` is impossible because \`i+j≤4m<p\`. If one index is high (\`>2m\`) and the other is middle (\`>m\`), the product valuation is at least 3; two highs have valuation at least 4. Thus modulo \`p³\` the **only surviving terms** are ordered pairs of exactly one high and one low (\`≤m\`), with the exact cutoff \`j≥p-k\`. Those are precisely the two orders of \`H\`; signs and degree weights are unchanged. This proves (1).

For (2), let \`a=p-k\`. The allowed \`k≥5m+1\` implies \`1≤a≤m\`. Reduce \`6(k+j)+1\` modulo \`p\` to \`1+6(j-a)\`, divide the p² factor and apply the *previously proved* reflection (C). Then
\[
\frac H{p^2}\equiv
\sum_{a=1}^{m}C_a\sum_{j=a}^{m}(1+6(j-a))t_j
=\sum_{j=1}^{m}t_j\sum_{a=1}^{j}(1+6(j-a))C_a
=\frac{R_p}{2}\pmod p.
\]
The division \`H/p²\` is integral, as each high factor has valuation 2. The final equality is the frozen formula (B), with no sign reversal or altered cutoff. QED.

**Theorem 2 (the Gauss moments J and E alias only at the required observer precision).** Every \`p≡1 (mod6)\` satisfies
\[
\boxed{E-J=\sum_{m<k≤2m}k t_k\equiv0\pmod p.}
\tag{3}
\]
Because \`C∈p² Z_(p)\`, one may *safely* replace \`JC\` by \`EC\` **only** modulo \`p³\`. Hence the five-object representation (A) can be written
\[
\boxed{W_p\equiv D^2+12DE+12EC-Q_p\pmod{p^3}.}
\tag{4}
\]
This is a proved sufficient compression in the exact declared observer; no claim of globally minimal BRC dimension or of an X6-native embedding is made.

The preceding five-observer note stated that **all five coordinates were essential**. That claim is **too strong** for the displayed second-digit observer: \`j=J mod p\` is already determined by \`e=E mod p²\` reduced modulo p, and \`h=H/p² mod p\` equals \`R_p/2\`, a *previously fixed, provenance-bound* original Task observable. Retaining **R itself** is necessary; this correction does not set R to zero or license ignoring the signed cutoff. In particular the p² precision for E and D/p remains binding.

## 3. Direct original Source-port formula — smaller current proof obligation

Now restrict to the **frozen target** primes \`p≡13,19 (mod24)\`. Reuse the *previously accepted* CM0 zero \`D≡0 mod p\` (derived from the low Legendre zero) and first-digit congruence \`W_p≡p mod p²\`. Define
\[
r=(D/p)\bmod p^2,\qquad e=E\bmod p^2,\qquad
c=(C/p^2)\bmod p,\qquad R=R_p\bmod p.
\]
The original Gauss scalar \`M=Σ_{k<p}t_k=D+C\`, \`N=Σ_{k<p}k t_k\`. Because \`C∈p²Z_(p)\` and \`N−E∈p²Z_(p)\`, one has
\[
M/p\equiv r+pc\pmod{p^2},\qquad M+12N\equiv pr+12e\pmod{p^2}.
\]
The *frozen original* observable is \(\Delta_p=[((M/p)(M+12N)-1)/p]\bmod p\). Its quotient is legal because accepted UR gives \`12re≡1 mod p\`. Thus direct multiplication proves
\[
\boxed{\Delta_p\equiv
 \frac{12re-1}{p}+r^2+12ec\pmod p.}
\tag{5}
\]
Combine the original Source scalar \`R_p\` and (2):
\[
\boxed{
\Delta_p-R_p\equiv\frac{12re-1}{p}+r^2+12ec-R_p
             \equiv\frac{W_p-p}{p^2}\pmod p.}
\tag{6}
\]
These identities are exact p-local algebra at the specified precisions, consuming existing CM0/UR and earlier reflection results; they **do not** prove that the right-hand side is always zero.

Equation (6) repairs the earlier five-observer overstatement with **four typed ports \`(r,e,c,R)\`**, of which \`R\` is the already-frozen Source observer; only \`(r,e,c)\` need be newly evaluated from this Gauss representation. The unclosed D25/LIFT mathematical obligation is precisely
\[
\boxed{\frac{12re-1}{p}+r^2+12ec-R_p\equiv0\pmod p}
\tag{7}
\]
for *every* p in both frozen classes. Future proof must control the nonzero high-tail contribution \`12ec\` together with original \`R_p\`; reducing a signed expression to its norm, erasing \`R_p\`, or discarding the p² tail would change the target.

## 4. Executed independent exact certificates

A standard-library integer program executed at this run (11 primes, two different original representations and direct double enumeration of the signed cutoff). New readback-verifiable executable file:

\`research_notes/portable_direct/d25_onhour_frozen_R_four_port_source_alignment_20261027.py\`, initially published in project commit \`ce460bfe4854bac10d712b39b833bee2455260f5\`, Git blob \`a0c488a9ec2ee9070b8f8d7628a22192408c15f6\`.

Coverage: target \`13,19,37,43,61,67,211,373\`, controls \`7,31,73\`. All 11 checked the **unconditional** \`Q≡2H mod p³\`, independently recomputed frozen \`R\` with (B) recurrence, checked \`Q/p²=R=2H/p² modp\` and verified the exact Clausen weighted original sum \`W=M(M+12N)−Q modp³\`. Only the 8 target primes invoked CM0/UR to check equation (5)/(6) and the full four-port obstruction. All assertions passed; these finite cases check implementation, **not** an all-prime zero proof.

| p | \`R_p mod p\` | \`H/p² mod p\` | \`12ec mod p\` | \`Δ_p mod p\` | \`(W_p-p)/p² mod p\` |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 9 | 0 | 0 |
| 19 | 12 | 6 | 6 | 12 | 0 |
| 37 | 11 | 24 | 10 | 11 | 0 |
| 43 | 15 | 29 | 3 | 15 | 0 |
| 61 | 3 | 32 | 46 | 3 | 0 |
| 67 | 21 | 44 | 51 | 21 | 0 |
| 211 | 119 | 165 | 110 | 119 | 0 |
| 373 | 196 | 98 | 197 | 196 | 0 |

At the frozen diagnostic p=373, all divisions and modulo operations were performed in integer modular arithmetic:
\[
(r,e,c,R)=(110805,108837,252,196),\quad
\frac{12re-1}{373}\equiv169,\quad r^2\equiv203,\quad12ec\equiv197,\quad -R\equiv177.
\]
Thus the exact source original \(\Delta_{373}=169+203+197=196\bmod373\) and \(\Delta_{373}-R_{373}=0\bmod373\), as independently found from \`W_373≡373 mod373³\`. The two high-observer values \`12ec=197\` and \`R=196\` are individually nonzero. This identifies **which** earlier five coordinates can be compressed and which signed residuals cannot.

Controls p=7/31/73 verify the algebraic cutoff alignment; the frozen CM0 zero premise does not hold there, so the target-class four-port reduction was not asserted for those primes.

## 5. Science frontier, provenance, and handoff

**Meaningful advance:** Correct the inaccurate necessity claim from the preceding author five-observer certificate; prove an observer-preserving compression into four fields including the *original frozen* signed cutoff; directly reconstruct the genuine original \`Δ_p\` rather than asserting a fitted correspondence. No reproof of frozen UR, CM0, the full previously proved reflection recurrence, previous third-digit finite tests or other lanes' results is credited. The D25 zero theorem remains open.

**Highest independent native acceptance debt:** existing \`awdawmip/enterprise-math#1559\` (as inspected 2026-10-27) is OPEN / PENDING_OWNER / NOT_EXECUTED. It requires a lawful executor to run the **unchanged same-original-class H0/B0 divided-power benchmark** at p=373 and return actual \`[X]U mod139129\`, module rank, semilinear Frobenius direction/eta, complete signed odd Green/Hesse, original κ, Δ−R, raw versioned runner/evidence, and independent validation. The present paper/code are a portable classical-p-adic **author-side proof**, not that experiment or its Source Result.

**Exact next action:** obtain a bona fide native H0/B0 runner/authorized executor through existing #1559; execute the original fixed object and bind real output to frozen source, retaining all signs and operator normalization. In parallel only if a distinct authorized canonical portable unit becomes available, use (7) to seek a single uniform relation linking \`c\` with the original \`R_p\` at their retained p-adic precision. Do not repeatedly append new redundant Clausen controls as substitutes for the native evidence.

**Control handoff:** logical conversation \`chatgpt-research-onhour-enterprise-math-20260923\`. Historical own recovery request \`research-onhour-20261027-0501-recovery-r13\` (#6575, SUCCEEDED) projected an ACTIVE session without Source-verifiable own claim/open. Original own dispatch \`research-onhour-20261027-0507-dispatch-r13\` (#6576) definitively FAILED/TimeoutExpired, not NO_DISPATCH. Later own exact continuation \`onhour-20261027T1705-D25-exact-continuation\` SUCCEEDED/read-only with \`execution_authorized=false\`. Site scope on 2026-10-27 is read-only with \`research_authority_granted=false\` and active native control quota 5/5; one attempt to read the old GitHub-bridge request ID via native \`control_result\` returned scope \`CONTROL_REQUEST_NOT_FOUND\`, so no reissue. Own claim/run/request of current native execution: **none Source-verified**. Former staging remains neutral and separately attributed. This author's GitHub documentation is **not** an official \`publish_checkpoint\` or authenticated Source continuation. Formal activity registration, native execution and independent review remain pending. This note changes no Source pin, owner, scientific taskbook, Source result or scheduler.
