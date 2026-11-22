# Uniform matching stability across packet cutoffs and elimination trees

Author result, 2026-11-22. Researcher EM-DIRECT-B5750A, TASK_RESEARCH.

This is an auxiliary signed-readout theorem on the complete integer road. It
does not identify signed cancellation with positive BRC mass cancellation,
delete composites, change the native X6 basis, or assert an RH estimate.
The actual thickness road and the auxiliary Lambda reference retain the same
unit convention, complete prefix, and true endpoints.

## 1. Common road and coefficient identities

Use the definitions and exact matching identity in
`../rh_short_interval_20261122/SHORT_INTERVAL_STRUCTURE_AND_UNIFORM_TRANSFER.md`:

\[
 c-c^*=\mu(n)I(\log n),\qquad
 c^*=\mu*(\Lambda-\kappa),\qquad
 0\le I(\log n)\le\eta_B\quad(n\le B).
\]

Here \(D_1=\Lambda(1)=0\), \(c_1=c_1^*=-2\log2\), and
\(\eta_B=(\prod_j a_j)(\log B)^{m+1}/(m+1)!\). The same quantity
bounds \(|D_n-\Lambda(n)|\) for every integer \(n\le B\).
For \(e_n=D_n-\Lambda(n)\), the full prefix difference is exactly

\[
 E_n=q_n-q_n^*=\sum_{k=2}^{n}e_k(n/k-1).
\]

Both roads include the identical affine term \((1+\gamma)n\). In particular,
the comparison does not reset either road to zero at the left endpoint.
Writing \(H_n^{\rm har}=\sum_{k=1}^n1/k\),

\[
 |E_n|\le\eta_B\{n(H_n^{\rm har}-1)-(n-1)\}
 \le\eta_B n\log n.
 \tag{1}
\]

On the closed window define \(\|v\|_w^2=\sum_{n=A}^{B}v_n^2/n^2\).
Thus

\[
 \|E\|_w\le D_B:=\eta_B\sqrt{B-A+1}\log B.
 \tag{2}
\]

## 2. The family being compared

Partition \([A,B]\) into integer dyadic blocks \([X,Y]\), with
\(Y\le2X\) and \(b_X=Y-X\). In each block choose any finite integer
fine partition and any legal binary elimination hierarchy. The block's
endpoints are retained. For a packet \(p=(L,x,R)\), put

\[
 a=x-L,\quad b=R-x,\quad h=R-L,\quad
 T_p(n)=G_{[L,R]}(n,x),\quad\tau_p=ab/h.
\]

Allow an independent integer cutoff \(1\le H_p\le X\) at every packet.
The bound \(H_p\le X\) is part of this theorem, not a conclusion about
which cutoff is optimal. On each road form

\[
 d_p=\sum_{2\le d\le H_p}c_d\,\delta K_{d,p},\qquad
 C=\sum_p d_pT_p,
 \qquad
 \delta K_{d,p}=K_{d,p}-K_{1,p}/d.
 \tag{3}
\]

Use exactly the same geometry and cutoffs for the paired reference \(C^*\).
The published packet/phase theorem gives
\(d_p=\mathcal L_pP_{H_p}\), exact simultaneous realization at all packet
moments, zero values at all retained block endpoints, and

\[
 \mathcal E_D\!\left(\sum_pz_pT_p\right)
 =\sum_p\tau_pz_p^2.
 \tag{4}
\]

The geometry and cutoffs may vary over the entire finite allowed family.
No assertion is made that the best choices for the two roads coincide.

## 3. A uniform coefficient perturbation bound

The exact phase-kernel estimate from the preceding triangle checkpoint is

\[
 |\delta K_{d,p}|\le\frac{d-1}{dx}.
\]

Together with \(c_d-c_d^*=\mu(d)I(\log d)\), this gives

\[
 |d_p-d_p^*|
 \le \frac{\eta_B}{x}\sum_{d=2}^{H_p}\frac{d-1}{d}
 =\eta_B\frac{H_p-H_{H_p}^{\rm har}}{x}
 \le\eta_B.
 \tag{5}
\]

This uses the exact squarefree-supported error. It has no divisor-count
factor and holds simultaneously for every allowed cutoff. More precise
bounds may replace \(\eta_B\) by \(I(\log H_p)\) or its product envelope.

## 4. From all packet errors to one complete-window norm

For a vector vanishing at \(X,Y\), the previously proved discrete Green
trace inequality is

