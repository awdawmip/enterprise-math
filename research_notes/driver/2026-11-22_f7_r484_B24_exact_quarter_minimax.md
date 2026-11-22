# CBRC F7 r484 — exact B24 minimax by a new static quarter-grid witness

Date: 2026-11-22 (Asia/Taipei). A bounded mathematical result of the existing RESEARCH_DRIVER logical research lane EM-DVR-DEBB5E. Original researcher EM-CBRCF7-83A1D4, frozen RR-AA38973D56330E59D315, Task/ownership and review history are unchanged.

## Theorem

Let the globally defined admissible functions q: Z² -> R satisfy q(-x,y)=q(x,y); q(0,0)=0; q(x,0)=1 for x≠0; q(x,y)≥1/2 for y≠0; q(2,1)=q(-1,-1)=1/2. Let

    k=a-2b-c+2d,
    D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
    e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|.

**r484: e_B=1/2 for every integer 1≤B≤24.**

## Exact lower bound

For any B≥1, input (a,b,c,d)=(1,-1,0,0) has k=3. Evenness and the marked value give q(1,-1)=q(-1,-1)=1/2, while q(4,2),q(-3,-3)≥1/2 and q(0,0)=0. Hence D_q(1,-1,0,0)≥1/2.

## Fixed upper-bound witness

Write Q=4q. Set Q(0,0)=0; Q(x,0)=4 for x≠0; the evenness-closed fixed marks Q(±2,1)=Q(±1,-1)=2. At all other off-axis coordinates use a deterministic finite lookup of 11,998 keys (|x|,y) on the B24 fiber index below, with baseline Q=2 outside it.

Index reconstruction: for each r=-48,...,48 define the integer interval T_r=[2r-min(24,r+24), 2r-max(-24,r-24)]. In increasing r, then increasing u>r, then concatenate increasing v∈T_r followed by increasing v∈T_u, and for each v visit rr=r followed by rr=u. Insert the first occurrence of (|2rr-v|,rr-v) when its second coordinate is nonzero and it is not a fixed-mark key. The complete index contains exactly 11,998 keys.

Assign Q values from the corresponding positions of the raw 11,998-byte array in:

    research_artifacts/F7_R484_B24_Exact_Quarter_Witness_20261122.b85

It is Base85(zlib(raw)) and its **raw** SHA256 is:

    313a72810ad89d4b2fee358b0ff015127cc7b8d1e95cbd78b4b671df9f6e0c94

Raw Q frequencies: 2 appears 7,985 times; 3 appears 3,149 times; 4 appears 864 times. Thus all off-axis values satisfy Q≥2; the prescribed axis, origin, evenness and fixed marks are built into the definition.

The separately executed Python standard-library checker

    research_checks/CBRC_F7_R484_B24_EXACT_QUARTER_CERT_20261122.py

rebuilds the index, checks SHA256 and frequencies, and independently enumerates **49⁴=5,764,801** original input quadruples. All quantities are exact integers. Its complete output histogram of 4D_q:

| 4D_q | Exact count |
| ---: | ---: |
| -2 | 142,384 |
| -1 | 1,282,608 |
| 0 | 2,811,473 |
| +1 | 1,367,126 |
| +2 | 161,210 |

The maximum |4D_q| is 2, with 303,594 tight input quadruples. Therefore E_24(q)=1/2. The original fixed-mark lower bound proves e_24=1/2 and the same global witness restricts to all B≤24.

## Construction provenance and precise scope

Starting from the immutable r483 B23 quarter-valued certificate, extend it to B24 using Q=2 for new keys. This initial extension has 10,048 violating B24 original-input tuples with max |4D|=4. A numerical sparse cutting-plane/L1 search returned the present integer quarter-valued candidate. Relative to r483, exactly **641 existing B23 keys change by one quarter-unit in Q** (623 increases by +1 Q unit, 18 decreases by -1 Q unit); all **972** newly indexed B24 keys retain Q=2. This is a construction description, **not** a minimum-repair claim. LP status is not used as theorem evidence.

The immutable static witness plus the independently run exact exhaustive Python verifier establish the stated finite-box theorem. The infinite-domain minimax remains open with the established 1/2≤e_infinity≤4/7; the next finite frontier is B25 exact feasibility or a rigorous obstruction.

Scientific unit r484: PROVED_BOUNDED. No new Native Review, Result admission, formal Task completion or mother-objective closure is claimed; no other researcher ownership, Source provenance, contribution identity or schedule was changed.

Prior exact B23 proof: https://github.com/awdawmip/enterprise-math/blob/5c9287fe8760d0b1149a3b4b7f52984956d92693/research_notes/driver/2026-11-22_f7_r483_B23_exact_quarter_minimax.md
