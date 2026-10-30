# D25/LIFT GH-148–GH-149 — Even trace-square quotient and independently counted CM anchor

2026-10-30; author-side portable research for logical Research lane chatgpt-research-hourly-enterprise-math-20260923, **not** the maintenance lane. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. P000 ACTIVE_LOCKED. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Input facts, strength and carrier

Reuse GH-131 (Hasse reflection) and GH-146/147 (marked ordinary elliptic trace line), at their **author-only** strength. Let p=8m+3>=11 prime, N=(p-1)/2=4m+1, rho^2=2 in F_(p^2), and H(B)=[X^N](X^2+X+B)^N in F_p[B]. Known: deg H<=2m and H(1/4-B)=H(B). Let B(v)=1/8+rho*v and v0=1/12, so B0=B(v0). The reduced integer Frobenius trace of E_B:y^2=x^3+x^2+Bx at B(v) is H(B(v))^2. GH-147 also proves S1(B0)=rho^(-1) d/dv [H(B(v))^2] evaluated at v0. These are auxiliary finite-field observer interfaces, not native P000 spatial theorems.

## GH-148 (proved): even-square trace compression

There is a unique G_p(W) in F_p[W] of degree at most m such that, as a polynomial identity,

    H(1/8+rho*v)=G_p(v^2).

Consequently the **whole labelled trace line** satisfies

    a_(p^2)(E_(1/8+rho*v)) mod p = J_p(v^2),  J_p(W)=G_p(W)^2,
    deg J_p <= 2m=(p-3)/4.

Proof: reflection gives k(v)=H(1/8+rho*v)=k(-v). The coefficientwise pth power sends rho to -rho, so k(v)^p=k(-v)=k(v); each coefficient of k belongs to F_p. Since k is even of degree <=2m, it is a degree-<=m polynomial in v^2. The trace identity is exactly GH-147's; no independent point-count claim is hidden in it.

Let L=2m+1=(p+1)/4. Choose any L distinct square classes w_i=v_i^2 in F_p and obtain **independent integer** curve traces t_i=a_(p^2)(E_(1/8+rho*v_i)) mod p. Write the Lagrange cardinal polynomials

    ell_i(W)=product_(j != i) (W-w_j)/(w_i-w_j).

Then J_p(W)=sum_i t_i ell_i(W). The marked first moment is recovered by

    S1(B0)=(rho/12) * sum_i t_i ell_i'(1/144).

The orientation multiplier follows from rho^(-1)*2v0=rho/12. The quotient v~(-v) preserves unmarked trace values, but retaining v0 or an equivalent orientation bit is mandatory for the signed first jet; the two signs give opposite S1 when it is nonzero. This is a precise BRC observer/future-operation preservation statement. L is a sufficient sample count, **not a minimality theorem**; the square structure J_p=G_p^2 may admit further proven compression.

For p=3347, m=418 and L=837, rather than the earlier GH-147 bound of 1673 independent trace values.

## GH-149 (proved direct certificate): CM fixed-point anchor

At v=0 the curve E_(1/8):y^2=x^3+x^2+x/8 is rationally isomorphic under (u,z)=(4x,8y) to z^2=u^3+4u^2+2u, and j(E_(1/8))=8000. This is the classical CM j-value with discriminant -8; external context: Sage's cm_discriminant example for j=8000 (https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_number_field.html) and the isomorphic model at https://planetmath.org/examplesofellipticcurveswithcomplexmultiplication. The CM identification is not used to *invent* the trace: the value below was directly counted.

At p=3347=57^2+2*7^2, direct 3347-term prime-field Legendre summation computes a_p(E_(1/8))=-114. Since the model is over F_p, Frobenius gives the **integer** extension trace

    a_(p^2)(E_(1/8))=a_p^2-2p=(-114)^2-2*3347=6302,

so the independently supplied sample t(0)=6302 mod 3347=2955. Only one of the 837 traces required by GH-148 is supplied in this unit independently of Hasse; the other 836 are not independent new large-prime counts.

Dependent cross-check with Hasse-generated remaining samples: v0=279, w0=860=144^(-1) mod 3347; G(0)=3233=-114, J(0)=2955, J(w0)=588, J'(w0)=997, so S1(B0)=(997/12)rho=362rho mod 3347. This checks the formula, **not** an independent special-value proof. The earlier GH-143 full-field 3347 trace at B0 is a separate existing evidence reference, not newly executed.

## Exact executed evidence

Verified script: research_notes/portable_direct/d25_gh148_gh149_even_trace_cm_anchor_check.py. Execution of its local version using Python 3 stdlib returned PASS_GH148_GH149_COMPRESSED_TRACE_CM_ANCHOR_EXACT. Small-prime direct F_(p^2) character enumeration covers p=11,19,43,59,67,83,107, 99 independently counted labelled curve traces and 604,827 field-character observations; every sample agrees with the compressed interpolation and marked S1 cross-check. At p=3347 the exact direct F_p anchor is independently counted, while the remaining 836 sample traces are explicitly HASSE_DERIVED_NOT_INDEPENDENT. No p=373 native divided-power experiment, independent referee, Lean proof or original-class [X]U mod p^2 measurement occurred.

The more extensive author report, exact local executed source and log are separately packaged for portable handoff; this GitHub text is not a canonical native Source checkpoint.

## Frontier and next exact scientific action

Preserve the frozen scientific source, GH-146/147 trace line, GH-148 even square quotient, and the GH-149 independently counted fixed-point anchor. Do not repeat the full 3347^2 enumeration or treat interpolation samples generated from H as independent CM evidence. Next: either independently determine the **remaining 836** distinct square-class trace inputs and reproduce J'(860)=997, or prove a smaller sign/phase-recovery scheme exploiting J=G^2 with the v0 orientation retained. Independently pending for the original mother Task: original-class native H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius/eta normalization, p=373 benchmark, GH-3 and GH-83 proof obligations. Mother D25/LIFT/JT2 stays OPEN.

The v0.6.11 ordinary Gateway continuation attempt in this unit returned INVALID_ARGUMENT / CONTROL_QUOTA. No recovery_status tool is exposed, and old #1558 protected service sessions/staging and native Source frontier cannot be claimed as a current owned run. No new CLAIM/OPEN/native checkpoint/Result/review was obtained, and no scheduler or P000/source-pin change was made. Controller support remains awdawmip/enterprise-math#1558; original p=373 validation remains #1559.
