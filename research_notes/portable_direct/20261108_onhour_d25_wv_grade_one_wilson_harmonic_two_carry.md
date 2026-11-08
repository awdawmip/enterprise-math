# D25: Original 216/2304 first-grade Wilson–harmonic lift and two-digit transport

Date: 2026-11-08 (Asia/Hong_Kong). Author-side mathematical work; independently unreviewed, not Source-admitted and not the native H0/B0 experiment.

Frozen task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923.

## Starting original series

For prime p>3 and 0<=n<p write

\[
w_n=(6n+1)\frac{(2n)!(3n)!}{(n!)^5\,216^n},\qquad
v_n=(8n+1)\frac{(4n)!}{(n!)^4\,2304^n}.
\]

Grade j means the p-adic valuation of the **coefficient before the optional linear weight**. Preserve model, source index, signed weight and grade as the BRC residual carrier, and combine only at the declared modulo-p^3 observer.

Earlier exact research proved the W grade-two tail's all-prime signed finite hypergeometric representation (20261108_onhour_d25_w216_grade2_allprime_character_kernel.md). The V grade-two tail **aggregate** vanishes mod p^3 by a source-derived corollary of the double-truncation theorem in Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, https://arxiv.org/abs/1803.01830 (prior author-side note 20261108_onhour_d25_2304_grade2_tail_universal_zero.md). The original missing arithmetic port for cross-grade transmission is the first-grade digit modulo p^2.

## Theorem 1 — first-grade correction, for every prime p>3

Define the Wilson quotient and harmonic residues in the p-local integers:
\[
\omega_p=((p-1)!+1)/p\pmod p,\quad H_a=\sum_{j=1}^a 1/j\pmod p,\quad H_0=0.
\]
For every 0<=a<p,
\[
\boxed{\frac{(p+a)!}{p}\equiv-a![1+p(H_a-\omega_p)]\pmod{p^2}.}\tag{1}
\]
Proof: split the factorial at p. The quotient is
\((p-1)!\,a!\prod_{j=1}^a(1+p/j)\).
Use \((p-1)!=-1+p\omega_p\) and the product expansion modulo p^2. QED.

Define the exact original first-grade intervals
\[
I_W=\{\lceil p/3\rceil,\ldots,(p-1)/2\},\qquad
I_V=\{\lceil p/4\rceil,\ldots,(p-1)/2\}.
\]
For n in I_W let \(a_W(n)=3n-p\) and
\[
B_W(n)=-(6n+1)\frac{(2n)!\,a_W(n)!}{(n!)^5\,216^n}.
\]
For n in I_V let \(a_V(n)=4n-p\) and
\[
B_V(n)=-(8n+1)\frac{a_V(n)!}{(n!)^4\,2304^n}.
\]
All denominators are p-units. Put \(W_1=\sum_{I_W}w_n\), \(V_1=\sum_{I_V}v_n\). Then for X=W,V:
\[
\boxed{\frac{X_1}{p}\equiv
\sum_{n\in I_X}B_X(n)+
p\left(\sum_{n\in I_X}B_X(n)H_{a_X(n)}
-\omega_p\sum_{n\in I_X}B_X(n)\right)\pmod{p^2}.}\tag{2}
\]
Proof: in I_W, 0<=3n-p<p and 2n<p, so (3n)! has exactly one p and the other factorials are units; apply (1) termwise. In I_V, use (4n)!, with 0<=4n-p<p and n<p. Sum the termwise congruences. QED.

Equation (2) is a full p^2 precision original-model evaluator of the first-grade quotient. It retains two separate source ports: local harmonic residue and global Wilson quotient.

## Theorem 2 — exact BRC carry criterion and lower-grade obstruction

