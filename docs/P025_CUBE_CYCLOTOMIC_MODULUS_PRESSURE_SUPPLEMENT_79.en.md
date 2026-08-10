# P025 Supplement 79 — Projective Threshold Pressure on Cyclotomic Congruence Moduli

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-cyclotomic-stage76`  
Depends on: P025 Supplements 75–78  
Hard block: `NONE`

## 1. Threshold pressure should control the congruence modulus, not only its support

Stages 76–78 show that repeated prime-cube cyclotomic factors live on primes `1 mod 6`, generate root-of-unity congruence signatures, and carry a finite pair-incidence cost.

The remaining question is whether a large projective value forces the repeated congruence modulus itself to be large.

For cube sums the answer is direct. For cube differences the pressure splits between centered-radius multiplicity and cyclotomic multiplicity.

## 2. P025-T153 — cube-sum activation forces a large `Phi_6` repeated modulus

Stage 75 gives

\[
\rho_+
=
\frac{\varepsilon_B g_B m(E)}{6\operatorname{rad}(B)},
\qquad
E=\Phi_6(p,q),
\]

where

\[
\varepsilon_B g_B\le6.
\]

If

\[
\rho_+\ge T,
\]

then

\[
\boxed{m(E)\ge T\operatorname{rad}(B).}
\]

Let the repeated prime-power part of `E` be

\[
M_E=\prod_{v_r(E)\ge2}r^{v_r(E)}.
\]

If `rho_+>=T>=1`, then `m(E)>1`, so the repeated support is nonempty. Stage 76 gives every repeated prime `r>=7`.

Also

\[
M_E
=
m(E)
\prod_{v_r(E)\ge2}r.
\]

Therefore

\[
\boxed{
M_E\ge7m(E)\ge7T\operatorname{rad}(B).
}
\]

Thus a high cube-sum projective state automatically creates a large order-six congruence modulus.

## 3. P025-T154 — cube-difference pressure splits between radius and `Phi_3`

Stage 75 gives

\[
\rho_-
=
\frac{\varepsilon_A g_A m(A)m(D)}{6B},
\qquad
D=\Phi_3(p,q),
\]

with

\[
\varepsilon_Ag_A\le6.
\]

Hence

\[
\rho_-\ge T
\Longrightarrow
\boxed{m(A)m(D)\ge TB.}
\]

Fix any integer split horizon

\[
1\le H\le TB.
\]

Then either

\[
\boxed{m(A)\ge H}
\]

or, if `m(A)<H`,

\[
Hm(D)>TB.
\]

The latter inequality forces `m(D)>1`. Let

\[
M_D=\prod_{v_r(D)\ge2}r^{v_r(D)}.
\]

Stage 76 again gives `M_D>=7m(D)`, so the second branch satisfies

\[
\boxed{
H M_D>7TB.
}
\]

Therefore every active cube-difference state obeys the exact dichotomy

\[
\boxed{
m(A)\ge H
\quad\text{or}\quad
H M_D>7TB.}
\]

The projective resource must be paid either by centered-radius multiplicity or by a large order-three congruence modulus.

## 4. P025-C24 — P018 size range eliminates the radius branch at `H=A+1`

Suppose the same centered prime pair lies in the canonical P018 size range

\[
q=B-A>A^2.
\]

Then

\[
A^2<B
\]

and trivially

\[
m(A)\le A.
\]

Choose

\[
\boxed{H=A+1.}
\]

Because `A+1<=B<=TB` for `T>=1`, P025-T154 applies. The radius branch

\[
m(A)\ge A+1
\]

is impossible.

Thus any P018-range cube-difference activation must satisfy

\[
\boxed{
(A+1)M_D>7TB.
}
\]

So on this overlap, projective pressure is forced entirely into the `Phi_3` root-of-unity congruence modulus.

This is a conditional theorem. It does not assert that such activated overlap pairs are abundant or even that a small example must exist.

## 5. Exact examples outside the P018 overlap

For

\[
(q,p)=(5,101),
\qquad
(B,A)=(53,48),
\]

Stage 75 gives

\[
m(A)=8,
\qquad
m(D)=7,
\qquad
M_D=7^2=49.
\]

At threshold one:

- choosing `H=8` lands in the radius-residual branch;
- choosing `H=9` forces the cyclotomic branch and indeed
  \[
  9\cdot49>7\cdot53.
  \]

Thus the split horizon is a genuine task parameter: it decides which hidden resource is treated as "large" and which is pushed into the congruence state.

## 6. Relation to Stage 78 incidence cost

Once the cyclotomic branch is selected, Stage 78 converts the modulus into a finite search-space bound.

For cube sum, P025-T153 gives a threshold-dependent lower bound on `M_E` directly.

For cube difference, P025-T154 gives the same after conditioning on the radius-residual branch being below `H`.

Thus the pipeline is

\[
\boxed{
\text{projective threshold}
\to
\text{residual/modulus split}
\to
M
\to
2^{\omega(M)}\text{ root classes}
\to
\text{finite pair-incidence envelope}.
}
\]

This is more informative than treating a repeated quadratic factor as a Boolean event.

## 7. Precision interpretation

The split horizon `H` is another task-relative precision knob.

- below `H`, radius multiplicity is treated as cheap/background state;
- above `H`, it becomes an explicit exceptional coordinate;
- if the radius remains below `H`, the same projective pressure is forced into a larger congruence modulus, which makes the prime-base quotient much more selective.

In the P018 overlap, the independent size theorem supplies a natural horizon `H=A+1` that completely removes one branch.

This is a direct example of an external/cross-route guard converting a two-resource ambiguity into a single theorem-native precision channel.

## 8. Prior-art / novelty discipline

The cyclotomic factorization and repeated-prime congruence theory are classical. The P018 size theorem retains canonical P018 ownership. P025-T153–T154 are elementary consequences of the project-specific Stage-75 projective formulas plus Stage-76 support rigidity.

No generic large-sieve or prime-distribution result is claimed.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_prime_cube_modulus_pressure.py`;
- `tests/test_abc_prime_cube_modulus_pressure.py`.

## 10. Next frontier

No hard block exists. Continue with:

1. combine P025-T153/T154 with Stage-78 incidence bounds and optimize the split horizon `H` for finite prime-base universes;
2. search whether the P018 overlap cube-difference condition is nonempty in meaningful ranges before investing in asymptotic counting;
3. compare radius-residual versus congruence-modulus precision as two branches of the same future query;
4. keep the Stage-79 generation independent of the frozen Stage61–75 PR payload.
