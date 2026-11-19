# OAI116-D: explicit bit-budget for rational formula evaluation and a shared-circuit boundary

Task: `RS-OAI7-116-D-20261007-6F2A81`; author-mode exploratory derivation, not independent review or theorem admission. Source scope: characteristic-zero division-free noncommutative formulae; bit-cost statements below specialize to rational, explicitly binary-encoded scalar leaves.

## Fixed external inputs

- `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `build/formula-systems.tex`, Git blob `8a0db831dd4a7142ece2b935de0ba256ef5e30fc`: acyclic scalar-edge elimination, formula-tree (m\le2s), ordered products (B_w).
- Same commit, `build/construction.tex`, Git blob `0abc841a6a0263f050c93ea926cc6c0cece05e53`: rational generators (T_i), (d=2ns^2), construction bit bound and (m)-state ABP extension.
- Same commit, `build/introduction.tex`, Git blob `bbbfbd3ff0bf7ed812cf20d23734ed9dac4bc4d6`: theorem explicitly distinguishes tuple construction from arbitrary-field oracle evaluation.
- These are external manuscript claims, not project-admitted theorems. The following integer bookkeeping and circuit counterexample are independently derived, conditional only on the displayed generator formula.

## Exact denominator-budget theorem (rational formulas)

Take (n,s\ge1), (ns\ge2), (d=2ns^2), and the lower triangular generators
[
 (T_i)_{rq}={(-1)^{r-q-1}\over r i^{r-q}}quad(0\le q<r<d),\qquad (T_i)_{rq}=0\ (r\le q).
]
Define the explicitly integral common multiplier
[
 M=d!\,(n!)^d.
]
For every nonzero generator entry its denominator (r i^{r-q}) divides (M): (r\mid d!) and (i^{r-q}\mid (n!)^d). Hence (A_i=MT_i) has integral entries and (|(A_i)_{rq}|\le M). In particular
[
 \log_2 M\le d\log_2 d +dn\log_2 n
]
(with (\log_2 1=0)); these bounds are intentionally conservative and polynomial in (n,s).

Let (F) be a binary tree formula with (k\le s) total gates and scalar leaves (p_j/q_j\in\mathbb Q), (q_j\ge1), with (|p_j|,q_j\le2^H). The tree leaves are distinctly counted even if their values coincide. For every subtree (U), put
[
 K_U=\prod_{\text{scalar leaves in }U}q_j\, M^{\#\text{variable leaves in }U}.
]
There is an integer matrix (Z_U) such that (U(T)=Z_U/K_U), constructible bottom-up without rational reductions:
- scalar (p/q): (Z=pI_d,K=q); variable (x_i): (Z=A_i,K=M);
- sum: (Z_{U+V}=Z_UK_V+Z_VK_U, K_{U+V}=K_UK_V);
- ordered product: (Z_{UV}=Z_UZ_V, K_{UV}=K_UK_V).

Set (U_0=\max(H,\lceil\log_2 M\rceil)) and (W=U_0+\lceil\log_2 d\rceil+2). Induction on total gate count (k_U) proves
[
 K_U\le2^{k_UU_0},\qquad \max_{a,b}|(Z_U)_{ab}|\le2^{k_UW}.
]
The product step uses at most (d) summands per entry. The sum step uses (K_U,K_V\le 2^{kU_0}), a factor of two for the two summands, and the extra parent gate; both fit (W\ge U_0+\lceil\log_2d\rceil+2). Every intermediate integer numerator therefore has at most (sW+2) binary digits; every denominator at most (sU_0+1). Straightforward (O(sd^3)) integer matrix arithmetic operations with schoolbook products give a deliberately coarse evaluation bound (O(sd^3(sW+2)^2)) bit operations, plus polynomial preprocessing for (M,A_i), and the scalar encodings. The generator itself has (nd^2) entries, constructible independently of (H). No uniform bit claim is made if scalar leaves range over an arbitrary characteristic-zero field without a finite bit encoding.

This provides an **explicit full input-encoding and intermediate-growth certificate** for formula evaluation, rather than inferring bit complexity merely from (m\le2s). The argument directly handles constants, sums and ordered products and never expands monomials.

## Acyclic branching-program distinction

Let an (m)-vertex DAG have (E) affine-linear edges with rational coefficients, each coefficient having at most (H) bits. Let (D) be the product of all positive coefficient denominators (at most (E(n+1)) factors) and set (C=DM). Each edge evaluation (L_e(T)) has integral numerator over denominator (C). Evaluate **exact path length layers** (ell=0,\ldots,m-1) by
[
 Z_{v,0}=\begin{cases}I_d&v=\text{sink}\\0&\text{otherwise}\end{cases},\quad
 Z_{v,\ell+1}=\sum_{e:v\to w}(C L_e(T))Z_{w,\ell}.
]
Then (Z_{v,\ell}/C^\ell) sums all length-(ell) ordered path evaluations from (v) to the sink. Since a DAG path has length (<m), summing after scaling to common denominator (C^m) yields the exact ABP output in (O(mEd^3)) integer ring operations. The integer operand lengths are bounded by (O(m[\log C+\log d+\log(E+1)+\log(n+1)+H])); (\log C\le E(n+1)H+O(d\log d+dn\log n)). Thus rational-input ABP evaluation is polynomial in the complete explicit input size, (m,n,d,E,H). This is a bit-cost statement about an **explicitly listed DAG**, not about the formula expansion of a shared circuit.

## Exact shared-circuit obstruction

Set (g_0=x_1), (g_{j+1}=g_jg_j), reusing the same previous gate at both inputs. This has (j) multiplication gates plus one leaf as a DAG, but represents the nonzero polynomial (x_1^{2^j}). Its formula-tree expansion has (2^j) leaves. Since (T_1) is strictly lower triangular (d\times d), (T_1^d=0). Hence for any (2^j\ge d),
[
 g_j(T_1,\ldots,T_n)=T_1^{2^j}=0.
]
In particular, blindly replacing formula size (s) by circuit-gate count (j+1) in (d=2n(j+1)^2) fails for sufficiently large (j) (e.g. (n=1,j=10): (d=242<1024)). This is an exact counterexample to **that size substitution/that nilpotent tuple**, not a statement that arbitrary small-circuit black-box identity testing is impossible.

## Finite diagnostic and scope

Direct rational arithmetic on (T_1,T_2) for (d\in\{3,4,6\}) found the first-column vector of ([T_1,T_2]) equal to zero through index 2 and with index-3 coefficient (-1/24) for (d\ge4). This verifies one ordered-word distinction; it is not a test of the external word-independence/multiplicity proofs.

Current return: explicit polynomial bit bound for binary-encoded rational formula inputs; exact DAG dynamic-programming bound; one rigorous non-transfer counterexample for shared circuits. Remaining task: test the full bit model for arbitrary coefficient domains and whether any improved circuit treatment avoids the nilpotent-degree obstruction without formula expansion. The original manuscript's (m\le2s), multiplicity and singleton-hitting guarantees remain external/unreviewed, and no native BRC correspondence is claimed.
