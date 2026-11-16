# PREFIX-823 — 合并操作 Q=R+A 的任意容量精确未来观察秩

Date: 2026-11-16 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH auxiliary mathematics. Scientific input frozen at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessor: PREFIX-822. Role and scope: Source-side author result, no new native X6 Claim/Result/Review or physical Cell/Link admission.

## Precise question and model

Fix capacity q≥1, marked-source insertion multiplicity a>0 and marked-source removal multiplicity b≥0, all integers. Named source states are subsets S of the marked source 0 and a finite set of unmarked sources, with |S|≤q. Each unmarked source i has positive integral removal multiplicity β_i. Operation R removes any present source with its own multiplicity; A inserts source 0 with multiplicity a if absent and the capacity permits. The **only** available future operation is the fixed sum Q=R+A (not individually addressable R and A). For every n≥0, the observer C records the exact population histogram by total source cardinality after Q^n. Initial signed integer mass vectors are allowed for linear-rank/minimality analysis; nonnegative mass inputs are the intended count model.

The preceding PREFIX-822 conditional integer moments are
`U_{k,h}=M_{0,k,h}` (marked absent, 0≤h≤k≤q),
`V_{k,h}=M_{1,k,h}` (marked present, 0≤h≤k≤q−1).
The full moment dimension is N=(q+1)^2, with exact updates
```text
(QM) U[k,h] = (h+1) U[k+1,h+1] + b V[k,h]
(QM) V[k,h] = (h+1) V[k+1,h+1] + a U[k,h]
(CM)[l]     = U[l,0] + V[l−1,0]
```
where out-of-domain terms vanish. These are BRC exact positive-branch count transitions, not signed/amplitude cancellation laws. The named source identities remain in the input; the moment quotient is certified only for this Q-language and this histogram output, not for hidden named-source queries or native X6 events.

## Theorem 823.1 (b>0: exact combined-only minimum and finite horizon)

For every q≥1 and a,b>0, the kernel of all future Q-only histogram observations equals
`ker(C) ∩ ker(Q)` on the N-dimensional conditional-moment space, and has dimension ceil(q/2). Therefore
```text
rank_Q(q,a,b) = (q+1)^2 − ceil(q/2).
```
Observations C Q^j for 0≤j≤2q already achieve this rank. In particular, the formula is independent of the magnitudes of positive a and b.

**Proof.** Put r=k−h. The space decomposes into Q-invariant blocks E_n indexed by r=0,…,q, where n=q−r and dim E_n=2n+1. Write their variables (u_0,v_0),(u_1,v_1),…,(u_{n−1},v_{n−1}),u_n. On each block,
```text
(Q_n u)_h = (h+1)u_{h+1}+b v_h  (0≤h<n),   (Q_n u)_n=0,
(Q_n v)_h = (h+1)v_{h+1}+a u_h  (0≤h<n),   v_n=0.
```
The diagonal 2×2 blocks are B=[[0,b],[a,0]] and the final diagonal block is [0], so char(Q_n)(λ)=λ(λ²−ab)^n. At a nonzero eigenvalue μ=±√(ab), an eigenvector has u_n=0. If h>0 were the highest nonzero paired level, its vector w_h=(u_h,v_h) would be a B eigenvector and the equation at h−1 would read (μI−B)w_{h−1}=h w_h. Multiplying by a left μ-eigenvector of B contradicts its nonzero pairing with w_h. Therefore every nonzero-eigenvalue eigenvector lies at level h=0, where u_0≠0. The zero eigenvalue is algebraically simple on each E_n.

Let \(\mathcal U=\bigcap_{j\ge0}\ker(CQ^j)\), the globally unobservable Q-invariant subspace. Suppose, over an algebraic closure, that Q restricted to \(\mathcal U\) has a nonzero eigenvalue \(\mu\) and eigenvector x. In each invariant block E_r with n=q−r≥1, a nonzero \(\mu\)-eigencomponent has first entry \(u^{(r)}_0\ne0\) and \(v^{(r)}_0=(a/\mu)u^{(r)}_0\) (as proved by the highest-nonzero-level argument above). The final block E_q is one-dimensional and Q=0 there, so its \(\mu\)-eigencomponent vanishes. Since Cx=0, its cardinality-0 output forces \(u^{(0)}_0=0\), so the entire block E_0 eigencomponent is zero. The cardinality-1 output now forces \(u^{(1)}_0=-v^{(0)}_0=0\), hence the E_1 eigencomponent vanishes. Continuing successively through cardinalities 2,...,q−1 annihilates every possible nonzero-\(\mu\) eigencomponent. This is a contradiction. Hence Q on \(\mathcal U\) has only eigenvalue 0.

On each E_r the zero eigenvalue has algebraic multiplicity one, since \(\operatorname{char}(Q_r)(\lambda)=\lambda(\lambda^2-ab)^{q-r}\); therefore zero is semisimple in the direct sum Q. As an invariant subspace with only the zero eigenvalue, \(\mathcal U\subseteq\ker Q\). Conversely \(\ker C\cap\ker Q\subseteq\mathcal U\). Consequently
\(\mathcal U=\ker C\cap\ker Q\).
This argument uses the **global output boundary**, and remains valid even when \(ab=1\) and a local block has a \(+1\) eigenvector. A local constant coordinate sequence alone would not justify the conclusion.

