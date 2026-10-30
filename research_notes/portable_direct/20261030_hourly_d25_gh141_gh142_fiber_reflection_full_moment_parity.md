# D25/LIFT GH-141–GH-142: quadratic-fibre reflection and all-index moment parity

**Date:** 2026-10-30 Asia/Hong_Kong. **Lane:** TASK_RESEARCH, logical conversation chatgpt-research-hourly-enterprise-math-20260923; distinct from maintenance. **Mother:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). **Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## GH-141 — Full quadratic-character fibre reflection (new scope beyond GH-131)

Let K=F_(p²), p odd, q=p², e=(q−1)/2, χ the quadratic character with χ(0)=0, and c=1/4. Every element of F_p^×, including −1 and 2, is a square in K. Count distinct roots, not polynomial multiplicities:

\[
F(t)=\sum_{x\in K:\ x^2+x+t=0}\chi(x).
\]

**Theorem 1 (whole-fibre involution).** For every t in K, including 0 and c,

\[
\boxed{F(t)=F(c-t).}\tag{1}
\]

**Complete proof.** At t=0 the roots 0,−1 give F(0)=1; at t=c the single root −1/2 gives F(c)=1. For t outside {0,c}, the first quadratic has discriminant 4(c−t) and its roots have product t. If either t or c−t is a nonsquare, both fibre sums vanish: one side has no roots, or its two nonzero roots have opposite quadratic characters. If both are nonzero squares, choose a,b nonzero with a²=1−4t and b²=4t; then a²+b²=1. The two roots within each quadratic have the same character, so F(t)=2χ((a−1)/2), F(c−t)=2χ((b−1)/2). Let u=b/(1+a); the denominators below are nonzero because t is neither 0 nor c. The standard rational parametrization of a²+b²=1 yields a=(1−u²)/(1+u²) and b=2u/(1+u²), hence

\[
\frac{a-1}{b-1}=2\left(\frac{u}{u-1}\right)^2.
\]

As χ(2)=1 the two characters agree. This proves (1) without any CM point count or GH-83 assumption.

For B,y in K define g_B(x)=x²+x+B and the **labelled weighted fibre** μ_B(y)=Σ_(g_B(x)=y)χ(x)=F(B−y). Consequently

\[
\boxed{\mu_{c-B}(y)=\mu_B(-y)\quad(\forall B,y\in K).}\tag{2}
\]

This is an identity of the entire weighted pushforward distribution. For every function h:K→K, Σ_x χ(x)h(g_(c−B)(x))=Σ_x χ(x)h(−g_B(x)). It is not merely a small-index congruence.

Consume GH-124's exact definition f_B(x)=xg_B(x),

\[
S_r(B)=\sum_{f_B(x)\ne0}\chi(f_B(x))(x/f_B(x))^r,\qquad r\ge0.
\]

For nonzero g, χ(g)=g^e and x/f_B(x)=1/g; the omitted x=0 carries zero χ weight. Thus S_r(B)=Σ_(y≠0)μ_B(y)y^(e−r), with negative exponents only on nonzero y. From (2), S_r(c−B)=(−1)^(e−r)S_r(B), and e is even as q≡1 (mod 8). Therefore:

\[
\boxed{S_r(c-B)=(-1)^r S_r(B)\quad\forall B\in K,\ r\ge0.}\tag{3}
\]

The scope is **all nonnegative indices**, including the GH-129 lower-half and GH-139 upper-half ranges; the earlier GH-131 result addressed the first Lucas blind band only.

For the original target family p≥11, p≡3 (mod 8), set ρ²=2, T=2ρ/3, B₀=(1+T)/8. Then B₀^p=c−B₀, and Frobenius commutes with finite sums:

\[
\boxed{S_r(B_0)^p=(-1)^r S_r(B_0)\quad \forall r\ge0.}\tag{4}
\]

Hence even-index moments lie in F_p, and odd-index moments lie in ρF_p (zero included). At the fixed parameter B=c/2=1/8, **all odd-index moments vanish**. This does not compute the original target B₀'s odd values.

**New lower-half polynomial descent.** For 0≤r<e, GH-129 gives P_r(B)=S_r(B)=−[X^e](X²+X+B)^(e−r), degree at most e−r<q in F_p[B]. Since the two polynomials P_r(c−B), (−1)^rP_r(B) agree at every B in K by (3), they are identical polynomials. Put z=1−8B. In characteristic p≠2, parity in z forces a polynomial Q_(r,p)∈F_p[U] such that

\[
\boxed{P_r(B)=z^{r\bmod2}Q_{r,p}(z^2),\quad0\le r<e.}\tag{5}
\]

