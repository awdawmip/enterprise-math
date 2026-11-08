# D25 — Exact degree-two Galois isogeny of the frozen original E3 and its p=373 Frobenius composition

2026-11-08 · Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT` · Publication `TP2-B6F4FC938FF94941C1B7` · Frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). **AUTHOR-SIDE PROVED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

## Original-class construction and rational proof

Work in K=Q(T), T²=2, σ(T)=-T. The **original** curve is E: y²+xy+cy=x³ with c=(2-T)/108, invariant differential ω=dx/(2y+x+c). Its Galois-conjugate original curve E^σ has c^σ=(2+T)/108. Let

[
e=(2T-3)/36,quad u=x-e,quad z=y+(x+c)/2.
]

The point P=(e,-(e+c)/2) has order 2; direct expansion gives

[
z²=u³+a u²+b u,qquad a=T/6,quad b=(3-2T)/432.
]

The Vélu quotient by {O,P} is represented by

[
U=u+a+b/u,qquad Z=z(1-b/u²),qquad
Z²=U³-2aU²+(a²-4b)U.
]

For Q=u²+au+b, the **polynomial identity** `(u²-b)²=Q²-2auQ+(a²-4b)u²` proves this rational map, with the kernel poles extended by the usual isogeny. Since a^σ=(-2a)/2 and b^σ=(a²-4b)/4, an actual isomorphism from the quotient to E^σ is

[
u_σ=U/2,quad z_σ=TZ/4,quad
x_σ=u_σ+e^σ,quad y_σ=z_σ-(x_σ+c^σ)/2.
]

Thus Φ:E→E^σ is a **separable degree-two isogeny**. The original curve and quotient have good reduction for p>3 (denominators and discriminant norms involve only powers of 2,3); reduction preserves this algebraic morphism. All of the above is over the frozen curve, not a replacement Hesse model.

As ω=du/(2z), the quotient is normalized because dU/du=1-b/u², while the last coordinate scaling satisfies

[
oxed{Phi^*ω_{E^σ}=T,ω_E.}
]

This T is a geometric differential-pullback factor, **not** an authenticated H0/B0 basis normalizer η. Conjugating gives σ(T)=-T. The u-coordinate of Φ^σ∘Φ is

[
rac{(u²-b)²}{4u(u²+au+b)}=u([2]P),
]

and its pullback of ω is -2ω, distinguishing [-2] from [+2]. Therefore

[
oxed{Phi^σcircPhi=[-2]}
]

as an exact elliptic-curve isogeny over K and after good reduction.

## Frobenius on the original object

For p≡13,19 (mod24), (2/p)=-1, so the p-power coefficient action on k=F_p[T]/(T²-2) is σ. With relative geometric Frobenius `Fr_p:E→E^σ`, the original-class endomorphism `A_p=Φ^σ∘Fr_p:E→E` has degree 2p. Frobenius naturality and the exact conjugate composition prove

[
oxed{A_p²=[-2]circ Fr_{p²}.}
]

At **p=373**, consume the independently established original-curve exact finite-field certificate `#E(F_(373²))=138384=(373-1)²`, which proves `Fr_(373²)=[+373]`. Consequently the new geometric identity gives

[
oxed{A_{373}²=[-746],qquad deg(A_{373})=746.}
]

For previously independently counted p=13 and p=19 original curves the corresponding geometric square values are [-26] and [-38]. This constructs an explicit geometric isogeny/Frobenius comparison of the **correct original class**. It does not manufacture a native divided-power [X]U readout, native rank, η or signed κ. Applying it to an H0/B0 matrix requires proving the exact original-class cohomological comparison and orientation.

## Verification and method reuse

The actually executed **standard-library exact-integer / Fraction** checker (companion `d25_original_e3_degree2_isogeny_certificate_20261108.py`) checked all K coefficients, 40 non-pole rational-chart substitutions, the polynomial quotient identity at **every one of 139659 u's** over F_(13²), F_(19²), F_(373²), and 128 non-pole conjugate-composition tests per prime (384). All passed; the exact JSON output is a companion artifact. The algebraic proof is independent of this finite testing; it also uses the earlier explicitly source-labelled point-count certificate instead of rerunning or recrediting it.

**BRC COMPOSE_APPLIED / standard Vélu REUSE_APPLIED**: the carrier retains original curve, Galois-conjugate target, 2-torsion kernel, quotient, differential, p-Frobenius/q-Frobenius and signed composition. Erasing σ or the sign changes the observer. This is external elliptic algebra, not P000 X6 or an original 2D native plane. Toolbox and method inventories contain no identified special-purpose 2-isogeny interface; standard Vélu is reused rather than promoted as a new global tool.

## Actual acceptance boundary and next executable action

The **mother objective stays open**: frozen `Δ_p-R_p=0 mod p` in both target prime classes, and the separate original same-class H0/B0 divided-power native benchmark #1559. That benchmark still requires measured **[X]U mod139129 at p=373**, genuine module rank, semilinear direction and actual η, signed odd Green/Hesse κ, original Δ-R, and independent reproducibility. If a legitimate native evaluator and comparison become available, test its appropriate operator against A_373²=[-746]; otherwise report PENDING_OWNER / NOT_EXECUTED, not experiment success. No repeated auxiliary proof replaces the native object.

The historical read-only continuation request `onhour11-20261106-1400-exact-research-lane-continuation` has a SUCCEEDED read receipt. Own `recovery_status` this turn was rejected with `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`, and Sites diagnostic is `CONFIGURED_NOT_LIVE_VERIFIED; research_authority_granted=false`. No own Source session, CLAIM/run, checkpoint, admitted Result, independent review or native benchmark execution is claimed. This author-side artifact and its next action preserve the logical Research label `chatgpt-research-onhour-enterprise-math-20260923` without adopting maintenance `chatgpt-hourly-enterprise-math-20260921`.