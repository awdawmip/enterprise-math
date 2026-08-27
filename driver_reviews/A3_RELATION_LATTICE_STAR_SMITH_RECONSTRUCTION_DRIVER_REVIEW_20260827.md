# Driver Review — A3 Relation-Lattice Star Smith Reconstruction

Status: `DRIVER_FINAL / ACCEPTED / TASK_HARD_TARGET_CLOSED / EXACT_SMITH_AND_COKERNEL_CLASSIFICATION / RESULT_ONLY / NO_PROMOTION`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-A3-RELATION-LATTICE`

Publication: `TP2-946818AF02EE15E31BF1`

Execution: `ER-EE0E1D7C8677979B5961`

Researcher-ID: `EM-A3RL-5A6CC5`

Result: `RR-A87B12827B51E8B7916B`

Source result PR: `#735`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`HARD_TARGET = ACHIEVED`.

`A3_STAR_SMITH_NORMAL_FORM_AND_COKERNEL_EXACTLY_CLASSIFIED = true`.

`RESULT_CLASS = EXACT_INTEGER_LATTICE_THEOREM / STAR_BASIS_SMITH_CLASSIFICATION / RESULT_ONLY`.

`DESTINATION = ARCHIVE / CURRENT_MAIN_RESULT_REGISTRY`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`SUCCESSOR_TASK_FROM_THIS_REVIEW = NONE`.

The Driver accepts the primitive and unnormalized star-coordinate Smith normal forms, their exact finite cokernels, the sharp primitive cyclicity boundary, and recovery of the previously frozen star index. This closes the published replay hard target. It does not classify arbitrary non-star spanning trees and does not constitute a Lean or Foundation promotion.

## 2. Decisive matrix reduction

Let

\[
g=\gcd_i(m_i),\qquad a_i=m_i/g,\qquad \tau=\sum_i a_i,
\]

place the star center at vertex \(0\), and write its primitive capacity as \(r=a_0\). For the remaining primitive capacities \(u=(u_1,\ldots,u_m)^T\), where \(m=N-1\), the total-plus-star coordinate matrix has first row \((1,\ldots,1)\) and leaf rows

\[
u_i e_0^T-r e_i^T.
\]

Subtracting the center column from every leaf column, then clearing the center entry of every relation row and changing relation-row signs, is unimodular and gives

\[
C_c^{\rm prim}\sim 1\oplus B,
\qquad
B=rI_m+u\mathbf 1^T.
\]

For unnormalized relations each relation row is multiplied by \(g\), so

\[
C_c\sim 1\oplus gB.
\]

This agrees exactly with the canonical relation convention
\(Z_{ij}=m_jp_i-m_ip_j\) and with the previously frozen star-index formula.

## 3. Exact determinantal divisors

For \(m=1\), \(B=[\tau]\), giving the \(N=2\) boundary immediately.

Assume \(m\ge2\). Off-diagonal entries expose every \(u_i\), while a diagonal entry minus an off-diagonal entry in the same row exposes \(r\). Since the primitive capacities have gcd one,

\[
\Delta_1(B)=\gcd(r,u_1,\ldots,u_m)=1.
\]

For \(2\le k\le m-1\), every \(k\times k\) minor of \(B=rI+u\mathbf1^T\) is divisible by \(r^{k-1}\): in the determinant expansion at most one column can be selected from the rank-one summand, because two such columns are proportional.

The lower divisibility bound is sharp. For distinct \(i,j\) and \(K\) of size \(k-1\), disjoint from them, the off-principal minor with rows \(K\cup\{i\}\) and columns \(K\cup\{j\}\) equals

\[
\pm r^{k-1}u_i.
\]

Thus \(\Delta_k(B)/r^{k-1}\) divides every \(u_i\). A principal \(k\)-minor on \(I\) is

\[
r^{k-1}\left(r+\sum_{i\in I}u_i\right).
\]

After subtracting the already-controlled \(u_i\)-terms, the normalized gcd also divides \(r\). Primitive gcd one therefore forces

\[
\Delta_k(B)=r^{k-1}
\qquad(1\le k\le m-1).
\]

Finally, the matrix determinant lemma gives

\[
\det B=r^{m-1}\tau.
\]

Hence

\[
\operatorname{SNF}(B)
=
(1,\underbrace{r,\ldots,r}_{m-2},r\tau)
\qquad(m\ge2).
\]

No determinant-only inference is being used; every determinantal divisor is fixed.

