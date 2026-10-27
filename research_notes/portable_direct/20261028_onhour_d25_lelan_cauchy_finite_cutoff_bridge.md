# D25/LIFT — original 216 series versus Le Lan (2026) Cauchy series: exact finite-cutoff bridge and boundary certificate

**At:** 2026-10-28 Asia/Hong_Kong. **Logical Research lane:** `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). **Mother:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Scientific classification:** AUTHOR-SIDE / EXACT FINITE IDENTITY PROVED / EXECUTED NINE-PRIME AND TEN-RATIONAL-COEFFICIENT CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE H0-B0 NOT EXECUTED / SOURCE REGISTER_PENDING. This is not an authorized Source CLAIM/run/checkpoint/Result.

## 1. Primary source, exact original-class match, and scope

Roman Le Lan, *Series for 1/π arising from Cauchy product*, arXiv:2604.03327v1, posted **2026-04-02**, https://arxiv.org/html/2604.03327v1 (Theorem 1, Lemma 1, equations (2.1), (3.2), (1.1), Conjecture 1).

The source proves the untruncated analytic identity via an Euler transformation and a Clausen square. In its own introduction, it **explicitly leaves the finite p-adic Cauchy-series congruence (Conjecture 1, modulo p²) unproved**. It is a distinct Cauchy series related to the Cohen–Guillera row-30 **original** 216 series, not a proof of D25 LIFT.

Set, formally over Q,

$$
A_k=\binom{2k}{k}^{2}\binom{3k}{k},\quad
d_k=\frac{A_k}{108^k},\quad
t_k=\frac{d_k}{2^k}=\frac{A_k}{216^k},\quad
b_j=\frac{\binom{2j}{j}}{8^j}.
$$

The source's Cauchy coefficients after evaluation at z=1/2 are **exactly**

$$
a_n=\sum_{j=0}^{n}b_j\,t_{n-j}.
$$

For example, the equality between this representation and Le Lan's four generalized binomial factors follows from the formal identity

$$
{}_2F_1(1/3,1/6;1;z)\,{}_2F_1(2/3,5/6;1;z)
=(1-z)^{-1/2}\,{}_3F_2(1/2,1/3,2/3;1,1;z),
$$

using Euler's and Clausen's identities. Here this is solely a formal series identity; no convergence at a p-adic unit or native X6 interpretation is implied.

Define the **different labeled finite sums**

$$
S_N=\sum_{n=0}^{N}(3n-1)a_n,\qquad
W_N=\sum_{k=0}^{N}(6k+1)t_k.
$$

The frozen D25 target is W_{p-1}, with the complete original cutoff and weight.

## 2. New proved finite-cutoff identity (all N≥0)

Write

$$
B_m=\sum_{j=0}^{m}b_j,\qquad
J_m=\sum_{j=0}^{m}j\,b_j.
$$

The exact coefficient ratio (b_m/b_{m-1}=(2m-1)/(4m)) (m≥1) proves, by induction,

$$
\boxed{B_m-2J_m=(2m+1)b_m\quad(m\geq0).}
$$

Reordering the **finite** Cauchy sum without dropping any term gives

$$
\begin{aligned}
S_N
&=\sum_{k=0}^{N}t_k\left((3k-1)B_{N-k}+3J_{N-k}\right)\\
&=\boxed{\frac12\sum_{k=0}^{N}(6k+1)t_k B_{N-k}
-\frac32\sum_{k=0}^{N}(2(N-k)+1)t_k b_{N-k}.}
\end{aligned}
$$

Denote the two terms on the last line by H_N and K_N, respectively, so **S_N=H_N-K_N exactly in Q**, before any congruence or approximation. The second summand K_N is the finite-cutoff boundary. It is not an optional p-adic error discarded by an infinite generating-function identity.

Equivalently, the exact finite transfer residue is

$$
\boxed{S_N-W_N=
\sum_{k=0}^{N}t_k\left[
(6k+1)\bigl(\tfrac12 B_{N-k}-1\bigr)
-\tfrac32(2(N-k)+1)b_{N-k}\right].}
$$

This formula is valid for every N, all p>3 after reduction modulo p^r (denominators are powers of 2,3), and preserves the signed weight, original 216 terms, all indices, convolution fibers, and full cutoff. It supplies a precise interface to investigate whether the separate finite Cauchy congruence has a provable relationship to frozen LIFT. The identity alone **does not** assert S_{p-1}=W_{p-1} modulo any particular p-power.

## 3. Exact fixed p=373 certificate

The companion `research_notes/portable_direct/d25_lelan_finite_cutoff_guard_20261028.py` uses Python standard-library exact integers. It computes the original A_k and independent Cauchy sum modulo (373^3=51895117), then checks the finite-cutoff identity.

For N=372, in Z/51895117 Z:

$$
\begin{array}{c|r}
W_{372}&373\\
S_{372}&8487242\\
H_{372}&29983232\\
K_{372}&21495990
\end{array}
$$

and (29983232-21495990=8487242) exactly as displayed. Modulo (373^2=139129),

$$
H_{372}\equiv70497=189\cdot373,\quad
K_{372}\equiv70124=188\cdot373,\quad
S_{372}\equiv373.
$$

Thus **dropping the boundary K would alter even the first surviving p-adic digit** in this original instance. At the next digit,

$$
S_{372}-W_{372}\equiv61\cdot373^2\pmod{373^3}.
$$

This is an exact counterexample to identifying the truncated Cauchy sum with the truncated 216 sum modulo p³, **not** a counterexample to the original LIFT (whose W_{372}=373 mod p³ is preserved).

The verification also performs exact rational coefficient comparisons for n=0,...,10 of both sides of the formal Cauchy identity and checks the finite bridge for p=7,11,13,19,37,43,61,211,373. Output: `PASS_D25_LELAN_FINITE_CUTOFF_BRIDGE_AUTHOR_SIDE`. The earlier general 216 computations are consumed as prior provenance, not recounted as new work. All computations are distinct from the native H0/B0 divided-power benchmark.

## 4. Source text precision audit

In the HTML source, immediately before its display (3.1)–(3.2) evaluation, the printed operator is (-1+\tfrac32 z\,d/dz), while the following displayed weighted coefficients are (3n-1) and the next line is (\tfrac32P'(1/2)-P(1/2)). The printed operator would instead multiply the z^n coefficient by (\tfrac32 n-1). The **operator consistent with the ensuing equations** is (-1+3z\,d/dz), or, at z=1/2, (-1+\tfrac32 d/dz). Our finite proof above uses direct finite sums, so it does not depend on silently adopting the inconsistent printed operator. This audit does not undermine the analytically established Theorem 1 when the operator is interpreted consistently.

## 5. BRC, X6 observer scope, and exact continuation

The native HEARTBEAT_WORLD X6 + separately typed time and P000 remain the mandatory project ontology. Here the hypergeometric and finite-field objects are **externally typed arithmetic observers**; no classical one-dimensional z-variable is declared a native X6 space or automatically promoted to full-X6 dynamics. BRC preservation carrier: original indexed (t_k), Cauchy fibers (b_jt_k), label of which finite sum is being observed, full (B_m,J_m), cutoff m=N-k and its boundary (K_N). Allowed operations: formal power-series transforms, exact finite convolution, integer binomial arithmetic, reduction modulo powers of p>3. **Unsafe quotient:** replace (B_m) by an infinite analytic value or erase K_N before proving the intended congruence factors through that quotient.

**Next lawful mathematical unit:** seek a uniformly valid p-adic reduction for H_{p-1} and K_{p-1} (both with their original exact cutoff) and determine whether their combined result connects the 2026 Cauchy conjecture to W_{p-1} modulo p²/p³. A numerical coincidence is not such a proof. The untruncated analytic identity remains a source of candidate transformations only.

**Higher-priority native work stays open:** https://github.com/awdawmip/enterprise-math/issues/1559 requires a real authorized same-original-class fixed p=373 H0/B0 divided-power evaluator, [X]U mod139129, actual rank, semilinear Frobenius direction and eta, signed Green/Hesse, original kappa and Delta_p-R_p. The new Cauchy bridge is a separate author-side paper comparison and cannot close that gate. Support path remains canonical Task owner / authorized native researcher or designated CodeX maintainer; without an accepting executor, **PENDING_OWNER / NATIVE_NOT_EXECUTED**.

**Source continuation at last actually verified receipt:** the onhour recovery request `research-onhour-20261027-0501-recovery-r13` in `awdawmip/kimi-query-bridge#6575` reports ACTIVE local session pointer but `source_authority_verified=false`, no own claim/run and no pending requests (not ownership). Dispatch request `research-onhour-20261027-0507-dispatch-r13` in #6576 ended `FAILED / TimeoutExpired`, rather than `NO_DISPATCH`. At the 2026-10-28 00:06 +0800 gateway read, the Site client was source/control READ-only, `research_authority_granted=false`, active native job quota 5/5, and `executor_binding_configured=false`. No Source role-bound mutation, claim/open, freeze or Result was made in this research unit. The old three staging files remain independently preserved; no researcher/Driver identity, source pin, or ownership is borrowed. **Next protected action:** restore a legitimate Site-bound execution credential/binding through its supported authorization path, then read current exact Source continuation and use the recovered actual owner/claim state; no reissue of the failed dispatch unless fresh canonical routing expressly authorizes it. This author note is NOT a Source-native checkpoint.

The scientific Source pin, already completed D24 UR/CM0, and original R_p remain frozen. D25/LIFT/JT2 remains OPEN. Existing hourly schedule and notifications are untouched.
