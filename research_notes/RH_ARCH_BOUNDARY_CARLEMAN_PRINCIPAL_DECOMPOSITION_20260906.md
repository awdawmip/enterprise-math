# RH archimedean boundary Carleman principal decomposition

Status: `TASK_RESEARCH / EXACT KERNEL AND OPERATOR DECOMPOSITION + FINITE-RANK REGULAR APPROXIMATION / NOT AN RH PROOF`
Date: `2026-09-06`
Researcher-ID: `EM-DIRECT-7C1A42`
Scope: `RH / Weil square-shell / archimedean old-to-shell cross / Carleman-Hankel boundary carrier / threshold inertia`

## 0. Why this note exists

The previous threshold-ablation note proposed completing the observed

`prime-only threshold inertia ~= full threshold inertia`

by treating the omitted archimedean cross as a finite-rank part plus a small operator-norm tail.

That target is **not valid for the raw continuum archimedean cross as a whole**. The archimedean multiplier has a universal `1/s` off-diagonal kernel singularity at an old/shell boundary. On the two same-sign touching branch pairs this produces a scale-invariant Carleman/Hankel carrier. It is bounded but noncompact, so shrinking the spatial boundary strip does not turn it into an arbitrarily small finite-rank remainder.

The correct split is instead

`ARCH CROSS = UNIVERSAL CAUCHY/CARLEMAN PRINCIPAL CARRIER + ANALYTIC REGULAR PART`,

and the corrected response reference should retain the principal carrier together with the prime comb.

This is a BRC observer-preservation correction: a boundary relation that remains visible at every finer scale may not be erased merely because it occupies a thin spatial strip.

Reuse resolution:

- `T0_BRC`: `REUSE_APPLIED` for labelled old+/old-/shell+/shell- branch provenance;
- `T2_BLOCK_FINITE_CERTIFICATE`: `REUSE_APPLIED` for threshold inertia after the corrected cross split;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`: `REUSE_APPLIED` for explicit finite repair rank of the regular approximation;
- `T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`; the noncompact boundary carrier is retained rather than collapsed;
- Wiener-Hopf/phase-space theorem adapter: `COMPOSE_APPLIED`; no new top-level Enterprise tool family is claimed.

## 1. Archimedean multiplier convention

Use the Fourier convention

`f_hat(tau)=integral_R f(x) exp(-i tau x) dx`

and the archimedean Mellin/Fourier multiplier appearing in the current Weil implementation,

`h_inf(tau) = Re psi(1/4 + i tau/2) - log pi`,

where `psi=Gamma'/Gamma`.

The corresponding quadratic contribution is

`D_inf(f,g) = (1/(2pi)) integral_R h_inf(tau) f_hat(tau) conjugate(g_hat(tau)) d tau`.

For `Re z>0`, the standard digamma integral representation gives

`psi(z) = -gamma + integral_0^infinity [e^(-t)-e^(-z t)]/(1-e^(-t)) dt`.

The pieces independent of `tau` are local distributions at zero separation. For cross terms between old and shell subspaces, whose supports are disjoint up to measure-zero endpoints, these local terms vanish. The nonlocal inverse Fourier transform is therefore exact away from zero.

## 2. Exact off-diagonal archimedean kernel

For `s!=0`,

`boxed: K_inf(s) = - exp(-|s|/2)/(1-exp(-2|s|))`

or equivalently

`boxed: K_inf(s) = - exp(|s|/2)/(2 sinh |s|)}`.

### Proof

The only nonlocal `tau`-dependent term in the digamma representation is

`- integral_0^infinity a(t) cos(tau t/2) dt`,

with

`a(t)=exp(-t/4)/(1-exp(-t))`.

Under the declared Fourier convention,

`F^{-1}[cos(tau t/2)](s)`
`= (1/2)[delta(s-t/2)+delta(s+t/2)]`.

Integrating over `t` gives, for `s>0`,

`-a(2s) = -exp(-s/2)/(1-exp(-2s))`,

and evenness gives the formula for `s<0`.

This agrees with the standard multiplicative Weil archimedean distribution after the autocorrelation double-counting is taken into account.

## 3. Exact singular/regular split

For positive separation `s>0`, define

`G(s) := K_inf(s) + 1/(2s)`.

Then

