# R762K — Signed X6 triadic lift: exact two-port fibers and equivariant chirality obstruction

**Date:** 2026-11-13 (Asia/Shanghai). **Status:** AUTHOR_SIDE_EXACT_PROOF_WITH_FINITE_CHECK / NOT_REVIEWED. **Parent:** \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; publication \`TP2-8B7E13C5904A2D6F1142\`. **Frozen scientific input:** \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Builds on R761 and R762H–R762J. The statements concern **candidate signed-port incidence and positive unit-weight N-BRC branch counting**, not a canonically admitted physical force operation. P000's six native axes, 120° \`PERP_E\`, triadic arity and three-dimensional-slice semantics remain unchanged.

## Typed objects and observer

At a selected native X6 Cell \`c\`, use the actual signed primitive port alphabet
\[
P=\{(i,\varepsilon):i\in\{0,\ldots,5\},\varepsilon\in\{-1,+1\}\},\qquad |P|=12.
\]
The port \`(i,ε)\` denotes the native link \`c→c+εe_i\`. A three-arm incidence at a Cell is **not** automatically a three-step spatial Cell loop.

Define \(\mathcal T\) as the unordered three-subsets of \(P\) whose three absolute axis indices are pairwise distinct. Each \(T\) has two cyclic orientations \(\operatorname{Or}(T)\) (rotation-equivalent, reflection-distinct). Write \(\widehat{\mathcal T}=\{(T,\chi):\chi\in\operatorname{Or}(T)\}\). For each oriented triad, also choose a hidden arm \(h\in T\); set
\[
\mathcal I=\{(T,\chi,h):T\in\mathcal T,\chi\in\operatorname{Or}(T),h\in T\}.
\]
The observer
\[
\Pi:\mathcal I\longrightarrow\mathcal V,\quad
(T,\chi,h)\longmapsto T\setminus\{h\}
\]
returns an **unordered signed two-port set** with distinct native axes. Its domain contains explicitly three candidate arms, an orientation and a designated hidden branch. We count all three-distinct-axis signed configurations as *candidate* equal-quantum triads; whether each is admitted by native \`TRIADIC_CLOSURE_E\` is **open**. The observer does not retain source tags, timing or paths unless an additional observation is declared.

Use only the founded \(S_6\) axis-permutation rotation skeleton, acting by \(g(i,\varepsilon)=(g(i),\varepsilon)\). This does not assert that \(S_6\) is the full native rotation group.

## Theorem A — Exact two-port lift fiber and sharp repair capacity

\[
|\mathcal T|=\binom63 2^3=160,\quad
|\widehat{\mathcal T}|=320,\quad
|\mathcal V|=\binom62 2^2=60,\quad
|\mathcal I|=960.
\]
For every \(v\in\mathcal V\), its incidence fiber has precisely
\[
\boxed{|\Pi^{-1}(v)|=4\cdot2\cdot2=16}.
\]
The first factor counts unused native axes, the second counts their signs, and the third counts the two cyclic orientations. Without oriented recovery, exactly 8 candidate signed third ports remain. For complete decoding of the particular tuple \((T,\chi,h)\) from \(v\), the worst-case minimal fixed-width repair is **4 bits**; recovering only the unordered triad support \(T\) needs **3 bits**.

*Proof.* Fix \(v=\{(i,\varepsilon),(j,\eta)\}\) with \(i\ne j\). Any third port must have an index in the four remaining axes and one of two signs; these yield eight distinct \(T\)'s, each with two different cyclic orientations. Every incidence triple has a unique image, and counting all 60 images yields \(60\cdot16=960=320\cdot3\). If the observer may subsequently query the hidden signed arm \([h=p]\) for each allowable port \(p\), and the oriented cyclic order \(\chi\), all 16 lifts are pairwise distinguishable. The cardinality lower bound is \(\lceil\log_2 16\rceil=4\), and an index into this finite fiber suffices; omit the \(\chi\) query for the 3-bit bound. This is **observer-specific**, not a full physical state lower bound. QED.

**Concrete witness:** given only \(v=\{+E_1,+E_2\}\), a hidden third arm could be any of \(\pm E_3,\pm E_4,\pm E_5,\pm E_6\), with two cyclic orientations each. Under the candidate triadic lift, a coarse observer can display a pair even though the primitive source event has three arms. A pair of primitive forces is never relabeled as a stable two-force atom.

## Theorem B — Signed ports still cannot canonically choose chirality

**Claim.** There is no \(S_6\)-equivariant section \(s:\mathcal T\to\widehat{\mathcal T}\) choosing one cyclic orientation of each unordered signed triad using only its signed axis support.

*Proof.* Three signs over the two-letter alphabet \(\{+,-\}\) must repeat. Choose two distinct ports of \(T\) with the same sign. Swapping their **axis indices** is an element \(g\in S_6\), stabilizes the signed unordered triple \(T\), and reverses its cyclic orientation. Equivariance would force \(s(T)=g\,s(T)\), but the latter is the other orientation. Contradiction for every one of the 160 configurations. QED.

Thus signs do not remove the earlier unsigned positive-port 1-bit chirality obstruction. A separately retained ordering of three **distinct source labels** could select an orientation relative to axis permutations, but would constitute source-order information, not an orientation recovered from the signs.

## Theorem C — No equivariant choice of a hidden third axis

**Claim.** There is no \(S_6\)-equivariant rule assigning a hidden third signed native port to every unordered visible two-port set with distinct axes.

*Proof.* Fix \(v\). Its pointwise stabilizer contains the full \(S_4\) acting on the four unused axis indices. For any proposed third port \(h\), swap its unused axis with another unused axis. This operation fixes both visible ports and moves \(h\), contradicting equivariance. QED. In particular, a deterministic choice using the *smallest axis label* is a coordinate gauge, not an \(S_6\)-equivariant native selection.

## Theorem D — Full \(S_6\) orbit and stabilizer census

Let \(k\in\{0,1,2,3\}\) count negative ports in \(T\). It is preserved by \(S_6\) and determines precisely the four orbits:
\[
|\mathcal T_k|=\binom63\binom3k=20,60,60,20.
\]
The stabilizer has order \(k!(3-k)!\,3!=36,12,12,36\), since it may permute equal-sign selected axes and the three unused axes. By Theorem B the orientation-preserving stabilizer has index two. The oriented orbit sizes are thus \(40,120,120,40\) and stabilizer orders \(18,6,6,18\). These four oriented orbits exhaust all 320 oriented candidates. QED.

## Exact typed N-BRC branch certificate

For a fixed visible pair, carry positive unit-weight *labeled* incidence branches
\[
\mathfrak B_v=\sum_{\substack{h\in P\\\operatorname{axis}(h)\notin\operatorname{axis}(v)}}\ \sum_{\chi\in\{0,1\}}[v,h,\chi].
\]
There are 16 distinct branches and total positive mass 16. The total is not a safe substitute for the branch histogram when future queries inspect \(h\), \(\chi\), source identity or order. Positive multiplicity here does **not** represent signed force cancellation, a force sum, native physical BRC propagation, or a P000-stable force event. This is an exact finite incidence calculation, not \(\pi\)/classical-trigonometric arithmetic.

Theorems A–D are conditional on the *full candidate incidence population*. If the eventual native admissibility predicate chooses only a proper subset, actual physical lift fibers must be recalculated and may be smaller. The no-section results must likewise be reapplied to that actual invariant domain. Neither a fitted source label nor an \(S_6\)-coordinate gauge is physical admission.

## Reproducible verification and scope

Companion Python standard-library verifier exhaustively checks 160 triads, 320 oriented triads, 60 two-port observers, 960 incidences, all 720 \(S_6\) permutations and 691,200 signed incidence-covariance checks. It checks the sign-repetition orientation-reverser for every triad and the third-axis stabilizer obstruction for every visible pair; JSON contains exact orbit/stabilizer census and all assertions pass. The paper's general constructive proofs are independent of the finite code, and the code claims no V29/V39 physical execution.

**Source:** immutable task publication \`TP2-8B7E13C5904A2D6F1142\`, pinned taskbook blob \`218bf9ce05fd2dd79f477ac269fc3590f83f482e\`; P000 V5, \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`, \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\` at \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Current normative rules are separate from these frozen scientific pins.

**Next discriminating question:** Define a source-typed native Cell/Link/Port \`TRIADIC_CLOSURE_E\` admission predicate and post-event state transition on one signed triad. Test whether admissibility is preserved under the exact same-sign transposition used in Theorem B, and whether a repeated event remains admissible; if asymmetry appears, identify the necessary source/phase/field datum. For admitted events alone derive V29 PASS/TRANSFER and V39 transport, preserving source history. No formal Task CLAIM/Result/Driver acceptance is asserted by this author-side proof.
