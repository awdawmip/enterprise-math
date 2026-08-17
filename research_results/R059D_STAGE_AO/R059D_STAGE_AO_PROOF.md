# R059D Stage AO — Proof

Researcher-ID: `EM-R059D-AO-2D7C46`

Task: `RS-R059D-STAGE-AO-MACROSCOPIC-BRC-DENSITY-PROFILE-LIMIT`

Frozen source: `454b57e4eab1c2d856074e653f5cb7db8c423e74`

Taskbook source: `3839dcfe0e6cfe819ec49fb6ffc9d3cdaa937a7f`

## 1. Scope and type separation

The target cycle is already fixed by AL. AO never uses source angle, source arc length, trigonometry, `sqrt(3)`, `log`, or `kappa_perp` to select or alter that cycle.

The source-compatibility angular chart is introduced only after canonical target selection. The theorem compares two measures on the same already-canonical target turns.

Write the first-sector canonical vertices as

`p_n=(a_n,b_n)`, `n=0,...,M_N(r)`,

with `p_0=(r,0)` and `p_M=(0,r)`.

The source-compatible first-sector ray angle is

`theta(a,b)=atan2(sqrt(3)*b,2*a+b)`.

The full source angular carrier is periodic with period `2*pi_source=2*kappa_perp`.

## 2. Uniform scaled frontier

AL froze the target support certificate

`SUP(a,b)=9Q_E(a,b)-9max(a,b)+3`,

where

`Q_E(a,b)=a^2+ab+b^2`

is typed only as primitive incidence/support rank.

Every canonical first-sector vertex is inside the support carrier:

`SUP(a,b)<=9r^2`.

Because the sector path is monotone from `(r,0)` to `(0,r)`,

`0<=a,b<=r`.

Therefore

`Q_E(a,b)-r^2 <= max(a,b)-1/3 <= r-1/3`.

For an outer-frontier vertex, an outward primitive neighbor is outside the carrier. Across one primitive adjacency the support rank changes by at most `27r+18` in the radius-r sector neighborhood. Hence

`SUP(a,b)>9r^2-(27r+18)`.

Substituting the coordinate certificate gives

`-3r-7/3 < Q_E(a,b)-r^2 <= r-1/3`.

Thus uniformly on the canonical frontier,

`Q_E(a,b)/r^2 -> 1`.

Now use the source-compatible triangular embedding only as a comparison chart. If

`rho=sqrt(Q_E(a,b))`,

then exactly

`a=rho*(cos theta-sin theta/sqrt(3))`,

`b=(2rho/sqrt(3))*sin theta`.

Since `rho/r->1` uniformly,

`a/r -> A(theta)=cos theta-sin theta/sqrt(3)`,

`b/r -> B(theta)=2sin theta/sqrt(3)`

uniformly along the canonical frontier.

## 3. Exact cumulative turn identities

The AK alphabet is

- `1:(a,b)->(a,b+1)`,
- `2:(a,b)->(a-1,b+1)`,
- `3:(a,b)->(a-1,b)`.

Before the bisector only symbols `1,2` occur, so every turn increases `b` by exactly one. Therefore, at every canonical vertex with `a>=b`,

`n=b`.

After the bisector only `2,3` occur, so every turn decreases `a` by exactly one. Since exactly `a` turns remain to `(0,r)`, at every canonical vertex with `a<=b`,

`n=M_N(r)-a`.

These are exact target-combinatorial statements.

They also give exact block symbol counts.

For left-half vertices `i<j`:

`#turns=b_j-b_i`,

`#2=a_i-a_j`,

`#1=(a_j+b_j)-(a_i+b_i)`.

For right-half vertices `i<j`:

`#turns=a_i-a_j`,

`#2=b_j-b_i`,

`#3=(a_i+b_i)-(a_j+b_j)`.

## 4. Cumulative limit and turn-density profile

AG/AI give

`M_N(r)/r -> beta`,

with

`3beta^2=4`, `beta>0`.

The display `beta=2/sqrt(3)` is used only in the source-compatible analytic chart.

On the left half-sector,

`N_r(theta)/r -> B(theta)`.

