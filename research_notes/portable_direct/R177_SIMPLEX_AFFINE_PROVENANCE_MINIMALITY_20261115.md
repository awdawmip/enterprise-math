# R177 — Optimal simplex-affine provenance lift for finite transformation labels

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R176 at immutable `59fc5a4c6ab063b52e1baf7c10d4d848d5a46013`, `research_notes/portable_direct/R176_NATIVE_AFFINE_PROVENANCE_BRIDGE_20261115.md`.
Current source inspected: `src/enterprise_math/brc_transport.py` at Source `b9bb5ba5907d8c1001aa9e0365e2e9a724cf30b5` (native `Affine.then`, positive rational `EffectHistogram.from_terms/alternatives/then`).
Scope: six signed primitive X6 spatial steps in a chosen chart, path-ordered serial composition, positive rational-weight branch families with integer multiplicity, matched ports and finite provenance selectors. The label monoid is `T_n`, all self maps of an n-point finite source set (n≥2), or a submonoid faithfully acting there. Native X6 is still six spatial axes; provenance and prefix-sum registers are bookkeeping, not new native space axes.

## R177A — Affine-simplex action of every finite transformation monoid

Let Ω={0,...,n−1} and `T_n=Ω^Ω`. Define chronological multiplication `f*g=g∘f`. In `Q^(n−1)`, let `v_0=0` and `v_i=e_i` for 1≤i<n. For each `f∈T_n`, define the affine map

```
F_f(z) = v_{f(0)} + Σ_{i=1}^{n−1} z_i (v_{f(i)}−v_{f(0)}).
```

Then `F_f(v_i)=v_{f(i)}`. Every affine map is determined by its values on these n affinely independent vertices, so `F_g∘F_f=F_{f*g}`. If `F_f=F_g`, equality on the vertices yields `f=g`. Thus `T_n→Aff(Q^(n−1))` is a faithful unital monoid homomorphism, including all noninvertible constant transformations. For a finite monoid `M` with faithful action `M↪T_n`, its restriction is also faithful.

## R177B — Exact minimum affine state dimension for full `T_n`

**Theorem.** Every faithful unital homomorphism `ρ:T_n→Aff(Q^r)` has `r≥n−1`. The construction above achieves equality.

**Proof.** For each `i∈Ω`, write `c_i` for the constant map with value i. Faithfulness makes `ρ(c_i)` pairwise distinct affine maps. Their pairwise coincidence loci on `Q^r` are proper affine subspaces; a finite union of those subspaces cannot cover `Q^r`. Choose `z` outside their union, so the points `x_i=ρ(c_i)(z)` are pairwise distinct. As `c_i*f=c_{f(i)}`, the homomorphism law gives `ρ(f)(x_i)=x_{f(i)}` for every `f∈T_n`. Suppose a nonzero affine dependence `Σ_i λ_i x_i=0`, `Σ_i λ_i=0` exists. Choose an index j with `λ_j≠0`, and distinct a,b∈Ω. Let f(j)=a and f(i)=b for every i≠j. Because affine maps preserve affine dependencies, one would have
`0=Σ_i λ_i x_{f(i)}=λ_j(x_a−x_b)`, a contradiction. Hence the n points are affinely independent in `Q^r`; necessarily `r≥n−1`. QED.

This is a minimum for **faithful affine representations of the entire transformation monoid**. It is not an assertion that every narrower observer, arbitrary provenance monoid, or globally shared spatial/label encoding has the same minimum.

## R177C — Exact six-axis BRC affine action and port algebra

For an ordered native signed-step path `P=(u_1,...,u_ℓ)`, define its displacement `D(P)=Σ_t u_t∈Z^6` and prefix integral `J(P)=Σ_{t=1}^ℓ Σ_{s=1}^t u_s∈Z^6`. On `Q^6_x⊕Q^6_j⊕Q^(n−1)_z`, define

```
U(f,P)(x,j,z)=(x+D(P), j+ℓx+J(P), F_f(z)).
```

