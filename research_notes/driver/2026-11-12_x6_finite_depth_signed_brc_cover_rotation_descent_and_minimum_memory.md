# X6 finite-depth signed-BRC cover: exact rotation descent obstruction and minimum finite memory

Date: 2026-11-12. Role context: RESEARCH_DRIVER scientific auxiliary audit (not a Native Driver Review, not independent Result admission, no CLAIM or Task closure).
Status: AUTHOR_PROVED / EXACT TESTS (6000 deterministic cases) / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Sources and scope

This note connects two already saved, independently attributable pieces of evidence without changing either:
1. The on-hour author's [LP026 finite cyclic cover signed BRC pushforward](../X6_LP026_FINITE_CYCLIC_COVER_SIGNED_BRC_PUSHFORWARD_20261112_ONHOUR.md), including exact native signed-word multiplicity and cover-step pushforward. Its original author, checker, and not-admitted status remain unchanged.
2. The earlier Driver-authored [X6 correlated signed word and phase-observer note](2026-11-12_x6_correlated_signed_word_pair_graph_and_exact_phase_recovery.md), especially the distinction between full raw state and min-zero observer.

The algebra here is on the candidate signed free X6 lattice \(\mathbb Z^6\), not an assertion that a signed frame permutation is a physical P000/Heartbeat rotation. Spatial signed primitive steps are retained as path letters; ordered-path provenance, triadic closure and native time law are not inferred from endpoint BRC counts.

## 1. Exact quotient and transition/rotation distinction

Let \(n\ge2\), \(D=(1,\ldots,1)\), \(h(z)=\min_i z_i\), \(r(z)=z-h(z)D\). For \(m\ge1\), define
\[
\pi_m(z)=(r(z),[h(z)]_m)\cong\mathbb Z^n/(m\mathbb ZD).
\]
The \(m=0\) convention stores the full integer \(h\), hence \(\pi_0\) is lossless.

**Descent theorem.** Every native signed translation \(z\mapsto z\pm e_i\) descends to \(\pi_m\) for each \(m\ge1\). A signed-permutation linear map \(g\) (possibly followed by a fixed translation) descends to a well-defined self-map of \(\pi_m\) **if and only if** all signs of \(gD\) are identical. In particular, a mixed-sign phase fails to descend for every positive finite depth modulus, although all signed path-word transitions and their projected BRC multiplicities descend.

**Proof.** Since the equivalence relation is translation by \(m\mathbb ZD\), adding a fixed step preserves it. A linear \(g\) descends precisely if \(g(mD)\in m\mathbb ZD\); for an invertible signed permutation this is equivalent to \(gD\in\mathbb ZD\). Each coordinate of \(gD\) equals \(\pm1\), so this occurs exactly for \(gD=D\) or \(gD=-D\). When signs mix, \(z=0\) and \(z=mD\) have the same input cover key, yet their transformed relative parts are \(0\) and \(q(mgD)\ne0\), respectively. A constant affine translation cancels in this comparison. QED.

Thus a quotient can correctly execute and count native BRC signed **steps** without being safe for interleaved mixed-sign **rotations**. Neither a positive-only Coord6 kernel nor a finite common-depth cover makes this rotation admissible automatically.

## 2. Sharp minimum extra memory under a known signed-word length

Fix a measured cover key \((r,[a]_m)\), an exact signed-native word length \(N\ge0\), and unrestricted paths over \(\{\pm e_i\}_{i=1}^n\). Put
\[
S_{N,m}(r,a)=\{h\in\mathbb Z:h\equiv a\pmod m,\ 
    f_r(h)=\textstyle\sum_{i=1}^n|r_i+h|\le N,\ 
    N-f_r(h)\equiv0\pmod2\}.
\]
Every \(h\in S\) is realized by at least one signed length-\(N\) native path to the endpoint \(r+hD\): first take \(f_r(h)\) necessary signed unit steps and then add \((N-f_r(h))/2\) cancellation pairs. Conversely no other \(h\) is reachable by a length-\(N\) signed word. These are exact support conditions for the LP026 \(B_N\) multiplicity, not an approximation.

