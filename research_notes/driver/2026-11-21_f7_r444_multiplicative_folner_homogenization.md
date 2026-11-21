# CBRC F7 Driver r444 — multiplicative Følner homogenization and the exact role of ray marks

Date: 2026-11-21 (+08:00). New auxiliary theorem developed in the continuing Driver scientific line `EM-DVR-DEBB5E`; original F7 mixing matrix, task and frozen author's contribution remain `EM-CBRCF7-83A1D4` / `RR-AA38973D56330E59D315`. This note is **not** a Native Review, accepted Result, Task completion or change to P000.

## Original precise setting

Use the exact original rank-one integral involution
[
A=I+uv^T,quad u=(1,1,-1,-1)^T,quad v=(1,-2,-1,2)^T,quad A^2=I.
]
For a scalar `q: Z^2 -> R_{>=0}`, define
[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4),qquad E(q)=sup_{zin Z^4}|D_q(z)|.
]
The original admissible class `Q` consists of `q(0,0)=0`; `q(x,y)=q(-x,y)` (the original J-evenness); `q(t,0)=1` for all nonzero integers `t`; `q(x,y)>=1/2` on all nonzero integer pairs; and the **two marks at their originally fixed scale** `q(2,1)=q(-1,-1)=1/2`. No integer-dilation homogeneity or upper cap is assumed.

If `E(q)<=epsilon<infinity`, the already proved old-axis identity (r441, r443)
`A(a-b,0,a-2b,0)=(a,b,a-3b,-b)`
implies `q(x,y)<=3/2+epsilon` when `y!=0`. Thus every finite-defect `q` in the original class is globally bounded by `M=3/2+epsilon`, including the fixed axis and origin.

## Theorem 1 — defect-nonincreasing homogeneous dilation limit, with precise mark caveat

For every `q in Q` with `E(q)<=epsilon<infinity`, there exists a scalar `h:Z^2->[0,M]` such that:

1. `h(0,0)=0`, `h(x,y)=h(-x,y)`, `h(t,0)=1` for all `t!=0`, and `h(x,y)>=1/2` on nonzero pairs.
2. `h(kx,ky)=h(x,y)` **for all positive integers k** and all integer pairs.
3. `E(h)<=E(q)<=epsilon`.
4. The original two **fixed-scale marks are not asserted** for `h` without the additional hypothesis in Theorem 2.

This is a theorem about the exact original `A` and scalar defect, not a replacement of its matrix or scalar domain.

### Constructive averaging and complete proof

For each `N>=2`, let `P_N` be the primes `p<=N` and form the finite multiplicative Følner set
[
S_N={prod_{pin P_N}p^{a_p}: a_p=0,1,ldots,N-1},qquad |S_N|=N^{|P_N|}.
]
Define the finite averaged scalar
[
q_N(w)=rac1{|S_N|}sum_{sin S_N}q(sw),qquad win Z^2.
]
Each `q_N` retains the origin, J-parity, old axis, positive floor, and global cap because each summand does. Integer linearity of `A` gives the **exact identity**
[
D_{q_N}(z)=rac1{|S_N|}sum_{sin S_N}D_q(sz)
]
and consequently `E(q_N)<=E(q)` for every `N`.

Fix a positive integer `k=prod_{p|k}p^{b_p}`. For all sufficiently large `N`, the two sets `S_N` and `kS_N` have the same cardinality, and the proportion of their overlap is exactly
[
rac{|S_Ncap kS_N|}{|S_N|}
=prod_{p|k}left(1-rac{b_p}{N}ight).
]
Every scalar summand lies in `[0,M]`, hence comparison of the uniform counting measures yields, **uniformly for every integer pair w**,
[
|q_N(kw)-q_N(w)|
le Mleft(1-prod_{p|k}(1-b_p/N)ight)
le rac{M}{N}sum_{p|k}b_plongrightarrow0. 	ag{H1}
]
(The estimate uses exactly matched points in the overlap; the unmatched portions have equal mass and scalar values in `[0,M]`.)

Since `Z^2` is countable and all `q_N(w)` lie in the compact real interval `[0,M]`, a diagonal subsequence `N_j->infinity` converges pointwise to some `h`. Fixed coordinate conditions survive limits, and (H1) for each fixed `k,w` implies `h(kw)=h(w)`. For any fixed `z`, its defect uses four scalar coordinates, so continuity gives `|D_h(z)|<=E(q)`. Taking the supremum proves Theorem 1.

