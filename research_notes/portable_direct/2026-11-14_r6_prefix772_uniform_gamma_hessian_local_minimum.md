# PREFIX-772 / R6 — Uniform rational-interval Gamma Hessian certificate and a unique two-clock local minimum

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Status: `AUTHOR_INTEGER_INTERVAL_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.

Scientific scope: external 189-layer killed-Pascal BRC first-stop model, two independent Gamma clocks, and their maximum. This continues the exact mathematical statements of PREFIX-770 and PREFIX-771, without changing the native Heartbeat World/P000 ontology or the frozen stopping model.

## 1. Definitions and exact prior dependencies

For the 189 survivor polynomials `s(u)=(S_0(u),...,S_188(u))`, let `d=s'`, `e=s''`, `f=s'''`. Define

[
K_{ij}={inom{i+j}{i}over2^{i+j+1}},qquad L_{ij}=(i+j+1)K_{ij}.
]

For `Y(p,z)=max(C_p,C_z)`, put `mu=E[Y]`, `W=Var(Y)`, `A(p,z)=-partial_p partial_z mu(p,z)`, `D(p,z)=-partial_p partial_z W(p,z)`. On any region where `D>0`, define `Q(p,z)=A(p,z)/D(p,z)`. At `p=z=u` use the abbreviation `Q(u)=Q(u,u)`.

PREFIX-771 establishes the diagonal derivatives, including
[
Q''(u)={(A''D-AD'')D-2(A'D-AD')D'over D^3}.
]
PREFIX-770 establishes the transverse expansion, with `p=u+t,z=u-t`,
[
Q(u+t,u-t)=Q(u,u)+Q_2(u)t^2+O(t^4),qquad
Q_2={(A_2D-AD_2)over D^2}.
]
The exact formulas for `A',A'',D',D'',A_2,D_2` are those of PREFIX-770/771, reconstructed directly in the attached verifier.

## 2. Theorem 772.1 — uniform positive diagonal and transverse curvature

Let
[
I=left[{502971451over10^{10}},{502971452over10^{10}}ight].
]
For **every real** `u in I`, in the frozen model,
[
oxed{D(u,u)>0,qquad 4<Q''(u)<5,qquad 21<Q_2(u)<22.}
]

This is a continuous-interval certificate, rather than a finite sample of parameters. The verifier implements the original integer BRC width predicate, reconstructs all 189 survivor layers, verifies exactly 9,529 nonzero survivor positions and an empty terminal layer, and builds interval enclosures of each `S_i^{(r)}(u)` for `r=0,1,2,3`.

**Certified interval proof.** Write `u=x/B` and `x in [x_L,x_R]` with the exact integer endpoints. Every term of a survivor derivative is an integer multiple of `(-1)^b u^{k-a}(1-u)^{n-k-b}`. The unsigned monomial is bounded below by its `x_L`-power and `(B-x_R)`-power product, and above by the corresponding `x_R`- and `(B-x_L)`-powers; changing sign reverses endpoints. Common exact denominator `B^191` for all four jets enables integer sums followed by outward floor/ceiling division onto scale `F=10^48`. The positive Erlang kernels `K,L` are independently enclosed on the same scale, and every subsequent addition, subtraction, multiplication, and bilinear contraction uses outward-rounded integer interval arithmetic.

By induction, each computed interval encloses the corresponding exact real quantity for every `u in I`. The program verifies `D_lower>0`; then, writing `N''=(A''D-AD'')D-2(A'D-AD')D'` and `N_2=A_2D-AD_2`, it verifies strictly by integer cross-products
[
4(D^3)_{m upper}<(N'')_{m lower},quad
(N'')_{m upper}<5(D^3)_{m lower},
]
[
21(D^2)_{m upper}<(N_2)_{m lower},quad
(N_2)_{m upper}<22(D^2)_{m lower}.
]
All denominators are positive, establishing the three displayed uniform claims. The stored Python assertions are the complete finite interval-certificate comparison; decimal displays play no role.

## 3. Theorem 772.2 — unique stationary point and strict two-parameter local minimum

PREFIX-771 certified exact endpoint signs
[
Q'(502971451/10^{10})<0<Q'(502971452/10^{10}).
]
Theorem 772.1 implies `Q''(u)>4` throughout `I`, hence `Q'` is strictly increasing on `I`. The intermediate value theorem now gives **exactly one** `u_* in I` satisfying `Q'(u_*)=0`.

The symmetry `Q(p,z)=Q(z,p)` gives zero first transverse derivative at `p=z=u_*`; the diagonal stationarity gives zero gradient. Set `u=(p+z)/2`, `t=(p-z)/2`. The mixed `ut` second derivative vanishes at `t=0` by exchange symmetry. The two pure curvatures are `Q''(u_*)>4` and `2Q_2(u_*)>42`. The Hessian is positive definite in these local coordinates. Consequently
[
oxed{(u_*,u_*)	ext{ is a strict local minimum of }Q(p,z).}
]
This is the first certificate in this line that supplies **both** interval-wide diagonal uniqueness and full two-dimensional local strict minimality.

## 4. Theorem 772.3 — a sharper global critical-parameter upper bound

Take the additional rational witness
[
u_0={5029714515over10^{11}}=0.05029714515.
]
A second exact interval computation with coincident endpoints `x_L=x_R` gives an outward enclosure for `Q(u_0,u_0)`; its decimal display is approximately `0.02851859116285760930849746304...`. Integer cross multiplication strictly verifies
[
oxed{0<q_cle Q(u_0,u_0)<
 {28518591162857609310over10^{21}}
 =0.028518591162857609310.}
]
This tightens PREFIX-771's upper bound `0.028518591162857609314` at the same frozen scientific input. The `q_c` implication uses the critical-curvature definition of PREFIX-763; it is not an independent proof that the global infimum is attained at the diagonal point.

## 5. Reproducibility, evidence and remaining questions

The complete Python 3 standard-library integer checker is `research_notes/portable_direct/PREFIX772_R6_UNIFORM_INTERVAL_HESSIAN_CHECK.py`. Execution of the local checker generated `PREFIX772_R6_UNIFORM_INTERVAL_HESSIAN_RESULTS.json` and printed `ALL_CHECKS_PASS PREFIX772 UNIFORM_HESSIAN_AND_POINT_Q`. It computes the full continuous-interval enclosure and a separate interior rational witness. There is no stochastic sampling, floating-point inequality test, solver assumption, or appeal to an unchecked derivative sign beyond the previously published exact PREFIX-771 endpoint certificate.

Provenance: PREFIX-770 transverse identities; PREFIX-771 diagonal second-jet identities and endpoint signs; immutable model `f42f2906d77f24085c123f3ccfe9667d41caa96d`. The run is an author-side exact arithmetic certificate; formal independent review remains open.

Next mathematical questions: determine whether another off-diagonal region or domain boundary has a lower `Q` than this strict local minimum; obtain a globally certified minimizer, or turn the precise Gamma moment inequalities into a genuinely new, previously unverified `1/768` comparison-cell exclusion. No historical Gamma-grid area was added in this result.