At B₀, z=−T and z²=8/9. Thus every such value descends to the single base-field invariant argument 8/9, with a labelled odd-sector factor −T. This is a structural reduction, not an independent evaluation of Q_(1,p)(8/9).

## GH-142 — Exact integer histogram and BRC orientation obstruction

For t≠0,c, F(t) is nonzero precisely when t and c−t are both nonzero quadratic residues; then F(t)=±2. The number of such t is

\[
M=\frac14\sum_{z\ne0,1}(1+\chi(z))(1+\chi(1-z))=\frac{q-5}{4}.
\]

Here Σ_(z≠0,1)χ(z)=Σ_(z≠0,1)χ(1−z)=−1 and the elementary Jacobi sum Σ_zχ(z(1−z))=−χ(−1)=−1. The latter follows by z(1−z)=[1−(2z−1)²]/4 and Σ_uχ(u²−1)=−1, obtained by counting (u−v)(u+v)=1. The exceptional t=0,c each contribute +1. Finally Σ_tF(t)=Σ_xχ(x)=0, since each x has exactly one t=−x²−x. Solving n_++n_-=M and 2n_+−2n_-+2=0 proves the **complete histogram**:

| F(t) | +2 | −2 | +1 | 0 |
|---|---:|---:|---:|---:|
| Number of t in K | (q−9)/8 | (q−1)/8 | 2 | 3(q−1)/4 |

No −1 fibres occur. The histogram is independent of B after translating t=B−y. It is not the same information as the **location-labelled** μ_B(y).

Under the operation (B,y)↦(c−B,−y) the entire labelled fibre is preserved by (2). If one identifies B and c−B while erasing orientation, even-index observations survive but odd-index queries generally do not. A concrete exact witness at p=3347 follows from the established GH-124 Hasse identity S₁=2H_p'(B)H_p(B)^p. Independently evaluating H_p(B₀)=783 and H_p'(B₀)=1351ρ by the modular multinomial expansion gives S₁(B₀)=362ρ and S₁(c−B₀)=−362ρ, distinct modulo 3347. This is a two-state readout collision, not a distinct real elliptic curve or a native P000 six-dimensional geometry theorem.

## Executed checks and evidence

Exact Python standard-library checker (author-side) uses quadratic extension pairs, nonsquare polynomial basis and three independent routes: build all integer fibres by direct x enumeration; evaluate original χ(f_B)(x/f_B)^r for a selection of B and all stated indices; and separately evaluate the p=3347 Hasse multinomial polynomial. The **complete executed source**, full terminal output and expanded proof were retained in the local portable bundle. The remotely published proof is this self-contained compressed exposition.

- Full fibre symmetry and histogram: 12 primes 3,5,7,11,13,17,19,23,31,43,59,83, testing every t (14,732 field elements), PASS.
- Direct original moment duality: p=11,19, five B each and every 0≤r≤p²−2; p=43, five B and 0≤r≤50 (2,655 direct comparisons), PASS.
- Original mark Frobenius check: p=11,19,43, PASS.
- p=3347: H=783, H'=1351ρ, S₁=362ρ and conjugate −362ρ, PASS (not an independent CM/Jacobi evaluation; no full 3347²-element sum or native p=373 experiment).
- Terminal marker: PASS_GH141_GH142_ALL_EXACT.

**BRC carrier:** (p,K,χ,B,y,root-status,multiplicity,F(B−y),r,provenance); observer: labelled μ_B and its moments; permitted operation: reflected B with reflected y. The parity quotient is lossless only for reflection-even future observables, not for unrestricted signed moments; scalar sign coincidence is not cancellation of joint branches. This external finite-field auxiliary result cannot be promoted into P000 native geometry without an explicit embedding/readout/operation-preservation bridge.

**Unfinished scientific target:** source-independent lower-half S₁(B₀) or two central moments S₈₃₇(B₀),S₈₃₈(B₀) at p=3347, and independent prediction of R₃₃₄₇(9)=0; GH-3/GH-83; D25 native H₀/B₀ divided-power, [X]U mod p², Frobenius, normalization η and native p=373. **Next:** evaluate the invariant scalar Q_(1,p)(8/9) from an independent CM/Jacobi/p-adic source, or solve the exact native LIFT second digit. Equation (5) is not itself that evaluation.

**Native control boundary on this turn:** Gateway v0.6.11 reports research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, Source CODE_REVIEW_REQUIRED; one exact D25 continuation read returned INVALID_ARGUMENT / CONTROL_QUOTA. No service session, winning claim, authorized run or Source checkpoint established; old pending native requests/staging untouched. Support remains EM #1558 and #1559. Portable GitHub evidence does not count as canonical predecessor completed_units, Result, review or Source checkpoint.