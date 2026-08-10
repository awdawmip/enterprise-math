# P025 Supplement 71 — Complement-Capacity Stratification of Projective Failures

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 51, 64, 70  
Hard block: `NONE`

## 1. Stage 64 erased one exact gain

For an active cyclic projective term, write the active component as `n_i` and the two complementary components as `n_j,n_k`.

With

\[
R_i=\operatorname{rad}(n_i),
\qquad
C_i=C(n_i),
\]

the active term is

\[
\rho_i
=
\frac{m_i}{R_kC_j+R_jC_k}.
\]

Stage 64 used only `C_j,C_k>=1` to produce a pair-radical state. The full denominator contains a stronger, orientation-dependent capacity coordinate.

## 2. P025-T140 — dual complement-capacity pair bounds

Fix an integer threshold

\[
T\ge1
\]

and suppose

\[
\rho_i\ge T.
\]

Then

\[
m_i
\ge
T(R_kC_j+R_jC_k).
\]

Keeping the two summands separately gives

\[
m_i\ge TR_kC_j
\]

and

\[
m_i\ge TR_jC_k.
\]

Since `m_i=n_i/R_i`, these are exactly

\[
\boxed{
R_iR_k\le\frac{n_i}{TC_j},
}
\]

and

\[
\boxed{
R_iR_j\le\frac{n_i}{TC_k}.
}
\]

Thus each complement capacity controls the pair radical containing the *other* complement.

## 3. P025-C16 — one pair gains the maximum complement capacity

Set

\[
\boxed{H_i=\max\{C_j,C_k\}.}
\]

If `C_j>=C_k`, use the first inequality and the pair `(i,k)`; otherwise use `(i,j)`. In either case there exists a complement `ell` such that

\[
\boxed{
\operatorname{rad}(n_in_\ell)
=R_iR_\ell
\le
\frac{n_i}{TH_i}
\le
\frac{c}{TH_i}.
}
\]

This is the exact capacity-stratified refinement of the generic Stage-64 pair-radical compiler.

Stage 64 is recovered by erasing the coordinate `H_i` and using only `H_i>=1`.

Stage 70 is recovered when one complement is a squarefree side `s`, because then `C(s)=s'` supplies an explicit lower bound for `H_i`.

## 4. High-capacity branch

For any declared capacity floor

\[
H\ge1,
\]

an active orientation with

\[
H_i\ge H
\]

produces a pair product whose radical obeys

\[
\boxed{
\operatorname{rad}(n_in_\ell)
\le
\frac{c}{TH}.
}
\]

Therefore any external pair-product radical count usable in Stage 64 can be applied with the stronger threshold `TH` instead of `T`.

In the same de Bruijn regime imported by Stage 64, this gives the capacity-stratified scale

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T,\ H_{\rm active}\ge H)
\ll_\varepsilon
\frac{X^{1+\varepsilon}}{TH},
}
\]

where `H_active` means that at least one threshold-active cyclic orientation has `H_i>=H`.

The asymptotic count is prior-art dependent; P025-T140/C16 are the exact internal arithmetic compiler.

## 5. Low-capacity branch closes against Stage 51

The complementary case is not an unstructured remainder.

Suppose an active orientation satisfies

\[
H_i<H_0
\]

for a fixed integer cutoff `H_0>=2`. Then

\[
C_j,C_k\le H_0-1.
\]

Stage 51 applies independently to both complementary blocks.

For each complement `n`:

\[
\boxed{
C(n)\le H_0-1
\Longrightarrow
\begin{cases}
n=p^e,\ 1\le e\le H_0-1, &\text{prime-power branch};\\
n\mid Q_{H_0-1}, &\text{finite non-prime-power branch}.
\end{cases}}
\]

Thus a low-complement-capacity active orientation has **two simultaneously rigid complementary blocks**.

The only infinite low-capacity pieces are pairs of bounded-exponent prime powers. Everything else belongs to a finite core depending only on the declared horizon.

## 6. P025-C17 — cutoff five gives a finite exponent atom family

Stage 51 proves

\[
C(n)<5\Longrightarrow n=p^e,
\qquad e\in\{1,2,3,4\}.
\]

Therefore

\[
\boxed{
H_i<5
\Longrightarrow
n_j=p^e,\quad n_k=q^f,
\quad e,f\in\{1,2,3,4\}.
}
\]

The active component is then fixed by the additive relation once the two complements are chosen.

So the threshold-active universe admits the exact routing split

\[
\boxed{
\text{high complement capacity}
\quad\cup\quad
\text{bounded-exponent prime-power atoms / finite core}.
}
\]

At cutoff five the finite core disappears entirely.

## 7. Exact examples

### `3+125=128`, threshold `T=4`

The active term is c-oriented. The complement capacities are

\[
C(3)=1,\qquad C(125)=3,
\]

so

\[
H_c=3<5.
\]

The two complements are exactly the Stage-51 atoms

\[
3=3^1,\qquad125=5^3.
\]

Using the larger capacity `3` controls the pair `(128,3)`:

\[
\operatorname{rad}(128\cdot3)=6,
\]

and indeed

\[
4\cdot3\cdot6=72\le128.
\]

### `10+2187=2197`, threshold `T=6`

The active term is b-oriented. Its complement capacities are

\[
C(10)=7,\qquad C(2197)=3.
\]

Hence

\[
H_b=7.
\]

The larger capacity `C(10)=7` controls the pair `(2187,2197)`:

\[
\operatorname{rad}(2187\cdot2197)=39,
\]

and

\[
6\cdot7\cdot39=1638\le2187.
\]

This recovers Stage 70's derivative gain from the general dual-capacity formula.

## 8. Precision architecture consequence

Stage 71 creates an adaptive theorem-native routing state:

\[
\boxed{
\text{active cyclic index}
+
H_i
}
\]

with two very different downstream paths:

- large `H_i`: forget most factor data and send one strengthened pair-radical state to an external counting theorem;
- small `H_i`: do not count generically; refine instead into the finite-core / bounded-exponent prime-power structural atlas supplied by Stage 51.

This is an explicit example of **precision-dependent algorithm selection**: the same scalar capacity coordinate determines which representation is cheapest for the next task.

## 9. Prior-art / ownership boundary

Stage 51's low-capacity rigidity is existing P025 WIP. De Bruijn radical counting is external prior art. The algebra in P025-T140 is elementary.

The project-side result is the exact composition of these pieces into a high-capacity-count / low-capacity-rigidity dichotomy for the projective observable. Historical novelty remains `NOVELTY_UNVERIFIED`.

Generic query routing/minimal repair belongs to A2/P023 if promoted.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_projective_capacity_stratified.py`;
- `tests/test_abc_projective_capacity_stratified.py`.

The executable layer verifies exact active-orientation pair bounds and reuses Stage 51 for low-capacity classification.

## 11. Next frontier

No hard block exists. Continue with:

1. study the cutoff-five atom families `p^e +/- q^f` for `e,f<=4` and determine which can actually support `sigma_proj>=1` or higher thresholds;
2. allow a moving capacity floor only after checking the uniformity range of the imported de Bruijn bound;
3. combine the capacity split with Stage 68's adaptive precision budget;
4. relay the pattern `large coordinate -> coarse theorem-native count; small coordinate -> rigid structural refinement` to A2/P023.