## 4. Accepted Smith forms and cokernels

The accepted primitive invariant factors are

\[
\operatorname{SNF}(C_c^{\rm prim})=
\begin{cases}
(1),&N=1,\\
(1,\tau),&N=2,\\
(1,1,\underbrace{r,\ldots,r}_{N-3},r\tau),&N\ge3.
\end{cases}
\]

Because a Smith reduction \(UBV=D\) implies
\(U(gB)V=gD\), and multiplication by \(g>0\) preserves the divisibility chain, the accepted unnormalized factors are

\[
\operatorname{SNF}(C_c)=
\begin{cases}
(1),&N=1,\\
(1,g\tau),&N=2,\\
(1,g,\underbrace{gr,\ldots,gr}_{N-3},gr\tau),&N\ge3.
\end{cases}
\]

Consequently, for primitive coordinates,

\[
\operatorname{coker}(C_c^{\rm prim})\cong
\begin{cases}
0,&N=1,\\
\mathbb Z/\tau\mathbb Z,&N=2,\\
\mathbb Z/(r\tau)\mathbb Z,&N=3,\\
(\mathbb Z/r\mathbb Z)^{N-3}\oplus
\mathbb Z/(r\tau)\mathbb Z,&N\ge4.
\end{cases}
\]

Thus the primitive obstruction is always cyclic for \(N\le3\), while for \(N\ge4\) it is cyclic exactly when \(r=a_c=1\). For \(r>1\), at least two nontrivial invariant factors remain, so the obstruction cannot be represented by one congruence after any integer basis change.

## 5. Recovery of the frozen index

For \(N\ge3\), the primitive invariant-factor product is

\[
\tau r^{N-2}.
\]

The unnormalized product is

\[
g^{N-1}\tau r^{N-2}
=
\left(\sum_i m_i\right)m_c^{N-2},
\]

which is exactly the star specialization of

\[
I_T=
\left(\sum_i m_i\right)
\prod_i m_i^{\deg_T(i)-1}.
\]

The new result therefore strictly refines, and does not contradict or replace, the earlier determinant/index theorem.

## 6. Independent regression boundary

The frozen checker does not invoke a Smith-normal-form oracle. It computes every minor of every order by exact Bareiss determinants, forms determinantal-divisor gcds, and reconstructs invariant factors by successive quotients.

Frozen scope:

- all capacity vectors with entries \(1,\ldots,6\) for \(N=1,2,3,4\);
- all capacity vectors with entries \(1,\ldots,4\) for \(N=5\);
- every star center;
- primitive and unnormalized matrices;
- \(2,578\) capacity vectors;
- \(22,060\) coordinate matrices;
- \(0\) failures.

This is accepted as falsification/regression evidence only. The general theorem is supplied by the exact determinantal-divisor argument.

## 7. Method harvest and routing

`METHOD_HARVEST = RESULT_ONLY`.

The reusable ingredients—unimodular matrix reduction, determinantal divisors, the matrix determinant lemma, and Smith classification—are standard tools. This review does not register a new general-purpose Enterprise tool and makes no external novelty claim.

The arbitrary-tree Smith problem and optional Lean formalization remain legitimate parent-program residue, but a successful star replay is not by itself a successor trigger. No continuation task is published in this review. Any future arbitrary-tree or formalization task must pass its own value, lineage, and successor gate.

## 8. Integration boundary

PR `#735` is based on an earlier moving-main snapshot and contains only the frozen return, execution/result records, exact-minor checker, and regression artifact. The accepted payload is semantically replayed onto current `main` with the immutable Driver review record; no shared mathematical source file is rewritten.

No CI-success claim is made. Acceptance rests on the exact proof audit, source-definition consistency, digest-pinned result chain, and exact-minor evidence.

## 9. Final freeze

`RR-A87B12827B51E8B7916B = ACCEPTED`.

`TP2-946818AF02EE15E31BF1 = TERMINAL_AT_TASK_SCOPE`.

`A3_STAR_SMITH_REPLAY_HARD_TARGET = CLOSED`.

`A3_GENERAL_TREE_SMITH = PARENT_PROGRAM_RESIDUE / NOT_OPENED_HERE`.

`LEAN_FORMALIZATION = OPTIONAL_PARENT_RESIDUE / NOT_OPENED_HERE`.

`FOUNDATION_AND_WORKING_TRUTH_STATUS = UNCHANGED`.
