# PREFIX-533 — Exact rooted BRC–gate observer fibers: 26 classes

Date: 2026-11-06 (Asia/Shanghai). Research line: `RS-X6-NATIVE-ROTATION-DYNAMICS`.
Frozen **scientific** input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Precursors: PREFIX-525 (endpoint BRC), PREFIX-530 (rank-one 49-coordinate realization), PREFIX-532 (18 fixed-origin gate-only classes).
Result status: **AUTHOR_PROVED / EXACT_SPARSE_POLYNOMIAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Question and observer
For the native, ordered, labeled two-branch paths of the four-STAR X6 candidate, classify the 48 fixed initial directed phases by their entire future **joint histogram** of `aAc` gate count and first-axis BRC signed-step cancellation count. This is a smaller explicitly declared observer than whole-path provenance or full six-axis data; source paths remain native six-axis paths. No interpretation as physical time, force, or a proved general rotation law is asserted.

The four STAR supports are
`A={L1,L3,L6}, B={L1,L4,L5}, C={L2,L3,L5}, D={L2,L4,L6}`.
A phase is `s=(j,p,c)` with `p,c` distinct, opposite-signed members of STAR `j`. From `s`, exactly three successor phases are allowed: one continuing in the same STAR and two in the unique other STAR containing `|c|`. Each phase edge has two labeled microstep words, `INNER=(-c,c')` and `OUTER=(c',-c)`. The target is `T=(A,+L1,-L3)`; a gate occurs on an edge ending in `T` exactly when that edge and its immediately preceding edge both carry INNER. Retain branch multiplicity.

For a path `w` of `d` macroedges from `s`, let `H(w)` be its number of gates and `p_1(w)=min(N_1^+(w),N_1^-(w))` its first-axis BRC cancellation pairs. The rooted observer is
```math
P_s(t,q,z)=\sum_{d\ge0}t^d\sum_{w:\,|w|=d,\,w_0=s}q^{p_1(w)}z^{H(w)}.
```
Two roots are equivalent precisely if these formal power series are equal in `Q[q,z][[t]]`.

## Theorem — exactly 26 rooted joint observer laws

The 48 rooted joint distributions split into **exactly 26 equivalence classes**, comprising **eight singletons, sixteen pairs, and two four-element classes**.

The partition of roots by their joint coefficient polynomials through length `d` has size:
`d=0:1; d=1:1; d=2:3; d=3:14; d=4:22; d=5:26;`
and remains **26** for every length `6 <= d <= 48`.
These computations prove the infinite-length classification by the finite-dimensional bound below, not by extrapolation.

The gate-only observer `P_s(t,1,z)` has exactly 18 classes (PREFIX-532). Therefore retaining the typed first-axis BRC cancellation histogram strictly refines that quotient, producing eight additional distinguishable observer classes.

### Proof: 49 exact coefficients suffice
Use a formal variable `v` with `q=v^2`; all calculations take place in the Laurent polynomial ring `Z[v,v^{-1},z]`. Define the current-axis sign observable
`sigma_1(r)=sign(c_r)` if `|c_r|=L1`, otherwise 0, and the flag `b(r)=1_{|c_r|=L1}`. On each phase transition `r -> u`, give its phase edge weight `v^{b(r)+b(u)}`, denoted by `W_{u,r}`. There is one phase edge per legal successor.

For the phase-resolved joint gate/axis-visit count, PREFIX-530 establishes the exact `49 x 49` one-step linear realization
```math
M(v,z)=\begin{pmatrix}2W &(z-1)e_T\\ e_T^TW^2 &0\end{pmatrix}.
```
At depth `d`, the starting state is `(e_s,0)`. Endpoint BRC cancellation is recovered from the axis-visit count `K_1` using the **exact signed X6 identity**
```math
p_1=\frac{K_1-|\sigma_1(r)-\sigma_1(s)|}{2}.
```
Therefore, for each initial sign `a in {-1,0,1}`, let `L_a(v)` be the terminal row with entry `v^{-|sigma_1(r)-a|}` on each of the 48 phase coordinates and 0 on the extra coordinate. Then
```math
[t^d]P_s(t,v^2,z)=L_{\sigma_1(s)}(v)\,M(v,z)^d(e_s,0).
```
This identity is exact for every finite `d`; powers of `v` in this particular scalar output are nonnegative even integers.

Cayley–Hamilton for the common 49-dimensional matrix gives a **single degree-49 characteristic recurrence** in `d` over `Q(v,z)`. Every scalar rooted output satisfies this same recurrence, regardless of its terminal row. Hence the difference between any two rooted output sequences vanishes at *all* depths if and only if it vanishes at depths `0,...,48`. This includes roots with different initial sign, because they use the same matrix.

The accompanying certificate builds the 48 phases and legal edges deterministically, computes each of the 49 initial coefficient polynomials exactly by three backwards row recursions (one for each initial axis sign), compares full sparse Laurent polynomials without floating-point arithmetic, and produces the exact class histogram above. This is a fully finite certificate for the asserted infinite formal-series partition. QED.

### Explicit information-loss witness at just two macroedges
Two roots `s=(A,+L6,-L3)` and `s'=(A,+L1,-L6)` lie in the *same* PREFIX-532 gate-only class, hence have equal gate-only distributions at every length. At length `d=2`, both have `H=0` for all 36 labeled paths, but their exact first-axis BRC histograms differ:
```
                p1=0      p1=1
(A,+L6,-L3)     24        12
(A,+L1,-L6)     36         0
```
Thus the coarse gate-only fiber contains genuinely distinct joint BRC–gate behavior. This provides a short, source-preserving counterexample to using the 18-class gate quotient as a sufficient statistic for the joint observer.

## Exact computation / independent verification
`PREFIX533_exact_certificate.py` is a standalone Python integer/sparse-polynomial certificate with no external dependencies. It checks all 49 depths (0..48) for all 48 roots; coefficient equality uses exact integer dictionaries keyed by `(v-exponent,z-exponent)`. It additionally independently generates native forward branch-labeled histories by integer dynamic programming for all 48 roots and lengths 0..7, checking **1131 distinct rooted histogram coefficients** against the backward linear calculation. All totals equal `6^d` for each root and all final powers are `v^{2p}` with nonnegative integral `p`.

Run: `python PREFIX533_exact_certificate.py`. It writes `PREFIX533_EXACT_EXECUTION.json` and reports `ALL_CHECKS_PASS` when each exact assertion holds. Its persisted JSON contains every class's phase members, the entire length-by-length class count, witness counts, the frozen input pin, and the explicit continuation question.

The finite run validates this executable construction; the all-length extension is justified by the stated 49-dimensional Cayley–Hamilton argument, not an empirical extrapolation. Computer-assisted classification has not been independently reviewed.

## BRC scope and future operation
Carrier: signed, ordered native X6 branch-labeled paths with multiplicity. The observation is the two-variable rooted count histogram `(p_1,H)`; the future-operation horizon is **all legal continuations before final observation**. The 26-class equality concerns aggregate future path-count distributions, **not** deterministic path-by-path successor state merging, native cell address, other five axes, or unrestricted six-axis BRC. The native original path is retained for any wider observation.

## Smallest next unresolved unit
Determine the minimum common scalar recurrence denominator (or minimal rooted linear representation) for the full `P_s(t,q,z)` family, and compare exact coefficient-generation bit costs with the 49-dimensional linear lift and 51-state deterministic online transducer. A feasible first test is symbolic denominator/gcd calculation for one representative of each of the 26 classes. Preserve the frozen scientific pin and source identity/claim separation.
