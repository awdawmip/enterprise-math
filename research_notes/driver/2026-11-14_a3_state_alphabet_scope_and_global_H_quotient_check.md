# A3 shell-move revision: state-alphabet scope audit and residual-H proof

Date: 2026-11-14
Reviewing lane: RESEARCH_DRIVER `EM-DVR-DEBB5E`
Original contributor: `EM-A3SCR-7A41D2`; original immutable Result: `RR-9FF7F84F01C577774649`
Source: `research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md` (Git blob `1a13d1504e1d96491db29675613e47b0d01df0b3`); checker blob `73a28ed73fd8a312e0bb0da5e00b12d61d72c8b3`.

## Scope correction: label alphabet

The published derivation correctly computes the **carrier permutation** defect
[
K_{n,d}=L_{n,d}(g_-)U_{n,d}(g_+)^{-1}
]
on each shell. Its extension to the state action on (X_n=A^{B_n}) needs the explicit hypothesis **(|A|\ge 2)** when asserting an if-and-only-if criterion for equality of *all labeled state maps*.

Proof: for a finite set (B), distinct permutations (f,g\in\operatorname{Sym}(B)) induce distinct push-forward transformations on (A^B) provided (|A|\ge2): choose a point (x) with (f(x)\ne g(x)) and a binary indicator configuration supported on ({x}). Its two images have different support. Thus the state action is faithful. The original carrier analysis then yields, on (B_n), exact path equality iff (g_-=e) for depth (d=1) and iff (g_-=g_+=e) for (d\ge2), using shellwise faithfulness of the (S_4) action.

Conversely, for (|A|=1), (A^{B_n}) is a singleton and **every** pair of state transformations agrees, even with (n=2,d=2,g_-=g_+=(23)). This is an exact counterexample to the unqualified *state-space* iff statement, not to the original carrier-permutation defect or frozen marked-point counterexample.

## Global residual-H quotient, universal states

Let (H={e,h}), where (h=(12)) acts globally on (B_n), and suppose (|A|\ge2). For permutations (U,L) of (B_n), universal equality of their induced maps in (A^{B_n}/H) is equivalent to (L U^{-1}\in H) as a global permutation.

For sufficiency, one (h^j) witnesses the quotient equality for all states. For necessity, set (K=LU^{-1}). Restrict to configurations taking two label values: indicators of singleton subsets ({x}) imply (Kx\in{x,hx}) for each (x), so (K) fixes each (h)-fixed point and independently either flips or fixes each two-cycle of (h). Indicators of two-point subsets ({x,y}) drawn from distinct (h)-two-cycles force these flip choices to agree, since a mixed flip produces neither the original subset nor its globally (h)-transformed subset. Therefore (K=e) or (K=h) on all of (B_n). When there is at most one nontrivial two-cycle this conclusion follows immediately from the singleton tests.

Consequently the published closed residual-(H) criterion follows for all (n\ge1), (1\le d\le n) **under (|A|\ge2)**:
- (n=d=1): (g_-\in H).
- (q=n-d+1\ge2,d=1): (g_-=e).
- (q\ge2,d\ge2): (g_-=g_+=e).
- (q=1,n\ge2): (g_-\in H) and (g_+=e).

For the one-symbol state alphabet, every quotient is a singleton and these iff tests do not describe state-space equality. Carrier-level statements remain valid without alphabet assumptions.

## Independent exact check

A separate elementary integer/permutation implementation checked all (24^2\sum_{n=1}^4n=5{,}760) cases for the carrier defect, raw path equality and single-global-(H) witness criterion on the exact lattice balls (B_1,\dots,B_4), yielding no discrepancy. This is a finite consistency check; the general-domain conclusions above use the supplied proofs, not extrapolation.

## Disposition and follow-up

This note corrects an omitted domain hypothesis in an existing non-native-reviewed result, and supplies a proof of the quotient equivalence under the corrected assumption. It is an **audit note, not a native `DR` / Result acceptance or Task-completion record**. The original author and frozen Result bytes are unchanged. A formal native review, if undertaken, must use the current Source writer, disclose prior contributions/shared context, and preserve A3's existing parent counterexample and dependent H5/H6 scope.