Then `U(f,P).then(U(g,Q))=U(f*g,PQ)` because `J(PQ)=J(P)+J(Q)+|Q|D(P)` and R177A respects chronological provenance composition. Equality of the affine actions recovers `f` from the label block, path length from the j-from-x coefficient, D from the x offset and J from the j offset; conversely those data determine the affine action. Thus this is a faithful carrier for the path quotient `(f,|P|,D,J)`.

For `T_n` the rational affine state dimension is

```
N_R177(n)=12+n−1=n+11,
N_R176(n)=12+|T_n|=12+n^n.
```

Examples: `T_2: 16→13`, `T_3: 39→14`, `T_4: 268→15`. The native positive `EffectHistogram` may store positive rational weight, full `U` affine action and integer multiplicity as one joint atom; its `then` uses action composition and multiplicative weights/counts, so alternatives, coalescence and serial port composition are exact. Noninvertible labels are supported by `Affine.then`; no inverse is invoked.

## R177D — Four-moment descent and preservation lease

At each port pair and transformation label f, project the positive branch histogram to

```
A_f=Σ wc, L_f=Σ wc|P|, B_f=Σ wcD(P), C_f=Σ wcJ(P).
```

The exact laws for a serial pair of families are, with label products and intermediate-port sums implicit,

```
A(FG)=A(F)A(G)
L(FG)=L(F)A(G)+A(F)L(G)
B(FG)=B(F)A(G)+A(F)B(G)
C(FG)=C(F)A(G)+A(F)C(G)+B(F)L(G).
```

They follow termwise from R177C and extend to arbitrary finite serial/alternative expressions by induction. Under the R175 observation contract—individually selectable f-labeled C readouts after arbitrary compatible two-sided serial contexts—the inherited four-moment projection is an exact observer quotient. The fine native effect histogram still retains the joint (weight,action,multiplicity) atoms.

If an original ordered provenance word is mapped into `T_n`, such compression is valid only for future operations/selectors that factor through this declared transformation label. Selectors that distinguish words with identical transformations require retaining the original source word or a stronger typed provenance coordinate. The labels are operators on a finite *source set*, not physical spatial directions or an asserted heartbeat time evolution. No physical residual attribution or BRC–Shor outcome is claimed.

## Finite exact verification

The companion executable `R177_simplex_affine_check.mjs` runs using portable ECMAScript. It checks all maps and all pairs for n=2,3,4 (16+729+65,536 label products); full faithfulness of the n^n distinct affine actions; 784 and 3,645 ordered joint affine path compositions in six native axes for n=2 and n=3; 36 rational positive-weight port-family products at each n=2,3; and 36 exact four-moment product identities at each n. Integers in the tests remain within the exactly representable IEEE-754 integer range and all rational weights use reduced integer numerator/denominator pairs, not floating approximations. Full n and all finite paths are covered by symbolic proofs; the finite tests cover the declared cases only.

Result: `R177_EXACT_SIMPLEX_PROVENANCE_LIFT_PASS`. Native imported `enterprise_math.brc_transport` tests actually run: **0** (the proof follows the interface source; this script is an independent exact reference). Independent review and formal Foundation promotion: **NOT_REVIEWED / NONE**.

## Next independent problems

1. Build an adapter importing the actual `Affine` and `EffectHistogram`, run the exact six-axis `T_2,T_3` positive branch/port cases and compare against this finite reference.
2. For real source selectors, find the smallest faithful finite action or prove that word-sensitive observations require stronger provenance; do not delete joint relation/history without a fiber-constancy certificate.
3. Compare dense affine matrix storage/operation counts with sparse block composition on realistic packets; measure construction, decoding, multiplicity and rational numerator growth rather than inferring runtime gains from dimension alone.

Control observation: `RS-S23-AV` continuation request `em-r1-20261115-1559-r177-s23-read-v1` returned `FAILED / CANONICAL_REJECTED: unknown current immutable task publication` (no formal CLAIM established). This science is independent portable research.
