# R122.2 — Exact fiber-clipped Sturmian vocabulary

Scientific type: author-side S23 auxiliary arithmetic-progression observer. Companion to R122-FIBER, frozen input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Theorem and constructive reduction

In R122.1, consider a single integer k band of `d*theta` over `J=(l,h)`. Put `v_-=min(dl,dh)`, `v_+=max(dl,dh)`, and `B_k=(max(0,v_--k), min(1,v_+-k))` with the natural available boundary from the intersection `(v_-,v_+)∩[k,k+1)`. This is a nonempty interval of beta-values whenever that k band intersects J.

Define the **restricted** lift set

`P_m(B_k)={ (floor(alpha+i*beta))_{i=0}^{m-1}: 0<=alpha<1, beta in B_k }`.

Any actual S23 parameter theta in that k band has `alpha=frac(x+(N-j)*theta)` and `beta=d*theta-k in B_k`, hence its actual lift q belongs to `P_m(B_k)`. Replacing universal `P_m` by `P_m(B_k)` in R122.1 is therefore **exact**: it never deletes a feasible original parameter, and the subsequent shared-theta inequalities still exclude false positives.

The restricted vocabulary is computable without enumerating phase cuts depending on large N or d. Enumerate the finite lines `alpha+i*beta=h` (`1<=i<m,1<=h<=i`) within the clipped square `0<=alpha<1, beta in B_k`. Split beta at exact line intersections and line-boundary crossings that lie in the clipped range; sample rational interior beta between successive splits and rational alpha between successive active line intercepts. The sampled floor vectors are exactly `P_m(B_k)`. To justify boundary values: at any finite intersection or half-open threshold, perturb alpha slightly upwards and beta by a sufficiently smaller positive or negative amount within the nonempty clipped interval. Each equality retains its higher-side floor; the finitely many non-equalities retain their values. Thus no extra q occurs only at a boundary. Beta=0 is covered by a small positive beta perturbation. The line arrangement is polynomial-sized in m and rational bit length; its cost is included separately from querying the reduced one-integer systems.

The oracle now needs at most `2^m * sum_{k in K(J,d)} |P_m(B_k)|` one-integer systems for one requested bit vector. It is never a weaker completeness guarantee than the universal vocabulary. No claim is made that the clipped vocabulary is always smaller, or that a generic total execution-time speedup follows without measuring the arrangement-generation overhead.

## Executed exact test

`check_r122_clip.py.gz.b64` is a gzip/base64 Python 3 `Fraction` script, to be decoded in the same directory as `check_r122.py`. Deterministic seed 12222026: 60 signed random cases with m in {2,3,4,5,7}, 2,256 exact bit-signature feasibility queries. The clipped oracle agreed in every case with R122's universal vocabulary oracle, including 228 positive witnesses checked against the original S23 predicate. Across the 63 k-bands, total unrestricted q-candidates numbered 792 versus 319 clipped q-candidates. In three illustrative narrow beta intervals of width 1/10000 at beta=1/5,3/7,7/11, with m=13, the exact vocabulary count was 13 each versus 224 universal patterns. Counts are oracle candidates rather than measured whole-program speedups.

Return: `R122_CLIPPED_PASS`. General native X6/Cell/Link/Port consequences and formal independent review remain unestablished.

## Next

Develop a less-than-arrangement-size generator for narrowly clipped mechanical words; combine the cheap one-integer fiber oracle with a genuine 2D integer feasibility implementation for wide k bands.
