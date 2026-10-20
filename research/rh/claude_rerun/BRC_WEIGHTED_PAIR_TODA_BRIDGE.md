# BRC_WEIGHTED_PAIR_TODA_BRIDGE — signed carrier upgrade, finite boundary network, and pair/Toda interface

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`  
Driver: `EM-DVR-7Q4K2C`  
Parent head: `4e8805116bd837439b1aede71dbe4e5267de4c43`

Status:

`WEIGHTED_PAIR_TODA_INTERFACE_FOUND / BOOLEAN_BRC_INSUFFICIENT_AT_SIGNED_NODE / FIRST_BOUNDARY_PAIR_WIDTH_LE_12 / MULTIPAIR_MAJORANT_REDUCED / RH_NOT_CLOSED`

This is a later correction/refinement of the constructive BRC notes. In particular, any wording in
`BRC_VERIFIED_BOUNDARY_LAYER.md` suggesting that a pair-local nonnegative branch may always be
recoalesced to a sign token is valid only for a terminal one-pair sign query. In a multi-pair
continuation the residual partition shape is future-relevant and must be retained.

## 1. Setup

Let

`G(z)=sum_(n>=0) a_n z^n = G(0) product_j (1+alpha_j z)`

be the normalized genus-zero Xi coefficient function, and let

`D_(r,k)=det[a_(k+j-i)]_(i,j=0)^(r-1)=s_(r^k)(alpha)`.

For a conjugate off-line pair keep the exact BRC atom

`Y={R exp(i theta), R exp(-i theta)}`.

For a two-row partition `(a,b)`,

`S_(a,b)(Y)=R^(a+b) sin((a-b+1)theta)/sin(theta)`.

Fix a rank `r` and suppose the pair is in its **first locally unsafe layer**

`pi/(r+1) < theta <= pi/r`.

Then every two-row Schur value of width at most `r` is nonnegative except possibly

`S_(r)(Y)=R^r sin((r+1)theta)/sin(theta) < 0`.

Write

`eta_Y := -S_(r)(Y) > 0`.

Because `phi=(r+1)theta-pi` lies in `(0,theta]`,

`eta_Y=R^r sin(phi)/sin(theta) <= R^r`.

This sharper first-layer bound is used below.

## 2. Exact top-row-drop theorem

Let `lambda` be any partition of width at most `r`. In the branching identity

`S_lambda(X union Y)=sum_(mu subset lambda) S_mu(X) S_(lambda/mu)(Y)`,

a negative pair-local component can only arise from the Schur component `(r)`.

By the Pieri rule, the coefficient `c_(mu,(r))^lambda` is `1` exactly when
`lambda/mu` is a horizontal `r`-strip.

Since `lambda` has at most `r` columns, a horizontal strip of size `r` must use exactly one
cell in every column. Therefore:

- if `lambda_1<r`, no negative `(r)` transition exists;
- if `lambda_1=r`, the predecessor is unique and is
  `lambda^-=(lambda_2,lambda_3,...)`.

Thus the first unsafe negative transition is the deterministic **top-row drop**

`lambda -> lambda^-`

when the proof is routed backwards from the target partition.

For the rectangle `lambda=(r^k)`, repeated negative transitions give uniquely

`(r^k) -> (r^(k-1)) -> ... -> (r^(k-j))`.

## 3. Boolean BRC saturation: a precise NO_RESURRECTION boundary

Assume `S_lambda(X)>0`, `S_(lambda^-)(X)>0`, and `S_(r)(Y)<0`.

The pair expansion contains simultaneously:

- the empty pair branch, contributing the positive term `S_lambda(X)`;
- the unique top-row-drop branch, contributing the negative term
  `S_(lambda^-)(X) S_(r)(Y)`.

Hence a Boolean/sign-support carrier immediately has support

`{POSITIVE, NEGATIVE}`.

Lossless union preserves that ambiguity; it cannot determine the sign of the summed amplitude.

Therefore the Boolean/result-support BRC semantics formalized in R023 is intentionally
insufficient for this RH node. The required carrier is at least

`partition future-signature + signed/amplitude weight`.

This is not a defect in R023: signed cancellation was explicitly outside its carrier contract.

## 4. Exact signed pair transfer

Let `U_nu` denote the Littlewood–Richardson multiplication operator on partition states:

`(U_nu f)(lambda)=sum_mu c_(mu,nu)^lambda f(mu)`.

These operators commute because the symmetric-function representation ring is commutative.

For a first-layer pair,

`T_Y = sum_nu S_nu(Y) U_nu`.

All coefficients are nonnegative except the coefficient of `U_(r)`. Hence

`boxed: T_Y = P_Y - eta_Y U_(r)`

where `P_Y` is coefficientwise nonnegative and contains the identity operator.

This is the signed/amplitude BRC replacement for sign-only branching.

## 5. Multi-pair positive-majorant theorem

Let `Y_1,...,Y_M` be first-layer unsafe pairs for the same rank `r`.
Put

`T_i=P_i-eta_i U_(r)`

as above, and let `f_X` be a nonnegative background partition-state vector.

Define the positive majorant state

`F := P_1 ... P_M f_X`

and rectangular coordinates

`F_k := F(r^k)`.

Because every `P_i` contains the identity and all `P_i,U_(r)` commute,

`P_(not J) f_X <= F`

coefficientwise for every subset `J`.

Expanding the exact product gives

`T_1...T_M
 = sum_(J subset {1,...,M}) (-1)^|J| eta_J U_(r)^|J| P_(not J)`,

where `eta_J=product_(j in J) eta_j`.

At the rectangular target, backward `U_(r)^j` is unique:

`[U_(r)^j g](r^k)=g(r^(k-j))`.

Dropping the nonnegative even-cardinality terms and majorizing the odd terms yields the exact
sufficient lower bound

`boxed:
 D_(r,k)(actual)
 >= F_k - sum_(1<=j<=min(M,k), j odd) e_j(eta_1,...,eta_M) F_(k-j).`

Therefore the finite domination criterion

`sum_(j odd) e_j(eta) F_(k-j)/F_k < 1`

implies `D_(r,k)>0` whenever `F_k>0`.

This is a genuine BRC recoalescence: the `2^M` signed subset paths are replaced by at most
`ceil(M/2)` odd elementary defect weights and a depth-`M` edge-state vector.

It is not yet RH because the needed edge ratios of the positive majorant `F` are not
globally bounded.

## 6. Single-pair exact interface with the Toda carrier

For one final unresolved first-layer pair `Y`, assume the actual background alphabet/state `X`
is rank-`r` safe and all pair-router terms other than `(r)` are nonnegative. Then

`D_(r,k)(X union Y)
 >= D_(r,k)(X) + D_(r,k-1)(X) S_(r)(Y)`.

Define the adjacent rectangle ratio

`P_(r,k)(X)=D_(r,k-1)(X)/D_(r,k)(X)`.

A sufficient condition for the unique negative pair branch not to flip the target is

`boxed: P_(r,k)(X) eta_Y < 1.`

For the actual Toeplitz determinant field define

`q_(r,k)=D_(r,k-1)D_(r,k+1)/D_(r,k)^2 = exp(-u_(r,k))`.

Then exactly

`P_(r,k)/P_(r,k+1)=q_(r,k)`

and hence

`P_(r,k)=P_(r,1) exp(sum_(j=1)^(k-1) u_(r,j)).`

Rectangular duality gives

`D_(r,1)=h_r(X)`

(the `r`-th complete homogeneous coefficient of the reciprocal/zero alphabet), so

`boxed:
 P_(r,k)
 = h_r(X)^(-1) exp(A_(r,k)),
 A_(r,k):=sum_(j=1)^(k-1) u_(r,j).`

Thus pair-space and coefficient-space meet at the exact inequality

`boxed:
 eta_Y exp(A_(r,k)) < h_r(X).`

## 7. Spectral-action NCC

Suppose the safe background contains the first verified critical-line Xi factor

`alpha_1=1/(4 gamma_1^2)`

and the remaining background has nonnegative complete-homogeneous coefficients through rank
`r`. Then

`h_r(X)>=alpha_1^r`.

For an off-line pair at ordinate `gamma`,

`R=1/(4(delta^2+gamma^2)) <= 1/(4 gamma^2)`

and in the first unsafe layer `eta_Y<=R^r`.

Consequently a failure of the one-pair domination certificate requires

`A_(r,k) >= r log(alpha_1/R)`

and therefore

`boxed:
 A_(r,k) >= 2r log(gamma/gamma_1).`

This is a cross-space **No-Completion Cone Certificate**:

- zero-space supplies the pair ordinate `gamma`;
- Toda-space must accumulate enough action `sum u` to amplify its tiny negative branch.

A pair-driven sign failure cannot occur while the integrated Toda action stays below this
spectral threshold.

## 8. Why the cubic scale reappears

For the exactly solvable PF baseline `a_k=1/k!`,

`q_(r,j)=j/(j+r)`

and hence

`A^0_(r,k)
 = sum_(j<k) log(1+r/j)
 = log binomial(k+r-1,r).`

For `k` on a cubic scale `k=C r^3`,

`A^0_(r,k)=2r log r + O(r)`.

At the first high-rank spectral boundary one has `gamma` proportional to `r`, so the
pair-action threshold

`2r log(gamma/gamma_1)=2r log r+O(r)`.

Thus the pair/Toda crossover and the independent saddle proof's `r^3/k` scale meet at the
same leading **cubic exponent**.

This is structural evidence, not a coverage theorem. The current explicit constants do not
overlap: the published cubic wedge begins only at `k>=10^18 r^3`.

## 9. Sharpened first-boundary spectral width

Use the published rigorous inputs

- Platt–Trudgian: RH verified through `H=3*10^12`;
- Bellotti–Trudgian–Yang (2026):
  `beta < 1-1/(R log|gamma|)` with `R=4.896`, `|gamma|>=3`.

For `t>=H` define the maximum allowed Xi angular defect

`Theta(t)=2 atan(x(t)),
 x(t)=(1/2-1/(R log t))/t`.

It is strictly decreasing. Let

`L=floor(pi/Theta(H))`.

The sharpened sector theorem covers rank `r<=L-1`; `r=L` is its first symbolic uncovered
rank.

An active first-layer pair at rank `L` must satisfy

`Theta(gamma)>pi/(L+1)`.

The initial threshold gap obeys

`Theta(H)-pi/(L+1) < Theta(H)^2/pi < 1/(3H^2)`.

On `H<=t<=H+2/5`:

- `log t>20`, `R>4`;
- writing `a(t)=1/2-1/(R log t)`,
  `a(t)-1/(R(log t)^2) > 779/1600`;
- `x(t)<1/20`;
- `t/H<21/20`.

Therefore direct differentiation gives the conservative derivative floor

`-Theta'(t) > (779/802)*(20/21)^2 * H^(-2) > 5/(6H^2)`.