\[
 \|v\|_{w,[X,Y]}^2\le J_{X,Y}\,\mathcal E_D(v),\qquad
 J_{X,Y}=\sum_{X<n<Y}\frac{(n-X)(Y-n)}{(Y-X)n^2}.
 \tag{6}
\]

In particular,

\[
 0\le J_{X,Y}\le\frac{b_X(b_X-1)}{4X^2}\le\frac14.
 \tag{7}
\]

At one tree depth the packet support interiors are disjoint and
\(\sum_p\tau_p\le\sum_p h_p/4\le b_X/4\).
Let \(L_X\) be the number of occupied depth levels, counting the root as
level 1 and an empty tree as 0. Then (4)--(7) prove the sharper bound

\[
 \boxed{\quad
 \|C-C^*\|_w^2
 \le\frac{\eta_B^2}{4}
       \sum_XJ_{X,Y}L_Xb_X.
 \quad}
 \tag{8}
\]

This sum is over actual blocks; their zero endpoint values prevent double
counting boundary contributions. In particular, if \(L_X\le L_{\max}\),

\[
 \|C-C^*\|_w\le\frac{\eta_B}{4}
                 \sqrt{L_{\max}(B-A)}.
 \tag{9}
\]

No balanced-tree assumption is needed for a uniform bound over *all*
integer hierarchies. Every packet removes one distinct interior integer,
so \(L_X\le b_X-1\). Consequently

\[
 \sum_XL_Xb_X\le\sum_Xb_X^2\le(B-A)^2,
\]

and therefore

\[
 \boxed{\quad\|C-C^*\|_w\le
          C_B:=\frac{\eta_B(B-A)}4.\quad}
 \tag{10}
\]

This costs no union bound over cutoffs, partitions, or hierarchies: a
deterministic estimate applies to every member of the finite family.

## 5. Corrected observations and optimization values

Positive and negative part are both 1-Lipschitz in this weighted Euclidean
norm. For each paired choice, (2) and (10) imply

\[
 \left|\|(q+C)_+\|_w-\|(q^*+C^*)_+\|_w\right|
 \le D_B+C_B.
 \tag{11}
\]

The natural return budget

\[
 \mathcal R(q,C)=\|(q+C)_+\|_w+\|C_-\|_w
\]

is an upper bound for \(\|q_+\|_w\), because
\(q_+\le(q+C)_++C_-\) pointwise. The full prefix and true closed
endpoints are included. For every allowed tree/cutoff choice,

\[
 |\mathcal R(q,C)-\mathcal R(q^*,C^*)|
 \le D_B+2C_B.
 \tag{12}
\]

Taking an infimum over the same allowed family preserves a uniform
pointwise comparison. However, a useful degeneracy must be made explicit:
the complete family includes \(H_p=1\) for every packet, hence \(C=0\).
Since \(\mathcal R(q,C)\ge\|q_+\|_w\),

\[
 \inf_C\mathcal R(q,C)=\|q_+\|_w.
 \tag{12a}
\]

Its full-family optimum therefore has the stronger comparison bound
\(D_B\) directly from (2); it is not a new optimization principle. The
uniform per-configuration conclusion (12), and the corrected-observation
comparison (11), retain their stated content. We do not change the
allowed family merely to conceal this degeneracy.

### 5.1 The computable packet budgets do have a uniform comparison

Write the exact fine decomposition as
\(q=J+\sum_pt_pT_p+P_{\rm fine}\), where \(J\) interpolates the true
block endpoints and \(P_{\rm fine}=q-I_\Pi q\). Both interpolants retain
their actual endpoint values. For \(s_p=t_p+d_p\), let either

\[
 W(s)=U(s):=\sum_p(s_p)_+T_p
\]

or use the companion ancestor envelope \(W(s)=Z(s)\), defined on each
tree by

\[
 Z_p(s)=(s_pT_p+Z_l(s)+Z_r(s))_+.
\]

In both cases \(W(s)\ge\sum_ps_pT_p\). The following is a closed-window
*root* budget, so its square is an energy upper bound:

\[
 \mathcal B_{\mathcal T,H}^{W}(q)
 =\|(J+W(t+d))_+\|_w
  +\|(P_{\rm fine})_+\|_w+\|C_-\|_w
 \ge\|q_+\|_w.
 \tag{12b}
\]

