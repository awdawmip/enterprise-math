# PREFIX-762 / R6 — Opposite signs of Gamma variance mixed curvature

Date: 2026-11-14. Frozen scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Research class: external independent two-Gamma-clock auxiliary, AUTHOR_EXACT_RATIONAL_REDUCTION / UNREVIEWED / NOT_ADMITTED. This paper does not assert a native X6 or three-dimensional-slice theorem.

## Setup and original exact evidence

Let \`T_x\` denote the first-stop layer of the frozen 189-layer BRC model and \`C_x|T_x=m ~ Gamma(m,1)\`. The two clocks \`C_p,C_z\` are independent. Put \`Y(p,z)=max(C_p,C_z)\`, \`mu=E[Y]\`, \`var=Var(Y)\`, and \`V_q=q^2 var-q mu\`.

Fix \`p0=0,p1=1/4\`. Define \`d_f(z)=f(p1,z)-f(p0,z)\`, and for an interval \`[a,b]\` write \`D_[a,b] f=d_f(b)-d_f(a)\`. Thus \`D_[a,b]\` is a rectangular two-parameter mixed finite difference.

Source witness: \`research_notes/portable_direct/PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json\`, exactly 24,743 bytes with SHA-256
\`1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76\`.
It records exact Fraction numerators/denominators for \`d_var\` and \`d_V2\` at \`z=0,1/4,1/2\`. Since \`d_V2=4 d_var-2 d_mu\`, derive each \`d_mu=2 d_var-d_V2/2\` *exactly* from those existing fractions. The attached checker verifies the source SHA-256 and all strict rational inequalities without rerunning the 189-layer recurrence.

## Theorem 762.1 — Variance has both mixed-difference signs

On \`R_-=[0,1/4]_p × [0,1/4]_z\`,

\`D_[0,1/4] var < -526\`.

On \`R_+=[0,1/4]_p × [1/4,1/2]_z\`,

\`D_[1/4,1/2] var > 155\`.

In particular, variance is neither globally submodular nor globally supermodular on the parameter square.

**Proof.** The original rational fractions certify \`d_var(0)>367\`, \`d_var(1/4)<-159\`, and \`d_var(1/2)>-4\`. Subtraction gives respectively \`-159-367=-526\` as a strict upper bound and \`-4-(-159)=155\` as a strict lower bound. The two rectangles violate the two possible global mixed-difference sign claims. QED.

## Theorem 762.2 — The objective Vq has both signs

For every real \`q>56/263\`, on \`R_-\`,

\`D_[0,1/4] V_q < -526 q^2 +112q <0\`.

For every real \`q>0\`, on \`R_+\`,

\`D_[1/4,1/2] V_q > 155q^2 >0\`.

Thus for every real \`q>=2\`, \`V_q\` has neither global mixed submodularity nor global mixed supermodularity.

**Proof.** Theorem 761.1 gives strictly negative mixed differences of the raw mean; equivalently, \`d_mu(b)<d_mu(a)\` for \`a<b\`. The exact fractions yield \`0<d_mu(1/2)<d_mu(1/4)<d_mu(0)<112\`; these inequalities are also checked by the attached script. Therefore \`-112<D_[0,1/4]mu<0\` and \`D_[1/4,1/2]mu<0\`. Substitute into \`D V_q=q^2 D var-q D mu\`, and use Theorem 762.1. The first upper bound changes sign at \`112/526=56/263\`; the second is positive for all \`q>0\`. QED.

## Corollary 762.3 — Sign-changing mixed derivatives

The finite Erlang survival sums and rational kernel formulas show that \`mu\`, \`M2=E[Y^2]\`, and hence \`var\`, are polynomials in \`(p,z)\`; therefore they are smooth. The rectangular mixed difference equals the integral of \`partial_p partial_z f\` over that rectangle. A negative integral over \`R_-\` and positive integral over \`R_+\` imply that the mixed derivative takes both signs at interior parameter points. Continuity on the convex open rectangle gives a zero of this mixed derivative along a connecting segment. The same assertion holds for \`V_q\` for each fixed \`q>56/263\`. No uniqueness is asserted.

The mechanism is visible in the exact identity

\`partial_p partial_z var = partial_p partial_z M2 - 2 mu (partial_p partial_z mu) -2(partial_p mu)(partial_z mu)\`.

Both raw moment mixed derivatives are strictly negative (PREFIX-761); the middle term has the opposite sign. Thus raw-moment submodularity does not force variance submodularity.

## Reproducibility

The attached Python standard-library \`Fraction\` checker reconstructs all three mean increments algebraically from the published exact \`d_var,d_V2\` witnesses and checks the strict rational signs. It validates the original source byte digest and frozen pin.

| z rectangle | mixed Var (display only) | mixed mean | mixed V2 |
| --- | ---: | ---: | ---: |
| 0 to 1/4 | -527.252710710715 | -100.180677622301 | -1908.64948759826 |
| 1/4 to 1/2 | +155.797473822365 | -10.7598160302871 | +644.709527350035 |

The local exact checker returned \`ALL_CHECKS_PASS PREFIX762\`. Decimals do not decide any sign.

**Scientific relevance and next frontier.** This is an exact model-internal structural obstruction to a uniform mixed-curvature sign proof for variance and \`V_q\`. Continue by constructing endpoint-only interval bounds using separate raw-moment and mean information, then test genuine uncertified 1/768 parameter cells. This paper adds no new Gamma exclusion-area count and is not an independent Result review.