`boxed: K_inf(s) = -1/(2s) + G(s)}`.

The apparent singularity of `G` at zero is removable, with

`G(0)=-1/4`,

and its Taylor expansion begins

`G(s) = -1/4 + s/48 + s^2/32 - 7 s^3/11520 + ...`.

As a complex function,

`G(z) = -exp(-z/2)/(1-exp(-2z)) + 1/(2z)`

is analytic in

`|z|<pi`,

because the zero at `z=0` has been removed and the nearest remaining poles are at

`z=+/- i pi`.

Thus the entire noncompact obstruction is isolated by the single universal Cauchy term `-1/(2s)`.

## 4. Square-shell boundary coordinates

At the step

`H_n -> H_(n+1)`

put

`L=log n`, `delta=log((n+1)/n)`.

Retain four labelled branches:

- old positive: `[0,L]`;
- old negative: `[-L,0]`;
- shell positive: `[L,L+delta]`;
- shell negative: `[-L-delta,-L]`.

On the touching positive pair write

`u=L-x >=0`, `v=y-L >=0`.

Then

`|y-x|=u+v`

and the singular principal cross kernel is exactly

`boxed: -1/[2(u+v)]`.

The negative touching pair has the identical formula after reflection.

Therefore the archimedean old/shell coupling contains two labelled copies of a truncated Carleman/Hankel boundary operator.

The opposite-sign branch pairs are separated by a positive distance and have no boundary singularity, but they should remain separately labelled until a safe recoalescence is proved.

## 5. Exact Carleman-to-Wiener-Hopf transform

Let the full Carleman operator on `L2(R_+)` be

`(C f)(v)=integral_0^infinity f(u)/(u+v) du`.

Use logarithmic boundary coordinates

`u=e^(-s)`, `v=e^(-t)`

and the unitary map

`(U f)(s)=e^(-s/2) f(e^(-s))`.

Then an exact calculation gives

`(U C U^(-1) g)(t)`
`= integral_R g(s) / [2 cosh((t-s)/2)] ds`.

Hence the Carleman operator is convolution in the logarithmic boundary coordinate. The Fourier transform of

`1/[2 cosh(x/2)]`

is

`pi/cosh(pi xi)`.

Therefore the singular archimedean principal carrier `-(1/2)C` has the explicit boundary symbol

`boxed: b_inf,principal(xi) = - pi/[2 cosh(pi xi)]`.

For finite old/shell boundary intervals, the logarithmic map turns the same carrier into a truncated Wiener-Hopf operator: the same convolution symbol with half-line cutoffs determined by the two interval lengths.

This is the first explicit non-prime principal symbol available for the square-shell threshold-block route without whitening by `A^(-1/2)` or `D^(-1/2)`.

## 6. Why the raw arch cross is not a small-norm tail

The touching Carleman carrier is noncompact.

### Direct dilation proof

Fix a nonzero `f` supported in `(1,2)` and choose `a_j -> 0`. Put

`f_j(u)=a_j^(-1/2) f(u/a_j)`.

For all large `j`, `f_j` lies in any fixed old boundary interval `(0,L)` and

`f_j -> 0` weakly in `L2`.

For `v=a_j w`, homogeneity gives

`(C f_j)(a_j w)=a_j^(-1/2) (C f)(w)`.

Therefore the output norm on `v in (a_j,2a_j)` is independent of `j` and strictly positive. A compact operator would send the weakly-null sequence `f_j` to a strongly-null sequence, contradiction.

Consequences:

`RAW TOUCHING ARCH CROSS != FINITE_RANK + ARBITRARILY_SMALL_NORM_TAIL`.

`THIN BOUNDARY STRIP != SMALL OPERATOR NORM`.

This is a genuine correction to the previous prime-only ablation completion target.

It does **not** contradict the floating observation that the arch-only *near-critical normalized response count* is small. Raw cross norm and threshold-normalized dangerous rank are different observables.

## 7. Corrected threshold reference block

Write the full old-to-shell cross as

`B_n = B_n^prime + B_n^arch + B_n^pole`.

The corrected decomposition is

`B_n^arch = B_n^Cauchy + B_n^reg`,