Across a width `2/5` the angular envelope drops by more than `1/(3H^2)`, which exceeds
the entire first-rank threshold gap. Hence

`boxed:
 every first-boundary active pair has
 H < |gamma| < H+2/5.`

So the dangerous spectral window is rigorously narrower than `0.4`.

## 10. Explicit branch-width bound: at most 12 off-line pair atoms

Bellotti–Wong prove

`|N(T)-M(T)| <= 0.10076 log T + 0.24460 log log T + 8.08292`

for `T>=e`, where

`M(T)=T/(2pi) log(T/(2pi e))`.

On `[H,H+2/5]` use only the conservative bounds

`log T<29`, `log log T<4`, `2pi>6`.

Then each endpoint error is `<11.98336`, while

`M(H+2/5)-M(H) < (2/5)*(29/6)`.

Thus

`N(H+2/5)-N(H) < 25.901 < 26`.

Since the left side is an integer,

`boxed: N(H+2/5)-N(H) <= 25.`

Every off-line conjugate Xi pair at positive ordinate consumes at least two zeta zeros counted
with multiplicity, at `beta` and `1-beta`. Therefore the first sharpened boundary layer contains
at most

`boxed: M_active <= 12`

dangerous off-line pair atoms (counted with multiplicity).

Combined with Section 5, the first genuinely uncovered signed-BRC network has at most six
odd defect orders `j=1,3,5,7,9,11`, rather than an infinite zero family.

