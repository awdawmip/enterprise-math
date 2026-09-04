# Post-#1161 free research — one-shell universality and adaptive return-depth resource law

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / QUADRATIC UNIVERSALITY + CERTIFIED STATE-COST SCHEDULE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessor: `research_notes/FREE_RESEARCH_POST1161_S4_GRADED_FINITE_RETURN_RG_20260904.md`

## 0. Result

The finite first-return depth needed to reproduce the **quadratic universality class** of the AGM shape RG is minimal: one first-return shell already suffices.

For every finite return depth `N>=1`, the explicit rational shape map

\[
T_N(s)=\frac{F_N(s)}{2-F_N(s)},
\qquad
F_N(s)=\sum_{k=1}^N f_ks^{2k},
\]

has the same quadratic fixed-point coefficient as the exact AGM map:

\[
\boxed{
\lim_{s\to0}\frac{T_N(s)}{s^2}=\frac14.
}
\]

On the standard shape range `0<s<=1/4`, uniformly in every `N>=1`,

\[
\boxed{
\frac{s^2}{4}
\le T_N(s)
<\frac{256}{961}s^2
<\frac4{15}s^2.
}
\]

Thus all nonzero finite return-depth models are genuinely quadratically contracting.

The minimal nontrivial depth `N=1` is explicit:

\[
\boxed{T_1(s)=\frac{s^2}{4-s^2}.}
\]

Across the twelve `S4` diamond positions, this uses only

\[
\boxed{|X_1|=36}
\]

scalar predictive states.

Deeper return shells improve the finite approximation to the exact AGM update but are not needed to create quadratic convergence.

## 1. Uniform finite-depth quadratic bound

The first return coefficient is

\[
f_1=\frac12.
\]

Therefore for every `N>=1`,

\[
F_N(s)\ge\frac{s^2}{2}.
\]

Since `F_N<=F`, where the completed first-return mass satisfies `F=1-r` and `r^2+s^2=1`, the standard range `s<=1/4` gives

\[
r>\frac{15}{16},
\qquad
F<\frac1{16}.
\]

Hence `F_N<1/16` and

\[
2-F_N>\frac{31}{16}.
\]

For the lower bound,

\[
T_N=\frac{F_N}{2-F_N}\ge\frac{F_N}{2}\ge\frac{s^2}{4}.
\]

For the upper bound, monotonicity in `F` gives `T_N<=T`, and the exact AGM shape map is

\[
T(s)=\frac{1-r}{1+r}=\frac{s^2}{(1+r)^2}.
\]

Thus

\[
T_N(s)
<\frac{s^2}{(31/16)^2}
=\boxed{\frac{256}{961}s^2}
<\frac4{15}s^2.
\]

The first coefficient alone forces the lower quadratic coefficient `1/4`; every deeper first-return shell only contributes order `s^4` and above.

## 2. Minimal shell

At depth one,

\[
F_1(s)=\frac{s^2}{2},
\]

so

\[
\boxed{
T_1(s)
=\frac{s^2/2}{2-s^2/2}
=\frac{s^2}{4-s^2}.
}
\]

Depth zero would have `F_0=0` and hence the degenerate map `T_0=0`; it does not preserve the nonzero quadratic coefficient.

Therefore

\[
\boxed{N=1\text{ is the unique minimal return depth capturing the AGM quadratic universality class}.}
\]

The corresponding graded predictive horizon is

\[
h=2N-1=1,
\]

so the scalar counter quotient has three states

\[
Q_1=\{0,1,\infty_1\}.
\]

Tensoring with the twelve `S4` diamond positions yields

\[
\boxed{|D_{12}\times Q_1|=36.}
\]

This `36` is a state count for the declared scalar predictive observer, not a claim of globally minimal native ontology.

## 3. Exact finite-depth error against the completed AGM shape map

Let

\[
e_N=F-F_N.
\]

The first-return tail theorem gives

\[
0\le e_N\le s^{2N+2}.
\]

Because

\[
T(F)=\frac{F}{2-F},
\]

one has the exact difference identity

\[
\boxed{
T-T_N
=\frac{2(F-F_N)}{(2-F)(2-F_N)}.
}
\]

On `s<=1/4`, both denominators exceed `31/16`; therefore

\[
\boxed{
0\le T(s)-T_N(s)
<\frac{512}{961}s^{2N+2}.
}
\]

For `N=1`, the finite rational map differs from the exact AGM shape map only at order `s^4`:

\[
\boxed{T-T_1=O(s^4).}
\]

So one-shell truncation preserves not merely quadratic convergence, but also the exact leading quadratic coefficient `1/4`.

## 4. Mean/channel error

The exact completed return update and finite-depth update satisfy