## Theorem 2 — eventual ray marks suffice, and class-optimal equality

Define `Q_tail` as the subclass of original `Q` for which there is a finite `K` (depending on `q`) such that, for every integer `k>=K`,
[
q(2k,k)=q(-k,-k)=1/2. 	ag{M_tail}
]
Define `Q_hom` as the subclass of original `Q` invariant under every positive integer dilation `q(kw)=q(w)`. Note that `Q_hom subset Q_tail subset Q` and the r435 signed-angular construction is an explicit finite-defect member of `Q_hom`.

**Claim:** In `Q_tail`, the homogeneous scalar in Theorem 1 can be chosen to retain **both exact marks**, and
[
oxed{inf_{qin Q_{m tail}}E(q)=min_{hin Q_{m hom}}E(h).} 	ag{H2}
]
The common optimum exists and belongs to `[1/2,4/7]`; this theorem does **not** determine its numerical value or the unrestricted original optimum `inf_{qin Q}E(q)`.

**Proof of retained marks.** For `w=(2,1)` or `w=(-1,-1)`, all sufficiently large `s` have `q(sw)=1/2`. Only finitely many elements of `S_N` can violate this condition. Since `|S_N|->infinity`,
[
0le q_N(w)-1/2
le (M-1/2)rac{K-1}{|S_N|}longrightarrow0.
]
Thus `h(2,1)=h(-1,-1)=1/2`, so `h in Q_hom`. Every finite-defect element of `Q_tail` therefore has a homogeneous counterpart with no larger defect. The reverse infimum inequality is immediate from `Q_hom subset Q_tail`, proving equality of infima.

**Attainment.** The r435 homogeneous scalar provides a nonempty comparison class and a uniform finite upper bound `4/7`. Take a minimizing sequence in `Q_hom`; the r441 axis coercivity bound supplies a common upper cap `3/2+4/7+o(1)`. A diagonal limit preserves the closed coordinate conditions, both marks, and exact homogeneity, while each defect inequality passes to the limit. The limit attains the common infimum. (Equivalently one may first homogenize any bounded minimizing sequence by the procedure above.)

**Useful extension.** Condition (M_tail) may be weakened to
[
|S_N|^{-1}sum_{sin S_N}|q(sw)-1/2|	o0
quad	ext{for } win{(2,1),(-1,-1)}.
]
The same proof retains the marks. This is an explicit asymptotic condition on the two marked rays; it is not silently assumed for every original `q`.

## Consequence for F7 continuation

Under the extra eventually-all-scale mark condition, allowing arbitrary dependence on integer scale cannot lower the optimal global defect below the best homogeneous scalar: averaging removes scale dependence without increasing error. **For the actual original F7 task, marks are specified only at k=1; the averaging can lose them**, so (H2) does not prove that the unrestricted optimum is homogeneous, or that its lower bound is `4/7`. If one later establishes an unrestricted optimum strictly below the homogeneous optimum, every improving scalar necessarily violates eventual marking on at least one marked ray at infinitely many scales. This conditional conclusion clarifies why r443's nonlocal tail requirement and r441's compactness are compatible.

### Evidence and provenance

- Original F7 author and immutable target: `EM-CBRCF7-83A1D4`, `RR-AA38973D56330E59D315`; original Task `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`.
- Exact old-axis coercivity and global compactness: Driver r441, commit `82027a566a0b9b84069fba9a4d3616027a3b4660`.
- Universal axis-scale pairing and extremal tail: Driver r443, commit `f5724a080c363dd941da69a7d301aff2479fb69f`.
- Original exact homogeneous comparison construction with defect `4/7`: Driver r435, commit `80bc36253e1e4b5210dc665206a6f2bff746157c`.
- The present theorem uses elementary finite integer averaging, boundedness and diagonal compactness; no formal checker, computer enumeration or new axiom is claimed. The original Native Review, frozen Result manifest discrepancies, Activity association, Task completion and parent objective closure remain separate unresolved control matters.

Next discriminating scientific action: evaluate whether any feasible original fixed-scale-mark scalar necessarily has positive-density tail marking, or construct a genuinely nonhomogeneous candidate exploiting infinitely many unmarked dilation points; compare against exact finite-cube minimax certificates.