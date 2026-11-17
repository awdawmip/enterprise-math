# R749STY — Sharp Boolean source-guard quotient with lifetime POP

**Date:** 2026-11-18 (+08:00). **Strength:** AUTHOR_EXACT_NOT_REVIEWED. **Mode:** independent portable TASK_RESEARCH, no shared Task CLAIM or native physical-event admission.

**Continuation:** R749STX, immutable Source commit \`3945736c7aa06f0b9e81d45fee5f3f241fc09f94\`; R749STW, commit \`2f0f17bcf0709b6f6b3bc8eeffff856a13999528\`. **Frozen scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. No P000, ACTIVE-worldview, source or task repinning occurs.

## 1. A smaller guard, not a full label window

Retain the P000 six signed spatial axes and separately typed time, the raw X6 Cell torsor with a chosen Cell anchor, and five distinct named sources \`A,B,C,D,E\` with scalar weights \`(1,1,2,3,6)\`. In the same **restricted path-formal adapter** used in R749STW/R749STX, source \`i\` denotes a composite path step along raw native axis \`+e_i\` (\`i=1,...,5\`). The sixth raw coordinate is fixed to chart-relative zero in this adapter, not removed from the six-dimensional ontology. This does not assert an admissible triadic physical event or native heartbeat evolution.

Fix the exact inventory \`n=(n_A,...,n_E)\`, word length \`ell=sum(n_i)\`, and population \`W(n)\` of all ordered source words with inventory \`n\`. They have one common raw terminal X6 Cell and scalar total, but generally different provenance. Fix the Boolean source partition \`G={A,B}\` and \`G^c={C,D,E}\`. The theorem holds verbatim for any fixed nonempty proper subset \`G\` of the five named sources.

Allowed formal operations are:

* \`APPEND_i\`: append a publicly selected named label \`i\`;
* \`POP\`: if nonempty, remove and **output the full named last label**; at most \`r\` POP calls are permitted over the entire adaptive experiment (no resource reset, cloned states, or parallel copies);
* \`GUARD_G\`: read only the one-bit answer \`1_{last label in G}\` without mutation; an empty word has its own declared sentinel and legality/length observable.

Each step also permits terminal raw X6 Cell, length, scalar, remaining POP budget and legality observations. \`GUARD_G\` is a hypothetical source-sensitive **Boolean** Port guard and is *not* claimed to belong to any already licensed native Cell/Link/Port event. It is deliberately weaker than R749STX's full \`PEEK_1\` source-label observation.

## 2. Exact theorem

Let \`s=min(r,ell)\` and let \`rev_s(w)\` denote the final \`s\` source labels in the **order emitted by successive POPs**. For \`r<ell\` set

\[
\sigma_{r,G}(w)=\bigl(\mathrm{rev}_r(w),\,1_{\{w_{\ell-r}\in G\}}\bigr),
\]

where word positions are 1-based. If \`r>=ell\`, set \(\sigma_{r,G}(w)=\mathrm{rev}_{\ell}(w)\), with no further guard symbol.

**Theorem A (future-observer equivalence).** For \`w,v in W(n)\` the following are equivalent:

1. Their outputs and operation legalities agree for **every** finite adaptive future experiment built from the allowed APPEND, POP and GUARD operations with lifetime POP budget \`r\`.
2. Their signatures \(\sigma_{r,G}(w)\) and \(\sigma_{r,G}(v)\) agree.

Thus a one-bit guard at arbitrary future times exposes at most one further *color* beyond the \`r\` fully named POP labels, rather than a whole extra named label.

**Proof of necessity.** POP repeatedly \`s\` times and inspect each output. If \`s=ell\`, the entire original word has been reconstructed. Otherwise perform \`r\` POPs and invoke \`GUARD_G\` on the next untouched original last label. Any unequal signature yields a legal finite experiment distinguishing the words.

**Proof of sufficiency.** Couple any two equal-signature histories under the same adaptive actions. All public APPEND choices coincide until a difference in output, so appended labels and their order coincide. Each POP removes either one of these identical appended labels or an original label. At most \`r\` original labels can be removed over the entire experiment; all such named labels belong to the stored common suffix. Every \`GUARD_G\` call can inspect only an appended label, a stored common original suffix label, or (after all \`r\` original removals) the single original boundary label at depth \`r+1\`; at that boundary the two GUARD bits agree by the signature. An action cannot expose a deeper original label, because it would need at least \`r+1\` POP calls. Endpoint, scalar, length, budget and legality also agree by inventory, public appends and identical removed letters. This inductively proves the same outputs and next adaptive choices for every experiment. QED.

## 3. Sharp class count and optimal codec

For a feasible \`r\`-letter suffix \`u\` with inventory \`a(u)\`, put \`c=n-a(u)\`. Write

\[
z_G(c)= 1_{\{\sum_{i\in G}c_i>0\}}+
         1_{\{\sum_{i\notin G}c_i>0\}}.
\]

For \`0<=r<ell\`, the exact number of distinguishable future-observation classes is

\[
\boxed{
M_{r,G}(n)=
\sum_{\substack{u\in\{A,\ldots,E\}^{r}\\a(u)\le n}}
 z_G(n-a(u))
=
\sum_{\substack{0\le a_i\le n_i\\\sum_i a_i=r}}
 \frac{r!}{\prod_i a_i!}\,z_G(n-a).
}
\]

For \`r>=ell\`, it is \(M_{r,G}(n)=\ell!/\prod_i n_i!\). In particular, the empty history has one class.

For every suffix \`u\`, each color for which at least one original label remains can occur immediately before \`u\`. Exactly one or two color classes therefore lie over \`u\`, giving the formula. The optimal additional fixed-width memory, with exact inventory/terminal X6 Cell known, is

\[
\boxed{b_{r,G}(n)=\lceil \log_2 M_{r,G}(n)\rceil.}
\]

The lower bound follows by pigeonhole over the distinguishable classes. To attain it, rank pairs \`(rev_r(u),color)\` lexicographically among feasible signatures. Define a subtree count on residual inventory \`c\`:

\[
T(c,0)=\begin{cases} z_G(c)&\sum c_i>0,\\1&\sum c_i=0,\end{cases}
\quad
T(c,k)=\sum_{i:c_i>0}T(c-e_i,k-1).
\]

Scanning POP outputs from right to left, skip preceding branches using \`T(c-e_i,k-1)\`, then rank the terminal available Boolean color. Unranking uses the inverse selection. This is an explicit bijection with \([0,M_{r,G}(n)-1]\) and meets the bit lower bound for all nonnegative inventories and budgets.

## 4. Exact comparison to R749STW and R749STX

Let \`N_s(n)\` denote the number of distinct feasible named suffixes of length \`s\` as in R749STW. For every \`r\`:

\[
\boxed{
N_{\min(r,\ell)}(n)\ \le\ M_{r,G}(n)\
 \le\ \min\!\bigl(2N_{\min(r,\ell)}(n),
 N_{\min(r+1,\ell)}(n)\bigr).
}
\]

Consequently the Boolean guard costs **at most one extra fixed-width bit** beyond the POP-only optimum:

\[
0\le b_{r,G}(n)-\lceil\log_2N_{\min(r,\ell)}(n)\rceil\le1.
\]

The first inequality follows because the POP trace remains visible. The factor-two inequality follows from the two Boolean colors over each suffix. A full named \`PEEK_1\` identifies the actual next source and refines the Boolean guard's partition, giving the third inequality.

For \`r<ell\`, \`M_r>N_r\` precisely when some feasible \`r\`-suffix leaves at least one source in each guard color. Equality \`M_r=N_{r+1}\` precisely when each feasible residual inventory has at most one distinct source type present *within each color class*. These are exact criteria, not generic statements about native operations.

An exact two-word witness is \`AC\` versus \`CA\`, with \`G={A,B}\`, \`r=0\`. The terminal raw X6 Cell and total scalar are identical, and POP-only sees one class; GUARD sees different last-source colors and hence two classes. By contrast, \`AB\` versus \`BA\` is **not** separated by this particular guard at \`r=0\`, since A and B deliberately share one color; a full \`PEEK_1\` would separate them. This demonstrates the genuine intermediate quotient between endpoint-only and full-name provenance.

## 5. Reproducible exact verification

The accompanying \`R749STY_BOOLEAN_GUARD_PORT_CERT.py\` uses integer-only Python, with no external package. An actual local execution returned \`PASS\`. It exhausts all \`5^ell\` five-source words for \`ell=0,...,7\`: **97,656 word instances**, **792 inventory fibers**, **3,876 inventory/resource cases**, and **488,086 rank/unrank checks**. Budgets are \`r=0,...,min(4,ell)\`; an independent trace oracle records the GUARD result before and after every available POP (with no APPEND). It checks equality of these trace partitions against the theorem signatures, the exact feasible-suffix count, the dynamic-programming count, the POP-only and full-PEEK bounds, and contiguous bijective rank ranges. Exact larger-inventory examples are computed by recursion, not exhaustive word enumeration.

\`n=(2,1,1,1,1)\`: at \`r=1\`, POP-only has 5 classes, Boolean guard has 10 (4 bits), full PEEK+POP has 21 (5 bits); at \`r=3\` the counts are 72, 135 (8 bits), 192 respectively.

\`n=(2,2,2,2,2)\`: at \`r=2\`, the counts are 25, 50 (6 bits), 120 respectively; at \`r=4\`, they are 540, 1074 (11 bits), 2220 respectively.

This is finite regression evidence only: the unbounded-length and arbitrary APPEND-interleaving theorem relies on the exact argument in Sections 2–4, not on the finite test. No formal independent review, native physical operation, heartbeat timing, signed-amplitude cancellation, Source Result/Review, or shared CLAIM is asserted.

## 6. Native Port transfer boundary and next question

WBRC-T31 licenses finite positive-rational contexts that connect and modify **visible port/external states only**. It does not permit direct reads of hidden internal provenance. Therefore a \`GUARD_G\` which inspects a hidden source label is outside that existing Port lease; neither WBRC-T31 nor R749STX makes it native by naming it "Port." To use this quotient in a real native context, one must first exhibit a genuinely admitted visible guard (or lift the required provenance/color into a declared visible port state), verify the actual triadic/resource/causal predicates, and prove action/output descent on the proposed quotient. WBRC-T31 remains valid inside its original positive-total-mass observer.

**Next discriminating question:** Take one actual licensed native Cell/Link/Port event with an explicit Boolean resource/phase/source-sensitive guard, compute the finite-state observer automaton (including time, branch and guard legality), and determine whether its true minimal future-stable residual fits this one-bit extension, requires multi-symbol memory, or is not finite-state. Do not identify the current toy Boolean guard with a native event before this test.

Sources: R749STW@2f0f17bc; R749STX@3945736c; frozen scientific pin@a72226e; \`definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md\` (WBRC-T30..T32), \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`, current P000 and ACTIVE worldview.
