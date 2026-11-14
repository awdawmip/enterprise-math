# A3 shell-move revision: state-alphabet scope audit and residual-H proof

Date: 2026-11-14
Reviewing lane: RESEARCH_DRIVER EM-DVR-DEBB5E
Original contributor: EM-A3SCR-7A41D2; immutable Result: RR-9FF7F84F01C577774649
Source: research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md (Git blob 1a13d1504e1d96491db29675613e47b0d01df0b3); checker blob 73a28ed73fd8a312e0bb0da5e00b12d61d72c8b3.

## Prior-art reconciliation and distinct contribution

**Prior result already exists.** The alphabet-size counterexample, binary-indicator quantifier bridge, and shell-faithfulness qualification were proved and saved in [2026-11-13 A3 theorem-domain audit](2026-11-13_a3_state_space_faithfulness_boundary_independent_audit.md), before this note. The distinction between *output-orbit comparison* and operators well-defined on a quotient, including the necessary centralizer test, was proved in [2026-11-13 residual-H quotient audit](2026-11-13_a3_residual_h_quotient_descent_normalizer_audit.md). Further exact all-scale orbit tests and an explicit single-input binary witness are in [2026-11-13 one-input theorem](2026-11-13_a3_universal_one_binary_input_orbit_naturality.md). This note is an **independent arithmetic recheck and provenance/source-currentness reconciliation of already saved mathematics**, not an additional novel theorem and not a second independent Driver reviewer.

The statement below concerns the two composites **as maps from labeled states to quotient output orbits**. To assert individual partial moves are well-defined maps on \(X_n/H\), additionally require \(g\in C_{S_4}((12))=\{e,(12),(34),(12)(34)\}\) for the relevant active scale, as proved in the linked 2026-11-13 quotient audit. The general shell-label naturality iff needs faithful shell actions; without faithfulness it is an iff of **induced operators**, not abstract group labels.

The new operational observation in this 2026-11-14 pass is that previously blocked original RR-9FF7F84F01C577774649 is now present on canonical \`main\` byte-for-byte (blob eb82ac58be5ceaecae07240edb5b4258c72fa3d6; integration commit 2e86304a5daf6f25d199f5f7e1e06b724f8c8d7d). This was linked to [control issue #1505](https://github.com/awdawmip/enterprise-math/issues/1505#issuecomment-6869076358). Native reducer review admission still requires its own fresh success receipt.

## Scope correction: label alphabet

The published derivation computes the exact **carrier-permutation defect**

\[
K_{n,d}=L_{n,d}(g_-)U_{n,d}(g_+)^{-1}
\]

on every shell. Transferring its iff classification to **equality of all labeled-state maps** on \(X_n=A^{B_n}\) requires the explicit hypothesis \(|A|\ge2\).

**Proof.** For a finite set \(B\), distinct permutations \(f,g\in\operatorname{Sym}(B)\) induce distinct push-forward maps on \(A^B\) if \(|A|\ge2\): take \(x\) with \(f(x)\ne g(x)\), and a two-label indicator of \(\{x\}\); the images have distinct singleton supports. The state action is therefore faithful. Since the original \(S_4\)-action on each \(S_r\), \(r\ge1\), is faithful, equality of all state maps is equivalent to \(K_{n,d}=e\): for \(d=1\) exactly \(g_-=e\); for \(d\ge2\) exactly \(g_-=g_+=e\).

For \(|A|=1\), the state space \(A^{B_n}\) is a singleton. Every pair of state transformations agrees, including \(n=2,d=2,g_-=g_+=(23)\). This refutes the unqualified *state-space iff* as written, while leaving the original carrier-permutation defect and frozen marked-point counterexample valid.

## Universal global residual-H quotient

Let \(H=\{e,h\}\), with \(h=(12)\) acting globally on \(B_n\), and \(|A|\ge2\). For carrier permutations \(U,L\), universal equality of their induced maps in \(A^{B_n}/H\) holds **iff** \(LU^{-1}\in H\) as a single global permutation.

Sufficiency is immediate. For necessity, write \(K=LU^{-1}\) and restrict the universal statement to two-label indicators. Indicators of singleton subsets \(\{x\}\) force \(Kx\in\{x,hx\}\), so \(K\) fixes each \(h\)-fixed point and acts independently on each two-cycle of \(h\) by either a flip or the identity. For two distinct nontrivial \(h\)-orbits choose \(x,y\) in different two-cycles. The indicator of \(\{x,y\}\) rules out a mixed flip: its image would equal neither \(\{x,y\}\) nor \(h\{x,y\}\). All two-cycles therefore share one flip choice, yielding \(K=e\) or \(K=h\) globally. With at most one two-cycle, the singleton tests already yield the conclusion.

Hence, for the present radius-preserving \(S_4\)-carrier and \(|A|\ge2\), the published global quotient criterion holds for all \(n\ge1\), \(1\le d\le n\):

- \(n=d=1\): \(g_-\in H\).
- \(q=n-d+1\ge2,d=1\): \(g_-=e\).
- \(q\ge2,d\ge2\): \(g_-=g_+=e\).
- \(q=1,n\ge2\): \(g_-\in H,\ g_+=e\).

If \(|A|=1\), all state-space quotient maps agree. The carrier-level results remain unchanged.

## Independent exact verification

A separately implemented exact integer/permutation check inspected \(24^2\sum_{n=1}^4 n=5{,}760\) cases across all \(g_-,g_+\in S_4\), \(1\le d\le n\le4\) for the shellwise defect, equality of carrier maps, and equality with one global \(H\)-witness. All cases agreed with the corrected formulas. This finite census checks formulas in its stated range; the statements for arbitrary \(n\) follow from the proofs above.

## Attribution, status, follow-up

The original author and frozen Result are retained. This independently implemented check and proof are an **audit note, not a native DR / Result acceptance or Task completion**. The reviewing lane has shared ambient project context; this note does not claim blind independence. Any formal review must preserve the current Source writer, contribution history, the earlier H4 counterexample, and dependent H5/H6 observer limits.
