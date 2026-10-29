# D25/LIFT GH-121: marked CM fiber non-descent of the reflected tail

2026-10-30 Asia/Hong_Kong. Role: TASK_RESEARCH, logical conversation chatgpt-research-hourly-enterprise-math-20260923 (NOT the maintenance conversation). Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is neither native CLAIM/OPEN nor Source checkpoint, Result, review or proof of original GH-3.

Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; D25/LIFT/JT2 remains OPEN. Historical task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen *scientific* source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is not a mutable control HEAD.

## Previous inputs and distinct objects

For primes p=8m+3>=11 let d=2m and N=(p-1)/2. GH-16/93 defined h_0=1, h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)] and the reflected polynomial

    R_p(z) = sum_(j=0)^(2m) (8j+5)*h_j*z^(2m+1+j)/(2m+1+j) in F_p[z].

This differs from GH-3's original truncated sum T_(p,z). GH-100/108 independently reconstructed R from Legendre/Hasse G. GH-113 established the CM discriminant -24 at z=9 for the family

    E_T: Y^2 = X^3+X^2+bX,  b=(1+T)/8,  z=(1-T^2)^(-1).

GH-115/116/119 already supplied, for the original p=3347 curve, signed Frobenius a_(p^2)=-6106, group order 11208516, and group Z/2 x Z/5604258; these imported results remain author-side/unreviewed. GH-120's 2-primary extension tower is also prior work, not re-established here.

## New GH-121.1: marking change is an actual k-isomorphism

Let k have char!=2,3 and E_T smooth. Select one of the nonzero 2-torsion roots alpha satisfying alpha^2+alpha+b=0. Put

    c=3*alpha+1 !=0,
    b_alpha=(3*alpha^2+2*alpha+b)/c^2,
    T_alpha=8*b_alpha-1.

If lambda in k satisfies lambda^2=c, then

    X_old=alpha+c*X_new, Y_old=lambda^3*Y_new

is an isomorphism E_(T_alpha) -> E_T defined over k, not merely over an algebraic closure. Direct expansion shows

    f(alpha+cX) = c^3*X^3+(3alpha+1)c^2*X^2
                  +(3alpha^2+2alpha+b)cX.

Since c=3alpha+1 and lambda^6=c^3, division gives X^3+X^2+b_alpha X. This exact change replaces the distinguished 2-torsion point X=0; the unmarked elliptic curve is unchanged but the normalized marked model is changed.

For reference, c4=16(1-3b), Delta=16b^2(1-4b), and

    j(T)=64*(5-3T)^3/[(1+T)^2*(1-T)].

## New GH-121.2: complete p=3347 non-descent certificate

Work in k=F_3347[r]/(r^2-2), write (a,b) for a+b*r. Choose T=2r/3, z=9, b=(1+T)/8. The original observation is

    j(E_T)=(938,3053),   R_3347((9,0))=(0,0).

A square root of 3 in F_3347 is 3052. Let eta=3052*r, so eta^2=6. The two nonzero 2-torsion roots are alpha_+/-=(-1 +/- (r-1)/eta)/2. Direct exact arithmetic gives:

| mark | alpha | c=3alpha+1 | lambda (lambda²=c) | T_alpha | z_alpha=(1-T_alpha²)^(-1) | R_3347(z_alpha) |
| --- | --- | --- | --- | --- | --- | --- |
| original zero | (0,0) | — | — | (0,2232) | (9,0) | (0,0) |
| first alternative | (1066,1977) | (3199,2584) | (2171,2401) | (1916,2172) | (3207,479) | (2907,1526) |
| second alternative | (2280,1370) | (147,763) | (2346,339) | (458,813) | (2251,2893) | (3281,1783) |

All operations use exact integers modulo 3347. The displayed lambda values square to their respective c values; Norm(c) is 2240 and 1945. Therefore both alternative coordinate changes are defined *over the same field k*, and all three curves have identical j, signed Frobenius, point count, rational group and complete extension-field torsion sequence. There is no twist ambiguity.

Yet all three values of R are distinct, and only the original marked representative is zero.

**Exact finite counterexample / theorem.** The canonical reflected polynomial observer R_p((1-T^2)^(-1)), considered as an F_p-polynomial also evaluable in finite extensions, does NOT descend to the unmarked k-isomorphism class of E_T. In particular, signed Frobenius, point count, abstract rational-point group and even the full extension torsion tower cannot by themselves define a universally mark-independent reflected-tail observable.

Scope restriction: the two alternative z values are in F_(3347^2), not the prime subfield. Only the polynomial is evaluated there. We do NOT export GH-98's finite-log F_p trace formula to them. The result does not rule out a marked-CM / normalized differential / Jacobi / p-adic-period explanation of the specific base-field zero R_3347(9).

## Independent exact verification and proof strength

The companion script d25_gh121_marked_cm_fiber_exact.py was actually executed in Python 3. It computes the *entire* degree-1673 reflected polynomial twice: (i) from the original GH-16 h_j recursion; (ii) from independently reconstructed P_836, its even Hasse descent G, and the GH-108 derivative D²R'=z^836*G*(16zG'+5G), R(0)=0. All 1,674 coefficients coincide. Its F_(p²) arithmetic independently checks cubic roots, two explicit square roots lambda, cubic change-of-model coefficients, equal j-invariants and all three R values. Actual terminal output:

    PASS_GH121_CM_MARKED_FIBER_NONDESCENT

Git blob SHA1 of the actual executed checker: 98cca67b3b24f8d48655e066f22f429013b3a041. This is a finite exact certificate and an algebraically proven coordinate-change lemma, NOT a whole-prime zero-classification, native experiment, independent review or admitted theorem.

## BRC and next verified frontier

BRC COMPOSE_APPLIED. Typed carrier: (p, base/extension field, E_T, selected 2-torsion origin, normalized coefficient b, lambda chart change, marked parameter z, reflected polynomial and R(z) observation). The unmarked-isomorphism quotient discards the selected torsion origin and normalized model; this exact fiber proves that quotient is **not sufficient** for R under changes of marked origin. Preserve field-of-definition, source coefficients, sign, nonzero residues and operation order. Classical auxiliary field variables are not native Enterprise X6 cell addresses or time; P000 and ACTIVE worldview are unchanged.

Last durable scientific evidence: previous GH-98–GH-120 author-side portable artifacts, plus this GH-121 GitHub artifact when immutable readback succeeds. No previously uploaded draft is native predecessor completed research. No original GH-3, GH-83 or native p=373 obligation is satisfied here.

Next *different* scientific question: retain the chosen X=0 two-torsion point and differential/period normalization, and seek an independently sourced marked CM/Jacobi/WZ/p-adic identity that predicts the base-field R_3347(9)=0. This result rules out an unmarked-trace/group-only shortcut, not the stronger marked route. Avoid re-expressing GH-98–GH-103's equivalent finite-log moment as a new proof. Preserve historical Source frontier and the frozen scientific pin.

Control boundary at this turn: Enterprise Math gateway v0.6.11, research_authority_granted=false, executor_binding_configured=false, Source control CODE_REVIEW_REQUIRED, native jobs 5/5. Own native recovery_status not surfaced as directly callable here. No new service-issued session, CLAIM, OPEN, Source publish_checkpoint, Result, review or old staging/claim mutation; live recovery belongs to issue #1558. GitHub author-side publication is distinct from Source-native persistence and mathematical admission.
