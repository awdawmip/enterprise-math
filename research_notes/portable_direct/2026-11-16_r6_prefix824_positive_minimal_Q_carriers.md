# PREFIX-824 — Nonnegative integer future-count carriers at the exact observable rank

Date: 2026-11-16 (Asia/Shanghai). Route: independent portable TASK_RESEARCH mathematical auxiliary result, following PREFIX-823. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. This is a typed BRC positive-branch **count** system and its Q-only cardinality observer. No native X6 Cell/Link/Port admission, event-time law, phase cancellation, or physics is asserted.

## 1. Exact scope and notation

Fix capacity q≥1, an insertion multiplicity a∈Z_{>0}, a marked source 0, and any finite set of **named** unmarked sources i with positive integer removal multiplicities β_i. States are subsets S of these names, |S|≤q. R removes an unmarked member i with multiplicity β_i; if 0 is present, R removes it with multiplicity b≥0. A adds 0 with multiplicity a if absent and capacity permits. The sole accessible future operator is Q=R+A. For initial nonnegative integer mass μ on named subsets, C_l μ is the total mass at cardinality l (0≤l≤q). All operators are integer, nonnegative, linear count maps. We investigate minimal **rational-linear** exact carriers, and construct nonnegative integer carriers attaining those dimensions in stated regimes.

Let U[k,h] and V[k,h] be the conditional elementary-symmetric moments of unmarked-source weights: U for marked absent with k unmarked sources, V for marked present with k; 0≤h≤k≤q (U), or k≤q−1 (V). For zero or absent indices use 0. As in PREFIX-822/823:
\[
(QU)_{k,h}=(h+1)U_{k+1,h+1}+bV_{k,h},\qquad
(QV)_{k,h}=(h+1)V_{k+1,h+1}+aU_{k,h},\qquad
(CM)_l=U_{l,0}+V_{l-1,0}.
\]
There are (q+1)^2 conditional moments. The named-state-to-moment map has full rational row rank when at least q+1 unmarked weights are pairwise distinct, by the subset-polynomial argument reproduced below.

## 2. Theorem 824.1: all capacities, singular marked-removal regime b=0

Set b=0 and define the integer-valued **future-output coordinates**
\[
z_{l,j}(\mu):=C_lQ^j\mu.
\]
Retain precisely the following index set:
\[
I_q=\{(0,j):0\le j\le q\}
\;\cup\;
\{(l,j):1\le l\le q,\ 0\le j\le q-l+2\}
\setminus\{(1,q),(1,q+1)\}.
\]
It has size
\[
D_0(q)=|I_q|=\frac{(q+1)(q+2)}2+2q-2.
\]
All coordinates are nonnegative integers for nonnegative integer initial mass. Their **exact linear update** under one Q step uses only nonnegative integer coefficients:
\[
z'_{0,j}=\begin{cases}z_{0,j+1}&j<q\\0&j=q,\end{cases}
\]
\[
z'_{1,j}=\begin{cases}z_{1,j+1}&j<q-1\\a q\,z_{0,q-1}&j=q-1,\end{cases}
\]
\[
z'_{l,j}=\begin{cases}z_{l,j+1}&j<q-l+2\\0&j=q-l+2,\end{cases}\quad 2\le l\le q.
\]
The current output is simply (z_{0,0},z_{1,0},…,z_{q,0}). These updates preserve **every finite future Q-only cardinality histogram**. If q+1 unmarked sources have pairwise distinct positive β_i, this is a **minimal-dimensional rational-linear exact carrier**, implemented with nonnegative integer coordinates and a nonnegative integer update matrix.

### Proof, sufficiency and positivity

For b=0 the marked source, once inserted, stays present. Every nonzero path contains at most q unmarked removals and at most one insertion, so Q^{q+2}=0. Counting the possible positions of that single insertion (capacity blocking the very first insertion when the source subset is full) gives:
\[
C_1Q^{q}=aq\,C_0Q^{q-1},\qquad C_1Q^{q+1}=aq\,C_0Q^{q}.
\]
Equivalently, using the conditional moments,
\[
z_{1,q}=a q!\,U_{q-1,q-1}=aq\,z_{0,q-1},\qquad
z_{1,q+1}=a q\,q!\,U_{q,q}=aq\,z_{0,q}.
\]
Every other nonzero coordinate C_lQ^j is retained in I_q. Since z_{l,j}(Q\mu)=z_{l,j+1}(\mu), ordinary rows shift by one; when the shift reaches the only deleted intermediate row z_{1,q}, the first identity above supplies the displayed positive update. Boundary rows shift to zero by finite nilpotence. Hence the update is exact at every step, and all coordinates and coefficients are nonnegative integers.

### Proof, minimal rational-linear dimension

The exact conditional-moment expansion follows from the removal combinatorics. For each 1≤l≤q and 0≤j≤q−l, the output row y_{l,j}:=C_lQ^j contains the conditional coordinate V_{l+j-1,j} with nonzero coefficient j!, and **no other** output row contains that V-coordinate: a state initially marked present can undergo only unmarked removals, and ending at cardinality l after j operations requires precisely j removals. These q(q+1)/2 rows are independent.