Hence

`G(theta)=2sin(theta)/sqrt(3)`

for `0<=theta<=pi_source/6`.

On the right half-sector,

`N_r(theta)/r -> beta-A(theta)`.

Hence

`G(theta)=beta-cos(theta)+sin(theta)/sqrt(3)`

for `pi_source/6<=theta<=pi_source/3`.

The frontier radial error is `O(1/r)`, the exact Beatty shell error in `M_N(r)` is `O(1)`, and the step-function interpolation error is one turn. Therefore the convergence `N_r/r->G` is uniform on each closed half-sector.

Differentiate the piecewise `C^1` limit:

Left:

`g(theta)=2cos(theta)/sqrt(3)`.

Right:

`g(theta)=sin(theta)+cos(theta)/sqrt(3)`

`=(2/sqrt(3))*cos(pi_source/3-theta)`.

This density is positive, reflection symmetric, and D6-periodic. Its first-sector mass is

`integral_sector g dtheta=beta`,

so over six sectors

`integral_full g dtheta=6beta=2kappa_E`,

matching `T_r/r->2kappa_E`.

## 5. Weak limit of native turn counting

Let `theta_(r,k)` be the midpoint angle of the AM source fiber corresponding to target turn `e_(r,k)`.

Uniform convergence of the cumulative distribution functions implies convergence of the associated Stieltjes measures:

`(1/r) sum_k delta_(theta_(r,k)) => g(theta)dtheta`.

Since `T_r/r->2kappa_E`,

`hat_nu_r=(1/T_r)sum_k delta_(theta_(r,k))`

converges weakly to

`d hat_nu_infty = [g(theta)/(2kappa_E)]dtheta`.

This holds against every continuous periodic test function.

## 6. Weak limit of the source pushforward measure

AM fibers partition the source angular circle up to shared boundary rays of zero source arc measure.

The source weight of one target turn is

`mu_r(e_k)=rDelta_(r,k)`.

After normalization by the source circumference,

`hat_mu_r(e_k)=Delta_(r,k)/(2kappa_perp)`.

The maximum fiber width tends to zero because the frontier has source-compatible radius `r+O(1)` and adjacent target vertices are primitive neighbors. Therefore midpoint sums are Riemann sums:

`sum_k [Delta_(r,k)/(2kappa_perp)] f(theta_(r,k))`

converges to

`(1/(2kappa_perp)) integral f(theta)dtheta`.

Thus

`d hat_mu_infty=[1/(2kappa_perp)]dtheta`.

Both limiting measures are mutually absolutely continuous and

`d hat_mu_infty/d hat_nu_infty`

`=kappa_E/[kappa_perp*g(theta)]`.

Because `g(0)=2/sqrt(3)` and `g(pi_source/6)=1`, this Radon–Nikodym derivative is nonconstant on a set of positive measure.

## 7. Exact local edge-weight limits

For consecutive source rays `p=(a,b)`, `q=(c,d)`, AM gives

`tan Delta = sqrt(3)*(ad-bc)/(2ac+2bd+ad+bc)`.

Apply this to the three target symbols.

Symbol 1:

`tan Delta_1 = sqrt(3)*a/[2Q_E+a+2b]`.

Symbol 2:

`tan Delta_2 = sqrt(3)*(a+b)/[2Q_E-a+b]`.

Symbol 3:

`tan Delta_3 = sqrt(3)*b/[2Q_E-2a-b]`.

Since `Q_E/r^2->1` uniformly and `Delta=O(1/r)`,

`r(Delta-tan Delta)->0`.

At macroscopic angle `theta`, define

`A=cos theta-sin theta/sqrt(3)`,

`B=2sin theta/sqrt(3)`.

Then the symbol-conditioned weight limits are

`ell_1=(sqrt(3)/2)A=(sqrt(3)cos theta-sin theta)/2`,

`ell_2=(sqrt(3)/2)(A+B)=(sqrt(3)cos theta+sin theta)/2`,

`ell_3=(sqrt(3)/2)B=sin theta`.

## 8. Symbol densities and the Young law

Use the exact block-count identities and differentiate the scaled coordinate functions.