where `B_n^Cauchy` uses the exact kernel `-1/(2|x-y|)` on the labelled old/shell branch pairs. Its two same-sign blocks are the noncompact Carleman principal carriers above; its opposite-sign blocks are separated and compact.

Define

`boxed: B_n^ref := B_n^prime + B_n^Cauchy`.

Then

`B_n = B_n^ref + B_n^reg + B_n^pole`.

The threshold block to certify first should therefore be

`H_n^ref(eta)=M_eta(B_n^ref)`,

not the prime-only `M_eta(B_n^prime)`.

The prime-only ablation table remains useful numerical evidence about which arithmetic component dominates after normalization, but a continuum proof cannot justify it by claiming the entire arch cross has small raw norm.

## 8. Special advantage of the first exact step `log 2 -> log 3`

For `n=2`,

`L=log 2`, `delta=log(3/2)`.

Every old/shell separation satisfies

`0 <= |x-y| <= log 6`.

Crucially,

`boxed: log 6 < pi`.

Therefore the regular function `G` is analytic on a complex disk strictly larger than the complete first-step separation range.

Let

`X=log 6`

and choose any

`X<r<pi`.

If

`M_r=max_(|z|=r) |G(z)|`

and `P_d` is the degree-`d` Taylor polynomial of `G` at zero, Cauchy's estimate gives the uniform remainder

`boxed: sup_(0<=s<=X) |G(s)-P_d(s)|`
`<= M_r * (X/r)^(d+1) / (1-X/r)`.

Thus the regular archimedean cross is exponentially compressible in the first exact square-shell step.

### Finite-rank consequence

On any fixed ordered branch pair, `s=+/-(y-x)`. A degree-`d` polynomial kernel

`P_d(+/-(y-x))`

has operator rank at most `d+1`, because it can be collected as

`sum_(ell=0)^d y^ell q_ell(x)`.

With four labelled old-sign/shell-sign branch pairs, a provenance-safe crude bound is therefore

`rank(K_d^reg) <= 4(d+1)`.

If the uniform kernel remainder is `e_d`, then the full regular cross remainder obeys the Hilbert-Schmidt, hence operator-norm, bound

`boxed: ||R_d^reg|| <= 2 sqrt(L delta) e_d}`

because the total old measure is `2L` and the total shell measure is `2delta`.

The global pole contribution is rank one in the current Weil decomposition, hence its old/shell cross has rank at most one.

Therefore, for the first step,

`B_2 = B_2^ref + K_d^reg + R_d^reg + B_2^pole`

with

`rank(K_d^reg)+rank(B_2^pole) <= 4(d+1)+1`

and the explicit norm tail above.

This is exactly the rank-plus-small-tail structure needed by the previous threshold-inertia theorem — **after** the universal Cauchy/Carleman carrier is moved into the reference block.

## 9. Exact first-step prime comb

The previous square-shell port decomposition gives the bare prime translation multiplier

`b_n^prime(xi)=sum_(1<m<=n(n+1)) Lambda(m) m^(-1/2+i xi)`

up to the fixed branch sign/conjugation convention and the exact support gates.

For `n=2`, only

`m in {2,3,4,5}`

have nonzero von Mangoldt weight below or at `6`. Hence

`b_2^prime(xi)`
`= (log 2)/sqrt(2) * 2^(i xi)`
`+ (log 3)/sqrt(3) * 3^(i xi)`
`+ (log 2)/2 * 4^(i xi)`
`+ (log 5)/sqrt(5) * 5^(i xi)`.

This is an exact finite arithmetic carrier before support truncation. It must remain coupled to the branch gates; the formula is not permission to replace the actual truncated cross by an unrestricted multiplier.

Combining it with the universal arch boundary symbol produces the first concrete no-whitening reference ingredients:

`PRIME TRANSLATION COMB + ARCH CAUCHY/CARLEMAN BOUNDARY CARRIER`.

## 10. Corrected finite inertia certificate

Let

`H_2^ref(eta)=M_eta(B_2^ref)`.

For a chosen Taylor degree `d`, put

`r_d=4(d+1)+1`

and

`eps_d=2 sqrt(log(2) log(3/2)) * e_d`.

The low-rank-plus-tail inertia theorem from

`RH_THRESHOLD_BLOCK_ABLATION_MATRIX_SYMBOL_ROUTE_20260906.md`

then gives

