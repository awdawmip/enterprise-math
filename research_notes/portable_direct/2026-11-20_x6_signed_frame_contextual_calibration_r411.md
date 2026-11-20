# X6 r411 — Exact suffix-context separation and minimal six-axis frame calibration

Date: 2026-11-20. Scope: finite group action on ordered signed primitive *word syntax*, not a primitive physical rotation/triadic event law. Status: Driver-context new analytic lemma, author-side proof, **NOT_INDEPENDENTLY_REVIEWED / NOT_NATIVE_RESULT_ADMITTED**.

## Exact sources and provenance

- Current immutable Task: \`RS-X6-NATIVE-ROTATION-DYNAMICS\`, publication \`TP2-6A1F9D8C2047E3B51C01\`. Original research identities and author contributions \`EM-EMF6D046-5A2844\`, \`EM-X6-DFD1FD\` are retained. Current Driver author of this *new auxiliary deduction* is \`EM-DVR-DEBB5E\`. The published native claims, parent objective and owners are not modified by this note.
- Original Source-published static-word orbit classification and non-congruence witness: \`awdawmip/enterprise-math@9d09f6bc13b36a8d47d11b524fae4dd5254ac333:research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-c618a61189764f23846a391a08518a1a/0f0e002ae5e625394259/X6_SIGNED_WORD_ORBIT_SPLITTING_AND_CONCATENATION_20261116.md\`. This existing result gives the group, its signed-letter action, the Stirling/Burnside word-orbit counts and the elementary failure of independent orbit concatenation.
- Existing Driver finite-depth endpoint/rotation observer result: \`awdawmip/enterprise-math@cc0d2f61bbf5516bd06f32c2714d2b2a7e0cc986:research_notes/driver/2026-11-12_x6_finite_depth_signed_brc_cover_rotation_descent_and_minimum_memory.md\`. Its endpoint-depth memory is a distinct observation problem.
- P000: six native signed primitive spatial axes, ordered provenance and triadic closure retained as scope boundaries. No existing static-word action is identified here with P000 physical dynamics.

## General group-action theorem: suffix calibration detects pointwise stabilizers

Let a finite group \`G\` act *faithfully* on a finite alphabet \`Sigma\`. Let it act on the free monoid \`Sigma^*\` letterwise, by the **same single** group element on all positions. For any fixed finite suffix \`s\`, define the suffix-calibrated orbit observer

\[
F_s:\Sigma^*\to\Sigma^*/G,\qquad F_s(u)=[us]_G.
\]

Then

\[
\boxed{F_s\ \text{is injective}\quad\Longleftrightarrow\quad
\operatorname{Stab}_G(s)=\{1\}},
\]

where the stabilizer fixes **every individual letter position** of the suffix. A suffix with trivial stabilizer is a base word for the action; its least possible length is the base size of the permutation action. This is a statement about a *known, common-frame suffix*, not about independently orbit-compressed suffix input.

**Proof (sufficiency).** Suppose \([us]_G=[vs]_G\). Word-orbit equality means that there exists a single \(g\in G\) with \(g(us)=vs\). Group actions preserve word length, and the last \(|s|\) positions force \(g(s)=s\). A trivial suffix stabilizer forces \(g=1\) and then \(u=v\).

**Proof (necessity).** Suppose \(g\ne1\) fixes \(s\). Faithfulness supplies some letter \(a\in\Sigma\) with \(g(a)\ne a\). The two distinct prefixes \(u=a\), \(v=g(a)\) have equal calibrated observations because \(g(as)=g(a)s=vs\). Hence \(F_s\) is not injective. Both directions are exact for all prefix lengths; no finite computational extrapolation is used. QED.

**Context-equivalence corollary.** Define the right-context closure of whole-word orbit equality by
\[
u\equiv_{\mathrm{right}}v\iff
(\forall s\in\Sigma^*)\ [us]_G=[vs]_G.
\]
Whenever the faithful action has a finite base suffix \(s_*\), the preceding theorem applied to \(s_*\) yields
\[
\boxed{u\equiv_{\mathrm{right}}v\iff u=v.}
\]
In particular, no two distinct ordered prefix words may be identified by a quotient that must retain the entire \(\Sigma^*/G\) **whole-word orbit** for every possible future right-concatenation context. This is the exact syntactic right-contextual obstruction for that specified output, not a general impossibility of enriched states or restricted future operations.

## Exact X6 specialization: six signed axes are necessary and sufficient

Use \(\Sigma=\{\pm e_1,\ldots,\pm e_6\}\), the original faithful signed-letter representation of
\[
H=(C_2)^6\rtimes A_6,\qquad |H|=23040.
\]
A signed word \(s\) has trivial pointwise stabilizer in \(H\) **iff** every one of the six **unsigned** axis labels appears at least once in \(s\).

If unsigned axis \(j\) is absent, the element that flips the sign on \(e_j\) alone, with identity (hence even) axis permutation, is a nonidentity element of \(H\) fixing all positions of \(s\). Conversely, if all six axes appear, fixing every signed letter forces the underlying unsigned permutation to fix each axis and its sign flip to be positive. Therefore only the group identity fixes \(s\).

Hence the **sharp minimal calibration length** is
\[
\boxed{b(H,\Sigma)=6}.
\]
One explicit minimal calibrator is \(s_*=e_1e_2e_3e_4e_5e_6\). For all ordered signed prefixes \(u,v\), of arbitrary finite lengths,
\[
[\,u e_1e_2e_3e_4e_5e_6\,]_H
=[\,v e_1e_2e_3e_4e_5e_6\,]_H
\iff u=v.
\]
Sharpness is witnessed for **every suffix of length \(0,\ldots,5\)**: choose one absent unsigned axis \(j\) and the sign-flip \(g_j\). Then \(u=e_j\), \(v=-e_j\) are distinct but
\[
[\,e_j s\,]_H=[\,-e_j s\,]_H
\]
because \(g_j\) fixes \(s\). This extends the original single concatenation non-congruence witness to a complete stabilizer/base-length classification.

**Application to prefix compression.** Whole-word static signed-frame orbit counting can still be useful at a *completed word* or for a specified family of equivariant queries. For a streaming representation required to reproduce \([us]_H\) for *every unrestricted future signed suffix* \(s\), the minimal congruence refining the orbit relation is literal word equality. A context-sensitive encoding may instead retain the shared frame, relative axis relations, branch, typed future operations, or constrain the suffix language; each such design needs its own observer-safety proof. The theorem supplies no bound on the optimal bit length of a lossless compressed code for whole words and is not a physical rotation claim.

## Verification boundary and portfolio conclusion

All statements follow deductively from the exact group action and faithful six-axis alphabet, with explicit witnesses for every shorter suffix. No extra axiom, computational checker, Source RUN or native physical admissibility is assumed.

New reviewable subunit: the general stabilizer iff injectivity theorem; the X6 exact six-axis calibration/base size; and the full right-context collapse. This closes the **static unrestricted suffix-orbit observation subquestion only**. The original X6 Task's native rotation, Cell/time updates, triadic event legality and physical path-fiber composition remain OPEN. This note is an author-side mathematical source; no independent Native Review, accepted Result, Task DONE, Objective closure, Source Activity link or live CLAIM is asserted.

Independent-review focus: verify the *same common group element* quantifier in the whole-word orbit observer, the faithful signed representation, and the unsigned-axis sign-flip stabilizer argument. A future native model must specify admissible event/suffix languages and its observer before importing this barrier.