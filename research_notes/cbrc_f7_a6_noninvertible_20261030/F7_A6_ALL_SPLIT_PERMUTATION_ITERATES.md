# F7 A6 — All 16 balanced channel permutations: conservation, growth and compulsory loss of iterated balance

**Provenance:** AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / NOT_INDEPENDENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
This is an exact auxiliary-model deduction on the already open F7 A6 Draft PR. It is not an independent Driver review, a native Result, a new V2 Task or a change to the frozen reversible F7 GL4(Z) no-go theorem. The mathematical carrier is the F6 auxiliary pair, not a native 2D plane or a complete X6/slice dynamics.

**Frozen source:** Task RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION; Result RR-AA38973D56330E59D315 (Git blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472), return blob 69265a0fadfd9fcd0be9354ff74f33e5e825fe84. This supplement consumes the existing exact A6 fixed-scalar family; it does not silently admit those author-side results.

## Theorem (all balanced split permutations, all nonzero integer multipliers)

Write the free part of the pair as Z^4 in slot order (n_1,m_1,n_2,m_2); the torsion part is (Z/3)^2. Put

\[
C=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
D=\operatorname{diag}(C,C),\quad D^2=2I_4.
\]

For each free pair, let its fixed four-channel scalar be

\[
Q(w)=\frac12\#\{j\in\{0,1,2,3\}:(Dw)_j\ne0\},
\]

so Q(w) equals the sum of the original two slot scalars q. Fix a permutation p of channels {0,1,2,3} and its permutation matrix P with P e_i=e_{p(i)}. Let K=diag(k_0,k_1,k_2,k_3) for **arbitrary nonzero integers** k_i; set B=PK and A=DBD. The marked input is e_0=(1,0,0,0), with D e_0=e_0+e_1.

Assume exactly the original one-step marked balance: the two channels p(0),p(1) occupy different output slots {0,1} and {2,3}.

**(1) Complete finite classification.** There are exactly **16** such permutations. They have the following cycles of marked balance (indices n modulo the permutation order, U = unbalanced, B = balanced):

| Permutation order | Number | Balance cycle for n=0,1,... | First unbalanced positive iterate after n=1 |
| ---: | ---: | :--- | ---: |
| 2 | 4 | UB | 2 |
| 3 | 8 | UBB | 3 |
| 4 | 4 | UBUB | 2 |

Thus every such endomorphism has an iterate 2 <= n <= 3 that **fails** the original 1/2 + 1/2 marked balance and A0, even though it conserves Q for all inputs at *every* iterate. The original witness is among the eight order-three cases.

**(2) All-power identity and coarse conservation.** For every integer n>=0,

\[
D A^n=2^n B^n D,\qquad Q(A^n w)=Q(w)\quad\forall w\in\mathbf Z^4.
\]

This is true even when |k_i|>1 and B is not of finite order: its powers remain nonzero-weight monomial matrices. In particular A is injective, and

\[
[\mathbf Z^4:A^n\mathbf Z^4]
=|\det A|^n
=\big(16\prod_i |k_i|\big)^n.
\]

For the full free-plus-torsion carrier, let the torsion block be any automorphism of (Z/3)^2, and allow an arbitrary additive free-to-torsion coupling. The same scalar/conservation/balance conclusions hold. The torsion block contributes no cokernel, so the full iterate has a cokernel naturally isomorphic to Z^4/A^n Z^4 after forgetting the torsion coordinate.

**(3) Exact marked-slot formula.** If S={0,1}, then the two individual slot scalar values of A^n e_0 are

\[
\Big(\tfrac12\,|p^n(S)\cap\{0,1\}|,\;\tfrac12\,|p^n(S)\cap\{2,3\}|\Big).
\]

They depend **only on the permutation**, not on k_i or the torsion extension. Hence balance holds iff p^n(S) is a transversal of the two slot-channel pairs. When balance fails, one slot has scalar zero, hence zero old/free projection, violating the marked A0 condition. This provides a strict semigroup-composition boundary: global scalar conservation survives composition, marked elementary balance does not.

## Proof and validation boundary

D^2=2I implies DA=2BD and inductively DA^n=2^n B^n D. Every power of the nonzero-weight monomial matrix B permutes and scales channel coordinates by nonzero integers; it preserves their zero pattern, proving Q conservation and the marked-slot formula. Since det D=4, det A=(det D)^2 det(P) det(K)=16 sgn(p) prod(k_i); nonzero determinant proves injectivity, and the lattice image index is its absolute determinant. For the torsion extension, invertibility of the torsion block allows every torsion component in the quotient to be eliminated; projection to the free cokernel is then an isomorphism.

For the finite classification, precisely one of the two initially active channels must go to each output pair. There are 2*2*2*2=16 choices. Exactly four are cross-slot transpositions (order two), eight are three-cycles (order three), and four are four-cycles (order four); identity and double transpositions never split the marked pair. The displayed balance cycles are verified for the **entire** 16-permutation finite set, not inferred from random numerical samples; this finite exhaustive enumeration is supplied by the standard-library checker below. Its algebraic identity/index checks for bounded multiplier tuples are regression tests only, not the universal proof.

## Reproducible evidence

The companion verify_f7_a6_split_cycle.py exhausts all 24 channel permutations and selects all 16 split cases; checks 256 nonzero multiplier 4-tuples from {-2,-1,1,2} for each selected permutation, determinant and seven matrix-power identities, and 27,216 sample scalar-conservation cases with nonunit/negative multipliers. Expected exact output in VERIFY_SPLIT_CYCLE_EVIDENCE.json:

- selected split permutations: 16;
- profile counts: order 2 -> 4, order 3 -> 8, order 4 -> 4;
- matrix-power identity checks: 28,672;
- scalar regression cases: 27,216;
- verdict: ALL_PASS.

**Non-claims:** no classification for arbitrary scalar functions, no reversible F7 witness, no independence, no native X6/three-dimensional-slice transfer, no physical conservation or irreversibility law, no review/reference/synthesis/follow-up, and no new published Task. Next admissible formal step remains current-authority, contribution-independent Driver review of the exact frozen Result and its existing review set.
