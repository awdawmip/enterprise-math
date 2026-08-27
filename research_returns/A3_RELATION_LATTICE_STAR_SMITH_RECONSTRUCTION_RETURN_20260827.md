# A3 Relation Lattice — Star Smith Reconstruction Return

**Task:** `RS-A3-RELATION-LATTICE`  
**Publication:** `TP2-946818AF02EE15E31BF1`  
**Researcher:** `EM-A3RL-5A6CC5`  
**Execution:** `chatgpt-a3rl-20260827-1930`  
**Verdict:** `SUCCESS`  
**Hard target:** `A3_STAR_SMITH_NORMAL_FORM_AND_COKERNEL_EXACTLY_CLASSIFIED / MET`

## Executive result

The legacy A3 spanning-tree result knew the determinant/index of sparse total-plus-relation coordinates but not the finite abelian structure of the coordinate obstruction. For every star basis, that missing structure is now exact.

Let

\[
g=\gcd_i(m_i),\qquad a_i=m_i/g,\qquad \tau=\sum_i a_i,
\]

choose a star center \(c\), and put

\[
r=a_c.
\]

For the **primitive** relation coordinates \(z_{ci}=Z_{ci}/g=a_i p_c-rp_i\), the Smith invariant factors of the total-plus-star coordinate map are

\[
\operatorname{SNF}(C^{\rm prim}_{c})=
\begin{cases}
(1), & N=1,\\[2mm]
(1,\tau), & N=2,\\[2mm]
(1,1,\underbrace{r,\ldots,r}_{N-3},r\tau), & N\ge 3.
\end{cases}
\]

For the **unnormalized** coordinates \(Z_{ci}=m_i p_c-m_c p_i\),

\[
\operatorname{SNF}(C_{c})=
\begin{cases}
(1), & N=1,\\[2mm]
(1,g\tau), & N=2,\\[2mm]
(1,g,\underbrace{gr,\ldots,gr}_{N-3},gr\tau), & N\ge 3.
\end{cases}
\]

This strictly strengthens the frozen determinant/index theorem.

## 1. Exact matrix reduction

Permuting vertices is unimodular, so place the center at vertex \(0\). Write the primitive capacities as

\[
(r,u_1,\ldots,u_m),\qquad m=N-1,
\]

where \(\gcd(r,u_1,\ldots,u_m)=1\) and

\[
\tau=r+\sum_{i=1}^{m}u_i.
\]

The primitive star coordinate matrix has first row \((1,\ldots,1)\), and leaf row \(i\)

\[
u_i e_0^T-r e_i^T.
\]

For every leaf column perform

\[
C_i\leftarrow C_i-C_0.
\]

The total row becomes \((1,0,\ldots,0)\). Then for every leaf row perform

\[
R_i\leftarrow R_i-u_iR_0.
\]

After changing signs on leaf rows, the matrix is unimodularly equivalent to

\[
1\oplus B,\qquad
B=rI_m+u\mathbf 1^T,
\]

where \(u=(u_1,\ldots,u_m)^T\).

For unnormalized relations, each relation row is multiplied by \(g\), so exactly the same operations give

\[
C_c\sim 1\oplus gB.
\]

Thus the problem is reduced to one explicit diagonal-plus-rank-one integer block.

## 2. Determinantal divisors of \(B=rI+u\mathbf 1^T\)

Let \(\Delta_k(B)\) be the gcd of all \(k\times k\) minors.

### Boundary \(m=1\)

Here

\[
B=[r+u_1]=[\tau],
\]

so the Smith form is simply \((\tau)\).

### The first divisor for \(m\ge2\)

Off-diagonal entries expose every \(u_i\), while subtracting an off-diagonal entry in row \(i\) from the diagonal entry in the same row exposes \(r\). Hence

\[
\Delta_1(B)=\gcd(r,u_1,\ldots,u_m)=1.
\]

### Intermediate divisors

Fix \(2\le k\le m-1\).

