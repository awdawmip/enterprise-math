# X6 Unit187 — Exact weighted-field native-horizon fibers and residual reconstruction

Date: 2026-11-20. Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Research lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane excluded. Author status: AUTHOR_PROVED / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED. This note is separate from native PROGRESS, Result, Driver review and P000 admission.

**Source pins.** Frozen signed-X6 science: awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md (blob b4d49a1bbcccad0521618c6d20f6dcfa242b420a). Historical genuine A3 producer: awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/weighted_relation_field.py (blob e50bf991e4dc4280063556a7aad1028f9f9404ed); functions weighted_relation_field at line 71, recover_totals_from_weighted_field at line 113, integer numerator at line 130. Its actual test caller tests/test_weighted_relation_field.py (blob 51748dfe340c385907c4f2218fa1ae5ae2260522). This is a new, explicitly typed X6-to-A3 mathematical adapter, not an assertion of an existing production import. Unit182–186 equal-unit-capacity and relative-depth results are consumed without re-originating them. Original R063 native benchmark is already complete and was not rerun.

## Theorem 1 — true integer kernel and constructive source-only representative

For six positive integer capacities m=(m_1,...,m_6), let g=gcd(m), v=m/g (primitive positive integer vector), Q=sum(v_i). For any signed native coordinate z in Z^6 the real frozen A3 producer yields Z_ij=m_j z_i-m_i z_j. Then

\[
\boxed{F_m(z)=F_m(z')\iff z'=z+t v\text{ for a unique }t\in\mathbb Z.}
\]

Given the *actually generated* field Z and capacities m, choose any integer Bézout coefficients u with sum(u_j m_j)=g. The following formula uses **only (m,Z)**:

\[
\boxed{z^0_i=g^{-1}\sum_j u_j Z_{ij}.}
\]

Each z^0_i is an integer, F_m(z^0)=Z, and all compatible integer endpoints are exactly z^0+t v. Proof: equal field values give m_j(z_i-z'_i)=m_i(z_j-z'_j), so their difference is a rational scalar times primitive v; Bézout forces that scalar integer. Expanding the displayed sum for a generated field gives z^0_i=z_i-v_i\sum_j u_j z_j, establishing the explicit integral representative and its complete fiber.

## Theorem 2 — exact finite-horizon inversion, including parity holes

At length M>=0 of the specified twelve signed six-axis primitive events from an anchor zero, a native endpoint x is reachable **iff** its L1 norm is <=M and M-sum_i x_i is even (shortest path plus backtracking pairs). For each of the 64 sign vectors sigma in {-1,+1}^6 define s_sigma=sum_i sigma_i v_i and b_sigma=sum_i sigma_i z^0_i. Require b_sigma<=M for every zero slope. If any fails, the fiber is empty. Otherwise define

\[
L=\max_{s_\sigma<0}\left\lceil\frac{M-b_\sigma}{s_\sigma}\right\rceil,\qquad
U=\min_{s_\sigma>0}\left\lfloor\frac{M-b_\sigma}{s_\sigma}\right\rfloor.
\]

Both slope sets are nonempty. The **complete** parameter set of endpoints consistent with (m,Z,M) is

\[
\boxed{\{t\in\mathbb Z:L\le t\le U,\quad Qt\equiv M-\sum_i z^0_i\pmod 2\}.}
\]

Proof: the exact identity ||z^0+tv||_1=max_sigma(b_sigma+s_sigma t) makes the 64 affine inequalities equivalent to norm feasibility, and the congruence is exactly native step parity. If Q is even, compatible parity admits every integer in [L,U] (or none); if Q is odd, only one parity class of t is allowed, so the fiber is a step-2 arithmetic progression. Thus the earlier interval-only theorem for six equal unit capacities (Q=6) is a proper special case.

Let p=1 for compatible even Q and p=2 for odd Q. Let t0 be the first allowed integer >=L, and K=max(0,1+floor((U-t0)/p)), or 0 if parity fails. Then the endpoints are precisely z^0+(t0+pj)v, 0<=j<K. This is a finite 64-inequality exact integer algorithm (no search over depths), with polynomial bit cost in the capacities, field and M. It makes no fixed-time bit cost or native runtime-speedup claim.

## Theorem 3 — minimal missing state for the *actual* absolute-total consumer

The historical consumer recovers each block total using T=sum_i m_i, row R_i=sum_j Z_ij, and z_i=(m_i C+R_i)/T from compatible grand total C. On the exact fiber,

\[
\boxed{C(t)=\sum_i z^0_i+Qt.}
\]

Since Q>0, different feasible endpoints have distinct totals. Given (m,Z,M), the rank j is sufficient to reconstruct C and invoke the genuine source formula to recover the exact signed native endpoint. If K>=1, \(\lceil\log_2 K\rceil\) additional fixed-width bits are both necessary and sufficient **for this particular observed fiber**. The ordering and j are independent of the selected Bézout representative because changing z^0 by kv shifts every t equally. This is endpoint, not full history or arbitrary weighted dynamics, recovery.

## Discriminating witness and observer typing

Take nonuniform m=v=(1,2,1,1,1,1), Q=7, source field Z=0. At M=7 the only compatible lifts are t=-1,+1: native endpoints -v,+v, each with 7!/2!=2520 shortest signed-axis words, giving 5040 field-aggregated words. t=0 is norm-feasible but parity-inadmissible. At M=14, admissible t are -2,0,2. This is a genuine arithmetic hole, not numerical noise or a failure of the source.

The R061 diagonal observer q(z)=z-min(z)1 and the weighted-field observer have different kernels for nonconstant m: q(0)=q(1) but F_m(0) differs from F_m(1); F_m(0)=F_m(v)=0 yet q(0) differs from q(v). Indeed F_m(z+k1)=F_m(z) for all z,k **iff all m_i are equal**. Retain these typed distinct observers instead of applying the earlier equal-capacity rank formula to arbitrary capacities.

## Independent executable evidence and remaining parent task

A standalone Python check used eight capacity vectors, 2237 native signed input states per vector, and three horizon offsets: 53,688 exact field/horizon comparisons of a 64-sign affine method against an independently enumerated norm/parity method. It verified 17,896 Bézout representatives constructed solely from field values, compared full endpoint sets, and checked 66,328 source-formula grand-total recoveries. Violations=0. Python normal, -O and -OO runs gave byte-identical JSON. The source was independently reimplemented, **not directly imported**, and a production native R063 benchmark was not substituted.

Pending parent obligations: LP011/LP019 original suspected error paths still need true offending commit:path:line and typed consumers; historic Native Units149–152, author Units175 onward, and independent Driver review remain unresolved as separately identified tasks. The preceding native authenticated research frontier was Unit174; this author source note does not alter it.

**Next exact scientific step:** test the *actual frozen* coarsen_weighted_relation_field / merge_weighted_relation_field consumer for its additional kernel when six native coordinates are partitioned, and classify how much of the fine field plus ranked endpoint must survive that coarsening. Preserve source and role boundaries.