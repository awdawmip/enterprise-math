# R762KD — Three flexible singletons: exact connected Euler theorem at one inactive Port

Date: 2026-11-23. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable mathematical note, not native protected PROGRESS, accepted Result or signed P000 dynamics.

## Model and frozen scientific input

Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; task publication `RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142`. Predecessor: R762KC, PR #3010, commit `73135e5353dcffe286344567bf9df1960294f675`.

The auxiliary **unsigned** model has 14 active Port vertices (V=\binom{\{0,\dots,5\}}2\setminus\{01\}) and 20 triple colors. Four forced colors (F=\{012,013,014,015\}) have one legal graph edge (0i-1i). The remaining 16 flexible colors (C) each permit all three edges of their corresponding triangle of pair Ports. An inventory (n_s\ge1) is realized by an edge-labeled connected multigraph on all 14 vertices, with exact count (n_s) per color and strictly positive even vertex degrees. It thus has an Euler circuit starting at any active Port.

## Theorem KD.1 — At most three flexible singletons

For **arbitrary positive integers** (n_s) on all four forced colors, and arbitrary positive integers on all 16 flexible colors subject to
[
|\{s\in C:n_s=1\}|\le3,
]
the inventory admits a connected all-Port even-degree Euler realization with exactly (\sum_s n_s) events. There is no restriction on the forced-color parities, on total event count, or on which three flexible colors are singleton.

### Lemma A: A flexible color of any multiplicity (n\ge2) realizes every prescribed one-edge GF(2) boundary and connects its entire triangle

For a prescribed edge (uv), with third triangle vertex (w), use edges (uw,vw) when (n) is even and append ((n-2)/2) identical-edge **pairs**. When (n) is odd use (uv,uw,uw) and append ((n-3)/2) identical-edge pairs. Both representations have the boundary (u\oplus v), exact multiplicity, and connected support on ({u,v,w}). Singleton colors contribute precisely one chosen edge. A forced color contributes its fixed edge (n) times.

### Lemma B: Every even Port boundary is attainable using one flexible edge of each of the 16 colors

Identify the 14-vertex even-parity space with (\mathbf F_2^{13}), dropping the last vertex bit. Initialize the integer convolution (N_0(0)=1); for each flexible triple (s), update
[
N_{j+1}(b)=\sum_{e\in E_s}N_j(b\oplus\partial e).
]
The exact exhaustive 16-stage integer computation evaluates all (2^{13}=8192) boundary targets and finds
[
\sum_bN_{16}(b)=3^{16}=43,046,721,\qquad
\min_bN_{16}(b)=3072,\quad\max_bN_{16}(b)=6819.
]
In particular every boundary has at least one assignment of one legal edge per flexible color. This is a finite computational lemma, reproducible from the complete short Python program in this batch, with exact integer arithmetic, no random input and no floating point. The larger local validation additionally compared each of the 8192 counts with an independent integer Walsh-transform computation and obtained exact equality.

### Lemma C: Deleting any three flexible colors leaves a connected backbone

Contract the four forced edges (02-12,03-13,04-14,05-15); there are ten quotient vertices. For each nontrivial quotient cut (511 cuts after fixing one side), count the distinct flexible colors whose triangles cross it. Complete exact enumeration gives minimum **four** crossing colors, attained on six cuts (the six isolated outer pair Ports (ij), (2\le i<j\le5)). Thus removal of any three colors leaves at least one crossing color on every cut. All non-singleton flexible colors of the retained set realize a connected path spanning their three vertices by Lemma A. Forced edges are always present because their multiplicities are positive. Their union consequently connects all 14 active Ports.

### Proof of KD.1

Take the forced-edge total boundary (b_F=\bigoplus_{s\in F}(n_s\bmod2)\partial f_s). By Lemma B choose one edge (e_s\in E_s) for each flexible color with (\bigoplus_{s\in C}\partial e_s=b_F). Realize each non-singleton color with the connected path or length-three pattern from Lemma A, and each singleton with (e_s). The exact flexible boundary equals (b_F), so adding forced edges gives total boundary zero: every Port has even degree. Lemma C gives global connectivity, hence every degree is positive. Edge counts are exact. Euler's undirected circuit theorem completes the construction.

## Corollary KD.2 — Complete `(d,t)=(2,2)` 42-event class

Let exactly two forced colors have count three and the other two have count one. Let exactly three flexible colors (D) have count one; choose five triple colors (T) from the remaining 13 flexible colors, and give the other eight flexible colors count two. Then the total event count is (2\cdot3+2\cdot1+3+5\cdot3+8\cdot2=42), and KD.1 applies to **every** such inventory.

The exact number of distinct labeled 42-event inventories is
[
\binom42\binom{16}3\binom{13}5=\boxed{4,324,320}.
]
Each inventory has precisely five singleton colors. Adding two occurrences of a single legal edge on any **marked** singleton color yields a connected 44-event source; removing those two copies recovers the target. Thus (\boxed{21,621,600}) marked (source inventory, removable color) pairs are constructed. The marking matters; this count is not a claim about distinct unmarked 44-event inventories.

An explicit **universal choice** of one edge from each flexible color for the forced-all-odd parity is:

```
023:02-03 024:02-04 025:02-05 034:03-04
035:03-05 045:04-05 123:13-23 124:12-14
125:15-25 134:13-14 135:13-15 145:14-15
234:24-34 235:23-25 245:24-45 345:34-45
```

For arbitrary forced parities, Lemma B's constructive integer DP recovers the corresponding assignment.

## Verification and provenance

Companion script: `R762KD_REPRO.py`; evidence `R762KD_EVIDENCE.json`. The local extended checker verified all 511 contracted cuts, all 8192 parity counts by **both** direct integer DP and integer Walsh transform, and 6720 concrete 42-event graphs (560 singleton triples × 6 forced-triple selections × 2 five-triple choices); all pass counts, legal edges, even strictly positive degrees, and connectivity. The published short checker independently reproduces the cut/DP claims and all 6720 actual graphs. A finite exhaustive certificate proves the exact lemma scope; the arbitrary-multiplicity conclusion follows from the symbolic local construction and cut argument, not from sampling arbitrary integers.

## Provenance boundary and next problem

This is a new author-side result for an unsigned auxiliary composite Port–Euler observer. P000 fixes a six-dimensional signed native space, primitive three-force `TRIADIC_CLOSURE_E`, native 120-degree Enterprise angle, ordered path/branch/multiplicity and BRC source information. No map establishing that each auxiliary colored graph edge is a legal signed primitive Cell/Link/Port transition, or that the Euler closed walk preserves native BRC provenance, has been proven. Freeze and worldview are unchanged.

Next: investigate **four** flexible singleton colors; the deleted-color connected-backbone criterion first becomes false on six minimal four-color cuts. Determine whether singleton edges and forced parities repair those cases, or produce an exact counterexample to universal Euler realizability. Independently address the signed event-lift and BRC observer safety.

Current native task snapshot as of 2026-11-23 08:27:33 UTC (`r3-20261123-1624-kd-task-read-v1`): `NEEDS_DISPATCH`, no actor/CLAIM, `execution_authorized=false`. This portable note does not use prior claimed identities as live protected-writer authority. Author proof remains `NOT_REVIEWED`.
