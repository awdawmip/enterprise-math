# BRC N=4 S23 time-only: exact ten-box threshold and nine-label plateau

Date: 2026-10-31. Status: **AUTHOR_FINITE_EXHAUSTIVE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a positive-mass finite observer theorem, not native P000/X6 dynamics.

## Frozen game, types, and quantifiers

Use the six latent cells (AU0, AU1, AV, BU0, BU1, BV) and the strictly positive P/Q sixteen-leaf source from the predecessor. Its six distinct prepared distributions on those cells are rows of

\[
 M=\frac1{20}\begin{pmatrix}
 10&10&0&0&0&0\\9&11&0&0&0&0\\0&0&20&0&0&0\\
 0&0&0&10&10&0\\0&0&0&2&18&0\\0&0&0&0&0&20
 \end{pmatrix}.
\]

The observation retains **only stopping time** \(T\in\{1,2,3,4\}\): no decision and no BU sensor or presence flag. A common stochastic source encoder \(E\) with \(k\) states is chosen before the legal stopping policy \(H\). At most \(m\) policy-label values \(L(H)\) may be communicated ex ante; a decoder \(D_\ell\) sees only the label and encoded state, not the complete policy, hidden source, or realized stopping coin. Total variation is used with the max over the six prepared rows:

\[
R_{k,m}^{S23}(T)=\inf_{E,L,D_1,\ldots,D_m}\sup_{H\ {\rm lawful\ S23}}\max_i
\operatorname{TV}((M K_H)_i,(M E D_{L(H)})_i).
\]

The S23 deterministic grammar has two first-stage A/B continuation bits, three second-stage AU=BU/AV/BV bits, and six third-stage latent-cell stop bits: \(4\cdot8\cdot64=2048\) tables. Behavioral randomizations respecting the same information sets are included **for the full-game upper bound**.

## Main theorem

**For every integer \(k\ge1\) and \(4\le m\le9\),**
\[
\boxed{R_{k,m}^{S23}(T)=2/3.}
\]
The lower bound uses only 64 deterministic lawful witnesses; the upper applies to all behavioral-randomized S23 policies. Sensor error \(\varepsilon\in[0,1/2]\) does not enter this time-only observation.

Define the restricted game \(R_{k,m}^{\mathcal S_{64}}(T)\) by allowing only those 64 deterministic signature policies. A second, exactly solved staircase is:

\[
R_{k,m}^{\mathcal S_{64}}(T)=
\begin{cases}
2/3,&4\le m\le9,\ k\ge1,\\
1/2,&10\le m\le63,\ k\ge4,\\
0,&m\ge64,\ k\ge4.
\end{cases}
\]

This restricted-game theorem **does not imply** that ten labels achieve 1/2 for the complete 2048-table S23 family or its randomizations.

## 64 genuine lawful signatures

For the four provenance classes (AU, AV, BU, BV), identify a signature \(s=(t_{AU},t_{AV},t_{BU},t_{BV})\) when both AU latent cells agree and both BU latent cells agree on deterministic stopping times. All six P/Q prepared rows then have deterministic time output according to the same four entries. Put \(H=\{2,3,4\}\), \(G=\{3,4\}\). The signatures are the disjoint union

\[
\begin{array}{ll}
 C_0=\{(1,1,1,1)\}&(1),\\
 C_1=\{(1,1,x,y):x,y\in H\}&(9),\\
 C_2=\{(x,y,1,1):x,y\in H\}&(9),\\
 C_3=\{(2,x,2,y):x,y\in H\}&(9),\\
 C_4=\{(x,u,y,v):x,y\in G,\ u,v\in H\}&(36).
\end{array}
\]

VERIFY.cpp independently enumerates all 2048 legal S23 tables using their first-/second-/third-stage information slots, derives all 64 unique signatures, and checks equality with these five classes. This does not silently assume that arbitrary four-coordinate signatures are legal.

## Why labels imply two-choice boxes

For a single policy label \(\ell\) and any fixed prepared provenance class \(j\), the reconstructed four-atom distribution \(q_{j,\ell}\) is independent of which policy in the label class was used. For a point-mass time output \(\delta_{s_j}\), loss \(<2/3\) forces
\[
1-q_{j,\ell}(s_j)<2/3
\quad\Longrightarrow\quad q_{j,\ell}(s_j)>1/3.
\]
A probability vector on four times has **at most two** entries strictly above \(1/3\). Consequently, every label's signatures lie inside a Cartesian product of four two-element subsets of \(\{1,2,3,4\}\). There are exactly \(6^4=1296\) maximal candidate boxes. This necessary condition holds for **arbitrary real-valued, randomized encoders**, all \(k\), and arbitrary label-conditioned randomized decoders.

## Exact exhaustive certificate: cover number is ten

Let \(\tau(\mathcal S_{64})\) be the least number of such maximal boxes covering the 64 signatures. The C++17 exact-integer executable proves

\[
\boxed{\tau(\mathcal S_{64})=10}.
\]

