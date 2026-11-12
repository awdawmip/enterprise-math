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


## 6. Sharp first fixed-length alias horizon (signed native paths)

**Theorem (exact universal first-alias length).** For any \(n\ge2\), modulus \(m\ge1\), and signed unit alphabet \(\{\pm e_i\}_{i=1}^n\), let \(E_N\subset\mathbb Z^n\) be the endpoints of *exactly* \(N\) steps from the chosen zero anchor. The finite cover map \(\pi_m\) is injective on \(E_N\) for every \(N<N_{\rm crit}\), while for **every** \(N\ge N_{\rm crit}\) it is not injective, where

\[
\boxed{N_{\rm crit}(n,m)=
 \begin{cases}
 nm/2,&nm\ \text{even},\\
 nm,&nm\ \text{odd}.
 \end{cases}}
\]

In native X6, \(N_{\rm crit}(6,m)=3m\) without exceptions. Consequently a finite cyclic depth cover of modulus \(m\) retains **the entire native endpoint**, not only BRC endpoint counts, on the declared exact-length layer \(E_N\) whenever \(N<3m\). This does **not** make mixed-sign rotation descend on the unrestricted quotient or preserve ordered branch histories; the claim is conditional on the given start anchor, free signed alphabet and fixed path length.

**Proof of lower bound.** Two distinct endpoints having the same \(\pi_m\) value differ by \(kmD\) for nonzero integer \(k\). Their endpoint lengths obey
\[
2N\ \ge\ \|z\|_1+\|z+kmD\|_1
\ \ge\ n|k|m.
\]
Moreover an exact signed path of length \(N\) reaches \(z\) only if \(N\equiv\sum z_i\pmod2\), and the same for \(z+kmD\). Thus \(nkm\) must be even. The least permissible \(|k|\) is \(1\) if \(nm\) is even and \(2\) otherwise. Therefore \(N\ge N_{\rm crit}\).

**Attainment at the boundary and beyond.** Choose that least positive \(k\), set \(L=km\) and \(C=nL/2=N_{\rm crit}\), an integer. Select integers \(0\le t_i\le L\) with \(\sum t_i=C\) (such a choice always exists) and set \(z_i=-t_i\), \(z'_i=L-t_i\). Then \(z'=z+kmD\), while \(\|z\|_1=\|z'\|_1=C\). Both endpoints are attained by signed \(C\)-step paths and have the same cover key. For larger \(N\) of the same parity, insert canceling \((+e_i,-e_i)\) pairs. To realize the other parity, replace one coordinate \(z_i\) by \(z_i+1\) and \(z'_i\) by \(z'_i+1\). Both new norms are \(\le C+1\), have parity \(C+1\), and thus both endpoints are reachable at length \(C+1\), then at \(C+3,C+5,\ldots\) by canceling pairs. This proves the *every* \(N\ge C\) assertion.

**Concrete X6 earliest witnesses.** At \(m=1,N=3\), the distinct endpoints
\[
(-1,-1,-1,0,0,0),\qquad (0,0,0,1,1,1)
\]
share the same modulo-one cover key and are both realized by three signed primitive steps. For \(m=2,N=6\), replace \(\pm1\) by \(\pm2\); their depth residues coincide modulo 2. For arbitrary \(m\), the analogous pair \((-m,-m,-m,0,0,0)\) and \((0,0,0,m,m,m)\) witnesses first alias at \(3m\). Any mixed-sign signed-permutation \(g\) produces distinct rotated min-zero observations on such a pair, by section 2's injectivity-in-depth argument.

**Finite checks and implementation boundary.** Fresh exact-integer enumeration of complete signed endpoint supports at \(N_{\rm crit}-1\), plus constructive collision searches at \(N_{\rm crit}\), passed for 14 parameter pairs \(2\le n\le6,\ 1\le m\le3,\ N_{\rm crit}\le10\). The observed first thresholds were \(n=2:(1,2,3)\), \(n=3:(3,3,9)\), \(n=4:(2,4,6)\), \(n=5:(5,5)\), and \(n=6:(3,6,9)\), listed by increasing \(m\) among checked cases. These are finite consistency tests; the proof above supplies the general result. Current source inspection confirms \`CoverState.step\` in \`experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py\` uses a representative integer lift and depth reduction, and \`signed_brc.endpoint_multiplicity\` supplies the signed full-endpoint counts. This turn did **not** execute a faithful current-source import test.

**Route:** For an endpoint-specific observer or subsequent mixed-sign phase after a known signed-word horizon \(H\), modulus \(m>\!H/3\) (equivalently \(m\ge\lfloor H/3\rfloor+1\)) suffices to reconstruct the native endpoint at that horizon. If \(H\ge3m\), no unconditional same-cover endpoint reconstruction is possible on the full free-word endpoint set. For nonfree, phase-restricted or triadic admissible words, recompute the actual reachable fiber before applying this universal threshold; all original authorships and native Result/Task review boundaries remain unchanged.
