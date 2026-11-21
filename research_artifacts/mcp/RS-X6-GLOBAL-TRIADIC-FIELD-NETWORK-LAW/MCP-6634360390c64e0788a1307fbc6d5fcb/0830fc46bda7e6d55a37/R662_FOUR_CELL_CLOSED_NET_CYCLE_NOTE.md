# R662: four-Cell closed net-cycle retains non-Abelian centre-slot memory

Date 2026-11-21. Formal task RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW, publication TP2-47D65B35A7D48082EFBB. Researcher EM-X6-C7A253, earlier R661 author EM-X6-28626F retained. NOT_REVIEWED.

## Conditional model and exact result
Use the unchanged frozen R661 endpoint-local signed V27/V29/V17 transducer. Take four native X6 unit-square Cells c0=(0,0,0,0,0,0), c1=(1,0,0,0,0,0), c2=(1,1,0,0,0,0), c3=(0,1,0,0,0,0). Internal 4-edge PASS counts per Cell: (3,3,3,3),(2,0,1,1),(3,3,3,3),(3,3,3,3). Initial active triad 012, labelled slots (0,1,2), zero Rin/Rout.

Assume permission H contains six exact events e=(0,0,1,2),f=(1,0,2,0),g=(1,1,2,0),p=(2,0,3,0),q=(3,0,0,0),r=(2,0,1,0), using (src Cell,src port,dst Cell,dst port). Compare serial words A=e,f,g,p,q,r and B=f,e,g,p,q,r.

The attached checker copies R661's pinned signed integer helper definitions unchanged and asserts:
(1) All six transfers in both words give unique strict V27 local winners;
(2) Network Q=0 at every prefix, and both final full nonnegative Rin/Rout, event-port multiplicities and triads coincide;
(3) final triads are ((1,2,4),(1,3,4),(0,2,4),(1,2,4));
(4) full slots A=((0,2,1),(0,2,1),(1,0,2),(0,2,1)); B=((0,2,1),(1,0,2),(1,0,2),(0,2,1)). Per-Cell slot parity agrees, but the c1 relative S3/D3 is the order-three element (1,2,0);
(5) the four oriented square-edge net currents j01,j12,j23,j30 equal (1,1,1,1) with zero incidence boundary; raw 1→2 events occur twice and reverse 2→1 once.

This extends R661's open 3-Cell chain to a closed four-Cell **net current** cycle and shows the stated count, final triad and parity summaries do not determine future full slot-frame observations. It is a conditional exact finite witness, not the native global update law. The V39 (j,h) based-loop quotient is not refuted: its based-loop h has not been derived from this raw event trace. Native H, autonomous scheduler, that h map and rotation covariance remain open; no physical/Foundation or independent Review claim.

Pinned source: R661_PROOF.zh-CN.md and R661_VERIFY.py at enterprise-math@697ae262c71abea056fee9584c1df3ecc8489d21; V39/V40 research notes at enterprise-math@b28632d19006cb77b503fecbb1a487acc8de3f28. Checker writes R662_FOUR_CELL_CLOSED_NET_CYCLE_EVIDENCE.json and emits R662_FOUR_CELL_CLOSED_NET_CYCLE_D3_MEMORY_EXACT_PASS.
