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


## 7. Signed-grade checksum and exact CRT depth amplification

**Theorem (exact effective-depth modulus).** In the same signed native lattice \(\mathbb Z^n\), for positive integers \(m,b\), augment the finite-depth observation by the *signed net-step grade*
\[
T(z)=\sum_{i=1}^{n}z_i,\qquad
K_{m,b}(z)=\bigl(r(z),[h(z)]_m,[T(z)]_b\bigr).
\]
The grade is an integer-valued **composite signed path observable**, not an additional native spatial axis; a native step \(\pm e_i\) changes it by \(\pm1\). Define
\[
\boxed{L=\operatorname{lcm}\left(m,\frac b{\gcd(b,n)}\right)
       =\frac{mb}{\gcd(b,nm)}.}
\]
Then for all \(z,z'\in\mathbb Z^n\),
\[
\boxed{K_{m,b}(z)=K_{m,b}(z')\iff z'-z\in L\mathbb ZD.}
\]
Thus the augmented observer is exactly the ordinary finite-depth quotient \(\pi_L\) under an alternative, incrementally maintainable encoding; it preserves the ordered signed-word **count** by the same LP026 fiber pushforward after replacing \(m\) with \(L\). If a key is realized and \(h_0\) is any compatible depth solution, its exact length-\(N\) BRC count is
\[
C_{N,K}=\sum_{t\equiv h_0\ (\mathrm{mod}\ L)} B_N(r+tD),
\]
with finite support as in §2.

**Proof.** Equality of min-zero representatives forces \(z'=z+tD\) for an integer \(t\); then \(h'=h+t\) and \(T'=T+nt\). The two residues agree precisely when \(m\mid t\) and \(b\mid nt\), i.e. \(m\mid t\) and \(b/\gcd(b,n)\mid t\), equivalent to \(L\mid t\). Conversely every shift by \(LD\) preserves all three recorded values. The same argument proves the exact BRC fiber formula, since endpoint fibers are disjoint signed-word sets. The transition on \((r,[h]_m,[T]_b)\) is well defined: use any representative integer \(h\), apply the native \(\pm e_i\) step to \(r+hD\), recanonicalize \(r,h\), and update \([T]_b\mapsto[T\pm1]_b\). Shifting the chosen lift by \(kmD\) leaves its \(\pi_m\) step unchanged; the checksum update depends only on the signed letter. QED.

**Sharp collision horizon.** The §6 fixed-length theorem applies to this augmented key with \(m\) replaced by \(L\):
\[
N_{\rm crit}(n;m,b)=
\begin{cases}
nL/2,&nL\text{ even},\\
nL,&nL\text{ odd}.
\end{cases}
\]
In X6 the sharp threshold is \(3L\); all native endpoints at a known exact signed-word length \(N<3L\) are recoverable, while every \(N\ge3L\) admits a collision. The same \(3L\) bound is the sharp *maximum-length horizon* \(H\) for the union of layers \(E_0\cup\cdots\cup E_H\): if \(H<3L\), distinct endpoints cannot share the key because a shift by \(kLD\ne0\) has \(\ell^1\)-distance at least \(6L\), so their maximum individual norm must be at least \(3L\). At \(H=3L\), the §6 pair already collides. The cross-length assertion is specific here to even-dimensional X6; odd-dimensional fixed-length parity gives a different threshold.

**Exact examples.** For X6, \(m=1,b=5\) gives \(L=5\) and first alias at 15 signed steps; \(m=2,b=5\) gives \(L=10\) and first alias at 30 steps. By contrast \(m=2,b=6\) gives \(L=2\), so the residue \([T]_6\) adds no depth discrimination and the first alias stays at 6 steps. For \(m=2,b=5\), the explicit first-alias endpoints \((-10,-10,-10,0,0,0)\) and \((0,0,0,10,10,10)\) have equal \(K_{2,5}\), each reached in 30 signed native steps. This shows a concrete CRT-guided checksum choice: values of \(b\) coprime to \(6m\) attain \(L=mb\), while shared factors may make some checksum states redundant for depth.

**Unbounded rotation scope.** Any mixed-sign signed-permutation phase still fails to descend on the *unbounded* \(K_{m,b}\) quotient, because shifts by \(LD\) remain identified and their transformed min-zero observations separate. For an anchored bounded signed-word horizon below \(3L\), reconstruct the unique endpoint first, then apply the phase; this is a finite-horizon exact observer protocol. It retains no claim about reconstructing ordered branch provenance or about a registered physical Heartbeat rotation rule.

**Exact checks.** A fresh integer-only test compared full signed endpoint-layer cardinalities with augmented-key cardinalities for all \(n=2,3,4\), \(m=1,\ldots,4\), \(b=1,\ldots,8\), \(N=0,\ldots,6\) (672 complete layers); every layer was injective exactly when \(N<N_{\rm crit}(n;m,b)\). Another 50,000 deterministic pseudo-random cases (seed 20261112, \(2\le n\le8\), \(1\le m\le15\), \(1\le b\le29\)) checked direct fiber equivalence and step update against chosen integer lifts, all passing. Those tests implement the above equations independently, **not** imports of current repository consumers. Original LP026 Author's separate 59,267-case DP/source-independent regression remains distinct; the current-source import branch in that checker is still an integration obligation.

**Consequence for the existing X6 research:** a native signed-step checksum modulo \(b\) can carry exactly quantified additional finite-depth information at one residue per event, using the same mathematical pushforward and avoiding full-depth storage within a specified horizon. This is a new Driver-context bridge lemma built from LP026's attributed BRC kernel and §§1–6; no independent Native Result, new CLAIM, physical law promotion, or Task/Objective closure is asserted.


## 8. Optimal worst-case endpoint side-memory over an unknown-length horizon

**Theorem (even-dimensional exact fiber capacity and information cost).** Fix an **even** native dimension \(n\ge2\), a cyclic depth modulus \(m\ge1\), an anchored zero starting Cell, and the full signed native alphabet \(\{\pm e_i\}\). Let \(B_H=\{z\in\mathbb Z^n:\|z\|_1\le H\}\), the set of all endpoints reachable in **at most** \(H\) signed primitive steps, without requiring the length to be known. Then
\[
\boxed{
\max_{k\in\pi_m(B_H)}|\pi_m^{-1}(k)\cap B_H|
=1+\left\lfloor\frac{2H}{nm}\right\rfloor.
}
\]
Consequently the sharp minimum **worst-case fixed-bit side memory**, in addition to the already observed cover key, that permits exact endpoint reconstruction anywhere in \(B_H\) is
\[
\boxed{
B_{\min}(n,m,H)=\left\lceil\log_2\left(1+
\left\lfloor\frac{2H}{nm}\right\rfloor\right)\right\rceil.
}
\]
For X6 this is \(B_{\min}(6,m,H)=\lceil\log_2(1+\lfloor H/(3m)\rfloor)\rceil\). It is a conditional encoding bound **per known cover key** and known external horizon \(H\); side-memory is an index of the compatible depth fiber, not a new spatial coordinate.

**Proof (upper bound).** All points in one cover fiber have the form \(r+(h_0+jm)D\). If the smallest and largest compatible depth differ by \(km\), the corresponding endpoints have \(\ell^1\)-distance \(nkm\). Both belong to \(B_H\), so by the triangle inequality \(nkm\le2H\). Since admissible depth indices are integers and the fiber has no more points than the full progression between its extremes, its cardinality is at most \(1+\lfloor2H/(nm)\rfloor\).

**Proof (sharp construction).** Set \(K=\lfloor2H/(nm)\rfloor\). Take the first \(n/2\) coordinates of \(z_0\) equal to \(-Km\), and the remaining \(n/2\) coordinates zero. For \(j=0,\ldots,K\), define \(z_j=z_0+jmD\). These \(K+1\) distinct native endpoints share exactly the same \(\pi_m\) key, while
\[
\|z_j\|_1=\tfrac n2(K-j)m+\tfrac n2jm=\tfrac{nKm}{2}\le H.
\]
Thus the upper bound is achieved. Any per-fiber code that uniquely distinguishes this fiber needs at least \(\lceil\log_2(K+1)\rceil\) bits; sorting the finitely many compatible integer depths and encoding their zero-based index attains this bound for every key. QED.

The theorem refines the first-alias threshold of §6: \(B_{\min}=0\) precisely when \(H<nm/2\) for even \(n\), and it grows in **logarithmic bits** with horizon when the cover modulus is held fixed. Examples: at \(n=6,m=1,H=5\) the maximum compatible depths are 2 (one bit); at \(H=30\) there are exactly 11 in the worst fiber (four bits); at \(n=6,m=2,H=30\) the maximum is 6 (three bits). A signed-grade checksum (§7) gives a simple *streaming modular alternative* and can match or exceed the needed discrimination depending on \(b\); the optimal per-fiber index need not itself support a one-residue-per-native-step update without additional bookkeeping.

**Independent exact test.** Enumerated the full \(\ell^1\) balls of signed-axis endpoints for \(n=2,4,6\), moduli \(m=1,\ldots,4\), and horizons \(H=0,\ldots,7\). Across all 96 combinations the maximum observed fiber cardinality matched \(1+\lfloor2H/(nm)\rfloor\), using exact Python integers and complete endpoint support. This result is a mathematically proved endpoint memory theorem with finite verification; neither current-source CoverState imports nor a physical signed rotation model is claimed by this test.

**Relevance:** For BRC/LP026 compressed computation, it gives a sharp information budget for reconstructing native signed endpoints from cyclic-depth projected states at a declared maximum path length. The branch/history population remains distinct; the same depth-repair bits alone do not recover ordered BRC branches or triadic interaction state.


## 9. Exact fixed-length fiber capacity in every dimension, and the odd-dimensional horizon extension

**Theorem (sharp depth-fiber capacities, all integer dimensions).** Let \(n\ge1\), \(m\ge1\), \(D=(1,\ldots,1)\), and \(\pi_m(z)=(z-\min(z)D,[\min(z)]_m)\). The native alphabet is the full set of signed unit steps \(\{\pm e_i\}_{i=1}^n\), with a fixed initial anchor \(0\). Write \(E_N\) for endpoints reachable in **exactly** \(N\ge0\) steps and \(B_H=\bigcup_{N=0}^{H}E_N\) for endpoints reachable within \(H\) steps. Set
\[
m_*=\begin{cases}m,&nm\ \text{even},\\2m,&nm\ \text{odd}.\end{cases}
\]
Then the largest fiber cardinalities are exactly
\[
\boxed{\max_k|E_N\cap\pi_m^{-1}(k)|=1+\left\lfloor{2N\over nm_*}\right\rfloor,}
\qquad
\boxed{\max_k|B_H\cap\pi_m^{-1}(k)|=1+\left\lfloor{2H\over nm}\right\rfloor.}
\]
The minimum worst-case number of *fixed-length binary side-memory bits*, conditional on knowing the cover key and the exact length \(N\), is the ceiling of base-two logarithm of the first displayed capacity. When the length is unknown but bounded by \(H\), replace it by the second capacity. The second formula extends §8's even-dimensional statement to **odd \(n\)**. The first formula is new even in X6: it sharpens the information budget when exact time/length is observed.

**Proof: fibers, parity and upper bounds.** Every cover fiber lies on one progression \(z_j=r+(h_0+jm)D\). Exact length \(N\) requires
\[
\|z_j\|_1\le N,\qquad \sum_i(z_j)_i\equiv N\pmod2.
\]
Because \(\sum_i(z_{j+1})_i-\sum_i(z_j)_i=nm\), the compatible indices are restricted to one parity class of \(j\) if \(nm\) is odd, and otherwise have no additional congruence restriction. Thus any two members of the same exact-length fiber differ by a multiple of \(m_*D\). For \(K+1\) distinct compatible endpoints the extreme separation has \(\ell^1\)-distance at least \(nKm_*\). The triangle inequality bounds that by \(2N\), proving the first upper bound. Without the exact-length parity condition, the same argument with \(m\) and \(2H\) proves the second bound.

**Proof: exact-length attainment.** Put \(K=\lfloor2N/(nm_*)\rfloor\). If \(K=0\), any realized key has capacity one. Otherwise \(A=Km_*\) and \(C=nA/2\) are integers because \(nm_*\) is even, with \(C\le N\) and \(C\ge1\). Choose an integer \(S\in[0,nA]\) of the same parity as \(N\) such that both \(S\le N\) and \(nA-S\le N\). Take \(S=C\) when \(C\equiv N\pmod2\); otherwise take \(S=C-1\), which is valid because \(C\ge1\) and the parity mismatch implies \(N\ge C+1\). Distribute \(S\) among integers \(t_i\in[0,A]\) with \(\sum_i t_i=S\), possible since the coordinate ranges have combined capacity \(nA\). Define \(z_j=(-t_i+jm_*)_{i=1}^n\) for \(j=0,\ldots,K\). These endpoints all have the same \(\pi_m\) key. The function \(j\mapsto\sum_i|jm_*-t_i|\) is convex, hence no larger on this interval than the greater endpoint value \(\max(S,nA-S)\le N\). Finally, every \(\sum_i(z_j)_i=njm_*-S\equiv N\pmod2\), since \(nm_*\) is even. Each \(z_j\) is therefore reachable by exactly \(N\) signed native steps, including cancellation pairs if necessary, and the first capacity is attained.

**Proof: unknown-length horizon attainment.** Put \(K=\lfloor2H/(nm)\rfloor\), \(A=Km\), and let \(S=\lfloor nA/2\rfloor\). Choose \(t_i\in[0,A]\) totaling \(S\) and define \(z_j=(-t_i+jm)_{i=1}^n\), \(j=0,\ldots,K\). The endpoint norms are \(S\) and \(nA-S=\lceil nA/2\rceil\le H\); convexity bounds all intermediate \(\ell^1\) norms by \(H\). All \(K+1\) endpoints have the same cover key and belong to \(B_H\). This attains the second capacity for any \(n\), including odd \(n\). QED.

**Parity-resolved examples and connection to previous results.** For \(n=3,m=1\), \(m_*=2\): at exact length \(N=2\) every cover fiber has one endpoint, whereas at \(N=3\) the pair \((-1,-1,-1)\), \((1,1,1)\) creates a two-endpoint fiber. If the length is unknown and only \(H=2\) is given, \((-1,0,0)\), \((0,1,1)\) already share one cover key (despite coming from different length parities). This explains the odd-\(nm\) parity jump in §6 without applying it incorrectly to mixed-length horizons. In X6, \(nm\) is always even, so both formulas reduce to \(1+\lfloor H/(3m)\rfloor\) after substituting the respective exact or maximum length. The theorem applies equally to the signed-grade augmented key of §7 after replacing \(m\) with its effective modulus \(L\).

**Executed exact finite check.** A fresh, source-independent exact-integer dynamic program enumerated all signed primitive endpoints \(E_N\) and their unions \(B_N\) for every \(n=1,\ldots,5\), \(m=1,\ldots,6\), and \(N=0,\ldots,8\): **270** complete parameter triples. For every triple it counted the largest min-zero/residue fiber in the exact layer and bounded-length ball independently, and both agreed with the two predicted formulas; zero mismatches. This does not replace the outstanding faithful-import check against current \`CoverState.step\` / signed-BRC consumers. The original LP026 author's attribution and existing Native Result state are preserved.

**Use.** On the registered free signed-native endpoint model, the correct side-memory allocation depends on whether the exact step count is part of the observation. In an odd-dimensional or odd-modulus slice, forgetting that parity can double the effective depth-spacing cost; retaining it gives the sharp smaller exact-layer capacity. No new physical Heartbeat update rule, independently accepted Native Result, or ordered-path provenance follows from an endpoint-only encoding theorem.