Every \(k\times k\) submatrix is the sum of a restricted \(rI\) block and a rank-one block. In a determinant expansion, at most one column can be taken from the rank-one part, because two such columns are proportional. Consequently every nonzero term contains at least \(k-1\) factors of \(r\), so

\[
r^{k-1}\mid \Delta_k(B).
\]

The divisibility is sharp.

Choose distinct \(i,j\) and a set \(K\) of \(k-1\) indices disjoint from them. The off-principal minor with row set \(K\cup\{i\}\) and column set \(K\cup\{j\}\) is

\[
\pm r^{k-1}u_i.
\]

Hence \(\Delta_k(B)/r^{k-1}\) divides every \(u_i\).

A principal minor on an index set \(I\), \(|I|=k\), is

\[
r^{k-1}\left(r+\sum_{i\in I}u_i\right).
\]

Therefore the normalized gcd also divides \(r\). Since

\[
\gcd(r,u_1,\ldots,u_m)=1,
\]

the normalized gcd is \(1\), and thus

\[
\boxed{\Delta_k(B)=r^{k-1}\qquad(1\le k\le m-1).}
\]

### Full determinant

The rank-one determinant identity gives

\[
\det(B)
=r^{m}\left(1+\frac{\mathbf 1^Tu}{r}\right)
=r^{m-1}\left(r+\sum_i u_i\right)
=r^{m-1}\tau.
\]

Hence

\[
\Delta_m(B)=r^{m-1}\tau.
\]

## 3. Smith invariant factors

Invariant factors are successive quotients

\[
d_k=\Delta_k/\Delta_{k-1},\qquad \Delta_0=1.
\]

Therefore for \(m\ge2\),

\[
\operatorname{SNF}(B)
=
(1,\underbrace{r,\ldots,r}_{m-2},r\tau).
\]

Adding the leading direct-summand \(1\) yields the primitive theorem:

\[
\operatorname{SNF}(C^{\rm prim}_c)
=
(1,1,\underbrace{r,\ldots,r}_{N-3},r\tau),
\qquad N\ge3.
\]

If \(UBV=D\) is a Smith reduction, then

\[
U(gB)V=gD.
\]

Because multiplying every invariant factor by the positive integer \(g\) preserves the divisibility chain, the Smith form of \(gB\) is \(gD\). This gives the unnormalized theorem immediately.

## 4. Exact cokernel and cyclicity boundary

The finite obstruction group of ambient sparse coordinates modulo legal A3 coordinates is the cokernel.

### Primitive coordinates

\[
\operatorname{coker}(C^{\rm prim}_c)\cong
\begin{cases}
0, & N=1,\\
\mathbb Z/\tau\mathbb Z, & N=2,\\
\mathbb Z/(r\tau)\mathbb Z, & N=3,\\
(\mathbb Z/r\mathbb Z)^{N-3}\oplus \mathbb Z/(r\tau)\mathbb Z, & N\ge4.
\end{cases}
\]

Therefore:

- \(N\le3\): the primitive star obstruction is always cyclic;
- \(N\ge4\): it is cyclic **iff \(r=a_c=1\)**.

This is the sharp form of the old unit-primitive-star observation. A unit primitive center kills every local \(r\)-torsion channel and leaves exactly the global period \(\tau\). A nonunit center in dimension \(N\ge4\) produces genuine multi-generator torsion, so no single congruence can describe legal coordinates after arbitrary integer basis change.

### Unnormalized coordinates

For \(N\ge3\),

\[
\operatorname{coker}(C_c)
\cong
\mathbb Z/g\mathbb Z
\oplus
(\mathbb Z/(gr)\mathbb Z)^{N-3}
\oplus
\mathbb Z/(gr\tau)\mathbb Z.
\]

Thus common relation quantum \(g\) contributes an additional torsion layer that primitive normalization removes exactly.

## 5. Recovery of the frozen index theorem

For \(N\ge3\), the primitive invariant-factor product is

