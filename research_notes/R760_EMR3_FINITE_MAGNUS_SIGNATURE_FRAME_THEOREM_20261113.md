# R760 — Finite-order BRC path signatures cannot determine the auxiliary rooted S7 frame

Date: 2026-11-13 (Asia/Shanghai). Research type: exact general algebraic theorem plus finite, independent tests. Project: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Previous author-side work: R759, PR #2222, `7358218ccd7944b1258474606ef3ca4c7783ddcc`.

## Defined candidate, not a P000 primitive force event

Let `F_m=<x_1,...,x_m>` be the free group of rooted **ordered signed native-axis path words** for a fixed chosen axis subset `S` with `m` elements, `2<=m<=6`. A generator `x_i` is one `+E_i` unit adjacency, inverse `x_i^{-1}` one `-E_i` adjacency in the six-axis Cell torsor. The chosen Cell is an affine chart anchor; auxiliary label `*` below is **not** another spatial axis. These words may be read in X6 or in a selected three-axis slice of X6 when `m=3`; using two axes for a commutator is merely a supported subword, not a native two-dimensional plane.

Use R759's *declared candidate* rooted frame connection, not an admitted native V39 map: `t_i=(* i)` on the auxiliary labels `{*,1,...,m}` (fix the other labels of the full seven-label set), and define group homomorphism `phi:F_m -> S_(m+1)` by `phi(x_i)=phi(x_i^{-1})=t_i`. The R759 chronologically accumulated frame is `H(w)=phi(w)^{-1}` under the standard right-to-left permutation-composition convention. Both readouts have identical image/fiber cardinality.

For each `d>=1`, define the **complete truncated noncommutative Magnus path-signature observer** `M_d` in the ring of integral polynomials in noncommuting `X_i` modulo monomials of total degree greater than `d`:
`M_d(x_i)=1+X_i`; `M_d(x_i^{-1})=(1+X_i)^{-1}=sum_{j=0}^d(-X_i)^j`. Retain *all* word coefficients to degree `d`, not only displacement or a few projected areas. For `d>=2` it contains strictly more information than R759's `(displacement, 15 signed projected areas)` along the selected axes. Its kernel contains the `(d+1)`th lower-central subgroup `gamma_(d+1)(F_m)`. This is a mathematical observer, not an empirically established BRC transport component.

## Theorem: every finite-order signature fiber has the full alternating-group frame ambiguity

**For every `m=2,...,6`, every integer `d>=1`, and every finite signed path `u in F_m`,**

`{phi(v): M_d(v)=M_d(u)} = phi(u) A_(m+1)`.

Equivalently for `H` the frame set is `A_(m+1) H(u)`, an alternating coset. In particular, if `M_d(v)=1`, the available auxiliary final frames are **exactly** `A_(m+1)`, independent of `d`.

*Proof.* Write `gamma_1(F_m)=F_m` and `gamma_(k+1)(F_m)=[gamma_k(F_m),F_m]`. An element with Magnus expansion starting in degree at least `a` commuted with one starting in degree at least `b` has its first possible nonconstant term in degree at least `a+b`. By induction `M_d(gamma_(d+1)(F_m))={1}`.

The map `phi` is surjective onto `S_(m+1)` because star transpositions generate all transpositions via `(i j)=t_i t_j t_i`.

For any distinct axes `i,j`, put `c_2=[x_i,x_j]` and `c_(k+1)=[c_k,x_i]`. Each `c_k` belongs to `gamma_k(F_m)`. Let `a=phi(c_2)=(t_i t_j)^2`, a nonidentity three-cycle supported on `{*,i,j}`. Conjugation by `t_i` inverts `a`. Therefore `phi(c_(k+1))=[phi(c_k),t_i]` alternates between `a` and `a^{-1}`; in particular is a nonidentity three-cycle for every `k>=2`. Since `gamma_k(F_m)` is normal in `F_m` and `phi` is onto, `phi(gamma_k(F_m))` is a normal subgroup of `S_(m+1)` containing a three-cycle, hence it contains every three-cycle and therefore `A_(m+1)`. Conversely `gamma_k(F_m)` lies in the commutator subgroup for `k>=2`, so its image lies in `A_(m+1)`. Thus **`phi(gamma_k(F_m))=A_(m+1)` for all `k>=2`**.

Now `M_d(v)=M_d(u)` implies `M_d(u^{-1}v)=1`. Degree-one Magnus terms determine the exponent sum of each generator, so `u^{-1}v` has zero exponent sums. Its `phi` image is even, giving `phi(v) in phi(u)A_(m+1)`. Conversely, for any `h in A_(m+1)`, choose `z in gamma_(d+1)(F_m)` with `phi(z)=h`; then `v=uz` has `M_d(v)=M_d(u)` and `phi(v)=phi(u)h`. This proves both inclusions. QED.

## Explicit witnesses, length and information bound

For every `d>=1` the nested commutator `c_(d+1)` above has `M_d(c_(d+1))=1` but `phi(c_(d+1))` is a nontrivial three-cycle. Its unreduced signed-axis word has length `L_d=6*2^(d-1)-2` (4, 10, 22, 46, 94, 190 for degrees 1,...,6). For `d>=2`, its *six-dimensional* endpoint and all fifteen integer signed projected areas vanish, because the Magnus expansion has no degree-one or degree-two term. These are finite X6 signed path witnesses with explicit source order; they are not three-force `TRIADIC_CLOSURE_E` events.

For `m=6`, **every** fixed finite-degree signature fiber carries all 2,520 possible frame values within one parity coset, and recovering the full rooted frame requires at least `ceil(log_2 2520)=12` fixed bits *in addition to that signature*. The same exact bounds by supported axis count are `3,12,60,360,2520` for `m=2,...,6` (2,4,6,9,12 bits). Storing `H` itself attains the frame-only lower bound and composes by `H(uv)=H(v)H(u)`; this is not permission to erase ordered branch/provenance for other future observations. In particular, increasing any **fixed** truncation order cannot certify elimination of R759's frame residual over unbounded path length. On bounded path sets one may instead study finite observer sufficiency separately.

## Reproducible independent finite checks

`R760_VERIFY.py` implements exact integer noncommutative Magnus truncation, freely generated signed paths, 15 projected areas, star-transposition permutations, and full generated subgroup BFS. It checks every 15 two-axis pair for `d=1,...,6` (90 nonzero witness checks), all 75 degree-`>=2` zero-area witnesses, degrees 1 through 6 with maximum word length 190, and six complete group closures of size 2,520. Results in `R760_EVIDENCE.json`. The algebraic result is for *all* `d`; the finite checks are validation samples and do not replace the proof.

## Scientific interface still to determine

The frozen P000 triadic force arity/`PERP_E`=120° remain unchanged. A signed coordinate walk, auxiliary star transposition and formal signature have no automatic type coercion to native `PRIMITIVE_FORCE_QUANTUM`, `TRIADIC_CLOSURE_E`, V29 PASS/TRANSFER or V39 based-loop holonomy. The current task still needs a legal Cell/Link/Port three-force incidence predicate and an actual source-preserving update, followed by a proof or counterexample for a map from *that event algebra* into the candidate loop/frame algebra. This result sharpens the downstream observer-loss test once such a map exists; it is not a Result/Driver acceptance event.