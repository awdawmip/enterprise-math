# D25/LIFT GH-123 — first-jet connection for the marked Hasse normalization

2026-10-30 Asia/Hong_Kong · TASK_RESEARCH logical conversation chatgpt-research-hourly-enterprise-math-20260923, not maintenance. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION / D25-LIFT-JT2 is still OPEN. Historical Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Preserve scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3; it is not the mutable control HEAD.

## New GH-123.1: exact inhomogeneous derivative law

Work over any field of characteristic p>=5. Fix the family

    E_T: y²=x³+x²+b(T)x,   b(T)=(1+T)/8,

and let H(T)=[x^(p-1)](x³+x²+b(T)x)^((p-1)/2). On a separable algebraic branch choose a nonzero two-torsion root alpha(T) of alpha²+alpha+b(T)=0, put

    c(T)=3alpha+1,  c=lambda² !=0,
    beta(T)=(3alpha²+2alpha+b(T))/c²,
    T_new(T)=8beta(T)-1.

Assume also 2alpha+1!=0 (away from the singular/discriminant branch) and the indicated root lambda exists in the chosen coefficient extension.

GH-121's exact coordinate change proves E_T and E_(T_new) are isomorphic by x_old=alpha+c*x_new, y_old=lambda³*y_new. GH-122 proved, using exact coefficient extraction rather than an unproved analytic statement,

    H(T_new(T)) = lambda(T)^(-(p-1))*H(T).

**Theorem GH-123.1 (formal derivative / first-jet transformation).** As an identity of rational/algebraic functions with the declared separable branch,

    H'(T_new)*T_new' =
      lambda^(-(p-1)) * [ H'(T) + (lambda'/lambda)*H(T) ].

Here primes denote **derivatives with respect to the original parameter T**, not Frobenius derivatives or native heartbeat time. The exact connection term is

    alpha' = -1/[8(2alpha+1)],
    lambda'/lambda = 3alpha'/[2(3alpha+1)].

For completeness, if U=3alpha²+2alpha+b and c=3alpha+1, then

    U'=(6alpha+2)alpha'+1/8,  c'=3alpha',
    T_new' = 8*( U'/c² - 2*U*c'/c³ ).

**Proof.** Differentiate the already proved GH-122 Hasse covariance in the separable function field. By the chain rule, the left side is H'(T_new)T_new'. Differentiation of lambda^(-(p-1)) is -(p-1)lambda^(-(p-1))(lambda'/lambda). In characteristic p the coefficient -(p-1) equals +1. This gives the exact formula. Differentiate alpha²+alpha+(1+T)/8=0 and lambda²=3alpha+1 to obtain alpha' and lambda'/lambda; differentiating U/c² gives T_new'. All denominators are assumed nonzero. QED.

This is a **classical covariance law's formally derived first jet**, not a newly asserted external Gauss-Manin theorem, not an ordinary derivative of the finite-log function on its sampled points, and not an original proof of GH-3. The new project-specific result is its exact operational application to the p=3347 CM marked fiber, demonstrating a concrete nonzero correction that is invisible to unmarked j/trace and to Hasse scalar values alone.

## GH-123.2: complete p=3347 first-jet certificate

Use k=F_3347[r]/(r²-2) and GH-121's original T=2r/3, z=9, with both exact k-isomorphisms. Write a pair (u,v) for u+v*r.

    H(T)=(783,0),    H'(T)=(0,1424).

The executed checker computed:

| chosen alternate origin | alpha' | lambda'/lambda | T_new' | H'(T_new) | both sides of GH-123 identity |
|---|---|---|---|---|---|
| first, alpha=(1066,1977) | (2584,1292) | (78,218) | (636,958) | (3032,1282) | (94,1491) |
| second, alpha=(2280,1370) | (763,2055) | (2470,1966) | (554,2076) | (1689,2223) | (763,1901) |

The previous GH-122 exact values H(T_new)*lambda^(p-1)=H(T) were also rechecked for both branches. The nonzero branch-specific logarithmic-derivative term is an explicit **repair coordinate for transporting Hasse first-jet information under a torsion re-marking**. It is not yet an independently sourced formula for the reflected tail R_p(9).

## Execution and provenance

The executed Python 3 standard-library script d25_gh123_marked_hasse_jet_connection_check.py imports the full GH-121 exact checker, uses the Legendre P_836 constructed there, differentiates its coefficients in F_p, differentiates the algebraic two-torsion-root and model parameters, and verifies every entry above exactly in k. Output:

    PASS_GH123_MARKED_HASSE_JET_CONNECTION

The actual executed program Git blob SHA1 is c61f53b42a3561248e0b3f819ec5f96a5f2d28b7; SHA256 dd2265d5adaf51c2f9a62881415045120179cac68c299d2f28b0ff6f6dc08f76. It depends on the previously published GH-121 exact source Git blob 98cca67b3b24f8d48655e066f22f429013b3a041. General identity: algebraic proof; specific values: exact finite computation; no formal prover, native experiment or independent mathematical review.

BRC COMPOSE_APPLIED: preserve (marked elliptic curve, selected 2-torsion origin, affine isomorphism lambda, invariant differential scaling, Hasse coefficient, Hasse derivative, parameter derivative and the explicit logarithmic-derivative correction). Projecting to signed Frobenius or Hasse value alone erases a future-relevant first jet; this formula constructs the exact retained transport. The parameter T and its formal derivative are an **auxiliary algebraic chart**; neither native X6 time nor a new spatial axis. P000/ACTIVE worldview and frozen scientific pin stay unchanged.

## Exact frontier and distinct obligations

GH-121: unmarked CM trace/group/torsion insufficient for R, shown by one p=3347 CM isomorphism fiber. GH-122: homogeneous Hasse normalization cannot repair R's zero/nonzero marked change; exact general Hasse covariance. GH-123: new first-jet connection law and two exact p=3347 certificates. These are portable author evidence, not canonical Source completed predecessor research and not a resolution of R_3347(9)=0.

**Next independent scientific action:** attempt a marked Jacobi/p-adic-period or WZ identity that carries the selected X=0 torsion point and the normalization/jet correction, and compute its nontrivial exact residue at the *original F_p point z=9* without simply reversing GH-98–103's finite-log moment. Separate GH-83, the original GH-3 truncation T_(p,9), and native p=373 remain OPEN.

Gateway v0.6.11 last read: research_authority_granted=false; executor binding false; Source control CODE_REVIEW_REQUIRED; active native jobs 5/5. Own recovery_status was not exposed as a direct callable; no new Source session, claim, open, publish_checkpoint, freeze or review. Old session, protected uploads and requests untouched. Native support path enterprise-math #1558 owns control restoration. Remote author-side GitHub evidence != native Source checkpoint/admission.