This formula uses the closed norm in every term. It is not numerically
identical to the slightly sharper finite certificate that first budgets
the open interior and then adds the exact two endpoint squares.

For any common integer interpolation partition, (1) and linear
interpolation of the function \(n\mapsto n\log B\) imply

\[
 \|J-J^*\|_w\le D_B,
 \qquad\|I_\Pi E\|_w\le D_B,
 \qquad\|P_{\rm fine}-P_{\rm fine}^*\|_w\le2D_B.
 \tag{12c}
\]

For a packet in a block starting at \(X\),

\[
 |t_p-t_p^*|\le\eta_BK_{1,p}
 \le\eta_Bh_p/(2X)\le\eta_B/2,
\]

because the complete integer hat sum equals \(h_p/2\). Thus
\(|s_p-s_p^*|\le3\eta_B/2\). Pointwise 1-Lipschitz continuity of positive
part, directly for \(U\) and inductively for \(Z\), yields

\[
 |W(s)-W(s^*)|\le V:=\sum_p|s_p-s_p^*|T_p.
\]

Apply the same orthogonal Dirichlet identity and trace bound to this
nonnegative-coefficient \(V\). Equations (8)--(10), with coefficient
bound \(3\eta_B/2\), give

\[
 \|W(s)-W(s^*)\|_w\le\tfrac32 C_B.
 \tag{12d}
\]

Combining (12b)--(12d) and (10) proves

\[
 \boxed{
 |\mathcal B_{\mathcal T,H}^{W}(q)
  -\mathcal B_{\mathcal T,H}^{W}(q^*)|
 \le3D_B+\tfrac52 C_B.}
 \tag{12e}
\]

This bound is uniform over the complete paired family of fine partitions,
legal trees, and permitted cutoffs, for either \(U\) or \(Z\). Hence it
also bounds the difference of the two infima of these computable budgets.
It does not assert the existence of a good budget, the same minimizing
tree on both roads, or a better estimate from phase correction. Without
phase correction, the corresponding bound improves to
\(3D_B+C_B/2\). The companion mixed-phase dominance theorem explains
which negative-packet information can account for an improvement.

## 6. An unconditional vanishing error for the existing node family

For the already constructed stable rational matching nodes, \(B\ge e^{10}\),
\(m=\lceil\log B\rceil\), the earlier Chebyshev/product bounds give

\[
 \eta_B\le\frac{8192}{189\log B}(e/8)^m
       \le K\frac{B^{-\beta}}{\log B},\qquad
 K=8192/189,\quad\beta=\log8-1>1.
 \tag{13}
\]

The constants come from the ideal product bound \(128/3\), followed
by the certified rational-perturbation factor \(64/63\). Therefore

\[
 D_B\le K B^{1/2-\beta},\qquad
 C_B\le\frac K4\frac{B^{1-\beta}}{\log B}
 \longrightarrow0.
 \tag{14}
\]

The convergence is uniform over all integer fine partitions, all legal
elimination hierarchies in the stated dyadic blocks, and all packet choices
\(H_p\le X\), including the two computable packet budgets in (12e).
For logarithmic-depth hierarchies, (9) is substantially sharper.
No unbounded cancellation estimate for \(\mu\) or \(\Lambda\) was used
in this perturbation result.

The mathematical implication is specific: in this whole permitted family,
finite-thickness matching is no longer an obstruction to transferring an
eventual subpower root-energy or return-budget estimate from the reference
road to the actual road. The needed reference arithmetic estimate remains
an open input. A uniform perturbation theorem is not that estimate.

## 7. Provenance and proof dependencies

- Previous Source commit:
  `2e8a9aad42950ce4e0980e284772f23ba8e8da21`.
- Packet kernel, phase realization, Dirichlet orthogonality and trace:
  `research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/rh_triangle_arithmetic_20261122/TRIANGLE_KERNEL_AND_PHASE_COMMUTATION.md`.
- Stable rational nodes and product bounds:
  local `rh_correlation_rational/NOTES.md`, and its cited
  `rh_next_root/CHEBYSHEV_THICKNESS_BRIDGE.md`.
- This batch's short-interval note supplies the exact coefficient split
  and explicitly retains the unit and the nonsquarefree population.
- Scientific premise snapshot: `9fc068244e4f1117f1e75df5eb0285c6697d21d7`.

Proof status: author mathematical derivation with companion author
cross-check. No independent project Review or truth promotion is asserted.
