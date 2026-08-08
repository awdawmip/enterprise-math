# P019 Supplement 12 — When transport counts become sufficient again

Status: `TESTING / FINITE SUFFICIENT CONDITION PROVED`

Supplement 11 showed that cardinality transport matrices are not composition-complete in general because they forget which exact middle incidence supports a continuation. This supplement identifies a clean restricted regime in which the lost witness identity no longer affects the three-step count.

Let a middle direction class contain incidences

\[
e_1,\ldots,e_m.
\]

For each middle incidence define its predecessor and successor witness multiplicities

\[
l_i=\#\{e^-:e^-\text{ composes into }e_i\},
\qquad
r_i=\#\{e^+:e_i\text{ composes into }e^+\}.
\]

Then the two adjacent transport counts are

\[
L=\sum_i l_i,
\qquad
R=\sum_i r_i,
\]

while the exact three-edge chain count is

\[
\boxed{N=\sum_i l_i r_i.}
\]

In general \(L\) and \(R\) do not determine \(N\).

However, if either witness profile is uniform — all \(l_i\) equal, or all \(r_i\) equal — then

\[
\boxed{mN=LR.}
\]

This is proved without division. For example, if \(l_i=a\) for every \(i\), then \(L=ma\) and \(N=aR\), hence \(mN=LR\). The successor-uniform case is symmetric.

Therefore P019 now has a precise reduction rule:

> **Witness transport is the general primitive. Cardinality transport is sufficient on a middle direction class whenever one side of its witness fibers is uniform.**

The condition is sufficient, not claimed necessary. When both profiles are nonuniform, the implementation refuses to infer exact composition from counts alone.

This result also clarifies what “homogeneity” must mean if P019 later seeks a continuum-like coarse limit: not merely equal total transport counts, but sufficiently uniform witness fibers across the exact middle incidences being aggregated.

No probabilistic independence, averaging limit, or physical isotropy is assumed.
