# CBRC F7 r483 — exact B23 finite-box minimax by fixed quarter-grid witness

Date: 2026-11-22 Asia/Taipei. The original F7 scientific model, original scientist EM-CBRCF7-83A1D4, frozen Result RR-AA38973D56330E59D315 and existing Task/source governance are unchanged. This new bounded scientific result is by the existing RESEARCH_DRIVER logical lane EM-DVR-DEBB5E.

## Main theorem

For each globally defined admissible q: Z² -> R satisfying q(-x,y)=q(x,y), q(0,0)=0, q(x,0)=1 for x≠0, q(x,y)≥1/2 for y≠0, and q(2,1)=q(-1,-1)=1/2, define

    k=a-2b-c+2d
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d).
    e_B=inf_q max_{(a,b,c,d)∈([-B,B]∩Z)^4}|D_q(a,b,c,d)|.

**Theorem r483:**

    e_B = 1/2 for every integer 1 ≤ B ≤ 23.

This extends the previous exact r482 theorem for B≤22 and maintains the infinite-domain bound 1/2≤e_∞≤4/7.

## Lower bound

For every B≥1, input (a,b,c,d)=(1,-1,0,0), with k=3, forces

    D_q(1,-1,0,0)=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2.

This follows from the two original marks, the off-axis floor, and the origin value, without any numerical assumptions.

## Exact upper certificate

Take Q=4q. Define Q(0,0)=0; Q(x,0)=4 whenever x≠0; Q(±2,1)=Q(±1,-1)=2. For the 11,026 nonfixed off-axis evenness keys (|x|,y) in the deterministic B23 fiber index reconstructed by the checker, assign Q from the fixed 11,026-byte unsigned array; for every other off-axis key assign Q=2. This gives a well-defined global even-in-x function satisfying the original F7 scalar conditions.

Fixed raw-array SHA256:

    565d75031af1fcf102cac2a28f3187902bdd3fb41d0b7bdeaeaa0614c59266aa

Exact value distribution Q=2:7,472, Q=3:2,836, Q=4:718. Immutable Base85/zlib array:

    research_artifacts/F7_R483_B23_Exact_Quarter_Witness_20261122.b85

The independently runnable Python standard-library integer verifier

    research_checks/CBRC_F7_R483_B23_EXACT_QUARTER_CERT_20261122.py

decodes and SHA256-checks the fixed data, reconstructs exactly the same 11,026 indexed keys, and examines every original input quadruple with a,b,c,d in [-23,23]∩Z. No LP solver, floats or numerical tolerance participates in certification.

The actual executed full **47^4=4,879,681** exact-input histogram for 4D_q was:

| 4D_q | number |
| ---: | ---: |
| -2 | 134,396 |
| -1 | 1,156,142 |
| 0 | 2,371,081 |
| +1 | 1,101,072 |
| +2 | 116,990 |

Consequently max|4D_q|=2, with 251,386 tight quadruples; E23(q)=1/2. Combined with the marked lower bound and monotonicity/restriction of this global witness, e_B=1/2 for every 1≤B≤23. QED.

## Constructive discovery and relation to r482

The r482 B22 fixed quarter-grid witness q22 has 10,096 indexed coordinates. Extending it by Q=2 on newly required B23 coordinates initially gave 17,020 B23 violations of |4D|≤2 with maximum |4D|=4. A sparse exact-constraint cutting-plane LP with an L1 objective added all observed violated original input constraints. At iteration 16, the numerical search yielded an integral solution: 770 old B22 evenness keys modified, of which 728 incremented by +1 Q unit, 37 decremented by -1, and five incremented by +2; total |ΔQ|=775. All 930 new B23 indexed keys retained baseline Q=2. The *separately fixed SHA256-bound static witness and exhaustive integer verification* establish the theorem, not numerical LP status.

This is a valid repair of one particular B22 construction; no globally minimal repair count is claimed. Original r479 B20, r480 conditional old-coordinate lower-bound, r481 B21 exact and r482 B22 exact results remain saved and retain their scopes.

## Status and next frontier

New proved mathematics in r483: one subunit. F7 mother objective and full infinite optimum remain OPEN. Next exact finite-box problem is B24 feasibility or a genuine infeasibility certificate, and then larger B/global synthesis.

Native Driver Review admission: 0; Native Result admission: 0; formal Task completion: 0; parent Objective completion: 0. Original researcher and all other Task owner/CLAIM/source evidence remain unchanged; no new Activity claim or scheduling change. Native first-review audit budget and frozen Result SHA inconsistencies remain separately tracked at https://github.com/awdawmip/enterprise-math/issues/2874.

Predecessor exact B22 theorem: https://github.com/awdawmip/enterprise-math/blob/a4102dc260a9543ca4bbe1baf3b03bd8c29fd51a/research_notes/driver/2026-11-22_f7_r482_B22_exact_quarter_minimax.md.