Let W_j,V_j be the original grade-j sums, reduced mod p^3. All higher-grade terms vanish at this observer, and the **aggregate** V_2=0 mod p^3 by the cited published theorem. Whenever W_0=V_0 mod p, define
\[
c_0=(W_0-V_0)/p\pmod{p^2},\quad
c_1=(W_1-V_1)/p\pmod{p^2},\quad
\tau=W_2/p^2\pmod p.
\]
By direct algebra,
\[
\boxed{W_p\equiv V_p\pmod{p^3}
\iff c_0+c_1+p\tau\equiv0\pmod{p^2}.}\tag{3}
\]
The equivalent ordered digit tests are \(c_0+c_1=0\pmod p\), followed by
\((c_0+c_1)/p+\tau=0\pmod p\). The quotient in the second test is formed after the first. This is a **conditional equivalence**, not a proof of the universal W/V congruence.

Exact original p=13 values modulo 2197:
\[
(W_0,W_1,W_2)=(780,1937,1690),\qquad
(V_0,V_1,V_2)=(325,1885,0).
\]
Thus c0=35, c1=4, tau=10 and \(35+4+13\cdot10=169\).
In particular \(W_0-V_0=455=13\cdot35\not\equiv0\pmod{13^2}\).
**This is an exact counterexample to any candidate identifying the original grade-zero W/V ports modulo p^2 separately.** It strengthens the earlier grade-two diagonal-map obstruction: compensation must begin between grade zero and grade one, and again at the next digit. It does not refute a triangular or source-mixing transformation.

Exact original p=373 values modulo 51895117:
\[
(W_0,W_1,W_2)=(28094360,38687933,37008314),\quad
(V_0,V_1,V_2)=(45069217,6826273,0).
\]
Thus (c0,c1,tau)=(93620,85420,266), and
\(93620+85420+373\cdot266=278258=2\cdot373^2\).
The independently computed first-grade Wilson/harmonic residues are:
- W: X1/p=103721; base=1892 mod 139129; harmonic coefficient=353 mod 373; Wilson coefficient=293; omega=224.
- V: X1/p=18301; base=104091 mod 139129; harmonic coefficient=297 mod 373; Wilson coefficient=219; omega=224.

These yield c1=85420 without collapsing the underlying source-index ports.

## Validation, scope, remaining interface

The companion checker executed standard Python integer arithmetic over all 301 primes 5<=p<=2000: **602 exact direct-original-binomial versus Wilson–harmonic congruence tests modulo p^2, all passed**. The p=5,11,13,19,373 two-stage witnesses were independently recomputed modulo p^3. General Theorem 1 follows from (1), while Theorem 2 is an algebraic equivalence; the finite observations do not establish a universal W/V equality.

BRC: COMPOSE_APPLIED, using a signed valuation/index carrier and two ordered carry readouts (not positive-mass branching). No independent mathematical review, Foundation promotion, or claimed native run.

Open mother target: Delta_p-R_p=0 mod p and W_p=p mod p^3 for p mod24=13,19. Next exact portable proof unit: derive an independent closed formula for c0 from original grade-zero terms and test its cancellation with equation (2) and the existing signed finite 3F2 tail; include p13,p19,p373 discrimination.

Native highest-priority unfinished evidence remains Issue #1559: original p373 same-class H0/B0 divided-power [X]U mod139129, rank, actual semilinear Frobenius/eta, signed Green/Hesse kappa, Delta-R, and independent reproduction. Responsible path: authorized Source owner/native evaluator or assigned Codex maintainer; PENDING_OWNER/NOT_EXECUTED. The present original-binomial diagnostic is not the native benchmark.

2026-11-08 Source readback of original request onhour11-20261106-1400-exact-research-lane-continuation returned RUNNING/REVALIDATING (collected=1233, verified_through=4, next_page=5, formal_task_created=false). Site is CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false; a subsequent status read failed BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false). Native Researcher session/CLAIM/run NOT_VERIFIED; no Source checkpoint or Result/Review written. Historical staging remains separate. Author-side checkpoint only; no borrowed maintenance lane.
