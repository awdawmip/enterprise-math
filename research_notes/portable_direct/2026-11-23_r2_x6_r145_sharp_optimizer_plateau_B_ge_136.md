# X6 R145 — sharp upper extent of the constant Port-10 BRC optimizer for every B >= 136

Date: 2026-11-23 (Asia/Shanghai). Status: **author exact finite integer certificate and analytic boundary proof PASS; independent mathematical review pending**.

## Fixed input, model, and provenance

Continue the R144 exact upper near-direction fan without changing P000 V5, the ACTIVE Heartbeat X6 basis, or the frozen R121/R122 scientific pins:
- `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.
- Immediate R144 source: `awdawmip/enterprise-math@56c49db776c79e57b345ffdbdeb7d8d7b1284907:research_notes/portable_direct/2026-11-23_r2_x6_r144_unbounded_B_two_entry_fan.md`.

This is the same declared centered-three-axis conditional BRC observer within X6, using *all six* gap observations. Integer Port is 10, directions a=(x,y,z) and -a alone are identified (all nonzero positive multiples remain distinct). Exactly 1,935 unoriented integer vectors meet q(a)=max(sum positive, sum absolute negative)<=10. Heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), gaps g_ij=|h_i-h_j| ordered by i<j; capacity vector is s=(136+B,312,136+D,B+176,B+D,176+D). Put F(a;B,D)=max_j(g_j/s_j) and eta(B,D)=min_a F(a;B,D).

## Theorem — exact sharp optimizer plateau boundary

For every real B>=136 and every real D>=528, put

```
Dopt(B) = max(1008,1248-B)
        = 1248-B for 136<=B<=240,
          1008   for B>=240.
```

Then the complete exact optimizer value satisfies

```
eta(B,D) = 1/104    if and only if    528<=D<=Dopt(B).
```

For every D>Dopt(B), one has strictly eta(B,D)<1/104. In particular, the finite upper boundary of the constant-optimum chamber is a **sharp continuous broken line** with a corner at (B,D)=(240,1008). The new theorem extends R144's previously proved rectangle 528<=D<=1008 by a nonrectangular wedge 136<=B<240, 1008<D<=1248-B; it makes no assertion about the full optimizer formula or strict-near set after crossing that boundary.

## Exact proof

Write b=(4,-1,0), and a0=(9,-5,1). The B-independent pair channels are j=1,2,5 with capacities s_1=312, s_2=136+D, s_5=176+D. Direct integer enumeration of the **1,934 directions a other than b** gives, for each a, at least one j in {1,2,5} satisfying

```
104*g_j(a) >= s_j(B,1112).
```

The selected fixed-pair certificate uses j=1 for exactly **1,920** directions and j=2 for exactly **14** directions; no other selection is necessary. Because D<=Dopt(B)<=1112 whenever 136<=B<=240, this establishes F(a)>=1/104 for all a!=b in that region. For B>=240 and D<=1008, the same certificate also applies, as D<=1112.

The two remaining cases for b are exhausted by its exact gaps `g(b)=(1,0,11,1,12,11)`. If D<=1008, the j=2 ratio is 11/(136+D)>=1/104. When 136<=B<=240 and 1008<D<=1248-B, the j=4 ratio is 12/(B+D)>=1/104. Consequently **every** Port-10 direction has score >=1/104 on the stated plateau.

Conversely, at the base corner (B,D)=(136,528), the previously certified exact witness a0 has F(a0)=1/104, and its B-independent j=1 gap ratio is exactly 3/312=1/104. Increasing B or D cannot increase any channel score; hence F(a0)=1/104 for every B>=136,D>=528. Combining the matching bounds proves eta=1/104 on the entire stated region.

For strict sharpness, consider D>max(1008,1248-B). The b direction then has each of its six ratios **strictly less** than 1/104: j=2 because D>1008, j=4 because B+D>1248, j=5 because D>968, j=0 and j=3 because B>=136, and j=1 is zero. Therefore F(b)<1/104 and so eta<=F(b)<1/104. This proves the if-and-only-if theorem including all equality boundary points.

## Reproducibility, status, and next question

The companion standalone verifier `research_notes/portable_direct/x6_r145_sharp_optimizer_plateau_verify.py` enumerates all 1,935 original Port-10 directions using integer arithmetic, checks all 1,934 fixed-pair lower certificates exactly, checks the explicit witness and b gaps, and performs 54 complete-population rational crosschecks around the critical wall, including B=136, 240, and unbounded-B samples. Executed locally using Python `fractions.Fraction` with output:

```
R145 SHARP OPTIMIZER PLATEAU EXACT CERTIFICATE PASS
population 1935 B-independent_lower_certificates_excluding_b 1934 pair_counts {1: 1920, 2: 14}
sharp_plateau_boundary max(1008,1248-B) for B>=136, D>=528 witness (9, -5, 1) exit_direction (4, -1, 0)
full_fraction_cross_checks 54
```

Local verifier SHA-256: `365de1f68f750d00ba71718dbccbde4ca724209c5e8c29cebe5f2b22d1d1e2c2`; Git blob SHA-1: `1c7f06183d5b7364c7c9cd9120bf9f3d56af412c`. No floating-point inference underlies the proof.

These results are author proofs and exact computations; formal independent mathematics review is pending. This static observer statement does not claim a physical native X6 temporal transition law.

Next: determine the exact optimizer branches and near-direction membership immediately **above** Dopt(B), distinguish b alone becoming optimal from simultaneous b/c optimizer transitions, and extend across B=20..136 to connect the R143 boundary to R144 and R145.
