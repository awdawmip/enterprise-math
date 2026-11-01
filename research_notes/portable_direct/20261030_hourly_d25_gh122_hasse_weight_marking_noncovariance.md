# D25/LIFT GH-122 — Hasse normalization transforms; reflected tail does not

Date: 2026-10-30 Asia/Hong_Kong. TASK_RESEARCH logical conversation chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. D25/LIFT/JT2 parent remains OPEN. Frozen *scientific* Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. No native CLAIM/OPEN/checkpoint/Result/review is implied.

## GH-122.1: exact all-characteristic-p Hasse coefficient change lemma

Let k have characteristic p>=5; let f(X) be any cubic, and suppose the coordinate change

    f(alpha+cY) = lambda^6*g(Y),   c=lambda^2 != 0

relates two normalized cubic elliptic equations. Write N=(p-1)/2 and define Hasse coefficients Ha(f)=[X^(p-1)]f(X)^N and Ha(g) analogously. Then

    Ha(g) = lambda^(-(p-1))*Ha(f).

**Elementary complete proof.** Let F=f^N, deg(F)<=3N=3(p-1)/2<2p-1. The coefficient of Y^(p-1) in F(alpha+cY) receives a contribution from X^j only for j>=p-1. Its coefficient equals c^(p-1)*binom(j,p-1)*alpha^(j-p+1). For p<=j<2p-1, binom(j,p-1) is divisible by p (numerator has a p-factor, denominator none). Consequently only j=p-1 contributes, and

    [Y^(p-1)]F(alpha+cY)=c^(p-1)*Ha(f).

But F(alpha+cY)=lambda^(6N)*g(Y)^N=lambda^(3(p-1))*g(Y)^N. Since c=lambda^2, divide to obtain Ha(g)=lambda^(-(p-1))*Ha(f). QED.

This is a classical Hasse/differential covariance law obtained here with the *exact coefficient normalization of GH-100*, not a claim of inventing the standard theorem. Its new use is the comparison with GH-121's exact marked CM isomorphism-fiber obstruction.

## GH-122.2: p=3347 direct numerical certificate

Use GH-121's k=F_3347[r]/(r²-2), T=2r/3, z=9, the two alternative origins at nonzero rational 2-torsion and their explicit lambda. The GH-100 Hasse polynomial here equals P_836(-T)=P_836(T); every value below comes from the independently built Legendre polynomial.

| Mark | Ha_p(T_mark) | lambda^(p-1) | Ha_p(T_mark)*lambda^(p-1) | R_p(z_mark)/Ha_p(T_mark)^2 |
|---|---|---|---|---|
| original z=(9,0) | (783,0) | 1 | (783,0) | (0,0) |
| first alternate, z=(3207,479) | (841,1147) | (249,1905) | (783,0) | (1346,1788) |
| second alternate, z=(2251,2893) | (49,1370) | (902,259) | (783,0) | (3227,128) |

All pairs denote a+b*r. All three curves are k-isomorphic by the **explicit** GH-121 coordinate changes; they have identical Frobenius/point group/torsion. Each Hasse value is nonzero, and the lemma is satisfied exactly. However, R at the original origin is zero while it is nonzero at both alternate origins.

**New precise non-homogeneity conclusion.** No weight-only change law R_p(z_alt)=u*R_p(9) with any unit u in k^* can hold across this marked isomorphism fiber. Dividing or multiplying R by any integral power of the nonzero Hasse factor alone cannot make R an unmarked-invariant scalar on this fiber: the zero/nonzero distinction persists.

This conclusion does NOT rule out a stronger **marked** CM/Jacobi/WZ/p-adic period formula, nor does it prove that the correction is additive in every representation. It proves that signed Frobenius, unmarked group and even the correct Hasse differential weight do not capture all data needed by the reflected-tail polynomial observer.

The alternate z lie in F_(p²) outside the prime field; these statements use the canonical polynomial R_p in F_p[z] extended as a polynomial, not an unproved extension of GH-98's base-field finite-logarithm trace.

## Actual check and dependency boundaries

The executed standard-library script d25_gh122_hasse_weight_marking_check.py imports the previously executed GH-121 program and uses its verified full P_836 and explicit finite-field isomorphisms. It checks both covariance equalities, all displayed Hasse and weight factors, and both nonzero ratios. The actual output was

    PASS_GH122_HASSE_COVARIANCE_AND_TAIL_NONHOMOGENEITY

Git blob of executed source: ea9f90d5c29c512fb7ed7a2c109d924717b4c783; SHA256 6b77f02bf613d83597b0ce4fce283ce9d917222b5674c06584cb5bfac2feb001. The GH-121 checker is a required same-directory import (Git blob 98cca67b3b24f8d48655e066f22f429013b3a041). Author exact computations do not constitute independent mathematical review or original native experiment.

BRC COMPOSE_APPLIED: preserve the chosen 2-torsion point, normalized differential scaling lambda^(-1), Hasse weight lambda^(-(p-1)), actual marked parameter z, source polynomial, extension-field carrier and distinct signed observations. Erasing the mark or replacing it by Hasse weight alone fails the declared observer. This uses a classical auxiliary finite-field chart; no new P000 spatial axis, Heartbeat time or physical model is claimed.

## Immutable frontier and exact next question

Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION, D25/LIFT/JT2 OPEN. Historical task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3.

GH-121/122 are author-side **portable** new evidence, not predecessor Source completed units. Avoid repeating the finite three-member fiber or GH-98–103 equivalent moments. Next independent science: find a **marked** Jacobi/p-adic period or WZ arithmetic evaluation retaining the selected X=0 two-torsion origin and a correction beyond the homogeneous Hasse factor, such that it predicts the specific base-field R_3347(9)=0. Preserve original GH-3, GH-83 and native p=373 as distinct open obligations.

Native recovery still belongs to enterprise-math issue #1558. Status at preparation: gateway v0.6.11, research_authority_granted=false, executor binding false, Source CODE_REVIEW_REQUIRED and active jobs 5/5; no directly exposed own recovery_status and no new session, CLAIM, OPEN, Source checkpoint, Result or review. Old session/request/staging was not modified. Published GitHub author evidence is not formal Source checkpoint or mathematical acceptance.
