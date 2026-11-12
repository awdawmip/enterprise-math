# R753 — Unique even-sign gauge transport between V1R sampled T^4 and R748 C3

Date 2026-11-12. Parent RS-X6-TRIADIC-CLOSURE-DYNAMICS. Original Run RUN-aea48b2b684b1204bf7fd828, generation 2, checkpoint revision 6 before this update. Researcher EM-X6-BD7DE5, CLAIM MCP-aa543cb564e2a231d3fe6017. Frozen P000 @a72226e2430ffa4786321ac86e7f0c599d5f0389.
Status: exact author-side conditional transport theorem and exhaustive checker; NO native coupled Cell/Link/Port event permission.

R752 proved that the direct source-preserving identification of V1R T^4 with R748 C^2 works only on 240 homogeneous-sign frames. Here the remaining 720 mixed-sign frames are not discarded or declared impossible; a unique, explicitly recorded sign-gauge transport restores an exact twisted relation.

Let p=((a0,s0),(a1,s1),(a2,s2)) be a signed-Port ordered triple with distinct axes. R748 C^2(p)=((a2,s2),(a0,s0),(a1,s1)). V1R T^4 changes the frame to ((a2,s0),(a0,s1),(a1,s2)) at fixed mode.

Define target-slot sign gauge g(p)=(s0*s2,s1*s0,s2*s1), acting on C^2(p) by multiplying the three target signs. Then
    T^4_port(p)=g(p) · C^2(p)
for all 960 frames.

**Theorem 1 (uniqueness and parity):** This is the unique slotwise sign-gauge transformation matching the two exact triples, because each target sign is ±1 and the axes agree slotwise. Its sign product is +1. Thus the correction belongs to the four-element even-flip subgroup of (C2)^3, and introduces no new spatial axes.

**Theorem 2 (sharp triviality):** g(p)=(+1,+1,+1) iff s0=s1=s2. Exactly 240 frames have trivial correction, and 720 require nontrivial correction. This recovers R752's sharp stratum.

**Theorem 3 (three-step cocycle closure):** Let U(p)=g(p)·C^2(p). By construction U acts as axis-cycle-by-two while leaving the sign tuple in its original slots. Hence U^3=identity for all 960 frames. The ordered three gauge factors, transported through their successive C^2 slot changes, multiply to the identity in the appropriate compositional action. This is an exact three-step twisted holonomy statement, not a claim that every individual gauge factor is identity.

**Provenance boundary:** g(p) changes the signed-Port identity of the target when nontrivial. Therefore the equation is a gauge-corrected comparison between two typed models, not a source-preserving native R748 event, and not an authorization to erase signed source/branch identity. A lawful native interpretation would need a declared signed-frame gauge equivalence or a typed source-transfer morphism with BRC provenance.

Finite verification: R753_TWISTED_SIGN_GAUGE_VERIFY.py checks all 960 frames, gauge uniqueness by direct construction, even parity, identity gauge count 240, nontrivial count 720, and U^3 identity. Exact expected JSON:
{"status":"PASS","frames":960,"even_gauge_products":960,"identity_gauge":240,"nontrivial_gauge":720,"three_step_return":960,"native_event_permission":false}.

Next: compare the exact sign-gauge transport against V5 four-twist signed generator gauge covariance and any declared Link/Port source transport, without mistaking gauge change for a physical event. No mathematical impossibility claim is made about further native couplings.
