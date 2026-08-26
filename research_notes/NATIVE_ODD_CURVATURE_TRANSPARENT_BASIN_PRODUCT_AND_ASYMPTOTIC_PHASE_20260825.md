# Odd-curvature filament: exact transparent-basin product and infinite-dimension phase theorem

Status: `FREE_RESEARCH_EXACT_PRODUCT + CLASSICAL_ASYMPTOTIC_INPUT / EXTERNAL_NOVELTY_UNRESOLVED / NOT_CANONICAL_ENTERPRISE_GEOMETRY`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Depends on:

- `NATIVE_FILAMENT_ODD_CURVATURE_DEFORMATION_MASTER_THEOREM_20260825.md`;
- `NATIVE_FILAMENT_ODD_CURVATURE_BREAKER_PHASE_DIAGRAM_MOD60_20260825.md`;
- `NATIVE_ODD_SECTOR_SHELL_ALLOCATOR_CENTRAL_FILAMENT_PHASE_THEOREM_20260825.md`.

Only `B=3` is the current native Enterprise tri-sector specialization. Other odd `B` are controlled deformation/comparator families.

## 1. Transparent residue basin for a finite wheel

Let

`F_B(H,r)=H+(B*r^2+eps(r))/2`

with positive odd `B`.

For squarefree positive integer

`M=product_(q in S) q`,

define the **full-filament transparent basin**

`T_B(M)`

as the set of residue classes `H mod M` such that

`gcd(F_B(H,r),M)=1`

for every integer shell `r`.

Let

`Theta_B(M)=|T_B(M)|`.

For one prime channel q, let

`tau_B(q)=Theta_B(q)`.

## 2. Exact one-prime factors

The previous phase theorem gives the complete local factor.

### q=2

`tau_B(2)=1` if `B=3 mod4`, otherwise0.

### q=3

`tau_B(3)=1` if `3|B`, otherwise0.

### q=5

- if `5|B`, `tau_B(5)=3`;
- if `B` is a nonzero quadratic residue mod5, `tau_B(5)=1`;
- if `B` is a quadratic nonresidue mod5, `tau_B(5)=0`.

### odd q>=7

If `q|B`,

`tau_B(q)=q-2`.

If `q` does not divide B,

`tau_B(q)=[q-3 + Legendre(B/q)+Legendre(-B/q)]/4`.

In particular `tau_B(q)>0` for every `q>=7`.

## 3. Exact CRT product theorem

Transparency modulo distinct prime factors is independent under CRT:

an `H mod M` is transparent to the entire wheel iff its projection `H mod q` is transparent for every `q|M`.

Therefore

`T_B(M) ~= product_(q|M) T_B(q)`

and

`Theta_B(M)=product_(q|M) tau_B(q)`.

This is an exact finite-dimensional formula.

Consequently

`Theta_B(M)=0`

iff

`M` contains at least one universal breaker prime for B.

Thus the earlier finite-wheel connectivity iff theorem is the zero/nonzero shadow of this exact basin-cardinality product.

## 4. Primorial collapse tower

Let

`P_d=product_(i=1)^d p_i`

be the first-d-prime primorial.

Then

`Theta_B(P_d)=product_(i=1)^d tau_B(p_i)`.

The four first-breaker phases become exact extinction dimensions:

- first breaker2 -> `Theta_B(P_d)=0` for all `d>=1`;
- first breaker3 -> zero for all `d>=2`;
- first breaker5 -> zero for all `d>=3`;
- no-breaker phase -> `Theta_B(P_d)>0` for every finite `d`.

For the native coefficient `B=3`,

`tau_3(2)=1`,

`tau_3(3)=1`,

`tau_3(5)=0`,

so

`Theta_3(P_1)=1`,

`Theta_3(P_2)=1`,

`Theta_3(P_d)=0` for every `d>=3`.

Freeze:

`NATIVE B=3 TRANSPARENT INFINITE-FILAMENT BASIN EXTINGUISHES EXACTLY AT COLLAPSE DIMENSION3`.

## 5. No-breaker sector classes

Among odd B modulo60 the no-breaker classes are exactly

`B=15,39,51 mod60`.

For any such B, all local factors are positive, so

`Theta_B(P_d)>0`

for every d.

Thus no finite number of prime-exclusion channels can remove every infinite filament in these deformation phases.

## 6. Generic high-prime local factor

Fix one no-breaker B. For every sufficiently large prime q not dividing `2B`, let

`chi_B(q)=Legendre(B/q)`,

`chi_minusB(q)=Legendre(-B/q)`.

Then

`tau_B(q)/q`