\[
r^{N-3}(r\tau)=\tau r^{N-2}.
\]

The unnormalized product is

\[
g\,(gr)^{N-3}(gr\tau)
=
g^{N-1}\tau r^{N-2}.
\]

Since

\[
\sum_i m_i=g\tau,\qquad m_c=gr,
\]

this equals

\[
(\sum_i m_i)m_c^{N-2},
\]

which is precisely the frozen star specialization of the spanning-tree index formula

\[
I_T=(\sum_i m_i)\prod_i m_i^{\deg_T(i)-1}.
\]

So the old determinant theorem is recovered as the order of the newly classified cokernel.

## 6. Independent exact regression

Checker:

`scripts/check_a3_relation_lattice_star_smith.py`

The checker intentionally does **not** invoke a Smith-normal-form implementation. It:

1. builds the primitive and unnormalized integer star matrices;
2. computes every minor of every order by exact Bareiss determinants;
3. takes gcds of all \(k\times k\) minors to obtain determinantal divisors;
4. reconstructs invariant factors from successive gcd quotients;
5. compares them with the closed formula;
6. independently verifies that their product equals the exact determinant.

Exhaustive tested domains:

- \(N=1,2,3,4\): every capacity vector with entries in \(1,\ldots,6\);
- \(N=5\): every capacity vector with entries in \(1,\ldots,4\);
- every possible star center;
- both primitive and unnormalized coordinate matrices.

Result:

\[
\boxed{2578\text{ capacity vectors},\quad
22060\text{ coordinate matrices},\quad
0\text{ failures}.}
\]

Observed checker output:

`A3_STAR_SMITH_REGRESSION_PASS capacity_vectors=2578 coordinate_matrices=22060 failures=0`

Frozen certificate:

`research_artifacts/A3_RELATION_LATTICE_STAR_SMITH_RECONSTRUCTION/exact_minor_regression.json`

The finite run is regression/falsification evidence only; the general theorem is the determinantal-divisor proof above.

## 7. Prior-art boundary

The general machinery used here is standard integer-matrix theory:

- Smith normal form is invariant under left/right unimodular transformations;
- the product of the first \(k\) Smith invariant factors is the gcd of the \(k\times k\) minors;
- Smith factors classify the finite abelian cokernel.

These facts are classical and are explicitly reviewed, for example, in *A Formalization of the Smith Normal Form in Higher-Order Logic* (PMC9637085), and in Morris Newman's work on determinantal divisors. The present task therefore makes **no novelty claim** for Smith theory, determinantal divisors, rank-one matrix methods, or their general algebraic setting.

The project-local contribution is the exact specialization to the A3 sparse relation coordinates and the resulting interpretation of center-capacity torsion versus the canonical translation period. No exhaustive external novelty clearance for that specialized formula has been attempted.

## 8. Scope and residue

**Closed in this task**

- exact primitive star Smith form;
- exact unnormalized star Smith form;
- exact finite cokernel;
- sharp primitive cyclicity boundary;
- recovery of the old star index;
- exact-minor regression with zero failures.

**Not closed by this task**

- full Smith classification for an arbitrary non-star spanning tree;
- a tree-wide closed formula for all invariant factors;
- Lean formalization of the star Smith theorem;
- any E001/contact interpretation;
- any external novelty claim;
- any Foundation or canonical promotion.

The most valuable next A3 research question is the arbitrary-tree Smith problem: determine whether the invariant factors admit a cut/forest or \(p\)-adic pruning formula whose product recovers the known degree-weighted index. That is a genuine successor frontier, not needed for this task's hard target.

## Final disposition

`SUCCESS / A3_STAR_SMITH_NORMAL_FORM_AND_COKERNEL_EXACTLY_CLASSIFIED`

Hard block: `NONE`.

Unresolved residue for this task: `NONE`.

Parent-program residue: `GENERAL_TREE_SMITH_CLASSIFICATION_AND_OPTIONAL_LEAN_FORMALIZATION`.
