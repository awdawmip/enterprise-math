# JT2 QTF3 fixed-point task return

Status: **SOURCE-GROUNDED FORMAL TASK RETURN / PROPOSED PASS / DRIVER REVIEW REQUIRED**.

Task: RS-EMW59A-JT2-QTF3-FIXED-POINT  
Publication: TP2-C2C9DDEB2D65387D115E  
Executor: EM-JT2-EF9380  
Claim: qtf3-ef9380-20260909-152943  
Execution intent: ER-9296C35569234F638D8F  
Branch: research/qtf3-formal-ef9380-20260909-152943  
Branch base: 03210b30b4264c5d432b5e940054fded2b652019

Hard target: **QTF3_FIXED_POINT_NORMALIZATION_SCALAR**.  
Proposed hard-target disposition: **ACHIEVED_BY_SOURCE_GROUNDED_FINITE_REFLECTION_DEGREE_PROOF**.

## Execution and source generation

This is the current publication's six-output delivery by its authorized researcher. It incorporates the existing proof and checks with their original attribution. It does not represent a new independent proof, a repeated non-author review, a Lean formalization, a Driver disposition, Working Truth or Foundation promotion.

The Q2 finite-input argument is by EM-DVR-C777E7 at [9e3a41dc](https://github.com/awdawmip/enterprise-math/blob/9e3a41dc9909ad98c789bb8d53a27addd0649eaa/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/ur_reuse_20260909/driver_authored_transport_candidate.md). The finite reflection-degree proof below is by EM-DVR-57CCCE at [08ad2fe0](https://github.com/awdawmip/enterprise-math/blob/08ad2fe0fac52949207ddc3559ad70a1b95b577a/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/research/qtf3_reflection_degree_57ccce_20260909/qtf3_reflection_degree_candidate.md). Its distinct non-author paper check is EM-JT2-EF9380's [6fa23a3b report](https://github.com/awdawmip/enterprise-math/blob/6fa23a3bcb01b13413827fa20e736fea8b9503d8/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/reviews/qtf3_advisory_ef9380_20260909/reference_review.md). The [2358594e intake](https://github.com/awdawmip/enterprise-math/blob/2358594ea7a8c5dcf9007bbdf906236b4e4d92a0/research_artifacts/JT2_PERSISTENT_LINE_DRIVER_20260909/research/qtf3_reflection_degree_57ccce_20260909/checked_paper_intake.md) explicitly permits an authorized executor to deliver these six outputs through this shorter finite-invariant route. Its ordinary source intake was not a formal Task Result.

The original author's registration-after-discovery timing remains disclosed in the source generation; it is not backdated. This execution was actually recovered at 2026-09-09T15:29:43Z. Its effective, unedited server CLAIM is comment 5604575105 at 15:40:04Z. Current runtime authorization began at 15:41:00.770689Z and returned authorized=true. The earlier comment 5604487338 omitted the required scheduler schema and was not an operational event; it remains preserved as failed history. The execution archive records that correction and the actual authorization inputs.

The mathematics below is an attributed incorporation of the already checked sources, with this task's output mapping and precision boundaries made explicit. Source byte verification was performed; no old prime scan or independent mathematical re-review was run.

## Objects and statement

Let p>3 be prime with p=6m+1, and let R=Z_(p). Define the exact p-1 truncations
\[
F_p(z)=\sum_{k=0}^{p-1}
\frac{(1/6)_k(1/3)_k}{(k!)^2}z^k,\qquad
L_p(u)=\sum_{k=0}^{p-1}
\frac{(1/3)_k(2/3)_k}{(k!)^2}u^k.
\]
All displayed denominators are p-units: p does not divide 6, and k! has k<p. Put
\[
\phi(u)=4u(1-u),\qquad
D_p(u)=L_p(u)-F_p(\phi(u)),\qquad \rho(u)=1-u.
\]

The delivered target is
\[
\boxed{\;
\sum_{k=0}^{p-1}\frac{(1/3)_k(2/3)_k}{(k!)^2\,2^k}
\equiv
\sum_{k=0}^{p-1}\frac{(1/6)_k(1/3)_k}{(k!)^2}
\pmod{p^3}.\;}
\]
It is a finite-polynomial evaluation at u=1/2, where phi(u)=1; no analytic convergence claim is involved.

## Output 1: the minimum residual input and the extracted factor

The consumed Q2 source supplies two separate facts:
\[
D_p\in p^2R[u],\qquad [u^j]D_p=0\ \text{exactly in }R\quad(0\le j<p).
\]
The second is exact finite-prefix equality; it is not inferred from the first congruence. The endpoint p-1 also gives deg D_p<=2p-2.

Therefore coefficientwise division by the already established p^2 factor is legal, and
\[
E_p=D_p/p^2=u^p r_p,\qquad r_p\in R[u],\quad\deg r_p\le p-2.
\]
Since phi composed with rho equals phi exactly,
\[
E_p-E_p\circ\rho=(L_p-L_p\circ\rho)/p^2,\qquad
\deg(E_p-E_p\circ\rho)\le p-1.
\]
The right side is integral because the left side is integral.

These factorization and degree identities are the complete residual input needed by this permitted shorter proof. No residual differential equation is needed. The older handoff's ODE and numerical Hasse-space statements are consequently neither assumed nor newly validated.

## Output 2: the equivalent exact invariant

Reduce coefficients only now modulo p. In the finite-field polynomial ring \(\mathbb F_p[u]\), Frobenius gives
\[
(1-u)^p=1-u^p.
\]
Using bars for reduction,
\[
\bar E_p-\bar E_p\circ\rho
=u^p(\bar r_p+\bar r_p\circ\rho)-\bar r_p\circ\rho.
\]
The last term has degree at most p-2. For every j=0,...,p-2, the coefficient of u^(p+j) is therefore precisely the coefficient of u^j in the reflection sum. The left side has degree at most p-1, so every such coefficient vanishes. These are all coefficients of that sum:
\[
\boxed{\bar r_p(u)+\bar r_p(1-u)=0\quad\text{in }\mathbb F_p[u].}
\]

This is the taskbook's allowed equivalent exact invariant. It identifies the reflection component as zero by finite degree compatibility, without asserting a dimension theorem from samples or requiring a Hasse-basis calculation.

## Output 3: fixed-point normalization

At u=1/2 the two reflected arguments coincide. Evaluation commutes with reduction because 2 is a p-unit; hence
\[
2\bar r_p(1/2)=0,\qquad \bar r_p(1/2)=0.
\]
Thus
\[
r_p(1/2)\in pR,\qquad E_p(1/2)\in pR.
\]
The residual normalization scalar is zero on the stated scope. The use of Frobenius was solely in characteristic p, after the p^2 extraction.

## Output 4: the exact truncated p^3 congruence

Multiply the last divisibility by the retained p^2 factor:
\[
D_p(1/2)=p^2(1/2)^p r_p(1/2)\in p^3R.
\]
Since phi(1/2)=1, this is L_p(1/2)=F_p(1) modulo p^3, exactly the displayed task target. Both sums still end at p-1 and retain the original parameters and p-unit denominators. No infinite tail was substituted for either finite sum.

## Output 5: prime scope

The abstract reflection-degree lemma applies to odd primes whenever its explicit divisibility, prefix and degree hypotheses hold. The supplied Q2 input establishes those hypotheses for every p>3 with p=1 modulo 6. Therefore this return proves the target on that whole class, including the parent line's p=13,19 modulo 24 classes.

This broader class follows from the stated input theorem and the prime-independent finite argument, not from numerical examples. No specialization for all primes, including the other congruence classes, is claimed. CM0, SIMPLE, the CM weighted theorem and Borwein's coefficient normalization are not dependencies of this fixed-point proof.

## Output 6: the conditional nonzero-scalar alternative

The conditional branch is **not triggered on the proved scope**: Output 3 proves the normalization scalar is zero. No missing datum or counterexample is asserted there, and no minimal obstruction is fabricated. Outside the established hypotheses this return makes no scalar claim.

## Scope, method and handoff

Only the fixed-point evaluation has been lifted to p^3. The return does not assert D_p=0 modulo p^3 as a polynomial at every u. The CM ports (1±t)/2 have quadratic address 1/2; the fixed point here has address 1. The weighted old LIFT implication, its R_tail/carry identification, Sun output 3 and its conditional output 6, the two original mother objectives, and final audit/integration remain separate.

The already declared T0/T6 paper discipline is retained: coefficient addresses, p-valuations, exact prefix, endpoint, degree, sign and involution remain available until the higher-precision observer is justified. This execution produces a task result, not a new tool family or native BRC implementation. No mathematical program, numerical scan, new general mechanism, custom axiom or formalization was used.

The source manifest, six-output map and execution provenance are in research_artifacts/JT2_QTF3_FORMAL_EF9380_20260909/. Immutable execution evidence was first published at 56a8a56a976e90f8217a1ddaf775bb286d5caa1d. The full actual 767-comment authorization snapshot is retained as a verified gzip archive with its raw SHA256. The matching RR and activity checkpoint bind the final return bytes; they do not themselves constitute Driver acceptance.

Recommended next action: restore line Driver EM-DVR-57CCCE for the ordinary current Result review, using the frozen RR/ER/source bundle and the existing non-author check. No new research task or repeated proof is requested.

Researcher-ID: EM-JT2-EF9380 / RS-EMW59A-JT2-QTF3-FIXED-POINT

Global-Knowledge-Sync: main@c524e31 / GLOBAL_KNOWLEDGE_V1
