# EC49FOY — Exact five-terminal-observation minima in two frozen native BRC classes

**Science status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
**Immutable scientific input pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
**Frozen original input SHA-256:** `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
**Scientific parent:** EC49FOX, PR #2445, commit `92e2b5479df80bcfeca5e1be5226a701229410d9`.
**Data scope:** Original frozen 94-key, 178,850-word, 38,169-configuration BRC byte-prefix-Trie cache corpus; complete named-root legal-domain classes represented by configuration IDs 14304 and 14309.

## Theorem FOY-1 (exact sparse terminal observation minima)

In each of the two specified complete legal-root-domain classes, the minimum number of **fixed legal complete root allocations** whose terminal integer costs distinguish every distinct reachable named-root/subset cost vector is exactly

\[
m_{14304}=m_{14309}=\boxed{5}.
\]

Here the four named roots are `03,05,06,07`, demand labels are `0,...,23`, and all chosen observations are complete legal assignments of every optional demand to exactly one of its legal named roots. Mandatory demands remain at their unique legal root.

Each complete class has 75 configurations, 40 distinct reachable named-root cost profiles, and 432 legal complete allocations. The preceding EC49FOX theorem proved that in each class the full 432-coordinate terminal-cost vector distinguishes all 40 rooted cost profiles. Therefore the present minimum is well-defined relative to these frozen classes.

### Exact collision-mask lemma

Let \(Q\) be the 40 distinct rooted cost profiles in a fixed class, and \(E=\binom{Q}{2}\), with \(|E|=780\). For a complete legal allocation \(a\), let

\[
M_a=\{\{u,v\}\in E:T_u(a)=T_v(a)\}
\]

be its indistinguishable-profile-pair mask. A set \(A\) of terminal allocations distinguishes all 40 rooted profiles if and only if \(\bigcap_{a\in A}M_a=\varnothing\). This is immediate by quantifying over each unordered pair \(u\ne v\).

Deduplicate the 432 original masks, leaving 425 distinct masks in each class. Let

\[
\mathcal H=\{M_a\cap M_b:a,b\in\mathcal A,\ a\ne b\}
\]

be the collection of **distinct** two-observation collision masks, where \(\mathcal A\) indexes the 425 distinct masks. Both classes have exactly 48,792 distinct elements of \(\mathcal H\), and zero is absent.

A separating four-observation set exists **if and only if** two elements of \(\mathcal H\) are disjoint. The forward direction splits its four masks into two pairs. Conversely, two disjoint pair intersections yield a separating set of at most four original observations, regardless of whether any indices overlap. This equivalence is exact and requires no independence assumption.

### Exhaustive lower-bound certificate

In both classes, the verification program constructs all 48,792 distinct two-observation collision masks from the frozen integer terminal-cost values. For each profile-pair bit \(e\in E\), it builds an integer incidence bitset containing exactly the indices of the two-observation masks that retain collision \(e\).

For every \(H\in\mathcal H\), it computes

\[
F(H)=\bigcup_{e\in H}\{J\in\mathcal H:e\in J\}.
\]

It checks the exact identity \(F(H)=\mathcal H\) for **each** of the 48,792 masks. Thus every pair \(H,J\in\mathcal H\) intersects. By the lemma no four observations separate all profiles. Any smaller separating family could be extended to four observations (425 distinct masks are available), so the lower bound is five.

All operations are integer comparisons, arbitrary-precision integer bitwise operations and exact finite loops. The verifier also independently retains EC49FOX's full enumeration of all 12,704,100 triples of unique masks, and reconstructs the original root-domain census and terminal profiles from the frozen source.

### Five-observation upper-bound witnesses

The following zero-based indices refer to EC49FOX's lexicographically ordered Cartesian product of legal named-root assignments for the optional demands:

| Class representative | Optional demand labels | Five complete allocation indices |
|---|---|---|
| 14304 | `[7,11,13,15,17,19,21]` | **[78,99,226,2,63]** |
| 14309 | `[5,11,13,15,17,19,21]` | **[119,153,237,6,135]** |

For 14304 the five corresponding named-root vectors are `[06,05,07,05,03,07,03]`, `[06,05,07,07,07,03,03]`, `[07,05,06,03,07,03,06]`, `[06,05,06,03,03,03,07]`, and `[06,05,07,03,07,03,03]`.

For 14309 the vectors are `[05,07,06,03,06,03,07]`, `[05,07,06,07,07,03,03]`, `[07,05,06,03,07,05,03]`, `[05,05,06,03,03,07,03]`, and `[05,07,06,07,03,03,03]`.

For each class, exact integer intersection of the five corresponding \(M_a\) masks is zero; every pair of different rooted profiles is therefore separated by at least one selected terminal cost. Together with the lower-bound certificate, this proves FOY-1.

## Reproduction and provenance

The accompanying `verify_ec49foy_exact_five_observers_20261115.py` expands the previously verified EC49FOX Python checker. It additionally enumerates all pair intersections and tests the exact pair-of-pairs obstruction. The full self-contained source input and native C++17 Trie extractor are in the earlier conversation archive `EC49FOX_FOUR_75_CLASSES_EVIDENCE_20261115.tar.xz`, SHA-256 `af3042c100abdb2a53b3df969dc314551e138e0b823f02827afc9f597036f637`; the archive contains the `EC49FOX_EVIDENCE/` root directory, two class-profile CSVs and checksum manifests.

Example after extracting the evidence archive:

```bash
python verify_ec49foy_exact_five_observers_20261115.py EC49FOX_EVIDENCE
```

The additional independent local verifier `EC49FOY_verify.py` (included in this run's evidence bundle) reconstructs these two classes from the same SHA-256 pinned frozen input and checks both exact minima. Original EC49FOX verification of the full four classes was rerun in this research turn.

The result is a **finite exact cardinality theorem for two frozen native BRC classes**. It completes the previous `4 <= m <= 5` interval without changing any root-cost semantics, the input pin, previous nonzero gauge witnesses, or P000.

## Continuation

The finite 625-domain census stands at the last verified 551 fully classified classes, leaving 74 known research targets at the EC49FOX frontier. Continue selecting unclassified classes for exact native-cost comparisons; search particularly for subset-dependent cross-root gauge perturbations invisible to all complete assignments, and study sparse observer lower bounds or structural certificates beyond these two classes.

This is independent portable research evidence only; the exact `RS-EC49AS` topic previously lacked an immutable task-publication directory. Formal Task/CLAIM/Result and independent mathematical review follow their distinct current controls.
