# R178 — Lossless chronological X6 path embedding into native BRC affine effects

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_REFERENCE_CHECKED / NOT_REVIEWED.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Immediate predecessor: R177, immutable commit `cea759ff34827a814257d102c201176f34ec821d`, `research_notes/portable_direct/R177_SIMPLEX_AFFINE_PROVENANCE_MINIMALITY_20261115.md`.
Native implementation read: `src/enterprise_math/brc_transport.py` at canonical main blob `be1debe367263931bd5e93fd750be3ed54624fe1`. This research does not change P000, the six native axes or the locked scientific inputs.

## Problem and typed setting

R171–R177 retain signed X6 six-axis displacement `D(P)`, the sum of all prefix displacements `J(P)`, path length, and a finite provenance action. Their common affine carrier need not retain the original ordered word: distinct native paths can have the same `(|P|,D(P),J(P))`. The question is whether the exact chronological word can be represented by **one additional affine bookkeeping coordinate** under the actual `Affine.then` operation, preserving positive weighted branches.

Let `Σ={+E_1,-E_1,...,+E_6,-E_6}` be exactly the twelve *directions* of the six X6 native spatial axes. All these are signed unit directions in a chosen relative Cell chart, not 12 new axes. Choose an injective digit map `c:Σ→{1,...,12}`, and set `B=13`. For a finite path `P=s_1...s_m`, define

`h(P)=Σ_{i=1}^m c(s_i)B^{m-i}`, with `h(ε)=0`.

For each path define the affine map on the additional one-dimensional rational register

`H_P(t)=B^m t+h(P)`.

The register is **provenance bookkeeping**, not a seventh spatial axis or time coordinate.

## R178A — Faithful chronological free-monoid embedding

**Theorem.** For all finite paths `P,Q`,

`h(PQ)=B^{|Q|}h(P)+h(Q)` and `H_P.then(H_Q)=H_{PQ}`.

The map `P↦H_P` is injective on the free monoid `Σ*`, including the empty path and paths of different lengths.

**Proof.** The displayed formula follows by splitting the positional base-`B` sum into its first `|P|` and last `|Q|` terms. Applying `H_P` before `H_Q` produces the map `t↦B^{|Q|}(B^{|P|}t+h(P))+h(Q)`, exactly `H_{PQ}`. Equality of two affine maps implies equality of positive slopes `B^{|P|}=B^{|Q|}`, so lengths coincide. Equality of intercepts then gives the same length-`m` base-`B` expansion, with digits in `{1,...,12}`. Uniqueness of positional representation forces equality at every step. The empty path is the identity map. ∎

The result applies to any finite native alphabet with `a` letters by using `B=a+1`. No finite-prefix or periodicity hypothesis is used.

## R178B — Lossless joint embedding with finite provenance labels

Use R177's faithful simplex affine representation `F_f` of a finite source-label monoid `M↪T_n` on `Q^{n-1}`, with chronological label multiplication `f*g=g∘f`. Define on a state `(x,j,z,t)\in Q^6×Q^6×Q^{n-1}×Q`:

`U(f,P)(x,j,z,t)=(x+D(P), j+|P|x+J(P), F_f(z), B^{|P|}t+h(P))`.

Here `D(P)=Σ_i s_i` and `J(P)=Σ_{k=1}^{|P|}Σ_{i=1}^k s_i`. The total affine state dimension is `6+6+(n-1)+1=n+12`.

**Theorem.** `U(f,P).then(U(g,Q))=U(g∘f,PQ)`. Moreover `U(f,P)=U(g,Q)` iff `f=g` and `P=Q`, assuming faithful `M↪T_n`.

**Proof.** The X6 blocks compose by `D(PQ)=D(P)+D(Q)` and `J(PQ)=J(P)+J(Q)+|Q|D(P)` (R171). The source block composes by the faithful simplex representation (R177). The final block composes by R178A. If two full maps are equal, equality of the final block determines the entire ordered path, and equality of the source block determines the source label. The converse is immediate. ∎

This is a direct mathematical adapter for the existing `Affine` matrix/offset API: its block matrix is `[[I6,0,0,0],[m I6,I6,0,0],[0,0,A_f,0],[0,0,0,B^m]]` with offset `(D,J,b_f,h)`. `Affine.then` in current `brc_transport.py` uses exactly chronological composition `(BA,Bb+c)`. No new algebraic primitive is required.

## R178C — Exact positive-branch BRC histogram lift

For a finite multiset of terms `(w,f,P,r)` where `w∈Q_{>0}` and multiplicity `r∈Z_{>0}`, map each term to `(w,U(f,P),r)` and form `EffectHistogram.from_terms`.

Because `(f,P)↦U(f,P)` is injective, canonical coalescing by the joint key `(w,U)` preserves exactly the original multiset of **weighted (source label, ordered path)** tuples, up to aggregation of equal tuples into their integer multiplicity. Native `EffectHistogram.then` sends each pair to weight `w_1w_2`, action `U(f,P).then(U(g,Q))`, and multiplicity `r_1r_2`. Therefore it agrees exactly with source-label composition and chronological path concatenation. Native `alternatives` adds multiplicities of equal full tuples.