Full 1296-box incidence enumeration has 949 distinct 64-bit masks. Dropping any mask properly included in another leaves 270 nondominated masks; this preserves existence of a cover of any size. With positive signature-class weights (16,5,5,6,2), the total weight is 232 and each nondominated box has at most 32 weight and 16 points. Exhaustive recurrence uses uncovered 64-bit mask \(U\) and remaining-box budget \(r\):

* If \(U\) is empty, succeed. If \(r=0\), fail. If \(|U|>16r\) or \(w(U)>32r\), fail.
* Choose an uncovered point \(p\). In every possible covering family some selected box contains \(p\); branch over all nondominated boxes containing \(p\), recurse on \(U\setminus B\) with \(r-1\).
* Identical intersections on \(U\), or an intersection strictly dominated on \(U\) by an already exhaustively failed larger candidate, may be dropped. A failed \(U\) with budget \(r\) remains failed with any smaller budget, validating the memo.
* The code contains *no floating-point arithmetic* and asserts all source, geometry, mask-count, and global bound invariants. An actual selected full box is retained for a constructive witness.

Execution gives **no eight-box cover**, **no nine-box cover**, and an explicit **ten-box cover**. The earlier weighted inequality 232>7*32 excludes at most seven boxes, but not eight or nine; both newly resolved cases rely on this exact exhaustive search.

One independently checked ten-box witness (each row specifies two choices in AU, AV, BU, BV order) is:

```
(34)(24)(34)(24)   (34)(23)(34)(34)   (34)(34)(34)(23)
(24)(24)(12)(12)   (12)(12)(24)(34)   (12)(13)(23)(24)
(23)(34)(12)(13)   (24)(34)(12)(14)   (13)(12)(13)(13)
(12)(12)(14)(12)
```

Here `(34)` means the set \(\{3,4\}\), not the integer thirty-four. The recorded independent Python set-membership check recovered all 64 points, zero uncovered. All ten boxes are also printed by the C++ run.

## Restricted-game upper and exact 1/2 threshold

When \(k\ge4\), encode the provenance classes AU, AV, BU, BV into four distinct states (both AU cells share one, both BU cells share one). For each of the 64 policies choose any covering box as label. For label box \(B=(B_1,\ldots,B_4)\), decode provenance state \(j\) to the uniform distribution on the **two** times in \(B_j\). Since \(s_j\in B_j\), the total variation from the true \(\delta_{s_j}\) is exactly \(1/2\) for all six prepared rows. Thus ten labels achieve \(1/2\) on \(\mathcal S_{64}\), and all \(m\ge10\) can reuse them.

If an error were strictly less than \(1/2\), a fixed label would need \(q_{j,\ell}(s_j)>1/2\). For each \(j\) this permits at most one distinct time per label, so each label can cover **at most one** of the 64 different signatures. Thus \(m\ge64\) is necessary for error \(<1/2\), independent of \(k\). At \(m\ge64\), a separate label for each signature and the four provenance states exactly reconstruct every point mass, yielding zero. This closes the restricted staircase.

## Full-S23 upper 2/3 (analytic, independently restated)

For AU and BU separately, the Q preparation is the equal mixture \((F_0+F_1)/2\) of two latent-cell stopping laws, and P is another convex mixture. If Q assigns \(>2/3\) to time \(v\), then \(F_0(v)+F_1(v)>4/3\); for any \(u\ne v\), \(F_0(u)+F_1(u)<2/3\), so P cannot be heavy at \(u\). Each of AU and BU therefore contributes at most one distinct heavy time; each of AV/BV contributes at most one. If time 1 is not heavy, there are only three other times. If time 1 is heavy for A, the common first-stage A-only information forces all A prepared inputs to stop there with the same probability \(>2/3\), so none can be heavy later; B contributes at most two other heavy times. Symmetrically for B. Hence some \(t^*(H)\in\{1,2,3,4\}\) satisfies \(p_i^H(t^*)\le2/3\) for all six inputs, including randomized policies respecting the common information sets.

Communicate \(t^*\) with **four possible labels**, encode everything into one state, and decode uniformly over the other three times. For every input,
\[
\operatorname{TV}(p_i,q^{t^*})=1-\sum_{t\ne t^*}\min(p_i(t),1/3)\le2/3.
\]
This supplies \(R_{k,m}\le2/3\) for \(m\ge4\), combined with the exact nine-box impossibility proving the full theorem.

## Limits / independent review obligations

This is an **author-side computer-assisted finite exhaustive proof**, with complete checker source and actual execution evidence. The C++ search implementation and its dominance/memo recurrences still merit independent audit or formal verification; integer execution is not a native Source mathematical acceptance. The ten-label 1/2 construction is **only** for the 64 deterministic signature policies. Full S23 \(m=10\), S2 causal embed, alternative observer/label quantifier orders, P000 native X6 six-dimensional spatial Cell and separately typed physical-time correspondence, and signed/phase BRC dynamics remain open/independent.
