# D25 / SECOND-DIGIT-LIFT: B2304 Clausen cutoff, residue-dependent Frobenius carry, and a derivative observer obstruction

Research date: 2026-10-29 Asia/Hong_Kong.
Status: AUTHOR-SIDE / EXACT FINITE-RING THEOREMS / EXECUTED 41-PRIME CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Canonical Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Task publication: TP2-B6F4FC938FF94941C1B7.
Immutable scientific Source pin (not rebased): c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923. Maintenance conversation remains a distinct lane.
Proof and original integer script in this research note are author-side, not a formal Source Result, native run, independent review, or new task publication.

## I. Original B2304 model and classical formal Clausen identity

Let p>3 be prime and define beta_n=(1/8)_n(3/8)_n/(n!)², gamma_n=(1/4)_n(1/2)_n(3/4)_n/(n!)³ and theta=z(d/dz). Set C_p(z)=sum_{n=0}^{p-1} gamma_n z^n.

The **original** 2304 weighted sum is exactly

\[
B_p=[(1+8\theta)C_p(z)]_{z=1/9}
=\sum_{n=0}^{p-1}(8n+1)\frac{\binom{2n}{n}^2\binom{4n}{2n}}{2304^n}.
\]

This equality follows coefficientwise from gamma_n 9^{-n}=binom(2n,n)^2 binom(4n,2n)/2304^n. Clausen's classical, previously known formal identity over Q is

\[
{}_2F_1(1/8,3/8;1;z)^2={}_3F_2(1/4,1/2,3/4;1,1;z).
\]

Classical identity reference: https://dlmf.nist.gov/16.12.E2 .
The new target-specific work is its exact *finite truncation and observer semantics*.

## II. First theorem: coefficientwise p² square after correct degree cutoff

Restrict p to p ≡ 3 or 5 (mod 8), covering the task's two frozen prime classes 19 and 13 (mod 24). Put

\[
b=\begin{cases}(3p-1)/8,&p\equiv3\pmod8;\\(7p-3)/8,&p\equiv5\pmod8,\end{cases}\qquad
K_p(z)=\sum_{n=0}^{b}\beta_n z^n.
\]

Denote by Pi_<p the operation retaining the original source-indexed polynomial terms of degree strictly below p.

**T1 (proved, full polynomial)**:
\[
\boxed{C_p(z)\equiv\Pi_{<p}(K_p(z)^2)\pmod{p^2}.}
\]

Proof. For the indicated residue classes, each of the factors (1/8)_n and (3/8)_n has one p-factor for b<n<p, so beta_n is 0 mod p² on that range, and n! remains a p-unit. The exact formal Clausen coefficient identity then applies for every original degree n<p, and replacing the two infinite companion series by K_p loses only terms divisible by p² in the preserved degree range. This is a coefficientwise proof; it neither uses numeric fitting nor redefines the original cutoff.

**Crucial class split**: for p≡3 mod8, 2b=(3p-1)/4<p, and hence the full, unprojected polynomial statement C_p≡K_p² (mod p²) is valid. For p≡5 mod8, the degree cutoff cannot be removed, even modulo p, as T2 establishes. This distinction applies respectively to the target classes p≡19 and p≡13 (mod24).

## III. Second theorem: a complete Frobenius carry polynomial

For p≡5 mod8 let

\[
a=(5p-1)/8,\quad t=(p-1)/4,\quad b=(7p-3)/8=a+t,\quad 2a=p+t.
\]
\[
Q_p(z)=\sum_{i=0}^a\binom ai\binom bi z^i,\qquad
T_t(z)=\sum_{r=0}^t\gamma_r z^r\pmod p.
\]

Reduction of the original coefficient beta_i shows K_p≡Q_p (mod p). The **exact whole high-degree remainder** is

\[
\boxed{K_p(z)^2-C_p(z)\equiv -z^p T_t(z)\pmod p\quad\text{in }\mathbb F_p[z].}\tag{T2}
\]

