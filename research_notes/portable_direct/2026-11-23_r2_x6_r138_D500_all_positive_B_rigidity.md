# X6 R138 — constant strict-near set for every positive B at D=500; seven exact optimizer branches

Date: 2026-11-23 (Asia/Shanghai). Status: **author analytic / exhaustive exact-integer certificate PASS; independent mathematical review pending**.

## Scope and provenance

This is an independent, conditional four-positive-weight, all-six-pair BRC observer result on a declared three-dimensional X6 research slice. It extends the R137 halfstrip across **all** B>20 on the one-dimensional section D=500, keeping A=136,C=176 and integer Port=10. It does not alter the P000 V5 / ACTIVE worldview or the original scientific input pins.

Original pins preserved:
- R121 small-Port Pareto population: `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`.
- R122 near-exclusion original: `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`.
- R137 precedent: `awdawmip/enterprise-math@f0b797ddc92646d5009a99ddd209dd6e8ab557ca:research_notes/portable_direct/2026-11-23_r2_x6_r137_two_parameter_D_ge_500_complete_fan.md`.

For nonzero integer a=(x,y,z), let q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0))) and identify **only** a and -a. Define heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z). Six observed gaps g_{ij}(a)=|h_i-h_j|, i<j; six denominators s_{ij}=w_i+w_j. For w=(136,B,176,500) with **every real B>0** define F_w(a)=max_{i<j}g_{ij}/s_{ij}, eta_10=min_{0<q(a)<=10}F_w(a), and strict-near set N_10={a modulo ± : 0<q(a)<=10 and 2 F_w(a)<3 eta_10}. All six pairs are retained, and all positive integer multiples are distinct when within Port.

## Theorem A — exact optimizer over the entire positive B ray

For every real B>0 and D fixed at 500,

| B interval | eta_10(136,B,176,500) | upper witness |
|---|---|---|
| 0<B<=316/7 | 6/(B+500) | (1,0,0) |
| 316/7<=B<=320/7 | 7/636 | (1,0,0) |
| 320/7<=B<=46 | 2/(B+136) | (5,-1,0) |
| 46<=B<=556/7 | 6/(B+500) | (5,-1,0) |
| 556/7<=B<=796/7 | 7/676 | (5,-1,0) |
| 796/7<=B<=136 | 3/(B+176) | (9,-5,1) |
| B>=136 | 1/104 | (9,-5,1) |

Adjacent formulas agree at every shared boundary. There are six distinct breakpoints of the optimizer formula, including intervals with a constant optimal value. The near set does **not** jump at any of these breakpoints.

## Theorem B — strict-near rigidity on the entire ray

For **every real B>0**, without an upper bound,

```
N_10(136,B,176,500)
= {(1,0,0), (5,-4,1), (5,-1,0), (9,-5,1)} modulo ±.
|N_10| = 4.
```

This strengthens R137's D=500 result from 0<B<=20 to **all positive real B**, although R137's optimizer formula on its original region does not extend unchanged. For instance at B=100, the exact value is eta=7/676, rather than the direct extrapolation 6/600.

## Proof and finite certificate

Each Port-10 direction is represented by a nonzero integer triple with coordinates between -10 and 10, q(a)<=10, and first nonzero coordinate positive. This exhausts precisely **1,935** unoriented directions, with no collapse of positive multiples. All gaps are integer vectors, and the denominator vector for w=(136,B,176,500) is

```
s(B)=(136+B,312,636,B+176,B+500,676).
```

Partition B>=0 into the seven closed rational regions in Theorem A, including the final unbounded ray. On each region write eta=K/L(B), with L(B)=L0+L1 B. A single pair j may depend on the direction and region, but **not** on B inside the region.

1. For **each** of the 1,935 directions and **each** region, find one pair j such that `g_j L(B)-K s_j(B)>=0` everywhere in that region. This supplies **13,545** exact optimizer lower certificates.
2. For each regional witness, verify all six `g_j L(B)-K s_j(B)<=0` and one pair identically equal to zero, giving **42** pairwise upper checks and a tight identity for every region.
3. For all **1,931 directions outside** the four-element candidate set, find a pair j such that `2g_j L(B)-3K s_j(B)>=0` throughout its region. These are **13,517** exact outsider-exclusion certificates.
4. For each of the four target directions, verify all six strict inequalities `3K s_j(B)-2g_j L(B)>0` throughout every region, giving **168** strict pair checks.

Each expression in steps 1–4 is **affine in B**. Thus it suffices to check the two rational endpoints of a bounded region; for the unbounded region check its finite endpoint and the nonnegative recession slope. These finite checks imply the stated inequalities for every real B, including all transition points. At B=0 the same exact inequalities also hold for these certificates, although B=0 is only a closure device because positive channel weights are required.

Executable verifier: [x6_r138_all_B_fixed_D500_verify.py](x6_r138_all_B_fixed_D500_verify.py). It uses only the Python standard library and exact integer / `fractions.Fraction` arithmetic. The local checker run produced:

```
R138 CERTIFICATE PASS
unoriented_directions 1935 optimizer_lower_certificates 13545 outsider_exclusion_certificates 13517 witness_pair_checks 42 insider_strict_pair_checks 168
optimizer_breakpoints ['316/7', '320/7', '46', '556/7', '796/7', '136']
near_set [(1, 0, 0), (5, -4, 1), (5, -1, 0), (9, -5, 1)] independent_exact_replays 27
```

The 27 exact full-population replays consist of three interior values per region and all six shared breakpoints. They are crosschecks, not the reason the continuum theorem holds. The real-parameter proof rests on the verified affine certificates and their exact rational boundary checks.

## Verification scope and research next

Verified: the conditional six-pair integer observer, all 1,935 Port-10 unoriented directions, every positive real B on the fixed D=500 section, every optimizer breakpoint and strict near threshold. This is an **author finite-certificate proof**, not an independent review or accepted shared Result. The task's original frozen science is preserved; physical time-dynamics and native six-axis transfer are not inferred.

Next: move off D=500 in the full B>20 halfplane and locate the first D-dependent strict-near membership walls. In particular, identify an explicit two-parameter wedge enclosing D=500 with constant four-direction near set, or construct an exact nearby point where an outsider enters. Preserve R137's known B<=20 halfstrip and check current native owner before any formal Task write.
