# Stage387-B — independent exact Stage373 central-band certificate audit

Date: 2026-11-03 (Asia/Shanghai). Research line: Research2, Draft PR #1736. Status: `PORTABLE_AUTHOR_PROOF / EXACT_FRACTION_EXECUTED / INDEPENDENT_IMPLEMENTATION / NOT_ADMITTED`.

## Frozen scientific input and model

Immutable science pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` (read and matched the frozen pin). Current applicable behavioral rules were read separately at GLOBAL main `8d1fc98178e194c7a79d10d2c1a8f81776fdb1e0` and EM main `74111b7ac7f0017ef0be88be4383ded05335dc2e`, not substituted for the scientific freeze. The mathematical object is the *external* Bernoulli/BRC two-source auxiliary observer. Native X6 six spatial axes, the three-dimensional slice, full provenance and typed future observations remain distinct from this auxiliary representation.

Let `W=(1,3,3,1)`, `M=(61,21,9,9)`, `B_k(z)=z^k(1-z)^(3-k)` for `k=0,1,2,3`, and let

\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{M_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3 W_k|r_k(x,y)|.
\]

For an anchor `a`, let `D(a,z)=1/2 sum_k W_k |B_k(a)-B_k(z)|`. Define the four independently labelled port costs

\[
 c(x,y)=\frac{63D(1/4,x)+D(3/4,x)+9D(1/4,y)+7D(3/4,y)}{256}.
\]

All 16 `(anchor,coordinate,k)` comparisons and all four residual channels enter the exact bounds separately. Let `q_*` be the unique joint root `r_0=r_1=0` in the box `x in [2310839,2310840]/10^7`, `y in [5555086,5555091]/10^7`, and `beta_*=b(q_*)`. Minimize `T(P,Q)=33/1024+c(P)+c(Q)` over `P,Q∈[0,1]^2` subject to `b(P)+b(Q)<=2beta_*+11/5000`.

## New independent verification theorem (conditional on inherited optimizer-core claims)

Assume Stage370's optimizer core `P,Q in (577/2500,239/1000]×(27/50,59/100)` and Stage372's source-relabelled strict x-straddle `x_P<469/2000<x_Q`. Then every global optimizer satisfies the *strict* central right-y condition

\[
 \boxed{\frac{57}{100}<y_Q<\frac{29}{50}}.
\]

This turn reconstructs Stage373's **8,544 entire-real-domain certificate leaves** using a separate implementation, independently of earlier stage programs. The regenerated deterministic CSV is **1,581,616 bytes** with SHA256 `fd8a761683245556cef44f15bd44fd1fadb539d6c3fa868f1dec6ff75b0bd5ae`, matching the original Stage373 recorded digest exactly.

### Certified continuous-domain bounds

Set `lambda=6/5`, `L=c+lambda*b`, `cut=469/2000`. The independent checker certifies strict lower bounds on the following three **closed** rectangles (including all shared edges and endpoints):

| region | complete rational rectangle | strict lower bound for `L` | closed leaves / max depth |
|---|---|---:|---:|
| LEFT_X | `[577/2500,cut]×[27/50,59/100]` | `1873/50000` | 4200 / 20 |
| RIGHT_Y_LE_57_100 | `[cut,239/1000]×[27/50,57/100]` | `37443/10^6` | 4258 / 23 |
| RIGHT_Y_GE_29_50 | `[cut,239/1000]×[29/50,59/100]` | `37445/10^6` | 86 / 14 |

The *smallest strictly positive leaf-level margins* `L_lower-threshold` computed and stored by the independent checker are respectively
`18206949944731/5368709120000000000000`,
`37718572861/42949672960000000000`, and
`5610727199121/5368709120000000000`.

### Why every leaf bound is valid for every real point

The verifier evaluates the four Bernoulli cubics through a power-basis Horner polynomial representation, independently of Stage373's factored polynomial code. On any rational interval `[u,v]`, the polynomial `B_k` has extrema only at endpoints or at interior `z=k/3`, so exact rational interval minima/maxima are known. For any interval `[a,b]` and rational target `q`, `max(0,a-q,q-b)` is a lower bound for `|z-q|` at every `z∈[a,b]`.

Applying this separately to each original port comparison and each residual gives exact rational `c_lower`,`b_lower`, hence `L>=c_lower+(6/5)b_lower` on the entire closed real rectangle. Every unaccepted parent is exactly bisected in x or y into **closed** children; no midpoint sample can substitute for a whole-box bound. The checker verifies strict inequality on every leaf, max depth below 40, number of leaves equals splits+1, and *exact total rational leaf area equals original rectangle area*. This establishes the universal inequalities without floating-point approximations.

### Feasible comparator and genuine cost exclusion

The independent script checks four exact Poincaré–Miranda boundary signs of `r0` and `r1`, with strict coordinate monotonicities. The joint root exists in the stated rational box and is unique there: `r0` strictly decreases with x and y, whereas `r1` strictly increases with x and decreases with y. Along `r0=0`, increasing x forces decreasing y, making `r1` strictly increase. By the exact identity `r0+3r1+3r2+r3=0`, and the signs `r2>0>r3` throughout the root box, `beta_*=(15/16)r2(q_*)`; monotonicity of `r2` gives the verified rational bracket. Thus

\[
 2\beta_*+\frac{11}{5000}<\frac{61}{6250}.
\]

The rational reference pair `P0=(231138/10^6,555681/10^6)`, `Q0=(237807/10^6,575694/10^6)` is strictly feasible, and its total audit cost is exactly

\[
 c(P_0)+c(Q_0)=\frac{16174439790495832521}{256000000000000000000}<\frac{6319}{100000}.
\]

For a feasible ordered pair in the inherited core with `y_Q<=57/100`, the support bounds imply

\[
 c(P)+c(Q)=L(P)+L(Q)-\frac65(b(P)+b(Q))
 > \frac{1873}{50000}+\frac{37443}{10^6}-\frac65\frac{61}{6250}
 =\frac{6319}{100000}+\frac1{10^6},
\]

which strictly exceeds the feasible reference by more than `1/10^6`. If `y_Q>=29/50`, the analogous strict gap is `3/10^6`. The boundaries are included in the excluded closed regions. This proves the necessary strict right-y localization, under the stated inherited optimizer-core hypotheses.

## Execution, evidence, scope

`REPRO_STAGE387B_INDEPENDENT.py` was executed twice with Python's exact `fractions.Fraction`, once with `--emit` producing the deterministic full CSV, once as a read-only replay; stdout was verified byte-identical. Exact CSV SHA256 and byte count match the Stage373 historical record. This is an **independent source implementation**, although it intentionally reuses the original model, thresholds and deterministic partition convention to test those exact assertions; it is not a fully independent formal-kernel proof of the entire upstream optimizer chain.

The immutable branch publication of the proof, checker, executed stdout, manifest and Stage388 continuation is a portable author-side mathematical artifact, not a formal native CLAIM, Result/Review, P000 theorem or X6 transfer. The *remaining dependency* for unconditional global localization is the Stage370 optimizer-core proof, Stage372 x-straddle proof and their Stage368/369 predecessors; none is erased by this independent Stage373 certificate.

## Next unresolved unit

Stage388-B: independently audit the Stage372 global optimizer x-straddle (two-same-side exclusions) together with its Stage370 core, starting from the original Stage372 exact 4,251-leaf rectangle certificate and Stage370's stated 2,948 leaf bounds. Verify the Stage368/369 dependency chain before treating the core as unconditional. If a source fails, preserve its first exact counterexample. Separately retain the typed observer-preserving P000/X6 three-dimensional-slice transfer question with explicit third coordinate, path/provenance and future operation scope.
