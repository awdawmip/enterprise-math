# BRC N=4 G4: sharp common-decoder deficiency with a noisy BU provenance bit

Date: 2026-10-30. Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This result is an **external finite 16-leaf dual-P/Q probability-observer theorem**, not an established native P000 X6 or heartbeat physical result.

## Frozen source and lawful action

For s in AU,AV,BU,BV and j,k in {0,1}, Q(s,j,k)=q_s/4 and P(s,j,k)=q_s r_(s,j)/4. In source order AU,AV,BU,BV: q=(1/6,1/3,1/4,1/4); r_AU=(9/10,11/10), r_AV=(1/4,1/4), r_BU=(1/5,9/5), r_BV=(2,2). All 16 leaf masses under each law are positive and normalized. This is the frozen source from PR #1738, head 0552b8b067068e779b8722e1689ceaa29a33d086.

Use deterministic lawful S23-compatible G4: AV/BV stop T2 with Q; AU stops T3 with P; BU j=0 stops T3 with Q, while BU j=1 continues to T4 and stops with Q, observing the already-sampled fair k. The legal terminal outcome Y takes E, A, B3, B4Q0, B4Q1. Old compression C has atoms E,A,B, with identical P and Q masses (7/12,1/6,1/4). Within BU, P(j=0|BU)=p=1/10 and Q(j=0|BU)=1/2, while k|BU,j is fair in BOTH laws.

**Declared auxiliary noisy readout (not a native S2/S23 physical action):** At BU stage three a sensor reports Z=j XOR N, where N is Bernoulli(epsilon), independent and with the same law under P/Q, for every real 0<=epsilon<=1/2. On non-BU Z=NA. The decoder sees (C,Z), knows the public G4 and epsilon, uses one stochastic kernel under BOTH P/Q, and must preserve the observed (C,Z) when reconstructing the joint law (C,Z,Y). The terminal k is read-only; no physical k-writing operation is postulated.

Set a=p+(1-2p)epsilon and b=1-a. Then P(Z=0|BU)=a and Q(Z=0|BU)=1/2. The BU total mass is 1/4 in each law. The only binary ambiguity in Y is j, because upon decoded j=1 a shared fair-k kernel reconstructs B4Qk.

## Theorem A — sharp full-joint reconstruction for every real epsilon

For every common stochastic kernel D preserving (C,Z), define

R_joint(epsilon)=inf_D max_{L in {P,Q}} TV( L_(C,Z,Y), L_(C,Z) D ).

Then the exact attained minimax radius is

\[
\boxed{R_{\rm joint}(\epsilon)=\frac{5\epsilon(1-\epsilon)}{(9-8\epsilon)(3+4\epsilon)}}.
\tag{A}
\]

The proof is for **all real kernel parameters**, not for a finite sample.

Projection onto the indicator Y=B3 reduces any candidate decoder (including decoders producing additional Y labels) to alpha=D(B3|B,Z=0), beta=D(B3|B,Z=1) in [0,1]. Write e_P and e_Q for the BU-conditional reconstruction errors of the joint (Z, indicator Y=B3) laws. Necessarily

\[
e_P\ge |a\alpha-p(1-\epsilon)|+|b\beta-p\epsilon|,\qquad
e_Q\ge \tfrac12\bigl(|\alpha-(1-\epsilon)|+|\beta-\epsilon|\bigr).
\]

As E=max(e_P,e_Q), the positive dual combination and |x|>=x imply

\[
E\ge\frac{e_P+2a e_Q}{1+2a}
\ge\frac{a-p(1-\epsilon)-a\beta+|b\beta-p\epsilon|}{1+2a}.
\]

For 0<=epsilon<=1/2, a<=b, so f(beta)=-a beta+|b beta-p epsilon| decreases up to beta*=p epsilon/b and is nondecreasing after it. This proves the global, all-real bound

\[
 E\ge e_*=\frac{(1-2p)\epsilon(1-\epsilon)}{b(1+2a)}.
\]

Define beta*=p epsilon/b and alpha*=1-beta*-2e*. The inequalities
\(p(1-\epsilon)/a\le\alpha_*\le 1-\epsilon\) and \(0\le\beta_*\le\epsilon\)
hold throughout the interval: indeed
\(\alpha_*-p(1-\epsilon)/a=e_*/a\) and
\((1-\epsilon)-\alpha_*=(1-2p)^2\epsilon(1-\epsilon)(1-2\epsilon)/(b(1+2a))\).
The decoder emits B3 with probability alpha* for Z=0 or beta* for Z=1; otherwise it emits B4Qk with a fresh fair k. It preserves E/A exactly. Both P and Q conditional joint-TV errors equal e*. Multiplication by the BU mass 1/4 proves exact attainment and formula (A).

## Theorem B — sharp output-marginal-only radius and the joint-observation premium

If Z can be read but the fidelity target is ONLY (C,Y), with Z discarded from the output, the exact attained minimax radius is

\[
\boxed{R_{\rm marginal}(\epsilon)=\frac{\epsilon}{6+8\epsilon}}.
\tag{B}
\]

The BU-conditional P and Q errors of the binary j marginal equal
\(|a\alpha+b\beta-p|\) and \(|(\alpha+\beta)/2-1/2|\).
Their signed contrast satisfies

\[
(a\alpha+b\beta-p)-2a((\alpha+\beta)/2-1/2)
=(b-a)\beta+(a-p)\ge a-p.
\]

Thus the conditional max error is at least (a-p)/(1+2a). The common decoder beta=0, alpha=1-2(a-p)/(1+2a), with fair k on B4, attains equality. The factor 1/4 gives (B). In particular the two radii differ strictly for 0<epsilon<1/2:

\[
\boxed{R_{\rm joint}-R_{\rm marginal}
=\frac{\epsilon(1-2\epsilon)}{2(9-8\epsilon)(3+4\epsilon)}}.
\tag{C}
\]

At epsilon=1/4 they equal 15/448 and 1/32, a gap of 1/448. At epsilon=0 both vanish; at epsilon=1/2 both equal 1/20. The noisy coarse experiment has
\(TV(P_{(C,Z)},Q_{(C,Z)})=(1-2\epsilon)/10\); the complete joint (C,Z,Y) has TV=1/10.

This exact additional cost arises from preserving the correlation with the *already observed noisy provenance bit*, not from changing G4 or altering k. Hence marginal reconstruction is not a joint-observation safety certificate.

## Evidence, validity, and scope

The attached VERIFY.py uses Fraction to reconstruct all original strictly positive leaves, the (C,Z,Y) law, both optimal common decoders and their exact errors, five rational physical sensor levels with 25 kernel tests each, and 15 general-prior rational cases with 36 tests each. RUN_EVIDENCE.txt is actual captured execution output. The continuous-range claim is proven by the algebraic dual certificate and explicit achievers above, not by the finite tests.

P000/ACTIVE six-axis X6 Cell geometry, a three-dimensional layer and independently typed time are still separate correspondence obligations. The source S2/S23 legal information set, original k semantics and observer-preservation constraints remain unchanged. This is portable author-side mathematics awaiting independent review and Source-native admission.

Pinned sources: GLOBAL_KNOWLEDGE_V1 main@fc9f072ae6b5b60a58033af953da364b93388237; enterprise-math main@0569b09ef35af9ed18e9c026bae6ddfa14fd643b; earlier PR #1738 source head@0552b8b067068e779b8722e1689ceaa29a33d086; P000 source blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Authenticated GitHub actor awdawmip; native authority not granted, active owner query returned CONTROL_QUOTA. No CLAIM, Result or independent Driver review is asserted.
