# P022 — Microscopic-Average Event Repair Is Sublinear

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE MEAN / ANALYTIC ASYMPTOTIC / NOVELTY_UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: two-sided event-driven repair; excursion repair; `B_2/C_2` quotient-path interpretation  
Cross-route relevance: P018/P023/P024 state-dependent repair budgets and history precision

## 1. Question

A length-`N` two-sided microscopic Barlow window contains exactly `2N` sign bits.  The coordination-history quotient forgets labels only at two wall-release events:

- zero-coordinate departures, producing orientation repair `E`;
- diagonal splits, producing side-label repair `B`.

The exact path-lift theorem gives repair dimension

\[
r=E+B,
\]

with sharp worst case `r<=N+1`.

This note asks for the arithmetic mean of `r` over all `4^N` ordered microscopic two-sided windows.

## 2. P022-AM01 — one-sided orientation mean

For one signed walk, an orientation bit is born whenever the walk is at zero before a next microscopic step.  Put

\[
m=\left\lfloor\frac{N-1}{2}\right\rfloor.
\]

At even time `2j`, the fraction of prefixes at zero is

\[
p_j=\frac{\binom{2j}{j}}{4^j}.
\]

Hence the one-sided mean excursion count is

\[
\sum_{j=0}^{m}p_j.
\]

The classical central-binomial partial-sum identity gives

\[
\boxed{
E_N^{(1)}
=(2m+1)\frac{\binom{2m}{m}}{4^m}.
}
\]

The two labelled sides contribute twice this amount.

## 3. P022-AM02 — exact diagonal-split mean

At prefix time `t>=1`, a diagonal split can occur only when the two signed walks have equal nonzero absolute magnitude.

The normalized count of ordered prefix pairs with equal absolute magnitude is

\[
\frac{2\binom{2t}{t}}{4^t},
\]

and when `t` is even the simultaneous-zero pairs must be removed:

\[
\frac{2\binom{t}{t/2}^2}{4^t}.
\]

Exactly half of the four next-step pairs split the absolute magnitudes. Therefore the mean diagonal-split load through horizon `N` is

\[
\boxed{
D_N
=
\sum_{t=1}^{N-1}
\frac{\binom{2t}{t}
-\mathbf 1_{2\mid t}\binom{t}{t/2}^2}{4^t}.
}
\]

Write `M=N-1`.  The first sum has the exact closed form

\[
\sum_{t=1}^{M}\frac{\binom{2t}{t}}{4^t}
=
(2M+1)\frac{\binom{2M}{M}}{4^M}-1.
\]

Thus

\[
\boxed{
D_N
=
(2N-1)\frac{\binom{2N-2}{N-1}}{4^{N-1}}-1
-
\sum_{j=1}^{\lfloor(N-1)/2\rfloor}
\frac{\binom{2j}{j}^2}{16^j}.
}
\]

All finite quantities are rational numbers with integer numerator and denominator.

## 4. P022-AM03 — exact total microscopic mean

Let

\[
\overline r_N
=
\frac1{4^N}
\sum_{\text{ordered microscopic windows}}r.
\]

Then

\[
\boxed{
\overline r_N
=2E_N^{(1)}+D_N.
}
\]

This agrees with the derivative identity from the repair polynomial,

\[
2R_N'(2)=
\sum_{\text{microscopic windows}}r,
\]

but the present decomposition identifies the exact contribution of each wall type.

## 5. P022-AM04 — square-root leading law with logarithmic correction

Standard central-binomial asymptotics give

\[
\frac{\binom{2j}{j}}{4^j}
=
\frac1{\sqrt{\pi j}}+O(j^{-3/2}),
\]

and therefore

\[
E_N^{(1)}
=
\sqrt{\frac{2N}{\pi}}+O(N^{-1/2}).
\]

Likewise,

\[
(2N-1)\frac{\binom{2N-2}{N-1}}{4^{N-1}}
=
2\sqrt{\frac N\pi}+O(N^{-1/2}).
\]

For the simultaneous-zero correction,

\[
\frac{\binom{2j}{j}^2}{16^j}
=
\frac1{\pi j}+O(j^{-2}),
\]

so summation gives

\[
\sum_{j\le (N-1)/2}
\frac{\binom{2j}{j}^2}{16^j}
=
\frac{\log N}{\pi}+O(1).
\]

Combining the terms yields

\[
\boxed{
\overline r_N
=
2(1+\sqrt2)\sqrt{\frac N\pi}
-
\frac{\log N}{\pi}
+O(1).
}
\]

In particular,

\[
\boxed{\overline r_N=\Theta(\sqrt N).}
\]

## 6. P022-AM05 — average repair density vanishes

The literal two-sided microscopic state uses `2N` sign bits.  Therefore

\[
\frac{\overline r_N}{2N}
=
O(N^{-1/2})
\longrightarrow0.
\]

So under uniform microscopic counting, the exact event-driven repair retains a vanishing fraction of the literal sign history:

\[
\boxed{
\text{average exact repair density}\to0.
}
\]

This is stronger than the structural statement that repair is event-driven.  It quantifies the compression gain.

## 7. Worst, average and quotient-state views are different

Three scales now coexist:

- worst repair: `N+1`, linear;
- microscopic-weighted mean repair: `Theta(sqrt(N))`;
- quotient-state mean fiber size: polynomial in `N`, from the repair-polynomial image count.

None can replace the complete fiber distribution.  In particular, a linear worst case does not imply typical linear memory, while a square-root mean does not imply concentration around one deterministic square-root budget.

The orientation-variance theorem already shows one repair component has standard deviation `Theta(sqrt(N))`.

## 8. Geometry interpretation

Under the `B_2/C_2` orbit quotient, the two mean terms are local-time scales of two different reflection walls:

\[
\overline E_N
\sim
2\sqrt{\frac{2N}{\pi}},
\qquad
\overline B_N
=
2\sqrt{\frac N\pi}
-
\frac{\log N}{\pi}
+O(1).
\]

The negative logarithmic term is the overlap correction from simultaneous visits to the coordinate-wall intersection `(0,0)`, which must not be counted as a nonzero diagonal split.

Thus even the lower-order correction has a geometric origin in wall intersection.

## 9. Foundation/backflow consequence

This P022 specialization strengthens a candidate general principle without promoting it here:

> when a quotient erases labels only on singular/stabilizer loci, exact future repair may scale with boundary-event local time rather than elapsed horizon.

The proved scope remains the two-channel Barlow signed-permutation system.  Any A2/P018/P023 abstraction must identify hypotheses guaranteeing local path-lift multiplicity and must preserve counterexamples where lift branching depends on more than the current quotient transition.

## 10. Prior-art discipline

Simple symmetric random-walk return probabilities, central binomial coefficients, Stirling asymptotics, harmonic sums and Weyl/reflection-chamber local-time methods are established mathematics.

The project-specific content is the exact identification of those counts with the two typed Barlow repair mechanisms and the resulting finite-precision compression statement.  Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/p022_barlow_average_repair.py`;
- `tests/test_p022_barlow_average_repair.py`.

The tests compare the closed rational formulas with direct microscopic enumeration at short horizons and cross-check the diagonal term against its independent finite decomposition.