The remaining nonzero rows are y_{0,j} (0≤j≤q) and two high rows y_{l,q-l+1}, y_{l,q-l+2} per l≥1. The high rows are:
\[
y_{l,q-l+1}=a(q-l+1)!\,U_{q-1,q-l},\quad
y_{l,q-l+2}=a(q-l+1)(q-l+1)!\,U_{q,q-l+1}.
\]
The diagonal rows are y_{0,j}=j!\,U_{j,j}. Among these, exactly the two identities displayed above repeat a coordinate (at l=1); deleting y_{1,q} and y_{1,q+1} leaves distinct U-pivots. Therefore the selected |I_q| rows are rational-linearly independent and span all output rows. The observable row-space rank is D_0(q).

To realize that rank on **actual named states**, choose for each k≤q a set of k+1 unmarked weights with distinct β. The k+1 polynomials \(\prod_{i\ne j}(1+\beta_i t)\) from the k-subsets obtained by omitting one j are independent: evaluate at t=−1/β_j to isolate the omitted-j polynomial. This proves surjectivity onto each U/V moment block and hence onto the entire conditional-moment space over Q. Thus an arbitrary rational-linear carrier for all Q-only outputs requires at least D_0(q) dimensions. Our nonnegative integer update attains it. QED.

The theorem is about carrier dimension and exact count preservation. It does not claim that its coordinates are minimal as an arbitrary nonlinear encoding or that preprocessing a named mass to all z-coordinates is free.

## 3. Theorem 824.2: positive marked-removal b>0, explicit q=1 and q=2 minimal positive carriers

For arbitrary integers a,b>0 and positive unmarked β_i, the following exact nonnegative integer carriers attain the minimal rational-linear Q-only rank proved in PREFIX-823.

### Capacity q=1: three nonnegative coordinates

Write u=U_{0,0}, s=U_{1,0}+V_{0,0}, t=U_{1,1}+bV_{0,0}. Then
\[
(u,s,t)\xmapsto{Q}(t,\,a u,\,ab u),\qquad (C_0,C_1)=(u,s).
\]
Every coefficient is a nonnegative integer. When at least two distinct positive unmarked β_i are available, the rational observable rank is 3.

### Capacity q=2: eight nonnegative coordinates

Define
\[
x=(U_{0,0},U_{1,0},U_{1,1},U_{2,2},
V_{0,0},V_{1,1},Z_0,Z_1),
\]
where
\[
Z_0=U_{2,0}+V_{1,0},\qquad Z_1=U_{2,1}+bV_{1,0}.
\]
For shorthand x=(u_0,u_1,u_{11},u_{22},v_0,v_{11},z_0,z_1), the update is
\[
x'=(u_{11}+bv_0,\ z_1,\ 2u_{22}+bv_{11},\ 0,\
v_{11}+a u_0,\ a u_{11},\ a u_1,\ ab u_1),
\]
and the observed histogram is
\[
(C_0,C_1,C_2)=(u_0,u_1+v_0,z_0).
\]
All eight retained coordinates and all update coefficients are nonnegative integers. Direct substitution into the conditional moment identities proves invariance. The corresponding q=2 Q-only rank from PREFIX-823 is (2+1)^2−ceil(2/2)=8, attained on named states with at least three distinct positive unmarked β_i. QED.

The q=2 construction removes a hidden direction by **positive mixing** rather than storing a signed difference. This is a concrete information-preserving reduction for a full future operation language.

## 4. Exact independent named-source checks

File: PREFIX824_R6_POSITIVE_CARRIER_CHECK.py. Results: PREFIX824_R6_POSITIVE_CARRIER_RESULTS.json. The checker enumerates the **named source subsets**, forms R and A directly by weighted branching, evaluates the exact future output rows and carriers, and checks that each displayed update intertwines with the named Q operator on every enumerated basis state. It also checks complete finite-horizon histograms and exact rational ranks, without floating point.

For b=0: capacities q=1,…,6, insertion weights a=1,2,3, unmarked β_i=1,…,q+1, 18 configurations, 1,395 named basis-state checks, 43,581 coordinate-update checks, 75,201 output/dependency checks, and six exact rational-rank calculations. Observed ranks were 3,8,14,21,29,38.

For b>0, q=1 and q=2, a,b∈{1,2,3}: 18 configurations, 135 basis states, 900 coordinate-update checks, 2,070 full-histogram checks and two exact rational-rank calculations. All programmed exact assertions passed. These are finite implementation checks; the stated all-q b=0 result is supported by the proof.

## 5. Remaining research and provenance

Investigate a nonnegative integer carrier at the optimal positive-b Q-only rank (q+1)^2−ceil(q/2) for every q≥3, either by constructive quotient or by an exact obstruction with explicit counterexample and a sharper positive-realization dimension. Test unmarked-source individually addressable operations, which enlarge the declared observation language and may require restoring named-source residuals. Study preprocessing cost and sparse update performance with complete transformation/bit-length accounting.

P000, ACTIVE worldview, declared observer semantics, six native X6 axes, separately ordered time, and named provenance are retained. Word depth is not an asserted heartbeat duration. This positive count model does not implement signed/complex amplitude cancellation.

Scientific predecessors and normative scopes: PREFIX-822, PREFIX-823; awdawmip/enterprise-math at frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d; docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; docs/PORTABLE_RESEARCH_PROTOCOL.md; research_priorities/research_method.json; p000_reality_foundation.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json. Status: AUTHOR_PROVED / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. No shared CLAIM acquired.