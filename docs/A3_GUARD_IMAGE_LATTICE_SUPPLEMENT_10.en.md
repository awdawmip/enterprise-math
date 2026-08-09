# A3 Guard-Image Lattice Supplement 10 — Global All-State Band Precision and the Boundary of Adaptive Residue Shortcuts

Status: `RESEARCH WIP / EXACT GLOBAL-BAND MINIMUM PARTITION THEOREM`

## 1. Why a finite workload is still not a global program

Supplement 08 established that state-local and finite-workload minimum precision can differ. A finite workload, however, is still only a finite set of states.

Here we study the finite-band predicate

\[
P_R(c):=[|w^Tc+b|\le R]
\]

over the full fine domain

\[
\boxed{c\in\mathbb Z^k.}
\]

The question is whether a partition can keep the scalar hidden and still answer this Boolean query exactly for **every** fine and coarse state.

## 2. Global scalar image

The integer linear map `c -> w^T c` has image

\[
\boxed{g\mathbb Z,}
\]

where

\[
\boxed{g=\gcd(|w_1|,\ldots,|w_k|).}
\]

If all coefficients vanish, `g=0` and the scalar is the constant `b`.

If `g>0`, the full-domain scalar values are

\[
\boxed{b+g\mathbb Z.}
\]

The domain contains a band-true state iff

\[
\boxed{\rho_g(b)\le R.}
\]

Because the progression is unbounded, false states also always exist when `g>0`.

## 3. A3-G37 — Global band constancy criterion

If `g=0`, the predicate is globally constant with value `[|b|<=R]` and every partition is exact.

If `g>0` but

\[
\rho_g(b)>R,
\]

the entire global scalar image misses the band, so

\[
\boxed{P_R\equiv\mathrm{False}}
\]

and again every partition is exact.

If `g>0` and

\[
\rho_g(b)\le R,
\]

then the full domain contains both true and false states, so the band task is globally nonconstant.

## 4. A3-G38 — A nonconstant global band requires scalar descent

Assume `P_R` is globally nonconstant and consider a partition `A`.

If the scalar still has nonzero hidden step `q>0`, choose a supported fine state `c_0`, which exists by global nonconstancy. The same coarse fiber `c_0+K_A` has scalar values

\[
z_0+q\mathbb Z.
\]

This progression is unbounded, so the same coarse fiber also contains an unsupported fine lift. One coarse state therefore has both Boolean outcomes, contradicting global exactness.

Hence global exactness requires

\[
\boxed{w(K_A)=0,}
\]

i.e. the scalar observable itself must descend.

Conversely, if the scalar descends, the band truth is directly computable from the coarse scalar.

Therefore, for a globally nonconstant finite band,

\[
\boxed{
\text{partition globally exact}
\iff
\text{scalar observable descends}.
}
\]

## 5. A3-G39 — Global minimum partition

Given an initial partition `P_0`:

- if the band predicate is globally constant, no refinement is needed and `P_*=P_0`;
- if it is globally nonconstant, G38 says global exactness is identical to exact scalar observation.

For coordinate partitions, scalar descent means the coefficient `w_i` is constant inside every block. Thus the unique coarsest exact refinement is the standard observation-aware split by coefficient value:

\[
\boxed{P_*=\operatorname{ObsRefine}(P_0,w).}
\]

This is a complete minimum-partition solver for a global finite-band query over `Z^k`.

## 6. Why the adaptive residue shortcut disappears globally

At one state, a hidden fiber can be exact false because its residue class misses the band. A finite workload may sample only such favorable residue classes.

A globally nonconstant task necessarily contains at least one supported fine state. Any nonzero hidden step through that supported state produces unsupported lifts in the same coarse fiber.

Therefore

\[
\boxed{
\text{residue shortcuts are adaptive/state-restricted optimizations,
not substitutes for all-state scalar visibility.}
}
\]

## 7. Three exact precision levels

For finite-band tasks the project now distinguishes:

- **state-local precision**: one coarse fiber must be exact;
- **finite-workload precision**: one common refinement must serve finitely many fibers;
- **global all-state precision**: one partition must serve the whole integer domain.

For a fixed workload state and its common workload,

\[
\boxed{
\Delta d_{local}
\le
\Delta d_{workload}
\le
\Delta d_{global},
}
\]

with either inequality potentially strict or equal depending on the task/domain.

## 8. Example

Take

\[
w=(0,2,4),\qquad R=1,\qquad b=0.
\]

The global scalar image is `2Z`, containing `0` and also unbounded values, so the band predicate is globally nonconstant.

The single-block partition hides the scalar and is not globally exact. The intermediate partition `{{0,2},{1}}` has hidden step `4`; some individual fibers can be exact false by residue miss, but fibers with residue zero still intersect the band, so the partition is not globally exact.

The singleton partition makes the scalar visible and is globally exact.

Thus a partition may be exact for selected states while failing the same task on the whole domain.

## 9. Globally constant-false exception

Take

\[
w=(4,8),\qquad b=1,\qquad R=0.
\]

The global image `1+4Z` never contains zero, so the predicate is globally false. Any partition is exact even if the scalar is completely hidden.

The visibility necessity in G38 therefore explicitly requires a **globally nonconstant** task.

## 10. Implementation

Extended:

- `src/enterprise_math/hidden_band_predicate.py`;
- `tests/test_hidden_band_predicate.py`.

New APIs:

- `scalar_global_image_step`;
- `global_band_profile`;
- `band_partition_globally_exact`;
- `minimum_global_band_partition`;
- `GlobalBandProfile`.

Tests cover the global gcd image, constant-false no-refinement case, visibility necessity for a nonconstant band, the unique coarsest coefficient refinement, and truth-variability checks on small integer boxes.

## 11. Meaning for P018/A2

This theorem gives adaptive precision a hard boundary:

> **task-local precision savings and one-model-fits-all global exactness are different optimization problems.**

P018 can exploit hidden subgroup residues for adaptive per-state/per-region precision. A fixed partition that must be exact on the full infinite domain cannot use that shortcut for a nonconstant scalar band; it must expose the scalar observable exactly.

General behavioral quotient theory remains owned by A2/P023; this is an A3 scalar-band specialization.

## 12. Next

1. relay the finite-workload/global-band gap to P018/P023;
2. derive symbolic all-state programs for general rank-one multi-guard effects rather than only bands;
3. study the coarse-readable quotient score state `Z^r/L_G` as a typed global predicate state;
4. relay the support corollary to the A3-to-A4 bridge;
5. separate adaptive local precision from shared/global precision in actual A4/P021 future languages.
