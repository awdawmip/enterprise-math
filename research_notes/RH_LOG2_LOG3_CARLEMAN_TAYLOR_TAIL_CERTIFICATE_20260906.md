# RH log2 -> log3 Carleman-regular Taylor tail certificate

Status: `TASK_RESEARCH / EXACT ANALYTIC BOUND + INTERVAL NUMERICAL CERTIFICATE / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil square-shell / first step log2->log3 / archimedean regular cross / interval tail certificate`

## 0. Purpose

`RH_ARCH_BOUNDARY_CARLEMAN_PRINCIPAL_DECOMPOSITION_20260906.md` isolates the noncompact touching-boundary archimedean carrier

`K_inf(s) = -1/(2s) + G(s)`

for `s>0`, with

`G(z) = -exp(-z/2)/(1-exp(-2z)) + 1/(2z)`
`     = -exp(z/2)/(2 sinh z) + 1/(2z)`.

The singularity of `G` at zero is removable and the nearest remaining poles are at `+/- i pi`. Thus `G` is analytic on `|z|<pi`.

This note converts that qualitative analyticity into a completely explicit, interval-certifiable operator-norm tail for the first exact square-shell step

`H_log2 -> H_log3`.

The result closes the regular-arch cross-tail part of the current threshold-inertia program at a numerically useful scale. It does not certify the diagonal blocks or the final inertia.

BRC / reuse:

- retain `prime`, `Carleman principal`, `regular arch`, and `pole` provenance separately;
- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED`;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` for finite Taylor repair capacity;
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; only the explicitly bounded tail is discarded from the finite reference matrix.

## 1. Complete first-step separation range

Put

`L = log 2`,
`delta = log(3/2)`,
`X = L + (L+delta) = log 6`.

For the old window `[-log2,log2]` and the two new shell intervals in `[-log3,-log2] union [log2,log3]`, every old/shell distance satisfies

`0 <= |x-y| <= X=log6`.

Numerically and exactly in ordering,

`log6 < 3 < pi`.

Hence the radius `r=3` circle lies strictly between the full real separation interval and the first complex poles of `G`.

## 2. Explicit lower bound for `|sinh z|` on `|z|=r`

Write

`z=x+i y`, `x^2+y^2=r^2`.

The exact identity

`|sinh(x+i y)|^2 = sinh^2 x + sin^2 y`

implies a uniform elementary lower bound.

If

`|x| >= r/sqrt(2)`,

then

`|sinh z| >= sinh(r/sqrt(2))`.

Otherwise

`|y| >= r/sqrt(2)`.

For `0<r<pi`, `|y|` lies in `[r/sqrt(2),r]`, where `sin |y|` is positive and its minimum on this interval occurs at an endpoint. Therefore

`|sinh z| >= min(sin(r/sqrt(2)), sin r)`.

Define

`boxed: m(r) := min{sinh(r/sqrt(2)), sin(r/sqrt(2)), sin r}`.

Then for every `|z|=r`, `0<r<pi`,

`boxed: |sinh z| >= m(r) > 0`.

No floating assumption enters this inequality.

## 3. Explicit Cauchy-circle bound for `G`

On `|z|=r`,

`G(z) = -exp(z/2)/(2 sinh z) + 1/(2z)`.

Using

`|exp(z/2)| <= exp(r/2)`,
`|z|=r`,
`|sinh z| >= m(r)`,

we obtain

`boxed: |G(z)| <= Mbar_r}`

with

`boxed: Mbar_r := exp(r/2)/(2 m(r)) + 1/(2r)`.

Thus no numerical maximization of a complex function is required to obtain a rigorous Cauchy bound.

## 4. Taylor remainder theorem

Let

`G(z)=sum_(k>=0) c_k z^k`

and

`P_d(z)=sum_(k=0)^d c_k z^k`.

For `0<=s<=X<r`, Cauchy's coefficient estimate gives

`|c_k| <= Mbar_r / r^k`.

Therefore

`|G(s)-P_d(s)|`
`<= sum_(k=d+1)^infinity Mbar_r (X/r)^k`
`= Mbar_r (X/r)^(d+1)/(1-X/r)`.

Define

`boxed: e_d(r) := Mbar_r (X/r)^(d+1)/(1-X/r)`.

Then

`boxed: sup_(0<=s<=log6) |G(s)-P_d(s)| <= e_d(r)}`.

