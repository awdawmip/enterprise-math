# R58 exact computation evidence — 2026-11-11

Frozen auxiliary S23/AV pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
R57 predecessor proof: 710a2d1d4dd9689e163543b6663b10ce4bc6164f.
Author method: CHECK_R58.py, Python exact integer rational operations; no floating point and no claim of native BRC/heartbeat physical simulation.

Run: python CHECK_R58.py (writes CERTIFICATE.json alongside the script).
Small cases: 1,440 for m=1..12, H=1..15, 8 seeded p/1009 per pair; 8,640 nonchronological/duplicate checkpoint queries, 74,880 exact original-label micro-event replays, 38,880 difference-array endpoint updates. Every queried entire owner vector and youngest-age vector equals an independent rational-phase/bisect oracle.

Pinned S23 endpoints: p=262204504569236716045286 or p+1, D=10^24, m=128,H=225,K=352, Farey denominator pair (164,225). Each parameter endpoint: 17 nonchronological/duplicate checkpoints, 3,825 owner entries and 2,176 youngest-age entries, 704 difference updates versus 28,800 complete-tour original-labelled source moves. Both full endpoint owner arrays and youngest vectors are identical at ranks 0 and 352, with nontrivial 28,800-step event path preserved. Exact rephasing checked at physical j=-10^18, j=10^12+128 and j=10^18 for all 225 source ages and checkpoint ranks k=0,176,352 on both parameter ends.

Finite-domain theorem tests require q/gcd(p,q)>m+H-1 to prevent rational ties in the specified cut set. The universal statements rely on PROOF.md's argument; the finite checker is evidence for its implementation, not mathematical project admission.

Deletion witness: latest({1,2})=latest({2})=2 but deleting 2 yields 1 and EMPTY. The fixed deletion-budget top-(d+1) theorem is proved in PROOF.md. Native Researcher-ID/Research-Activity-ID are recorded separately by the real service; Source write and shared owner/CLAIM have independent receipts.
