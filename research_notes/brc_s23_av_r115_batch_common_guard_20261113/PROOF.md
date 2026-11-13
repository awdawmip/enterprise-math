# R115 — Finite-stratum locality and exact threshold queries for batched common-source edits

Date: 2026-11-13 (Asia/Shanghai). Status: author-side mathematics with exact finite validation; no independent semantic review. Preserved frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Immediate predecessor R114 at `dfc43cbd5f3adedab377653bd14d2b5615842067:research_notes/brc_s23_av_r114_minimum_locus_guards_20261113/PROOF.md`. This is the **auxiliary** finite ranked-source/S23 directed-circle model, not a statement of native six-dimensional Heartbeat dynamics.

## 1. Definitions and edit class

Let `(U, ≻)` be a totally ordered set of distinct full source identities. Fix a parameter domain `I`, eligibility predicate `M_u(θ)` for each source (independent of the source version), and two finite versions `F,G⊆U`. For `θ∈I`, define `Δ=F△G` and the highest eligible difference `d(θ)=max_≻{v∈Δ:M_v(θ)}`, if any. The exact first-difference rank capacity is

```
h(θ) = #{v∈F∩G:v≻d(θ), M_v(θ)}    when d(θ) exists,
h(θ) = ∞                            otherwise.
K = min_{θ∈I} h(θ).
```

As proved in R112, for every `k≥1`, the Top-k sequences of `F,G` agree throughout `I` if and only if `k≤K`. A point of finite minimal capacity witnesses their first discrepancy at position `K+1`.

Let `A` be a set of `r=|A|` **fresh** full source identities, disjoint from `F∪G`. Let `D⊆F∩G` consist of `s=|D|` common sources to be removed from *both* versions, with `A∩D=∅`. Set

```
F'=(F∪A)\D,        G'=(G∪A)\D.
```

Then `F'△G'=Δ`; all edits preserve the full identity and rank order. On a parameter where `d(θ)` exists, define:

```
g_A(θ) = #{u∈A : u≻d(θ), M_u(θ)};
g_D(θ) = #{u∈D : u≻d(θ), M_u(θ)}.
```

Both guards vanish in the no-eligible-difference case.

## 2. R115.1 — Exact batch edit identity and sharp finite horizon

**Theorem.** At every `θ` with `h(θ)<∞`,

```
h'(θ) = h(θ)+g_A(θ)-g_D(θ),       0≤g_A≤r,  0≤g_D≤s.
```

At a point with `h(θ)=∞`, the edited capacity remains `∞`. Consequently, if `K<∞`, the whole-domain capacity satisfies

```
max(0,K-s) ≤ K' ≤ K+r.
```

If `K=∞`, then `K'=∞`. In particular, a single symmetric common edit (`r+s=1`) specializes to R114.

**Proof.** Since `Δ` is unchanged, the highest eligible differing full identity `d(θ)` is unchanged. A common source contributes to `h` exactly if it is eligible and strictly outranks `d(θ)`. The two symmetric edits add exactly `g_A` such sources and remove exactly `g_D`. Neither eligibility nor the relative rank of any other identity changes, proving the pointwise identity. The no-difference case retains identical full eligible lists.

Taking minima in the pointwise bounds `h-s≤h'≤h+r` gives `K-s≤K'≤K+r`: for the upper bound, take an old minimizer, and for the lower bound apply the pointwise inequality at every parameter. Counts cannot be negative. If no difference is eligible at any parameter, `h≡∞` is unchanged. ∎

The upper change `K→K+r` is attained in auxiliary S23 on `I=[0,1]`, `(j,x,a,c)=(0,1/4,0,1)`, with `F={(2,0)},G=∅, A={(2,1),(2,2)},D=∅`: each added higher-ranked same-time source is coeligible with `(2,0)`; thus `K:0→2`. Reversing the batch attains `K:2→0` for `s=2` (as a removal from the common set of the reversed pair). No claim is made that *all* r,s combinations are simultaneously attained in the fixed bounded test universe.

## 3. R115.2 — Finite low-stratum locality for exact global minimum

**Theorem.** Assume finite `K` is attained. Any parameter `θ` with old `h(θ)>K+r+s` cannot minimize the new capacity `h'`. In particular, all new minimizers belong to

```
L_{r,s} = {θ∈I : h(θ)≤K+r+s}.
```

It suffices to compute `h'` exactly on this old low-stratum set to obtain the global `K'` and an exact minimizing witness.

**Proof.** Take any old minimizer `θ_0`: the batch identity gives `h'(θ_0)≤K+r`, hence `K'≤K+r`. At a parameter with old `h>K+r+s`, `h'≥h-s>K+r≥K'`. Thus it cannot be a new minimizer. Parameters with `h=∞` stay infinite and cannot minimize finite `K'`. The minimum is therefore achieved inside the stated low-stratum set. ∎

**Remark (stronger threshold-specific pruning).** For a target integer `τ≥0`, an old finite-capacity point with `h(θ)≥τ+s` automatically has `h'(θ)≥τ`. Thus the exact question `K'≥τ` only requires checking the old locus