This applies simultaneously to all four labelled old-sign/shell-sign branch pairs, including the opposite-sign pairs, because their separations also lie in `[0,log6]`.

## 5. Operator-norm consequence

On each ordered branch pair, a degree-`d` polynomial kernel in `+/- (y-x)` has rank at most `d+1`.

Retaining all four branch labels gives the provenance-safe finite-rank bound

`rank(K_d^reg) <= 4(d+1)`.

Let `R_d^reg` be the residual regular-arch cross operator after replacing `G` by `P_d` on all branch pairs. The total old measure is `2L` and total shell measure is `2delta`, so the Hilbert-Schmidt estimate gives

`||R_d^reg||`
`<= ||R_d^reg||_HS`
`<= sqrt((2L)(2delta)) e_d(r)`
`= 2 sqrt(log2 * log(3/2)) e_d(r)`.

Hence

`boxed: ||R_d^reg|| <= 2 sqrt(log2 log(3/2)) e_d(r)}`.

The noncompact Cauchy/Carleman principal carrier is not part of this tail; it remains explicitly in the reference block.

## 6. Interval-certified numerical instance: `r=3`, `d=50`

Take

`r=3`, `d=50`.

Directed interval evaluation of the elementary quantities gives disjoint enclosures

`sinh(3/sqrt2) > 4.111135733186517`,
`sin(3/sqrt2) > 0.8522505081524893`,
`0.14112000805986722 < sin 3 < 0.14112000805986723`.

Therefore the minimum is certified to be

`m(3)=sin 3`.

Interval evaluation then yields

`16.0456661506973139895 < Mbar_3`
`< 16.0456661506973139896`,

and, with `X=log6`,

`e_50(3)`
`< 1.528997379731282e-10`.

Finally,

`boxed: ||R_50^reg|| < 1.62116123736002e-10}`.

The last displayed decimal upper bounds are rounded outward from interval enclosures. The underlying interval computation used only elementary monotone/interval operations on the proved formulas above.

## 7. Correct way to use this certificate

Do **not** use the finite-rank theorem as a `2r` counting penalty if the degree-50 Taylor block can be assembled explicitly in the finite reference matrix.

Instead construct

`B_2^(50) = B_2^prime + B_2^Cauchy + K_50^reg + B_2^pole`

with the pole endpoint channels retained at their exact finite rank, and form

`H_2^(50)(eta)=M_eta(B_2^(50))`.

The full first-step threshold block differs from this by the off-diagonal residual generated by `R_50^reg`, whose Hermitian perturbation norm is exactly `||R_50^reg||` and therefore at most

`1.62116123736002e-10`.

Consequently, if an interval-certified finite threshold matrix has no eigenvalue in

`[-1.62116123736002e-10, +1.62116123736002e-10]`

after all other discretization/integration errors are included in the budget, its inertia is stable under the complete regular-arch remainder.

This is much sharper than discarding the degree-50 Taylor block and paying its full rank as an inertia-count uncertainty.

## 8. What is now closed and what remains open

Closed for the first step:

1. exact isolation of the noncompact Carleman boundary carrier;
2. explicit finite-rank approximation theorem for the complete regular arch cross;
3. explicit elementary Cauchy bound requiring no complex maximization;
4. an interval-certified degree-50 residual operator-norm bound below `1.622e-10`.

Still open:

1. interval-certified construction of the old diagonal block `A_2`;
2. interval-certified construction of the shell diagonal block `D_2`;
3. interval-certified finite matrix for the retained reference cross, including exact prime gates, Carleman principal block, Taylor regular block, and two unreduced pole channels;
4. certified zero gaps / inertia at `eta=0.9,0.99,0.999`;
5. finite-section complement/tail theorem needed to lift Galerkin inertia to the full operator;
6. any conclusion at the RH threshold `eta=1`.

The main analytical blocker has therefore moved from `B`-cross tail control to **certified diagonal-block construction and finite-section complement control**.

## 9. Hard boundaries

- `1.62e-10 REGULAR-ARCH TAIL != TOTAL NUMERICAL ERROR`.
- The Carleman principal carrier is retained exactly and is not hidden in this tail.
- A finite matrix whose floating smallest eigenvalue is around `1e-10` is not certified merely because this one tail is smaller.
- Interval eigenvalue/inertia certification still needs rigorous enclosures for every matrix entry or an equivalent validated factorization.
- Finite-section inertia is not infinite-operator inertia without a separate complement theorem.
- No RH proof is claimed.