In particular [z^p]K_p²≡-1 modp universally for this class: an unprojected Clausen square is impossible already modulo p. The carry is a polynomial-source effect, not an artificial change in the original B2304 model.

**Proof of all high-degree coefficients.** Put L=binom(b,a) and Q*(z)=z^a Q_p(1/z). Reversing exact binomial coefficients yields

\[
Q^*(z)=L\cdot {}_2F_1(-a,-a;t+1;z),
\]
where the hypergeometric polynomial terminates at degree a. Since -a≡1/8 and t+1≡3/4 modp, the classical Clausen identity can be applied modp to its coefficients of degrees k=0,...,t (all displayed denominators are units). Define

\[
d_k=\frac{(1/4)_k^3}{(1/2)_k(3/4)_k k!}.
\]
Then [z^k](Q*)²≡L²d_k for k≤t. Degree reversal at total degree 2a=p+t gives
\[
[z^{p+r}]Q_p^2=[z^{t-r}](Q^*)^2\equiv L^2d_{t-r}\quad(0\le r\le t).
\]
The exact ratio d_{k-1}/d_k=((k-1/2)(k-1/4)k)/(k-3/4)^3, substituted at k=t-r+1≡3/4-r modp, gives
d_{t-r}/d_t≡gamma_r. The remaining constant can be evaluated without any conjectural step: at degree p of the **complete rational Clausen identity**, modulo p only its endpoint coefficients 2beta_p and the pairs with both 1≤i,p-i≤a survive, so L²d_t≡gamma_p-2beta_p modp.

For each rational parameter s/d with 0<s<d and p∤d, choose 1≤ell≤d with ell*p≡s mod d. Wilson's factorial reduction gives ((s/d)_p)/p!≡ell/d (modp). When p≡5 mod8 it evaluates beta_p≡(5/8)(7/8)=35/64, gamma_p≡(1/4)(1/2)(3/4)=3/32. Thus gamma_p-2beta_p=-1 exactly, proving [z^{p+r}]Q²≡-gamma_r. Degrees greater than p+t in Q² do not exist; high coefficients contributed by p-divisible beta_i in K² vanish modp. Low degrees follow T1. Therefore T2 holds for **every** p in the class.

No novel general Clausen identity is claimed; T1/T2 are explicit finite-ring and cutoff theorems for this Task's original B2304 object.

## IV. Third theorem: the weighted derivative detects a lossy quotient

Apply the original operator 1+8theta to T2 *before* evaluating at w in F_p. As theta(z^p T_t)≡z^p theta(T_t) modp, and w^p=w, we obtain

\[
\boxed{
[(1+8\theta)C_p]_{w}\equiv
[(1+8\theta)K_p^2]_{w}
+w[T_t+8\theta T_t]_{w}\pmod p.}\tag{T3}
\]

The quotient z^p=z is valid for scalar functions evaluated on F_p, but does NOT commute with theta in the polynomial source algebra. Replacing z^p by z *before* applying theta gives an incorrect extra 8wT_t(w). This is a genuine BRC-style loss of the degree/provenance port, not mere notation.

Exact pointwise witnesses for the admissible future observer operation:
- p=373, w=2: T_t(2)=36, theta T_t(2)=263. Correct carry 2(36+8*263)=177 mod373; illegal quotient-first derivative gives 2(9*36+8*263)=7 mod373.
- p=13, w=2: correct carry 12, illegal quotient-first carry 3.

For the original scalar w=1/9 some finite CM instances happen to have a vanishing carry; do not turn that observation into a polynomial equality or full-p proof. The witness concerns the stated observation family, not a claim of nonzero scalar discrepancy at w=1/9.

**Actual BRC application.** Carrier is the typed family (p, i, j, beta_i, beta_j, i+j, v_p, source branch). Future operations are Pi_<p, weighted theta, then scalar readout at w. Quotienting z^p to z prematurely erases the degree identity that theta consumes. T2 supplies the exact repair coordinate, with pair/source signs retained; result is external finite-ring mathematics, not a native X6 spatial or H0/B0 theorem. BRC resolution: COMPOSE_APPLIED (source-preserving observer and residual).