`N_(H_2^ref(eta))((−infinity,−eps_d)) - 2 r_d`
`<= r_full(eta;2)`
`<= N_(H_2^ref(eta))((−infinity,eps_d)) + 2 r_d`,

with the lower bound truncated at zero.

This is deliberately conservative. The four branch polynomial blocks share structure and the pole vector is symmetry constrained, so the practical repair rank can be lower after a basis-specific exact audit. The displayed bound is a theorem-level safe envelope.

## 11. New matrix-symbol route

The previous no-whitening idea used a matrix-valued threshold symbol

`m_eta(x,xi)=[[eta^2 a,b],[conj(b),d]]`.

The present decomposition identifies a missing explicit part of `b`.

At a same-side old/shell boundary, the reference cross symbol should contain

`b_ref = b_prime + b_Carleman`

with

`b_Carleman(xi) = -pi/[2 cosh(pi xi)]`

in logarithmic boundary coordinates, plus the exact prime translation/gating symbol in its own declared coordinate chart.

The remaining regular arch and pole terms are then finite-rank/compact corrections at the first step.

This replaces the earlier overly optimistic slogan

`PRIME THRESHOLD BLOCK + SMALL ARCH TAIL`

by the structurally correct target

`PRIME + UNIVERSAL CARLEMAN PRINCIPAL THRESHOLD BLOCK + COMPRESSIBLE REGULAR ARCH/POLE REPAIR`.

## 12. What this does and does not establish

Established exactly:

1. the off-diagonal archimedean kernel from the current digamma multiplier;
2. its `-1/(2s)` singular principal term;
3. the touching old/shell Carleman/Hankel boundary carrier;
4. its exact logarithmic Wiener-Hopf symbol `-pi/(2 cosh(pi xi))`;
5. noncompactness of the raw touching principal carrier;
6. analyticity radius `pi` of the regular remainder;
7. exponential finite-rank compressibility of the complete regular remainder at `log2 -> log3` because `log6<pi`;
8. an explicit theorem-level rank/norm budget for transferring threshold inertia from the corrected reference block to the full first-step block.

Not established:

- the inertia of `H_2^ref(eta)`;
- a proof that prime coupling dominates the Carleman principal carrier after normalization;
- an infinite-operator truncation theorem for finite Galerkin inertia;
- `sigma_max(C_2)<1`;
- RH.

## 13. Smallest unresolved unit

The next computation/theorem should no longer try to certify a prime-only threshold block first.

Construct a support-exact finite section of

`H_2^ref(eta)=M_eta(B_2^prime+B_2^Cauchy)`

for `eta in {0.9,0.99,0.999}`, with the four branch labels retained, and certify:

1. its negative inertia;
2. its zero spectral gap;
3. the interval bound `M_r` for one convenient `r in (log6,pi)` and hence a rigorous `eps_d`;
4. the basis-specific rank of the regular Taylor block and pole cross;
5. the full-response inertia sandwich.

Only after that certificate exists should the phrase `prime-dominated threshold response` be promoted beyond floating evidence.

## 14. Hard boundaries

- `ARCHIMedean SPATIAL THINNESS != SMALL OPERATOR NORM`.
- `NONCOMPACT CARLEMAN PRINCIPAL CARRIER != FINITE-RANK REPAIR`.
- `PRIME-ONLY FLOATING ABLATION ~= FULL FLOATING ABLATION` is evidence, not a norm theorem.
- The Cauchy/Carleman split is an operator decomposition, not an RH proof.
- Finite-section inertia still requires a certified complement/tail theorem before it controls the infinite operator.
- Branch gates, signs, conjugations, parity and inversion provenance must be retained until an exact recoalescence certificate is supplied.

## 15. External theorem/convention anchors

- Current truncated-Weil implementations use the archimedean multiplier `Re psi(1/4+i tau/2)-log pi` and a rank-one pole correction.
- The classical Carleman operator with kernel `1/(u+v)` is diagonalized by the Mellin transform with multiplier `pi/cosh(pi xi)`.
- Classical Hankel/Carleman spectral theory confirms that the `1/t` singularity is the noncompact principal carrier, while sufficiently regular error kernels are compact under the relevant hypotheses.

The derivations above are self-contained once these standard identities and the declared Fourier convention are fixed.
