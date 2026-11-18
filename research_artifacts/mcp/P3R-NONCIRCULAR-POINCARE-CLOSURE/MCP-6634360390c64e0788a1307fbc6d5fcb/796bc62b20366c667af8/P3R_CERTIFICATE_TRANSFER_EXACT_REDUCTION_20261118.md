# P3R 精确归约：群平凡性正证书与 3-球识别正证书（2026-11-18）

Task: P3R-NONCIRCULAR-POINCARE-CLOSURE · Researcher: EM-X6-C7A253 · Classification: exact conditional reduction / dependency audit, **not** a proof of Poincaré or a novelty claim.

## Definitions

Let \(\mathcal T\) be the effectively recognizable set of finite triangulations of closed, connected, orientable 3-manifolds. Standard cell-complex methods produce a finite presentation \(P_T=\langle x_1,\ldots,x_m\mid r_1,\ldots,r_k\rangle\) of \(\pi_1(|T|)\).

A **D-certificate** for \(T\) is, for every generator \(x_i\), a finite list of words \(u_{ij}\), relator indices \(\ell_{ij}\), and signs \(\epsilon_{ij}\in\{\pm1\}\) whose free-group reduction verifies
\[
x_i=\prod_{j=1}^{N_i}u_{ij}r_{\ell_{ij}}^{\epsilon_{ij}}u_{ij}^{-1}.
\]
Validity is decidable by free-word reduction; \(D(T)\) exists iff \(\pi_1(|T|)=1\), because the latter condition means precisely that every generator lies in the normal closure of the relators. No a priori bound on certificate length is asserted.

Fix any total, sound and complete algorithm \(R\) recognizing \(S^3\) from finite valid 3-manifold triangulations: \(R(T)\) accepts iff \(|T|\cong S^3\). A **W-certificate** is a finite accepting execution transcript of \(R(T)\), checkable by a finite simulator. Hence \(W(T)\) exists iff \(|T|\cong S^3\). This definition is implementation-neutral; a geometric almost-normal witness is not silently equated with a full accepting trace.

## Theorem A: computable certificate transfer is Poincaré-equivalent

The following are equivalent:

**(PC)** Every \(T\in\mathcal T\) with \(\pi_1(|T|)=1\) satisfies \(|T|\cong S^3\).

**(F)** There is one total computable map \(F(T,D)\) on finite syntactic inputs, outputting a valid W-certificate whenever \(T\in\mathcal T\) and \(D\) is a valid D-certificate; on invalid inputs, \(F\) may output a distinguished error symbol.

*Proof.* Under (F), each simply connected \(T\) has some D (normal-closure characterization); its image is an accepting computation of \(R(T)\), so soundness gives \(|T|\cong S^3\). Conversely assume (PC). Test syntactic validity of \(T,D\) by finite algorithms and output error if invalid. For valid D, the group is trivial and (PC) implies \(|T|\cong S^3\). Run total \(R(T)\), which therefore accepts, and output its finite accepting trace. The procedure halts on every input. QED.

**Interpretation.** Theorem A locates the missing constructive interface precisely: turn verifiable null-homotopy relations of all fundamental-group generators into a 3-sphere recognition witness. The reverse implication in the proof *assumes* (PC); presenting this use of \(R\) as an independent proof would be circular. A genuine new method must construct such a transfer for a specified class with justified premises, without assuming (PC) or equivalent geometrization-strength input.

## Theorem B: certified arithmetic pruning preserves the recognition language

Suppose a fixed finite witness-search recognition implementation \(R_W\) accepts inputs iff at least one valid candidate is found in its finite branch/reconstruction search. For every branch and zero-triangle repair state \((\beta,\tau)\) removed by the BRC filter, assume an exact certificate proves **no accepting candidate belongs to that state**. Require coverage of every repair state capable of representing a valid accepting candidate, and delete a whole branch only if all its relevant states are certified empty. Then the pruned search \(R_W^{\mathrm{prune}}\) accepts **exactly the same input triangulations** as the unpruned search.

*Proof.* Any accepted witness before pruning has an admissible representation in a repair state; that state cannot be removed by a sound emptiness certificate, so it remains searchable and accepted. Conversely pruning creates no witnesses or changes their verifier, hence every accepted input afterward was accepted before. QED.

This theorem is about the accepted **input language**, not equality of execution traces, search order, complexity, or the set of syntactic transcripts. The exact prime-local \(d_{p,\tau}\) row-space test and gcd/Smith descendants from the frozen BRC source instantiate its premises when their rank/gauge/coverage hypotheses are verified. It leaves the D-to-W interface untouched.

## Research consequence and next discriminating unit

The separated interfaces are:

1. finite presentation and a checkable D-certificate of trivial \(\pi_1\);
2. a currently **open**, Poincaré-equivalent D→W construction;
3. a checkable positive 3-sphere recognition W-certificate, optionally accelerated by sound Q/QO arithmetic pruning.

H₁=0 cannot replace D: the Poincaré homology sphere has vanishing first integral homology but nontrivial fundamental group. A tractable next test is to select a rigorously restricted family \(\mathcal C\) of triangulations, construct a D→W transformation for that family, and verify actual outputs against independent classical recognition. Such a result would be a scoped theorem for \(\mathcal C\), not general closure.

## Pinned antecedents

- Enterprise Math frozen corrected frontier: awdawmip/enterprise-math@3359de19ffb776ebfaa59bc7443b171b23d35f4d, research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md.
- Global Knowledge frozen arithmetic observer: awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7, knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md.
- Joachim H. Rubinstein, *An Algorithm to Recognize the 3-Sphere* (ICM); Joel Hass, *What is an Almost Normal Surface* (arXiv:1208.0568); Benjamin A. Burton, *Quadrilateral-octagon coordinates for almost normal surfaces* (arXiv:0904.3041).

Evidence class: hand-checkable logical equivalence under explicit recognizer assumptions; no finite Regina benchmark, formal proof checker, or independent mathematical review in this unit. Existing normal/almost-normal results and BRC modular/gcd lemmas are reused, not re-proved.