Each E_n has a one-dimensional zero eigenspace. Solving Q_n x=0 by the recurrence shows: if n is even, its generator has u_0≠0,v_0=0 (n=0 included); if n is odd, u_0=0,v_0≠0. Its C image is consequently e_r for even q−r and e_{r+1} for odd q−r. The q+1 generators produce floor(q/2)+1 distinct coordinate output directions, with ceil(q/2) linearly independent pairwise cancellations. Hence dim(ker C∩ker Q)=ceil(q/2).

Finally the highest block E_q has a single Jordan block of size q for each μ=±√(ab), since each nonzero eigenvalue has algebraic multiplicity q and geometric multiplicity one. The zero root is simple in every E_n. Hence the global minimal polynomial is λ(λ²−ab)^q, of degree 2q+1. Cayley–Hamilton for this minimal polynomial shows C,…,C Q^(2q) determine every later C Q^j. QED.

## Theorem 823.2 (b=0: exact singular formula)

For every q≥1 and a>0, b=0,
```text
rank_Q(q,a,0) = (q+1)(q+2)/2 + 2q − 2.
```
All observations occur within 0≤j≤q+1, since Q^(q+2)=0.

**Proof.** With b=0 the marked source, once present, is never deleted, so a Q-word contains at most one effective A. For a named unmarked state with k sources and j applications of Q, unmarked removal contributes the elementary-symmetric moment with coefficient j!. For a single insertion, the j possible positions have the same product of (j−1) unmarked removals, except when the starting k=q, where insertion at the first position is capacity-forbidden, leaving j−1 positions. The resulting nonzero output rows y_{l,j}=(C Q^j)_l are exactly:
```text
y[0,j]  for 0≤j≤q;
y[l,j]  for 1≤l≤q, 0≤j≤q−l+2.
```
There are T(q)+2q such rows, where T(q)=(q+1)(q+2)/2.

For each l≥1 and 0≤j≤q−l, the row y[l,j] contains the unique coordinate V[l+j−1,j], with coefficient j!, and no other output row contains that coordinate. These q(q+1)/2 rows are linearly independent, and every linear dependence must give them coefficient zero. The remaining rows comprise y[0,j] (q+1 rows) and, for each l≥1, the two high rows j=q−l+1 and j=q−l+2. Their explicit forms are
```text
y[0,j]       = j! U[j,j]
y[l,q−l+1]   = a (q−l+1)! U[q−1,q−l]
y[l,q−l+2]   = a (q−l+1)(q−l+1)! U[q,q−l+1].
```
The first high family uses all distinct U[q−1,h] for 0≤h≤q−1, and the second uses all distinct U[q,h] for 1≤h≤q. The diagonal rows y[0,j] use distinct U[j,j]. The only coincidences occur at U[q−1,q−1] and U[q,q], yielding precisely the two dependencies
```text
y[1,q]   = aq · y[0,q−1],
y[1,q+1] = aq · y[0,q].
```
All other remaining rows have a unique U-coordinate, so no further dependencies exist. Subtracting two from T(q)+2q proves the formula. Since at most q unmarked deletions and one marked insertion can occur, Q^(q+2)=0. QED.

## Corollary: genuine named states, not only a formal moment space

Assume at least q+1 unmarked sources have pairwise distinct positive integral β_i. In each (marked status z, unmarked count k) block, select k+1 of these source weights and the k-subsets obtained by omitting one. Their polynomials ∏(1+β_i t), with one index omitted in each column, form an independent set: evaluating at t=−1/β_j isolates the j-th column. Thus the named-state mass→conditional-moment map is surjective over Q. The two displayed ranks are therefore the **minimal rational-linear future histogram carrier dimensions** among all linear representations of unrestricted named-state initial mass. The full conditional-moment carrier remains a nonnegative integer implementation; constructing a minimal nonnegative integer carrier for Q alone is a separate problem. Arbitrary nonlinear coding minimality is not asserted.

## Exact independent regression and scopes

File: `PREFIX823_R6_COMBINED_Q_OBSERVER_CHECK.py`, output `PREFIX823_R6_COMBINED_Q_OBSERVER_RESULTS.json`. The checker uses sparse exact integer transition coefficients and Gaussian elimination modulo prime 1000000007 for all q=1,…,10, a∈{1,2}, b∈{1,3} (40 positive-b configurations) and b=0 (20 configurations); the predicted ranks and the stated finite-horizon ranks agree. Independent exact Fraction elimination covers q≤5, a=1, b∈{0,1,3} (15 cases). An independently enumerated named-subset transition compares every cardinality histogram to the conditional-moment update for q≤4 and (a,b)=(1,0),(1,1),(2,3): 12 configurations, 2,286 exact comparisons. All assertions passed. Integer combinatorial counts are exact; modular rank gives characteristic-zero lower bounds, while the proofs provide exact equality. The independent named test checks the carrier/output law within its finite input window.

## Next frontier

Find explicit nonnegative integer Q-only quotients attaining the rational dimensions; compare the rank jump between b=0 and b>0 for large q; test individually addressable unmarked-source operators to identify the additional named-source residual beyond Q-only compression. Then separately study native X6 Cell/Link/Port admissibility and real event-time ordering; the auxiliary formal Q word depth is not a physical heartbeat interval.

Sources: `awdawmip/enterprise-math` PREFIX-818 through PREFIX-822; pinned Source P000, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, current `docs/RESEARCH_CONTINUATION_PROTOCOL.md` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Present status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
