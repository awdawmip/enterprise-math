# C264 | Final three-free-coordinate hull — author exact proof (2026-10-23)

**Status:** AUTHOR_EXACT / EXTERNAL C195-H168 POSITIVE-RATIONAL AUXILIARY / NO FORMAL CLAIM / NOT DRIVER-ADMITTED. This is a research handoff, **not** a canonical Source Result or Working Truth.

## Fixed provenance

GLOBAL_KNOWLEDGE_V1 canonical main read: \`abed76a9c866347d9c3b3ba2844853229a4e8c22\`.
Enterprise Math source read: \`3102dc08dcc1fe649de542367409bfb98bd77025\`.
Parent: C263 7 positive-hull author package SHA256 \`aa3977915e5de9dba0fff75c092423a7fbd8380534ee7309203e1ffd72879db4\`.

The node list and C254 35-box source are inherited byte-for-byte. This document records a new proof, not independent acceptance of its parent classification.

## Theorem

Let I=(5,50,55,56), J={0,...,78}\I, Q=2^128, H=2^166,
Z=141421356237309504880/10^20, A=6912*50000^2/17^2, with the 79 strictly increasing C195 source rational nodes u_j. Put

B_j=floor[(QA/H)/((2-u_j²)(3-u_j²))³ * product_(r!=j)((Z-u_r)/abs(u_j-u_r))] > 0 for j in J.

Define the exact 79-branch scalar auxiliary F(v) by the sum of (i) fixed branches

B_j * product_(p in I) [((Z-v_p)/(Z-u_p))*(abs(u_j-u_p)/abs(u_j-v_p))]

and (ii) moving branches for k in I,

[(QA/H)/((2-v_k²)(3-v_k²))³] *
product_(j in J)[(Z-u_j)/abs(v_k-u_j)] *
product_(p in I\{k})[(Z-v_p)/abs(v_k-v_p)].

On the entire continuous rectangle

- v_5 in [1/135, 3/205];
- v_50 in [34/49, 12/17];
- v_55 = 4/5;
- v_56 in [57/71, 22/27],

the exact bound is

**F(v) >= 2^128 + 95008155998302734852413916540688525 > 2^128.**

This is a **continuous real-domain** theorem, not a discrete point sample.

## Complete proof mechanism

On every pole-free ordered interval define T_jp(t) = c_jp*(Z-t)/abs(u_j-t), c_jp=abs(u_j-u_p)/(Z-u_p)>0.

For j>p (t<u_j), T'_jp=c_jp*(Z-u_j)/(u_j-t)^2>0 and T''_jp=2*c_jp*(Z-u_j)/(u_j-t)^3>0. For j<p (t>u_j), T'_jp=-c_jp*(Z-u_j)/(t-u_j)^2<0 and T''_jp=2*c_jp*(Z-u_j)/(t-u_j)^3>0. Thus all non-shared fixed-branch coordinates may be reduced to their minimizing endpoints, preserving one common variable across all 75 positive fixed branches. This retained sum is convex in the shared variable.

For each moving branch k, reduce the other active coordinates to their minimizing ordered endpoints e_p: lower for p<k, upper for p>k, giving M_k(t)>0. On each legal interval

(log M_k)'' = 6(2+t²)/(2-t²)^2 + 6(3+t²)/(3-t²)^2 +
sum_(j in J)(t-u_j)^(-2) + sum_(p!=k)(t-e_p)^(-2) >0.

Therefore M_k is strictly convex. A tangent at the rational midpoint s gives the globally valid affine lower bound M_k(t)>=M_k(s)+M'_k(s)*(t-s), minimized at the correct rational endpoint depending on slope.

For a chosen shared k, sum all 75 fixed branches with their k-dependence retained and M_k(t), take its single convex tangent at s; add separate moving-branch tangent bounds for the other 3 branches. This yields an exact **all-points** lower bound LB_k(C) on every closed subbox C. The BASE alternative uses independently minimized positive factors and separate moving-branch tangents. Both are valid lower bounds regardless of how the algorithm chooses among them.

Starting from the stated root, the certificate gives **52 midpoint bisections and 53 closed leaves**. At every split the child closed boxes cover the parent exactly, including all boundaries. Each leaf records its four exact rational bounds, path, chosen method, and floor(LB(C))-Q. All 53 values are positive. The smallest is exactly 95008155998302734852413916540688525. By induction over the bisection tree, the full rectangle satisfies the theorem. Leaf methods: SHARED_5=1, SHARED_50=26, SHARED_56=26.

## Classification gain and important boundary

The inherited eligible pair-hull partition was 363=213 documented F<Q hulls +89 previously proven F>Q hulls +61 unresolved. Exact rational bounding-box dimensional classification finds only ONE three-free-coordinate unresolved hull: pair (10,24). This theorem certifies that one. Hence **363=213+90+60** and **all remaining 60 unresolved eligible hulls have four free coordinates**. Original 35 fundamental certificate leaves remain unchanged.

BRC boundary: positive branch totals discard native phase, sign, label, port and future-operation information. Neither F>Q nor positive branch mass is the native GF(2)-BRC theorem or the proof of an original finite-configuration precision conjecture. Historical complete enumeration of 15,685 candidate inputs was inherited, not rerun. P000 remains unchanged.

## Exact evidence in the C264 handoff package

- Complete full prose: C264_THEOREM_AND_PROOF.zh-CN.md, SHA256 \`5c49351bb4f1fefa9b248f4bdd85e6874819165149fa6d82c3044d886f5ad812\`.
- 53-leaf certificate JSON: SHA256 \`9a34713c94aa164813a87006ea16a57d61a84a2c3cb46ed10cafe60982c8dc87\`.
- Compact 79 nodes / 35-box bounds / legal-negative-positive sets: SHA256 \`dd5940376339e75020b8b094f2b5260252f8ecce5618a4da4df1b4605bcccb97\`.
- Standalone exact Fraction verifier: SHA256 \`7c958ee09a8f134588a722221bb2d5bf38a72aa9e0067399db3cafa94f17ddcb\`.
- Distinct second-author-algorithm cross-check (not an independent Driver): PASS on all 53 leaves; SHA256 \`28df133cd5967bb830184e9925c32bbca58e2a7ead497f3174277e861f4bfd9f\`.

The standalone verification requires only Python standard library + the certificate JSON + compact input JSON, and yields \`C264_STANDALONE_EXACT_VERIFY_PASS\`. The full C263 parent ZIP is preserved unchanged inside the local handoff archive. Checkpoint/source publication remains unclaimed.

**Next exact question:** On the (0,16)=(0,28) four-coordinate outer hull, covering 25 still-unclassified pairs, develop a joint two-shared-variable rational Hessian/tangent lower bound or supply an exact rational F<Q witness. Do not mistake float Hessian samples for a global certificate.