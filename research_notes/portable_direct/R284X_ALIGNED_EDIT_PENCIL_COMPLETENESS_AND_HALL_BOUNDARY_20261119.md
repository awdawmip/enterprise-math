# R284X — Completeness of constant-kernel certificates for aligned Port edit pencils, and a sharp Hall boundary

Date: 2026-11-19. **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**. Frozen science pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. New direct predecessor R284W `research_notes/portable_direct/R284W_COMMON_KERNEL_MATCHING_PRESENT_DEGREE_CERTIFICATE_20261119.md` at commit `60720c2cc920f3710a880771f0a4d675272ab58a`; R284V's Hall complement theorem at `851060e73f9915e78e463f738c1c144962752c49`. This is the exact finite auxiliary BRC Port model of those notes, with no native X6 correspondence claimed.

## 1. A completeness theorem, not just a sufficient rank test

Let `K` be any characteristic-zero field (in the Port applications, `K=Q`), and `A_0\in K^{k x k}`. For any vectors `u,v_1,...,v_m\in K^k`, consider the **aligned-row rank-one pencil**
```
A(z)=A_0+sum_{j=1}^m z_j u v_j^T.
```
There is no restriction on the number of independent `z_j`, and zero update matrices are harmless.

**Theorem X1 (aligned-edit singularity characterization).**
```
det A(z) == 0 as a polynomial in all z
  if and only if
there exists a nonzero q with A_0 q=A_j q=0 for every j,
  or a nonzero p with p^T A_0=p^T A_j=0 for every j.
```
The same holds for *aligned-column pencils* `A(z)=A_0+sum_j z_j u_j v^T`, by transposing.

*Proof.* The reverse implication is the fixed-kernel determinant argument of R284W. For the forward implication, `det A_0=0`. If `rank A_0<=k-2`, then its left nullspace has dimension at least two; the linear condition `p^T u=0` leaves a nonzero `p` in that nullspace. It annihilates each update, giving a common left kernel. If `rank A_0=k-1`, choose nonzero right and left nullvectors `q,p` of `A_0`; the rank-one adjugate has the form `adj(A_0)=lambda q p^T` for some `lambda != 0` (after scaling the chosen vectors). The matrix determinant lemma, valid even when `A_0` is singular, gives
```
det(A_0+u f(z)^T) = det(A_0)+f(z)^T adj(A_0)u
                 = lambda (p^T u) * sum_j z_j(v_j^T q).
```
By polynomial independence of the `z_j), this is identically zero exactly when either `p^T u=0` (common left kernel) or `v_j^T q=0` for all `j` (common right kernel). This exhausts all ranks of singular `A_0`; the `k=1` case is included. QED.

**Corollary X2 (complete inexpensive criterion for aligned Port edits).** In the complementary `(n-2)x(n-2)` pencil for a fixed numerator coefficient `[x]N_ab`, if *all other surviving named matrix-unit edits* occupy one surviving row, or all occupy one surviving column, then R284W's W2 rational rank check is **both necessary and sufficient** for `[x]N_ab\equiv0`. One exact baseline-rank test on permitted untouched rows/columns therefore decides the coefficient's global zero identity without tensor interpolation. Endpoint-excluded edits are handled directly. No generic exact determinant expression needs expanding.

The corollary concerns the full *declared variable family* and does not assert that one or two coordinates suffice when the edits populate several independent rows and columns.

## 2. Hall deficiency without a constant left or right kernel: exact five-Port witness

The converse of W1 is false for general multirow/multicol edit pencils, even with small nonnegative rational Port data and strictly substochastic transitions. Take Ports `0,...,4`, output `F_30=(I-W)^-1_{30}`, named target edit `x:1->4`, and four independent other edits `z_1:3->0`, `z_2:4->0`, `z_3:2->1`, `z_4:2->2`. Baseline edges of weight `1/8` are
```
0->1, 0->2, 2->0, 2->1, 3->0, 4->0.
```
All other baseline weights are zero. For `0<=x,z_j<=1/8` each row sum is less than one. The complementary minor for `[x]N_30` deletes rows `b=0,u=1` and columns `a=3,v=4`. With remaining rows `(2,3,4)`, columns `(0,1,2)`, its matrix is
```
A(z) = [ [-1/8, -(1/8+z_3), 1-z_4],
         [-(1/8+z_1),       0,     0],
         [-(1/8+z_2),       0,     0] ].
```
Rows 3 and 4 have only column 0 as possible neighbors, so **Hall's condition fails** and `det A(z)\equiv0`. Yet **no nonzero constant common right kernel exists**: the named updates `z_1` and `z_2` force `q_0=0`; `z_3` forces `q_1=0`; `z_4` forces `q_2=0`. **No constant common left kernel exists**: `z_1,z_2,z_3` force each of the three left-vector components to vanish. Thus Hall and fixed-kernel tests are genuinely complementary, and X1's aligned-row hypothesis is substantive.

The target and all four other edits are on potential future-observer paths for `F_30` in the complete declared edit language: `3->0->1->4->0`, `3->0->2->0`, and `3->0->2->1->4->0` provide witnessing feedback/return possibilities when edits are positive. This remains a valid counterexample after observer relevance screening; the graph has the specified full observation context.

Independent cofactor calculation gives the complete numerator
```
N_30(x,z)=(1/8+z_1)(1-z_4),
```
which is globally independent of the target edit `x`, despite the absence of a constant kernel. For example at zero other edits, `N_30=1/8` and `D(0,0)=63/64>0`. The full formula is separately testable at any declared stable parameter values.

## 3. Reproducible checking and actual scope

Code: `research_notes/portable_direct/R284X_aligned_pencil_completeness.py`, importing the local exact Fraction determinant/rank helpers from `R284W_common_kernel_certificate.py`. Machine-readable output: `R284X_aligned_pencil_verification.json`.

Executed deterministic seeded checks using Python `Fraction`:
- **960** exact independently generated square pencils of sizes `k=2,3,4,5`, with `m=1,2,3` independent other-edit names sharing one row (80 cases for each `k,m` pair), all `2^m` binary parameter assignments, and independently computed common-kernel rank criteria. The polynomial determinant is multi-affine in each `z_j`, so this binary tensor evaluation is exhaustive *for each generated pencil*. In **285** of the 960 cases the determinant vanished at all nodes and the W2 common-kernel test also succeeded; all other generated cases passed the predicted logical equivalence.
- For the five-Port Hall counterexample, tested all **16** points of `z\in\{0,1/16\}^4` and both `x=0,1/8`. Cofactors exactly matched `(1/8+z_1)(1-z_4)` and all observed determinants were positive. Exact W2 tests returned neither common right nor common left kernel, while the support-matching routine returned no perfect matching.

The finite suite corroborates the algebraic theorem and verifies the given five-Port witness at these parameters. No independent review or theorem admission was performed.

## 4. Remaining mathematical problem

For complementary pencils where independently named remaining edits span **at least two rows and two columns**, characterize the singularity subspaces that are not explained by either Hall deficiency or a constant left/right kernel. Seek a compact witness with a *perfect matching* and genuine variable-dependent kernel, if such a witness is compatible with the nonnegative stable Port constraints. Determine whether one can certify the complete comparison polynomial's low degree in fewer bit operations than R284T's substituted determinants, accounting for preprocessing and exact-rank coefficient growth.
