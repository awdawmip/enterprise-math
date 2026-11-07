# D25/LIFT arbitrary-rank signed Frobenius first-jet quotient — 2026-10-28

**AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** This is an exact **auxiliary matrix-ring theorem**, not a native H0/B0 calculation or LIFT transfer. Reuses earlier same-author rank-one work, not an independent reviewer or new native researcher identity. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Theorem (all odd p, any matrix rank r>=1)

Let R=(Z/p²Z)[T]/(T²-2), sigma(T)=-T. Let sigma act coefficientwise on R^r and F_(A,B)=(I_r+p(A+TB))sigma for A,B in M_r(F_p), lifted arbitrarily.

(1) Exact square: F_(A,B)²=I_r+2pA (mod p²). For each fixed square, A is uniquely determined and there are **p^(r²)** distinct *source-marked* odd matrices B; all reduce to the same sigma modulo p.

(2) For each first-congruence gauge U=I+p(C+TD), exact semilinear conjugation gives U F_(A,B) U^-1 = F_(A,B+2D). Thus the full first-congruence gauge group has **one unmarked orbit** per fixed-square fiber: marked B itself is not gauge invariant.

(3) For an arbitrary admissible subgroup H of G1=1+pM_r(R), let L(H)={2D: I+p(C+TD) belongs to H}. This is an F_p-linear subspace of M_r(F_p). If d=dim_Fp L(H), there are exactly **p^(r²-d) H-orbits**, each with p^d distinct marked B's. The complete invariant is the coset B+L(H). For diagonal H, d=r and the r(r-1) off-diagonal entries are a complete invariant; for scalar H, d=1; for full G1, d=r²; for the identity-only gauge, d=0.

## Proof (complete)

Because p²=0 in Z/p² and sigma²=1, products with two p factors vanish, regardless of matrix noncommutativity. Hence F²=(I+p(A+TB))(I+p(A-TB))=I+2pA. Equality of squares gives 2(A-A')=0 in F_p; 2 is invertible and A=A'. Every B gives a distinct multiplier I+p(A+TB). This proves (1).

Writing Y=C+TD, the inverse of U=I+pY is I-pY and sigma(U^-1)=I-p sigma(Y). Semilinear conjugation gives
U F U^-1=(I+pY)(I+pX)(I-p sigma(Y))sigma=[I+p(X+Y-sigma(Y))]sigma.
Since Y-sigma(Y)=2TD, the action is exactly B→B+2D. Any two B's are connected under full gauge by D=(B'-B)/2. This proves (2).

The group law (I+pY)(I+pZ)=I+p(Y+Z) makes G1 an elementary abelian p-group. Hence every subgroup H and its odd-shift image L(H) are F_p-vector subspaces. Its translation action on B has orbit size |L(H)|=p^d and quotient size p^(r²-d); the invariant is exactly the additive coset. Diagonal and scalar cases follow by their corresponding D subspaces. This proves (3), with no unproved native rank-one or split/non-split assumption.

## Fully explicit p=373, r=2 signed witness

Let E12=[[0,1],[0,0]] and work modulo 373²=139129. Set F0=sigma and F1=(I+373T E12)sigma. Both have F²=I and identical mod-373 reductions, while their marked signed (1,2)-odd coefficients are respectively 0 and 1. They **cannot** be conjugate under diagonal gauges, which never alter B12; they **are** conjugate under full gauge by U=I+373·187 T E12, since 2·187=374=1 modulo 373. This is a precise auxiliary model witness and **not** a contradiction or native experiment for H0/B0.

## BRC / original-observer gate and evidence

Source: the declared auxiliary finite coefficient ring and fixed basis. Future operations: square F², and actual allowed H-conjugation. Readout: marked B or the quotient B+L(H). This is a typed residual-information result; it is **not** an independent lower-dimensional native spatial world. P000's six-dimensional discrete Heartbeat World plus separately typed time remains fixed. There is no original X6 state embedding/readout or source-preserving operator map in this proof.

Authentic original-class H0/B0 rank, Frobenius and permitted gauge group, original fixed CM normalization, [X]U modulo p², odd Hesse/Green observer, kappa and Delta_p-R_p remain **PENDING_OWNER / NOT_RUN** at issue #1559. The native executor must supply these before testing the quotient criterion, not force rank one or substitute this p373 auxiliary witness. The original four-file UR V2 bundle (historically 94687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remains to recover as original bytes and writer provenance, not to reprove.

Author-side exact Python standard-library checker executed locally: 540 actual pair-ring matrix-square/gauge cases for p={3,5,7,13,19,37,373}, r=1,2,3; 3107 exhaustively visited rank-two odd matrices for p=3,5,7 with full-gauge representatives; complete diagonal/scalar gauge quotient counts; exact p373 matrix witness. A shorter independently coded check under the **same author's context**, not an independent mathematical reviewer, passed another 162 matrix operations with exhaustive counts (p=3:81/9/27; p=5:625/25/125; p=7:2401/49/343 marked/diagonal/scalar orbit counts). These finite checks are author evidence, the general proof is the algebra above. Local executable sources and full row-wise JSON are available in this conversation's 2026-10-28 D25 artifact set; this GitHub proof is an author preservation, not Source checkpoint, Result freeze, or review.

## Source/provenance continuation

Gateway 0.6.11 currently has no Site research execution binding; quota active 5/5; own checkpoint ACCESS_DENIED; previous original request receipts CONTROL_REQUEST_NOT_FOUND. No own winning CLAIM/OPEN/run or Source continuation seed was verified; do not replay refused mutations. If a canonical seed says CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, fully read input_artifacts and use completed_units=[] before lawful typed continuation_prepare. Existing Draft PR preservation does not change native ownership. Next exact science: issue #1559 native owner must provide original H0/B0 ring/rank/semilinear direction/allowed H and signed source readout, then prove/refute source-preserving transfer to Delta_p-R_p. No schedule, notification, worldview or frozen pin changes.
