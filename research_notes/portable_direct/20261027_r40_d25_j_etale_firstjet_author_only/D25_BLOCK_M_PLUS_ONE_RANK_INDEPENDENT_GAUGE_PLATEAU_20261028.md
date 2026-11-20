# D25/LIFT — universal repeated-block `(m+1)` signed-jet gauge plateau

**Date and classification:** 2026-10-28; `AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE` until independent and Source review. This is an auxiliary finite-field theorem, **not** an original-class H0/B0 computation or a solution of `Δ_p−R_p`. Mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. Existing Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; immutable science Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` preserved. Author context: the continuing portable author lineage already disclosed in PR #1566; no independent reviewer or native researcher/session/claim is inferred.

## Narrow uncompleted problem and reuse

Earlier author evidence (same PR) established the auxiliary second-jet identity `K=[B,A]`, the trace-annihilator feasibility test and the full-gauge classification for rank three with a repeated `(2+1)` eigenblock (`q+3` orbits). Original native H0/B0 rank, actual `A`, gauge subgroup `H`, signed port and `Δ_p−R_p` map are still absent (Issue #1559). The remaining portable question here is **whether the `(2+1)` result is exceptional or extends to arbitrarily large repeated eigenblocks**, and exactly how source/observer counts grow with rank. This does not redo the rank-three derivation as new evidence.

Let `k=F_q` be any finite field (the D25 application requires odd `q`), `m≥1`, `a,b∈k`, `a≠b`. On `V=k^m ⊕ k`, put

\[
 A=\begin{pmatrix}a I_m&0\\0&b\end{pmatrix},\qquad K=[B,A]=BA-AB.
\]

The **marked source carrier** is the full matrix `B∈M_{m+1}(k)` with basis/eigenspace normalization and each off-block component retained. The derived signed jet is

\[
 K(X,Y)=\begin{pmatrix}0&X\\Y&0\end{pmatrix},\qquad X\in k^m,\quad Y\in (k^m)^*,
\]

where `X=(b−a)B_{12}` and `Y=(a−b)B_{21}`. The residual **full centralizer** `G=GL_m(k)×k^*` acts by `(P,t)·(X,Y)=(PX/t,tYP^{-1})`. This is a declared **auxiliary operation**, not the asserted native allowed gauge subgroup.

## Theorem A — a rank-independent gauge-orbit plateau

For every `m≥2` and finite field `k=F_q`, the entire set of `q^{2m}` derived jets has **exactly `q+3`** orbits under the above full centralizer. The complete, source-aware orbit observer is

\[
 \boxed{\mathcal I(K)=\bigl(\mathbf1_{X\ne0},\mathbf1_{Y\ne0},s=YX\bigr).}
\]

The distinct orbit strata and their **exact cardinalities** are:

| Typed signed/source stratum | Number of orbits | Size of each orbit |
| --- | ---: | ---: |
| `X=0,Y=0` | 1 | `1` |
| `X≠0,Y=0` | 1 | `q^m−1` |
| `X=0,Y≠0` | 1 | `q^m−1` |
| `X≠0,Y≠0,s=0` | 1, only if `m≥2` | `(q^m−1)(q^{m−1}−1)` |
| `X≠0,Y≠0,s=c` for each `c∈k*` | `q−1` | `(q^m−1)q^{m−1}` |

Consequently `s=tr(K²)/2` for odd characteristic is **complete only on each fixed `s≠0` fiber**; the `s=0` fiber contains exactly **four distinct full-gauge orbits for all `m≥2`**. The extra Boolean source-presence flags repair the scalar observer loss without choosing a rank-specific coordinate basis.

**Sharp boundary `m=1`.** The `X,Y≠0,s=0` stratum is empty; the orbit number is `q+2`, recovering the earlier split rank-two calculation. The general `q+3` plateau begins precisely at repeated-eigenspace dimension two.

**Proof.** The effective image of `G` on `(X,Y)` is all `GL_m(k)` by taking `t=1`; its action is `(X,Y)↦(PX,YP^{-1})`. It preserves both zero flags and the scalar `s=YX`. Conversely, `GL_m(k)` is transitive on nonzero vectors and nonzero covectors separately, establishing the two one-sided nonzero orbits. If `X,Y` are both nonzero and `s≠0`, choose the first basis vector `v_1=X` and the remaining `m−1` basis vectors in `ker(Y)`. Then `Y=(s,0,…,0)` in that basis, proving a single orbit for each nonzero `s`. For `s=0`, `X∈ker(Y)` and, when `m≥2`, choose `v_1=X`, a vector `v_2` with `Y(v_2)=1` and then a complement of `v_1` inside `ker(Y)`; this gives a single orbit with `X=e_1`, `Y=e_2^*`. No such pair exists for `m=1`. This proves completeness of `I`.

For each nonzero `X` (`q^m−1` choices), the equation `YX=c` defines an affine hyperplane of `q^{m−1}` covectors when `c≠0`; the zero hyperplane has `q^{m−1}−1` **nonzero** covectors when `c=0`. Summation yields the table and

\[
 1+2(q^m-1)+(q^m-1)(q^{m-1}-1)
 +(q-1)(q^m-1)q^{m-1}=q^{2m}.
\]

This is a finite-field proof independent of the regression cases. □

## Theorem B — source multiplicity and restricted scalar gauge

The linear map `B↦[B,A]` has kernel `M_m(k)⊕k` of dimension `m²+1`, since `b−a` is invertible. **Every individual signed `K` jet has exactly `q^{m²+1}` distinct marked source matrices `B`**, and the source population `q^{(m+1)²}` is partitioned into `q^{2m}` equal fibers. The classifying `I(K)` does **not** reconstruct the original `B`; a future observer of its within-eigenblock components is not implied to descend.

If the allowed gauge group is instead the scalar-on-block subgroup `diag(λ I_m,t)` with effective ratio subgroup `R={λ/t}` of order `h | (q−1)`, then `(X,Y)↦(rX,r^{-1}Y)` is free on every nonzero pair, and

\[
 \boxed{N_{\mathrm{scalar}}(m,q,h)=1+\frac{q^{2m}-1}{h}.}
\]

The **full centralizer result `q+3` cannot be substituted** for this proper-subgroup result without proving the actual permitted operations. This is an explicit source/observer BRC composition: preserve `(B,X,Y,A,H)` first; only quotient when the future operations are `H`-equivariant and all claimed observer maps are invariant.

## Precise `p=373` conditional consequences (not an experiment)

For `q=373` and an auxiliary `A=diag(a I_m,b)`, the full centralizer has **376** orbits for **every** `m≥2`, even though the jet population and per-jet source multiplicity grow rapidly:

| Repeated-block dimension | `#K=q^(2m)` | `#B` per fixed `K=q^(m²+1)` | full-gauge orbits | maximal scalar-ratio gauge orbits (`h=372`) |
| --- | ---: | ---: | ---: | ---: |
| `m=2` | `19,356,878,641` | `7,220,115,733,093` | `376` | `52,034,621` |
| `m=3` | `2,693,103,168,443,689` | `52,130,071,199,257,068,815,346,649` | `376` | `7,239,524,646,355` |
| `m=4` | `374,688,750,722,402,006,881` | `52,366,089,149,382,037,791,632,551,418,044,746,512,864,053` | `376` | `1,007,227,824,522,586,041` |