**Scope.** The representation distinguishes ordered paths, finite source labels, positive rational weights and counts. It does not independently identify two otherwise identical branches by an external unique branch ID; such an observer needs an explicit additional branch selector. Signed coefficients are also not positive branch weights. This lifting is not a native force/rotation dynamics proof.

## R178D — Sharp first alias depth of the R171 four-moment path projection

The tuple `(|P|,D(P),J(P))` is injective for paths of length `m≤3` over the 12 signed unit directions, but loses ordered-path identity already at `m=4`.

**Proof for `m≤3`.** For two same-length paths write `δ_i=s_i-t_i`. Equality of `D,J` for `m=2` gives `δ_1+δ_2=0` and `2δ_1+δ_2=0`, forcing both to vanish. For `m=3` it gives `δ_1+δ_2+δ_3=0` and `3δ_1+2δ_2+δ_3=0`, hence `δ_2=-2δ_1`. Every nonzero difference of two signed coordinate units is either `±2E_i` or `±E_i±E_j` with `i≠j`; twice such a difference cannot itself be a difference of two signed coordinate units. Thus `δ_1=0`, followed by `δ_2=δ_3=0`. The one-step case is immediate.

**Four-step witness.** Let `e=+E_1`, `f=-E_1`. The two distinct paths

`P=(e,f,f,e)`, `Q=(f,e,e,f)`

both have length four, final displacement zero and prefix sum `J=0`. Their four-moment-path actions coincide on `(x,j)`. With digits `c(f)=1,c(e)=2`, their positional codes are `h(P)=4578` and `h(Q)=2562`, so the R178 full actions remain distinct. ∎

This is the **smallest** possible alias length for the `(m,D,J)` carrier on signed X6 unit-step paths, and gives a concrete reason to retain the extra path coordinate when the declared future observers can ask for the exact ordered word.

## R178E — Storage-bit accounting and necessary distinction

There are exactly `12^m` ordered X6 native paths of length `m`. Any injective binary encoding for this fixed-length family requires at least `ceil(m log2(12))` bits in the worst case. The positional integer `h(P)<13^m` uses at most `ceil(m log2(13))` bits, up to the usual zero/length convention. Thus the code has optimal **Θ(m)** bit storage order. Its affine slope `13^m` adds another Θ(m)-bit integer; storing the length or deriving the slope avoids mistaking a fixed-dimensional representation for constant-bit storage.

No runtime speedup is claimed. Dense `(n+12)`-dimensional affine composition, materializing all branches, integer multiplication and output recovery have separate costs. One compressed coordinate is useful for exact composition and retention of identity, not for constant-size physical state.

## Exact verification and reproducibility

The accompanying `R178_lossless_native_path_code_check.py` is an independent exact reference with optional native import. Its local invocation was `python R178_lossless_native_path_code_check.py`. Full enumeration checked the code and `(D,J)` uniqueness for all `1+12+144+1728+20736=22621` paths of lengths `0..4`. At `m=4`: 20,305 distinct `(D,J)` pairs and 431 excess colliding words, versus 20,736 distinct positional codes. It also checked 180 exact matrix compositions for `T_3` labels and sampled signed X6 paths, and 36 exact positive-rational histogram products. All standalone checks passed.

The actual Python package `enterprise_math` is unavailable in this execution sandbox, so the optional **native module import-and-composition check is PENDING**; the reference uses the native API's publicly read current mathematical semantics but is not represented as a successfully executed native test. The code executes native assertions automatically in a project runtime where the package is installed. See `R178_verification.json` for exact coverage and status.

## Source/role state and next questions

- Scope: independent portable research, no shared protected Task/CLAIM mutation. The original `RS-S23-AV` directory lookup request `em-r1-20261115-1705-r178-s23-publication-check` read back `SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `5a1651a21831ea8d991f682468eaca4ac3aca28b`. It did not evaluate the full owner projection, and grants no execution authority.
- Own predecessor research identity source: `EM-DIRECT-BF4AD7`, Session `MCP-46f202db13e64ad6b4c8860e06908245`, Activity `RA-7A118452894D2600AE7DE5A2`; public recovery read verifies that Session remains open, while formal TASK claim/authorization is false. A new Activity checkpoint for R178 requires the source's actual authorized association and is separate from publication.
- Next: execute the optional native `Affine`/`EffectHistogram` check in the actual repository Python environment, evaluate the genuine finite provenance-selector action needed by BRC users, and compare total bit/operation cost of full ordered-path encoding versus the minimal `(D,J)` observer quotient and any source-word-sensitive selectors. Retain external branch IDs when observers require them.

Proof and finite calculation are author-side research; independent review remains `NOT_REVIEWED`. No Foundation admission or physical claim is made.
