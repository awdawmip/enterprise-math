# R183 — Quadratic-dimensional affine action for every latest-source subset query

Date: 2026-11-15. Status: **AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED**.
Frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; R182 exact last-occurrence quotient and observer separation theorem:
[R182](https://github.com/awdawmip/enterprise-math/blob/83824bda8cb4ca4d9db71d660165f00fd92326ef/research_notes/portable_direct/R182_LAST_OCCURRENCE_SOURCE_QUERY_CONTEXT_QUOTIENT_20261115.md).

This is a typed source-selection observer over complete native X6 branch atoms. P000 physical space (six axes) and ordered heartbeat time remain as before; the extra rational coordinates below are metadata observer memory.

## R183A. A faithful affine representation of dimension k(k+1)/2

Fix `k >= 1` target source IDs indexed 0,...,k-1. Let `C_k` consist of all `k` singletons {i} and all `binom(k,2)` unordered pairs {i,j}. Its cardinality is
`d(k)=k + binom(k,2)=k(k+1)/2`.

The R182 state `s` is an ordered list of distinct targets by last-occurrence age; for a feature `U in C_k`, let `q_U(s)` be the last element of s belonging to U, or NONE. Define a scalar encoding `c_U(NONE)=0`, `c_U(i)=i+1`. An affine transformation associated to a singleton source atom i acts on coordinate `x_U` as

`T_i(x)_U = i+1 if i in U, else x_U`.

An atom from an unselected source has the identity action. Equivalently `T_i(x)=D_i x+b_i`, where diagonal `D_i[U,U]=0` for `i in U`, else 1, and `b_i[U]=(i+1)` for `i in U`, else 0.

For a complete history w use chronological composition `T_w=T_(first).then(...).then(T_last)`, as in native `Affine.then`.

**Theorem A.** For every history w and feature U, the coordinate action of `T_w` is exactly the identity if w contains no U target, or the constant map `x_U -> c_U(q_U(w))` otherwise. Consequently

1. `T_(uv)=T_u.then(T_v)` for all whole-atom histories u,v.
2. `T_u=T_v` if and only if their R182 states `lambda_T(u)` and `lambda_T(v)` coincide.
3. The R182 right-regular-band quotient embeds faithfully into rational affine transformations of dimension `k(k+1)/2`, with a **diagonal** linear part.
4. The embedding commutes exactly with positive rational BRC packet alternatives and serial composition when keys retain (exact weight, affine effect) and multiplicities are accumulated.

**Proof.** Every symbol i either leaves x_U untouched or overwrites it with the fixed value c_U(i). The last such overwrite, if any, therefore determines the output independently of the input. Composition is chronological and associative. Equal R182 states give the same last queried source for every U in C_k and hence exactly the same diagonal action. Conversely, different R182 states are distinguished by a singleton or pair query by R182B; evaluating the affine action at x=0 recovers c_U(q_U), so their actions differ. The histogram statement follows from the exact homomorphism and multiplication of positive rational weights and integer multiplicities, exactly as in R182C. QED.

The dimension is **quadratic in k** instead of the preceding universal simplex construction's `N_k-1 = floor(e*k!)-1`. For k=6 this reduces 1,956 affine coordinates to **21**; for k=8 it reduces 109,600 to **36**. Both represent the same fixed-source-selector observer quotient.

## R183B. Sharp dimension inside the independent reset-or-identity coordinate class

Define a **coordinatewise reset representation** to be an affine action on Q^d in which every generator i acts separately on each scalar coordinate h by either (a) leaving it unchanged, or (b) overwriting it with a generator-specific rational constant, independently of every other coordinate. Thus every coordinate has an associated trigger set `V_h subseteq T` of sources that overwrite it. No cross-coordinate mixing is allowed in this class. The representation must distinguish all R182 states by its affine actions, with arbitrary complete-history contexts.

**Theorem B.** Every faithful representation in this class has
`d >= k + binom(k,2)`.
The R183A diagonal reset construction attains equality.

**Proof: singleton necessity.** Fix i and let R list all k-1 other targets. The histories `iR` and `R` differ under the singleton query {i}. A coordinate triggered by any member of R is overwritten by the identical final R suffix in both histories, hence cannot distinguish them. A coordinate not triggered by i cannot distinguish them either. Therefore a distinguishing coordinate needs trigger set `V_h={i}`. Each i forces its own distinct coordinate.

**Proof: pair necessity.** Fix distinct i,j and let R list the remaining k-2 targets, identically in both histories. The histories `ijR` and `jiR` differ under the pair query {i,j}. Any coordinate with a trigger in R is overwritten in the same way by the common suffix. Among coordinates not triggered by R, those triggered by neither of i,j or by exactly one of them yield the same final output for both words. Distinguishing the opposite order therefore requires `V_h={i,j}` and differing reset outputs for i and j. Distinct unordered pairs force distinct coordinates. The required k singleton and binom(k,2) pair trigger sets are disjoint, so d has the stated lower bound. QED.

**Boundary of the result.** The lower bound is for the independent diagonal reset/identity class just defined. General rational affine maps may couple coordinates, and the exact minimum dimension across that larger class is a separate open problem. No optimality for all affine representations is asserted.

## Resource and native BRC interpretation

The diagonal matrix has d=k(k+1)/2 entries; for a single selected source i, exactly k coordinates are overwritten (the singleton {i} and k-1 pairs). A sparse typed adapter applies an atom in O(k) source-feature updates, composes two already aggregated diagonal actions in O(k^2) arithmetic operations, and stores each action in O(k^2) small rational coordinates before histogram aggregation. The action coefficients are integral 0/1 and reset codes 1..k, so no hidden rational approximation or exponential base-encoding is needed. The input source-to-target index and native branch/path information remain separate. This O(k^2) affine carrier is an optional implementation of the fixed observer; the raw R182 partial-permutation state is more compact for direct queries.

Exact source interface: `src/enterprise_math/brc_transport.py`: `Affine.then`, `EffectHistogram.from_terms`, `.alternatives`, `.then`. No direct installed-package test in this run: the executable checker is independent reference Python. For native ports whose future operators inspect branch identity, signed path, unselected sources or interaction data, retain the original carrier until independently certified.

## Reproduction and next problem

Checker: `R183_quadratic_reset_affine_check.py`; JSON: `R183_verification.json`.
Validation `R183_EXACT_QUADRATIC_RESET_PASS` performed k=1..5 full state-pair affine products (110,786), all distinct-state injectivity comparisons (55,186), 35 explicit required-coordinate trigger witnesses across those k, and 80 exact positive rational packet product/alternative comparisons. Universal results are proved symbolically above.

Control and author metadata are inherited from R182: unpublished historical `RS-S23-AV` with no asserted formal CLAIM; historical researcher `EM-DIRECT-BF4AD7`, SID `MCP-46f202db13e64ad6b4c8860e06908245`, Activity `RA-7A118452894D2600AE7DE5A2`. New activity checkpoint pending legitimate Source association.

Next: test actual native `enterprise_math.brc_transport` imports and `EffectHistogram` compositions with the R183 diagonal maps; determine the **unrestricted** minimal rational affine dimension or a smaller faithful mixed-coordinate construction, and benchmark conversion, coalescing and query cost against compact partial-permutation state and full R180 path preservation.