\[
H^+=H\left(1-\frac F2\right),
\qquad
H_N^+=H\left(1-\frac{F_N}2\right),
\]

\[
U^+=H\frac F2,
\qquad
U_N^+=H\frac{F_N}2,
\]

and

\[
b^+=\frac H2(1-F),
\qquad
b_N^+=\frac H2(1-F_N).
\]

Therefore the same scalar tail controls every finite mean-channel error:

\[
\boxed{
H_N^+-H^+
=U^+-U_N^+
=b_N^+-b^+
=\frac H2e_N.
}
\]

On the standard orbit `H<2`,

\[
\boxed{
0<H_N^+-H^+<s^{2N+2},
}
\]

and likewise for the other displayed differences.

Thus `s^(2N+2)` is an exact common resource/error currency for one finite return-depth AGM step.

## 5. Dyadic shape bound along the exact AGM orbit

The #1161 shape analysis already gives the explicit contraction

\[
s_n<\frac{15}{4}\,15^{-2^n}.
\]

Using only

\[
\frac{15}{4}<4,
\qquad
15>8,
\]

we obtain the simpler dyadic bound

\[
\boxed{
s_n<2^{\,2-3\cdot2^n}.}
\]

Therefore at outer AGM step `n`, return depth `N` gives the one-step mean/channel error certificate

\[
s_n^{2N+2}
<
\boxed{
2^{-(3\cdot2^n-2)(2N+2)}.
}
\]

No logarithm needs to be materialized in the finite state; the exponent is an exact integer readout.

## 6. Minimal sufficient return depth for p certified bits

To make the one-step inner return-depth error strictly below `2^{-p}`, it suffices that

\[
(3\cdot2^n-2)(2N+2)\ge p.
\]

The least depth allowed by the nontrivial-shell constraint `N>=1` under this dyadic bound is

\[
\boxed{
N_n(p)
=
\max\left(
1,
\left\lceil\frac{p}{2(3\cdot2^n-2)}\right\rceil-1
\right).
}
\]

The scalar `S4` predictive-state cost is

\[
\boxed{
C_n(p)
=12(2N_n(p)+1)
=24N_n(p)+12.
}
\]

Thus the required return depth decays asymptotically like

\[
N_n(p)\sim \frac{p}{6\,2^n},
\]

until it reaches the universal minimum `N=1`.

So the inner first-return resource requirement roughly halves every outer AGM step.

## 7. Example: 256-bit one-step inner certificate

For `p=256`, the exact sufficient schedule from the dyadic theorem is:

| outer step `n` | return depth `N_n` | scalar S4 states `24N+12` | certified exponent |
|---:|---:|---:|---:|
| 0 | 127 | 3060 | 256 |
| 1 | 31 | 756 | 256 |
| 2 | 12 | 300 | 260 |
| 3 | 5 | 132 | 264 |
| 4 | 2 | 60 | 276 |
| 5 | 1 | 36 | 376 |
| 6 | 1 | 36 | 760 |
| 7 | 1 | 36 | 1528 |
| 8 | 1 | 36 | 3064 |

By outer step five, the minimal 36-state inner RG already exceeds the 256-bit one-step target by a wide margin.

The large first-step depth is a consequence of the deliberately coarse universal dyadic bound `s_0<1/2`; using the exact current finite/algebraic shape enclosure can only reduce the required depth. The table is therefore a robust sufficient schedule, not an optimal numerical implementation claim.

## 8. Executable verification

Task-local checker:

`scripts/check_free_research_agm_adaptive_return_depth.py`

Initial commit:

`4db74fbd3dd77727ce3b0a447ba29fe78c8a3eb5`.

The checker uses only integer/rational arithmetic and verifies:

- `496` positive rational shape values in `0<s<=1/4`;
- depths `N=1..8` for every shape;
- `11904` exact rational inequalities covering the quadratic bounds and shape-error bracket;
- the closed one-shell formula `T_1=s^2/(4-s^2)`;
- adaptive schedules for targets `64,128,256,512,1024` bits;
- minimality of each chosen `N>1` relative to the stated dyadic exponent bound;
- the exact 256-bit schedule above.

The file was fetched from `main` and its full logic was replayed successfully.

## 9. Scope boundary

This theorem concerns **one-step inner return-depth error** and the shape-RG universality class. It does not by itself assert that independently replacing every exact AGM step by a finite-depth point estimate yields a final `p`-bit enclosure of the exact AGM completion constant: accumulated trajectory error must be propagated, preferably by outward intervals rather than by treating finite point approximants as exact states.

That is the next precision problem.

The theorem also does not promote the 36-state predictive machine to bare P000/G0 ontology. The finite states remain observer-relative N1/N2 predictive quotients carried equivariantly over the derived `S4` diamond geometry.
