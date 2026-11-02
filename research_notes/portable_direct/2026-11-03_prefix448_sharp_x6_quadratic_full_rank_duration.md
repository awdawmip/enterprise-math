# PREFIX-448 — Sharp minimum native-X6 duration for full quadratic history-sector BRC rank

**Date:** 2026-11-03 (Asia/Shanghai). **Parent:** PREFIX-447, GitHub commit 74111b7ac7f0017ef0be88be4383ded05335dc2e. **Immutable scientific input:** awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. **Status:** author-side analytic proof and exact integer certificate; independent review/admission pending.

## Question, carrier, and declared observation language

PREFIX-447 establishes sharp 28q rational-linear quadratic observation dimension on a full native six-axis X6 signed-step family at the explicit duration N=2q+2. This study determines the **least common native word length N** at which the full 28q-dimensional observation can already be realized, for each integer history modulus q>=2.

Fix a chosen native Cell as chart anchor (not a distinguished ontic origin). Each primitive word w has exactly N ordered steps in {+e_i,-e_i:1<=i<=6}, endpoint x(w) in Z^6 relative to the anchor, and auxiliary history sector r(w)=count_w(-e_1) mod q. This history label is not a seventh spatial coordinate. The source is a positive-rational weighted bag of such words, retaining native path provenance. Its sector-labeled quadratic observer is

T_{r,alpha}=sum_{w:r(w)=r} c_w x(w)^alpha, with 0<=r<q and |alpha|<=2.

There are 1+6+6+15=28 monomials of total degree at most two in six chart coordinates. Equivalently, for each sector retain Q_r=sum c_w z_w z_w^T with z_w=(x_1,...,x_6,1). The future operation language is positive-rational alternative and finite history-conditioned affine BRC effect composition x -> A x+b. All algebraic affine effects are typed BRC transport/observation operations; primitive native steps remain single signed-axis steps.

## Theorem 448.1 — sharp first full-rank duration

**For every integer q>=2, the least common length N for which the sector-labeled quadratic observation map has full rational-linear rank 28q on finite positive-rational native X6 word bags is**

N_min(q) = q+1.

**Lower bound.** At any N<=q, examine sector r=q-1. If N<q-1, this sector has no words. If N=q-1, its words necessarily consist of q-1 negative first-axis steps, with a single endpoint. If N=q, the number k of -e_1 steps must equal q-1 (the next possible k=2q-1 exceeds q). The final unused step may be any primitive signed direction except -e_1; there are eleven choices, hence at most eleven distinct endpoints. The sector quadratic evaluation rank is therefore at most eleven, strictly less than twenty-eight. Thus no N<=q attains total rank 28q. The positive rational domain does not alter this linear upper bound.

**Construction at N=q+1.** Build 28 two-step tails, none using -e_1, with endpoints S consisting of:

1. zero, realized by (+e_2,-e_2);
2. +2e_j and -2e_j for j=2,...,6 (10 points);
3. e_i+e_j for 2<=i<j<=6 (10 points);
4. e_1+e_j for j=2,...,6 (5 points);
5. e_1-e_2 (1 point);
6. 2e_1 (1 point).

This is a set of 28 different endpoints with legal length-two words. For each sector r in {0,...,q-1}, prefix every one of these tails with r copies of -e_1 followed by q-1-r copies of +e_1. Every resulting word has length q+1 and sector r, and its endpoint set is the translate S+(q-1-2r)e_1. The q sectors therefore provide 28q distinct valid ordered words.

**Quadratic unisolvence.** Let a degree-at-most-two polynomial P(x)=c+sum a_i x_i+sum b_i x_i^2+sum_{i<j}d_ij x_i x_j vanish at all S. The zero endpoint gives c=0. Evaluation at +/-2e_j for j>=2 gives a_j=b_j=0. Evaluation at e_i+e_j for 2<=i<j gives d_ij=0. Evaluation at e_1+e_2 and e_1-e_2 gives a_1+b_1=0 and d_12=0. Evaluation at e_1+e_j for j=3,...,6 gives d_1j=0. Finally, P(2e_1)=2a_1+4b_1=0 together with a_1+b_1=0 yields a_1=b_1=0. Thus P vanishes identically; the 28-by-28 rational evaluation matrix is invertible.

Translation of all endpoints is an invertible degree-filtration-preserving linear transformation on the 28-dimensional quadratic polynomial space, so every sector has rank 28. Sector coordinates occupy disjoint observer blocks, giving total rank 28q. Positive rational weight vectors contain a relatively open positive orthant, and a nonzero rational row difference can be realized with small positive perturbations of strictly positive weights, so the same rank characterizes the positive-source observer. This proves the result.

**Exact ordered-basis determinant.** For the tails in the certificate order (zero; +/-2e_j; e_i+e_j with i,j>=2; e_1+e_j; e_1-e_2; 2e_1), with columns (1,x_1,...,x_6,x_1^2,...,x_6^2,x_ix_j for i<j), fraction-free Bareiss elimination gives det(V)=-4194304=-2^22. Every translated sector has the same determinant in this ordering. This numerical value is a reproducible exact certificate; the vanishing-polynomial proof above independently establishes invertibility for all q.

## Consequences and comparison with the actual preceding frontier

At q=3, full 84-dimensional quadratic BRC sector observability is realizable with **84 distinct native words of length four**. PREFIX-447 supplied the valid but longer length-eight construction. The new length saves q+1 steps per word (from 2q+2 to q+1) for every q>=2. The 28q observation-coordinate requirement remains unchanged. This is an exact path-duration improvement, not a claim of reduced cost for arbitrary BRC kernels.

The result directly uses the P000 signed X6 cell torsor, the ACTIVE residual/observer preservation stance and the frozen BRC control/effect/moment algebra. The supported scope is finite positive-rational word bags, sector-labeled quadratic observations and the declared affine future-operation language. It does not assign physical heartbeat durations, phase cancellation, final Cell addresses or external Euclidean geometry to the chart-relative constructions.

## Certificate and execution scope

Exact source: accompanying prefix448_sharp_duration_certificate.py. It constructs all 28 tails, computes the 28x28 determinant via integer Bareiss elimination, constructs 28q legal words for q=2,3,4,5,6,8,12, checks each sector rank modulo 1000000007, verifies symmetric homogeneous 7x7 moments, and checks the lower-bound endpoint cap in finite listed cases. The log PREFIX448_EXACT_EXECUTION.log is the actual Python standard-library execution output. General q and the minimum-length conclusion follow from the analytic proof, not extrapolation from finite tests.

Relevant frozen interfaces: src/enterprise_math/brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1; src/enterprise_math/brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91bdb8. **Tool reuse: COMPOSE_APPLIED**, specifically the 7x7 homogeneous MomentState quadratic transport law and sector-conditioned ControlPacket semantics. The certificate executes the exact mathematical word/evaluation/Gram construction independently; upstream class-level direct-import execution is still pending. No new native session/CLAIM/Result/review is asserted: current Site research authority is not granted and owner inquiry returned CONTROL_QUOTA.

## Next independent question (PREFIX-449)

Execute the unchanged frozen upstream ControlPacket.from_edges, then, alternatives, evaluate and moment_action on the 84-word q=3,N=4 witness and verify the native 3x28 moment blocks. Then measure exact serialized size and runtime against a full EffectHistogram at fixed, explicitly stated q,N,weights. Separately ask whether a non-affine future observation requires third-order or provenance repair beyond these 28q quadratic coordinates. Preserve current source pins and true authorization state.