For a **mixed-sign** \(g\), the outputs
\[
q\bigl(g(r+hD)\bigr),\quad h\in S_{N,m}(r,a)
\]
are pairwise distinct: if two coincide, \((h-h')gD\in\mathbb ZD\), forcing \(h=h'\). Hence the minimum number of additional *fixed-length binary bits*, conditioned on this already known \((r,[a]_m,N)\), necessary and sufficient to determine the rotated relative observer is exactly
\[
\boxed{\left\lceil\log_2 |S_{N,m}(r,a)|\right\rceil}
\]
when \(|S|\ge1\). If \(|S|=1\) this is zero; if \(|S|=0\) the observed key is unreachable under the declared \(N\). The lower bound follows from pairwise distinct possible outputs; a compact index of \(S\) attains the bound. If \(gD=\pm D\), no extra depth bits are necessary. If \(N\) is unrestricted, \(\{h\equiv a\pmod m\}\) is infinite, and **no fixed finite number of bits** can make a mixed-sign rotation well-defined on all such cover states.

## 3. Exact interval and parity algorithm

Because \(r_i\ge0\) and \(\min r_i=0\), all reachable \(h\) lie in \([-N,N]\). The convex integer function \(f_r(h)=\sum|r_i+h|\) has an integer interval of sublevel solutions \(I_N=[\ell,u]\cap\mathbb Z\), possibly empty.

Using \(|x|\equiv x\pmod2\), the parity requirement becomes
\[
N-\sum_i r_i-nh\equiv0\pmod2.
\]

* When \(n\) is even (in particular X6), it is independent of \(h\): if \(N-\sum r_i\) is odd, the cover key has no length-\(N\) signed-word realization. Otherwise \(S\) is exactly the arithmetic progression \(h\equiv a\pmod m\) inside \([\ell,u]\), and
\[
|S|=\max\left(0,1+\left\lfloor\frac{u-a}{m}\right\rfloor-\left\lceil\frac{\ell-a}{m}\right\rceil\right).
\]
* When \(n\) is odd, impose additionally \(h\equiv N-\sum r_i\pmod2\). This yields either no solution or one CRT progression of modulus \(\operatorname{lcm}(m,2)\) in \([\ell,u]\), to which the same floor/ceiling formula applies with the correct residue.

No enumeration of all \(12^N\) ordered native words is required for this exact support-and-information calculation. This distinguishes exact endpoint recovery from recovery of the **ordered** BRC word, which the cover observation does not determine.

**X6 example.** For \(r=0\), \(N=6\), \(m=1\), \(a=0\), the reachable depths are \(S=\{-1,0,1\}\); a mixed-sign phase thus requires 2 additional bits, even though the modulo-one cover reports the same key for all three. For \(m=2,a=0\), \(S=\{0\}\) and zero bits suffice under this fixed length; for \(m=2,a=1\), \(S=\{-1,1\}\) and one bit suffices. With \(g=\mathrm{diag}(-1,1,1,1,1,1)\), the three modulo-one case outputs are respectively \((2,0,0,0,0,0)\), \(0\), \((0,2,2,2,2,2)\), all different.

## 4. Exact computational check

Executed a fresh deterministic Python integer-only check (seed 11) on 6000 random parameter tuples \(n\in\{3,4,5,6\}\), min-zero \(r\), \(0\le N\le20\), \(1\le m\le6\), and \(0\le a<m\). Direct enumeration of \(h\in[-N,N]\) satisfying native length, parity and cover congruence agreed in every case with the convex-interval-plus-parity arithmetic progression algorithm; for every nonempty reachable set, mixed-sign transformed relative observations were pairwise distinct. This checks implementations and examples; the general theorem is the algebraic proof above. The independent on-hour LP026 published checker was **not** claimed re-executed here.

## 5. Scientific relationship and next typed test

This is a scoped **bridge result**: native signed path dynamics and exact BRC pushforward are well-defined on every cyclic common-depth cover, but mixed-sign registered frame transitions are not. For a bounded length-\(N\) path endpoint, the minimal missing depth information is calculated exactly. The extra integer depth does not substitute for phase, force, incoming branch, ordered path, or actual Heartbeat law. A future native adapter must either retain the full lift, use this explicit finite support/index under a declared fixed word length, or restrict transformations to uniform-sign descent. Test actual CoverState and signed_brc callers separately before claiming a physical/operational implementation.

Authorship/provenance: this new cross-result is Driver-context mathematical reasoning; LP026 source author and its original Result/CLAIM/review states remain untouched. No independent Native Result accepted, Task completed, mother objective closed, or physical rotation law certified.