On the left half-sector:

`h_1(theta)=cos theta/sqrt(3)-sin theta`,

`h_2(theta)=sin theta+cos theta/sqrt(3)`,

and

`h_1+h_2=g`.

On the right half-sector:

`h_2(theta)=2cos theta/sqrt(3)`,

`h_3(theta)=sin theta-cos theta/sqrt(3)`,

and again

`h_2+h_3=g`.

Thus the correct local two-scale law is

Left:

`Y_theta=(h_1/g)delta_(ell_1)+(h_2/g)delta_(ell_2)`.

Right:

`Y_theta=(h_2/g)delta_(ell_2)+(h_3/g)delta_(ell_3)`.

In every open half-sector, both relevant symbol densities are positive on positive-measure subintervals and the two weight atoms are distinct except at symmetry endpoints. Hence a single generic individual-edge pointwise limit is false.

The conditional mean nevertheless collapses exactly:

Left:

`h_1 ell_1+h_2 ell_2=1`.

Right:

`h_2 ell_2+h_3 ell_3=1`.

Therefore

`integral w dY_theta=1/g(theta)`.

This is the macroscopic source-weight profile.

At an axis, `g=2/sqrt(3)` and `1/g=sqrt(3)/2`, recovering AN's axis limit.

At a sector bisector, `g=1` and `1/g=1`, recovering AN's central limit.

## 9. Positive limiting variance

Let

`m_infty=kappa_perp/kappa_E`.

### 9.1 Macro block-average variance

The macro weight is `w_macro=1/g`.

By D6 and reflection, reduce the second moment to twelve copies of `0<=theta<=pi_source/6`:

`E_[hat_nu](w_macro^2)`

`= [12/(2kappa_E)] integral_0^(pi_source/6) [1/g(theta)] dtheta`.

On this interval `g=2cos theta/sqrt(3)` and `kappa_E=2sqrt(3)` as a secondary algebraic display of `kappa_E^2=12`, `kappa_E>0`.

Using the source-side identity

`integral_0^(pi_source/6) sec theta dtheta=log(sqrt(3))`,

we obtain

`E_[hat_nu](w_macro^2)=(3/4)log 3`.

Therefore

`Var_macro=(3/4)log 3-(kappa_perp/kappa_E)^2>0`.

Positivity is structural: `1/g` is nonconstant on a set of positive target-limit measure.

### 9.2 Actual edge-level variance

On the left half-sector the conditional Young second moment simplifies to

`integral w^2 dY_theta=3/4+sin^2 theta`.

The right half is its reflection.

Integrating with density `g/(2kappa_E)` over the full circle yields

`E_edge(w^2)=5/6`.

Hence the actual discrete edge variance satisfies

`(1/T_r)sum_k(w_(r,k)-bar_w_r)^2`

`-> Var_edge=5/6-(kappa_perp/kappa_E)^2>0`.

The difference

`Var_edge-Var_macro=5/6-(3/4)log 3`

is positive because it is exactly the integrated conditional Young-measure variance. No decimal estimate of `pi_source` is used.

Thus the taskbook candidate `(3/4)log 3` is correct for the squared macro block-average profile, but not for the second moment of individual edge weights.

## 10. Semantic firewalls

- Target canonicality remains AL's theorem and is never reopened.
- Source angle, trigonometry, `sqrt(3)`, `log`, source arc measure, and `kappa_perp` occur only in the compatibility analysis.
- Target circumference remains minimal legal-turn count.
- `kappa_perp` is not identified with `kappa_E`.
- No theorem about standard real `pi` is asserted.
- AM fibers remain relational closed fibers; no bijective point map is introduced.
- The generic local edge-weight object is explicitly two-scale/Young rather than a falsely imposed single pointwise profile.

## 11. Final theorem status before replay

The symbolic theorem package proves:

`FULL_MACROSCOPIC_BRC_DENSITY_PROFILE_PROVED__NONCONSTANT_RADON_NIKODYM_LIMIT__POSITIVE_LIMITING_VARIANCE`.

Deterministic replay is implementation validation only and cannot alter these theorem statements.