```
T_τ={θ∈I : h(θ)<τ+s}.
```

The predicate is true precisely when all points of `T_τ` have `h'(θ)≥τ`; `T_τ=∅` certifies it immediately. This holds for arbitrary old finite K, including cases where the new capacity stays infinite.

The cutoff for the *global minimum* is deliberately inclusive, and is conservative: it can be tightened further when existing candidate witnesses give a smaller known upper bound. If an application merely asks whether two versions have equal Top-k, take `τ=k` to obtain a specialized certificate with no need to compute the exact `K'` value.

## 4. R115.3 — Exact rational S23 local refinement and witness

In the auxiliary S23 model, source identities are `(t,b)` and are ordered by descending `(t,b)`. Set rational `x,L,U` and integer `j,a,c`. Membership of `(t,b)` is the half-open directed fractional-circle arc test

```
M_t(θ)  iff  {x+(t-j)θ} ∈ directed arc [{aθ},{cθ}),
```

with equal arc endpoints representing the empty arc. For any finite old relevant source family, its eligibility predicates and hence `h` admit an exact atom partition: singleton affine integer crossings and the open gaps between them, with one rational midpoint representing each gap (R111–R112).

Let each old atom `J` store constant `h(J)`. For an exact post-batch global-minimum/witness query, ignore atoms with `h(J)>K+r+s`. For each remaining *open* atom insert only the changed times' integer crossings of the six affine phase families

```
aθ, cθ, (a-c)θ,
x+(t-j)θ, x+(t-j-a)θ, x+(t-j-c)θ,       t∈times(A∪D).
```

Evaluate `g_A,g_D` at each resulting cut singleton and rational midpoint, and evaluate the old selected singleton atoms directly. Take the minimum of `h(J)+g_A-g_D` over these local representatives.

**Theorem.** This procedure returns exactly `K'` and an exact rational witness when finite. For the threshold question `K'≥τ`, the same local refinement of only `h(J)<τ+s` atoms is necessary and sufficient.

**Proof.** On each original atom the old highest eligible difference, common prefix and old capacity are constant. Each changed source predicate has all its changes among the six affine crossing families, so between added cuts every `g_A,g_D` is constant; each cut is separately evaluated to respect half-open endpoint semantics. The batch identity computes `h'` exactly on each local subatom. R115.2 excludes every skipped atom from attaining `K'`. The threshold-specific pointwise lower bound excludes every skipped atom from falsifying `K'≥τ`. Rational endpoints and midpoints supply exact witnesses in the finite case. ∎

**Complexity scope.** The theorem reduces the *new-cut materialization region* and certificate evaluations for these query classes; obtaining old low strata, counting them, crossing generation, sorting, exact big-integer arithmetic, building fully updated persistent history DAGs, and outputting a witness still incur costs. A complete runtime advantage requires end-to-end benchmarks and bit-cost accounting. Neither the finite ranked-source representation nor these auxiliary half-open circle predicates constitute a native six-dimensional Heartbeat realization.

## 5. Exact executable verification

The supporting program `check_r115.py.gz.b64` is a gzip/base64-compressed UTF-8 Python 3 checker, decoded SHA256 `e37b57c5552ae538383cc4713e632fdf80f974ec76ceea92340479eb4b77c59b`. It imports the unchanged verified `check_r114.py` primitives (decoded source SHA256 `fcc99bad2d9352cbacb0c54aaa3cd69f0e7531ef9c4143cffb26261be97a295b`). Decode both source files into the same directory and run `python check_r115.py`. Both use only Python standard library exact `fractions.Fraction`.

The deterministic checker uses `(j,x,a,c)=(0,1/4,0,1)`, `I=[0,1]`, source times `-5..5`, branches `0..2` and exact S23 atoms. Three seeded historical fork campaigns `11511,11512,11513` produce 227 batched common-source edits; one targeted sharpness example contributes the 228th, plus one identical-version `∞` example.

It tests the pointwise identity against direct full atom recalculation, compares exact Top-k tuples at each finite capacity and the first disagreement, checks the exact low-stratum local certificate and rational minimizing witness, and compares 799 threshold-local Boolean decisions against direct global capacity.

Observed results: `R115_PASS`, 228 verified finite batches, 14,427 full atom checks, 12,275 local low-stratum representatives, 799 threshold certificates, 228 rational witnesses, one finite capacity jump, one `∞` case. The complete raw data are in `verification_r115.json` (SHA256 `35c11d4e0c622c3b71e6708eee7be0a2bf532c394e87dbd086242b5977fd071b`). These are bounded implementation checks, not exhaustive verification of all version pairs or mathematical independent review.

## 6. Next work

Maintain a *symbolic low-stratum index* and exact guard-range summaries across historical forks, combining R113 persistent rank-tree leaves, R111 reversible crossing support, R114 one-edit minimum-locus logic, and the present batched threshold-local pruning. Compare total construction, update, query, memory, history retention, arbitrary-precision bit work, and witness restoration against full partition recomputation for adversarial alternating edit batches. Maintain the frozen scientific pin and strict auxiliary-to-native type boundary.