`=1/4 * [1 + (-3+chi_B(q)+chi_minusB(q))/q]`.

Because `B=3 mod4` in every no-breaker phase, B is not a square; `-B` is also not a rational square. Hence the associated quadratic Dirichlet characters are nonprincipal after passing to their primitive representatives.

## 7. Asymptotic transparent-basin density

Let

`P(x)=product_(q<=x) q`

and

`D_B(x)=Theta_B(P(x))/P(x)`.

Remove the finitely many primes dividing `2B` and the small channels. Using the generic factor above,

`D_B(x)`

is a finite positive constant times

`4^(-pi(x)) * product_q<=x [1+(-3+chi_B(q)+chi_minusB(q))/q]`.

Now compare the second product with

`product_q<=x (1-1/q)^3 (1-chi_B(q)/q)^(-1) (1-chi_minusB(q)/q)^(-1)`.

The local ratio is `1+O(q^-2)`, so the ratio product converges absolutely to a positive finite constant.

Mertens' product theorem and the nonvanishing of `L(1,chi)` for nonprincipal Dirichlet characters therefore give a positive constant `C_B` such that

`D_B(x) ~ C_B * 4^(-pi(x)) / (log x)^3`.

Equivalently, at collapse dimension d (`x=p_d`),

`Theta_B(P_d)/P_d ~ C_B * 4^(-d) / (log p_d)^3`.

Using `p_d ~ d log d`, this is also

`density_d = 4^(-d) * (log d)^(-3+o(1))`

up to a positive B-dependent constant.

## 8. Absolute basin grows despite density collapse

The exact ambient transverse space has size `P_d`.

Thus

`Theta_B(P_d) ~ C_B * P_d / [4^d (log p_d)^3]`.

By the prime number theorem,

`log P_d = theta(p_d) ~ p_d ~ d log d`.

Therefore

`log Theta_B(P_d)`

`= log P_d - d log4 -3 log log p_d + O(1)`

`tends to +infinity`.

Hence in every no-breaker phase:

`Theta_B(P_d) -> infinity`,

while simultaneously

`Theta_B(P_d)/P_d -> 0`.

Freeze the phase name:

`SPARSE-EXPANDING TRANSPARENT BASIN`.

The basin occupies an asymptotically vanishing fraction of the high-dimensional residue carrier, but contains an unbounded and rapidly growing number of complete infinite-filament states.

## 9. Infinite-dimensional phase dichotomy

The odd-curvature family therefore has two qualitatively different collapse-channel behaviors.

### Extinction phase

If `Break(B)` is nonempty, let `q_*` be its smallest element and let `d_*` be its prime index.

Then

`Theta_B(P_d)>0` for `d<d_*`,

and

`Theta_B(P_d)=0` for all `d>=d_*`.

The extinction dimensions are only

`d_*=1,2,3`

corresponding to breaker primes

`2,3,5`.

### Sparse-expanding phase

If `Break(B)` is empty (`B=15,39,51 mod60`), then

`Theta_B(P_d)>0` for every d,

`Theta_B(P_d)->infinity`,

but

`Theta_B(P_d)/P_d ->0`

with exact leading thinning scale

`4^(-d)/(log p_d)^3`.

So the sector/curvature parameter selects a genuine high-dimensional basin phase transition:

`FINITE-DIMENSION EXTINCTION`

versus

`INFINITE-DIMENSION SPARSE EXPANSION`.

## 10. d=19 comparison

For the first19 prime channels (`p_19=67`):

- native `B=3`: `Theta=0` from d=3 onward;
- `B=15`: `Theta=13,948,526,592,000`;
- `B=39`: `Theta=19,670,999,040,000`;
- `B=51`: `Theta=29,208,453,120,000`.

The corresponding d=19 basin densities are approximately

- B15: `1.7750e-12`;
- B39: `2.5032e-12`;
- B51: `3.7169e-12`.

Thus the no-breaker phases are already extremely sparse by dimension19, while retaining trillions of fully transparent transverse residue classes.

## 11. Boundary

CRT, Mertens' theorem, Dirichlet characters, `L(1,chi)!=0`, and the prime number theorem are classical analytic number theory.

No novelty claim is made for those tools or for Euler-product asymptotics in isolation.

The research-specific candidate is the exact coupling

`odd sector / curvature phase`

`-> local transparent-class formula`

`-> finite-wheel product basin`

`-> finite-dimensional extinction OR sparse-expanding infinite-dimensional phase`.

The native tri-sector specialization lies in the extinction-at-dimension3 phase. External novelty of the coupled phase theorem remains unresolved pending independent statement-level literature review.