## 11. Correct current frontier

The previous `PAIR_CLUSTER_DOMINATION` target is now replaced by two more precise bridges.

### `WEIGHTED_BOUNDARY_MAJORANT`

Bound

`F_(k-j)/F_k`, `j in {1,3,5,7,9,11}`,

for the positive majorant generated by at most 12 active pairs.

### `PAIR_TODA_ACTION_STABILITY`

For an actual safe background, prove that the exact Toda action

`A_(r,k)=sum_(j<k) u_(r,j)`

cannot reach the spectral-action NCC before the known cubic tail certificate takes over.

A third exploratory carrier is also available:

`RADIAL_ANCHOR_DEFECT`:
replace `Y={Re^{+-itheta}}` by the PF-infinity anchor `{R,R}`. The exact factor residual is

`(1+2R cos(theta)z+R^2z^2)-(1+Rz)^2
 = -2R(1-cos(theta))z`

with size at most `R theta^2 <= 1/(4 gamma^4)`.

Absolute smallness alone is not enough because high-rank minors are ill-conditioned near the
sector threshold, but it gives a sparse anchor-plus-residual representation for future
whitened-norm work.

## 12. Classification

Exact/proved in this checkpoint:

- first-unsafe top-row-drop uniqueness;
- Boolean sign-support saturation / signed-carrier necessity;
- signed transfer `T_Y=P_Y-eta U_(r)`;
- multi-pair positive-majorant lower bound;
- exact one-pair adjacent-ratio/Toda interface;
- spectral-action NCC;
- first sharpened boundary window `<2/5`;
- at most 12 dangerous off-line pair atoms in that window.

Structural/conditional only:

- cubic-scale match with the solvable PF baseline;
- any claim that Xi's true Toda action obeys the baseline bound;
- global positivity from the weighted majorant.

Final status:

`RH_NOT_CLOSED`.