Numbers are exact integer substitutions into the proved auxiliary formulas; **no** `p=373` native H0/B0 operator, rank, gauge or `Δ_p−R_p` computation is asserted. If the actual `A` has several eigenblocks or a nonsemisimple part, this special theorem is not the right interface; the earlier general Burnside/double-commutator formula remains available for authenticated `A,H`.

## Reproducible author-side check

Executable Python standard-library checker: `d25_block_m1_gauge_plateau_checker_20261028.py`. It constructs actual finite-group orbit partitions on each `F_p^{2m}` using elementary transvections generating `SL_m(F_p)` and a primitive diagonal generating `GL_m(F_p)`. It checks exact equality of each orbit with the proposed typed invariant fiber, all orbit sizes, and the `m=1` boundary; in addition it checks the source-to-commutator and `tr(K²)=2YX` identities for 480 deterministic marked matrices including `p=373` (not native).

Recorded execution: `d25_block_m1_gauge_plateau_author_check_20261028.json`. **12 exhaustive `(m,p)` cases**, `158,516` states, `1,076,762` explicit generator transitions and `480` source-matrix identity checks, all `PASS`. Cases include `(m,p)=(3,7),(4,3)`; the theorem covers **all finite fields** by proof, while exhaustive tests cover only the stated prime fields. This is **author-context verification, not independent review, Lean formalization or native experiment**.

## Unfinished target and exact responsible path

Existing [H0/B0 original fixed-class capability/benchmark intake #1559](https://github.com/awdawmip/enterprise-math/issues/1559) remains `PENDING_OWNER`. The next genuinely discriminating step belongs to its lawful native evaluator: provide actual coefficient ring, basis, Frobenius matrix rank and first even jet `A`, actual permitted residual group `H`, signed odd ports and `κ,Δ_p−R_p` with original source. If `A` has exactly an `(m+1)` split block as above, use the rank-independent classification here and **test** whether its flag/pairing quotient preserves the specified native observers and future operations; otherwise use the general Burnside formula and retain marked ports. `m≥2` must be established, not guessed from the number of written coordinates. No transfer to P000 X6/t or native three-dimensional slice follows from this auxiliary finite-field model. P000 ACTIVE premises, their six native axes and independent time, and the immutable science source pin are unchanged.

The earlier UR V2 four-file **mathematics is already written** in its own portable context. Original-byte provenance remains `UNVERIFIED_BYTES`: target `94687` bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. This note neither reconstructs nor re-proves the UR bundle. Source native research session/CLAIM/OPEN/checkpoint, formal Result, independent review and admission are not inferred from GitHub Draft storage.