## V. Reproducible exact arithmetic

Actually executed Python standard-library-only program:
research_notes/portable_direct/d25_b2304_frobenius_carry_guard_20261029.py
Git blob sha1: 6ab50412b2c7a88365d6877e939974b6c4d01755.
Immutable commit for program: b2495e9b3ee004ee068b296ab4d129727a218d14.

The code checks T1 coefficientwise modulo p² and T2 coefficientwise modulo p, the weighted T3 at w=1/9, and at p=13,373 an independent chosen observer w=2. The prime sample is every p<400 satisfying p≡3,5 mod8: 41 primes total, 19 and 22 respectively. Actual output (selected):

    OBSERVER_FROBENIUS_LOSS 13 10 6 12 3
    OBSERVER_FROBENIUS_LOSS 373 36 263 177 7
    PASS_D25_B2304_FROBENIUS_CARRY 41 primes <400; mod p² coefficientwise; mod p exact high-tail
    GROUP_COUNTS {'p_mod_8_3': 19, 'p_mod_8_5': 22}
    P_EXACT ('5', 13, 11, 3, 0, 0, 0, 0)
    P_EXACT ('3', 19, 7, 0, 0, 0, 0, 0)
    P_EXACT ('5', 373, 326, 93, 0, 0, 0, 0)

At p=373: a=233, b=326, t=93 and the first six coefficients of the carry [z^{373+r}]K² for r=0,...,5 are (372,268,209,77,183,68) modulo 373, each the negative of gamma_r. The scalar instances give B_p≡0 (modp); they are **finite regression evidence**, not a universal CM/Hasse theorem or native benchmark. T1–T3 stand on the separate algebraic proofs above.

## VI. Status, unchanged benchmark, next exact scientific work

The *actual canonical native H0/B0* fixed p=373 divided-power [X]U mod 139129 is still unexecuted in this lane. The same-original-class experiment must retain actual module rank, semilinear Frobenius direction/normalization eta, signed Green/Hesse ports, original kappa and Delta_p-R_p. Existing support: https://github.com/awdawmip/enterprise-math/issues/1559 ; at this read OPEN, no responsible assignee, PENDING_OWNER. Responsible action is for authorized original-class executor/Codex native implementation owner to execute and publish exact code/pins/input/output for independent review. The scalar Clausen/finite-field derivation does not satisfy its acceptance.

Previous A216 author-side Clausen and p³ cutoff repair at commit 996de464c253d08520c7c5d0e5c814c676cd9777 is consumed, not redone. Earlier 781-prime A/B comparisons, 216 reflection and composite falsifiers retain their original finite/conditional evidence grades. **Smallest next algebraic unit**: retain and lift the B2304 carry polynomial through the required p² precision and compare, with original weighted observer and cutoff, against A216's p³ source-preserving correction to decide p≡13,19 mod24 all-prime A/B modp³ bridge. Do not replace formal z^p by z before theta. No full bridge theorem is asserted.

The last historically verified own recovery bridge request research-onhour-20261027-0501-recovery-r13 (Issue #6575) showed no own winning Source claim/run, only a nonauthoritative session pointer and neutral staging archive. Prior dispatch research-onhour-20261027-0507-dispatch-r13 (Issue #6576) ended FAILED/TimeoutExpired. Read/reconcile original IDs when authorized; do not blind-reissue. Current Sites reports Researcher authorization false, write_relay_enabled false; native job quota reported 5/5. This evidence has been preserved as an authorized author-side GitHub proof/code pair, not source-native checkpoint, accepted Result, registered research activity, formal review or native computation.

Next restore action when permissions genuinely change: use the **Research** conversation ID and current Source continuation, check actual claim CAS before any native mutation, keep maintenance identity separate, never rebase scientific pin or duplicate accepted results. No scheduler/Actions/hosted cron was introduced; no automation controls modified.